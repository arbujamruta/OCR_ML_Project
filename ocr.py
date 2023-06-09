

DATA_DIR = 'data/'
TEST_DATA_FILENAME= 't10k-images.idx3-ubyte'
TEST_LABELS_FILENAME= 't10k-labels.idx1-ubyte'
TRAIN_DATA_FILENAME = 'train-images.idx3-ubyte'
TRAIN_LABELS_FILENAME= 'train-labels.idx1-ubyte' 

def bytes_to_int(byte_data):
    return int.from_bytes(byte_data, 'big')

def read_images(filename, n_max_images= None ):
    images =[]
    with open(filename, 'rb') as f:
        _ = f.read(4) #magic number
        n_images= bytes_to_int(f.read(4))
        if n_max_images:
            n_images = n_max_images
                
        n_rows = bytes_to_int(f.read(4))
        n_columns = bytes_to_int(f.read(4))
        for image_idx in range(n_images):
            image=[]
            for row_idx in range(n_rows):
                row=[]
                for col_idx in range(n_columns):
                    pixel = f.read(1)
                    row.append(pixel)
                image.append(row)
            images.append(image)        
    return images

def read_labels(filename, n_max_labels= None ):
    labels =[]
    with open(filename, 'rb') as f:
        _ =f.read(4) #magic number
        n_labels= bytes_to_int(f.read(4))
        if n_max_labels:
            n_labels = n_max_labels
        for label_idx in range(n_labels):
            label= f.read(1)
            labels.append(label)        
    return labels

def flatten_list(l):
    return[pixel for sublist in l for pixel in sublist]

def extract_features_from_sample(X):
    return [flatten_list for sample in X]


def extract_features(X):
    return[flatten_list(sample) for sample in X]

def dist(x,y):
    return sum(
        [(x_i - y_i)** 2 for x_i, y_i in zip(x,y)]
    )** (0.5)

def get_training_distances_for_test_sample(X_train, test_sample):
    return [dist(train_sample, test_sample) for train_sample in X_train]


def knn(X_train, y_train, X_test, k=3):
    y_pred =[]
    for test_sample in X_test:
        training_distances = get_training_distances_for_test_sample(X_train, test_sample )
        sorted_distances_indices = [
            pair[0]

            for pair in sorted(
                enumerate(training_distances, key=lambda x: x[1])
                )       
        ]
        print(sorted_distances_indices)
        y_sample=5
        y_pred.append(y_sample)
    return y_pred      


def main():
    X_train = read_images(TRAIN_DATA_FILENAME,100)
    y_train = read_labels(TRAIN_LABELS_FILENAME)
    X_test = read_images(TEST_DATA_FILENAME,100)
    y_test = read_labels(TEST_LABELS_FILENAME)
    print(len(X_train))
    print(len(y_train))
    print(len(X_test))
    print(len(y_test))
    
    
    print(len(X_train[0]))
    print(len(X_test[0]))

    X_train = extract_features(X_train)
    X_test = extract_features(X_test)
    
    print(len(X_train[0]))
    print(len(X_test[0]))

    knn(X_train, y_train, X_test, 3)

main() 
    

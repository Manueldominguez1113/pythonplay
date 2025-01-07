import csv

def get_questions(filename):
    print("Reading questions from " + filename)
    try:
        with open(filename,'r') as csvfile:
            reader = csv.reader(csvfile)
            questions = list(reader)

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(e)

    return questions

if __name__ == '__main__':
    get_questions("quiz.csv")
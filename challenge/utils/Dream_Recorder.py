# A dream recorder to record life in dream.
import cPickle
from datetime import date


class DreamRecorder(object):
    dream_of = {}
    store_file = 'dream_recorder.dat'

    def __init__(self):
        self.load_data()

    def add(self, person_list):
        for person in person_list:
            self.add_person(person)

    def save_checkpoint(self):
        file_opener = open(self.store_file, 'wb')
        cPickle.dump(self.dream_of, file_opener)
        file_opener.close()

    def add_person(self, person, dream_date=str(date.today()), save_to_file=False):
        if person not in self.dream_of.keys():
            self.dream_of[person] = [dream_date]
        else:
            self.dream_of[person].append(dream_date)
        if save_to_file:
            self.save_checkpoint()

    def load_data(self):
        try:
            file_opener = open(self.store_file, 'rb')
            self.dream_of = cPickle.load(file_opener)
            file_opener.close()
        except IOError:
            print "First use the dream recorder, no store file!"

    def print_person(self, person):
        if len(self.dream_of.keys()) == 0:
            self.load_data()
        if person in self.dream_of.keys():
            print "I have dream of %s %d times!" % (person, len(self.dream_of[person]))
            print "In date: %s" % str(self.dream_of[person])
        else:
            print "I have never dream of %s yet!" % person

    def print_all(self):
        for person in self.dream_of.keys():
            self.print_person(person)


if __name__ == '__main__':
    dream_recorder = DreamRecorder()
    # dream_recorder.add(['zhangheng'])
    dream_recorder.print_all()

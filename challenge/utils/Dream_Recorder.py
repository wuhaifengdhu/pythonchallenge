# A dream recorder to record life in dream.
import cPickle


class DreamRecorder(object):
    dream_of = {}
    store_file = 'dream_recorder.dat'

    def __init__(self):
        self.load_data()

    def add(self, person_list):
        file_opener = open(self.store_file, 'wb')
        for person in person_list:
            if person not in self.dream_of.keys():
                self.dream_of[person] = 1
            else:
                self.dream_of[person] += 1
            if person == 'zhangheng':
                print "Dream_Of[%s] += 1" % person
        cPickle.dump(self.dream_of, file_opener)
        file_opener.close()

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
            print "I have dream of %s %d times!" % (person, self.dream_of[person])
        else:
            print "I have never dream of %s yet!" % person


if __name__ == '__main__':
    dream_recorder = DreamRecorder()
    dream_recorder.add(['zhangheng'])
    # dream_recorder.print_person('zhangheng')
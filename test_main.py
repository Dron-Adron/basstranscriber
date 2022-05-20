import os
from pydub import AudioSegment


from scripts.main import process

def test_process1():

    test_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'test')
    for fname in os.listdir(test_path):
        if not fname.endswith('.wav'):
            continue
        note_fname = fname[:-4] + '.txt'
        print(fname, note_fname)

        song = AudioSegment.from_file(os.path.join(test_path, fname))
        notes_pred = process(song, 100, -50)

        with open(os.path.join(test_path, note_fname)) as f:
            notes_gt = f.read().strip().split()

        assert len(notes_pred) == len(notes_gt)

        errors = 0
        for n_pr, n_gt in zip(notes_pred, notes_gt):
            if (n_pr != n_gt):
                errors += 1
        assert errors <= 1

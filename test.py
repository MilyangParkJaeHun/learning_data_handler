import bar.progressbar as pb
import time

total = 20000
progressbar = pb.Progressbar(total, 'Progress:', 'Complete', 3, 50, 0.1)
for i in range(total):
  progressbar.progress()
  time.sleep(0.001)

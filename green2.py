# _*_ coding: utf-8 _*_

import datetime
import os
import random
from random import choice

comments = [
    'Update ReactFiberScheduler',
    'Update CHANGELOG for 16.7',
    'v16.7.0',
    'Move SchedulerFeatureFlags fork to src directory to fix lint',
    'Make scheduler debugging feature flag static',
    'Create separate SchedulerFeatureFlags instead of using ReactFeatureFl…',
    'Memoize promise listeners to prevent exponential growth',
    'Removed Fabric-specific feature flag files and updated Rollup to use',
    'Updated version incrementing suggestion in release script based on te…',
    'Implement pauseExecution, continueExecution, dumpQueue for Scheduler',
    'Added ErrorBoundary tests for useEffect and useLayoutEffect',
    'Enable hooks in fabric',
    'Tweaked wording for v8 "performance cliff" issue',
    'Automated fixture tests',
    'Removed unnecessary externals from Jest bundles',
    'Fixed scheduler setTimeout fallback',
    'Fix bug in cloneHook',
    '[Fire] Add initial build infrastructure',
    'Adding isMemo check to react-is package',
    'Remove useMutationEffect',
    'Add a null type test for memo',
    'Minified Deep Learn  ',
    'Deep net learn',
    'update credits',
    'update url',
    'Update rnnrbm.py',
    'Update segmentation tutorials and .gitignore.',
    'Preload data for 1D cortical dataset',
    'Results for unet',
    'added per class jaccard',
    'Formatting',
    'Remove files that are not used any more',
    'More small fixes',
    'data augmentation fixed',
    'remove loading pretrained weights',
    'index updated with new links',
    'removed files .pyc',
    'small change',
    'import conv2DDDNlayer',
    'fix input dim and details',
    'fix dataset loader for em, name for polyps',
    'adde training loop link',
    'small changes',
    'relative paths',
    'with BN',
    'update from pascal comment',
    'polyps results image',
    'acknowledgements',
    'added code',
    'first commit for fcn1D segmentations',
    'deleted files',
    'figure 4 description',
    'explanation ground truth vs predicted segmentation',
    'FCN description fixed',
    'cortical layers imagse'
]

def modify():
    file = open('zero.md', 'r')
    flag = file.readline() == '0'
    file.close()
    file = open('zero.md', 'w+')
    if flag:
        file.write('1')
    else:
        file.write('0')
        file.close()


def commit():
    cm = 'git commit -a -m "' + choice(comments) + '"'
    print(cm)
    os.system(cm)


def set_sys_time(day, month, year):
    os.system('date %02d%02d1720%04d' % (month, day, year))


def trick_commit(year, month, day):
    set_sys_time(year, month, day)
    modify()
    commit()


def daily_commit(start_date, end_date):
    count = 0
    while (count < 2):
        for i in range((end_date - start_date).days - 5):
            if (i%random.randint(1,2)):
                cur_date = start_date + datetime.timedelta(days=(i+random.randint(1,5)))
                trick_commit(cur_date.day, cur_date.month, cur_date.year)
        count = count + 1


if __name__ == '__main__':
    daily_commit(datetime.date(2015, 2, 21), datetime.date(2018, 12, 19))
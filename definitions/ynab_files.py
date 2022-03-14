
class budget_metadata:
    filename = 'Budget.ymeta'
    fields = [
        'formatVersion',
        'relativeDataFolderName',
        'TED'
    ]


class device:
    file_extension = '.ydevice'

    fields = [
        'friendlyName',
        'knowledgeInFullBudgetFile',
        'YNABVersion',
        'lastDataVersionFullyKnown',
        'deviceType',
        'knowledge',
        'highestDataVersionImported',
        'shortDeviceId',
        'formatVersion',
        'hasFullKnowledge',
        'deviceGUID'
    ]


class budget:
    filename = 'Budget.yfull'

    fields = [
        'masterCategories',
        'payees',
        'monthlyBudgets',
        'fileMetaData',
        'transactions',
        'scheduledTransactions',
        'accountMappings',
        'budgetMetaData',
        'accounts'
    ]


class diffs:
    file_extension = '.ydiff'

    fields = [
        'shortDeviceId',
        'startVersion',
        'endVersion',
        'deviceGUID',
        'publishTime',
        'budgetDataGUID',
        'formatVersion',
        'dataVersion',
        'items'
    ]

class account:
    fields = [
        'entityId',
        'entityType',
        'entityVersion',
        'hidden',
        'accountType',
        'accountName',
        'onBudget',
        'lastReconciledBalance',
        'lastReconciledDate',
        'lastEnteredCheckNumber',
        'sortableIndex',
        'note'
    ]


class master_category:
    fields = [
        'entityId',
        'entityType',
        'entityVersion',
        'isTombstone',
        'expanded',
        'name',
        'type',
        'note',
        'deleteable',
        'subCategories',
        'sortableIndex'
    ]


class sub_category:
    fields = [
        'entityId',
        'entityType',
        'entityVersion',
        'isTombstone',
        'name',
        'type',
        'note',
        'cachedBalance',
        'masterCategoryId',
        'sortableIndex'
    ]


class payee:
    fields = [
        'entityId',
        'entityType',
        'entityVersion',
        'isTombstone',
        'autoFillCategoryId',
        'autoFillAmount',
        'name',
        'renameConditions',
        'autoFillMemo',
        'targetAccountId',
        'locations',
        'enabled'
    ]


class location:
    fields = [
        'entityId',
        'entityType',
        'entityVersion',
        'latitude',
        'longitude',
        'parentPayeeId'
    ]


class rename_payee_conditions:
    fields = [
        'entityId',
        'entityType',
        'entityVersion',
        'isTombstone',
        'operator',
        'operand',
        'parentPayeeId'
    ]


class monthly_budget:
    fields = [
        'entityId',
        'entityType',
        'entityVersion',
        'monthlySubCategoryBudgets',
        'month',
        'note'
    ]


class subcategory_budget:
    fields = [
        'entityId',
        'entityType',
        'entityVersion',
        'isTombstone',
        'categoryId',
        'budgeted',
        'overspendingHandling',
        'parentMonthlyBudgetId'
    ]


class file_metadata:
    fields = [
        'entityType',
        'budgetDataVersion',
        'currentKnowledge'
    ]


class transaction:
    fields = [
        'entityId',
        'entityType',
        'entityVersion',
        'isTombstone',
        'categoryId',
        'payeeId',
        'amount',
        'date',
        'memo',
        'accountId',
        'cleared',
        'accepted',
        'targetAccountId',
        'subTransactions',
        'transferTransactionId',
        'flag',
        'source',
        'parentTransactionIdIfMatched',
        'dateEnteredFromSchedule',
        'checkNumber',
        'importedPayee',
        'matchedTransactions',
        'YNABID',
        'FITID'
    ]


class subtransaction:
    fields = [
        'entityId',
        'entityType',
        'entityVersion',
        'isTombstone',
        'categoryId',
        'amount',
        'memo',
        'targetAccountId',
        'transferTransactionId',
        'parentTransactionId'
    ]


class budget_metadata:
    fields = [
        'entityId',
        'entityType',
        'entityVersion',
        'strictBudget',
        'currencyISOSymbol',
        'currencyLocale',
        'budgetType',
        'dateLocale'
    ]


class items:
    fields = [
        'entityId',
        'entityType',
        'entityVersion',
        'isTombstone',
        'isResolvedConflict',
        'madeWithKnowledge'
    ]


class entity_type:
    ordered_options = True

    options = [
        'masterCategory',
        'category',
        'payee',
        'location',
        'payeeStringCondition',
        'monthlyBudget',
        'monthlyCategoryBudget',
        'fileMetaData',
        'transaction',
        'subTransaction',
        'budgetMetaData',
        'account'
    ]


class account_type:
    options = [
        'Cash',
        'Checking',
        'CreditCard',
        'InvestmentAccount',
        'LineofCredit',
        'MerchantAccount',
        'Mortgage',
        'OtherAsset',
        'OtherLiability',
        'Paypal',
        'Savings'
    ]


class overspending_handling:
    options = [
        'AffectsBuffer',
        'Confined'
    ]


class category_type:
    options = [
        'INFLOW',
        'OUTFLOW'
    ]


class rename_operators:
    options = [
        'Contains',
        'EndsWith',
        'Is',
        'StartsWith'
    ]


class flags:
    options = [
        'Orange',
        'Red',
        'Purple',
        'Yellow',
        'Green',
        'Blue'
    ]


class clearance:
    options = [
        'Cleared',
        'Reconciled',
        'Uncleared'
    ]

class account:
    fields = [
        'entityId',
        'entityType',
        'entityVersion',
        'lastReconciledDate',
        'lastEnteredCheckNumber',
        'lastReconciledBalance',
        'accountType',
        'hidden',
        'sortableIndex',
        'onBudget',
        'accountName'
    ]


class master_category:
    fields = [
        'entityId',
        'entityType',
        'entityVersion',
        'expanded',
        'name',
        'type',
        'deleteable',
        'isTombstone',
        'subCategories',
        'sortableIndex'
    ]


class sub_category:
    fields = [
        'entityId',
        'entityType',
        'entityVersion',
        'name',
        'type',
        'note',
        'isTombstone',
        'cachedBalance',
        'masterCategoryId',
        'sortableIndex'
    ]


class payee:
    fields = [
        'entityId',
        'entityType',
        'entityVersion',
        'autoFillCategoryId',
        'autoFillAmount',
        'name',
        'renameConditions',
        'autoFillMemo',
        'targetAccountId',
        'locations',
        'enabled'
    ]


class monthly_budget:
    fields = [
        'entityId',
        'entityType',
        'entityVersion',
        'monthlySubCategoryBudgets',
        'month'
    ]


class subcategory_budget:
    fields = [
        'entityId',
        'entityType',
        'entityVersion',
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
        'categoryId',
        'payeeId',
        'amount',
        'date',
        'accountId',
        'cleared',
        'accepted'
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


class entity_type:
    ordered_options = True

    options = [
        'masterCategory',
        'category',
        'payee',
        'monthlyBudget',
        'monthlyCategoryBudget',
        'fileMetaData',
        'transaction',
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
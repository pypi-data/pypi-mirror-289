# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AccumulatedType',
    'ChartType',
    'CompressionModeType',
    'DataOverwriteBehaviorType',
    'DaysOfWeek',
    'DestinationType',
    'ExportType',
    'FileFormat',
    'FilterItemNames',
    'FormatType',
    'FunctionType',
    'GranularityType',
    'KpiTypeType',
    'MetricType',
    'OperatorType',
    'PivotTypeType',
    'QueryColumnType',
    'RecurrenceType',
    'ReportConfigSortingType',
    'ReportGranularityType',
    'ReportTimeframeType',
    'ReportType',
    'ScheduleFrequency',
    'ScheduledActionKind',
    'ScheduledActionStatus',
    'StatusType',
    'SystemAssignedServiceIdentityType',
    'TimeframeType',
    'WeeksOfMonth',
]


class AccumulatedType(str, Enum):
    """
    Show costs accumulated over time.
    """
    TRUE = "true"
    FALSE = "false"


class ChartType(str, Enum):
    """
    Chart type of the main view in Cost Analysis. Required.
    """
    AREA = "Area"
    LINE = "Line"
    STACKED_COLUMN = "StackedColumn"
    GROUPED_COLUMN = "GroupedColumn"
    TABLE = "Table"


class CompressionModeType(str, Enum):
    """
    Allow customers to select compress data(gzip) for exports. This setting will enable destination file compression scheme at runtime. By default set to None.
    """
    GZIP = "gzip"
    NONE = "None"


class DataOverwriteBehaviorType(str, Enum):
    """
    Allow customers to select overwrite data(OverwritePreviousReport) for exports. This setting will enable overwrite data for the same month in customer storage account. By default set to CreateNewReport.
    """
    OVERWRITE_PREVIOUS_REPORT = "OverwritePreviousReport"
    CREATE_NEW_REPORT = "CreateNewReport"


class DaysOfWeek(str, Enum):
    """
    Days of Week.
    """
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class DestinationType(str, Enum):
    """
    The export delivery destination type. Currently only 'AzureBlob' is supported.
    """
    AZURE_BLOB = "AzureBlob"


class ExportType(str, Enum):
    """
    The type of the export. Note that 'Usage' is equivalent to 'ActualCost' and is applicable to exports that do not yet provide data for charges or amortization for service reservations.
    """
    USAGE = "Usage"
    ACTUAL_COST = "ActualCost"
    AMORTIZED_COST = "AmortizedCost"
    FOCUS_COST = "FocusCost"
    PRICE_SHEET = "PriceSheet"
    RESERVATION_TRANSACTIONS = "ReservationTransactions"
    RESERVATION_RECOMMENDATIONS = "ReservationRecommendations"
    RESERVATION_DETAILS = "ReservationDetails"


class FileFormat(str, Enum):
    """
    Destination of the view data. Currently only CSV format is supported.
    """
    CSV = "Csv"


class FilterItemNames(str, Enum):
    """
    The name of the filter. This is currently only supported for Export Definition type of ReservationRecommendations. Supported names are ['ReservationScope', 'LookBackPeriod', 'ResourceType']
    """
    RESERVATION_SCOPE = "ReservationScope"
    RESOURCE_TYPE = "ResourceType"
    LOOK_BACK_PERIOD = "LookBackPeriod"


class FormatType(str, Enum):
    """
    The format of the export being delivered. Currently only 'Csv' is supported.
    """
    CSV = "Csv"


class FunctionType(str, Enum):
    """
    The name of the aggregation function to use.
    """
    SUM = "Sum"


class GranularityType(str, Enum):
    """
    The granularity of rows in the export. Currently 'Daily' is supported for most cases.
    """
    DAILY = "Daily"
    MONTHLY = "Monthly"


class KpiTypeType(str, Enum):
    """
    KPI type (Forecast, Budget).
    """
    FORECAST = "Forecast"
    BUDGET = "Budget"


class MetricType(str, Enum):
    """
    Metric to use when displaying costs.
    """
    ACTUAL_COST = "ActualCost"
    AMORTIZED_COST = "AmortizedCost"
    AHUB = "AHUB"


class OperatorType(str, Enum):
    """
    The operator to use for comparison.
    """
    IN_ = "In"
    CONTAINS = "Contains"


class PivotTypeType(str, Enum):
    """
    Data type to show in view.
    """
    DIMENSION = "Dimension"
    TAG_KEY = "TagKey"


class QueryColumnType(str, Enum):
    """
    Has type of the column to group.
    """
    TAG_KEY = "TagKey"
    """
    The tag associated with the cost data.
    """
    DIMENSION = "Dimension"
    """
    The dimension of cost data.
    """


class RecurrenceType(str, Enum):
    """
    The schedule recurrence.
    """
    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"
    ANNUALLY = "Annually"


class ReportConfigSortingType(str, Enum):
    """
    Direction of sort.
    """
    ASCENDING = "Ascending"
    DESCENDING = "Descending"


class ReportGranularityType(str, Enum):
    """
    The granularity of rows in the report.
    """
    DAILY = "Daily"
    MONTHLY = "Monthly"


class ReportTimeframeType(str, Enum):
    """
    The time frame for pulling data for the report. If custom, then a specific time period must be provided.
    """
    WEEK_TO_DATE = "WeekToDate"
    MONTH_TO_DATE = "MonthToDate"
    YEAR_TO_DATE = "YearToDate"
    CUSTOM = "Custom"


class ReportType(str, Enum):
    """
    The type of the report. Usage represents actual usage, forecast represents forecasted data and UsageAndForecast represents both usage and forecasted data. Actual usage and forecasted data can be differentiated based on dates.
    """
    USAGE = "Usage"


class ScheduleFrequency(str, Enum):
    """
    Frequency of the schedule.
    """
    DAILY = "Daily"
    """
    Cost analysis data will be emailed every day.
    """
    WEEKLY = "Weekly"
    """
    Cost analysis data will be emailed every week.
    """
    MONTHLY = "Monthly"
    """
    Cost analysis data will be emailed every month.
    """


class ScheduledActionKind(str, Enum):
    """
    Kind of the scheduled action.
    """
    EMAIL = "Email"
    """
    Cost analysis data will be emailed.
    """
    INSIGHT_ALERT = "InsightAlert"
    """
    Cost anomaly information will be emailed. Available only on subscription scope at daily frequency. If no anomaly is detected on the resource, an email won't be sent.
    """


class ScheduledActionStatus(str, Enum):
    """
    Status of the scheduled action.
    """
    DISABLED = "Disabled"
    """
    Scheduled action is saved but will not be run.
    """
    ENABLED = "Enabled"
    """
    Scheduled action is saved and will be run.
    """
    EXPIRED = "Expired"
    """
    Scheduled action is expired.
    """


class StatusType(str, Enum):
    """
    The status of the export's schedule. If 'Inactive', the export's schedule is paused. 'SystemSuspended' can only be set by export service.
    """
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    SYSTEM_SUSPENDED = "SystemSuspended"


class SystemAssignedServiceIdentityType(str, Enum):
    """
    Type of managed service identity (either system assigned, or none).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"


class TimeframeType(str, Enum):
    """
    The time frame for pulling data for the export. If custom, then a specific time period must be provided.
    """
    MONTH_TO_DATE = "MonthToDate"
    BILLING_MONTH_TO_DATE = "BillingMonthToDate"
    THE_LAST_MONTH = "TheLastMonth"
    THE_LAST_BILLING_MONTH = "TheLastBillingMonth"
    WEEK_TO_DATE = "WeekToDate"
    CUSTOM = "Custom"
    THE_CURRENT_MONTH = "TheCurrentMonth"


class WeeksOfMonth(str, Enum):
    """
    Weeks of month.
    """
    FIRST = "First"
    SECOND = "Second"
    THIRD = "Third"
    FOURTH = "Fourth"
    LAST = "Last"

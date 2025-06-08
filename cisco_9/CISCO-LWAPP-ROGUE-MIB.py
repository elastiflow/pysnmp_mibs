# SNMP MIB module (CISCO-LWAPP-ROGUE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-ROGUE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:55:05 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(cLApDot11IfType,
 cLApDot11RadioChannelNumber,
 cLApDot11RadioMACAddress,
 cLApIfSmtDot11Bssid,
 cLApName,
 cLApRogueApMacAddress,
 cLApRogueDetectedChannel,
 cLApRogueDot11RadioBand,
 cLApRogueMode) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApDot11IfType",
    "cLApDot11RadioChannelNumber",
    "cLApDot11RadioMACAddress",
    "cLApIfSmtDot11Bssid",
    "cLApName",
    "cLApRogueApMacAddress",
    "cLApRogueDetectedChannel",
    "cLApRogueDot11RadioBand",
    "cLApRogueMode")

(cldcClientMacAddress,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-MIB",
    "cldcClientMacAddress")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappRogueMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610)
)
if mibBuilder.loadTexts:
    ciscoLwappRogueMIB.setRevisions(
        ("2020-12-02 00:00",
         "2017-03-21 00:00",
         "2011-09-07 00:00",
         "2011-03-11 00:00",
         "2010-07-17 00:00",
         "2007-02-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CLAutoContainActions(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarmOnly", 1),
          ("contain", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoLwappRogueMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappRogueMIBNotifs = _CiscoLwappRogueMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 0)
)
_CiscoLwappRogueMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappRogueMIBObjects = _CiscoLwappRogueMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1)
)
_CLRogueConfig_ObjectIdentity = ObjectIdentity
cLRogueConfig = _CLRogueConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1)
)
_CLRoguePolicyConfig_ObjectIdentity = ObjectIdentity
cLRoguePolicyConfig = _CLRoguePolicyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1)
)


class _CLRogueAdhocRogueReportEnable_Type(TruthValue):
    """Custom type cLRogueAdhocRogueReportEnable based on TruthValue"""
    defaultValue = 1


_CLRogueAdhocRogueReportEnable_Type.__name__ = "TruthValue"
_CLRogueAdhocRogueReportEnable_Object = MibScalar
cLRogueAdhocRogueReportEnable = _CLRogueAdhocRogueReportEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 1),
    _CLRogueAdhocRogueReportEnable_Type()
)
cLRogueAdhocRogueReportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRogueAdhocRogueReportEnable.setStatus("current")


class _CLRogueReportInterval_Type(Unsigned32):
    """Custom type cLRogueReportInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_CLRogueReportInterval_Type.__name__ = "Unsigned32"
_CLRogueReportInterval_Object = MibScalar
cLRogueReportInterval = _CLRogueReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 2),
    _CLRogueReportInterval_Type()
)
cLRogueReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRogueReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLRogueReportInterval.setUnits("seconds")


class _CLRogueMinimumRssi_Type(Integer32):
    """Custom type cLRogueMinimumRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, -70),
    )


_CLRogueMinimumRssi_Type.__name__ = "Integer32"
_CLRogueMinimumRssi_Object = MibScalar
cLRogueMinimumRssi = _CLRogueMinimumRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 3),
    _CLRogueMinimumRssi_Type()
)
cLRogueMinimumRssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRogueMinimumRssi.setStatus("current")
if mibBuilder.loadTexts:
    cLRogueMinimumRssi.setUnits("dBm")


class _CLRogueTransientInterval_Type(Unsigned32):
    """Custom type cLRogueTransientInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 1800),
    )


_CLRogueTransientInterval_Type.__name__ = "Unsigned32"
_CLRogueTransientInterval_Object = MibScalar
cLRogueTransientInterval = _CLRogueTransientInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 4),
    _CLRogueTransientInterval_Type()
)
cLRogueTransientInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRogueTransientInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLRogueTransientInterval.setUnits("seconds")
_CLRogueClientNumThreshold_Type = Unsigned32
_CLRogueClientNumThreshold_Object = MibScalar
cLRogueClientNumThreshold = _CLRogueClientNumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 5),
    _CLRogueClientNumThreshold_Type()
)
cLRogueClientNumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRogueClientNumThreshold.setStatus("current")


class _CLRogueDetectionSecurityLevel_Type(Integer32):
    """Custom type cLRogueDetectionSecurityLevel based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2),
          ("critical", 3),
          ("custom", 4))
    )


_CLRogueDetectionSecurityLevel_Type.__name__ = "Integer32"
_CLRogueDetectionSecurityLevel_Object = MibScalar
cLRogueDetectionSecurityLevel = _CLRogueDetectionSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 6),
    _CLRogueDetectionSecurityLevel_Type()
)
cLRogueDetectionSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRogueDetectionSecurityLevel.setStatus("current")


class _CLRogueValidateRogueClientsAgainstMse_Type(Integer32):
    """Custom type cLRogueValidateRogueClientsAgainstMse based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CLRogueValidateRogueClientsAgainstMse_Type.__name__ = "Integer32"
_CLRogueValidateRogueClientsAgainstMse_Object = MibScalar
cLRogueValidateRogueClientsAgainstMse = _CLRogueValidateRogueClientsAgainstMse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 7),
    _CLRogueValidateRogueClientsAgainstMse_Type()
)
cLRogueValidateRogueClientsAgainstMse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRogueValidateRogueClientsAgainstMse.setStatus("current")


class _CLRogueValidateRogueApsAgainstAAA_Type(Integer32):
    """Custom type cLRogueValidateRogueApsAgainstAAA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CLRogueValidateRogueApsAgainstAAA_Type.__name__ = "Integer32"
_CLRogueValidateRogueApsAgainstAAA_Object = MibScalar
cLRogueValidateRogueApsAgainstAAA = _CLRogueValidateRogueApsAgainstAAA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 8),
    _CLRogueValidateRogueApsAgainstAAA_Type()
)
cLRogueValidateRogueApsAgainstAAA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRogueValidateRogueApsAgainstAAA.setStatus("current")
_CLRogueApPollingInterval_Type = Unsigned32
_CLRogueApPollingInterval_Object = MibScalar
cLRogueApPollingInterval = _CLRogueApPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 9),
    _CLRogueApPollingInterval_Type()
)
cLRogueApPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRogueApPollingInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLRogueApPollingInterval.setUnits("seconds")
_CLRogueContainAutoRateEnable_Type = TruthValue
_CLRogueContainAutoRateEnable_Object = MibScalar
cLRogueContainAutoRateEnable = _CLRogueContainAutoRateEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 10),
    _CLRogueContainAutoRateEnable_Type()
)
cLRogueContainAutoRateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRogueContainAutoRateEnable.setStatus("current")


class _CLRogueAdhocRogueNotifEnabled_Type(TruthValue):
    """Custom type cLRogueAdhocRogueNotifEnabled based on TruthValue"""
    defaultValue = 2


_CLRogueAdhocRogueNotifEnabled_Type.__name__ = "TruthValue"
_CLRogueAdhocRogueNotifEnabled_Object = MibScalar
cLRogueAdhocRogueNotifEnabled = _CLRogueAdhocRogueNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 2),
    _CLRogueAdhocRogueNotifEnabled_Type()
)
cLRogueAdhocRogueNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRogueAdhocRogueNotifEnabled.setStatus("current")
_CLRogueRuleConfig_ObjectIdentity = ObjectIdentity
cLRogueRuleConfig = _CLRogueRuleConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3)
)
_CLRuleConfigTable_Object = MibTable
cLRuleConfigTable = _CLRuleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cLRuleConfigTable.setStatus("current")
_CLRuleConfigEntry_Object = MibTableRow
cLRuleConfigEntry = _CLRuleConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1)
)
cLRuleConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLRuleName"),
)
if mibBuilder.loadTexts:
    cLRuleConfigEntry.setStatus("current")


class _CLRuleName_Type(SnmpAdminString):
    """Custom type cLRuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRuleName_Type.__name__ = "SnmpAdminString"
_CLRuleName_Object = MibTableColumn
cLRuleName = _CLRuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 1),
    _CLRuleName_Type()
)
cLRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLRuleName.setStatus("current")


class _CLRuleRogueType_Type(Integer32):
    """Custom type cLRuleRogueType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("friendly", 1),
          ("malicious", 2),
          ("unclassified", 3),
          ("custom", 4))
    )


_CLRuleRogueType_Type.__name__ = "Integer32"
_CLRuleRogueType_Object = MibTableColumn
cLRuleRogueType = _CLRuleRogueType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 2),
    _CLRuleRogueType_Type()
)
cLRuleRogueType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRuleRogueType.setStatus("current")


class _CLRuleConditionsMatch_Type(Integer32):
    """Custom type cLRuleConditionsMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("any", 2))
    )


_CLRuleConditionsMatch_Type.__name__ = "Integer32"
_CLRuleConditionsMatch_Object = MibTableColumn
cLRuleConditionsMatch = _CLRuleConditionsMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 3),
    _CLRuleConditionsMatch_Type()
)
cLRuleConditionsMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRuleConditionsMatch.setStatus("current")
_CLRulePriority_Type = Unsigned32
_CLRulePriority_Object = MibTableColumn
cLRulePriority = _CLRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 4),
    _CLRulePriority_Type()
)
cLRulePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRulePriority.setStatus("current")
_CLRuleEnable_Type = TruthValue
_CLRuleEnable_Object = MibTableColumn
cLRuleEnable = _CLRuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 5),
    _CLRuleEnable_Type()
)
cLRuleEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRuleEnable.setStatus("current")


class _CLRuleStorageType_Type(StorageType):
    """Custom type cLRuleStorageType based on StorageType"""
    defaultValue = 3


_CLRuleStorageType_Type.__name__ = "StorageType"
_CLRuleStorageType_Object = MibTableColumn
cLRuleStorageType = _CLRuleStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 6),
    _CLRuleStorageType_Type()
)
cLRuleStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRuleStorageType.setStatus("current")
_CLRuleRowStatus_Type = RowStatus
_CLRuleRowStatus_Object = MibTableColumn
cLRuleRowStatus = _CLRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 7),
    _CLRuleRowStatus_Type()
)
cLRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRuleRowStatus.setStatus("current")
_CLRuleSeverityScore_Type = Unsigned32
_CLRuleSeverityScore_Object = MibTableColumn
cLRuleSeverityScore = _CLRuleSeverityScore_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 8),
    _CLRuleSeverityScore_Type()
)
cLRuleSeverityScore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRuleSeverityScore.setStatus("current")
_CLRuleClassificationName_Type = SnmpAdminString
_CLRuleClassificationName_Object = MibTableColumn
cLRuleClassificationName = _CLRuleClassificationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 9),
    _CLRuleClassificationName_Type()
)
cLRuleClassificationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRuleClassificationName.setStatus("current")


class _CLRuleNotifyType_Type(Integer32):
    """Custom type cLRuleNotifyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("global", 1),
          ("local", 2),
          ("none", 3),
          ("all", 4))
    )


_CLRuleNotifyType_Type.__name__ = "Integer32"
_CLRuleNotifyType_Object = MibTableColumn
cLRuleNotifyType = _CLRuleNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 10),
    _CLRuleNotifyType_Type()
)
cLRuleNotifyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRuleNotifyType.setStatus("current")


class _CLRuleStateType_Type(Integer32):
    """Custom type cLRuleStateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("contain", 2),
          ("internal", 3),
          ("external", 4),
          ("delete", 5))
    )


_CLRuleStateType_Type.__name__ = "Integer32"
_CLRuleStateType_Object = MibTableColumn
cLRuleStateType = _CLRuleStateType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 11),
    _CLRuleStateType_Type()
)
cLRuleStateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRuleStateType.setStatus("current")
_CLConditionConfigTable_Object = MibTable
cLConditionConfigTable = _CLConditionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cLConditionConfigTable.setStatus("current")
_CLConditionConfigEntry_Object = MibTableRow
cLConditionConfigEntry = _CLConditionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1)
)
cLConditionConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLRuleName"),
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLConditionName"),
)
if mibBuilder.loadTexts:
    cLConditionConfigEntry.setStatus("current")


class _CLConditionName_Type(SnmpAdminString):
    """Custom type cLConditionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CLConditionName_Type.__name__ = "SnmpAdminString"
_CLConditionName_Object = MibTableColumn
cLConditionName = _CLConditionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 1),
    _CLConditionName_Type()
)
cLConditionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLConditionName.setStatus("current")


class _CLConditionType_Type(Integer32):
    """Custom type cLConditionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("managedSsid", 1),
          ("rssi", 2),
          ("duration", 3),
          ("clientCount", 4),
          ("noEncryption", 5),
          ("userConfigSsid", 6),
          ("wildCardSsid", 7))
    )


_CLConditionType_Type.__name__ = "Integer32"
_CLConditionType_Object = MibTableColumn
cLConditionType = _CLConditionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 2),
    _CLConditionType_Type()
)
cLConditionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionType.setStatus("current")
_CLConditionValue_Type = Integer32
_CLConditionValue_Object = MibTableColumn
cLConditionValue = _CLConditionValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 3),
    _CLConditionValue_Type()
)
cLConditionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionValue.setStatus("current")
_CLConditionEnable_Type = TruthValue
_CLConditionEnable_Object = MibTableColumn
cLConditionEnable = _CLConditionEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 4),
    _CLConditionEnable_Type()
)
cLConditionEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionEnable.setStatus("current")


class _CLConditionStorageType_Type(StorageType):
    """Custom type cLConditionStorageType based on StorageType"""
    defaultValue = 3


_CLConditionStorageType_Type.__name__ = "StorageType"
_CLConditionStorageType_Object = MibTableColumn
cLConditionStorageType = _CLConditionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 5),
    _CLConditionStorageType_Type()
)
cLConditionStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionStorageType.setStatus("current")
_CLConditionRowStatus_Type = RowStatus
_CLConditionRowStatus_Object = MibTableColumn
cLConditionRowStatus = _CLConditionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 6),
    _CLConditionRowStatus_Type()
)
cLConditionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionRowStatus.setStatus("current")


class _CLConditionRssi_Type(Integer32):
    """Custom type cLConditionRssi based on Integer32"""
    defaultValue = 0


_CLConditionRssi_Type.__name__ = "Integer32"
_CLConditionRssi_Object = MibTableColumn
cLConditionRssi = _CLConditionRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 7),
    _CLConditionRssi_Type()
)
cLConditionRssi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionRssi.setStatus("current")


class _CLConditionClientCount_Type(Unsigned32):
    """Custom type cLConditionClientCount based on Unsigned32"""
    defaultValue = 0


_CLConditionClientCount_Type.__name__ = "Unsigned32"
_CLConditionClientCount_Object = MibTableColumn
cLConditionClientCount = _CLConditionClientCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 8),
    _CLConditionClientCount_Type()
)
cLConditionClientCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionClientCount.setStatus("current")


class _CLConditionNoEncryptionEnabled_Type(TruthValue):
    """Custom type cLConditionNoEncryptionEnabled based on TruthValue"""
    defaultValue = 1


_CLConditionNoEncryptionEnabled_Type.__name__ = "TruthValue"
_CLConditionNoEncryptionEnabled_Object = MibTableColumn
cLConditionNoEncryptionEnabled = _CLConditionNoEncryptionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 9),
    _CLConditionNoEncryptionEnabled_Type()
)
cLConditionNoEncryptionEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionNoEncryptionEnabled.setStatus("current")


class _CLConditionManagedSsidEnabled_Type(TruthValue):
    """Custom type cLConditionManagedSsidEnabled based on TruthValue"""
    defaultValue = 1


_CLConditionManagedSsidEnabled_Type.__name__ = "TruthValue"
_CLConditionManagedSsidEnabled_Object = MibTableColumn
cLConditionManagedSsidEnabled = _CLConditionManagedSsidEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 10),
    _CLConditionManagedSsidEnabled_Type()
)
cLConditionManagedSsidEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionManagedSsidEnabled.setStatus("current")


class _CLConditionDuration_Type(Unsigned32):
    """Custom type cLConditionDuration based on Unsigned32"""
    defaultValue = 0


_CLConditionDuration_Type.__name__ = "Unsigned32"
_CLConditionDuration_Object = MibTableColumn
cLConditionDuration = _CLConditionDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 11),
    _CLConditionDuration_Type()
)
cLConditionDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionDuration.setStatus("current")
if mibBuilder.loadTexts:
    cLConditionDuration.setUnits("seconds")
_CLConditionSsidConfigTable_Object = MibTable
cLConditionSsidConfigTable = _CLConditionSsidConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cLConditionSsidConfigTable.setStatus("current")
_CLConditionSsidConfigEntry_Object = MibTableRow
cLConditionSsidConfigEntry = _CLConditionSsidConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 3, 1)
)
cLConditionSsidConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLRuleName"),
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLConditionName"),
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidValue"),
)
if mibBuilder.loadTexts:
    cLConditionSsidConfigEntry.setStatus("current")


class _CLConditionSsidValue_Type(SnmpAdminString):
    """Custom type cLConditionSsidValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLConditionSsidValue_Type.__name__ = "SnmpAdminString"
_CLConditionSsidValue_Object = MibTableColumn
cLConditionSsidValue = _CLConditionSsidValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 3, 1, 1),
    _CLConditionSsidValue_Type()
)
cLConditionSsidValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLConditionSsidValue.setStatus("current")


class _CLConditionSsidStorageType_Type(StorageType):
    """Custom type cLConditionSsidStorageType based on StorageType"""
    defaultValue = 3


_CLConditionSsidStorageType_Type.__name__ = "StorageType"
_CLConditionSsidStorageType_Object = MibTableColumn
cLConditionSsidStorageType = _CLConditionSsidStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 3, 1, 2),
    _CLConditionSsidStorageType_Type()
)
cLConditionSsidStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionSsidStorageType.setStatus("current")
_CLConditionSsidRowStatus_Type = RowStatus
_CLConditionSsidRowStatus_Object = MibTableColumn
cLConditionSsidRowStatus = _CLConditionSsidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 3, 1, 3),
    _CLConditionSsidRowStatus_Type()
)
cLConditionSsidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionSsidRowStatus.setStatus("current")


class _CLConditionSsidType_Type(Integer32):
    """Custom type cLConditionSsidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("wildCard", 2))
    )


_CLConditionSsidType_Type.__name__ = "Integer32"
_CLConditionSsidType_Object = MibTableColumn
cLConditionSsidType = _CLConditionSsidType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 3, 1, 4),
    _CLConditionSsidType_Type()
)
cLConditionSsidType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLConditionSsidType.setStatus("current")
_CLRogueIgnoreListConfig_ObjectIdentity = ObjectIdentity
cLRogueIgnoreListConfig = _CLRogueIgnoreListConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 4)
)
_CLRogueIgnoreListTable_Object = MibTable
cLRogueIgnoreListTable = _CLRogueIgnoreListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cLRogueIgnoreListTable.setStatus("current")
_CLRogueIgnoreListEntry_Object = MibTableRow
cLRogueIgnoreListEntry = _CLRogueIgnoreListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 4, 1, 1)
)
cLRogueIgnoreListEntry.setIndexNames(
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListMACAddress"),
)
if mibBuilder.loadTexts:
    cLRogueIgnoreListEntry.setStatus("current")
_CLRogueIgnoreListMACAddress_Type = MacAddress
_CLRogueIgnoreListMACAddress_Object = MibTableColumn
cLRogueIgnoreListMACAddress = _CLRogueIgnoreListMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 4, 1, 1, 1),
    _CLRogueIgnoreListMACAddress_Type()
)
cLRogueIgnoreListMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLRogueIgnoreListMACAddress.setStatus("current")


class _CLRogueIgnoreListStorageType_Type(StorageType):
    """Custom type cLRogueIgnoreListStorageType based on StorageType"""
    defaultValue = 3


_CLRogueIgnoreListStorageType_Type.__name__ = "StorageType"
_CLRogueIgnoreListStorageType_Object = MibTableColumn
cLRogueIgnoreListStorageType = _CLRogueIgnoreListStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 4, 1, 1, 2),
    _CLRogueIgnoreListStorageType_Type()
)
cLRogueIgnoreListStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRogueIgnoreListStorageType.setStatus("current")
_CLRogueIgnoreListRowStatus_Type = RowStatus
_CLRogueIgnoreListRowStatus_Object = MibTableColumn
cLRogueIgnoreListRowStatus = _CLRogueIgnoreListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 4, 1, 1, 3),
    _CLRogueIgnoreListRowStatus_Type()
)
cLRogueIgnoreListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRogueIgnoreListRowStatus.setStatus("current")
_CLRldpAutoContainConfig_ObjectIdentity = ObjectIdentity
cLRldpAutoContainConfig = _CLRldpAutoContainConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5)
)


class _CLRldpAutoContainFeatureOnWiredNetwork_Type(Integer32):
    """Custom type cLRldpAutoContainFeatureOnWiredNetwork based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CLRldpAutoContainFeatureOnWiredNetwork_Type.__name__ = "Integer32"
_CLRldpAutoContainFeatureOnWiredNetwork_Object = MibScalar
cLRldpAutoContainFeatureOnWiredNetwork = _CLRldpAutoContainFeatureOnWiredNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5, 1),
    _CLRldpAutoContainFeatureOnWiredNetwork_Type()
)
cLRldpAutoContainFeatureOnWiredNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRldpAutoContainFeatureOnWiredNetwork.setStatus("current")


class _CLRldpAutoContainRoguesAdvertisingSsid_Type(CLAutoContainActions):
    """Custom type cLRldpAutoContainRoguesAdvertisingSsid based on CLAutoContainActions"""
    defaultValue = 1


_CLRldpAutoContainRoguesAdvertisingSsid_Type.__name__ = "CLAutoContainActions"
_CLRldpAutoContainRoguesAdvertisingSsid_Object = MibScalar
cLRldpAutoContainRoguesAdvertisingSsid = _CLRldpAutoContainRoguesAdvertisingSsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5, 2),
    _CLRldpAutoContainRoguesAdvertisingSsid_Type()
)
cLRldpAutoContainRoguesAdvertisingSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRldpAutoContainRoguesAdvertisingSsid.setStatus("current")


class _CLRldpAutoContainAdhocNetworks_Type(CLAutoContainActions):
    """Custom type cLRldpAutoContainAdhocNetworks based on CLAutoContainActions"""
    defaultValue = 1


_CLRldpAutoContainAdhocNetworks_Type.__name__ = "CLAutoContainActions"
_CLRldpAutoContainAdhocNetworks_Object = MibScalar
cLRldpAutoContainAdhocNetworks = _CLRldpAutoContainAdhocNetworks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5, 3),
    _CLRldpAutoContainAdhocNetworks_Type()
)
cLRldpAutoContainAdhocNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRldpAutoContainAdhocNetworks.setStatus("current")


class _CLRldpAutoContainTrustedClientsOnRogueAps_Type(CLAutoContainActions):
    """Custom type cLRldpAutoContainTrustedClientsOnRogueAps based on CLAutoContainActions"""
    defaultValue = 1


_CLRldpAutoContainTrustedClientsOnRogueAps_Type.__name__ = "CLAutoContainActions"
_CLRldpAutoContainTrustedClientsOnRogueAps_Object = MibScalar
cLRldpAutoContainTrustedClientsOnRogueAps = _CLRldpAutoContainTrustedClientsOnRogueAps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5, 4),
    _CLRldpAutoContainTrustedClientsOnRogueAps_Type()
)
cLRldpAutoContainTrustedClientsOnRogueAps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRldpAutoContainTrustedClientsOnRogueAps.setStatus("current")


class _CLRldpAutoContainLevel_Type(Integer32):
    """Custom type cLRldpAutoContainLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_CLRldpAutoContainLevel_Type.__name__ = "Integer32"
_CLRldpAutoContainLevel_Object = MibScalar
cLRldpAutoContainLevel = _CLRldpAutoContainLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5, 5),
    _CLRldpAutoContainLevel_Type()
)
cLRldpAutoContainLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRldpAutoContainLevel.setStatus("current")


class _CLRldpAutoContainOnlyforMonitorModeAps_Type(Integer32):
    """Custom type cLRldpAutoContainOnlyforMonitorModeAps based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CLRldpAutoContainOnlyforMonitorModeAps_Type.__name__ = "Integer32"
_CLRldpAutoContainOnlyforMonitorModeAps_Object = MibScalar
cLRldpAutoContainOnlyforMonitorModeAps = _CLRldpAutoContainOnlyforMonitorModeAps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5, 6),
    _CLRldpAutoContainOnlyforMonitorModeAps_Type()
)
cLRldpAutoContainOnlyforMonitorModeAps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRldpAutoContainOnlyforMonitorModeAps.setStatus("current")


class _CLRldpAutoContainFlexStandaloneAp_Type(Integer32):
    """Custom type cLRldpAutoContainFlexStandaloneAp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CLRldpAutoContainFlexStandaloneAp_Type.__name__ = "Integer32"
_CLRldpAutoContainFlexStandaloneAp_Object = MibScalar
cLRldpAutoContainFlexStandaloneAp = _CLRldpAutoContainFlexStandaloneAp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5, 7),
    _CLRldpAutoContainFlexStandaloneAp_Type()
)
cLRldpAutoContainFlexStandaloneAp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRldpAutoContainFlexStandaloneAp.setStatus("current")
_CLRogueApConfig_ObjectIdentity = ObjectIdentity
cLRogueApConfig = _CLRogueApConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6)
)
_CLRogueApTable_Object = MibTable
cLRogueApTable = _CLRogueApTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cLRogueApTable.setStatus("deprecated")
_CLRogueApEntry_Object = MibTableRow
cLRogueApEntry = _CLRogueApEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1, 1)
)
cLRogueApEntry.setIndexNames(
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLRogueApMACAddress"),
)
if mibBuilder.loadTexts:
    cLRogueApEntry.setStatus("deprecated")
_CLRogueApMACAddress_Type = MacAddress
_CLRogueApMACAddress_Object = MibTableColumn
cLRogueApMACAddress = _CLRogueApMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1, 1, 1),
    _CLRogueApMACAddress_Type()
)
cLRogueApMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLRogueApMACAddress.setStatus("deprecated")


class _CLRogueApClassType_Type(Integer32):
    """Custom type cLRogueApClassType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("friendly", 1),
          ("malicious", 2),
          ("unclassified", 3),
          ("custom", 4))
    )


_CLRogueApClassType_Type.__name__ = "Integer32"
_CLRogueApClassType_Object = MibTableColumn
cLRogueApClassType = _CLRogueApClassType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1, 1, 2),
    _CLRogueApClassType_Type()
)
cLRogueApClassType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRogueApClassType.setStatus("deprecated")


class _CLRogueApState_Type(Integer32):
    """Custom type cLRogueApState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("pending", 1),
          ("alert", 2),
          ("detectedLrad", 3),
          ("known", 4),
          ("acknowledge", 5),
          ("contained", 6),
          ("threat", 7),
          ("containedPending", 8),
          ("knownContained", 9),
          ("trustedMissing", 10),
          ("initializing", 11))
    )


_CLRogueApState_Type.__name__ = "Integer32"
_CLRogueApState_Object = MibTableColumn
cLRogueApState = _CLRogueApState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1, 1, 3),
    _CLRogueApState_Type()
)
cLRogueApState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRogueApState.setStatus("deprecated")


class _CLRogueApStorageType_Type(StorageType):
    """Custom type cLRogueApStorageType based on StorageType"""
    defaultValue = 3


_CLRogueApStorageType_Type.__name__ = "StorageType"
_CLRogueApStorageType_Object = MibTableColumn
cLRogueApStorageType = _CLRogueApStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1, 1, 4),
    _CLRogueApStorageType_Type()
)
cLRogueApStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRogueApStorageType.setStatus("deprecated")
_CLRogueApRowStatus_Type = RowStatus
_CLRogueApRowStatus_Object = MibTableColumn
cLRogueApRowStatus = _CLRogueApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1, 1, 5),
    _CLRogueApRowStatus_Type()
)
cLRogueApRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRogueApRowStatus.setStatus("deprecated")
_CLRogueApListTable_Object = MibTable
cLRogueApListTable = _CLRogueApListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cLRogueApListTable.setStatus("current")
_CLRogueApListEntry_Object = MibTableRow
cLRogueApListEntry = _CLRogueApListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 2, 1)
)
cLRogueApListEntry.setIndexNames(
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLRogueApMacAddr"),
)
if mibBuilder.loadTexts:
    cLRogueApListEntry.setStatus("current")
_CLRogueApMacAddr_Type = MacAddress
_CLRogueApMacAddr_Object = MibTableColumn
cLRogueApMacAddr = _CLRogueApMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 2, 1, 1),
    _CLRogueApMacAddr_Type()
)
cLRogueApMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLRogueApMacAddr.setStatus("current")
_CLRogueApSeverityScore_Type = Unsigned32
_CLRogueApSeverityScore_Object = MibTableColumn
cLRogueApSeverityScore = _CLRogueApSeverityScore_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 2, 1, 2),
    _CLRogueApSeverityScore_Type()
)
cLRogueApSeverityScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueApSeverityScore.setStatus("current")
_CLRogueApRuleName_Type = SnmpAdminString
_CLRogueApRuleName_Object = MibTableColumn
cLRogueApRuleName = _CLRogueApRuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 2, 1, 3),
    _CLRogueApRuleName_Type()
)
cLRogueApRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueApRuleName.setStatus("current")
_CLRogueApClassName_Type = SnmpAdminString
_CLRogueApClassName_Object = MibTableColumn
cLRogueApClassName = _CLRogueApClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 2, 1, 4),
    _CLRogueApClassName_Type()
)
cLRogueApClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueApClassName.setStatus("current")
_CLRogueClientConfig_ObjectIdentity = ObjectIdentity
cLRogueClientConfig = _CLRogueClientConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 7)
)
_CLRogueClientTable_Object = MibTable
cLRogueClientTable = _CLRogueClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cLRogueClientTable.setStatus("current")
_CLRogueClientEntry_Object = MibTableRow
cLRogueClientEntry = _CLRogueClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 7, 1, 1)
)
cLRogueClientEntry.setIndexNames(
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLRogueClientMacAddress"),
)
if mibBuilder.loadTexts:
    cLRogueClientEntry.setStatus("current")
_CLRogueClientMacAddress_Type = MacAddress
_CLRogueClientMacAddress_Object = MibTableColumn
cLRogueClientMacAddress = _CLRogueClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 7, 1, 1, 1),
    _CLRogueClientMacAddress_Type()
)
cLRogueClientMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLRogueClientMacAddress.setStatus("current")
_CLRogueClientGatewayMacAddress_Type = MacAddress
_CLRogueClientGatewayMacAddress_Object = MibTableColumn
cLRogueClientGatewayMacAddress = _CLRogueClientGatewayMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 7, 1, 1, 2),
    _CLRogueClientGatewayMacAddress_Type()
)
cLRogueClientGatewayMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueClientGatewayMacAddress.setStatus("current")
_CLRogueApDetectingApDetails_ObjectIdentity = ObjectIdentity
cLRogueApDetectingApDetails = _CLRogueApDetectingApDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8)
)
_CLRogueAPDetectingAPTable_Object = MibTable
cLRogueAPDetectingAPTable = _CLRogueAPDetectingAPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cLRogueAPDetectingAPTable.setStatus("current")
_CLRogueAPDetectingAPEntry_Object = MibTableRow
cLRogueAPDetectingAPEntry = _CLRogueAPDetectingAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1)
)
cLRogueAPDetectingAPEntry.setIndexNames(
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLRogueApMacAddr"),
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLRogueAPDetectingAPMacAddress"),
    (0, "CISCO-LWAPP-ROGUE-MIB", "cLRogueAPDetectingAPSlotId"),
)
if mibBuilder.loadTexts:
    cLRogueAPDetectingAPEntry.setStatus("current")
_CLRogueAPDetectingAPMacAddress_Type = MacAddress
_CLRogueAPDetectingAPMacAddress_Object = MibTableColumn
cLRogueAPDetectingAPMacAddress = _CLRogueAPDetectingAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1, 1),
    _CLRogueAPDetectingAPMacAddress_Type()
)
cLRogueAPDetectingAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueAPDetectingAPMacAddress.setStatus("current")


class _CLRogueAPDetectingAPSlotId_Type(Unsigned32):
    """Custom type cLRogueAPDetectingAPSlotId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CLRogueAPDetectingAPSlotId_Type.__name__ = "Unsigned32"
_CLRogueAPDetectingAPSlotId_Object = MibTableColumn
cLRogueAPDetectingAPSlotId = _CLRogueAPDetectingAPSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1, 2),
    _CLRogueAPDetectingAPSlotId_Type()
)
cLRogueAPDetectingAPSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueAPDetectingAPSlotId.setStatus("current")


class _CLRogueAPRadioType_Type(Integer32):
    """Custom type cLRogueAPRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("dot11b", 1),
          ("dot11a", 2),
          ("dot11abgn", 3),
          ("uwb", 4),
          ("dot11g", 5),
          ("dot11n24", 6),
          ("dot11n5", 7),
          ("unknown", 8),
          ("dot11ac", 9),
          ("dot11ax24", 10),
          ("dot11ax5", 11),
          ("dot11ax6", 12))
    )


_CLRogueAPRadioType_Type.__name__ = "Integer32"
_CLRogueAPRadioType_Object = MibTableColumn
cLRogueAPRadioType = _CLRogueAPRadioType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1, 3),
    _CLRogueAPRadioType_Type()
)
cLRogueAPRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueAPRadioType.setStatus("current")
_CLRogueAPDetectingAPName_Type = SnmpAdminString
_CLRogueAPDetectingAPName_Object = MibTableColumn
cLRogueAPDetectingAPName = _CLRogueAPDetectingAPName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1, 4),
    _CLRogueAPDetectingAPName_Type()
)
cLRogueAPDetectingAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueAPDetectingAPName.setStatus("current")
_CLRogueAPChannelNumber_Type = Integer32
_CLRogueAPChannelNumber_Object = MibTableColumn
cLRogueAPChannelNumber = _CLRogueAPChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1, 5),
    _CLRogueAPChannelNumber_Type()
)
cLRogueAPChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueAPChannelNumber.setStatus("current")
_CLRogueAPSsid_Type = SnmpAdminString
_CLRogueAPSsid_Object = MibTableColumn
cLRogueAPSsid = _CLRogueAPSsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1, 6),
    _CLRogueAPSsid_Type()
)
cLRogueAPSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueAPSsid.setStatus("current")


class _CLRogueAPHiddenSsid_Type(Integer32):
    """Custom type cLRogueAPHiddenSsid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CLRogueAPHiddenSsid_Type.__name__ = "Integer32"
_CLRogueAPHiddenSsid_Object = MibTableColumn
cLRogueAPHiddenSsid = _CLRogueAPHiddenSsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1, 7),
    _CLRogueAPHiddenSsid_Type()
)
cLRogueAPHiddenSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueAPHiddenSsid.setStatus("current")
_CLRogueAPDetectingAPRSSI_Type = Integer32
_CLRogueAPDetectingAPRSSI_Object = MibTableColumn
cLRogueAPDetectingAPRSSI = _CLRogueAPDetectingAPRSSI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1, 8),
    _CLRogueAPDetectingAPRSSI_Type()
)
cLRogueAPDetectingAPRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueAPDetectingAPRSSI.setStatus("current")


class _CLRogueAPContainmentMode_Type(Integer32):
    """Custom type cLRogueAPContainmentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("deauthBroadcast", 1),
          ("cfp", 2),
          ("clientContianment", 3),
          ("adhocContainment", 4),
          ("max", 5),
          ("unknown", 99))
    )


_CLRogueAPContainmentMode_Type.__name__ = "Integer32"
_CLRogueAPContainmentMode_Object = MibTableColumn
cLRogueAPContainmentMode = _CLRogueAPContainmentMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1, 9),
    _CLRogueAPContainmentMode_Type()
)
cLRogueAPContainmentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueAPContainmentMode.setStatus("current")
_CLRogueAPContainmentChannelCount_Type = Unsigned32
_CLRogueAPContainmentChannelCount_Object = MibTableColumn
cLRogueAPContainmentChannelCount = _CLRogueAPContainmentChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1, 10),
    _CLRogueAPContainmentChannelCount_Type()
)
cLRogueAPContainmentChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueAPContainmentChannelCount.setStatus("current")
_CLRogueAPContainmentChannels_Type = SnmpAdminString
_CLRogueAPContainmentChannels_Object = MibTableColumn
cLRogueAPContainmentChannels = _CLRogueAPContainmentChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1, 11),
    _CLRogueAPContainmentChannels_Type()
)
cLRogueAPContainmentChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueAPContainmentChannels.setStatus("current")
_CLRogueAPDetectingAPLastHeard_Type = Counter32
_CLRogueAPDetectingAPLastHeard_Object = MibTableColumn
cLRogueAPDetectingAPLastHeard = _CLRogueAPDetectingAPLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1, 12),
    _CLRogueAPDetectingAPLastHeard_Type()
)
cLRogueAPDetectingAPLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueAPDetectingAPLastHeard.setStatus("current")


class _CLRogueAPDetectingAPWepMode_Type(Integer32):
    """Custom type cLRogueAPDetectingAPWepMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CLRogueAPDetectingAPWepMode_Type.__name__ = "Integer32"
_CLRogueAPDetectingAPWepMode_Object = MibTableColumn
cLRogueAPDetectingAPWepMode = _CLRogueAPDetectingAPWepMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1, 13),
    _CLRogueAPDetectingAPWepMode_Type()
)
cLRogueAPDetectingAPWepMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueAPDetectingAPWepMode.setStatus("current")


class _CLRogueAPDetectingAPPreamble_Type(Integer32):
    """Custom type cLRogueAPDetectingAPPreamble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 0),
          ("short", 1),
          ("notSupported", 2))
    )


_CLRogueAPDetectingAPPreamble_Type.__name__ = "Integer32"
_CLRogueAPDetectingAPPreamble_Object = MibTableColumn
cLRogueAPDetectingAPPreamble = _CLRogueAPDetectingAPPreamble_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1, 14),
    _CLRogueAPDetectingAPPreamble_Type()
)
cLRogueAPDetectingAPPreamble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueAPDetectingAPPreamble.setStatus("current")


class _CLRogueAPDetectingAPWpaMode_Type(Integer32):
    """Custom type cLRogueAPDetectingAPWpaMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CLRogueAPDetectingAPWpaMode_Type.__name__ = "Integer32"
_CLRogueAPDetectingAPWpaMode_Object = MibTableColumn
cLRogueAPDetectingAPWpaMode = _CLRogueAPDetectingAPWpaMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1, 15),
    _CLRogueAPDetectingAPWpaMode_Type()
)
cLRogueAPDetectingAPWpaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueAPDetectingAPWpaMode.setStatus("current")


class _CLRogueAPDetectingAPWpa2Mode_Type(Integer32):
    """Custom type cLRogueAPDetectingAPWpa2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CLRogueAPDetectingAPWpa2Mode_Type.__name__ = "Integer32"
_CLRogueAPDetectingAPWpa2Mode_Object = MibTableColumn
cLRogueAPDetectingAPWpa2Mode = _CLRogueAPDetectingAPWpa2Mode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1, 16),
    _CLRogueAPDetectingAPWpa2Mode_Type()
)
cLRogueAPDetectingAPWpa2Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueAPDetectingAPWpa2Mode.setStatus("current")


class _CLRogueAPDetectingAPFTMode_Type(Integer32):
    """Custom type cLRogueAPDetectingAPFTMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CLRogueAPDetectingAPFTMode_Type.__name__ = "Integer32"
_CLRogueAPDetectingAPFTMode_Object = MibTableColumn
cLRogueAPDetectingAPFTMode = _CLRogueAPDetectingAPFTMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1, 17),
    _CLRogueAPDetectingAPFTMode_Type()
)
cLRogueAPDetectingAPFTMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueAPDetectingAPFTMode.setStatus("current")
_CLRogueAPDetectingAPSNR_Type = Integer32
_CLRogueAPDetectingAPSNR_Object = MibTableColumn
cLRogueAPDetectingAPSNR = _CLRogueAPDetectingAPSNR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1, 18),
    _CLRogueAPDetectingAPSNR_Type()
)
cLRogueAPDetectingAPSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueAPDetectingAPSNR.setStatus("current")


class _CLRogueAPChannelWidth_Type(Integer32):
    """Custom type cLRogueAPChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("five", 1),
          ("ten", 2),
          ("twenty", 3),
          ("aboveforty", 4),
          ("belowforty", 5),
          ("abovefortyAndEighty", 6),
          ("abovefortyBelowEighty", 7),
          ("aboveEightyBelowforty", 8),
          ("belowfortyBelowEighty", 9),
          ("aboveOnesixtyAboveFortyAboveEighty", 10),
          ("belowOnesixtyAboveFortyAboveEighty", 11),
          ("aboveOnesixtyBelowFortyAboveEighty", 12),
          ("belowOnesixtyBelowFortyAboveEighty", 13),
          ("aboveOnesixtyAboveFortyBelowEighty", 14),
          ("belowOnesixtyAboveFortyBelowEighty", 15),
          ("aboveOnesixtyBelowFortyBelowEighty", 16),
          ("belowOnesixtyBelowFortyBelowEighty", 17))
    )


_CLRogueAPChannelWidth_Type.__name__ = "Integer32"
_CLRogueAPChannelWidth_Object = MibTableColumn
cLRogueAPChannelWidth = _CLRogueAPChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1, 19),
    _CLRogueAPChannelWidth_Type()
)
cLRogueAPChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueAPChannelWidth.setStatus("current")
_CLRogueAPPhysicalAPSlot_Type = Integer32
_CLRogueAPPhysicalAPSlot_Object = MibTableColumn
cLRogueAPPhysicalAPSlot = _CLRogueAPPhysicalAPSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 8, 1, 1, 20),
    _CLRogueAPPhysicalAPSlot_Type()
)
cLRogueAPPhysicalAPSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueAPPhysicalAPSlot.setStatus("current")
_CiscoLwappRogueMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappRogueMIBConform = _CiscoLwappRogueMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2)
)
_CiscoLwappRogueMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappRogueMIBCompliances = _CiscoLwappRogueMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 1)
)
_CiscoLwappRogueMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappRogueMIBGroups = _CiscoLwappRogueMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2)
)
_CiscoLwappRogueMIBNotifObjects_ObjectIdentity = ObjectIdentity
ciscoLwappRogueMIBNotifObjects = _CiscoLwappRogueMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 3)
)


class _CLRogueApContainmentLevel_Type(Integer32):
    """Custom type cLRogueApContainmentLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unassigned", 0),
          ("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4))
    )


_CLRogueApContainmentLevel_Type.__name__ = "Integer32"
_CLRogueApContainmentLevel_Object = MibScalar
cLRogueApContainmentLevel = _CLRogueApContainmentLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 3, 1),
    _CLRogueApContainmentLevel_Type()
)
cLRogueApContainmentLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLRogueApContainmentLevel.setStatus("current")
_CLRogueClientTotalDetectingAPs_Type = Integer32
_CLRogueClientTotalDetectingAPs_Object = MibScalar
cLRogueClientTotalDetectingAPs = _CLRogueClientTotalDetectingAPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 3, 2),
    _CLRogueClientTotalDetectingAPs_Type()
)
cLRogueClientTotalDetectingAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueClientTotalDetectingAPs.setStatus("current")
_CLRogueClientFirstReported_Type = SnmpAdminString
_CLRogueClientFirstReported_Object = MibScalar
cLRogueClientFirstReported = _CLRogueClientFirstReported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 3, 3),
    _CLRogueClientFirstReported_Type()
)
cLRogueClientFirstReported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueClientFirstReported.setStatus("current")
_CLRogueClientLastReported_Type = SnmpAdminString
_CLRogueClientLastReported_Object = MibScalar
cLRogueClientLastReported = _CLRogueClientLastReported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 3, 4),
    _CLRogueClientLastReported_Type()
)
cLRogueClientLastReported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRogueClientLastReported.setStatus("current")
_CLRogueClientGatewayMac_Type = MacAddress
_CLRogueClientGatewayMac_Object = MibScalar
cLRogueClientGatewayMac = _CLRogueClientGatewayMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 3, 5),
    _CLRogueClientGatewayMac_Type()
)
cLRogueClientGatewayMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLRogueClientGatewayMac.setStatus("current")
_CLLastDetectingRadioMACAddress_Type = MacAddress
_CLLastDetectingRadioMACAddress_Object = MibScalar
cLLastDetectingRadioMACAddress = _CLLastDetectingRadioMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 3, 6),
    _CLLastDetectingRadioMACAddress_Type()
)
cLLastDetectingRadioMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLLastDetectingRadioMACAddress.setStatus("current")

# Managed Objects groups

ciscoLwappRogueConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2, 1)
)
ciscoLwappRogueConfigGroup.setObjects(
      *(("CISCO-LWAPP-ROGUE-MIB", "cLRogueAdhocRogueReportEnable"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAdhocRogueNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoLwappRogueConfigGroup.setStatus("current")

ciscoLwappRogueConfigSup1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2, 3)
)
ciscoLwappRogueConfigSup1Group.setObjects(
      *(("CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleRogueType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleConditionsMatch"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRulePriority"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleEnable"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionValue"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionEnable"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainFeatureOnWiredNetwork"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainRoguesAdvertisingSsid"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainAdhocNetworks"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainTrustedClientsOnRogueAps"))
)
if mibBuilder.loadTexts:
    ciscoLwappRogueConfigSup1Group.setStatus("deprecated")

ciscoLwappRogueConfigSup2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2, 4)
)
ciscoLwappRogueConfigSup2Group.setObjects(
      *(("CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleRogueType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleConditionsMatch"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRulePriority"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleEnable"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionValue"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionEnable"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainFeatureOnWiredNetwork"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainRoguesAdvertisingSsid"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainAdhocNetworks"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainTrustedClientsOnRogueAps"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainLevel"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainOnlyforMonitorModeAps"))
)
if mibBuilder.loadTexts:
    ciscoLwappRogueConfigSup2Group.setStatus("deprecated")

ciscoLwappRogueConfigSup3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2, 5)
)
ciscoLwappRogueConfigSup3Group.setObjects(
      *(("CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleRogueType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleConditionsMatch"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRulePriority"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleEnable"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionValue"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionEnable"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainFeatureOnWiredNetwork"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainRoguesAdvertisingSsid"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainAdhocNetworks"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainTrustedClientsOnRogueAps"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainLevel"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainOnlyforMonitorModeAps"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueReportInterval"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueMinimumRssi"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueTransientInterval"))
)
if mibBuilder.loadTexts:
    ciscoLwappRogueConfigSup3Group.setStatus("current")

ciscoLwappRogueConfigSup4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2, 6)
)
ciscoLwappRogueConfigSup4Group.setObjects(
      *(("CISCO-LWAPP-ROGUE-MIB", "cLRogueApClassType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueApState"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueApStorageType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueApRowStatus"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueClientNumThreshold"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueDetectionSecurityLevel"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueValidateRogueClientsAgainstMse"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionRssi"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionClientCount"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionNoEncryptionEnabled"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionManagedSsidEnabled"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionDuration"))
)
if mibBuilder.loadTexts:
    ciscoLwappRogueConfigSup4Group.setStatus("current")

ciscoLwappRogueConfigSup5Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2, 7)
)
ciscoLwappRogueConfigSup5Group.setObjects(
      *(("CISCO-LWAPP-ROGUE-MIB", "cLRuleSeverityScore"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleClassificationName"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleNotifyType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleStateType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAPDetectingAPSlotId"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAPRadioType"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAPDetectingAPName"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAPChannelNumber"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAPSsid"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAPHiddenSsid"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAPDetectingAPRSSI"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAPContainmentMode"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAPContainmentChannelCount"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAPContainmentChannels"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAPDetectingAPLastHeard"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAPDetectingAPWepMode"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAPDetectingAPPreamble"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAPDetectingAPWpaMode"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAPDetectingAPWpa2Mode"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAPDetectingAPFTMode"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAPDetectingAPSNR"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAPChannelWidth"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAPPhysicalAPSlot"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueClientGatewayMacAddress"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueApRuleName"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueApClassName"))
)
if mibBuilder.loadTexts:
    ciscoLwappRogueConfigSup5Group.setStatus("current")


# Notification objects

cLRogueAdhocRogueDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 0, 1)
)
cLRogueAdhocRogueDetected.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApName")
)
if mibBuilder.loadTexts:
    cLRogueAdhocRogueDetected.setStatus(
        "current"
    )

cLRogueClientExceededThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 0, 2)
)
cLRogueClientExceededThreshold.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApDot11RadioMACAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioChannelNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfSmtDot11Bssid"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleStateType"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueDetectedChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueDot11RadioBand"))
)
if mibBuilder.loadTexts:
    cLRogueClientExceededThreshold.setStatus(
        "current"
    )

cLRogueExceededClientRemovedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 0, 3)
)
cLRogueExceededClientRemovedThreshold.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApDot11RadioMACAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioChannelNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfSmtDot11Bssid"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRuleStateType"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueDetectedChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueDot11RadioBand"))
)
if mibBuilder.loadTexts:
    cLRogueExceededClientRemovedThreshold.setStatus(
        "current"
    )

cLRogueApRuleContained = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 0, 4)
)
cLRogueApRuleContained.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApRogueApMacAddress"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueApContainmentLevel"))
)
if mibBuilder.loadTexts:
    cLRogueApRuleContained.setStatus(
        "current"
    )

cLRogueClientDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 0, 5)
)
cLRogueClientDetected.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLLastDetectingRadioMACAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueMode"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueClientTotalDetectingAPs"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueClientFirstReported"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueClientLastReported"),
        ("CISCO-LWAPP-ROGUE-MIB", "cLRogueClientGatewayMac"))
)
if mibBuilder.loadTexts:
    cLRogueClientDetected.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappRogueNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2, 2)
)
ciscoLwappRogueNotifsGroup.setObjects(
    ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAdhocRogueDetected")
)
if mibBuilder.loadTexts:
    ciscoLwappRogueNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappRogueMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 1, 1)
)
ciscoLwappRogueMIBCompliance.setObjects(
      *(("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigGroup"),
        ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueNotifsGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappRogueMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappRogueMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 1, 2)
)
ciscoLwappRogueMIBComplianceRev1.setObjects(
      *(("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigGroup"),
        ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueNotifsGroup"),
        ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigSup1Group"))
)
if mibBuilder.loadTexts:
    ciscoLwappRogueMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoLwappRogueMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 1, 3)
)
ciscoLwappRogueMIBComplianceRev2.setObjects(
      *(("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigGroup"),
        ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueNotifsGroup"),
        ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigSup2Group"))
)
if mibBuilder.loadTexts:
    ciscoLwappRogueMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoLwappRogueMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 1, 4)
)
ciscoLwappRogueMIBComplianceRev3.setObjects(
      *(("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigGroup"),
        ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueNotifsGroup"),
        ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigSup3Group"))
)
if mibBuilder.loadTexts:
    ciscoLwappRogueMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoLwappRogueMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 1, 5)
)
ciscoLwappRogueMIBComplianceRev4.setObjects(
      *(("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigGroup"),
        ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueNotifsGroup"),
        ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigSup3Group"),
        ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigSup4Group"))
)
if mibBuilder.loadTexts:
    ciscoLwappRogueMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoLwappRogueMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 1, 6)
)
ciscoLwappRogueMIBComplianceRev5.setObjects(
      *(("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigGroup"),
        ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueNotifsGroup"),
        ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigSup3Group"),
        ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigSup4Group"),
        ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigSup5Group"))
)
if mibBuilder.loadTexts:
    ciscoLwappRogueMIBComplianceRev5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-ROGUE-MIB",
    **{"CLAutoContainActions": CLAutoContainActions,
       "ciscoLwappRogueMIB": ciscoLwappRogueMIB,
       "ciscoLwappRogueMIBNotifs": ciscoLwappRogueMIBNotifs,
       "cLRogueAdhocRogueDetected": cLRogueAdhocRogueDetected,
       "cLRogueClientExceededThreshold": cLRogueClientExceededThreshold,
       "cLRogueExceededClientRemovedThreshold": cLRogueExceededClientRemovedThreshold,
       "cLRogueApRuleContained": cLRogueApRuleContained,
       "cLRogueClientDetected": cLRogueClientDetected,
       "ciscoLwappRogueMIBObjects": ciscoLwappRogueMIBObjects,
       "cLRogueConfig": cLRogueConfig,
       "cLRoguePolicyConfig": cLRoguePolicyConfig,
       "cLRogueAdhocRogueReportEnable": cLRogueAdhocRogueReportEnable,
       "cLRogueReportInterval": cLRogueReportInterval,
       "cLRogueMinimumRssi": cLRogueMinimumRssi,
       "cLRogueTransientInterval": cLRogueTransientInterval,
       "cLRogueClientNumThreshold": cLRogueClientNumThreshold,
       "cLRogueDetectionSecurityLevel": cLRogueDetectionSecurityLevel,
       "cLRogueValidateRogueClientsAgainstMse": cLRogueValidateRogueClientsAgainstMse,
       "cLRogueValidateRogueApsAgainstAAA": cLRogueValidateRogueApsAgainstAAA,
       "cLRogueApPollingInterval": cLRogueApPollingInterval,
       "cLRogueContainAutoRateEnable": cLRogueContainAutoRateEnable,
       "cLRogueAdhocRogueNotifEnabled": cLRogueAdhocRogueNotifEnabled,
       "cLRogueRuleConfig": cLRogueRuleConfig,
       "cLRuleConfigTable": cLRuleConfigTable,
       "cLRuleConfigEntry": cLRuleConfigEntry,
       "cLRuleName": cLRuleName,
       "cLRuleRogueType": cLRuleRogueType,
       "cLRuleConditionsMatch": cLRuleConditionsMatch,
       "cLRulePriority": cLRulePriority,
       "cLRuleEnable": cLRuleEnable,
       "cLRuleStorageType": cLRuleStorageType,
       "cLRuleRowStatus": cLRuleRowStatus,
       "cLRuleSeverityScore": cLRuleSeverityScore,
       "cLRuleClassificationName": cLRuleClassificationName,
       "cLRuleNotifyType": cLRuleNotifyType,
       "cLRuleStateType": cLRuleStateType,
       "cLConditionConfigTable": cLConditionConfigTable,
       "cLConditionConfigEntry": cLConditionConfigEntry,
       "cLConditionName": cLConditionName,
       "cLConditionType": cLConditionType,
       "cLConditionValue": cLConditionValue,
       "cLConditionEnable": cLConditionEnable,
       "cLConditionStorageType": cLConditionStorageType,
       "cLConditionRowStatus": cLConditionRowStatus,
       "cLConditionRssi": cLConditionRssi,
       "cLConditionClientCount": cLConditionClientCount,
       "cLConditionNoEncryptionEnabled": cLConditionNoEncryptionEnabled,
       "cLConditionManagedSsidEnabled": cLConditionManagedSsidEnabled,
       "cLConditionDuration": cLConditionDuration,
       "cLConditionSsidConfigTable": cLConditionSsidConfigTable,
       "cLConditionSsidConfigEntry": cLConditionSsidConfigEntry,
       "cLConditionSsidValue": cLConditionSsidValue,
       "cLConditionSsidStorageType": cLConditionSsidStorageType,
       "cLConditionSsidRowStatus": cLConditionSsidRowStatus,
       "cLConditionSsidType": cLConditionSsidType,
       "cLRogueIgnoreListConfig": cLRogueIgnoreListConfig,
       "cLRogueIgnoreListTable": cLRogueIgnoreListTable,
       "cLRogueIgnoreListEntry": cLRogueIgnoreListEntry,
       "cLRogueIgnoreListMACAddress": cLRogueIgnoreListMACAddress,
       "cLRogueIgnoreListStorageType": cLRogueIgnoreListStorageType,
       "cLRogueIgnoreListRowStatus": cLRogueIgnoreListRowStatus,
       "cLRldpAutoContainConfig": cLRldpAutoContainConfig,
       "cLRldpAutoContainFeatureOnWiredNetwork": cLRldpAutoContainFeatureOnWiredNetwork,
       "cLRldpAutoContainRoguesAdvertisingSsid": cLRldpAutoContainRoguesAdvertisingSsid,
       "cLRldpAutoContainAdhocNetworks": cLRldpAutoContainAdhocNetworks,
       "cLRldpAutoContainTrustedClientsOnRogueAps": cLRldpAutoContainTrustedClientsOnRogueAps,
       "cLRldpAutoContainLevel": cLRldpAutoContainLevel,
       "cLRldpAutoContainOnlyforMonitorModeAps": cLRldpAutoContainOnlyforMonitorModeAps,
       "cLRldpAutoContainFlexStandaloneAp": cLRldpAutoContainFlexStandaloneAp,
       "cLRogueApConfig": cLRogueApConfig,
       "cLRogueApTable": cLRogueApTable,
       "cLRogueApEntry": cLRogueApEntry,
       "cLRogueApMACAddress": cLRogueApMACAddress,
       "cLRogueApClassType": cLRogueApClassType,
       "cLRogueApState": cLRogueApState,
       "cLRogueApStorageType": cLRogueApStorageType,
       "cLRogueApRowStatus": cLRogueApRowStatus,
       "cLRogueApListTable": cLRogueApListTable,
       "cLRogueApListEntry": cLRogueApListEntry,
       "cLRogueApMacAddr": cLRogueApMacAddr,
       "cLRogueApSeverityScore": cLRogueApSeverityScore,
       "cLRogueApRuleName": cLRogueApRuleName,
       "cLRogueApClassName": cLRogueApClassName,
       "cLRogueClientConfig": cLRogueClientConfig,
       "cLRogueClientTable": cLRogueClientTable,
       "cLRogueClientEntry": cLRogueClientEntry,
       "cLRogueClientMacAddress": cLRogueClientMacAddress,
       "cLRogueClientGatewayMacAddress": cLRogueClientGatewayMacAddress,
       "cLRogueApDetectingApDetails": cLRogueApDetectingApDetails,
       "cLRogueAPDetectingAPTable": cLRogueAPDetectingAPTable,
       "cLRogueAPDetectingAPEntry": cLRogueAPDetectingAPEntry,
       "cLRogueAPDetectingAPMacAddress": cLRogueAPDetectingAPMacAddress,
       "cLRogueAPDetectingAPSlotId": cLRogueAPDetectingAPSlotId,
       "cLRogueAPRadioType": cLRogueAPRadioType,
       "cLRogueAPDetectingAPName": cLRogueAPDetectingAPName,
       "cLRogueAPChannelNumber": cLRogueAPChannelNumber,
       "cLRogueAPSsid": cLRogueAPSsid,
       "cLRogueAPHiddenSsid": cLRogueAPHiddenSsid,
       "cLRogueAPDetectingAPRSSI": cLRogueAPDetectingAPRSSI,
       "cLRogueAPContainmentMode": cLRogueAPContainmentMode,
       "cLRogueAPContainmentChannelCount": cLRogueAPContainmentChannelCount,
       "cLRogueAPContainmentChannels": cLRogueAPContainmentChannels,
       "cLRogueAPDetectingAPLastHeard": cLRogueAPDetectingAPLastHeard,
       "cLRogueAPDetectingAPWepMode": cLRogueAPDetectingAPWepMode,
       "cLRogueAPDetectingAPPreamble": cLRogueAPDetectingAPPreamble,
       "cLRogueAPDetectingAPWpaMode": cLRogueAPDetectingAPWpaMode,
       "cLRogueAPDetectingAPWpa2Mode": cLRogueAPDetectingAPWpa2Mode,
       "cLRogueAPDetectingAPFTMode": cLRogueAPDetectingAPFTMode,
       "cLRogueAPDetectingAPSNR": cLRogueAPDetectingAPSNR,
       "cLRogueAPChannelWidth": cLRogueAPChannelWidth,
       "cLRogueAPPhysicalAPSlot": cLRogueAPPhysicalAPSlot,
       "ciscoLwappRogueMIBConform": ciscoLwappRogueMIBConform,
       "ciscoLwappRogueMIBCompliances": ciscoLwappRogueMIBCompliances,
       "ciscoLwappRogueMIBCompliance": ciscoLwappRogueMIBCompliance,
       "ciscoLwappRogueMIBComplianceRev1": ciscoLwappRogueMIBComplianceRev1,
       "ciscoLwappRogueMIBComplianceRev2": ciscoLwappRogueMIBComplianceRev2,
       "ciscoLwappRogueMIBComplianceRev3": ciscoLwappRogueMIBComplianceRev3,
       "ciscoLwappRogueMIBComplianceRev4": ciscoLwappRogueMIBComplianceRev4,
       "ciscoLwappRogueMIBComplianceRev5": ciscoLwappRogueMIBComplianceRev5,
       "ciscoLwappRogueMIBGroups": ciscoLwappRogueMIBGroups,
       "ciscoLwappRogueConfigGroup": ciscoLwappRogueConfigGroup,
       "ciscoLwappRogueNotifsGroup": ciscoLwappRogueNotifsGroup,
       "ciscoLwappRogueConfigSup1Group": ciscoLwappRogueConfigSup1Group,
       "ciscoLwappRogueConfigSup2Group": ciscoLwappRogueConfigSup2Group,
       "ciscoLwappRogueConfigSup3Group": ciscoLwappRogueConfigSup3Group,
       "ciscoLwappRogueConfigSup4Group": ciscoLwappRogueConfigSup4Group,
       "ciscoLwappRogueConfigSup5Group": ciscoLwappRogueConfigSup5Group,
       "ciscoLwappRogueMIBNotifObjects": ciscoLwappRogueMIBNotifObjects,
       "cLRogueApContainmentLevel": cLRogueApContainmentLevel,
       "cLRogueClientTotalDetectingAPs": cLRogueClientTotalDetectingAPs,
       "cLRogueClientFirstReported": cLRogueClientFirstReported,
       "cLRogueClientLastReported": cLRogueClientLastReported,
       "cLRogueClientGatewayMac": cLRogueClientGatewayMac,
       "cLLastDetectingRadioMACAddress": cLLastDetectingRadioMACAddress}
)

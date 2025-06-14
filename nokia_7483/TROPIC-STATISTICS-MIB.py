# SNMP MIB module (TROPIC-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-STATISTICS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:59:16 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(tnStatisticsMIB,
 tnSystemModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnStatisticsMIB",
    "tnSystemModules")

(tnOthIfIndex,
 tnOthIfIndexLo,
 tnOthOdukTcmIfIndex,
 tnOthOdukTcmIfIndexLo) = mibBuilder.importSymbols(
    "TROPIC-OTH-MIB",
    "tnOthIfIndex",
    "tnOthIfIndexLo",
    "tnOthOdukTcmIfIndex",
    "tnOthOdukTcmIfIndexLo")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")

(TnCommand,
 TnStatsProfileId) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "TnCommand",
    "TnStatsProfileId")


# MODULE-IDENTITY

tnStatisticsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tnStatisticsMibModule.setRevisions(
        ("2008-03-17 12:00",
         "2008-03-28 12:00",
         "2008-04-03 12:00",
         "2008-04-05 12:00",
         "2008-04-08 12:00",
         "2008-11-06 12:00",
         "2009-02-26 12:00",
         "2009-07-07 12:00",
         "2009-09-01 12:00",
         "2009-12-08 12:00",
         "2010-03-05 12:00",
         "2010-05-17 12:00",
         "2010-06-07 12:00",
         "2010-06-30 12:00",
         "2010-07-29 12:00",
         "2010-08-02 12:00",
         "2010-08-05 12:00",
         "2010-08-26 12:00",
         "2010-10-14 12:00",
         "2010-10-18 12:00",
         "2010-11-23 12:00",
         "2010-11-28 12:00",
         "2011-05-02 12:00",
         "2012-03-10 12:00",
         "2012-07-24 12:00",
         "2012-08-21 12:00",
         "2012-08-22 12:00",
         "2012-08-28 12:00",
         "2012-08-31 12:00",
         "2012-10-16 12:00",
         "2012-10-22 12:00",
         "2012-11-05 12:00",
         "2012-11-12 12:00",
         "2013-05-24 12:00",
         "2013-08-05 12:00",
         "2013-11-22 12:00",
         "2013-12-06 12:00",
         "2013-12-10 12:00",
         "2014-08-29 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TnStatsGroupId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class TnStatsIntervalType(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class TnStatsBinType(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class TnStatsBinStatus(TextualConvention, Integer32):
    status = "current"
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("rxValid", 2),
          ("txValid", 3),
          ("invalid", 4),
          ("dataNotAvailable", 5),
          ("partial", 6),
          ("adjusted", 7),
          ("dataLong", 8),
          ("dataComplete", 9),
          ("disabled", 10))
    )



# MIB Managed Objects in the order of their OIDs

_TnStatisticsConf_ObjectIdentity = ObjectIdentity
tnStatisticsConf = _TnStatisticsConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1)
)
_TnStatisticsGroups_ObjectIdentity = ObjectIdentity
tnStatisticsGroups = _TnStatisticsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1)
)
_TnStatisticsCompliances_ObjectIdentity = ObjectIdentity
tnStatisticsCompliances = _TnStatisticsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 2)
)
_TnStatisticsObjs_ObjectIdentity = ObjectIdentity
tnStatisticsObjs = _TnStatisticsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2)
)
_TnStatisticsTCA_ObjectIdentity = ObjectIdentity
tnStatisticsTCA = _TnStatisticsTCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1)
)
_TnStatsPortIntervalTable_Object = MibTable
tnStatsPortIntervalTable = _TnStatsPortIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnStatsPortIntervalTable.setStatus("current")
_TnStatsPortIntervalEntry_Object = MibTableRow
tnStatsPortIntervalEntry = _TnStatsPortIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 1, 1)
)
tnStatsPortIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsGroupId"),
)
if mibBuilder.loadTexts:
    tnStatsPortIntervalEntry.setStatus("current")
_TnStatsPortNumberOfIntervals_Type = TnStatsIntervalType
_TnStatsPortNumberOfIntervals_Object = MibTableColumn
tnStatsPortNumberOfIntervals = _TnStatsPortNumberOfIntervals_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 1, 1, 1),
    _TnStatsPortNumberOfIntervals_Type()
)
tnStatsPortNumberOfIntervals.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnStatsPortNumberOfIntervals.setStatus("current")
_TnStatsCardIntervalTable_Object = MibTable
tnStatsCardIntervalTable = _TnStatsCardIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnStatsCardIntervalTable.setStatus("current")
_TnStatsCardIntervalEntry_Object = MibTableRow
tnStatsCardIntervalEntry = _TnStatsCardIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 2, 1)
)
tnStatsCardIntervalEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsGroupId"),
)
if mibBuilder.loadTexts:
    tnStatsCardIntervalEntry.setStatus("current")
_TnStatsCardNumberOfIntervals_Type = TnStatsIntervalType
_TnStatsCardNumberOfIntervals_Object = MibTableColumn
tnStatsCardNumberOfIntervals = _TnStatsCardNumberOfIntervals_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 2, 1, 1),
    _TnStatsCardNumberOfIntervals_Type()
)
tnStatsCardNumberOfIntervals.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnStatsCardNumberOfIntervals.setStatus("current")
_TnStatsPortTable_Object = MibTable
tnStatsPortTable = _TnStatsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tnStatsPortTable.setStatus("current")
_TnStatsPortEntry_Object = MibTableRow
tnStatsPortEntry = _TnStatsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 3, 1)
)
tnStatsPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsGroupId"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
)
if mibBuilder.loadTexts:
    tnStatsPortEntry.setStatus("current")
_TnStatsInterval_Type = TnStatsIntervalType
_TnStatsInterval_Object = MibTableColumn
tnStatsInterval = _TnStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 3, 1, 1),
    _TnStatsInterval_Type()
)
tnStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnStatsInterval.setStatus("current")
_TnStatsPortIntervalLength_Type = Unsigned32
_TnStatsPortIntervalLength_Object = MibTableColumn
tnStatsPortIntervalLength = _TnStatsPortIntervalLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 3, 1, 2),
    _TnStatsPortIntervalLength_Type()
)
tnStatsPortIntervalLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnStatsPortIntervalLength.setStatus("current")
if mibBuilder.loadTexts:
    tnStatsPortIntervalLength.setUnits("seconds")
_TnStatsPortNumberOfBins_Type = TnStatsBinType
_TnStatsPortNumberOfBins_Object = MibTableColumn
tnStatsPortNumberOfBins = _TnStatsPortNumberOfBins_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 3, 1, 3),
    _TnStatsPortNumberOfBins_Type()
)
tnStatsPortNumberOfBins.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnStatsPortNumberOfBins.setStatus("current")
_TnStatsPortProfileId_Type = TnStatsProfileId
_TnStatsPortProfileId_Object = MibTableColumn
tnStatsPortProfileId = _TnStatsPortProfileId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 3, 1, 4),
    _TnStatsPortProfileId_Type()
)
tnStatsPortProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnStatsPortProfileId.setStatus("current")
_TnStatsPortClear_Type = TnCommand
_TnStatsPortClear_Object = MibTableColumn
tnStatsPortClear = _TnStatsPortClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 3, 1, 5),
    _TnStatsPortClear_Type()
)
tnStatsPortClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnStatsPortClear.setStatus("current")
_TnStatsCardTable_Object = MibTable
tnStatsCardTable = _TnStatsCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tnStatsCardTable.setStatus("current")
_TnStatsCardEntry_Object = MibTableRow
tnStatsCardEntry = _TnStatsCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 4, 1)
)
tnStatsCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsGroupId"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
)
if mibBuilder.loadTexts:
    tnStatsCardEntry.setStatus("current")
_TnStatsCardIntervalLength_Type = Unsigned32
_TnStatsCardIntervalLength_Object = MibTableColumn
tnStatsCardIntervalLength = _TnStatsCardIntervalLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 4, 1, 1),
    _TnStatsCardIntervalLength_Type()
)
tnStatsCardIntervalLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnStatsCardIntervalLength.setStatus("current")
if mibBuilder.loadTexts:
    tnStatsCardIntervalLength.setUnits("seconds")
_TnStatsCardNumberOfBins_Type = TnStatsBinType
_TnStatsCardNumberOfBins_Object = MibTableColumn
tnStatsCardNumberOfBins = _TnStatsCardNumberOfBins_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 4, 1, 2),
    _TnStatsCardNumberOfBins_Type()
)
tnStatsCardNumberOfBins.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnStatsCardNumberOfBins.setStatus("current")
_TnStatsCardProfileId_Type = TnStatsProfileId
_TnStatsCardProfileId_Object = MibTableColumn
tnStatsCardProfileId = _TnStatsCardProfileId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 4, 1, 3),
    _TnStatsCardProfileId_Type()
)
tnStatsCardProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnStatsCardProfileId.setStatus("current")
_TnStatsCardClear_Type = TnCommand
_TnStatsCardClear_Object = MibTableColumn
tnStatsCardClear = _TnStatsCardClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 4, 1, 4),
    _TnStatsCardClear_Type()
)
tnStatsCardClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnStatsCardClear.setStatus("current")
_TnStatsTCAProfileTable_Object = MibTable
tnStatsTCAProfileTable = _TnStatsTCAProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tnStatsTCAProfileTable.setStatus("current")
_TnStatsTCAProfileEntry_Object = MibTableRow
tnStatsTCAProfileEntry = _TnStatsTCAProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 5, 1)
)
tnStatsTCAProfileEntry.setIndexNames(
    (0, "TROPIC-STATISTICS-MIB", "tnStatsGroupId"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsTCAProfileId"),
)
if mibBuilder.loadTexts:
    tnStatsTCAProfileEntry.setStatus("current")
_TnStatsGroupId_Type = TnStatsGroupId
_TnStatsGroupId_Object = MibTableColumn
tnStatsGroupId = _TnStatsGroupId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 5, 1, 1),
    _TnStatsGroupId_Type()
)
tnStatsGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnStatsGroupId.setStatus("current")
_TnStatsTCAProfileId_Type = TnStatsProfileId
_TnStatsTCAProfileId_Object = MibTableColumn
tnStatsTCAProfileId = _TnStatsTCAProfileId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 5, 1, 2),
    _TnStatsTCAProfileId_Type()
)
tnStatsTCAProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnStatsTCAProfileId.setStatus("current")


class _TnStatsTCAProfileDescr_Type(SnmpAdminString):
    """Custom type tnStatsTCAProfileDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnStatsTCAProfileDescr_Type.__name__ = "SnmpAdminString"
_TnStatsTCAProfileDescr_Object = MibTableColumn
tnStatsTCAProfileDescr = _TnStatsTCAProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 5, 1, 3),
    _TnStatsTCAProfileDescr_Type()
)
tnStatsTCAProfileDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnStatsTCAProfileDescr.setStatus("current")
_TnStatsTCATable_Object = MibTable
tnStatsTCATable = _TnStatsTCATable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tnStatsTCATable.setStatus("current")
_TnStatsTCAEntry_Object = MibTableRow
tnStatsTCAEntry = _TnStatsTCAEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 6, 1)
)
tnStatsTCAEntry.setIndexNames(
    (0, "TROPIC-STATISTICS-MIB", "tnStatsGroupId"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsTCAProfileId"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsTCAVariableId"),
)
if mibBuilder.loadTexts:
    tnStatsTCAEntry.setStatus("current")
_TnStatsTCAVariableId_Type = Unsigned32
_TnStatsTCAVariableId_Object = MibTableColumn
tnStatsTCAVariableId = _TnStatsTCAVariableId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 6, 1, 1),
    _TnStatsTCAVariableId_Type()
)
tnStatsTCAVariableId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnStatsTCAVariableId.setStatus("current")
_TnStatsTCAVariable_Type = ObjectIdentifier
_TnStatsTCAVariable_Object = MibTableColumn
tnStatsTCAVariable = _TnStatsTCAVariable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 6, 1, 2),
    _TnStatsTCAVariable_Type()
)
tnStatsTCAVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsTCAVariable.setStatus("current")


class _TnStatsTCAValue_Type(SnmpAdminString):
    """Custom type tnStatsTCAValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TnStatsTCAValue_Type.__name__ = "SnmpAdminString"
_TnStatsTCAValue_Object = MibTableColumn
tnStatsTCAValue = _TnStatsTCAValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 6, 1, 7),
    _TnStatsTCAValue_Type()
)
tnStatsTCAValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnStatsTCAValue.setStatus("current")
_TnStatsTCAItuTable_Object = MibTable
tnStatsTCAItuTable = _TnStatsTCAItuTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tnStatsTCAItuTable.setStatus("current")
_TnStatsTCAItuEntry_Object = MibTableRow
tnStatsTCAItuEntry = _TnStatsTCAItuEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 7, 1)
)
tnStatsTCAItuEntry.setIndexNames(
    (0, "TROPIC-STATISTICS-MIB", "tnStatsGroupId"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsTCAProfileId"),
    (0, "TROPIC-STATISTICS-MIB", "tnOpticalStatsITUChannel"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsTCAVariableId"),
)
if mibBuilder.loadTexts:
    tnStatsTCAItuEntry.setStatus("current")
_TnOpticalStatsITUChannel_Type = Unsigned32
_TnOpticalStatsITUChannel_Object = MibTableColumn
tnOpticalStatsITUChannel = _TnOpticalStatsITUChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 7, 1, 1),
    _TnOpticalStatsITUChannel_Type()
)
tnOpticalStatsITUChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOpticalStatsITUChannel.setStatus("current")
_TnStatsPortClearAllTable_Object = MibTable
tnStatsPortClearAllTable = _TnStatsPortClearAllTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    tnStatsPortClearAllTable.setStatus("current")
_TnStatsPortClearAllEntry_Object = MibTableRow
tnStatsPortClearAllEntry = _TnStatsPortClearAllEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 8, 1)
)
tnStatsPortClearAllEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnStatsPortClearAllEntry.setStatus("current")
_TnStatsPortClearAll_Type = TnCommand
_TnStatsPortClearAll_Object = MibTableColumn
tnStatsPortClearAll = _TnStatsPortClearAll_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 8, 1, 1),
    _TnStatsPortClearAll_Type()
)
tnStatsPortClearAll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnStatsPortClearAll.setStatus("current")
_TnStatsClearAll_Type = TnCommand
_TnStatsClearAll_Object = MibScalar
tnStatsClearAll = _TnStatsClearAll_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 9),
    _TnStatsClearAll_Type()
)
tnStatsClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnStatsClearAll.setStatus("current")
_TnOthOdukStatsRxConfigAttributeTotal_Type = Integer32
_TnOthOdukStatsRxConfigAttributeTotal_Object = MibScalar
tnOthOdukStatsRxConfigAttributeTotal = _TnOthOdukStatsRxConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 16),
    _TnOthOdukStatsRxConfigAttributeTotal_Type()
)
tnOthOdukStatsRxConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsRxConfigAttributeTotal.setStatus("current")
_TnOthOdukStatsRxConfigTable_Object = MibTable
tnOthOdukStatsRxConfigTable = _TnOthOdukStatsRxConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 17)
)
if mibBuilder.loadTexts:
    tnOthOdukStatsRxConfigTable.setStatus("current")
_TnOthOdukStatsRxConfigEntry_Object = MibTableRow
tnOthOdukStatsRxConfigEntry = _TnOthOdukStatsRxConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 17, 1)
)
tnOthOdukStatsRxConfigEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
)
if mibBuilder.loadTexts:
    tnOthOdukStatsRxConfigEntry.setStatus("current")
_TnOthOdukStatsRxNumberofBins_Type = TnStatsBinType
_TnOthOdukStatsRxNumberofBins_Object = MibTableColumn
tnOthOdukStatsRxNumberofBins = _TnOthOdukStatsRxNumberofBins_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 17, 1, 1),
    _TnOthOdukStatsRxNumberofBins_Type()
)
tnOthOdukStatsRxNumberofBins.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStatsRxNumberofBins.setStatus("current")
_TnOthOdukStatsRxProfileid_Type = TnStatsProfileId
_TnOthOdukStatsRxProfileid_Object = MibTableColumn
tnOthOdukStatsRxProfileid = _TnOthOdukStatsRxProfileid_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 17, 1, 2),
    _TnOthOdukStatsRxProfileid_Type()
)
tnOthOdukStatsRxProfileid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStatsRxProfileid.setStatus("current")
_TnOthOdukStatsRxClear_Type = TnCommand
_TnOthOdukStatsRxClear_Object = MibTableColumn
tnOthOdukStatsRxClear = _TnOthOdukStatsRxClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 17, 1, 3),
    _TnOthOdukStatsRxClear_Type()
)
tnOthOdukStatsRxClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStatsRxClear.setStatus("current")
_TnOthOdukStatsRxIntervalLength_Type = Unsigned32
_TnOthOdukStatsRxIntervalLength_Object = MibTableColumn
tnOthOdukStatsRxIntervalLength = _TnOthOdukStatsRxIntervalLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 17, 1, 4),
    _TnOthOdukStatsRxIntervalLength_Type()
)
tnOthOdukStatsRxIntervalLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStatsRxIntervalLength.setStatus("current")
if mibBuilder.loadTexts:
    tnOthOdukStatsRxIntervalLength.setUnits("seconds")
_TnOthOdukStatsTxConfigAttributeTotal_Type = Integer32
_TnOthOdukStatsTxConfigAttributeTotal_Object = MibScalar
tnOthOdukStatsTxConfigAttributeTotal = _TnOthOdukStatsTxConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 18),
    _TnOthOdukStatsTxConfigAttributeTotal_Type()
)
tnOthOdukStatsTxConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTxConfigAttributeTotal.setStatus("current")
_TnOthOdukStatsTxConfigTable_Object = MibTable
tnOthOdukStatsTxConfigTable = _TnOthOdukStatsTxConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 19)
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTxConfigTable.setStatus("current")
_TnOthOdukStatsTxConfigEntry_Object = MibTableRow
tnOthOdukStatsTxConfigEntry = _TnOthOdukStatsTxConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 19, 1)
)
tnOthOdukStatsTxConfigEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTxConfigEntry.setStatus("current")
_TnOthOdukStatsTxNumberofBins_Type = TnStatsBinType
_TnOthOdukStatsTxNumberofBins_Object = MibTableColumn
tnOthOdukStatsTxNumberofBins = _TnOthOdukStatsTxNumberofBins_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 19, 1, 1),
    _TnOthOdukStatsTxNumberofBins_Type()
)
tnOthOdukStatsTxNumberofBins.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStatsTxNumberofBins.setStatus("current")
_TnOthOdukStatsTxProfileid_Type = TnStatsProfileId
_TnOthOdukStatsTxProfileid_Object = MibTableColumn
tnOthOdukStatsTxProfileid = _TnOthOdukStatsTxProfileid_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 19, 1, 2),
    _TnOthOdukStatsTxProfileid_Type()
)
tnOthOdukStatsTxProfileid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStatsTxProfileid.setStatus("current")
_TnOthOdukStatsTxClear_Type = TnCommand
_TnOthOdukStatsTxClear_Object = MibTableColumn
tnOthOdukStatsTxClear = _TnOthOdukStatsTxClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 19, 1, 3),
    _TnOthOdukStatsTxClear_Type()
)
tnOthOdukStatsTxClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStatsTxClear.setStatus("current")
_TnOthOdukStatsTxIntervalLength_Type = Unsigned32
_TnOthOdukStatsTxIntervalLength_Object = MibTableColumn
tnOthOdukStatsTxIntervalLength = _TnOthOdukStatsTxIntervalLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 19, 1, 4),
    _TnOthOdukStatsTxIntervalLength_Type()
)
tnOthOdukStatsTxIntervalLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStatsTxIntervalLength.setStatus("current")
if mibBuilder.loadTexts:
    tnOthOdukStatsTxIntervalLength.setUnits("seconds")
_TnOthOdukStatsControlAttributeTotal_Type = Integer32
_TnOthOdukStatsControlAttributeTotal_Object = MibScalar
tnOthOdukStatsControlAttributeTotal = _TnOthOdukStatsControlAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 20),
    _TnOthOdukStatsControlAttributeTotal_Type()
)
tnOthOdukStatsControlAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsControlAttributeTotal.setStatus("current")
_TnOthOdukStatsControlTable_Object = MibTable
tnOthOdukStatsControlTable = _TnOthOdukStatsControlTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 21)
)
if mibBuilder.loadTexts:
    tnOthOdukStatsControlTable.setStatus("current")
_TnOthOdukStatsControlEntry_Object = MibTableRow
tnOthOdukStatsControlEntry = _TnOthOdukStatsControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 21, 1)
)
tnOthOdukStatsControlEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnOthOdukStatsControlEntry.setStatus("current")
_TnOthOdukStatsClearAll_Type = TnCommand
_TnOthOdukStatsClearAll_Object = MibTableColumn
tnOthOdukStatsClearAll = _TnOthOdukStatsClearAll_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 21, 1, 1),
    _TnOthOdukStatsClearAll_Type()
)
tnOthOdukStatsClearAll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStatsClearAll.setStatus("current")


class _TnOthOdukStatsRxEnable_Type(Integer32):
    """Custom type tnOthOdukStatsRxEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnOthOdukStatsRxEnable_Type.__name__ = "Integer32"
_TnOthOdukStatsRxEnable_Object = MibTableColumn
tnOthOdukStatsRxEnable = _TnOthOdukStatsRxEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 21, 1, 2),
    _TnOthOdukStatsRxEnable_Type()
)
tnOthOdukStatsRxEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStatsRxEnable.setStatus("current")


class _TnOthOdukStatsTxEnable_Type(Integer32):
    """Custom type tnOthOdukStatsTxEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnOthOdukStatsTxEnable_Type.__name__ = "Integer32"
_TnOthOdukStatsTxEnable_Object = MibTableColumn
tnOthOdukStatsTxEnable = _TnOthOdukStatsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 21, 1, 3),
    _TnOthOdukStatsTxEnable_Type()
)
tnOthOdukStatsTxEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStatsTxEnable.setStatus("current")
_TnOthOdukStatsDMConfigAttributeTotal_Type = Integer32
_TnOthOdukStatsDMConfigAttributeTotal_Object = MibScalar
tnOthOdukStatsDMConfigAttributeTotal = _TnOthOdukStatsDMConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 22),
    _TnOthOdukStatsDMConfigAttributeTotal_Type()
)
tnOthOdukStatsDMConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsDMConfigAttributeTotal.setStatus("current")
_TnOthOdukStatsDMConfigTable_Object = MibTable
tnOthOdukStatsDMConfigTable = _TnOthOdukStatsDMConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 23)
)
if mibBuilder.loadTexts:
    tnOthOdukStatsDMConfigTable.setStatus("current")
_TnOthOdukStatsDMConfigEntry_Object = MibTableRow
tnOthOdukStatsDMConfigEntry = _TnOthOdukStatsDMConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 23, 1)
)
tnOthOdukStatsDMConfigEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
)
if mibBuilder.loadTexts:
    tnOthOdukStatsDMConfigEntry.setStatus("current")
_TnOthOdukStatsDMNumberofBins_Type = TnStatsBinType
_TnOthOdukStatsDMNumberofBins_Object = MibTableColumn
tnOthOdukStatsDMNumberofBins = _TnOthOdukStatsDMNumberofBins_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 23, 1, 1),
    _TnOthOdukStatsDMNumberofBins_Type()
)
tnOthOdukStatsDMNumberofBins.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStatsDMNumberofBins.setStatus("current")
_TnOthOdukStatsDMProfileid_Type = TnStatsProfileId
_TnOthOdukStatsDMProfileid_Object = MibTableColumn
tnOthOdukStatsDMProfileid = _TnOthOdukStatsDMProfileid_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 23, 1, 2),
    _TnOthOdukStatsDMProfileid_Type()
)
tnOthOdukStatsDMProfileid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStatsDMProfileid.setStatus("current")
_TnOthOdukStatsDMClear_Type = TnCommand
_TnOthOdukStatsDMClear_Object = MibTableColumn
tnOthOdukStatsDMClear = _TnOthOdukStatsDMClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 23, 1, 3),
    _TnOthOdukStatsDMClear_Type()
)
tnOthOdukStatsDMClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStatsDMClear.setStatus("current")
_TnOthOdukStatsDMIntervalLength_Type = Unsigned32
_TnOthOdukStatsDMIntervalLength_Object = MibTableColumn
tnOthOdukStatsDMIntervalLength = _TnOthOdukStatsDMIntervalLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 23, 1, 4),
    _TnOthOdukStatsDMIntervalLength_Type()
)
tnOthOdukStatsDMIntervalLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStatsDMIntervalLength.setStatus("current")
if mibBuilder.loadTexts:
    tnOthOdukStatsDMIntervalLength.setUnits("seconds")
_TnOthOdukStatsTcmConfigAttributeTotal_Type = Integer32
_TnOthOdukStatsTcmConfigAttributeTotal_Object = MibScalar
tnOthOdukStatsTcmConfigAttributeTotal = _TnOthOdukStatsTcmConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 24),
    _TnOthOdukStatsTcmConfigAttributeTotal_Type()
)
tnOthOdukStatsTcmConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmConfigAttributeTotal.setStatus("current")
_TnOthOdukStatsTcmConfigTable_Object = MibTable
tnOthOdukStatsTcmConfigTable = _TnOthOdukStatsTcmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 25)
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmConfigTable.setStatus("current")
_TnOthOdukStatsTcmConfigEntry_Object = MibTableRow
tnOthOdukStatsTcmConfigEntry = _TnOthOdukStatsTcmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 25, 1)
)
tnOthOdukStatsTcmConfigEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthOdukTcmIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthOdukTcmIfIndexLo"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmConfigEntry.setStatus("current")
_TnOthOdukStatsTcmConfigNumberOfBins_Type = TnStatsBinType
_TnOthOdukStatsTcmConfigNumberOfBins_Object = MibTableColumn
tnOthOdukStatsTcmConfigNumberOfBins = _TnOthOdukStatsTcmConfigNumberOfBins_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 25, 1, 1),
    _TnOthOdukStatsTcmConfigNumberOfBins_Type()
)
tnOthOdukStatsTcmConfigNumberOfBins.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmConfigNumberOfBins.setStatus("current")
_TnOthOdukStatsTcmConfigProfileId_Type = TnStatsProfileId
_TnOthOdukStatsTcmConfigProfileId_Object = MibTableColumn
tnOthOdukStatsTcmConfigProfileId = _TnOthOdukStatsTcmConfigProfileId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 25, 1, 2),
    _TnOthOdukStatsTcmConfigProfileId_Type()
)
tnOthOdukStatsTcmConfigProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmConfigProfileId.setStatus("current")
_TnOthOdukStatsTcmConfigClear_Type = TnCommand
_TnOthOdukStatsTcmConfigClear_Object = MibTableColumn
tnOthOdukStatsTcmConfigClear = _TnOthOdukStatsTcmConfigClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 25, 1, 3),
    _TnOthOdukStatsTcmConfigClear_Type()
)
tnOthOdukStatsTcmConfigClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmConfigClear.setStatus("current")
_TnOthOdukStatsTcmEnableAttributeTotal_Type = Integer32
_TnOthOdukStatsTcmEnableAttributeTotal_Object = MibScalar
tnOthOdukStatsTcmEnableAttributeTotal = _TnOthOdukStatsTcmEnableAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 26),
    _TnOthOdukStatsTcmEnableAttributeTotal_Type()
)
tnOthOdukStatsTcmEnableAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmEnableAttributeTotal.setStatus("current")
_TnOthOdukStatsTcmEnableTable_Object = MibTable
tnOthOdukStatsTcmEnableTable = _TnOthOdukStatsTcmEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 27)
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmEnableTable.setStatus("current")
_TnOthOdukStatsTcmEnableEntry_Object = MibTableRow
tnOthOdukStatsTcmEnableEntry = _TnOthOdukStatsTcmEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 27, 1)
)
tnOthOdukStatsTcmEnableEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthOdukTcmIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthOdukTcmIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmEnableEntry.setStatus("current")
_TnOthOdukStatsTcmClearAll_Type = TnCommand
_TnOthOdukStatsTcmClearAll_Object = MibTableColumn
tnOthOdukStatsTcmClearAll = _TnOthOdukStatsTcmClearAll_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 27, 1, 1),
    _TnOthOdukStatsTcmClearAll_Type()
)
tnOthOdukStatsTcmClearAll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmClearAll.setStatus("current")


class _TnOthOdukStatsTcmEnable_Type(Integer32):
    """Custom type tnOthOdukStatsTcmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnOthOdukStatsTcmEnable_Type.__name__ = "Integer32"
_TnOthOdukStatsTcmEnable_Object = MibTableColumn
tnOthOdukStatsTcmEnable = _TnOthOdukStatsTcmEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 27, 1, 2),
    _TnOthOdukStatsTcmEnable_Type()
)
tnOthOdukStatsTcmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmEnable.setStatus("current")
_TnStatsLanePwrsConfigAttributeTotal_Type = Integer32
_TnStatsLanePwrsConfigAttributeTotal_Object = MibScalar
tnStatsLanePwrsConfigAttributeTotal = _TnStatsLanePwrsConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 28),
    _TnStatsLanePwrsConfigAttributeTotal_Type()
)
tnStatsLanePwrsConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsLanePwrsConfigAttributeTotal.setStatus("current")
_TnStatsLanePwrsConfigTable_Object = MibTable
tnStatsLanePwrsConfigTable = _TnStatsLanePwrsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 29)
)
if mibBuilder.loadTexts:
    tnStatsLanePwrsConfigTable.setStatus("current")
_TnStatsLanePwrsConfigEntry_Object = MibTableRow
tnStatsLanePwrsConfigEntry = _TnStatsLanePwrsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 29, 1)
)
tnStatsLanePwrsConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnStatsLanePwrsConfigEntry.setStatus("current")
_TnStatsLanePwrsConfigProfileId_Type = TnStatsProfileId
_TnStatsLanePwrsConfigProfileId_Object = MibTableColumn
tnStatsLanePwrsConfigProfileId = _TnStatsLanePwrsConfigProfileId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 1, 29, 1, 1),
    _TnStatsLanePwrsConfigProfileId_Type()
)
tnStatsLanePwrsConfigProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnStatsLanePwrsConfigProfileId.setStatus("current")
_TnStatisticsGrouping_ObjectIdentity = ObjectIdentity
tnStatisticsGrouping = _TnStatisticsGrouping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2)
)
_TnCardStatsTotalMembers_Type = Integer32
_TnCardStatsTotalMembers_Object = MibScalar
tnCardStatsTotalMembers = _TnCardStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 1),
    _TnCardStatsTotalMembers_Type()
)
tnCardStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardStatsTotalMembers.setStatus("current")
_TnCardStatsTable_Object = MibTable
tnCardStatsTable = _TnCardStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tnCardStatsTable.setStatus("current")
_TnCardStatsEntry_Object = MibTableRow
tnCardStatsEntry = _TnCardStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 2, 1)
)
tnCardStatsEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnCardStatsProcessor"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnCardStatsBin"),
)
if mibBuilder.loadTexts:
    tnCardStatsEntry.setStatus("current")
_TnCardStatsProcessor_Type = Unsigned32
_TnCardStatsProcessor_Object = MibTableColumn
tnCardStatsProcessor = _TnCardStatsProcessor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 2, 1, 1),
    _TnCardStatsProcessor_Type()
)
tnCardStatsProcessor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCardStatsProcessor.setStatus("current")
_TnCardStatsBin_Type = TnStatsBinType
_TnCardStatsBin_Object = MibTableColumn
tnCardStatsBin = _TnCardStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 2, 1, 2),
    _TnCardStatsBin_Type()
)
tnCardStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCardStatsBin.setStatus("current")
_TnCardStatsBinStatus_Type = TnStatsBinStatus
_TnCardStatsBinStatus_Object = MibTableColumn
tnCardStatsBinStatus = _TnCardStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 2, 1, 3),
    _TnCardStatsBinStatus_Type()
)
tnCardStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardStatsBinStatus.setStatus("current")
_TnCardStatsStartTime_Type = DateAndTime
_TnCardStatsStartTime_Object = MibTableColumn
tnCardStatsStartTime = _TnCardStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 2, 1, 4),
    _TnCardStatsStartTime_Type()
)
tnCardStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardStatsStartTime.setStatus("current")
_TnCardStatCpuAverage_Type = Counter32
_TnCardStatCpuAverage_Object = MibTableColumn
tnCardStatCpuAverage = _TnCardStatCpuAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 2, 1, 5),
    _TnCardStatCpuAverage_Type()
)
tnCardStatCpuAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardStatCpuAverage.setStatus("current")
_TnCardStatHeapUsage_Type = Counter32
_TnCardStatHeapUsage_Object = MibTableColumn
tnCardStatHeapUsage = _TnCardStatHeapUsage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 2, 1, 6),
    _TnCardStatHeapUsage_Type()
)
tnCardStatHeapUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardStatHeapUsage.setStatus("current")
_TnCardStatPoolUsage_Type = Counter32
_TnCardStatPoolUsage_Object = MibTableColumn
tnCardStatPoolUsage = _TnCardStatPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 2, 1, 7),
    _TnCardStatPoolUsage_Type()
)
tnCardStatPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardStatPoolUsage.setStatus("current")
_TnInterfaceStatsTotalMembers_Type = Integer32
_TnInterfaceStatsTotalMembers_Object = MibScalar
tnInterfaceStatsTotalMembers = _TnInterfaceStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 3),
    _TnInterfaceStatsTotalMembers_Type()
)
tnInterfaceStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnInterfaceStatsTotalMembers.setStatus("current")
_TnInterfaceStatsTable_Object = MibTable
tnInterfaceStatsTable = _TnInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    tnInterfaceStatsTable.setStatus("current")
_TnInterfaceStatsEntry_Object = MibTableRow
tnInterfaceStatsEntry = _TnInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 4, 1)
)
tnInterfaceStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnIfStatsBin"),
)
if mibBuilder.loadTexts:
    tnInterfaceStatsEntry.setStatus("current")
_TnIfStatsBin_Type = TnStatsBinType
_TnIfStatsBin_Object = MibTableColumn
tnIfStatsBin = _TnIfStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 4, 1, 1),
    _TnIfStatsBin_Type()
)
tnIfStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIfStatsBin.setStatus("current")
_TnIfStatsBinStatus_Type = TnStatsBinStatus
_TnIfStatsBinStatus_Object = MibTableColumn
tnIfStatsBinStatus = _TnIfStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 4, 1, 2),
    _TnIfStatsBinStatus_Type()
)
tnIfStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfStatsBinStatus.setStatus("current")
_TnIfStatsStartTime_Type = DateAndTime
_TnIfStatsStartTime_Object = MibTableColumn
tnIfStatsStartTime = _TnIfStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 4, 1, 3),
    _TnIfStatsStartTime_Type()
)
tnIfStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfStatsStartTime.setStatus("current")
_TnIfStatInOctets_Type = Counter64
_TnIfStatInOctets_Object = MibTableColumn
tnIfStatInOctets = _TnIfStatInOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 4, 1, 4),
    _TnIfStatInOctets_Type()
)
tnIfStatInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfStatInOctets.setStatus("current")
_TnIfStatInUcastPkts_Type = Counter64
_TnIfStatInUcastPkts_Object = MibTableColumn
tnIfStatInUcastPkts = _TnIfStatInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 4, 1, 5),
    _TnIfStatInUcastPkts_Type()
)
tnIfStatInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfStatInUcastPkts.setStatus("current")
_TnIfStatInDiscards_Type = Counter64
_TnIfStatInDiscards_Object = MibTableColumn
tnIfStatInDiscards = _TnIfStatInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 4, 1, 6),
    _TnIfStatInDiscards_Type()
)
tnIfStatInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfStatInDiscards.setStatus("current")
_TnIfStatInErrors_Type = Counter64
_TnIfStatInErrors_Object = MibTableColumn
tnIfStatInErrors = _TnIfStatInErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 4, 1, 7),
    _TnIfStatInErrors_Type()
)
tnIfStatInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfStatInErrors.setStatus("current")
_TnIfStatInUnknownProtos_Type = Counter64
_TnIfStatInUnknownProtos_Object = MibTableColumn
tnIfStatInUnknownProtos = _TnIfStatInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 4, 1, 8),
    _TnIfStatInUnknownProtos_Type()
)
tnIfStatInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfStatInUnknownProtos.setStatus("current")
_TnIfStatOutOctets_Type = Counter64
_TnIfStatOutOctets_Object = MibTableColumn
tnIfStatOutOctets = _TnIfStatOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 4, 1, 9),
    _TnIfStatOutOctets_Type()
)
tnIfStatOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfStatOutOctets.setStatus("current")
_TnIfStatOutUcastPkts_Type = Counter64
_TnIfStatOutUcastPkts_Object = MibTableColumn
tnIfStatOutUcastPkts = _TnIfStatOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 4, 1, 10),
    _TnIfStatOutUcastPkts_Type()
)
tnIfStatOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfStatOutUcastPkts.setStatus("current")
_TnIfStatOutDiscards_Type = Counter64
_TnIfStatOutDiscards_Object = MibTableColumn
tnIfStatOutDiscards = _TnIfStatOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 4, 1, 11),
    _TnIfStatOutDiscards_Type()
)
tnIfStatOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfStatOutDiscards.setStatus("current")
_TnIfStatOutErrors_Type = Counter64
_TnIfStatOutErrors_Object = MibTableColumn
tnIfStatOutErrors = _TnIfStatOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 4, 1, 12),
    _TnIfStatOutErrors_Type()
)
tnIfStatOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfStatOutErrors.setStatus("current")
_TnIfStatInMulticastPkts_Type = Counter64
_TnIfStatInMulticastPkts_Object = MibTableColumn
tnIfStatInMulticastPkts = _TnIfStatInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 4, 1, 13),
    _TnIfStatInMulticastPkts_Type()
)
tnIfStatInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfStatInMulticastPkts.setStatus("current")
_TnIfStatInBroadcastPkts_Type = Counter64
_TnIfStatInBroadcastPkts_Object = MibTableColumn
tnIfStatInBroadcastPkts = _TnIfStatInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 4, 1, 14),
    _TnIfStatInBroadcastPkts_Type()
)
tnIfStatInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfStatInBroadcastPkts.setStatus("current")
_TnIfStatOutMulticastPkts_Type = Counter64
_TnIfStatOutMulticastPkts_Object = MibTableColumn
tnIfStatOutMulticastPkts = _TnIfStatOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 4, 1, 15),
    _TnIfStatOutMulticastPkts_Type()
)
tnIfStatOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfStatOutMulticastPkts.setStatus("current")
_TnIfStatOutBroadcastPkts_Type = Counter64
_TnIfStatOutBroadcastPkts_Object = MibTableColumn
tnIfStatOutBroadcastPkts = _TnIfStatOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 4, 1, 16),
    _TnIfStatOutBroadcastPkts_Type()
)
tnIfStatOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfStatOutBroadcastPkts.setStatus("current")
_TnIfStatInPacketsNotClassified_Type = Counter64
_TnIfStatInPacketsNotClassified_Object = MibTableColumn
tnIfStatInPacketsNotClassified = _TnIfStatInPacketsNotClassified_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 4, 1, 17),
    _TnIfStatInPacketsNotClassified_Type()
)
tnIfStatInPacketsNotClassified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfStatInPacketsNotClassified.setStatus("current")
_TnEtherStatsTotalMembers_Type = Integer32
_TnEtherStatsTotalMembers_Object = MibScalar
tnEtherStatsTotalMembers = _TnEtherStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 5),
    _TnEtherStatsTotalMembers_Type()
)
tnEtherStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatsTotalMembers.setStatus("current")
_TnEtherStatsTable_Object = MibTable
tnEtherStatsTable = _TnEtherStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    tnEtherStatsTable.setStatus("current")
_TnEtherStatsEntry_Object = MibTableRow
tnEtherStatsEntry = _TnEtherStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1)
)
tnEtherStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnEtherStatsBin"),
)
if mibBuilder.loadTexts:
    tnEtherStatsEntry.setStatus("current")
_TnEtherStatsBin_Type = TnStatsBinType
_TnEtherStatsBin_Object = MibTableColumn
tnEtherStatsBin = _TnEtherStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 1),
    _TnEtherStatsBin_Type()
)
tnEtherStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEtherStatsBin.setStatus("current")
_TnEtherStatsBinStatus_Type = TnStatsBinStatus
_TnEtherStatsBinStatus_Object = MibTableColumn
tnEtherStatsBinStatus = _TnEtherStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 2),
    _TnEtherStatsBinStatus_Type()
)
tnEtherStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatsBinStatus.setStatus("current")
_TnEtherStatsStartTime_Type = DateAndTime
_TnEtherStatsStartTime_Object = MibTableColumn
tnEtherStatsStartTime = _TnEtherStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 3),
    _TnEtherStatsStartTime_Type()
)
tnEtherStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatsStartTime.setStatus("current")
_TnEtherStatRxDropEvents_Type = Counter64
_TnEtherStatRxDropEvents_Object = MibTableColumn
tnEtherStatRxDropEvents = _TnEtherStatRxDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 4),
    _TnEtherStatRxDropEvents_Type()
)
tnEtherStatRxDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxDropEvents.setStatus("current")
_TnEtherStatRxFragments_Type = Counter64
_TnEtherStatRxFragments_Object = MibTableColumn
tnEtherStatRxFragments = _TnEtherStatRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 5),
    _TnEtherStatRxFragments_Type()
)
tnEtherStatRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxFragments.setStatus("current")
_TnEtherStatRxJabbers_Type = Counter64
_TnEtherStatRxJabbers_Object = MibTableColumn
tnEtherStatRxJabbers = _TnEtherStatRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 6),
    _TnEtherStatRxJabbers_Type()
)
tnEtherStatRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxJabbers.setStatus("current")
_TnEtherStatRxMcastPkts_Type = Counter64
_TnEtherStatRxMcastPkts_Object = MibTableColumn
tnEtherStatRxMcastPkts = _TnEtherStatRxMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 7),
    _TnEtherStatRxMcastPkts_Type()
)
tnEtherStatRxMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxMcastPkts.setStatus("current")
_TnEtherStatRxOctets_Type = Counter64
_TnEtherStatRxOctets_Object = MibTableColumn
tnEtherStatRxOctets = _TnEtherStatRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 8),
    _TnEtherStatRxOctets_Type()
)
tnEtherStatRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxOctets.setStatus("current")
_TnEtherStatRxOversizedPkts_Type = Counter64
_TnEtherStatRxOversizedPkts_Object = MibTableColumn
tnEtherStatRxOversizedPkts = _TnEtherStatRxOversizedPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 9),
    _TnEtherStatRxOversizedPkts_Type()
)
tnEtherStatRxOversizedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxOversizedPkts.setStatus("current")
_TnEtherStatRxPkts_Type = Counter64
_TnEtherStatRxPkts_Object = MibTableColumn
tnEtherStatRxPkts = _TnEtherStatRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 10),
    _TnEtherStatRxPkts_Type()
)
tnEtherStatRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxPkts.setStatus("current")
_TnEtherStatRxPktsSize1024to1518_Type = Counter64
_TnEtherStatRxPktsSize1024to1518_Object = MibTableColumn
tnEtherStatRxPktsSize1024to1518 = _TnEtherStatRxPktsSize1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 11),
    _TnEtherStatRxPktsSize1024to1518_Type()
)
tnEtherStatRxPktsSize1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxPktsSize1024to1518.setStatus("current")
_TnEtherStatRxPktsSize128to255_Type = Counter64
_TnEtherStatRxPktsSize128to255_Object = MibTableColumn
tnEtherStatRxPktsSize128to255 = _TnEtherStatRxPktsSize128to255_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 12),
    _TnEtherStatRxPktsSize128to255_Type()
)
tnEtherStatRxPktsSize128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxPktsSize128to255.setStatus("current")
_TnEtherStatRxPktsSize256to511_Type = Counter64
_TnEtherStatRxPktsSize256to511_Object = MibTableColumn
tnEtherStatRxPktsSize256to511 = _TnEtherStatRxPktsSize256to511_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 13),
    _TnEtherStatRxPktsSize256to511_Type()
)
tnEtherStatRxPktsSize256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxPktsSize256to511.setStatus("current")
_TnEtherStatRxPktsSize512to1023_Type = Counter64
_TnEtherStatRxPktsSize512to1023_Object = MibTableColumn
tnEtherStatRxPktsSize512to1023 = _TnEtherStatRxPktsSize512to1023_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 14),
    _TnEtherStatRxPktsSize512to1023_Type()
)
tnEtherStatRxPktsSize512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxPktsSize512to1023.setStatus("current")
_TnEtherStatRxPktsSize65to127_Type = Counter64
_TnEtherStatRxPktsSize65to127_Object = MibTableColumn
tnEtherStatRxPktsSize65to127 = _TnEtherStatRxPktsSize65to127_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 16),
    _TnEtherStatRxPktsSize65to127_Type()
)
tnEtherStatRxPktsSize65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxPktsSize65to127.setStatus("current")
_TnEtherStatRxUndersizedPkts_Type = Counter64
_TnEtherStatRxUndersizedPkts_Object = MibTableColumn
tnEtherStatRxUndersizedPkts = _TnEtherStatRxUndersizedPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 17),
    _TnEtherStatRxUndersizedPkts_Type()
)
tnEtherStatRxUndersizedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxUndersizedPkts.setStatus("current")
_TnEtherStatTxBcastPkts_Type = Counter64
_TnEtherStatTxBcastPkts_Object = MibTableColumn
tnEtherStatTxBcastPkts = _TnEtherStatTxBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 18),
    _TnEtherStatTxBcastPkts_Type()
)
tnEtherStatTxBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxBcastPkts.setStatus("current")
_TnEtherStatTxCrcAlignErrs_Type = Counter64
_TnEtherStatTxCrcAlignErrs_Object = MibTableColumn
tnEtherStatTxCrcAlignErrs = _TnEtherStatTxCrcAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 19),
    _TnEtherStatTxCrcAlignErrs_Type()
)
tnEtherStatTxCrcAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxCrcAlignErrs.setStatus("current")
_TnEtherStatTxDropEvents_Type = Counter64
_TnEtherStatTxDropEvents_Object = MibTableColumn
tnEtherStatTxDropEvents = _TnEtherStatTxDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 20),
    _TnEtherStatTxDropEvents_Type()
)
tnEtherStatTxDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxDropEvents.setStatus("current")
_TnEtherStatTxFragments_Type = Counter64
_TnEtherStatTxFragments_Object = MibTableColumn
tnEtherStatTxFragments = _TnEtherStatTxFragments_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 21),
    _TnEtherStatTxFragments_Type()
)
tnEtherStatTxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxFragments.setStatus("current")
_TnEtherStatTxJabbers_Type = Counter64
_TnEtherStatTxJabbers_Object = MibTableColumn
tnEtherStatTxJabbers = _TnEtherStatTxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 22),
    _TnEtherStatTxJabbers_Type()
)
tnEtherStatTxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxJabbers.setStatus("current")
_TnEtherStatTxMcastPkts_Type = Counter64
_TnEtherStatTxMcastPkts_Object = MibTableColumn
tnEtherStatTxMcastPkts = _TnEtherStatTxMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 23),
    _TnEtherStatTxMcastPkts_Type()
)
tnEtherStatTxMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxMcastPkts.setStatus("current")
_TnEtherStatTxOctets_Type = Counter64
_TnEtherStatTxOctets_Object = MibTableColumn
tnEtherStatTxOctets = _TnEtherStatTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 24),
    _TnEtherStatTxOctets_Type()
)
tnEtherStatTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxOctets.setStatus("current")
_TnEtherStatTxOversizedPkts_Type = Counter64
_TnEtherStatTxOversizedPkts_Object = MibTableColumn
tnEtherStatTxOversizedPkts = _TnEtherStatTxOversizedPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 25),
    _TnEtherStatTxOversizedPkts_Type()
)
tnEtherStatTxOversizedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxOversizedPkts.setStatus("current")
_TnEtherStatTxPkts_Type = Counter64
_TnEtherStatTxPkts_Object = MibTableColumn
tnEtherStatTxPkts = _TnEtherStatTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 26),
    _TnEtherStatTxPkts_Type()
)
tnEtherStatTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxPkts.setStatus("current")
_TnEtherStatTxPktsSize1024to1518_Type = Counter64
_TnEtherStatTxPktsSize1024to1518_Object = MibTableColumn
tnEtherStatTxPktsSize1024to1518 = _TnEtherStatTxPktsSize1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 27),
    _TnEtherStatTxPktsSize1024to1518_Type()
)
tnEtherStatTxPktsSize1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxPktsSize1024to1518.setStatus("current")
_TnEtherStatTxPktsSize128to255_Type = Counter64
_TnEtherStatTxPktsSize128to255_Object = MibTableColumn
tnEtherStatTxPktsSize128to255 = _TnEtherStatTxPktsSize128to255_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 28),
    _TnEtherStatTxPktsSize128to255_Type()
)
tnEtherStatTxPktsSize128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxPktsSize128to255.setStatus("current")
_TnEtherStatTxPktsSize256to511_Type = Counter64
_TnEtherStatTxPktsSize256to511_Object = MibTableColumn
tnEtherStatTxPktsSize256to511 = _TnEtherStatTxPktsSize256to511_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 29),
    _TnEtherStatTxPktsSize256to511_Type()
)
tnEtherStatTxPktsSize256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxPktsSize256to511.setStatus("current")
_TnEtherStatTxPktsSize512to1023_Type = Counter64
_TnEtherStatTxPktsSize512to1023_Object = MibTableColumn
tnEtherStatTxPktsSize512to1023 = _TnEtherStatTxPktsSize512to1023_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 30),
    _TnEtherStatTxPktsSize512to1023_Type()
)
tnEtherStatTxPktsSize512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxPktsSize512to1023.setStatus("current")
_TnEtherStatTxPktsSize65to127_Type = Counter64
_TnEtherStatTxPktsSize65to127_Object = MibTableColumn
tnEtherStatTxPktsSize65to127 = _TnEtherStatTxPktsSize65to127_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 32),
    _TnEtherStatTxPktsSize65to127_Type()
)
tnEtherStatTxPktsSize65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxPktsSize65to127.setStatus("current")
_TnEtherStatTxUndersizedPkts_Type = Counter64
_TnEtherStatTxUndersizedPkts_Object = MibTableColumn
tnEtherStatTxUndersizedPkts = _TnEtherStatTxUndersizedPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 33),
    _TnEtherStatTxUndersizedPkts_Type()
)
tnEtherStatTxUndersizedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxUndersizedPkts.setStatus("current")
_TnEtherStatRxBcastPkts_Type = Counter64
_TnEtherStatRxBcastPkts_Object = MibTableColumn
tnEtherStatRxBcastPkts = _TnEtherStatRxBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 34),
    _TnEtherStatRxBcastPkts_Type()
)
tnEtherStatRxBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxBcastPkts.setStatus("current")
_TnEtherStatRxCrcAlignErrs_Type = Counter64
_TnEtherStatRxCrcAlignErrs_Object = MibTableColumn
tnEtherStatRxCrcAlignErrs = _TnEtherStatRxCrcAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 35),
    _TnEtherStatRxCrcAlignErrs_Type()
)
tnEtherStatRxCrcAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxCrcAlignErrs.setStatus("current")
_TnEtherStatRxCollisions_Type = Counter64
_TnEtherStatRxCollisions_Object = MibTableColumn
tnEtherStatRxCollisions = _TnEtherStatRxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 36),
    _TnEtherStatRxCollisions_Type()
)
tnEtherStatRxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxCollisions.setStatus("current")
_TnEtherStatRxJumboPkts_Type = Counter64
_TnEtherStatRxJumboPkts_Object = MibTableColumn
tnEtherStatRxJumboPkts = _TnEtherStatRxJumboPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 37),
    _TnEtherStatRxJumboPkts_Type()
)
tnEtherStatRxJumboPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxJumboPkts.setStatus("current")
_TnEtherStatTxCollisions_Type = Counter64
_TnEtherStatTxCollisions_Object = MibTableColumn
tnEtherStatTxCollisions = _TnEtherStatTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 38),
    _TnEtherStatTxCollisions_Type()
)
tnEtherStatTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxCollisions.setStatus("current")
_TnEtherStatTxJumboPkts_Type = Counter64
_TnEtherStatTxJumboPkts_Object = MibTableColumn
tnEtherStatTxJumboPkts = _TnEtherStatTxJumboPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 39),
    _TnEtherStatTxJumboPkts_Type()
)
tnEtherStatTxJumboPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxJumboPkts.setStatus("current")
_TnEtherStatRxPktsSize64_Type = Counter64
_TnEtherStatRxPktsSize64_Object = MibTableColumn
tnEtherStatRxPktsSize64 = _TnEtherStatRxPktsSize64_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 40),
    _TnEtherStatRxPktsSize64_Type()
)
tnEtherStatRxPktsSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxPktsSize64.setStatus("current")
_TnEtherStatTxPktsSize64_Type = Counter64
_TnEtherStatTxPktsSize64_Object = MibTableColumn
tnEtherStatTxPktsSize64 = _TnEtherStatTxPktsSize64_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 41),
    _TnEtherStatTxPktsSize64_Type()
)
tnEtherStatTxPktsSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxPktsSize64.setStatus("current")
_TnEtherStatRxPktErrRatio_Type = Counter64
_TnEtherStatRxPktErrRatio_Object = MibTableColumn
tnEtherStatRxPktErrRatio = _TnEtherStatRxPktErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 42),
    _TnEtherStatRxPktErrRatio_Type()
)
tnEtherStatRxPktErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxPktErrRatio.setStatus("current")
_TnEtherStatTxPktErrRatio_Type = Counter64
_TnEtherStatTxPktErrRatio_Object = MibTableColumn
tnEtherStatTxPktErrRatio = _TnEtherStatTxPktErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 43),
    _TnEtherStatTxPktErrRatio_Type()
)
tnEtherStatTxPktErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxPktErrRatio.setStatus("current")
_TnEtherStatRxPktErrRatio15MinTr_Type = Counter64
_TnEtherStatRxPktErrRatio15MinTr_Object = MibTableColumn
tnEtherStatRxPktErrRatio15MinTr = _TnEtherStatRxPktErrRatio15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 44),
    _TnEtherStatRxPktErrRatio15MinTr_Type()
)
tnEtherStatRxPktErrRatio15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxPktErrRatio15MinTr.setStatus("current")
_TnEtherStatTxPktErrRatio15MinTr_Type = Counter64
_TnEtherStatTxPktErrRatio15MinTr_Object = MibTableColumn
tnEtherStatTxPktErrRatio15MinTr = _TnEtherStatTxPktErrRatio15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 45),
    _TnEtherStatTxPktErrRatio15MinTr_Type()
)
tnEtherStatTxPktErrRatio15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxPktErrRatio15MinTr.setStatus("current")
_TnEtherStatRxPktErrRatio1DayTr_Type = Counter64
_TnEtherStatRxPktErrRatio1DayTr_Object = MibTableColumn
tnEtherStatRxPktErrRatio1DayTr = _TnEtherStatRxPktErrRatio1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 46),
    _TnEtherStatRxPktErrRatio1DayTr_Type()
)
tnEtherStatRxPktErrRatio1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxPktErrRatio1DayTr.setStatus("current")
_TnEtherStatTxPktErrRatio1DayTr_Type = Counter64
_TnEtherStatTxPktErrRatio1DayTr_Object = MibTableColumn
tnEtherStatTxPktErrRatio1DayTr = _TnEtherStatTxPktErrRatio1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 47),
    _TnEtherStatTxPktErrRatio1DayTr_Type()
)
tnEtherStatTxPktErrRatio1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxPktErrRatio1DayTr.setStatus("current")
_TnEtherStatRxPktErrRatio15MinRtr_Type = Counter64
_TnEtherStatRxPktErrRatio15MinRtr_Object = MibTableColumn
tnEtherStatRxPktErrRatio15MinRtr = _TnEtherStatRxPktErrRatio15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 48),
    _TnEtherStatRxPktErrRatio15MinRtr_Type()
)
tnEtherStatRxPktErrRatio15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatRxPktErrRatio15MinRtr.setStatus("current")
_TnEtherStatTxPktErrRatio15MinRtr_Type = Counter64
_TnEtherStatTxPktErrRatio15MinRtr_Object = MibTableColumn
tnEtherStatTxPktErrRatio15MinRtr = _TnEtherStatTxPktErrRatio15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 6, 1, 49),
    _TnEtherStatTxPktErrRatio15MinRtr_Type()
)
tnEtherStatTxPktErrRatio15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherStatTxPktErrRatio15MinRtr.setStatus("current")
_TnSonetStatsTotalMembers_Type = Integer32
_TnSonetStatsTotalMembers_Object = MibScalar
tnSonetStatsTotalMembers = _TnSonetStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 7),
    _TnSonetStatsTotalMembers_Type()
)
tnSonetStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsTotalMembers.setStatus("current")
_TnSonetStatsTable_Object = MibTable
tnSonetStatsTable = _TnSonetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8)
)
if mibBuilder.loadTexts:
    tnSonetStatsTable.setStatus("current")
_TnSonetStatsEntry_Object = MibTableRow
tnSonetStatsEntry = _TnSonetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1)
)
tnSonetStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnSonetStatsBin"),
)
if mibBuilder.loadTexts:
    tnSonetStatsEntry.setStatus("current")
_TnSonetStatsBin_Type = TnStatsBinType
_TnSonetStatsBin_Object = MibTableColumn
tnSonetStatsBin = _TnSonetStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 1),
    _TnSonetStatsBin_Type()
)
tnSonetStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSonetStatsBin.setStatus("current")
_TnSonetStatsBinStatus_Type = TnStatsBinStatus
_TnSonetStatsBinStatus_Object = MibTableColumn
tnSonetStatsBinStatus = _TnSonetStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 2),
    _TnSonetStatsBinStatus_Type()
)
tnSonetStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsBinStatus.setStatus("current")
_TnSonetStatsStartTime_Type = DateAndTime
_TnSonetStatsStartTime_Object = MibTableColumn
tnSonetStatsStartTime = _TnSonetStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 3),
    _TnSonetStatsStartTime_Type()
)
tnSonetStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsStartTime.setStatus("current")
_TnSonetStatRxCVS_Type = Counter32
_TnSonetStatRxCVS_Object = MibTableColumn
tnSonetStatRxCVS = _TnSonetStatRxCVS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 4),
    _TnSonetStatRxCVS_Type()
)
tnSonetStatRxCVS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatRxCVS.setStatus("current")
_TnSonetStatRxESS_Type = Counter32
_TnSonetStatRxESS_Object = MibTableColumn
tnSonetStatRxESS = _TnSonetStatRxESS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 5),
    _TnSonetStatRxESS_Type()
)
tnSonetStatRxESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatRxESS.setStatus("current")
_TnSonetStatRxSESS_Type = Counter32
_TnSonetStatRxSESS_Object = MibTableColumn
tnSonetStatRxSESS = _TnSonetStatRxSESS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 6),
    _TnSonetStatRxSESS_Type()
)
tnSonetStatRxSESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatRxSESS.setStatus("current")
_TnSonetStatRxSEFSS_Type = Counter32
_TnSonetStatRxSEFSS_Object = MibTableColumn
tnSonetStatRxSEFSS = _TnSonetStatRxSEFSS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 7),
    _TnSonetStatRxSEFSS_Type()
)
tnSonetStatRxSEFSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatRxSEFSS.setStatus("current")
_TnSonetStatRxCVL_Type = Counter32
_TnSonetStatRxCVL_Object = MibTableColumn
tnSonetStatRxCVL = _TnSonetStatRxCVL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 8),
    _TnSonetStatRxCVL_Type()
)
tnSonetStatRxCVL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatRxCVL.setStatus("current")
_TnSonetStatRxESL_Type = Counter32
_TnSonetStatRxESL_Object = MibTableColumn
tnSonetStatRxESL = _TnSonetStatRxESL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 9),
    _TnSonetStatRxESL_Type()
)
tnSonetStatRxESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatRxESL.setStatus("current")
_TnSonetStatRxSESL_Type = Counter32
_TnSonetStatRxSESL_Object = MibTableColumn
tnSonetStatRxSESL = _TnSonetStatRxSESL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 10),
    _TnSonetStatRxSESL_Type()
)
tnSonetStatRxSESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatRxSESL.setStatus("current")
_TnSonetStatRxUASL_Type = Counter32
_TnSonetStatRxUASL_Object = MibTableColumn
tnSonetStatRxUASL = _TnSonetStatRxUASL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 11),
    _TnSonetStatRxUASL_Type()
)
tnSonetStatRxUASL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatRxUASL.setStatus("current")
_TnSonetStatRxFCL_Type = Counter32
_TnSonetStatRxFCL_Object = MibTableColumn
tnSonetStatRxFCL = _TnSonetStatRxFCL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 12),
    _TnSonetStatRxFCL_Type()
)
tnSonetStatRxFCL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatRxFCL.setStatus("current")
_TnSonetStatTxCVS_Type = Counter32
_TnSonetStatTxCVS_Object = MibTableColumn
tnSonetStatTxCVS = _TnSonetStatTxCVS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 13),
    _TnSonetStatTxCVS_Type()
)
tnSonetStatTxCVS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatTxCVS.setStatus("current")
_TnSonetStatTxESS_Type = Counter32
_TnSonetStatTxESS_Object = MibTableColumn
tnSonetStatTxESS = _TnSonetStatTxESS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 14),
    _TnSonetStatTxESS_Type()
)
tnSonetStatTxESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatTxESS.setStatus("current")
_TnSonetStatTxSESS_Type = Counter32
_TnSonetStatTxSESS_Object = MibTableColumn
tnSonetStatTxSESS = _TnSonetStatTxSESS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 15),
    _TnSonetStatTxSESS_Type()
)
tnSonetStatTxSESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatTxSESS.setStatus("current")
_TnSonetStatTxSEFSS_Type = Counter32
_TnSonetStatTxSEFSS_Object = MibTableColumn
tnSonetStatTxSEFSS = _TnSonetStatTxSEFSS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 16),
    _TnSonetStatTxSEFSS_Type()
)
tnSonetStatTxSEFSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatTxSEFSS.setStatus("current")
_TnSonetStatTxCVL_Type = Counter32
_TnSonetStatTxCVL_Object = MibTableColumn
tnSonetStatTxCVL = _TnSonetStatTxCVL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 17),
    _TnSonetStatTxCVL_Type()
)
tnSonetStatTxCVL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatTxCVL.setStatus("current")
_TnSonetStatTxESL_Type = Counter32
_TnSonetStatTxESL_Object = MibTableColumn
tnSonetStatTxESL = _TnSonetStatTxESL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 18),
    _TnSonetStatTxESL_Type()
)
tnSonetStatTxESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatTxESL.setStatus("current")
_TnSonetStatTxSESL_Type = Counter32
_TnSonetStatTxSESL_Object = MibTableColumn
tnSonetStatTxSESL = _TnSonetStatTxSESL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 19),
    _TnSonetStatTxSESL_Type()
)
tnSonetStatTxSESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatTxSESL.setStatus("current")
_TnSonetStatTxUASL_Type = Counter32
_TnSonetStatTxUASL_Object = MibTableColumn
tnSonetStatTxUASL = _TnSonetStatTxUASL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 20),
    _TnSonetStatTxUASL_Type()
)
tnSonetStatTxUASL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatTxUASL.setStatus("current")
_TnSonetStatTxFCL_Type = Counter32
_TnSonetStatTxFCL_Object = MibTableColumn
tnSonetStatTxFCL = _TnSonetStatTxFCL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 21),
    _TnSonetStatTxFCL_Type()
)
tnSonetStatTxFCL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatTxFCL.setStatus("current")
_TnSonetStatRxUASS_Type = Counter32
_TnSonetStatRxUASS_Object = MibTableColumn
tnSonetStatRxUASS = _TnSonetStatRxUASS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 22),
    _TnSonetStatRxUASS_Type()
)
tnSonetStatRxUASS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatRxUASS.setStatus("current")
_TnSonetStatTxUASS_Type = Counter32
_TnSonetStatTxUASS_Object = MibTableColumn
tnSonetStatTxUASS = _TnSonetStatTxUASS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 23),
    _TnSonetStatTxUASS_Type()
)
tnSonetStatTxUASS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatTxUASS.setStatus("current")
_TnSonetStatRxFECVL_Type = Counter32
_TnSonetStatRxFECVL_Object = MibTableColumn
tnSonetStatRxFECVL = _TnSonetStatRxFECVL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 84),
    _TnSonetStatRxFECVL_Type()
)
tnSonetStatRxFECVL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatRxFECVL.setStatus("current")
_TnSonetStatRxFEESL_Type = Counter32
_TnSonetStatRxFEESL_Object = MibTableColumn
tnSonetStatRxFEESL = _TnSonetStatRxFEESL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 85),
    _TnSonetStatRxFEESL_Type()
)
tnSonetStatRxFEESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatRxFEESL.setStatus("current")
_TnSonetStatRxFESESL_Type = Counter32
_TnSonetStatRxFESESL_Object = MibTableColumn
tnSonetStatRxFESESL = _TnSonetStatRxFESESL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 86),
    _TnSonetStatRxFESESL_Type()
)
tnSonetStatRxFESESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatRxFESESL.setStatus("current")
_TnSonetStatRxFEUASL_Type = Counter32
_TnSonetStatRxFEUASL_Object = MibTableColumn
tnSonetStatRxFEUASL = _TnSonetStatRxFEUASL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 8, 1, 87),
    _TnSonetStatRxFEUASL_Type()
)
tnSonetStatRxFEUASL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatRxFEUASL.setStatus("current")
_TnOptStatsTotalMembers_Type = Integer32
_TnOptStatsTotalMembers_Object = MibScalar
tnOptStatsTotalMembers = _TnOptStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 13),
    _TnOptStatsTotalMembers_Type()
)
tnOptStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOptStatsTotalMembers.setStatus("current")
_TnOptStatsTable_Object = MibTable
tnOptStatsTable = _TnOptStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 14)
)
if mibBuilder.loadTexts:
    tnOptStatsTable.setStatus("current")
_TnOptStatsEntry_Object = MibTableRow
tnOptStatsEntry = _TnOptStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 14, 1)
)
tnOptStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnOptStatsBin"),
)
if mibBuilder.loadTexts:
    tnOptStatsEntry.setStatus("current")
_TnOptStatsBin_Type = TnStatsBinType
_TnOptStatsBin_Object = MibTableColumn
tnOptStatsBin = _TnOptStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 14, 1, 1),
    _TnOptStatsBin_Type()
)
tnOptStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOptStatsBin.setStatus("current")
_TnOptStatsBinStatus_Type = TnStatsBinStatus
_TnOptStatsBinStatus_Object = MibTableColumn
tnOptStatsBinStatus = _TnOptStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 14, 1, 2),
    _TnOptStatsBinStatus_Type()
)
tnOptStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOptStatsBinStatus.setStatus("current")
_TnOptStatsStartTime_Type = DateAndTime
_TnOptStatsStartTime_Object = MibTableColumn
tnOptStatsStartTime = _TnOptStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 14, 1, 3),
    _TnOptStatsStartTime_Type()
)
tnOptStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOptStatsStartTime.setStatus("current")
_TnOptStatMinPower_Type = Integer32
_TnOptStatMinPower_Object = MibTableColumn
tnOptStatMinPower = _TnOptStatMinPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 14, 1, 4),
    _TnOptStatMinPower_Type()
)
tnOptStatMinPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOptStatMinPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOptStatMinPower.setUnits("mBm")
_TnOptStatMaxPower_Type = Integer32
_TnOptStatMaxPower_Object = MibTableColumn
tnOptStatMaxPower = _TnOptStatMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 14, 1, 5),
    _TnOptStatMaxPower_Type()
)
tnOptStatMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOptStatMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOptStatMaxPower.setUnits("mBm")
_TnOptStatAveragePower_Type = Integer32
_TnOptStatAveragePower_Object = MibTableColumn
tnOptStatAveragePower = _TnOptStatAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 14, 1, 6),
    _TnOptStatAveragePower_Type()
)
tnOptStatAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOptStatAveragePower.setStatus("current")
if mibBuilder.loadTexts:
    tnOptStatAveragePower.setUnits("mBm")
_TnOptStatMinPowerTr_Type = Integer32
_TnOptStatMinPowerTr_Object = MibTableColumn
tnOptStatMinPowerTr = _TnOptStatMinPowerTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 14, 1, 7),
    _TnOptStatMinPowerTr_Type()
)
tnOptStatMinPowerTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOptStatMinPowerTr.setStatus("current")
if mibBuilder.loadTexts:
    tnOptStatMinPowerTr.setUnits("mBm")
_TnOptStatMaxPowerTr_Type = Integer32
_TnOptStatMaxPowerTr_Object = MibTableColumn
tnOptStatMaxPowerTr = _TnOptStatMaxPowerTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 14, 1, 8),
    _TnOptStatMaxPowerTr_Type()
)
tnOptStatMaxPowerTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOptStatMaxPowerTr.setStatus("current")
if mibBuilder.loadTexts:
    tnOptStatMaxPowerTr.setUnits("mBm")
_TnOptStatMinPowerRtr_Type = Integer32
_TnOptStatMinPowerRtr_Object = MibTableColumn
tnOptStatMinPowerRtr = _TnOptStatMinPowerRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 14, 1, 9),
    _TnOptStatMinPowerRtr_Type()
)
tnOptStatMinPowerRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOptStatMinPowerRtr.setStatus("current")
if mibBuilder.loadTexts:
    tnOptStatMinPowerRtr.setUnits("mBm")
_TnOptStatMaxPowerRtr_Type = Integer32
_TnOptStatMaxPowerRtr_Object = MibTableColumn
tnOptStatMaxPowerRtr = _TnOptStatMaxPowerRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 14, 1, 10),
    _TnOptStatMaxPowerRtr_Type()
)
tnOptStatMaxPowerRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOptStatMaxPowerRtr.setStatus("current")
if mibBuilder.loadTexts:
    tnOptStatMaxPowerRtr.setUnits("mBm")
_TnOprStatsTotalMembers_Type = Integer32
_TnOprStatsTotalMembers_Object = MibScalar
tnOprStatsTotalMembers = _TnOprStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 15),
    _TnOprStatsTotalMembers_Type()
)
tnOprStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOprStatsTotalMembers.setStatus("current")
_TnOprStatsTable_Object = MibTable
tnOprStatsTable = _TnOprStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 16)
)
if mibBuilder.loadTexts:
    tnOprStatsTable.setStatus("current")
_TnOprStatsEntry_Object = MibTableRow
tnOprStatsEntry = _TnOprStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 16, 1)
)
tnOprStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnOprStatsBin"),
)
if mibBuilder.loadTexts:
    tnOprStatsEntry.setStatus("current")
_TnOprStatsBin_Type = TnStatsBinType
_TnOprStatsBin_Object = MibTableColumn
tnOprStatsBin = _TnOprStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 16, 1, 1),
    _TnOprStatsBin_Type()
)
tnOprStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOprStatsBin.setStatus("current")
_TnOprStatsBinStatus_Type = TnStatsBinStatus
_TnOprStatsBinStatus_Object = MibTableColumn
tnOprStatsBinStatus = _TnOprStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 16, 1, 2),
    _TnOprStatsBinStatus_Type()
)
tnOprStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOprStatsBinStatus.setStatus("current")
_TnOprStatsStartTime_Type = DateAndTime
_TnOprStatsStartTime_Object = MibTableColumn
tnOprStatsStartTime = _TnOprStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 16, 1, 3),
    _TnOprStatsStartTime_Type()
)
tnOprStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOprStatsStartTime.setStatus("current")
_TnOprStatMinPower_Type = Integer32
_TnOprStatMinPower_Object = MibTableColumn
tnOprStatMinPower = _TnOprStatMinPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 16, 1, 4),
    _TnOprStatMinPower_Type()
)
tnOprStatMinPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOprStatMinPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOprStatMinPower.setUnits("mBm")
_TnOprStatMaxPower_Type = Integer32
_TnOprStatMaxPower_Object = MibTableColumn
tnOprStatMaxPower = _TnOprStatMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 16, 1, 5),
    _TnOprStatMaxPower_Type()
)
tnOprStatMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOprStatMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOprStatMaxPower.setUnits("mBm")
_TnOprStatAveragePower_Type = Integer32
_TnOprStatAveragePower_Object = MibTableColumn
tnOprStatAveragePower = _TnOprStatAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 16, 1, 6),
    _TnOprStatAveragePower_Type()
)
tnOprStatAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOprStatAveragePower.setStatus("current")
if mibBuilder.loadTexts:
    tnOprStatAveragePower.setUnits("mBm")
_TnOprStatMinPowerTr_Type = Integer32
_TnOprStatMinPowerTr_Object = MibTableColumn
tnOprStatMinPowerTr = _TnOprStatMinPowerTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 16, 1, 7),
    _TnOprStatMinPowerTr_Type()
)
tnOprStatMinPowerTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOprStatMinPowerTr.setStatus("current")
if mibBuilder.loadTexts:
    tnOprStatMinPowerTr.setUnits("mBm")
_TnOprStatMaxPowerTr_Type = Integer32
_TnOprStatMaxPowerTr_Object = MibTableColumn
tnOprStatMaxPowerTr = _TnOprStatMaxPowerTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 16, 1, 8),
    _TnOprStatMaxPowerTr_Type()
)
tnOprStatMaxPowerTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOprStatMaxPowerTr.setStatus("current")
if mibBuilder.loadTexts:
    tnOprStatMaxPowerTr.setUnits("mBm")
_TnOprStatMinPowerRtr_Type = Integer32
_TnOprStatMinPowerRtr_Object = MibTableColumn
tnOprStatMinPowerRtr = _TnOprStatMinPowerRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 16, 1, 9),
    _TnOprStatMinPowerRtr_Type()
)
tnOprStatMinPowerRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOprStatMinPowerRtr.setStatus("current")
if mibBuilder.loadTexts:
    tnOprStatMinPowerRtr.setUnits("mBm")
_TnOprStatMaxPowerRtr_Type = Integer32
_TnOprStatMaxPowerRtr_Object = MibTableColumn
tnOprStatMaxPowerRtr = _TnOprStatMaxPowerRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 16, 1, 10),
    _TnOprStatMaxPowerRtr_Type()
)
tnOprStatMaxPowerRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOprStatMaxPowerRtr.setStatus("current")
if mibBuilder.loadTexts:
    tnOprStatMaxPowerRtr.setUnits("mBm")
_TnOpOutStatsTotalMembers_Type = Integer32
_TnOpOutStatsTotalMembers_Object = MibScalar
tnOpOutStatsTotalMembers = _TnOpOutStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 17),
    _TnOpOutStatsTotalMembers_Type()
)
tnOpOutStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOutStatsTotalMembers.setStatus("current")
_TnOpOutStatsTable_Object = MibTable
tnOpOutStatsTable = _TnOpOutStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 18)
)
if mibBuilder.loadTexts:
    tnOpOutStatsTable.setStatus("current")
_TnOpOutStatsEntry_Object = MibTableRow
tnOpOutStatsEntry = _TnOpOutStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 18, 1)
)
tnOpOutStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnOpOutStatsBin"),
)
if mibBuilder.loadTexts:
    tnOpOutStatsEntry.setStatus("current")
_TnOpOutStatsBin_Type = TnStatsBinType
_TnOpOutStatsBin_Object = MibTableColumn
tnOpOutStatsBin = _TnOpOutStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 18, 1, 1),
    _TnOpOutStatsBin_Type()
)
tnOpOutStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOpOutStatsBin.setStatus("current")
_TnOpOutStatsBinStatus_Type = TnStatsBinStatus
_TnOpOutStatsBinStatus_Object = MibTableColumn
tnOpOutStatsBinStatus = _TnOpOutStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 18, 1, 2),
    _TnOpOutStatsBinStatus_Type()
)
tnOpOutStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOutStatsBinStatus.setStatus("current")
_TnOpOutStatsStartTime_Type = DateAndTime
_TnOpOutStatsStartTime_Object = MibTableColumn
tnOpOutStatsStartTime = _TnOpOutStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 18, 1, 3),
    _TnOpOutStatsStartTime_Type()
)
tnOpOutStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOutStatsStartTime.setStatus("current")
_TnOpOutStatMinPower_Type = Integer32
_TnOpOutStatMinPower_Object = MibTableColumn
tnOpOutStatMinPower = _TnOpOutStatMinPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 18, 1, 4),
    _TnOpOutStatMinPower_Type()
)
tnOpOutStatMinPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOutStatMinPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpOutStatMinPower.setUnits("mBm")
_TnOpOutStatMaxPower_Type = Integer32
_TnOpOutStatMaxPower_Object = MibTableColumn
tnOpOutStatMaxPower = _TnOpOutStatMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 18, 1, 5),
    _TnOpOutStatMaxPower_Type()
)
tnOpOutStatMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOutStatMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpOutStatMaxPower.setUnits("mBm")
_TnOpOutStatAveragePower_Type = Integer32
_TnOpOutStatAveragePower_Object = MibTableColumn
tnOpOutStatAveragePower = _TnOpOutStatAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 18, 1, 6),
    _TnOpOutStatAveragePower_Type()
)
tnOpOutStatAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOutStatAveragePower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpOutStatAveragePower.setUnits("mBm")
_TnOpInStatsTotalMembers_Type = Integer32
_TnOpInStatsTotalMembers_Object = MibScalar
tnOpInStatsTotalMembers = _TnOpInStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 19),
    _TnOpInStatsTotalMembers_Type()
)
tnOpInStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpInStatsTotalMembers.setStatus("current")
_TnOpInStatsTable_Object = MibTable
tnOpInStatsTable = _TnOpInStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 20)
)
if mibBuilder.loadTexts:
    tnOpInStatsTable.setStatus("current")
_TnOpInStatsEntry_Object = MibTableRow
tnOpInStatsEntry = _TnOpInStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 20, 1)
)
tnOpInStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnOpInStatsBin"),
)
if mibBuilder.loadTexts:
    tnOpInStatsEntry.setStatus("current")
_TnOpInStatsBin_Type = TnStatsBinType
_TnOpInStatsBin_Object = MibTableColumn
tnOpInStatsBin = _TnOpInStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 20, 1, 1),
    _TnOpInStatsBin_Type()
)
tnOpInStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOpInStatsBin.setStatus("current")
_TnOpInStatsBinStatus_Type = TnStatsBinStatus
_TnOpInStatsBinStatus_Object = MibTableColumn
tnOpInStatsBinStatus = _TnOpInStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 20, 1, 2),
    _TnOpInStatsBinStatus_Type()
)
tnOpInStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpInStatsBinStatus.setStatus("current")
_TnOpInStatsStartTime_Type = DateAndTime
_TnOpInStatsStartTime_Object = MibTableColumn
tnOpInStatsStartTime = _TnOpInStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 20, 1, 3),
    _TnOpInStatsStartTime_Type()
)
tnOpInStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpInStatsStartTime.setStatus("current")
_TnOpInStatMinPower_Type = Integer32
_TnOpInStatMinPower_Object = MibTableColumn
tnOpInStatMinPower = _TnOpInStatMinPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 20, 1, 4),
    _TnOpInStatMinPower_Type()
)
tnOpInStatMinPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpInStatMinPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpInStatMinPower.setUnits("mBm")
_TnOpInStatMaxPower_Type = Integer32
_TnOpInStatMaxPower_Object = MibTableColumn
tnOpInStatMaxPower = _TnOpInStatMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 20, 1, 5),
    _TnOpInStatMaxPower_Type()
)
tnOpInStatMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpInStatMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpInStatMaxPower.setUnits("mBm")
_TnOpInStatAveragePower_Type = Integer32
_TnOpInStatAveragePower_Object = MibTableColumn
tnOpInStatAveragePower = _TnOpInStatAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 20, 1, 6),
    _TnOpInStatAveragePower_Type()
)
tnOpInStatAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpInStatAveragePower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpInStatAveragePower.setUnits("mBm")
_TnOpOchOutStatsTotalMembers_Type = Integer32
_TnOpOchOutStatsTotalMembers_Object = MibScalar
tnOpOchOutStatsTotalMembers = _TnOpOchOutStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 21),
    _TnOpOchOutStatsTotalMembers_Type()
)
tnOpOchOutStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchOutStatsTotalMembers.setStatus("current")
_TnOpOchOutStatsTable_Object = MibTable
tnOpOchOutStatsTable = _TnOpOchOutStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 22)
)
if mibBuilder.loadTexts:
    tnOpOchOutStatsTable.setStatus("current")
_TnOpOchOutStatsEntry_Object = MibTableRow
tnOpOchOutStatsEntry = _TnOpOchOutStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 22, 1)
)
tnOpOchOutStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnOpticalStatsITUChannel"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnOpOchOutStatsBin"),
)
if mibBuilder.loadTexts:
    tnOpOchOutStatsEntry.setStatus("current")
_TnOpOchOutStatsBin_Type = TnStatsBinType
_TnOpOchOutStatsBin_Object = MibTableColumn
tnOpOchOutStatsBin = _TnOpOchOutStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 22, 1, 1),
    _TnOpOchOutStatsBin_Type()
)
tnOpOchOutStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOpOchOutStatsBin.setStatus("current")
_TnOpOchOutStatsBinStatus_Type = TnStatsBinStatus
_TnOpOchOutStatsBinStatus_Object = MibTableColumn
tnOpOchOutStatsBinStatus = _TnOpOchOutStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 22, 1, 2),
    _TnOpOchOutStatsBinStatus_Type()
)
tnOpOchOutStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchOutStatsBinStatus.setStatus("current")
_TnOpOchOutStatsStartTime_Type = DateAndTime
_TnOpOchOutStatsStartTime_Object = MibTableColumn
tnOpOchOutStatsStartTime = _TnOpOchOutStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 22, 1, 3),
    _TnOpOchOutStatsStartTime_Type()
)
tnOpOchOutStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchOutStatsStartTime.setStatus("current")
_TnOpOchOutStatMinPower_Type = Integer32
_TnOpOchOutStatMinPower_Object = MibTableColumn
tnOpOchOutStatMinPower = _TnOpOchOutStatMinPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 22, 1, 4),
    _TnOpOchOutStatMinPower_Type()
)
tnOpOchOutStatMinPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchOutStatMinPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpOchOutStatMinPower.setUnits("mBm")
_TnOpOchOutStatMaxPower_Type = Integer32
_TnOpOchOutStatMaxPower_Object = MibTableColumn
tnOpOchOutStatMaxPower = _TnOpOchOutStatMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 22, 1, 5),
    _TnOpOchOutStatMaxPower_Type()
)
tnOpOchOutStatMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchOutStatMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpOchOutStatMaxPower.setUnits("mBm")
_TnOpOchOutStatAveragePower_Type = Integer32
_TnOpOchOutStatAveragePower_Object = MibTableColumn
tnOpOchOutStatAveragePower = _TnOpOchOutStatAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 22, 1, 6),
    _TnOpOchOutStatAveragePower_Type()
)
tnOpOchOutStatAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchOutStatAveragePower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpOchOutStatAveragePower.setUnits("mBm")
_TnOpOchInStatsTotalMembers_Type = Integer32
_TnOpOchInStatsTotalMembers_Object = MibScalar
tnOpOchInStatsTotalMembers = _TnOpOchInStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 23),
    _TnOpOchInStatsTotalMembers_Type()
)
tnOpOchInStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchInStatsTotalMembers.setStatus("current")
_TnOpOchInStatsTable_Object = MibTable
tnOpOchInStatsTable = _TnOpOchInStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 24)
)
if mibBuilder.loadTexts:
    tnOpOchInStatsTable.setStatus("current")
_TnOpOchInStatsEntry_Object = MibTableRow
tnOpOchInStatsEntry = _TnOpOchInStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 24, 1)
)
tnOpOchInStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnOpticalStatsITUChannel"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnOpOchInStatsBin"),
)
if mibBuilder.loadTexts:
    tnOpOchInStatsEntry.setStatus("current")
_TnOpOchInStatsBin_Type = TnStatsBinType
_TnOpOchInStatsBin_Object = MibTableColumn
tnOpOchInStatsBin = _TnOpOchInStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 24, 1, 1),
    _TnOpOchInStatsBin_Type()
)
tnOpOchInStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOpOchInStatsBin.setStatus("current")
_TnOpOchInStatsBinStatus_Type = TnStatsBinStatus
_TnOpOchInStatsBinStatus_Object = MibTableColumn
tnOpOchInStatsBinStatus = _TnOpOchInStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 24, 1, 2),
    _TnOpOchInStatsBinStatus_Type()
)
tnOpOchInStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchInStatsBinStatus.setStatus("current")
_TnOpOchInStatsStartTime_Type = DateAndTime
_TnOpOchInStatsStartTime_Object = MibTableColumn
tnOpOchInStatsStartTime = _TnOpOchInStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 24, 1, 3),
    _TnOpOchInStatsStartTime_Type()
)
tnOpOchInStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchInStatsStartTime.setStatus("current")
_TnOpOchInStatMinPower_Type = Integer32
_TnOpOchInStatMinPower_Object = MibTableColumn
tnOpOchInStatMinPower = _TnOpOchInStatMinPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 24, 1, 4),
    _TnOpOchInStatMinPower_Type()
)
tnOpOchInStatMinPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchInStatMinPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpOchInStatMinPower.setUnits("mBm")
_TnOpOchInStatMaxPower_Type = Integer32
_TnOpOchInStatMaxPower_Object = MibTableColumn
tnOpOchInStatMaxPower = _TnOpOchInStatMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 24, 1, 5),
    _TnOpOchInStatMaxPower_Type()
)
tnOpOchInStatMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchInStatMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpOchInStatMaxPower.setUnits("mBm")
_TnOpOchInStatAveragePower_Type = Integer32
_TnOpOchInStatAveragePower_Object = MibTableColumn
tnOpOchInStatAveragePower = _TnOpOchInStatAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 24, 1, 6),
    _TnOpOchInStatAveragePower_Type()
)
tnOpOchInStatAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchInStatAveragePower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpOchInStatAveragePower.setUnits("mBm")
_TnSdhStatsTotalMembers_Type = Integer32
_TnSdhStatsTotalMembers_Object = MibScalar
tnSdhStatsTotalMembers = _TnSdhStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 25),
    _TnSdhStatsTotalMembers_Type()
)
tnSdhStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsTotalMembers.setStatus("current")
_TnSdhStatsTable_Object = MibTable
tnSdhStatsTable = _TnSdhStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26)
)
if mibBuilder.loadTexts:
    tnSdhStatsTable.setStatus("current")
_TnSdhStatsEntry_Object = MibTableRow
tnSdhStatsEntry = _TnSdhStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1)
)
tnSdhStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnSdhStatsBin"),
)
if mibBuilder.loadTexts:
    tnSdhStatsEntry.setStatus("current")
_TnSdhStatsBin_Type = TnStatsBinType
_TnSdhStatsBin_Object = MibTableColumn
tnSdhStatsBin = _TnSdhStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 1),
    _TnSdhStatsBin_Type()
)
tnSdhStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSdhStatsBin.setStatus("current")
_TnSdhStatsBinStatus_Type = TnStatsBinStatus
_TnSdhStatsBinStatus_Object = MibTableColumn
tnSdhStatsBinStatus = _TnSdhStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 2),
    _TnSdhStatsBinStatus_Type()
)
tnSdhStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsBinStatus.setStatus("current")
_TnSdhStatsStartTime_Type = DateAndTime
_TnSdhStatsStartTime_Object = MibTableColumn
tnSdhStatsStartTime = _TnSdhStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 3),
    _TnSdhStatsStartTime_Type()
)
tnSdhStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsStartTime.setStatus("current")
_TnSdhStatRxRSEB_Type = Counter32
_TnSdhStatRxRSEB_Object = MibTableColumn
tnSdhStatRxRSEB = _TnSdhStatRxRSEB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 4),
    _TnSdhStatRxRSEB_Type()
)
tnSdhStatRxRSEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatRxRSEB.setStatus("current")
_TnSdhStatRxRSES_Type = Counter32
_TnSdhStatRxRSES_Object = MibTableColumn
tnSdhStatRxRSES = _TnSdhStatRxRSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 5),
    _TnSdhStatRxRSES_Type()
)
tnSdhStatRxRSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatRxRSES.setStatus("current")
_TnSdhStatRxRSSES_Type = Counter32
_TnSdhStatRxRSSES_Object = MibTableColumn
tnSdhStatRxRSSES = _TnSdhStatRxRSSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 6),
    _TnSdhStatRxRSSES_Type()
)
tnSdhStatRxRSSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatRxRSSES.setStatus("current")
_TnSdhStatRxMSEB_Type = Counter32
_TnSdhStatRxMSEB_Object = MibTableColumn
tnSdhStatRxMSEB = _TnSdhStatRxMSEB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 7),
    _TnSdhStatRxMSEB_Type()
)
tnSdhStatRxMSEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatRxMSEB.setStatus("current")
_TnSdhStatRxMSES_Type = Counter32
_TnSdhStatRxMSES_Object = MibTableColumn
tnSdhStatRxMSES = _TnSdhStatRxMSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 8),
    _TnSdhStatRxMSES_Type()
)
tnSdhStatRxMSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatRxMSES.setStatus("current")
_TnSdhStatRxMSSES_Type = Counter32
_TnSdhStatRxMSSES_Object = MibTableColumn
tnSdhStatRxMSSES = _TnSdhStatRxMSSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 9),
    _TnSdhStatRxMSSES_Type()
)
tnSdhStatRxMSSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatRxMSSES.setStatus("current")
_TnSdhStatRxMSUAS_Type = Counter32
_TnSdhStatRxMSUAS_Object = MibTableColumn
tnSdhStatRxMSUAS = _TnSdhStatRxMSUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 10),
    _TnSdhStatRxMSUAS_Type()
)
tnSdhStatRxMSUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatRxMSUAS.setStatus("current")
_TnSdhStatTxRSEB_Type = Counter32
_TnSdhStatTxRSEB_Object = MibTableColumn
tnSdhStatTxRSEB = _TnSdhStatTxRSEB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 11),
    _TnSdhStatTxRSEB_Type()
)
tnSdhStatTxRSEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatTxRSEB.setStatus("current")
_TnSdhStatTxRSES_Type = Counter32
_TnSdhStatTxRSES_Object = MibTableColumn
tnSdhStatTxRSES = _TnSdhStatTxRSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 12),
    _TnSdhStatTxRSES_Type()
)
tnSdhStatTxRSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatTxRSES.setStatus("current")
_TnSdhStatTxRSSES_Type = Counter32
_TnSdhStatTxRSSES_Object = MibTableColumn
tnSdhStatTxRSSES = _TnSdhStatTxRSSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 13),
    _TnSdhStatTxRSSES_Type()
)
tnSdhStatTxRSSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatTxRSSES.setStatus("current")
_TnSdhStatTxMSEB_Type = Counter32
_TnSdhStatTxMSEB_Object = MibTableColumn
tnSdhStatTxMSEB = _TnSdhStatTxMSEB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 14),
    _TnSdhStatTxMSEB_Type()
)
tnSdhStatTxMSEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatTxMSEB.setStatus("current")
_TnSdhStatTxMSES_Type = Counter32
_TnSdhStatTxMSES_Object = MibTableColumn
tnSdhStatTxMSES = _TnSdhStatTxMSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 15),
    _TnSdhStatTxMSES_Type()
)
tnSdhStatTxMSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatTxMSES.setStatus("current")
_TnSdhStatTxMSSES_Type = Counter32
_TnSdhStatTxMSSES_Object = MibTableColumn
tnSdhStatTxMSSES = _TnSdhStatTxMSSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 16),
    _TnSdhStatTxMSSES_Type()
)
tnSdhStatTxMSSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatTxMSSES.setStatus("current")
_TnSdhStatTxMSUAS_Type = Counter32
_TnSdhStatTxMSUAS_Object = MibTableColumn
tnSdhStatTxMSUAS = _TnSdhStatTxMSUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 17),
    _TnSdhStatTxMSUAS_Type()
)
tnSdhStatTxMSUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatTxMSUAS.setStatus("current")
_TnSdhStatRxRSUAS_Type = Counter32
_TnSdhStatRxRSUAS_Object = MibTableColumn
tnSdhStatRxRSUAS = _TnSdhStatRxRSUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 18),
    _TnSdhStatRxRSUAS_Type()
)
tnSdhStatRxRSUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatRxRSUAS.setStatus("current")
_TnSdhStatTxRSUAS_Type = Counter32
_TnSdhStatTxRSUAS_Object = MibTableColumn
tnSdhStatTxRSUAS = _TnSdhStatTxRSUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 19),
    _TnSdhStatTxRSUAS_Type()
)
tnSdhStatTxRSUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatTxRSUAS.setStatus("current")
_TnSdhStatRxMSFEEB_Type = Counter32
_TnSdhStatRxMSFEEB_Object = MibTableColumn
tnSdhStatRxMSFEEB = _TnSdhStatRxMSFEEB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 68),
    _TnSdhStatRxMSFEEB_Type()
)
tnSdhStatRxMSFEEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatRxMSFEEB.setStatus("current")
_TnSdhStatRxMSFEES_Type = Counter32
_TnSdhStatRxMSFEES_Object = MibTableColumn
tnSdhStatRxMSFEES = _TnSdhStatRxMSFEES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 69),
    _TnSdhStatRxMSFEES_Type()
)
tnSdhStatRxMSFEES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatRxMSFEES.setStatus("current")
_TnSdhStatRxMSFESES_Type = Counter32
_TnSdhStatRxMSFESES_Object = MibTableColumn
tnSdhStatRxMSFESES = _TnSdhStatRxMSFESES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 70),
    _TnSdhStatRxMSFESES_Type()
)
tnSdhStatRxMSFESES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatRxMSFESES.setStatus("current")
_TnSdhStatRxMSFEUAS_Type = Counter32
_TnSdhStatRxMSFEUAS_Object = MibTableColumn
tnSdhStatRxMSFEUAS = _TnSdhStatRxMSFEUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 26, 1, 71),
    _TnSdhStatRxMSFEUAS_Type()
)
tnSdhStatRxMSFEUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatRxMSFEUAS.setStatus("current")
_TnPhyCodeSublayerStatsTotalMembers_Type = Integer32
_TnPhyCodeSublayerStatsTotalMembers_Object = MibScalar
tnPhyCodeSublayerStatsTotalMembers = _TnPhyCodeSublayerStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 31),
    _TnPhyCodeSublayerStatsTotalMembers_Type()
)
tnPhyCodeSublayerStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerStatsTotalMembers.setStatus("current")
_TnPhyCodeSublayerStatsTable_Object = MibTable
tnPhyCodeSublayerStatsTable = _TnPhyCodeSublayerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 32)
)
if mibBuilder.loadTexts:
    tnPhyCodeSublayerStatsTable.setStatus("current")
_TnPhyCodeSublayerStatsEntry_Object = MibTableRow
tnPhyCodeSublayerStatsEntry = _TnPhyCodeSublayerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 32, 1)
)
tnPhyCodeSublayerStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerStatsBin"),
)
if mibBuilder.loadTexts:
    tnPhyCodeSublayerStatsEntry.setStatus("current")
_TnPhyCodeSublayerStatsBin_Type = TnStatsBinType
_TnPhyCodeSublayerStatsBin_Object = MibTableColumn
tnPhyCodeSublayerStatsBin = _TnPhyCodeSublayerStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 32, 1, 1),
    _TnPhyCodeSublayerStatsBin_Type()
)
tnPhyCodeSublayerStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerStatsBin.setStatus("current")
_TnPhyCodeSublayerStatsBinStatus_Type = TnStatsBinStatus
_TnPhyCodeSublayerStatsBinStatus_Object = MibTableColumn
tnPhyCodeSublayerStatsBinStatus = _TnPhyCodeSublayerStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 32, 1, 2),
    _TnPhyCodeSublayerStatsBinStatus_Type()
)
tnPhyCodeSublayerStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerStatsBinStatus.setStatus("current")
_TnPhyCodeSublayerStatsStartTime_Type = DateAndTime
_TnPhyCodeSublayerStatsStartTime_Object = MibTableColumn
tnPhyCodeSublayerStatsStartTime = _TnPhyCodeSublayerStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 32, 1, 3),
    _TnPhyCodeSublayerStatsStartTime_Type()
)
tnPhyCodeSublayerStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerStatsStartTime.setStatus("current")
_TnPhyCodeSublayerStatRxCV_Type = Counter32
_TnPhyCodeSublayerStatRxCV_Object = MibTableColumn
tnPhyCodeSublayerStatRxCV = _TnPhyCodeSublayerStatRxCV_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 32, 1, 4),
    _TnPhyCodeSublayerStatRxCV_Type()
)
tnPhyCodeSublayerStatRxCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerStatRxCV.setStatus("current")
_TnPhyCodeSublayerStatRxES_Type = Counter32
_TnPhyCodeSublayerStatRxES_Object = MibTableColumn
tnPhyCodeSublayerStatRxES = _TnPhyCodeSublayerStatRxES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 32, 1, 5),
    _TnPhyCodeSublayerStatRxES_Type()
)
tnPhyCodeSublayerStatRxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerStatRxES.setStatus("current")
_TnPhyCodeSublayerStatRxSES_Type = Counter32
_TnPhyCodeSublayerStatRxSES_Object = MibTableColumn
tnPhyCodeSublayerStatRxSES = _TnPhyCodeSublayerStatRxSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 32, 1, 6),
    _TnPhyCodeSublayerStatRxSES_Type()
)
tnPhyCodeSublayerStatRxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerStatRxSES.setStatus("current")
_TnPhyCodeSublayerStatRxSEFS_Type = Counter32
_TnPhyCodeSublayerStatRxSEFS_Object = MibTableColumn
tnPhyCodeSublayerStatRxSEFS = _TnPhyCodeSublayerStatRxSEFS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 32, 1, 7),
    _TnPhyCodeSublayerStatRxSEFS_Type()
)
tnPhyCodeSublayerStatRxSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerStatRxSEFS.setStatus("current")
_TnPhyCodeSublayerStatTxCV_Type = Counter32
_TnPhyCodeSublayerStatTxCV_Object = MibTableColumn
tnPhyCodeSublayerStatTxCV = _TnPhyCodeSublayerStatTxCV_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 32, 1, 8),
    _TnPhyCodeSublayerStatTxCV_Type()
)
tnPhyCodeSublayerStatTxCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerStatTxCV.setStatus("current")
_TnPhyCodeSublayerStatTxES_Type = Counter32
_TnPhyCodeSublayerStatTxES_Object = MibTableColumn
tnPhyCodeSublayerStatTxES = _TnPhyCodeSublayerStatTxES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 32, 1, 9),
    _TnPhyCodeSublayerStatTxES_Type()
)
tnPhyCodeSublayerStatTxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerStatTxES.setStatus("current")
_TnPhyCodeSublayerStatTxSES_Type = Counter32
_TnPhyCodeSublayerStatTxSES_Object = MibTableColumn
tnPhyCodeSublayerStatTxSES = _TnPhyCodeSublayerStatTxSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 32, 1, 10),
    _TnPhyCodeSublayerStatTxSES_Type()
)
tnPhyCodeSublayerStatTxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerStatTxSES.setStatus("current")
_TnPhyCodeSublayerStatTxSEFS_Type = Counter32
_TnPhyCodeSublayerStatTxSEFS_Object = MibTableColumn
tnPhyCodeSublayerStatTxSEFS = _TnPhyCodeSublayerStatTxSEFS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 32, 1, 11),
    _TnPhyCodeSublayerStatTxSEFS_Type()
)
tnPhyCodeSublayerStatTxSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerStatTxSEFS.setStatus("current")
_TnDigitalWrapper64BitStatsTotalMembers_Type = Integer32
_TnDigitalWrapper64BitStatsTotalMembers_Object = MibScalar
tnDigitalWrapper64BitStatsTotalMembers = _TnDigitalWrapper64BitStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 33),
    _TnDigitalWrapper64BitStatsTotalMembers_Type()
)
tnDigitalWrapper64BitStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDigitalWrapper64BitStatsTotalMembers.setStatus("current")
_TnDigitalWrapper64BitStatsTable_Object = MibTable
tnDigitalWrapper64BitStatsTable = _TnDigitalWrapper64BitStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34)
)
if mibBuilder.loadTexts:
    tnDigitalWrapper64BitStatsTable.setStatus("current")
_TnDigitalWrapper64BitStatsEntry_Object = MibTableRow
tnDigitalWrapper64BitStatsEntry = _TnDigitalWrapper64BitStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1)
)
tnDigitalWrapper64BitStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnDw64BitStatsBin"),
)
if mibBuilder.loadTexts:
    tnDigitalWrapper64BitStatsEntry.setStatus("current")
_TnDw64BitStatsBin_Type = TnStatsBinType
_TnDw64BitStatsBin_Object = MibTableColumn
tnDw64BitStatsBin = _TnDw64BitStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 1),
    _TnDw64BitStatsBin_Type()
)
tnDw64BitStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDw64BitStatsBin.setStatus("current")
_TnDw64BitStatsBinStatus_Type = TnStatsBinStatus
_TnDw64BitStatsBinStatus_Object = MibTableColumn
tnDw64BitStatsBinStatus = _TnDw64BitStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 2),
    _TnDw64BitStatsBinStatus_Type()
)
tnDw64BitStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsBinStatus.setStatus("current")
_TnDw64BitStatsStartTime_Type = DateAndTime
_TnDw64BitStatsStartTime_Object = MibTableColumn
tnDw64BitStatsStartTime = _TnDw64BitStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 3),
    _TnDw64BitStatsStartTime_Type()
)
tnDw64BitStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsStartTime.setStatus("current")
_TnDw64BitStatRxRSCorrCnt_Type = Counter64
_TnDw64BitStatRxRSCorrCnt_Object = MibTableColumn
tnDw64BitStatRxRSCorrCnt = _TnDw64BitStatRxRSCorrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 4),
    _TnDw64BitStatRxRSCorrCnt_Type()
)
tnDw64BitStatRxRSCorrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxRSCorrCnt.setStatus("current")
_TnDw64BitStatRxRSUncorrCnt_Type = Counter64
_TnDw64BitStatRxRSUncorrCnt_Object = MibTableColumn
tnDw64BitStatRxRSUncorrCnt = _TnDw64BitStatRxRSUncorrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 5),
    _TnDw64BitStatRxRSUncorrCnt_Type()
)
tnDw64BitStatRxRSUncorrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxRSUncorrCnt.setStatus("current")
_TnDw64BitStatRxSMBIP8ErrCnt_Type = Counter64
_TnDw64BitStatRxSMBIP8ErrCnt_Object = MibTableColumn
tnDw64BitStatRxSMBIP8ErrCnt = _TnDw64BitStatRxSMBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 6),
    _TnDw64BitStatRxSMBIP8ErrCnt_Type()
)
tnDw64BitStatRxSMBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxSMBIP8ErrCnt.setStatus("current")
_TnDw64BitStatRxPMBIP8ErrCnt_Type = Counter64
_TnDw64BitStatRxPMBIP8ErrCnt_Object = MibTableColumn
tnDw64BitStatRxPMBIP8ErrCnt = _TnDw64BitStatRxPMBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 7),
    _TnDw64BitStatRxPMBIP8ErrCnt_Type()
)
tnDw64BitStatRxPMBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxPMBIP8ErrCnt.setStatus("current")
_TnDw64BitStatRxSMES_Type = Counter64
_TnDw64BitStatRxSMES_Object = MibTableColumn
tnDw64BitStatRxSMES = _TnDw64BitStatRxSMES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 11),
    _TnDw64BitStatRxSMES_Type()
)
tnDw64BitStatRxSMES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxSMES.setStatus("current")
_TnDw64BitStatRxPMES_Type = Counter64
_TnDw64BitStatRxPMES_Object = MibTableColumn
tnDw64BitStatRxPMES = _TnDw64BitStatRxPMES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 12),
    _TnDw64BitStatRxPMES_Type()
)
tnDw64BitStatRxPMES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxPMES.setStatus("current")
_TnDw64BitStatRxSMSES_Type = Counter64
_TnDw64BitStatRxSMSES_Object = MibTableColumn
tnDw64BitStatRxSMSES = _TnDw64BitStatRxSMSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 13),
    _TnDw64BitStatRxSMSES_Type()
)
tnDw64BitStatRxSMSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxSMSES.setStatus("current")
_TnDw64BitStatRxPMSES_Type = Counter64
_TnDw64BitStatRxPMSES_Object = MibTableColumn
tnDw64BitStatRxPMSES = _TnDw64BitStatRxPMSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 14),
    _TnDw64BitStatRxPMSES_Type()
)
tnDw64BitStatRxPMSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxPMSES.setStatus("current")
_TnDw64BitStatRxSMUAS_Type = Counter64
_TnDw64BitStatRxSMUAS_Object = MibTableColumn
tnDw64BitStatRxSMUAS = _TnDw64BitStatRxSMUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 15),
    _TnDw64BitStatRxSMUAS_Type()
)
tnDw64BitStatRxSMUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxSMUAS.setStatus("current")
_TnDw64BitStatRxPMUAS_Type = Counter64
_TnDw64BitStatRxPMUAS_Object = MibTableColumn
tnDw64BitStatRxPMUAS = _TnDw64BitStatRxPMUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 16),
    _TnDw64BitStatRxPMUAS_Type()
)
tnDw64BitStatRxPMUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxPMUAS.setStatus("current")
_TnDw64BitStatRxBERPreFEC_Type = Counter64
_TnDw64BitStatRxBERPreFEC_Object = MibTableColumn
tnDw64BitStatRxBERPreFEC = _TnDw64BitStatRxBERPreFEC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 47),
    _TnDw64BitStatRxBERPreFEC_Type()
)
tnDw64BitStatRxBERPreFEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxBERPreFEC.setStatus("current")
_TnDw64BitStatRxBERPostFEC_Type = Counter64
_TnDw64BitStatRxBERPostFEC_Object = MibTableColumn
tnDw64BitStatRxBERPostFEC = _TnDw64BitStatRxBERPostFEC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 48),
    _TnDw64BitStatRxBERPostFEC_Type()
)
tnDw64BitStatRxBERPostFEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxBERPostFEC.setStatus("current")
_TnDw64BitStatRxSMFEBIP8ErrCnt_Type = Counter64
_TnDw64BitStatRxSMFEBIP8ErrCnt_Object = MibTableColumn
tnDw64BitStatRxSMFEBIP8ErrCnt = _TnDw64BitStatRxSMFEBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 49),
    _TnDw64BitStatRxSMFEBIP8ErrCnt_Type()
)
tnDw64BitStatRxSMFEBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxSMFEBIP8ErrCnt.setStatus("current")
_TnDw64BitStatRxPMFEBIP8ErrCnt_Type = Counter64
_TnDw64BitStatRxPMFEBIP8ErrCnt_Object = MibTableColumn
tnDw64BitStatRxPMFEBIP8ErrCnt = _TnDw64BitStatRxPMFEBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 50),
    _TnDw64BitStatRxPMFEBIP8ErrCnt_Type()
)
tnDw64BitStatRxPMFEBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxPMFEBIP8ErrCnt.setStatus("current")
_TnDw64BitStatRxSMBIAESErrCnt_Type = Counter64
_TnDw64BitStatRxSMBIAESErrCnt_Object = MibTableColumn
tnDw64BitStatRxSMBIAESErrCnt = _TnDw64BitStatRxSMBIAESErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 51),
    _TnDw64BitStatRxSMBIAESErrCnt_Type()
)
tnDw64BitStatRxSMBIAESErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxSMBIAESErrCnt.setStatus("current")
_TnDw64BitStatRxSMIAESErrCnt_Type = Counter64
_TnDw64BitStatRxSMIAESErrCnt_Object = MibTableColumn
tnDw64BitStatRxSMIAESErrCnt = _TnDw64BitStatRxSMIAESErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 52),
    _TnDw64BitStatRxSMIAESErrCnt_Type()
)
tnDw64BitStatRxSMIAESErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxSMIAESErrCnt.setStatus("current")
_TnDw64BitStatRxSMFEES_Type = Counter64
_TnDw64BitStatRxSMFEES_Object = MibTableColumn
tnDw64BitStatRxSMFEES = _TnDw64BitStatRxSMFEES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 53),
    _TnDw64BitStatRxSMFEES_Type()
)
tnDw64BitStatRxSMFEES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxSMFEES.setStatus("current")
_TnDw64BitStatRxPMFEES_Type = Counter64
_TnDw64BitStatRxPMFEES_Object = MibTableColumn
tnDw64BitStatRxPMFEES = _TnDw64BitStatRxPMFEES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 54),
    _TnDw64BitStatRxPMFEES_Type()
)
tnDw64BitStatRxPMFEES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxPMFEES.setStatus("current")
_TnDw64BitStatRxSMFESES_Type = Counter64
_TnDw64BitStatRxSMFESES_Object = MibTableColumn
tnDw64BitStatRxSMFESES = _TnDw64BitStatRxSMFESES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 55),
    _TnDw64BitStatRxSMFESES_Type()
)
tnDw64BitStatRxSMFESES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxSMFESES.setStatus("current")
_TnDw64BitStatRxPMFESES_Type = Counter64
_TnDw64BitStatRxPMFESES_Object = MibTableColumn
tnDw64BitStatRxPMFESES = _TnDw64BitStatRxPMFESES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 56),
    _TnDw64BitStatRxPMFESES_Type()
)
tnDw64BitStatRxPMFESES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxPMFESES.setStatus("current")
_TnDw64BitStatRxSMFEUAS_Type = Counter64
_TnDw64BitStatRxSMFEUAS_Object = MibTableColumn
tnDw64BitStatRxSMFEUAS = _TnDw64BitStatRxSMFEUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 57),
    _TnDw64BitStatRxSMFEUAS_Type()
)
tnDw64BitStatRxSMFEUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxSMFEUAS.setStatus("current")
_TnDw64BitStatRxPMFEUAS_Type = Counter64
_TnDw64BitStatRxPMFEUAS_Object = MibTableColumn
tnDw64BitStatRxPMFEUAS = _TnDw64BitStatRxPMFEUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 34, 1, 58),
    _TnDw64BitStatRxPMFEUAS_Type()
)
tnDw64BitStatRxPMFEUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatRxPMFEUAS.setStatus("current")
_TnCdrStatsTotalMembers_Type = Integer32
_TnCdrStatsTotalMembers_Object = MibScalar
tnCdrStatsTotalMembers = _TnCdrStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 35),
    _TnCdrStatsTotalMembers_Type()
)
tnCdrStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCdrStatsTotalMembers.setStatus("current")
_TnCdrStatsTable_Object = MibTable
tnCdrStatsTable = _TnCdrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 36)
)
if mibBuilder.loadTexts:
    tnCdrStatsTable.setStatus("current")
_TnCdrStatsEntry_Object = MibTableRow
tnCdrStatsEntry = _TnCdrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 36, 1)
)
tnCdrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnCdrStatsBin"),
)
if mibBuilder.loadTexts:
    tnCdrStatsEntry.setStatus("current")
_TnCdrStatsBin_Type = TnStatsBinType
_TnCdrStatsBin_Object = MibTableColumn
tnCdrStatsBin = _TnCdrStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 36, 1, 1),
    _TnCdrStatsBin_Type()
)
tnCdrStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCdrStatsBin.setStatus("current")
_TnCdrStatsBinStatus_Type = TnStatsBinStatus
_TnCdrStatsBinStatus_Object = MibTableColumn
tnCdrStatsBinStatus = _TnCdrStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 36, 1, 2),
    _TnCdrStatsBinStatus_Type()
)
tnCdrStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCdrStatsBinStatus.setStatus("current")
_TnCdrStatsStartTime_Type = DateAndTime
_TnCdrStatsStartTime_Object = MibTableColumn
tnCdrStatsStartTime = _TnCdrStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 36, 1, 3),
    _TnCdrStatsStartTime_Type()
)
tnCdrStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCdrStatsStartTime.setStatus("current")
_TnCdrStatMin_Type = Integer32
_TnCdrStatMin_Object = MibTableColumn
tnCdrStatMin = _TnCdrStatMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 36, 1, 4),
    _TnCdrStatMin_Type()
)
tnCdrStatMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCdrStatMin.setStatus("current")
if mibBuilder.loadTexts:
    tnCdrStatMin.setUnits("ps/nm")
_TnCdrStatMax_Type = Integer32
_TnCdrStatMax_Object = MibTableColumn
tnCdrStatMax = _TnCdrStatMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 36, 1, 5),
    _TnCdrStatMax_Type()
)
tnCdrStatMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCdrStatMax.setStatus("current")
if mibBuilder.loadTexts:
    tnCdrStatMax.setUnits("ps/nm")
_TnCdrStatAverage_Type = Integer32
_TnCdrStatAverage_Object = MibTableColumn
tnCdrStatAverage = _TnCdrStatAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 36, 1, 6),
    _TnCdrStatAverage_Type()
)
tnCdrStatAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCdrStatAverage.setStatus("current")
if mibBuilder.loadTexts:
    tnCdrStatAverage.setUnits("ps/nm")
_TnDgdrStatsTotalMembers_Type = Integer32
_TnDgdrStatsTotalMembers_Object = MibScalar
tnDgdrStatsTotalMembers = _TnDgdrStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 37),
    _TnDgdrStatsTotalMembers_Type()
)
tnDgdrStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDgdrStatsTotalMembers.setStatus("current")
_TnDgdrStatsTable_Object = MibTable
tnDgdrStatsTable = _TnDgdrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 38)
)
if mibBuilder.loadTexts:
    tnDgdrStatsTable.setStatus("current")
_TnDgdrStatsEntry_Object = MibTableRow
tnDgdrStatsEntry = _TnDgdrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 38, 1)
)
tnDgdrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnDgdrStatsBin"),
)
if mibBuilder.loadTexts:
    tnDgdrStatsEntry.setStatus("current")
_TnDgdrStatsBin_Type = TnStatsBinType
_TnDgdrStatsBin_Object = MibTableColumn
tnDgdrStatsBin = _TnDgdrStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 38, 1, 1),
    _TnDgdrStatsBin_Type()
)
tnDgdrStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDgdrStatsBin.setStatus("current")
_TnDgdrStatsBinStatus_Type = TnStatsBinStatus
_TnDgdrStatsBinStatus_Object = MibTableColumn
tnDgdrStatsBinStatus = _TnDgdrStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 38, 1, 2),
    _TnDgdrStatsBinStatus_Type()
)
tnDgdrStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDgdrStatsBinStatus.setStatus("current")
_TnDgdrStatsStartTime_Type = DateAndTime
_TnDgdrStatsStartTime_Object = MibTableColumn
tnDgdrStatsStartTime = _TnDgdrStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 38, 1, 3),
    _TnDgdrStatsStartTime_Type()
)
tnDgdrStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDgdrStatsStartTime.setStatus("current")
_TnDgdrStatMin_Type = Integer32
_TnDgdrStatMin_Object = MibTableColumn
tnDgdrStatMin = _TnDgdrStatMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 38, 1, 4),
    _TnDgdrStatMin_Type()
)
tnDgdrStatMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDgdrStatMin.setStatus("current")
if mibBuilder.loadTexts:
    tnDgdrStatMin.setUnits("ps")
_TnDgdrStatMax_Type = Integer32
_TnDgdrStatMax_Object = MibTableColumn
tnDgdrStatMax = _TnDgdrStatMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 38, 1, 5),
    _TnDgdrStatMax_Type()
)
tnDgdrStatMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDgdrStatMax.setStatus("current")
if mibBuilder.loadTexts:
    tnDgdrStatMax.setUnits("ps")
_TnDgdrStatAverage_Type = Integer32
_TnDgdrStatAverage_Object = MibTableColumn
tnDgdrStatAverage = _TnDgdrStatAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 38, 1, 6),
    _TnDgdrStatAverage_Type()
)
tnDgdrStatAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDgdrStatAverage.setStatus("current")
if mibBuilder.loadTexts:
    tnDgdrStatAverage.setUnits("ps")
_TnFoffrStatsTotalMembers_Type = Integer32
_TnFoffrStatsTotalMembers_Object = MibScalar
tnFoffrStatsTotalMembers = _TnFoffrStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 39),
    _TnFoffrStatsTotalMembers_Type()
)
tnFoffrStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFoffrStatsTotalMembers.setStatus("current")
_TnFoffrStatsTable_Object = MibTable
tnFoffrStatsTable = _TnFoffrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 40)
)
if mibBuilder.loadTexts:
    tnFoffrStatsTable.setStatus("current")
_TnFoffrStatsEntry_Object = MibTableRow
tnFoffrStatsEntry = _TnFoffrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 40, 1)
)
tnFoffrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnFoffrStatsBin"),
)
if mibBuilder.loadTexts:
    tnFoffrStatsEntry.setStatus("current")
_TnFoffrStatsBin_Type = TnStatsBinType
_TnFoffrStatsBin_Object = MibTableColumn
tnFoffrStatsBin = _TnFoffrStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 40, 1, 1),
    _TnFoffrStatsBin_Type()
)
tnFoffrStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnFoffrStatsBin.setStatus("current")
_TnFoffrStatsBinStatus_Type = TnStatsBinStatus
_TnFoffrStatsBinStatus_Object = MibTableColumn
tnFoffrStatsBinStatus = _TnFoffrStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 40, 1, 2),
    _TnFoffrStatsBinStatus_Type()
)
tnFoffrStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFoffrStatsBinStatus.setStatus("current")
_TnFoffrStatsStartTime_Type = DateAndTime
_TnFoffrStatsStartTime_Object = MibTableColumn
tnFoffrStatsStartTime = _TnFoffrStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 40, 1, 3),
    _TnFoffrStatsStartTime_Type()
)
tnFoffrStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFoffrStatsStartTime.setStatus("current")
_TnFoffrStatMin_Type = Integer32
_TnFoffrStatMin_Object = MibTableColumn
tnFoffrStatMin = _TnFoffrStatMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 40, 1, 4),
    _TnFoffrStatMin_Type()
)
tnFoffrStatMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFoffrStatMin.setStatus("current")
if mibBuilder.loadTexts:
    tnFoffrStatMin.setUnits("GHz")
_TnFoffrStatMax_Type = Integer32
_TnFoffrStatMax_Object = MibTableColumn
tnFoffrStatMax = _TnFoffrStatMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 40, 1, 5),
    _TnFoffrStatMax_Type()
)
tnFoffrStatMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFoffrStatMax.setStatus("current")
if mibBuilder.loadTexts:
    tnFoffrStatMax.setUnits("GHz")
_TnFoffrStatAverage_Type = Integer32
_TnFoffrStatAverage_Object = MibTableColumn
tnFoffrStatAverage = _TnFoffrStatAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 40, 1, 6),
    _TnFoffrStatAverage_Type()
)
tnFoffrStatAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFoffrStatAverage.setStatus("current")
if mibBuilder.loadTexts:
    tnFoffrStatAverage.setUnits("GHz")
_TnE1StatsTotalMembers_Type = Integer32
_TnE1StatsTotalMembers_Object = MibScalar
tnE1StatsTotalMembers = _TnE1StatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 41),
    _TnE1StatsTotalMembers_Type()
)
tnE1StatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatsTotalMembers.setStatus("current")
_TnE1StatsTable_Object = MibTable
tnE1StatsTable = _TnE1StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42)
)
if mibBuilder.loadTexts:
    tnE1StatsTable.setStatus("current")
_TnE1StatsEntry_Object = MibTableRow
tnE1StatsEntry = _TnE1StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1)
)
tnE1StatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnE1StatsBin"),
)
if mibBuilder.loadTexts:
    tnE1StatsEntry.setStatus("current")
_TnE1StatsBin_Type = TnStatsBinType
_TnE1StatsBin_Object = MibTableColumn
tnE1StatsBin = _TnE1StatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 1),
    _TnE1StatsBin_Type()
)
tnE1StatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnE1StatsBin.setStatus("current")
_TnE1StatsBinStatus_Type = TnStatsBinStatus
_TnE1StatsBinStatus_Object = MibTableColumn
tnE1StatsBinStatus = _TnE1StatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 2),
    _TnE1StatsBinStatus_Type()
)
tnE1StatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatsBinStatus.setStatus("current")
_TnE1StatsStartTime_Type = DateAndTime
_TnE1StatsStartTime_Object = MibTableColumn
tnE1StatsStartTime = _TnE1StatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 3),
    _TnE1StatsStartTime_Type()
)
tnE1StatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatsStartTime.setStatus("current")
_TnE1StatRxBBEP_Type = Counter32
_TnE1StatRxBBEP_Object = MibTableColumn
tnE1StatRxBBEP = _TnE1StatRxBBEP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 4),
    _TnE1StatRxBBEP_Type()
)
tnE1StatRxBBEP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxBBEP.setStatus("current")
_TnE1StatRxESP_Type = Counter32
_TnE1StatRxESP_Object = MibTableColumn
tnE1StatRxESP = _TnE1StatRxESP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 5),
    _TnE1StatRxESP_Type()
)
tnE1StatRxESP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxESP.setStatus("current")
_TnE1StatRxSESP_Type = Counter32
_TnE1StatRxSESP_Object = MibTableColumn
tnE1StatRxSESP = _TnE1StatRxSESP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 6),
    _TnE1StatRxSESP_Type()
)
tnE1StatRxSESP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxSESP.setStatus("current")
_TnE1StatRxUASP_Type = Counter32
_TnE1StatRxUASP_Object = MibTableColumn
tnE1StatRxUASP = _TnE1StatRxUASP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 7),
    _TnE1StatRxUASP_Type()
)
tnE1StatRxUASP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxUASP.setStatus("current")
_TnE1StatRxESL_Type = Counter32
_TnE1StatRxESL_Object = MibTableColumn
tnE1StatRxESL = _TnE1StatRxESL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 8),
    _TnE1StatRxESL_Type()
)
tnE1StatRxESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxESL.setStatus("current")
_TnE1StatRxSESL_Type = Counter32
_TnE1StatRxSESL_Object = MibTableColumn
tnE1StatRxSESL = _TnE1StatRxSESL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 9),
    _TnE1StatRxSESL_Type()
)
tnE1StatRxSESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxSESL.setStatus("current")
_TnE1StatTxBBEP_Type = Counter32
_TnE1StatTxBBEP_Object = MibTableColumn
tnE1StatTxBBEP = _TnE1StatTxBBEP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 10),
    _TnE1StatTxBBEP_Type()
)
tnE1StatTxBBEP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatTxBBEP.setStatus("current")
_TnE1StatTxESP_Type = Counter32
_TnE1StatTxESP_Object = MibTableColumn
tnE1StatTxESP = _TnE1StatTxESP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 11),
    _TnE1StatTxESP_Type()
)
tnE1StatTxESP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatTxESP.setStatus("current")
_TnE1StatTxSESP_Type = Counter32
_TnE1StatTxSESP_Object = MibTableColumn
tnE1StatTxSESP = _TnE1StatTxSESP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 12),
    _TnE1StatTxSESP_Type()
)
tnE1StatTxSESP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatTxSESP.setStatus("current")
_TnE1StatTxUASP_Type = Counter32
_TnE1StatTxUASP_Object = MibTableColumn
tnE1StatTxUASP = _TnE1StatTxUASP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 13),
    _TnE1StatTxUASP_Type()
)
tnE1StatTxUASP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatTxUASP.setStatus("current")
_TnE1StatRxBBEP15MinTr_Type = Counter32
_TnE1StatRxBBEP15MinTr_Object = MibTableColumn
tnE1StatRxBBEP15MinTr = _TnE1StatRxBBEP15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 14),
    _TnE1StatRxBBEP15MinTr_Type()
)
tnE1StatRxBBEP15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxBBEP15MinTr.setStatus("current")
_TnE1StatRxESP15MinTr_Type = Counter32
_TnE1StatRxESP15MinTr_Object = MibTableColumn
tnE1StatRxESP15MinTr = _TnE1StatRxESP15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 15),
    _TnE1StatRxESP15MinTr_Type()
)
tnE1StatRxESP15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxESP15MinTr.setStatus("current")
_TnE1StatRxSESP15MinTr_Type = Counter32
_TnE1StatRxSESP15MinTr_Object = MibTableColumn
tnE1StatRxSESP15MinTr = _TnE1StatRxSESP15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 16),
    _TnE1StatRxSESP15MinTr_Type()
)
tnE1StatRxSESP15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxSESP15MinTr.setStatus("current")
_TnE1StatRxUASP15MinTr_Type = Counter32
_TnE1StatRxUASP15MinTr_Object = MibTableColumn
tnE1StatRxUASP15MinTr = _TnE1StatRxUASP15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 17),
    _TnE1StatRxUASP15MinTr_Type()
)
tnE1StatRxUASP15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxUASP15MinTr.setStatus("current")
_TnE1StatRxESL15MinTr_Type = Counter32
_TnE1StatRxESL15MinTr_Object = MibTableColumn
tnE1StatRxESL15MinTr = _TnE1StatRxESL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 18),
    _TnE1StatRxESL15MinTr_Type()
)
tnE1StatRxESL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxESL15MinTr.setStatus("current")
_TnE1StatRxSESL15MinTr_Type = Counter32
_TnE1StatRxSESL15MinTr_Object = MibTableColumn
tnE1StatRxSESL15MinTr = _TnE1StatRxSESL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 19),
    _TnE1StatRxSESL15MinTr_Type()
)
tnE1StatRxSESL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxSESL15MinTr.setStatus("current")
_TnE1StatTxBBEP15MinTr_Type = Counter32
_TnE1StatTxBBEP15MinTr_Object = MibTableColumn
tnE1StatTxBBEP15MinTr = _TnE1StatTxBBEP15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 20),
    _TnE1StatTxBBEP15MinTr_Type()
)
tnE1StatTxBBEP15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatTxBBEP15MinTr.setStatus("current")
_TnE1StatTxESP15MinTr_Type = Counter32
_TnE1StatTxESP15MinTr_Object = MibTableColumn
tnE1StatTxESP15MinTr = _TnE1StatTxESP15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 21),
    _TnE1StatTxESP15MinTr_Type()
)
tnE1StatTxESP15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatTxESP15MinTr.setStatus("current")
_TnE1StatTxSESP15MinTr_Type = Counter32
_TnE1StatTxSESP15MinTr_Object = MibTableColumn
tnE1StatTxSESP15MinTr = _TnE1StatTxSESP15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 22),
    _TnE1StatTxSESP15MinTr_Type()
)
tnE1StatTxSESP15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatTxSESP15MinTr.setStatus("current")
_TnE1StatTxUASP15MinTr_Type = Counter32
_TnE1StatTxUASP15MinTr_Object = MibTableColumn
tnE1StatTxUASP15MinTr = _TnE1StatTxUASP15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 23),
    _TnE1StatTxUASP15MinTr_Type()
)
tnE1StatTxUASP15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatTxUASP15MinTr.setStatus("current")
_TnE1StatRxBBEP1DayTr_Type = Counter32
_TnE1StatRxBBEP1DayTr_Object = MibTableColumn
tnE1StatRxBBEP1DayTr = _TnE1StatRxBBEP1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 24),
    _TnE1StatRxBBEP1DayTr_Type()
)
tnE1StatRxBBEP1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxBBEP1DayTr.setStatus("current")
_TnE1StatRxESP1DayTr_Type = Counter32
_TnE1StatRxESP1DayTr_Object = MibTableColumn
tnE1StatRxESP1DayTr = _TnE1StatRxESP1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 25),
    _TnE1StatRxESP1DayTr_Type()
)
tnE1StatRxESP1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxESP1DayTr.setStatus("current")
_TnE1StatRxSESP1DayTr_Type = Counter32
_TnE1StatRxSESP1DayTr_Object = MibTableColumn
tnE1StatRxSESP1DayTr = _TnE1StatRxSESP1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 26),
    _TnE1StatRxSESP1DayTr_Type()
)
tnE1StatRxSESP1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxSESP1DayTr.setStatus("current")
_TnE1StatRxUASP1DayTr_Type = Counter32
_TnE1StatRxUASP1DayTr_Object = MibTableColumn
tnE1StatRxUASP1DayTr = _TnE1StatRxUASP1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 27),
    _TnE1StatRxUASP1DayTr_Type()
)
tnE1StatRxUASP1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxUASP1DayTr.setStatus("current")
_TnE1StatRxESL1DayTr_Type = Counter32
_TnE1StatRxESL1DayTr_Object = MibTableColumn
tnE1StatRxESL1DayTr = _TnE1StatRxESL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 28),
    _TnE1StatRxESL1DayTr_Type()
)
tnE1StatRxESL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxESL1DayTr.setStatus("current")
_TnE1StatRxSESL1DayTr_Type = Counter32
_TnE1StatRxSESL1DayTr_Object = MibTableColumn
tnE1StatRxSESL1DayTr = _TnE1StatRxSESL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 29),
    _TnE1StatRxSESL1DayTr_Type()
)
tnE1StatRxSESL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxSESL1DayTr.setStatus("current")
_TnE1StatTxBBEP1DayTr_Type = Counter32
_TnE1StatTxBBEP1DayTr_Object = MibTableColumn
tnE1StatTxBBEP1DayTr = _TnE1StatTxBBEP1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 30),
    _TnE1StatTxBBEP1DayTr_Type()
)
tnE1StatTxBBEP1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatTxBBEP1DayTr.setStatus("current")
_TnE1StatTxESP1DayTr_Type = Counter32
_TnE1StatTxESP1DayTr_Object = MibTableColumn
tnE1StatTxESP1DayTr = _TnE1StatTxESP1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 31),
    _TnE1StatTxESP1DayTr_Type()
)
tnE1StatTxESP1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatTxESP1DayTr.setStatus("current")
_TnE1StatTxSESP1DayTr_Type = Counter32
_TnE1StatTxSESP1DayTr_Object = MibTableColumn
tnE1StatTxSESP1DayTr = _TnE1StatTxSESP1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 32),
    _TnE1StatTxSESP1DayTr_Type()
)
tnE1StatTxSESP1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatTxSESP1DayTr.setStatus("current")
_TnE1StatTxUASP1DayTr_Type = Counter32
_TnE1StatTxUASP1DayTr_Object = MibTableColumn
tnE1StatTxUASP1DayTr = _TnE1StatTxUASP1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 33),
    _TnE1StatTxUASP1DayTr_Type()
)
tnE1StatTxUASP1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatTxUASP1DayTr.setStatus("current")
_TnE1StatRxBBEP15MinRtr_Type = Counter32
_TnE1StatRxBBEP15MinRtr_Object = MibTableColumn
tnE1StatRxBBEP15MinRtr = _TnE1StatRxBBEP15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 34),
    _TnE1StatRxBBEP15MinRtr_Type()
)
tnE1StatRxBBEP15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxBBEP15MinRtr.setStatus("current")
_TnE1StatRxESP15MinRtr_Type = Counter32
_TnE1StatRxESP15MinRtr_Object = MibTableColumn
tnE1StatRxESP15MinRtr = _TnE1StatRxESP15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 35),
    _TnE1StatRxESP15MinRtr_Type()
)
tnE1StatRxESP15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxESP15MinRtr.setStatus("current")
_TnE1StatRxSESP15MinRtr_Type = Counter32
_TnE1StatRxSESP15MinRtr_Object = MibTableColumn
tnE1StatRxSESP15MinRtr = _TnE1StatRxSESP15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 36),
    _TnE1StatRxSESP15MinRtr_Type()
)
tnE1StatRxSESP15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxSESP15MinRtr.setStatus("current")
_TnE1StatRxUASP15MinRtr_Type = Counter32
_TnE1StatRxUASP15MinRtr_Object = MibTableColumn
tnE1StatRxUASP15MinRtr = _TnE1StatRxUASP15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 37),
    _TnE1StatRxUASP15MinRtr_Type()
)
tnE1StatRxUASP15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxUASP15MinRtr.setStatus("current")
_TnE1StatRxESL15MinRtr_Type = Counter32
_TnE1StatRxESL15MinRtr_Object = MibTableColumn
tnE1StatRxESL15MinRtr = _TnE1StatRxESL15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 38),
    _TnE1StatRxESL15MinRtr_Type()
)
tnE1StatRxESL15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxESL15MinRtr.setStatus("current")
_TnE1StatRxSESL15MinRtr_Type = Counter32
_TnE1StatRxSESL15MinRtr_Object = MibTableColumn
tnE1StatRxSESL15MinRtr = _TnE1StatRxSESL15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 39),
    _TnE1StatRxSESL15MinRtr_Type()
)
tnE1StatRxSESL15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatRxSESL15MinRtr.setStatus("current")
_TnE1StatTxBBEP15MinRtr_Type = Counter32
_TnE1StatTxBBEP15MinRtr_Object = MibTableColumn
tnE1StatTxBBEP15MinRtr = _TnE1StatTxBBEP15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 40),
    _TnE1StatTxBBEP15MinRtr_Type()
)
tnE1StatTxBBEP15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatTxBBEP15MinRtr.setStatus("current")
_TnE1StatTxESP15MinRtr_Type = Counter32
_TnE1StatTxESP15MinRtr_Object = MibTableColumn
tnE1StatTxESP15MinRtr = _TnE1StatTxESP15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 41),
    _TnE1StatTxESP15MinRtr_Type()
)
tnE1StatTxESP15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatTxESP15MinRtr.setStatus("current")
_TnE1StatTxSESP15MinRtr_Type = Counter32
_TnE1StatTxSESP15MinRtr_Object = MibTableColumn
tnE1StatTxSESP15MinRtr = _TnE1StatTxSESP15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 42),
    _TnE1StatTxSESP15MinRtr_Type()
)
tnE1StatTxSESP15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatTxSESP15MinRtr.setStatus("current")
_TnE1StatTxUASP15MinRtr_Type = Counter32
_TnE1StatTxUASP15MinRtr_Object = MibTableColumn
tnE1StatTxUASP15MinRtr = _TnE1StatTxUASP15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 42, 1, 43),
    _TnE1StatTxUASP15MinRtr_Type()
)
tnE1StatTxUASP15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1StatTxUASP15MinRtr.setStatus("current")
_TnPreFECBitsStatsTotalMembers_Type = Integer32
_TnPreFECBitsStatsTotalMembers_Object = MibScalar
tnPreFECBitsStatsTotalMembers = _TnPreFECBitsStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 43),
    _TnPreFECBitsStatsTotalMembers_Type()
)
tnPreFECBitsStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPreFECBitsStatsTotalMembers.setStatus("current")
_TnPreFECBitsStatsTable_Object = MibTable
tnPreFECBitsStatsTable = _TnPreFECBitsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 44)
)
if mibBuilder.loadTexts:
    tnPreFECBitsStatsTable.setStatus("current")
_TnPreFECBitsStatsEntry_Object = MibTableRow
tnPreFECBitsStatsEntry = _TnPreFECBitsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 44, 1)
)
tnPreFECBitsStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnPreFECBitsStatsBin"),
)
if mibBuilder.loadTexts:
    tnPreFECBitsStatsEntry.setStatus("current")
_TnPreFECBitsStatsBin_Type = TnStatsBinType
_TnPreFECBitsStatsBin_Object = MibTableColumn
tnPreFECBitsStatsBin = _TnPreFECBitsStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 44, 1, 1),
    _TnPreFECBitsStatsBin_Type()
)
tnPreFECBitsStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPreFECBitsStatsBin.setStatus("current")
_TnPreFECBitsStatsBinStatus_Type = TnStatsBinStatus
_TnPreFECBitsStatsBinStatus_Object = MibTableColumn
tnPreFECBitsStatsBinStatus = _TnPreFECBitsStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 44, 1, 2),
    _TnPreFECBitsStatsBinStatus_Type()
)
tnPreFECBitsStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPreFECBitsStatsBinStatus.setStatus("current")
_TnPreFECBitsStatsStartTime_Type = DateAndTime
_TnPreFECBitsStatsStartTime_Object = MibTableColumn
tnPreFECBitsStatsStartTime = _TnPreFECBitsStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 44, 1, 3),
    _TnPreFECBitsStatsStartTime_Type()
)
tnPreFECBitsStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPreFECBitsStatsStartTime.setStatus("current")
_TnPreFECBitsStatMin_Type = Counter64
_TnPreFECBitsStatMin_Object = MibTableColumn
tnPreFECBitsStatMin = _TnPreFECBitsStatMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 44, 1, 4),
    _TnPreFECBitsStatMin_Type()
)
tnPreFECBitsStatMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPreFECBitsStatMin.setStatus("current")
if mibBuilder.loadTexts:
    tnPreFECBitsStatMin.setUnits("Bits in 1-second")
_TnPreFECBitsStatMax_Type = Counter64
_TnPreFECBitsStatMax_Object = MibTableColumn
tnPreFECBitsStatMax = _TnPreFECBitsStatMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 44, 1, 5),
    _TnPreFECBitsStatMax_Type()
)
tnPreFECBitsStatMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPreFECBitsStatMax.setStatus("current")
if mibBuilder.loadTexts:
    tnPreFECBitsStatMax.setUnits("Bits in 1-second")
_TnPreFECBitsStatAverage_Type = Counter64
_TnPreFECBitsStatAverage_Object = MibTableColumn
tnPreFECBitsStatAverage = _TnPreFECBitsStatAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 44, 1, 6),
    _TnPreFECBitsStatAverage_Type()
)
tnPreFECBitsStatAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPreFECBitsStatAverage.setStatus("current")
if mibBuilder.loadTexts:
    tnPreFECBitsStatAverage.setUnits("Bits in 1-second")
_TnEncrypt64BitStatsTotalMembers_Type = Integer32
_TnEncrypt64BitStatsTotalMembers_Object = MibScalar
tnEncrypt64BitStatsTotalMembers = _TnEncrypt64BitStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 47),
    _TnEncrypt64BitStatsTotalMembers_Type()
)
tnEncrypt64BitStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEncrypt64BitStatsTotalMembers.setStatus("current")
_TnEncrypt64BitStatsTable_Object = MibTable
tnEncrypt64BitStatsTable = _TnEncrypt64BitStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 48)
)
if mibBuilder.loadTexts:
    tnEncrypt64BitStatsTable.setStatus("current")
_TnEncrypt64BitStatsEntry_Object = MibTableRow
tnEncrypt64BitStatsEntry = _TnEncrypt64BitStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 48, 1)
)
tnEncrypt64BitStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnEncrypt64BitStatsBin"),
)
if mibBuilder.loadTexts:
    tnEncrypt64BitStatsEntry.setStatus("current")
_TnEncrypt64BitStatsBin_Type = TnStatsBinType
_TnEncrypt64BitStatsBin_Object = MibTableColumn
tnEncrypt64BitStatsBin = _TnEncrypt64BitStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 48, 1, 1),
    _TnEncrypt64BitStatsBin_Type()
)
tnEncrypt64BitStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEncrypt64BitStatsBin.setStatus("current")
_TnEncrypt64BitStatsBinStatus_Type = TnStatsBinStatus
_TnEncrypt64BitStatsBinStatus_Object = MibTableColumn
tnEncrypt64BitStatsBinStatus = _TnEncrypt64BitStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 48, 1, 2),
    _TnEncrypt64BitStatsBinStatus_Type()
)
tnEncrypt64BitStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEncrypt64BitStatsBinStatus.setStatus("current")
_TnEncrypt64BitStatsStartTime_Type = DateAndTime
_TnEncrypt64BitStatsStartTime_Object = MibTableColumn
tnEncrypt64BitStatsStartTime = _TnEncrypt64BitStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 48, 1, 3),
    _TnEncrypt64BitStatsStartTime_Type()
)
tnEncrypt64BitStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEncrypt64BitStatsStartTime.setStatus("current")
_TnEncrypt64BitStatTx128BitBlkCnt_Type = Counter64
_TnEncrypt64BitStatTx128BitBlkCnt_Object = MibTableColumn
tnEncrypt64BitStatTx128BitBlkCnt = _TnEncrypt64BitStatTx128BitBlkCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 48, 1, 4),
    _TnEncrypt64BitStatTx128BitBlkCnt_Type()
)
tnEncrypt64BitStatTx128BitBlkCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEncrypt64BitStatTx128BitBlkCnt.setStatus("current")
_TnEncrypt64BitStatRxFailToDecryptCnt_Type = Counter64
_TnEncrypt64BitStatRxFailToDecryptCnt_Object = MibTableColumn
tnEncrypt64BitStatRxFailToDecryptCnt = _TnEncrypt64BitStatRxFailToDecryptCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 48, 1, 5),
    _TnEncrypt64BitStatRxFailToDecryptCnt_Type()
)
tnEncrypt64BitStatRxFailToDecryptCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEncrypt64BitStatRxFailToDecryptCnt.setStatus("current")
_TnOthOdukStatsRxTotalMembers_Type = Integer32
_TnOthOdukStatsRxTotalMembers_Object = MibScalar
tnOthOdukStatsRxTotalMembers = _TnOthOdukStatsRxTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 49),
    _TnOthOdukStatsRxTotalMembers_Type()
)
tnOthOdukStatsRxTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsRxTotalMembers.setStatus("current")
_TnOthOdukStatsRxTable_Object = MibTable
tnOthOdukStatsRxTable = _TnOthOdukStatsRxTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 50)
)
if mibBuilder.loadTexts:
    tnOthOdukStatsRxTable.setStatus("current")
_TnOthOdukStatsRxEntry_Object = MibTableRow
tnOthOdukStatsRxEntry = _TnOthOdukStatsRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 50, 1)
)
tnOthOdukStatsRxEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnOthOdukStatsBin"),
)
if mibBuilder.loadTexts:
    tnOthOdukStatsRxEntry.setStatus("current")
_TnOthOdukStatsBin_Type = TnStatsBinType
_TnOthOdukStatsBin_Object = MibTableColumn
tnOthOdukStatsBin = _TnOthOdukStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 50, 1, 1),
    _TnOthOdukStatsBin_Type()
)
tnOthOdukStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthOdukStatsBin.setStatus("current")
_TnOthOdukStatsRxBinStatus_Type = TnStatsBinStatus
_TnOthOdukStatsRxBinStatus_Object = MibTableColumn
tnOthOdukStatsRxBinStatus = _TnOthOdukStatsRxBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 50, 1, 2),
    _TnOthOdukStatsRxBinStatus_Type()
)
tnOthOdukStatsRxBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsRxBinStatus.setStatus("current")
_TnOthOdukStatsRxStartTime_Type = DateAndTime
_TnOthOdukStatsRxStartTime_Object = MibTableColumn
tnOthOdukStatsRxStartTime = _TnOthOdukStatsRxStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 50, 1, 3),
    _TnOthOdukStatsRxStartTime_Type()
)
tnOthOdukStatsRxStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsRxStartTime.setStatus("current")
_TnOthOdukStatsRxNeBIP8ErrCnt_Type = Counter64
_TnOthOdukStatsRxNeBIP8ErrCnt_Object = MibTableColumn
tnOthOdukStatsRxNeBIP8ErrCnt = _TnOthOdukStatsRxNeBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 50, 1, 4),
    _TnOthOdukStatsRxNeBIP8ErrCnt_Type()
)
tnOthOdukStatsRxNeBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsRxNeBIP8ErrCnt.setStatus("current")
_TnOthOdukStatsRxNeES_Type = Counter64
_TnOthOdukStatsRxNeES_Object = MibTableColumn
tnOthOdukStatsRxNeES = _TnOthOdukStatsRxNeES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 50, 1, 5),
    _TnOthOdukStatsRxNeES_Type()
)
tnOthOdukStatsRxNeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsRxNeES.setStatus("current")
_TnOthOdukStatsRxNeSES_Type = Counter64
_TnOthOdukStatsRxNeSES_Object = MibTableColumn
tnOthOdukStatsRxNeSES = _TnOthOdukStatsRxNeSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 50, 1, 6),
    _TnOthOdukStatsRxNeSES_Type()
)
tnOthOdukStatsRxNeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsRxNeSES.setStatus("current")
_TnOthOdukStatsRxNeUAS_Type = Counter64
_TnOthOdukStatsRxNeUAS_Object = MibTableColumn
tnOthOdukStatsRxNeUAS = _TnOthOdukStatsRxNeUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 50, 1, 7),
    _TnOthOdukStatsRxNeUAS_Type()
)
tnOthOdukStatsRxNeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsRxNeUAS.setStatus("current")
_TnOthOdukStatsRxFeBIP8ErrCnt_Type = Counter64
_TnOthOdukStatsRxFeBIP8ErrCnt_Object = MibTableColumn
tnOthOdukStatsRxFeBIP8ErrCnt = _TnOthOdukStatsRxFeBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 50, 1, 8),
    _TnOthOdukStatsRxFeBIP8ErrCnt_Type()
)
tnOthOdukStatsRxFeBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsRxFeBIP8ErrCnt.setStatus("current")
_TnOthOdukStatsRxFeES_Type = Counter64
_TnOthOdukStatsRxFeES_Object = MibTableColumn
tnOthOdukStatsRxFeES = _TnOthOdukStatsRxFeES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 50, 1, 9),
    _TnOthOdukStatsRxFeES_Type()
)
tnOthOdukStatsRxFeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsRxFeES.setStatus("current")
_TnOthOdukStatsRxFeSES_Type = Counter64
_TnOthOdukStatsRxFeSES_Object = MibTableColumn
tnOthOdukStatsRxFeSES = _TnOthOdukStatsRxFeSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 50, 1, 10),
    _TnOthOdukStatsRxFeSES_Type()
)
tnOthOdukStatsRxFeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsRxFeSES.setStatus("current")
_TnOthOdukStatsRxFeUAS_Type = Counter64
_TnOthOdukStatsRxFeUAS_Object = MibTableColumn
tnOthOdukStatsRxFeUAS = _TnOthOdukStatsRxFeUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 50, 1, 11),
    _TnOthOdukStatsRxFeUAS_Type()
)
tnOthOdukStatsRxFeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsRxFeUAS.setStatus("current")
_TnOthOdukStatsTxTotalMembers_Type = Integer32
_TnOthOdukStatsTxTotalMembers_Object = MibScalar
tnOthOdukStatsTxTotalMembers = _TnOthOdukStatsTxTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 51),
    _TnOthOdukStatsTxTotalMembers_Type()
)
tnOthOdukStatsTxTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTxTotalMembers.setStatus("current")
_TnOthOdukStatsTxTable_Object = MibTable
tnOthOdukStatsTxTable = _TnOthOdukStatsTxTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 52)
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTxTable.setStatus("current")
_TnOthOdukStatsTxEntry_Object = MibTableRow
tnOthOdukStatsTxEntry = _TnOthOdukStatsTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 52, 1)
)
tnOthOdukStatsTxEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnOthOdukStatsBin"),
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTxEntry.setStatus("current")
_TnOthOdukStatsTxBinStatus_Type = TnStatsBinStatus
_TnOthOdukStatsTxBinStatus_Object = MibTableColumn
tnOthOdukStatsTxBinStatus = _TnOthOdukStatsTxBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 52, 1, 1),
    _TnOthOdukStatsTxBinStatus_Type()
)
tnOthOdukStatsTxBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTxBinStatus.setStatus("current")
_TnOthOdukStatsTxStartTime_Type = DateAndTime
_TnOthOdukStatsTxStartTime_Object = MibTableColumn
tnOthOdukStatsTxStartTime = _TnOthOdukStatsTxStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 52, 1, 2),
    _TnOthOdukStatsTxStartTime_Type()
)
tnOthOdukStatsTxStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTxStartTime.setStatus("current")
_TnOthOdukStatsTxNeBIP8ErrCnt_Type = Counter64
_TnOthOdukStatsTxNeBIP8ErrCnt_Object = MibTableColumn
tnOthOdukStatsTxNeBIP8ErrCnt = _TnOthOdukStatsTxNeBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 52, 1, 3),
    _TnOthOdukStatsTxNeBIP8ErrCnt_Type()
)
tnOthOdukStatsTxNeBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTxNeBIP8ErrCnt.setStatus("current")
_TnOthOdukStatsTxNeES_Type = Counter64
_TnOthOdukStatsTxNeES_Object = MibTableColumn
tnOthOdukStatsTxNeES = _TnOthOdukStatsTxNeES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 52, 1, 4),
    _TnOthOdukStatsTxNeES_Type()
)
tnOthOdukStatsTxNeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTxNeES.setStatus("current")
_TnOthOdukStatsTxNeSES_Type = Counter64
_TnOthOdukStatsTxNeSES_Object = MibTableColumn
tnOthOdukStatsTxNeSES = _TnOthOdukStatsTxNeSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 52, 1, 5),
    _TnOthOdukStatsTxNeSES_Type()
)
tnOthOdukStatsTxNeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTxNeSES.setStatus("current")
_TnOthOdukStatsTxNeUAS_Type = Counter64
_TnOthOdukStatsTxNeUAS_Object = MibTableColumn
tnOthOdukStatsTxNeUAS = _TnOthOdukStatsTxNeUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 52, 1, 6),
    _TnOthOdukStatsTxNeUAS_Type()
)
tnOthOdukStatsTxNeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTxNeUAS.setStatus("current")
_TnOthOdukStatsTxFeBIP8ErrCnt_Type = Counter64
_TnOthOdukStatsTxFeBIP8ErrCnt_Object = MibTableColumn
tnOthOdukStatsTxFeBIP8ErrCnt = _TnOthOdukStatsTxFeBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 52, 1, 7),
    _TnOthOdukStatsTxFeBIP8ErrCnt_Type()
)
tnOthOdukStatsTxFeBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTxFeBIP8ErrCnt.setStatus("current")
_TnOthOdukStatsTxFeES_Type = Counter64
_TnOthOdukStatsTxFeES_Object = MibTableColumn
tnOthOdukStatsTxFeES = _TnOthOdukStatsTxFeES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 52, 1, 8),
    _TnOthOdukStatsTxFeES_Type()
)
tnOthOdukStatsTxFeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTxFeES.setStatus("current")
_TnOthOdukStatsTxFeSES_Type = Counter64
_TnOthOdukStatsTxFeSES_Object = MibTableColumn
tnOthOdukStatsTxFeSES = _TnOthOdukStatsTxFeSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 52, 1, 9),
    _TnOthOdukStatsTxFeSES_Type()
)
tnOthOdukStatsTxFeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTxFeSES.setStatus("current")
_TnOthOdukStatsTxFeUAS_Type = Counter64
_TnOthOdukStatsTxFeUAS_Object = MibTableColumn
tnOthOdukStatsTxFeUAS = _TnOthOdukStatsTxFeUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 52, 1, 10),
    _TnOthOdukStatsTxFeUAS_Type()
)
tnOthOdukStatsTxFeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTxFeUAS.setStatus("current")
_TnOthOtukStatsTotalMembers_Type = Integer32
_TnOthOtukStatsTotalMembers_Object = MibScalar
tnOthOtukStatsTotalMembers = _TnOthOtukStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 53),
    _TnOthOtukStatsTotalMembers_Type()
)
tnOthOtukStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatsTotalMembers.setStatus("current")
_TnOthOtukStatsTable_Object = MibTable
tnOthOtukStatsTable = _TnOthOtukStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 54)
)
if mibBuilder.loadTexts:
    tnOthOtukStatsTable.setStatus("current")
_TnOthOtukStatsEntry_Object = MibTableRow
tnOthOtukStatsEntry = _TnOthOtukStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 54, 1)
)
tnOthOtukStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnOthOtukStatsBin"),
)
if mibBuilder.loadTexts:
    tnOthOtukStatsEntry.setStatus("current")
_TnOthOtukStatsBin_Type = TnStatsBinType
_TnOthOtukStatsBin_Object = MibTableColumn
tnOthOtukStatsBin = _TnOthOtukStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 54, 1, 1),
    _TnOthOtukStatsBin_Type()
)
tnOthOtukStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthOtukStatsBin.setStatus("current")
_TnOthOtukStatsBinStatus_Type = TnStatsBinStatus
_TnOthOtukStatsBinStatus_Object = MibTableColumn
tnOthOtukStatsBinStatus = _TnOthOtukStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 54, 1, 2),
    _TnOthOtukStatsBinStatus_Type()
)
tnOthOtukStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatsBinStatus.setStatus("current")
_TnOthOtukStatsStartTime_Type = DateAndTime
_TnOthOtukStatsStartTime_Object = MibTableColumn
tnOthOtukStatsStartTime = _TnOthOtukStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 54, 1, 3),
    _TnOthOtukStatsStartTime_Type()
)
tnOthOtukStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatsStartTime.setStatus("current")
_TnOthOtukStatRxRsCorrCnt_Type = Counter64
_TnOthOtukStatRxRsCorrCnt_Object = MibTableColumn
tnOthOtukStatRxRsCorrCnt = _TnOthOtukStatRxRsCorrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 54, 1, 4),
    _TnOthOtukStatRxRsCorrCnt_Type()
)
tnOthOtukStatRxRsCorrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxRsCorrCnt.setStatus("current")
_TnOthOtukStatRxRsUncorrCnt_Type = Counter64
_TnOthOtukStatRxRsUncorrCnt_Object = MibTableColumn
tnOthOtukStatRxRsUncorrCnt = _TnOthOtukStatRxRsUncorrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 54, 1, 5),
    _TnOthOtukStatRxRsUncorrCnt_Type()
)
tnOthOtukStatRxRsUncorrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxRsUncorrCnt.setStatus("current")
_TnOthOtukStatRxBERPreFEC_Type = Counter64
_TnOthOtukStatRxBERPreFEC_Object = MibTableColumn
tnOthOtukStatRxBERPreFEC = _TnOthOtukStatRxBERPreFEC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 54, 1, 6),
    _TnOthOtukStatRxBERPreFEC_Type()
)
tnOthOtukStatRxBERPreFEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxBERPreFEC.setStatus("current")
_TnOthOtukStatRxBERPostFEC_Type = Counter64
_TnOthOtukStatRxBERPostFEC_Object = MibTableColumn
tnOthOtukStatRxBERPostFEC = _TnOthOtukStatRxBERPostFEC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 54, 1, 7),
    _TnOthOtukStatRxBERPostFEC_Type()
)
tnOthOtukStatRxBERPostFEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxBERPostFEC.setStatus("current")
_TnOthOtukStatNeRxSMBIP8ErrCnt_Type = Counter64
_TnOthOtukStatNeRxSMBIP8ErrCnt_Object = MibTableColumn
tnOthOtukStatNeRxSMBIP8ErrCnt = _TnOthOtukStatNeRxSMBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 54, 1, 8),
    _TnOthOtukStatNeRxSMBIP8ErrCnt_Type()
)
tnOthOtukStatNeRxSMBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatNeRxSMBIP8ErrCnt.setStatus("current")
_TnOthOtukStatNeRxBIAESErrCnt_Type = Counter64
_TnOthOtukStatNeRxBIAESErrCnt_Object = MibTableColumn
tnOthOtukStatNeRxBIAESErrCnt = _TnOthOtukStatNeRxBIAESErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 54, 1, 9),
    _TnOthOtukStatNeRxBIAESErrCnt_Type()
)
tnOthOtukStatNeRxBIAESErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatNeRxBIAESErrCnt.setStatus("current")
_TnOthOtukStatNeRxSMES_Type = Counter64
_TnOthOtukStatNeRxSMES_Object = MibTableColumn
tnOthOtukStatNeRxSMES = _TnOthOtukStatNeRxSMES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 54, 1, 10),
    _TnOthOtukStatNeRxSMES_Type()
)
tnOthOtukStatNeRxSMES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatNeRxSMES.setStatus("current")
_TnOthOtukStatNeRxSMSES_Type = Counter64
_TnOthOtukStatNeRxSMSES_Object = MibTableColumn
tnOthOtukStatNeRxSMSES = _TnOthOtukStatNeRxSMSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 54, 1, 11),
    _TnOthOtukStatNeRxSMSES_Type()
)
tnOthOtukStatNeRxSMSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatNeRxSMSES.setStatus("current")
_TnOthOtukStatNeRxSMUAS_Type = Counter64
_TnOthOtukStatNeRxSMUAS_Object = MibTableColumn
tnOthOtukStatNeRxSMUAS = _TnOthOtukStatNeRxSMUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 54, 1, 12),
    _TnOthOtukStatNeRxSMUAS_Type()
)
tnOthOtukStatNeRxSMUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatNeRxSMUAS.setStatus("current")
_TnOthOtukStatNeRxIAES_Type = Counter64
_TnOthOtukStatNeRxIAES_Object = MibTableColumn
tnOthOtukStatNeRxIAES = _TnOthOtukStatNeRxIAES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 54, 1, 13),
    _TnOthOtukStatNeRxIAES_Type()
)
tnOthOtukStatNeRxIAES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatNeRxIAES.setStatus("current")
_TnOthOtukStatFeRxSMBIP8ErrCnt_Type = Counter64
_TnOthOtukStatFeRxSMBIP8ErrCnt_Object = MibTableColumn
tnOthOtukStatFeRxSMBIP8ErrCnt = _TnOthOtukStatFeRxSMBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 54, 1, 14),
    _TnOthOtukStatFeRxSMBIP8ErrCnt_Type()
)
tnOthOtukStatFeRxSMBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatFeRxSMBIP8ErrCnt.setStatus("current")
_TnOthOtukStatFeRxSMES_Type = Counter64
_TnOthOtukStatFeRxSMES_Object = MibTableColumn
tnOthOtukStatFeRxSMES = _TnOthOtukStatFeRxSMES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 54, 1, 15),
    _TnOthOtukStatFeRxSMES_Type()
)
tnOthOtukStatFeRxSMES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatFeRxSMES.setStatus("current")
_TnOthOtukStatFeRxSMSES_Type = Counter64
_TnOthOtukStatFeRxSMSES_Object = MibTableColumn
tnOthOtukStatFeRxSMSES = _TnOthOtukStatFeRxSMSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 54, 1, 16),
    _TnOthOtukStatFeRxSMSES_Type()
)
tnOthOtukStatFeRxSMSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatFeRxSMSES.setStatus("current")
_TnOthOtukStatFeRxSMUAS_Type = Counter64
_TnOthOtukStatFeRxSMUAS_Object = MibTableColumn
tnOthOtukStatFeRxSMUAS = _TnOthOtukStatFeRxSMUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 54, 1, 17),
    _TnOthOtukStatFeRxSMUAS_Type()
)
tnOthOtukStatFeRxSMUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatFeRxSMUAS.setStatus("current")
_TnOthOtukStatFeRxIAES_Type = Counter64
_TnOthOtukStatFeRxIAES_Object = MibTableColumn
tnOthOtukStatFeRxIAES = _TnOthOtukStatFeRxIAES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 54, 1, 18),
    _TnOthOtukStatFeRxIAES_Type()
)
tnOthOtukStatFeRxIAES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatFeRxIAES.setStatus("current")
_TnOsnrStatsTotalMembers_Type = Integer32
_TnOsnrStatsTotalMembers_Object = MibScalar
tnOsnrStatsTotalMembers = _TnOsnrStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 55),
    _TnOsnrStatsTotalMembers_Type()
)
tnOsnrStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOsnrStatsTotalMembers.setStatus("current")
_TnOsnrStatsTable_Object = MibTable
tnOsnrStatsTable = _TnOsnrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 56)
)
if mibBuilder.loadTexts:
    tnOsnrStatsTable.setStatus("current")
_TnOsnrStatsEntry_Object = MibTableRow
tnOsnrStatsEntry = _TnOsnrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 56, 1)
)
tnOsnrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnOpticalStatsITUChannel"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnOsnrStatsBin"),
)
if mibBuilder.loadTexts:
    tnOsnrStatsEntry.setStatus("current")
_TnOsnrStatsBin_Type = TnStatsBinType
_TnOsnrStatsBin_Object = MibTableColumn
tnOsnrStatsBin = _TnOsnrStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 56, 1, 1),
    _TnOsnrStatsBin_Type()
)
tnOsnrStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOsnrStatsBin.setStatus("current")
_TnOsnrStatsBinStatus_Type = TnStatsBinStatus
_TnOsnrStatsBinStatus_Object = MibTableColumn
tnOsnrStatsBinStatus = _TnOsnrStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 56, 1, 2),
    _TnOsnrStatsBinStatus_Type()
)
tnOsnrStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOsnrStatsBinStatus.setStatus("current")
_TnOsnrStatsStartTime_Type = DateAndTime
_TnOsnrStatsStartTime_Object = MibTableColumn
tnOsnrStatsStartTime = _TnOsnrStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 56, 1, 3),
    _TnOsnrStatsStartTime_Type()
)
tnOsnrStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOsnrStatsStartTime.setStatus("current")
_TnOsnrStatMinOSNR_Type = Integer32
_TnOsnrStatMinOSNR_Object = MibTableColumn
tnOsnrStatMinOSNR = _TnOsnrStatMinOSNR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 56, 1, 4),
    _TnOsnrStatMinOSNR_Type()
)
tnOsnrStatMinOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOsnrStatMinOSNR.setStatus("current")
if mibBuilder.loadTexts:
    tnOsnrStatMinOSNR.setUnits("mB")
_TnOsnrStatMaxOSNR_Type = Integer32
_TnOsnrStatMaxOSNR_Object = MibTableColumn
tnOsnrStatMaxOSNR = _TnOsnrStatMaxOSNR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 56, 1, 5),
    _TnOsnrStatMaxOSNR_Type()
)
tnOsnrStatMaxOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOsnrStatMaxOSNR.setStatus("current")
if mibBuilder.loadTexts:
    tnOsnrStatMaxOSNR.setUnits("mB")
_TnOsnrStatAverageOSNR_Type = Integer32
_TnOsnrStatAverageOSNR_Object = MibTableColumn
tnOsnrStatAverageOSNR = _TnOsnrStatAverageOSNR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 56, 1, 6),
    _TnOsnrStatAverageOSNR_Type()
)
tnOsnrStatAverageOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOsnrStatAverageOSNR.setStatus("current")
if mibBuilder.loadTexts:
    tnOsnrStatAverageOSNR.setUnits("mB")


class _TnOsnrStatStatusOSNR_Type(Integer32):
    """Custom type tnOsnrStatStatusOSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("update", 1),
          ("noUpdate", 2))
    )


_TnOsnrStatStatusOSNR_Type.__name__ = "Integer32"
_TnOsnrStatStatusOSNR_Object = MibTableColumn
tnOsnrStatStatusOSNR = _TnOsnrStatStatusOSNR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 56, 1, 7),
    _TnOsnrStatStatusOSNR_Type()
)
tnOsnrStatStatusOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOsnrStatStatusOSNR.setStatus("current")
_TnOthOdukStatsDMTotalMembers_Type = Integer32
_TnOthOdukStatsDMTotalMembers_Object = MibScalar
tnOthOdukStatsDMTotalMembers = _TnOthOdukStatsDMTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 57),
    _TnOthOdukStatsDMTotalMembers_Type()
)
tnOthOdukStatsDMTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsDMTotalMembers.setStatus("current")
_TnOthOdukStatsDMTable_Object = MibTable
tnOthOdukStatsDMTable = _TnOthOdukStatsDMTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 58)
)
if mibBuilder.loadTexts:
    tnOthOdukStatsDMTable.setStatus("current")
_TnOthOdukStatsDMEntry_Object = MibTableRow
tnOthOdukStatsDMEntry = _TnOthOdukStatsDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 58, 1)
)
tnOthOdukStatsDMEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnOthOdukStatsBin"),
)
if mibBuilder.loadTexts:
    tnOthOdukStatsDMEntry.setStatus("current")
_TnOthOdukStatsDMBinStatus_Type = TnStatsBinStatus
_TnOthOdukStatsDMBinStatus_Object = MibTableColumn
tnOthOdukStatsDMBinStatus = _TnOthOdukStatsDMBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 58, 1, 1),
    _TnOthOdukStatsDMBinStatus_Type()
)
tnOthOdukStatsDMBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsDMBinStatus.setStatus("current")
_TnOthOdukStatsDMStartTime_Type = DateAndTime
_TnOthOdukStatsDMStartTime_Object = MibTableColumn
tnOthOdukStatsDMStartTime = _TnOthOdukStatsDMStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 58, 1, 2),
    _TnOthOdukStatsDMStartTime_Type()
)
tnOthOdukStatsDMStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsDMStartTime.setStatus("current")
_TnOthOdukStatsDMMinDm_Type = Integer32
_TnOthOdukStatsDMMinDm_Object = MibTableColumn
tnOthOdukStatsDMMinDm = _TnOthOdukStatsDMMinDm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 58, 1, 3),
    _TnOthOdukStatsDMMinDm_Type()
)
tnOthOdukStatsDMMinDm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsDMMinDm.setStatus("current")
if mibBuilder.loadTexts:
    tnOthOdukStatsDMMinDm.setUnits("us")
_TnOthOdukStatsDMMaxDm_Type = Integer32
_TnOthOdukStatsDMMaxDm_Object = MibTableColumn
tnOthOdukStatsDMMaxDm = _TnOthOdukStatsDMMaxDm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 58, 1, 4),
    _TnOthOdukStatsDMMaxDm_Type()
)
tnOthOdukStatsDMMaxDm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsDMMaxDm.setStatus("current")
if mibBuilder.loadTexts:
    tnOthOdukStatsDMMaxDm.setUnits("us")
_TnOthOdukStatsDMAverageDm_Type = Integer32
_TnOthOdukStatsDMAverageDm_Object = MibTableColumn
tnOthOdukStatsDMAverageDm = _TnOthOdukStatsDMAverageDm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 58, 1, 5),
    _TnOthOdukStatsDMAverageDm_Type()
)
tnOthOdukStatsDMAverageDm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsDMAverageDm.setStatus("current")
if mibBuilder.loadTexts:
    tnOthOdukStatsDMAverageDm.setUnits("us")
_TnOthOdukStatsTcmTotalMembers_Type = Integer32
_TnOthOdukStatsTcmTotalMembers_Object = MibScalar
tnOthOdukStatsTcmTotalMembers = _TnOthOdukStatsTcmTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 59),
    _TnOthOdukStatsTcmTotalMembers_Type()
)
tnOthOdukStatsTcmTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmTotalMembers.setStatus("current")
_TnOthOdukStatsTcmTable_Object = MibTable
tnOthOdukStatsTcmTable = _TnOthOdukStatsTcmTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 60)
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmTable.setStatus("current")
_TnOthOdukStatsTcmEntry_Object = MibTableRow
tnOthOdukStatsTcmEntry = _TnOthOdukStatsTcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 60, 1)
)
tnOthOdukStatsTcmEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthOdukTcmIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthOdukTcmIfIndexLo"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
    (0, "TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmBin"),
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmEntry.setStatus("current")
_TnOthOdukStatsTcmBin_Type = TnStatsBinType
_TnOthOdukStatsTcmBin_Object = MibTableColumn
tnOthOdukStatsTcmBin = _TnOthOdukStatsTcmBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 60, 1, 1),
    _TnOthOdukStatsTcmBin_Type()
)
tnOthOdukStatsTcmBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmBin.setStatus("current")
_TnOthOdukStatsTcmBinStatus_Type = TnStatsBinType
_TnOthOdukStatsTcmBinStatus_Object = MibTableColumn
tnOthOdukStatsTcmBinStatus = _TnOthOdukStatsTcmBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 60, 1, 2),
    _TnOthOdukStatsTcmBinStatus_Type()
)
tnOthOdukStatsTcmBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmBinStatus.setStatus("current")
_TnOthOdukStatsTcmStartTime_Type = DateAndTime
_TnOthOdukStatsTcmStartTime_Object = MibTableColumn
tnOthOdukStatsTcmStartTime = _TnOthOdukStatsTcmStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 60, 1, 3),
    _TnOthOdukStatsTcmStartTime_Type()
)
tnOthOdukStatsTcmStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmStartTime.setStatus("current")
_TnOthOdukStatsTcmNeRxBIP8ErrCnt_Type = Counter64
_TnOthOdukStatsTcmNeRxBIP8ErrCnt_Object = MibTableColumn
tnOthOdukStatsTcmNeRxBIP8ErrCnt = _TnOthOdukStatsTcmNeRxBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 60, 1, 4),
    _TnOthOdukStatsTcmNeRxBIP8ErrCnt_Type()
)
tnOthOdukStatsTcmNeRxBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmNeRxBIP8ErrCnt.setStatus("current")
_TnOthOdukStatsTcmNeRxIAESErrCnt_Type = Counter64
_TnOthOdukStatsTcmNeRxIAESErrCnt_Object = MibTableColumn
tnOthOdukStatsTcmNeRxIAESErrCnt = _TnOthOdukStatsTcmNeRxIAESErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 60, 1, 5),
    _TnOthOdukStatsTcmNeRxIAESErrCnt_Type()
)
tnOthOdukStatsTcmNeRxIAESErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmNeRxIAESErrCnt.setStatus("current")
_TnOthOdukStatsTcmNeRxES_Type = Counter64
_TnOthOdukStatsTcmNeRxES_Object = MibTableColumn
tnOthOdukStatsTcmNeRxES = _TnOthOdukStatsTcmNeRxES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 60, 1, 6),
    _TnOthOdukStatsTcmNeRxES_Type()
)
tnOthOdukStatsTcmNeRxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmNeRxES.setStatus("current")
_TnOthOdukStatsTcmNeRxSES_Type = Counter64
_TnOthOdukStatsTcmNeRxSES_Object = MibTableColumn
tnOthOdukStatsTcmNeRxSES = _TnOthOdukStatsTcmNeRxSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 60, 1, 7),
    _TnOthOdukStatsTcmNeRxSES_Type()
)
tnOthOdukStatsTcmNeRxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmNeRxSES.setStatus("current")
_TnOthOdukStatsTcmNeRxUAS_Type = Counter64
_TnOthOdukStatsTcmNeRxUAS_Object = MibTableColumn
tnOthOdukStatsTcmNeRxUAS = _TnOthOdukStatsTcmNeRxUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 60, 1, 8),
    _TnOthOdukStatsTcmNeRxUAS_Type()
)
tnOthOdukStatsTcmNeRxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmNeRxUAS.setStatus("current")
_TnOthOdukStatsTcmFeRxBIP8ErrCnt_Type = Counter64
_TnOthOdukStatsTcmFeRxBIP8ErrCnt_Object = MibTableColumn
tnOthOdukStatsTcmFeRxBIP8ErrCnt = _TnOthOdukStatsTcmFeRxBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 60, 1, 9),
    _TnOthOdukStatsTcmFeRxBIP8ErrCnt_Type()
)
tnOthOdukStatsTcmFeRxBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmFeRxBIP8ErrCnt.setStatus("current")
_TnOthOdukStatsTcmFeRxBIAESErrCnt_Type = Counter64
_TnOthOdukStatsTcmFeRxBIAESErrCnt_Object = MibTableColumn
tnOthOdukStatsTcmFeRxBIAESErrCnt = _TnOthOdukStatsTcmFeRxBIAESErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 60, 1, 10),
    _TnOthOdukStatsTcmFeRxBIAESErrCnt_Type()
)
tnOthOdukStatsTcmFeRxBIAESErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmFeRxBIAESErrCnt.setStatus("current")
_TnOthOdukStatsTcmFeRxES_Type = Counter64
_TnOthOdukStatsTcmFeRxES_Object = MibTableColumn
tnOthOdukStatsTcmFeRxES = _TnOthOdukStatsTcmFeRxES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 60, 1, 11),
    _TnOthOdukStatsTcmFeRxES_Type()
)
tnOthOdukStatsTcmFeRxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmFeRxES.setStatus("current")
_TnOthOdukStatsTcmFeRxSES_Type = Counter64
_TnOthOdukStatsTcmFeRxSES_Object = MibTableColumn
tnOthOdukStatsTcmFeRxSES = _TnOthOdukStatsTcmFeRxSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 60, 1, 12),
    _TnOthOdukStatsTcmFeRxSES_Type()
)
tnOthOdukStatsTcmFeRxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmFeRxSES.setStatus("current")
_TnOthOdukStatsTcmFeRxUAS_Type = Counter64
_TnOthOdukStatsTcmFeRxUAS_Object = MibTableColumn
tnOthOdukStatsTcmFeRxUAS = _TnOthOdukStatsTcmFeRxUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 2, 60, 1, 13),
    _TnOthOdukStatsTcmFeRxUAS_Type()
)
tnOthOdukStatsTcmFeRxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmFeRxUAS.setStatus("current")
_TnStatisticsRawCounts_ObjectIdentity = ObjectIdentity
tnStatisticsRawCounts = _TnStatisticsRawCounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3)
)
_TnControlNetworkLinkRawCountStatsTotalMembers_Type = Integer32
_TnControlNetworkLinkRawCountStatsTotalMembers_Object = MibScalar
tnControlNetworkLinkRawCountStatsTotalMembers = _TnControlNetworkLinkRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 1),
    _TnControlNetworkLinkRawCountStatsTotalMembers_Type()
)
tnControlNetworkLinkRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnControlNetworkLinkRawCountStatsTotalMembers.setStatus("current")
_TnControlNetworkLinkRawCountStatsTable_Object = MibTable
tnControlNetworkLinkRawCountStatsTable = _TnControlNetworkLinkRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    tnControlNetworkLinkRawCountStatsTable.setStatus("current")
_TnControlNetworkLinkRawCountStatsEntry_Object = MibTableRow
tnControlNetworkLinkRawCountStatsEntry = _TnControlNetworkLinkRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 2, 1)
)
tnControlNetworkLinkRawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnControlNetworkLinkRawCountStatsEntry.setStatus("current")
_TnCNLinkRawCountStatIpInReceives_Type = Counter32
_TnCNLinkRawCountStatIpInReceives_Object = MibTableColumn
tnCNLinkRawCountStatIpInReceives = _TnCNLinkRawCountStatIpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 2, 1, 1),
    _TnCNLinkRawCountStatIpInReceives_Type()
)
tnCNLinkRawCountStatIpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNLinkRawCountStatIpInReceives.setStatus("current")
_TnCNLinkRawCountStatIpInDiscards_Type = Counter32
_TnCNLinkRawCountStatIpInDiscards_Object = MibTableColumn
tnCNLinkRawCountStatIpInDiscards = _TnCNLinkRawCountStatIpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 2, 1, 2),
    _TnCNLinkRawCountStatIpInDiscards_Type()
)
tnCNLinkRawCountStatIpInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNLinkRawCountStatIpInDiscards.setStatus("current")
_TnCNLinkRawCountStatIpOutRequests_Type = Counter32
_TnCNLinkRawCountStatIpOutRequests_Object = MibTableColumn
tnCNLinkRawCountStatIpOutRequests = _TnCNLinkRawCountStatIpOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 2, 1, 3),
    _TnCNLinkRawCountStatIpOutRequests_Type()
)
tnCNLinkRawCountStatIpOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNLinkRawCountStatIpOutRequests.setStatus("current")
_TnCNLinkRawCountStatIpOutDiscards_Type = Counter32
_TnCNLinkRawCountStatIpOutDiscards_Object = MibTableColumn
tnCNLinkRawCountStatIpOutDiscards = _TnCNLinkRawCountStatIpOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 2, 1, 4),
    _TnCNLinkRawCountStatIpOutDiscards_Type()
)
tnCNLinkRawCountStatIpOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNLinkRawCountStatIpOutDiscards.setStatus("current")
_TnCNLinkRawCountStatIpForwDatagrams_Type = Counter32
_TnCNLinkRawCountStatIpForwDatagrams_Object = MibTableColumn
tnCNLinkRawCountStatIpForwDatagrams = _TnCNLinkRawCountStatIpForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 2, 1, 5),
    _TnCNLinkRawCountStatIpForwDatagrams_Type()
)
tnCNLinkRawCountStatIpForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNLinkRawCountStatIpForwDatagrams.setStatus("current")
_TnCardRawCountStatsTotalMembers_Type = Integer32
_TnCardRawCountStatsTotalMembers_Object = MibScalar
tnCardRawCountStatsTotalMembers = _TnCardRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 3),
    _TnCardRawCountStatsTotalMembers_Type()
)
tnCardRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardRawCountStatsTotalMembers.setStatus("current")
_TnCardRawCountStatsTable_Object = MibTable
tnCardRawCountStatsTable = _TnCardRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 4)
)
if mibBuilder.loadTexts:
    tnCardRawCountStatsTable.setStatus("current")
_TnCardRawCountStatsEntry_Object = MibTableRow
tnCardRawCountStatsEntry = _TnCardRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 4, 1)
)
tnCardRawCountStatsEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnCardStatsProcessor"),
)
if mibBuilder.loadTexts:
    tnCardRawCountStatsEntry.setStatus("current")
_TnCardRawCountStatsClear_Type = TnCommand
_TnCardRawCountStatsClear_Object = MibTableColumn
tnCardRawCountStatsClear = _TnCardRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 4, 1, 1),
    _TnCardRawCountStatsClear_Type()
)
tnCardRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardRawCountStatsClear.setStatus("current")
_TnCardRawCountStatCpuAverage_Type = Counter32
_TnCardRawCountStatCpuAverage_Object = MibTableColumn
tnCardRawCountStatCpuAverage = _TnCardRawCountStatCpuAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 4, 1, 2),
    _TnCardRawCountStatCpuAverage_Type()
)
tnCardRawCountStatCpuAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardRawCountStatCpuAverage.setStatus("current")
_TnCardRawCountStatHeapUsage_Type = Counter32
_TnCardRawCountStatHeapUsage_Object = MibTableColumn
tnCardRawCountStatHeapUsage = _TnCardRawCountStatHeapUsage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 4, 1, 3),
    _TnCardRawCountStatHeapUsage_Type()
)
tnCardRawCountStatHeapUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardRawCountStatHeapUsage.setStatus("current")
_TnCardRawCountStatPoolUsage_Type = Counter32
_TnCardRawCountStatPoolUsage_Object = MibTableColumn
tnCardRawCountStatPoolUsage = _TnCardRawCountStatPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 4, 1, 4),
    _TnCardRawCountStatPoolUsage_Type()
)
tnCardRawCountStatPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardRawCountStatPoolUsage.setStatus("current")
_TnCardRawCountStatStartTime_Type = DateAndTime
_TnCardRawCountStatStartTime_Object = MibTableColumn
tnCardRawCountStatStartTime = _TnCardRawCountStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 4, 1, 5),
    _TnCardRawCountStatStartTime_Type()
)
tnCardRawCountStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardRawCountStatStartTime.setStatus("current")
_TnInterfaceRawCountStatsTotalMembers_Type = Integer32
_TnInterfaceRawCountStatsTotalMembers_Object = MibScalar
tnInterfaceRawCountStatsTotalMembers = _TnInterfaceRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 5),
    _TnInterfaceRawCountStatsTotalMembers_Type()
)
tnInterfaceRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnInterfaceRawCountStatsTotalMembers.setStatus("current")
_TnInterfaceRawCountStatsTable_Object = MibTable
tnInterfaceRawCountStatsTable = _TnInterfaceRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 6)
)
if mibBuilder.loadTexts:
    tnInterfaceRawCountStatsTable.setStatus("current")
_TnInterfaceRawCountStatsEntry_Object = MibTableRow
tnInterfaceRawCountStatsEntry = _TnInterfaceRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 6, 1)
)
tnInterfaceRawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnInterfaceRawCountStatsEntry.setStatus("current")
_TnIfRawCountStatsClear_Type = TnCommand
_TnIfRawCountStatsClear_Object = MibTableColumn
tnIfRawCountStatsClear = _TnIfRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 6, 1, 1),
    _TnIfRawCountStatsClear_Type()
)
tnIfRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIfRawCountStatsClear.setStatus("current")
_TnIfRawCountStatInOctets_Type = Counter64
_TnIfRawCountStatInOctets_Object = MibTableColumn
tnIfRawCountStatInOctets = _TnIfRawCountStatInOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 6, 1, 2),
    _TnIfRawCountStatInOctets_Type()
)
tnIfRawCountStatInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfRawCountStatInOctets.setStatus("current")
_TnIfRawCountStatInUcastPkts_Type = Counter64
_TnIfRawCountStatInUcastPkts_Object = MibTableColumn
tnIfRawCountStatInUcastPkts = _TnIfRawCountStatInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 6, 1, 3),
    _TnIfRawCountStatInUcastPkts_Type()
)
tnIfRawCountStatInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfRawCountStatInUcastPkts.setStatus("current")
_TnIfRawCountStatInDiscards_Type = Counter64
_TnIfRawCountStatInDiscards_Object = MibTableColumn
tnIfRawCountStatInDiscards = _TnIfRawCountStatInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 6, 1, 4),
    _TnIfRawCountStatInDiscards_Type()
)
tnIfRawCountStatInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfRawCountStatInDiscards.setStatus("current")
_TnIfRawCountStatInErrors_Type = Counter64
_TnIfRawCountStatInErrors_Object = MibTableColumn
tnIfRawCountStatInErrors = _TnIfRawCountStatInErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 6, 1, 5),
    _TnIfRawCountStatInErrors_Type()
)
tnIfRawCountStatInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfRawCountStatInErrors.setStatus("current")
_TnIfRawCountStatInUnknownProtos_Type = Counter64
_TnIfRawCountStatInUnknownProtos_Object = MibTableColumn
tnIfRawCountStatInUnknownProtos = _TnIfRawCountStatInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 6, 1, 6),
    _TnIfRawCountStatInUnknownProtos_Type()
)
tnIfRawCountStatInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfRawCountStatInUnknownProtos.setStatus("current")
_TnIfRawCountStatOutOctets_Type = Counter64
_TnIfRawCountStatOutOctets_Object = MibTableColumn
tnIfRawCountStatOutOctets = _TnIfRawCountStatOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 6, 1, 7),
    _TnIfRawCountStatOutOctets_Type()
)
tnIfRawCountStatOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfRawCountStatOutOctets.setStatus("current")
_TnIfRawCountStatOutUcastPkts_Type = Counter64
_TnIfRawCountStatOutUcastPkts_Object = MibTableColumn
tnIfRawCountStatOutUcastPkts = _TnIfRawCountStatOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 6, 1, 8),
    _TnIfRawCountStatOutUcastPkts_Type()
)
tnIfRawCountStatOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfRawCountStatOutUcastPkts.setStatus("current")
_TnIfRawCountStatOutDiscards_Type = Counter64
_TnIfRawCountStatOutDiscards_Object = MibTableColumn
tnIfRawCountStatOutDiscards = _TnIfRawCountStatOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 6, 1, 9),
    _TnIfRawCountStatOutDiscards_Type()
)
tnIfRawCountStatOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfRawCountStatOutDiscards.setStatus("current")
_TnIfRawCountStatOutErrors_Type = Counter64
_TnIfRawCountStatOutErrors_Object = MibTableColumn
tnIfRawCountStatOutErrors = _TnIfRawCountStatOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 6, 1, 10),
    _TnIfRawCountStatOutErrors_Type()
)
tnIfRawCountStatOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfRawCountStatOutErrors.setStatus("current")
_TnIfRawCountStatInMulticastPkts_Type = Counter64
_TnIfRawCountStatInMulticastPkts_Object = MibTableColumn
tnIfRawCountStatInMulticastPkts = _TnIfRawCountStatInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 6, 1, 11),
    _TnIfRawCountStatInMulticastPkts_Type()
)
tnIfRawCountStatInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfRawCountStatInMulticastPkts.setStatus("current")
_TnIfRawCountStatInBroadcastPkts_Type = Counter64
_TnIfRawCountStatInBroadcastPkts_Object = MibTableColumn
tnIfRawCountStatInBroadcastPkts = _TnIfRawCountStatInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 6, 1, 12),
    _TnIfRawCountStatInBroadcastPkts_Type()
)
tnIfRawCountStatInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfRawCountStatInBroadcastPkts.setStatus("current")
_TnIfRawCountStatOutMulticastPkts_Type = Counter64
_TnIfRawCountStatOutMulticastPkts_Object = MibTableColumn
tnIfRawCountStatOutMulticastPkts = _TnIfRawCountStatOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 6, 1, 13),
    _TnIfRawCountStatOutMulticastPkts_Type()
)
tnIfRawCountStatOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfRawCountStatOutMulticastPkts.setStatus("current")
_TnIfRawCountStatOutBroadcastPkts_Type = Counter64
_TnIfRawCountStatOutBroadcastPkts_Object = MibTableColumn
tnIfRawCountStatOutBroadcastPkts = _TnIfRawCountStatOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 6, 1, 14),
    _TnIfRawCountStatOutBroadcastPkts_Type()
)
tnIfRawCountStatOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfRawCountStatOutBroadcastPkts.setStatus("current")
_TnIfRawCountStatInPacketsNotClassified_Type = Counter64
_TnIfRawCountStatInPacketsNotClassified_Object = MibTableColumn
tnIfRawCountStatInPacketsNotClassified = _TnIfRawCountStatInPacketsNotClassified_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 6, 1, 15),
    _TnIfRawCountStatInPacketsNotClassified_Type()
)
tnIfRawCountStatInPacketsNotClassified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfRawCountStatInPacketsNotClassified.setStatus("current")
_TnIfRawCountStatStartTime_Type = DateAndTime
_TnIfRawCountStatStartTime_Object = MibTableColumn
tnIfRawCountStatStartTime = _TnIfRawCountStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 6, 1, 16),
    _TnIfRawCountStatStartTime_Type()
)
tnIfRawCountStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfRawCountStatStartTime.setStatus("current")
_TnEtherRawCountStatsTotalMembers_Type = Integer32
_TnEtherRawCountStatsTotalMembers_Object = MibScalar
tnEtherRawCountStatsTotalMembers = _TnEtherRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 7),
    _TnEtherRawCountStatsTotalMembers_Type()
)
tnEtherRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatsTotalMembers.setStatus("current")
_TnEtherRawCountStatsTable_Object = MibTable
tnEtherRawCountStatsTable = _TnEtherRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8)
)
if mibBuilder.loadTexts:
    tnEtherRawCountStatsTable.setStatus("current")
_TnEtherRawCountStatsEntry_Object = MibTableRow
tnEtherRawCountStatsEntry = _TnEtherRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1)
)
tnEtherRawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnEtherRawCountStatsEntry.setStatus("current")
_TnEtherRawCountStatsClear_Type = TnCommand
_TnEtherRawCountStatsClear_Object = MibTableColumn
tnEtherRawCountStatsClear = _TnEtherRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 1),
    _TnEtherRawCountStatsClear_Type()
)
tnEtherRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEtherRawCountStatsClear.setStatus("current")
_TnEtherRawCountStatRxDropEvents_Type = Counter64
_TnEtherRawCountStatRxDropEvents_Object = MibTableColumn
tnEtherRawCountStatRxDropEvents = _TnEtherRawCountStatRxDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 2),
    _TnEtherRawCountStatRxDropEvents_Type()
)
tnEtherRawCountStatRxDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatRxDropEvents.setStatus("current")
_TnEtherRawCountStatRxFragments_Type = Counter64
_TnEtherRawCountStatRxFragments_Object = MibTableColumn
tnEtherRawCountStatRxFragments = _TnEtherRawCountStatRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 3),
    _TnEtherRawCountStatRxFragments_Type()
)
tnEtherRawCountStatRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatRxFragments.setStatus("current")
_TnEtherRawCountStatRxJabbers_Type = Counter64
_TnEtherRawCountStatRxJabbers_Object = MibTableColumn
tnEtherRawCountStatRxJabbers = _TnEtherRawCountStatRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 4),
    _TnEtherRawCountStatRxJabbers_Type()
)
tnEtherRawCountStatRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatRxJabbers.setStatus("current")
_TnEtherRawCountStatRxMcastPkts_Type = Counter64
_TnEtherRawCountStatRxMcastPkts_Object = MibTableColumn
tnEtherRawCountStatRxMcastPkts = _TnEtherRawCountStatRxMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 5),
    _TnEtherRawCountStatRxMcastPkts_Type()
)
tnEtherRawCountStatRxMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatRxMcastPkts.setStatus("current")
_TnEtherRawCountStatRxOctets_Type = Counter64
_TnEtherRawCountStatRxOctets_Object = MibTableColumn
tnEtherRawCountStatRxOctets = _TnEtherRawCountStatRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 6),
    _TnEtherRawCountStatRxOctets_Type()
)
tnEtherRawCountStatRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatRxOctets.setStatus("current")
_TnEtherRawCountStatRxOversizedPkts_Type = Counter64
_TnEtherRawCountStatRxOversizedPkts_Object = MibTableColumn
tnEtherRawCountStatRxOversizedPkts = _TnEtherRawCountStatRxOversizedPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 7),
    _TnEtherRawCountStatRxOversizedPkts_Type()
)
tnEtherRawCountStatRxOversizedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatRxOversizedPkts.setStatus("current")
_TnEtherRawCountStatRxPkts_Type = Counter64
_TnEtherRawCountStatRxPkts_Object = MibTableColumn
tnEtherRawCountStatRxPkts = _TnEtherRawCountStatRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 8),
    _TnEtherRawCountStatRxPkts_Type()
)
tnEtherRawCountStatRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatRxPkts.setStatus("current")
_TnEtherRawCountStatRxPktsSize1024to1518_Type = Counter64
_TnEtherRawCountStatRxPktsSize1024to1518_Object = MibTableColumn
tnEtherRawCountStatRxPktsSize1024to1518 = _TnEtherRawCountStatRxPktsSize1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 9),
    _TnEtherRawCountStatRxPktsSize1024to1518_Type()
)
tnEtherRawCountStatRxPktsSize1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatRxPktsSize1024to1518.setStatus("current")
_TnEtherRawCountStatRxPktsSize128to255_Type = Counter64
_TnEtherRawCountStatRxPktsSize128to255_Object = MibTableColumn
tnEtherRawCountStatRxPktsSize128to255 = _TnEtherRawCountStatRxPktsSize128to255_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 10),
    _TnEtherRawCountStatRxPktsSize128to255_Type()
)
tnEtherRawCountStatRxPktsSize128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatRxPktsSize128to255.setStatus("current")
_TnEtherRawCountStatRxPktsSize256to511_Type = Counter64
_TnEtherRawCountStatRxPktsSize256to511_Object = MibTableColumn
tnEtherRawCountStatRxPktsSize256to511 = _TnEtherRawCountStatRxPktsSize256to511_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 11),
    _TnEtherRawCountStatRxPktsSize256to511_Type()
)
tnEtherRawCountStatRxPktsSize256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatRxPktsSize256to511.setStatus("current")
_TnEtherRawCountStatRxPktsSize512to1023_Type = Counter64
_TnEtherRawCountStatRxPktsSize512to1023_Object = MibTableColumn
tnEtherRawCountStatRxPktsSize512to1023 = _TnEtherRawCountStatRxPktsSize512to1023_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 12),
    _TnEtherRawCountStatRxPktsSize512to1023_Type()
)
tnEtherRawCountStatRxPktsSize512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatRxPktsSize512to1023.setStatus("current")
_TnEtherRawCountStatRxPktsSize65to127_Type = Counter64
_TnEtherRawCountStatRxPktsSize65to127_Object = MibTableColumn
tnEtherRawCountStatRxPktsSize65to127 = _TnEtherRawCountStatRxPktsSize65to127_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 14),
    _TnEtherRawCountStatRxPktsSize65to127_Type()
)
tnEtherRawCountStatRxPktsSize65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatRxPktsSize65to127.setStatus("current")
_TnEtherRawCountStatRxUndersizedPkts_Type = Counter64
_TnEtherRawCountStatRxUndersizedPkts_Object = MibTableColumn
tnEtherRawCountStatRxUndersizedPkts = _TnEtherRawCountStatRxUndersizedPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 15),
    _TnEtherRawCountStatRxUndersizedPkts_Type()
)
tnEtherRawCountStatRxUndersizedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatRxUndersizedPkts.setStatus("current")
_TnEtherRawCountStatTxBcastPkts_Type = Counter64
_TnEtherRawCountStatTxBcastPkts_Object = MibTableColumn
tnEtherRawCountStatTxBcastPkts = _TnEtherRawCountStatTxBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 16),
    _TnEtherRawCountStatTxBcastPkts_Type()
)
tnEtherRawCountStatTxBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatTxBcastPkts.setStatus("current")
_TnEtherRawCountStatTxCrcAlignErrs_Type = Counter64
_TnEtherRawCountStatTxCrcAlignErrs_Object = MibTableColumn
tnEtherRawCountStatTxCrcAlignErrs = _TnEtherRawCountStatTxCrcAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 17),
    _TnEtherRawCountStatTxCrcAlignErrs_Type()
)
tnEtherRawCountStatTxCrcAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatTxCrcAlignErrs.setStatus("current")
_TnEtherRawCountStatTxDropEvents_Type = Counter64
_TnEtherRawCountStatTxDropEvents_Object = MibTableColumn
tnEtherRawCountStatTxDropEvents = _TnEtherRawCountStatTxDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 18),
    _TnEtherRawCountStatTxDropEvents_Type()
)
tnEtherRawCountStatTxDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatTxDropEvents.setStatus("current")
_TnEtherRawCountStatTxFragments_Type = Counter64
_TnEtherRawCountStatTxFragments_Object = MibTableColumn
tnEtherRawCountStatTxFragments = _TnEtherRawCountStatTxFragments_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 19),
    _TnEtherRawCountStatTxFragments_Type()
)
tnEtherRawCountStatTxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatTxFragments.setStatus("current")
_TnEtherRawCountStatTxJabbers_Type = Counter64
_TnEtherRawCountStatTxJabbers_Object = MibTableColumn
tnEtherRawCountStatTxJabbers = _TnEtherRawCountStatTxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 20),
    _TnEtherRawCountStatTxJabbers_Type()
)
tnEtherRawCountStatTxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatTxJabbers.setStatus("current")
_TnEtherRawCountStatTxMcastPkts_Type = Counter64
_TnEtherRawCountStatTxMcastPkts_Object = MibTableColumn
tnEtherRawCountStatTxMcastPkts = _TnEtherRawCountStatTxMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 21),
    _TnEtherRawCountStatTxMcastPkts_Type()
)
tnEtherRawCountStatTxMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatTxMcastPkts.setStatus("current")
_TnEtherRawCountStatTxOctets_Type = Counter64
_TnEtherRawCountStatTxOctets_Object = MibTableColumn
tnEtherRawCountStatTxOctets = _TnEtherRawCountStatTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 22),
    _TnEtherRawCountStatTxOctets_Type()
)
tnEtherRawCountStatTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatTxOctets.setStatus("current")
_TnEtherRawCountStatTxOversizedPkts_Type = Counter64
_TnEtherRawCountStatTxOversizedPkts_Object = MibTableColumn
tnEtherRawCountStatTxOversizedPkts = _TnEtherRawCountStatTxOversizedPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 23),
    _TnEtherRawCountStatTxOversizedPkts_Type()
)
tnEtherRawCountStatTxOversizedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatTxOversizedPkts.setStatus("current")
_TnEtherRawCountStatTxPkts_Type = Counter64
_TnEtherRawCountStatTxPkts_Object = MibTableColumn
tnEtherRawCountStatTxPkts = _TnEtherRawCountStatTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 24),
    _TnEtherRawCountStatTxPkts_Type()
)
tnEtherRawCountStatTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatTxPkts.setStatus("current")
_TnEtherRawCountStatTxPktsSize1024to1518_Type = Counter64
_TnEtherRawCountStatTxPktsSize1024to1518_Object = MibTableColumn
tnEtherRawCountStatTxPktsSize1024to1518 = _TnEtherRawCountStatTxPktsSize1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 25),
    _TnEtherRawCountStatTxPktsSize1024to1518_Type()
)
tnEtherRawCountStatTxPktsSize1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatTxPktsSize1024to1518.setStatus("current")
_TnEtherRawCountStatTxPktsSize128to255_Type = Counter64
_TnEtherRawCountStatTxPktsSize128to255_Object = MibTableColumn
tnEtherRawCountStatTxPktsSize128to255 = _TnEtherRawCountStatTxPktsSize128to255_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 26),
    _TnEtherRawCountStatTxPktsSize128to255_Type()
)
tnEtherRawCountStatTxPktsSize128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatTxPktsSize128to255.setStatus("current")
_TnEtherRawCountStatTxPktsSize256to511_Type = Counter64
_TnEtherRawCountStatTxPktsSize256to511_Object = MibTableColumn
tnEtherRawCountStatTxPktsSize256to511 = _TnEtherRawCountStatTxPktsSize256to511_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 27),
    _TnEtherRawCountStatTxPktsSize256to511_Type()
)
tnEtherRawCountStatTxPktsSize256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatTxPktsSize256to511.setStatus("current")
_TnEtherRawCountStatTxPktsSize512to1023_Type = Counter64
_TnEtherRawCountStatTxPktsSize512to1023_Object = MibTableColumn
tnEtherRawCountStatTxPktsSize512to1023 = _TnEtherRawCountStatTxPktsSize512to1023_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 28),
    _TnEtherRawCountStatTxPktsSize512to1023_Type()
)
tnEtherRawCountStatTxPktsSize512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatTxPktsSize512to1023.setStatus("current")
_TnEtherRawCountStatTxPktsSize65to127_Type = Counter64
_TnEtherRawCountStatTxPktsSize65to127_Object = MibTableColumn
tnEtherRawCountStatTxPktsSize65to127 = _TnEtherRawCountStatTxPktsSize65to127_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 30),
    _TnEtherRawCountStatTxPktsSize65to127_Type()
)
tnEtherRawCountStatTxPktsSize65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatTxPktsSize65to127.setStatus("current")
_TnEtherRawCountStatTxUndersizedPkts_Type = Counter64
_TnEtherRawCountStatTxUndersizedPkts_Object = MibTableColumn
tnEtherRawCountStatTxUndersizedPkts = _TnEtherRawCountStatTxUndersizedPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 31),
    _TnEtherRawCountStatTxUndersizedPkts_Type()
)
tnEtherRawCountStatTxUndersizedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatTxUndersizedPkts.setStatus("current")
_TnEtherRawCountStatRxBcastPkts_Type = Counter64
_TnEtherRawCountStatRxBcastPkts_Object = MibTableColumn
tnEtherRawCountStatRxBcastPkts = _TnEtherRawCountStatRxBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 32),
    _TnEtherRawCountStatRxBcastPkts_Type()
)
tnEtherRawCountStatRxBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatRxBcastPkts.setStatus("current")
_TnEtherRawCountStatRxCrcAlignErrs_Type = Counter64
_TnEtherRawCountStatRxCrcAlignErrs_Object = MibTableColumn
tnEtherRawCountStatRxCrcAlignErrs = _TnEtherRawCountStatRxCrcAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 33),
    _TnEtherRawCountStatRxCrcAlignErrs_Type()
)
tnEtherRawCountStatRxCrcAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatRxCrcAlignErrs.setStatus("current")
_TnEtherRawCountStatRxCollisions_Type = Counter64
_TnEtherRawCountStatRxCollisions_Object = MibTableColumn
tnEtherRawCountStatRxCollisions = _TnEtherRawCountStatRxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 34),
    _TnEtherRawCountStatRxCollisions_Type()
)
tnEtherRawCountStatRxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatRxCollisions.setStatus("current")
_TnEtherRawCountStatRxJumboPkts_Type = Counter64
_TnEtherRawCountStatRxJumboPkts_Object = MibTableColumn
tnEtherRawCountStatRxJumboPkts = _TnEtherRawCountStatRxJumboPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 35),
    _TnEtherRawCountStatRxJumboPkts_Type()
)
tnEtherRawCountStatRxJumboPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatRxJumboPkts.setStatus("current")
_TnEtherRawCountStatTxCollisions_Type = Counter64
_TnEtherRawCountStatTxCollisions_Object = MibTableColumn
tnEtherRawCountStatTxCollisions = _TnEtherRawCountStatTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 36),
    _TnEtherRawCountStatTxCollisions_Type()
)
tnEtherRawCountStatTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatTxCollisions.setStatus("current")
_TnEtherRawCountStatTxJumboPkts_Type = Counter64
_TnEtherRawCountStatTxJumboPkts_Object = MibTableColumn
tnEtherRawCountStatTxJumboPkts = _TnEtherRawCountStatTxJumboPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 37),
    _TnEtherRawCountStatTxJumboPkts_Type()
)
tnEtherRawCountStatTxJumboPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatTxJumboPkts.setStatus("current")
_TnEtherRawCountStatRmonIndex_Type = Unsigned32
_TnEtherRawCountStatRmonIndex_Object = MibTableColumn
tnEtherRawCountStatRmonIndex = _TnEtherRawCountStatRmonIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 38),
    _TnEtherRawCountStatRmonIndex_Type()
)
tnEtherRawCountStatRmonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatRmonIndex.setStatus("current")
_TnEtherRawCountStatRxPktsSize64_Type = Counter64
_TnEtherRawCountStatRxPktsSize64_Object = MibTableColumn
tnEtherRawCountStatRxPktsSize64 = _TnEtherRawCountStatRxPktsSize64_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 39),
    _TnEtherRawCountStatRxPktsSize64_Type()
)
tnEtherRawCountStatRxPktsSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatRxPktsSize64.setStatus("current")
_TnEtherRawCountStatTxPktsSize64_Type = Counter64
_TnEtherRawCountStatTxPktsSize64_Object = MibTableColumn
tnEtherRawCountStatTxPktsSize64 = _TnEtherRawCountStatTxPktsSize64_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 40),
    _TnEtherRawCountStatTxPktsSize64_Type()
)
tnEtherRawCountStatTxPktsSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatTxPktsSize64.setStatus("current")
_TnEtherRawCountStatRxPktErrRatio_Type = Counter64
_TnEtherRawCountStatRxPktErrRatio_Object = MibTableColumn
tnEtherRawCountStatRxPktErrRatio = _TnEtherRawCountStatRxPktErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 41),
    _TnEtherRawCountStatRxPktErrRatio_Type()
)
tnEtherRawCountStatRxPktErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatRxPktErrRatio.setStatus("current")
_TnEtherRawCountStatTxPktErrRatio_Type = Counter64
_TnEtherRawCountStatTxPktErrRatio_Object = MibTableColumn
tnEtherRawCountStatTxPktErrRatio = _TnEtherRawCountStatTxPktErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 42),
    _TnEtherRawCountStatTxPktErrRatio_Type()
)
tnEtherRawCountStatTxPktErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatTxPktErrRatio.setStatus("current")
_TnEtherRawCountStatStartTime_Type = DateAndTime
_TnEtherRawCountStatStartTime_Object = MibTableColumn
tnEtherRawCountStatStartTime = _TnEtherRawCountStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 8, 1, 43),
    _TnEtherRawCountStatStartTime_Type()
)
tnEtherRawCountStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEtherRawCountStatStartTime.setStatus("current")
_TnSonetRawCountStatsTotalMembers_Type = Integer32
_TnSonetRawCountStatsTotalMembers_Object = MibScalar
tnSonetRawCountStatsTotalMembers = _TnSonetRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 9),
    _TnSonetRawCountStatsTotalMembers_Type()
)
tnSonetRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatsTotalMembers.setStatus("current")
_TnSonetRawCountStatsTable_Object = MibTable
tnSonetRawCountStatsTable = _TnSonetRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10)
)
if mibBuilder.loadTexts:
    tnSonetRawCountStatsTable.setStatus("current")
_TnSonetRawCountStatsEntry_Object = MibTableRow
tnSonetRawCountStatsEntry = _TnSonetRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1)
)
tnSonetRawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnSonetRawCountStatsEntry.setStatus("current")
_TnSonetRawCountStatsClear_Type = TnCommand
_TnSonetRawCountStatsClear_Object = MibTableColumn
tnSonetRawCountStatsClear = _TnSonetRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 1),
    _TnSonetRawCountStatsClear_Type()
)
tnSonetRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSonetRawCountStatsClear.setStatus("current")
_TnSonetRawCountStatRxCVS_Type = Counter32
_TnSonetRawCountStatRxCVS_Object = MibTableColumn
tnSonetRawCountStatRxCVS = _TnSonetRawCountStatRxCVS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 2),
    _TnSonetRawCountStatRxCVS_Type()
)
tnSonetRawCountStatRxCVS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatRxCVS.setStatus("current")
_TnSonetRawCountStatRxESS_Type = Counter32
_TnSonetRawCountStatRxESS_Object = MibTableColumn
tnSonetRawCountStatRxESS = _TnSonetRawCountStatRxESS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 3),
    _TnSonetRawCountStatRxESS_Type()
)
tnSonetRawCountStatRxESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatRxESS.setStatus("current")
_TnSonetRawCountStatRxSESS_Type = Counter32
_TnSonetRawCountStatRxSESS_Object = MibTableColumn
tnSonetRawCountStatRxSESS = _TnSonetRawCountStatRxSESS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 4),
    _TnSonetRawCountStatRxSESS_Type()
)
tnSonetRawCountStatRxSESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatRxSESS.setStatus("current")
_TnSonetRawCountStatRxSEFSS_Type = Counter32
_TnSonetRawCountStatRxSEFSS_Object = MibTableColumn
tnSonetRawCountStatRxSEFSS = _TnSonetRawCountStatRxSEFSS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 5),
    _TnSonetRawCountStatRxSEFSS_Type()
)
tnSonetRawCountStatRxSEFSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatRxSEFSS.setStatus("current")
_TnSonetRawCountStatRxCVL_Type = Counter32
_TnSonetRawCountStatRxCVL_Object = MibTableColumn
tnSonetRawCountStatRxCVL = _TnSonetRawCountStatRxCVL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 6),
    _TnSonetRawCountStatRxCVL_Type()
)
tnSonetRawCountStatRxCVL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatRxCVL.setStatus("current")
_TnSonetRawCountStatRxESL_Type = Counter32
_TnSonetRawCountStatRxESL_Object = MibTableColumn
tnSonetRawCountStatRxESL = _TnSonetRawCountStatRxESL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 7),
    _TnSonetRawCountStatRxESL_Type()
)
tnSonetRawCountStatRxESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatRxESL.setStatus("current")
_TnSonetRawCountStatRxSESL_Type = Counter32
_TnSonetRawCountStatRxSESL_Object = MibTableColumn
tnSonetRawCountStatRxSESL = _TnSonetRawCountStatRxSESL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 8),
    _TnSonetRawCountStatRxSESL_Type()
)
tnSonetRawCountStatRxSESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatRxSESL.setStatus("current")
_TnSonetRawCountStatRxUASL_Type = Counter32
_TnSonetRawCountStatRxUASL_Object = MibTableColumn
tnSonetRawCountStatRxUASL = _TnSonetRawCountStatRxUASL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 9),
    _TnSonetRawCountStatRxUASL_Type()
)
tnSonetRawCountStatRxUASL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatRxUASL.setStatus("current")
_TnSonetRawCountStatRxFCL_Type = Counter32
_TnSonetRawCountStatRxFCL_Object = MibTableColumn
tnSonetRawCountStatRxFCL = _TnSonetRawCountStatRxFCL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 10),
    _TnSonetRawCountStatRxFCL_Type()
)
tnSonetRawCountStatRxFCL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatRxFCL.setStatus("current")
_TnSonetRawCountStatTxCVS_Type = Counter32
_TnSonetRawCountStatTxCVS_Object = MibTableColumn
tnSonetRawCountStatTxCVS = _TnSonetRawCountStatTxCVS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 11),
    _TnSonetRawCountStatTxCVS_Type()
)
tnSonetRawCountStatTxCVS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatTxCVS.setStatus("current")
_TnSonetRawCountStatTxESS_Type = Counter32
_TnSonetRawCountStatTxESS_Object = MibTableColumn
tnSonetRawCountStatTxESS = _TnSonetRawCountStatTxESS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 12),
    _TnSonetRawCountStatTxESS_Type()
)
tnSonetRawCountStatTxESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatTxESS.setStatus("current")
_TnSonetRawCountStatTxSESS_Type = Counter32
_TnSonetRawCountStatTxSESS_Object = MibTableColumn
tnSonetRawCountStatTxSESS = _TnSonetRawCountStatTxSESS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 13),
    _TnSonetRawCountStatTxSESS_Type()
)
tnSonetRawCountStatTxSESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatTxSESS.setStatus("current")
_TnSonetRawCountStatTxSEFSS_Type = Counter32
_TnSonetRawCountStatTxSEFSS_Object = MibTableColumn
tnSonetRawCountStatTxSEFSS = _TnSonetRawCountStatTxSEFSS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 14),
    _TnSonetRawCountStatTxSEFSS_Type()
)
tnSonetRawCountStatTxSEFSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatTxSEFSS.setStatus("current")
_TnSonetRawCountStatTxCVL_Type = Counter32
_TnSonetRawCountStatTxCVL_Object = MibTableColumn
tnSonetRawCountStatTxCVL = _TnSonetRawCountStatTxCVL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 15),
    _TnSonetRawCountStatTxCVL_Type()
)
tnSonetRawCountStatTxCVL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatTxCVL.setStatus("current")
_TnSonetRawCountStatTxESL_Type = Counter32
_TnSonetRawCountStatTxESL_Object = MibTableColumn
tnSonetRawCountStatTxESL = _TnSonetRawCountStatTxESL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 16),
    _TnSonetRawCountStatTxESL_Type()
)
tnSonetRawCountStatTxESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatTxESL.setStatus("current")
_TnSonetRawCountStatTxSESL_Type = Counter32
_TnSonetRawCountStatTxSESL_Object = MibTableColumn
tnSonetRawCountStatTxSESL = _TnSonetRawCountStatTxSESL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 17),
    _TnSonetRawCountStatTxSESL_Type()
)
tnSonetRawCountStatTxSESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatTxSESL.setStatus("current")
_TnSonetRawCountStatTxUASL_Type = Counter32
_TnSonetRawCountStatTxUASL_Object = MibTableColumn
tnSonetRawCountStatTxUASL = _TnSonetRawCountStatTxUASL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 18),
    _TnSonetRawCountStatTxUASL_Type()
)
tnSonetRawCountStatTxUASL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatTxUASL.setStatus("current")
_TnSonetRawCountStatTxFCL_Type = Counter32
_TnSonetRawCountStatTxFCL_Object = MibTableColumn
tnSonetRawCountStatTxFCL = _TnSonetRawCountStatTxFCL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 19),
    _TnSonetRawCountStatTxFCL_Type()
)
tnSonetRawCountStatTxFCL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatTxFCL.setStatus("current")
_TnSonetRawCountStatRxUASS_Type = Counter32
_TnSonetRawCountStatRxUASS_Object = MibTableColumn
tnSonetRawCountStatRxUASS = _TnSonetRawCountStatRxUASS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 20),
    _TnSonetRawCountStatRxUASS_Type()
)
tnSonetRawCountStatRxUASS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatRxUASS.setStatus("current")
_TnSonetRawCountStatTxUASS_Type = Counter32
_TnSonetRawCountStatTxUASS_Object = MibTableColumn
tnSonetRawCountStatTxUASS = _TnSonetRawCountStatTxUASS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 21),
    _TnSonetRawCountStatTxUASS_Type()
)
tnSonetRawCountStatTxUASS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatTxUASS.setStatus("current")
_TnSonetRawCountStatStartTime_Type = DateAndTime
_TnSonetRawCountStatStartTime_Object = MibTableColumn
tnSonetRawCountStatStartTime = _TnSonetRawCountStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 22),
    _TnSonetRawCountStatStartTime_Type()
)
tnSonetRawCountStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatStartTime.setStatus("current")
_TnSonetRawCountStatRxFECVL_Type = Counter32
_TnSonetRawCountStatRxFECVL_Object = MibTableColumn
tnSonetRawCountStatRxFECVL = _TnSonetRawCountStatRxFECVL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 23),
    _TnSonetRawCountStatRxFECVL_Type()
)
tnSonetRawCountStatRxFECVL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatRxFECVL.setStatus("current")
_TnSonetRawCountStatRxFEESL_Type = Counter32
_TnSonetRawCountStatRxFEESL_Object = MibTableColumn
tnSonetRawCountStatRxFEESL = _TnSonetRawCountStatRxFEESL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 24),
    _TnSonetRawCountStatRxFEESL_Type()
)
tnSonetRawCountStatRxFEESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatRxFEESL.setStatus("current")
_TnSonetRawCountStatRxFESESL_Type = Counter32
_TnSonetRawCountStatRxFESESL_Object = MibTableColumn
tnSonetRawCountStatRxFESESL = _TnSonetRawCountStatRxFESESL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 25),
    _TnSonetRawCountStatRxFESESL_Type()
)
tnSonetRawCountStatRxFESESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatRxFESESL.setStatus("current")
_TnSonetRawCountStatRxFEUASL_Type = Counter32
_TnSonetRawCountStatRxFEUASL_Object = MibTableColumn
tnSonetRawCountStatRxFEUASL = _TnSonetRawCountStatRxFEUASL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 10, 1, 26),
    _TnSonetRawCountStatRxFEUASL_Type()
)
tnSonetRawCountStatRxFEUASL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetRawCountStatRxFEUASL.setStatus("current")
_TnOptRawCountStatsTotalMembers_Type = Integer32
_TnOptRawCountStatsTotalMembers_Object = MibScalar
tnOptRawCountStatsTotalMembers = _TnOptRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 15),
    _TnOptRawCountStatsTotalMembers_Type()
)
tnOptRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOptRawCountStatsTotalMembers.setStatus("current")
_TnOptRawCountStatsTable_Object = MibTable
tnOptRawCountStatsTable = _TnOptRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 16)
)
if mibBuilder.loadTexts:
    tnOptRawCountStatsTable.setStatus("current")
_TnOptRawCountStatsEntry_Object = MibTableRow
tnOptRawCountStatsEntry = _TnOptRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 16, 1)
)
tnOptRawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnOptRawCountStatsEntry.setStatus("current")
_TnOptRawCountStatsClear_Type = TnCommand
_TnOptRawCountStatsClear_Object = MibTableColumn
tnOptRawCountStatsClear = _TnOptRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 16, 1, 1),
    _TnOptRawCountStatsClear_Type()
)
tnOptRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOptRawCountStatsClear.setStatus("current")
_TnOptRawCountStatMinPower_Type = Integer32
_TnOptRawCountStatMinPower_Object = MibTableColumn
tnOptRawCountStatMinPower = _TnOptRawCountStatMinPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 16, 1, 2),
    _TnOptRawCountStatMinPower_Type()
)
tnOptRawCountStatMinPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOptRawCountStatMinPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOptRawCountStatMinPower.setUnits("mBm")
_TnOptRawCountStatMaxPower_Type = Integer32
_TnOptRawCountStatMaxPower_Object = MibTableColumn
tnOptRawCountStatMaxPower = _TnOptRawCountStatMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 16, 1, 3),
    _TnOptRawCountStatMaxPower_Type()
)
tnOptRawCountStatMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOptRawCountStatMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOptRawCountStatMaxPower.setUnits("mBm")
_TnOptRawCountStatAveragePower_Type = Integer32
_TnOptRawCountStatAveragePower_Object = MibTableColumn
tnOptRawCountStatAveragePower = _TnOptRawCountStatAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 16, 1, 4),
    _TnOptRawCountStatAveragePower_Type()
)
tnOptRawCountStatAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOptRawCountStatAveragePower.setStatus("current")
if mibBuilder.loadTexts:
    tnOptRawCountStatAveragePower.setUnits("mBm")
_TnOptRawCountStatStartTime_Type = DateAndTime
_TnOptRawCountStatStartTime_Object = MibTableColumn
tnOptRawCountStatStartTime = _TnOptRawCountStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 16, 1, 5),
    _TnOptRawCountStatStartTime_Type()
)
tnOptRawCountStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOptRawCountStatStartTime.setStatus("current")
_TnOprRawCountStatsTotalMembers_Type = Integer32
_TnOprRawCountStatsTotalMembers_Object = MibScalar
tnOprRawCountStatsTotalMembers = _TnOprRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 17),
    _TnOprRawCountStatsTotalMembers_Type()
)
tnOprRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOprRawCountStatsTotalMembers.setStatus("current")
_TnOprRawCountStatsTable_Object = MibTable
tnOprRawCountStatsTable = _TnOprRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 18)
)
if mibBuilder.loadTexts:
    tnOprRawCountStatsTable.setStatus("current")
_TnOprRawCountStatsEntry_Object = MibTableRow
tnOprRawCountStatsEntry = _TnOprRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 18, 1)
)
tnOprRawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnOprRawCountStatsEntry.setStatus("current")
_TnOprRawCountStatsClear_Type = TnCommand
_TnOprRawCountStatsClear_Object = MibTableColumn
tnOprRawCountStatsClear = _TnOprRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 18, 1, 1),
    _TnOprRawCountStatsClear_Type()
)
tnOprRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOprRawCountStatsClear.setStatus("current")
_TnOprRawCountStatMinPower_Type = Integer32
_TnOprRawCountStatMinPower_Object = MibTableColumn
tnOprRawCountStatMinPower = _TnOprRawCountStatMinPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 18, 1, 2),
    _TnOprRawCountStatMinPower_Type()
)
tnOprRawCountStatMinPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOprRawCountStatMinPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOprRawCountStatMinPower.setUnits("mBm")
_TnOprRawCountStatMaxPower_Type = Integer32
_TnOprRawCountStatMaxPower_Object = MibTableColumn
tnOprRawCountStatMaxPower = _TnOprRawCountStatMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 18, 1, 3),
    _TnOprRawCountStatMaxPower_Type()
)
tnOprRawCountStatMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOprRawCountStatMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOprRawCountStatMaxPower.setUnits("mBm")
_TnOprRawCountStatAveragePower_Type = Integer32
_TnOprRawCountStatAveragePower_Object = MibTableColumn
tnOprRawCountStatAveragePower = _TnOprRawCountStatAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 18, 1, 4),
    _TnOprRawCountStatAveragePower_Type()
)
tnOprRawCountStatAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOprRawCountStatAveragePower.setStatus("current")
if mibBuilder.loadTexts:
    tnOprRawCountStatAveragePower.setUnits("mBm")
_TnOprRawCountStatStartTime_Type = DateAndTime
_TnOprRawCountStatStartTime_Object = MibTableColumn
tnOprRawCountStatStartTime = _TnOprRawCountStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 18, 1, 5),
    _TnOprRawCountStatStartTime_Type()
)
tnOprRawCountStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOprRawCountStatStartTime.setStatus("current")
_TnOpOutRawCountStatsTotalMembers_Type = Integer32
_TnOpOutRawCountStatsTotalMembers_Object = MibScalar
tnOpOutRawCountStatsTotalMembers = _TnOpOutRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 19),
    _TnOpOutRawCountStatsTotalMembers_Type()
)
tnOpOutRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOutRawCountStatsTotalMembers.setStatus("current")
_TnOpOutRawCountStatsTable_Object = MibTable
tnOpOutRawCountStatsTable = _TnOpOutRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 20)
)
if mibBuilder.loadTexts:
    tnOpOutRawCountStatsTable.setStatus("current")
_TnOpOutRawCountStatsEntry_Object = MibTableRow
tnOpOutRawCountStatsEntry = _TnOpOutRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 20, 1)
)
tnOpOutRawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnOpOutRawCountStatsEntry.setStatus("current")
_TnOpOutRawCountStatsClear_Type = TnCommand
_TnOpOutRawCountStatsClear_Object = MibTableColumn
tnOpOutRawCountStatsClear = _TnOpOutRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 20, 1, 1),
    _TnOpOutRawCountStatsClear_Type()
)
tnOpOutRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOpOutRawCountStatsClear.setStatus("current")
_TnOpOutRawCountStatMinPower_Type = Integer32
_TnOpOutRawCountStatMinPower_Object = MibTableColumn
tnOpOutRawCountStatMinPower = _TnOpOutRawCountStatMinPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 20, 1, 2),
    _TnOpOutRawCountStatMinPower_Type()
)
tnOpOutRawCountStatMinPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOutRawCountStatMinPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpOutRawCountStatMinPower.setUnits("mBm")
_TnOpOutRawCountStatMaxPower_Type = Integer32
_TnOpOutRawCountStatMaxPower_Object = MibTableColumn
tnOpOutRawCountStatMaxPower = _TnOpOutRawCountStatMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 20, 1, 3),
    _TnOpOutRawCountStatMaxPower_Type()
)
tnOpOutRawCountStatMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOutRawCountStatMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpOutRawCountStatMaxPower.setUnits("mBm")
_TnOpOutRawCountStatAveragePower_Type = Integer32
_TnOpOutRawCountStatAveragePower_Object = MibTableColumn
tnOpOutRawCountStatAveragePower = _TnOpOutRawCountStatAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 20, 1, 4),
    _TnOpOutRawCountStatAveragePower_Type()
)
tnOpOutRawCountStatAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOutRawCountStatAveragePower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpOutRawCountStatAveragePower.setUnits("mBm")
_TnOpOutRawCountStatStartTime_Type = DateAndTime
_TnOpOutRawCountStatStartTime_Object = MibTableColumn
tnOpOutRawCountStatStartTime = _TnOpOutRawCountStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 20, 1, 5),
    _TnOpOutRawCountStatStartTime_Type()
)
tnOpOutRawCountStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOutRawCountStatStartTime.setStatus("current")
_TnOpInRawCountStatsTotalMembers_Type = Integer32
_TnOpInRawCountStatsTotalMembers_Object = MibScalar
tnOpInRawCountStatsTotalMembers = _TnOpInRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 21),
    _TnOpInRawCountStatsTotalMembers_Type()
)
tnOpInRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpInRawCountStatsTotalMembers.setStatus("current")
_TnOpInRawCountStatsTable_Object = MibTable
tnOpInRawCountStatsTable = _TnOpInRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 22)
)
if mibBuilder.loadTexts:
    tnOpInRawCountStatsTable.setStatus("current")
_TnOpInRawCountStatsEntry_Object = MibTableRow
tnOpInRawCountStatsEntry = _TnOpInRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 22, 1)
)
tnOpInRawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnOpInRawCountStatsEntry.setStatus("current")
_TnOpInRawCountStatsClear_Type = TnCommand
_TnOpInRawCountStatsClear_Object = MibTableColumn
tnOpInRawCountStatsClear = _TnOpInRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 22, 1, 1),
    _TnOpInRawCountStatsClear_Type()
)
tnOpInRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOpInRawCountStatsClear.setStatus("current")
_TnOpInRawCountStatMinPower_Type = Integer32
_TnOpInRawCountStatMinPower_Object = MibTableColumn
tnOpInRawCountStatMinPower = _TnOpInRawCountStatMinPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 22, 1, 2),
    _TnOpInRawCountStatMinPower_Type()
)
tnOpInRawCountStatMinPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpInRawCountStatMinPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpInRawCountStatMinPower.setUnits("mBm")
_TnOpInRawCountStatMaxPower_Type = Integer32
_TnOpInRawCountStatMaxPower_Object = MibTableColumn
tnOpInRawCountStatMaxPower = _TnOpInRawCountStatMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 22, 1, 3),
    _TnOpInRawCountStatMaxPower_Type()
)
tnOpInRawCountStatMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpInRawCountStatMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpInRawCountStatMaxPower.setUnits("mBm")
_TnOpInRawCountStatAveragePower_Type = Integer32
_TnOpInRawCountStatAveragePower_Object = MibTableColumn
tnOpInRawCountStatAveragePower = _TnOpInRawCountStatAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 22, 1, 4),
    _TnOpInRawCountStatAveragePower_Type()
)
tnOpInRawCountStatAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpInRawCountStatAveragePower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpInRawCountStatAveragePower.setUnits("mBm")
_TnOpInRawCountStatStartTime_Type = DateAndTime
_TnOpInRawCountStatStartTime_Object = MibTableColumn
tnOpInRawCountStatStartTime = _TnOpInRawCountStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 22, 1, 5),
    _TnOpInRawCountStatStartTime_Type()
)
tnOpInRawCountStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpInRawCountStatStartTime.setStatus("current")
_TnOpOchOutRawCountStatsTotalMembers_Type = Integer32
_TnOpOchOutRawCountStatsTotalMembers_Object = MibScalar
tnOpOchOutRawCountStatsTotalMembers = _TnOpOchOutRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 23),
    _TnOpOchOutRawCountStatsTotalMembers_Type()
)
tnOpOchOutRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchOutRawCountStatsTotalMembers.setStatus("current")
_TnOpOchOutRawCountStatsTable_Object = MibTable
tnOpOchOutRawCountStatsTable = _TnOpOchOutRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 24)
)
if mibBuilder.loadTexts:
    tnOpOchOutRawCountStatsTable.setStatus("current")
_TnOpOchOutRawCountStatsEntry_Object = MibTableRow
tnOpOchOutRawCountStatsEntry = _TnOpOchOutRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 24, 1)
)
tnOpOchOutRawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnOpticalStatsITUChannel"),
)
if mibBuilder.loadTexts:
    tnOpOchOutRawCountStatsEntry.setStatus("current")
_TnOpOchOutRawCountStatsClear_Type = TnCommand
_TnOpOchOutRawCountStatsClear_Object = MibTableColumn
tnOpOchOutRawCountStatsClear = _TnOpOchOutRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 24, 1, 1),
    _TnOpOchOutRawCountStatsClear_Type()
)
tnOpOchOutRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOpOchOutRawCountStatsClear.setStatus("current")
_TnOpOchOutRawCountStatMinPower_Type = Integer32
_TnOpOchOutRawCountStatMinPower_Object = MibTableColumn
tnOpOchOutRawCountStatMinPower = _TnOpOchOutRawCountStatMinPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 24, 1, 2),
    _TnOpOchOutRawCountStatMinPower_Type()
)
tnOpOchOutRawCountStatMinPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchOutRawCountStatMinPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpOchOutRawCountStatMinPower.setUnits("mBm")
_TnOpOchOutRawCountStatMaxPower_Type = Integer32
_TnOpOchOutRawCountStatMaxPower_Object = MibTableColumn
tnOpOchOutRawCountStatMaxPower = _TnOpOchOutRawCountStatMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 24, 1, 3),
    _TnOpOchOutRawCountStatMaxPower_Type()
)
tnOpOchOutRawCountStatMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchOutRawCountStatMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpOchOutRawCountStatMaxPower.setUnits("mBm")
_TnOpOchOutRawCountStatAveragePower_Type = Integer32
_TnOpOchOutRawCountStatAveragePower_Object = MibTableColumn
tnOpOchOutRawCountStatAveragePower = _TnOpOchOutRawCountStatAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 24, 1, 4),
    _TnOpOchOutRawCountStatAveragePower_Type()
)
tnOpOchOutRawCountStatAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchOutRawCountStatAveragePower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpOchOutRawCountStatAveragePower.setUnits("mBm")
_TnOpOchOutRawCountStatStartTime_Type = DateAndTime
_TnOpOchOutRawCountStatStartTime_Object = MibTableColumn
tnOpOchOutRawCountStatStartTime = _TnOpOchOutRawCountStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 24, 1, 5),
    _TnOpOchOutRawCountStatStartTime_Type()
)
tnOpOchOutRawCountStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchOutRawCountStatStartTime.setStatus("current")
_TnOpOchInRawCountStatsTotalMembers_Type = Integer32
_TnOpOchInRawCountStatsTotalMembers_Object = MibScalar
tnOpOchInRawCountStatsTotalMembers = _TnOpOchInRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 25),
    _TnOpOchInRawCountStatsTotalMembers_Type()
)
tnOpOchInRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchInRawCountStatsTotalMembers.setStatus("current")
_TnOpOchInRawCountStatsTable_Object = MibTable
tnOpOchInRawCountStatsTable = _TnOpOchInRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 26)
)
if mibBuilder.loadTexts:
    tnOpOchInRawCountStatsTable.setStatus("current")
_TnOpOchInRawCountStatsEntry_Object = MibTableRow
tnOpOchInRawCountStatsEntry = _TnOpOchInRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 26, 1)
)
tnOpOchInRawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnOpticalStatsITUChannel"),
)
if mibBuilder.loadTexts:
    tnOpOchInRawCountStatsEntry.setStatus("current")
_TnOpOchInRawCountStatsClear_Type = TnCommand
_TnOpOchInRawCountStatsClear_Object = MibTableColumn
tnOpOchInRawCountStatsClear = _TnOpOchInRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 26, 1, 1),
    _TnOpOchInRawCountStatsClear_Type()
)
tnOpOchInRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOpOchInRawCountStatsClear.setStatus("current")
_TnOpOchInRawCountStatMinPower_Type = Integer32
_TnOpOchInRawCountStatMinPower_Object = MibTableColumn
tnOpOchInRawCountStatMinPower = _TnOpOchInRawCountStatMinPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 26, 1, 2),
    _TnOpOchInRawCountStatMinPower_Type()
)
tnOpOchInRawCountStatMinPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchInRawCountStatMinPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpOchInRawCountStatMinPower.setUnits("mBm")
_TnOpOchInRawCountStatMaxPower_Type = Integer32
_TnOpOchInRawCountStatMaxPower_Object = MibTableColumn
tnOpOchInRawCountStatMaxPower = _TnOpOchInRawCountStatMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 26, 1, 3),
    _TnOpOchInRawCountStatMaxPower_Type()
)
tnOpOchInRawCountStatMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchInRawCountStatMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpOchInRawCountStatMaxPower.setUnits("mBm")
_TnOpOchInRawCountStatAveragePower_Type = Integer32
_TnOpOchInRawCountStatAveragePower_Object = MibTableColumn
tnOpOchInRawCountStatAveragePower = _TnOpOchInRawCountStatAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 26, 1, 4),
    _TnOpOchInRawCountStatAveragePower_Type()
)
tnOpOchInRawCountStatAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchInRawCountStatAveragePower.setStatus("current")
if mibBuilder.loadTexts:
    tnOpOchInRawCountStatAveragePower.setUnits("mBm")
_TnOpOchInRawCountStatStartTime_Type = DateAndTime
_TnOpOchInRawCountStatStartTime_Object = MibTableColumn
tnOpOchInRawCountStatStartTime = _TnOpOchInRawCountStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 26, 1, 5),
    _TnOpOchInRawCountStatStartTime_Type()
)
tnOpOchInRawCountStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpOchInRawCountStatStartTime.setStatus("current")
_TnSdhRawCountStatsTotalMembers_Type = Integer32
_TnSdhRawCountStatsTotalMembers_Object = MibScalar
tnSdhRawCountStatsTotalMembers = _TnSdhRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 27),
    _TnSdhRawCountStatsTotalMembers_Type()
)
tnSdhRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatsTotalMembers.setStatus("current")
_TnSdhRawCountStatsTable_Object = MibTable
tnSdhRawCountStatsTable = _TnSdhRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28)
)
if mibBuilder.loadTexts:
    tnSdhRawCountStatsTable.setStatus("current")
_TnSdhRawCountStatsEntry_Object = MibTableRow
tnSdhRawCountStatsEntry = _TnSdhRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1)
)
tnSdhRawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnSdhRawCountStatsEntry.setStatus("current")
_TnSdhRawCountStatsClear_Type = TnCommand
_TnSdhRawCountStatsClear_Object = MibTableColumn
tnSdhRawCountStatsClear = _TnSdhRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 1),
    _TnSdhRawCountStatsClear_Type()
)
tnSdhRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSdhRawCountStatsClear.setStatus("current")
_TnSdhRawCountStatRxRSEB_Type = Counter32
_TnSdhRawCountStatRxRSEB_Object = MibTableColumn
tnSdhRawCountStatRxRSEB = _TnSdhRawCountStatRxRSEB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 2),
    _TnSdhRawCountStatRxRSEB_Type()
)
tnSdhRawCountStatRxRSEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatRxRSEB.setStatus("current")
_TnSdhRawCountStatRxRSES_Type = Counter32
_TnSdhRawCountStatRxRSES_Object = MibTableColumn
tnSdhRawCountStatRxRSES = _TnSdhRawCountStatRxRSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 3),
    _TnSdhRawCountStatRxRSES_Type()
)
tnSdhRawCountStatRxRSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatRxRSES.setStatus("current")
_TnSdhRawCountStatRxRSSES_Type = Counter32
_TnSdhRawCountStatRxRSSES_Object = MibTableColumn
tnSdhRawCountStatRxRSSES = _TnSdhRawCountStatRxRSSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 4),
    _TnSdhRawCountStatRxRSSES_Type()
)
tnSdhRawCountStatRxRSSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatRxRSSES.setStatus("current")
_TnSdhRawCountStatRxMSEB_Type = Counter32
_TnSdhRawCountStatRxMSEB_Object = MibTableColumn
tnSdhRawCountStatRxMSEB = _TnSdhRawCountStatRxMSEB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 5),
    _TnSdhRawCountStatRxMSEB_Type()
)
tnSdhRawCountStatRxMSEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatRxMSEB.setStatus("current")
_TnSdhRawCountStatRxMSES_Type = Counter32
_TnSdhRawCountStatRxMSES_Object = MibTableColumn
tnSdhRawCountStatRxMSES = _TnSdhRawCountStatRxMSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 6),
    _TnSdhRawCountStatRxMSES_Type()
)
tnSdhRawCountStatRxMSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatRxMSES.setStatus("current")
_TnSdhRawCountStatRxMSSES_Type = Counter32
_TnSdhRawCountStatRxMSSES_Object = MibTableColumn
tnSdhRawCountStatRxMSSES = _TnSdhRawCountStatRxMSSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 7),
    _TnSdhRawCountStatRxMSSES_Type()
)
tnSdhRawCountStatRxMSSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatRxMSSES.setStatus("current")
_TnSdhRawCountStatRxMSUAS_Type = Counter32
_TnSdhRawCountStatRxMSUAS_Object = MibTableColumn
tnSdhRawCountStatRxMSUAS = _TnSdhRawCountStatRxMSUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 8),
    _TnSdhRawCountStatRxMSUAS_Type()
)
tnSdhRawCountStatRxMSUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatRxMSUAS.setStatus("current")
_TnSdhRawCountStatTxRSEB_Type = Counter32
_TnSdhRawCountStatTxRSEB_Object = MibTableColumn
tnSdhRawCountStatTxRSEB = _TnSdhRawCountStatTxRSEB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 9),
    _TnSdhRawCountStatTxRSEB_Type()
)
tnSdhRawCountStatTxRSEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatTxRSEB.setStatus("current")
_TnSdhRawCountStatTxRSES_Type = Counter32
_TnSdhRawCountStatTxRSES_Object = MibTableColumn
tnSdhRawCountStatTxRSES = _TnSdhRawCountStatTxRSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 10),
    _TnSdhRawCountStatTxRSES_Type()
)
tnSdhRawCountStatTxRSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatTxRSES.setStatus("current")
_TnSdhRawCountStatTxRSSES_Type = Counter32
_TnSdhRawCountStatTxRSSES_Object = MibTableColumn
tnSdhRawCountStatTxRSSES = _TnSdhRawCountStatTxRSSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 11),
    _TnSdhRawCountStatTxRSSES_Type()
)
tnSdhRawCountStatTxRSSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatTxRSSES.setStatus("current")
_TnSdhRawCountStatTxMSEB_Type = Counter32
_TnSdhRawCountStatTxMSEB_Object = MibTableColumn
tnSdhRawCountStatTxMSEB = _TnSdhRawCountStatTxMSEB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 12),
    _TnSdhRawCountStatTxMSEB_Type()
)
tnSdhRawCountStatTxMSEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatTxMSEB.setStatus("current")
_TnSdhRawCountStatTxMSES_Type = Counter32
_TnSdhRawCountStatTxMSES_Object = MibTableColumn
tnSdhRawCountStatTxMSES = _TnSdhRawCountStatTxMSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 13),
    _TnSdhRawCountStatTxMSES_Type()
)
tnSdhRawCountStatTxMSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatTxMSES.setStatus("current")
_TnSdhRawCountStatTxMSSES_Type = Counter32
_TnSdhRawCountStatTxMSSES_Object = MibTableColumn
tnSdhRawCountStatTxMSSES = _TnSdhRawCountStatTxMSSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 14),
    _TnSdhRawCountStatTxMSSES_Type()
)
tnSdhRawCountStatTxMSSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatTxMSSES.setStatus("current")
_TnSdhRawCountStatTxMSUAS_Type = Counter32
_TnSdhRawCountStatTxMSUAS_Object = MibTableColumn
tnSdhRawCountStatTxMSUAS = _TnSdhRawCountStatTxMSUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 15),
    _TnSdhRawCountStatTxMSUAS_Type()
)
tnSdhRawCountStatTxMSUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatTxMSUAS.setStatus("current")
_TnSdhRawCountStatRxRSUAS_Type = Counter32
_TnSdhRawCountStatRxRSUAS_Object = MibTableColumn
tnSdhRawCountStatRxRSUAS = _TnSdhRawCountStatRxRSUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 16),
    _TnSdhRawCountStatRxRSUAS_Type()
)
tnSdhRawCountStatRxRSUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatRxRSUAS.setStatus("current")
_TnSdhRawCountStatTxRSUAS_Type = Counter32
_TnSdhRawCountStatTxRSUAS_Object = MibTableColumn
tnSdhRawCountStatTxRSUAS = _TnSdhRawCountStatTxRSUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 17),
    _TnSdhRawCountStatTxRSUAS_Type()
)
tnSdhRawCountStatTxRSUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatTxRSUAS.setStatus("current")
_TnSdhRawCountStatStartTime_Type = DateAndTime
_TnSdhRawCountStatStartTime_Object = MibTableColumn
tnSdhRawCountStatStartTime = _TnSdhRawCountStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 18),
    _TnSdhRawCountStatStartTime_Type()
)
tnSdhRawCountStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatStartTime.setStatus("current")
_TnSdhRawCountStatRxMSFEEB_Type = Counter32
_TnSdhRawCountStatRxMSFEEB_Object = MibTableColumn
tnSdhRawCountStatRxMSFEEB = _TnSdhRawCountStatRxMSFEEB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 19),
    _TnSdhRawCountStatRxMSFEEB_Type()
)
tnSdhRawCountStatRxMSFEEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatRxMSFEEB.setStatus("current")
_TnSdhRawCountStatRxMSFEES_Type = Counter32
_TnSdhRawCountStatRxMSFEES_Object = MibTableColumn
tnSdhRawCountStatRxMSFEES = _TnSdhRawCountStatRxMSFEES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 20),
    _TnSdhRawCountStatRxMSFEES_Type()
)
tnSdhRawCountStatRxMSFEES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatRxMSFEES.setStatus("current")
_TnSdhRawCountStatRxMSFESES_Type = Counter32
_TnSdhRawCountStatRxMSFESES_Object = MibTableColumn
tnSdhRawCountStatRxMSFESES = _TnSdhRawCountStatRxMSFESES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 21),
    _TnSdhRawCountStatRxMSFESES_Type()
)
tnSdhRawCountStatRxMSFESES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatRxMSFESES.setStatus("current")
_TnSdhRawCountStatRxMSFEUAS_Type = Counter32
_TnSdhRawCountStatRxMSFEUAS_Object = MibTableColumn
tnSdhRawCountStatRxMSFEUAS = _TnSdhRawCountStatRxMSFEUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 28, 1, 22),
    _TnSdhRawCountStatRxMSFEUAS_Type()
)
tnSdhRawCountStatRxMSFEUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhRawCountStatRxMSFEUAS.setStatus("current")
_TnPhyCodeSublayerRawCountStatsTotalMembers_Type = Integer32
_TnPhyCodeSublayerRawCountStatsTotalMembers_Object = MibScalar
tnPhyCodeSublayerRawCountStatsTotalMembers = _TnPhyCodeSublayerRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 33),
    _TnPhyCodeSublayerRawCountStatsTotalMembers_Type()
)
tnPhyCodeSublayerRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerRawCountStatsTotalMembers.setStatus("current")
_TnPhyCodeSublayerRawCountStatsTable_Object = MibTable
tnPhyCodeSublayerRawCountStatsTable = _TnPhyCodeSublayerRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 34)
)
if mibBuilder.loadTexts:
    tnPhyCodeSublayerRawCountStatsTable.setStatus("current")
_TnPhyCodeSublayerRawCountStatsEntry_Object = MibTableRow
tnPhyCodeSublayerRawCountStatsEntry = _TnPhyCodeSublayerRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 34, 1)
)
tnPhyCodeSublayerRawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPhyCodeSublayerRawCountStatsEntry.setStatus("current")
_TnPhyCodeSublayerRawCountStatsClear_Type = TnCommand
_TnPhyCodeSublayerRawCountStatsClear_Object = MibTableColumn
tnPhyCodeSublayerRawCountStatsClear = _TnPhyCodeSublayerRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 34, 1, 1),
    _TnPhyCodeSublayerRawCountStatsClear_Type()
)
tnPhyCodeSublayerRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerRawCountStatsClear.setStatus("current")
_TnPhyCodeSublayerRawCountStatRxCV_Type = Counter32
_TnPhyCodeSublayerRawCountStatRxCV_Object = MibTableColumn
tnPhyCodeSublayerRawCountStatRxCV = _TnPhyCodeSublayerRawCountStatRxCV_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 34, 1, 2),
    _TnPhyCodeSublayerRawCountStatRxCV_Type()
)
tnPhyCodeSublayerRawCountStatRxCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerRawCountStatRxCV.setStatus("current")
_TnPhyCodeSublayerRawCountStatRxES_Type = Counter32
_TnPhyCodeSublayerRawCountStatRxES_Object = MibTableColumn
tnPhyCodeSublayerRawCountStatRxES = _TnPhyCodeSublayerRawCountStatRxES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 34, 1, 3),
    _TnPhyCodeSublayerRawCountStatRxES_Type()
)
tnPhyCodeSublayerRawCountStatRxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerRawCountStatRxES.setStatus("current")
_TnPhyCodeSublayerRawCountStatRxSES_Type = Counter32
_TnPhyCodeSublayerRawCountStatRxSES_Object = MibTableColumn
tnPhyCodeSublayerRawCountStatRxSES = _TnPhyCodeSublayerRawCountStatRxSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 34, 1, 4),
    _TnPhyCodeSublayerRawCountStatRxSES_Type()
)
tnPhyCodeSublayerRawCountStatRxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerRawCountStatRxSES.setStatus("current")
_TnPhyCodeSublayerRawCountStatRxSEFS_Type = Counter32
_TnPhyCodeSublayerRawCountStatRxSEFS_Object = MibTableColumn
tnPhyCodeSublayerRawCountStatRxSEFS = _TnPhyCodeSublayerRawCountStatRxSEFS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 34, 1, 5),
    _TnPhyCodeSublayerRawCountStatRxSEFS_Type()
)
tnPhyCodeSublayerRawCountStatRxSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerRawCountStatRxSEFS.setStatus("current")
_TnPhyCodeSublayerRawCountStatTxCV_Type = Counter32
_TnPhyCodeSublayerRawCountStatTxCV_Object = MibTableColumn
tnPhyCodeSublayerRawCountStatTxCV = _TnPhyCodeSublayerRawCountStatTxCV_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 34, 1, 6),
    _TnPhyCodeSublayerRawCountStatTxCV_Type()
)
tnPhyCodeSublayerRawCountStatTxCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerRawCountStatTxCV.setStatus("current")
_TnPhyCodeSublayerRawCountStatTxES_Type = Counter32
_TnPhyCodeSublayerRawCountStatTxES_Object = MibTableColumn
tnPhyCodeSublayerRawCountStatTxES = _TnPhyCodeSublayerRawCountStatTxES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 34, 1, 7),
    _TnPhyCodeSublayerRawCountStatTxES_Type()
)
tnPhyCodeSublayerRawCountStatTxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerRawCountStatTxES.setStatus("current")
_TnPhyCodeSublayerRawCountStatTxSES_Type = Counter32
_TnPhyCodeSublayerRawCountStatTxSES_Object = MibTableColumn
tnPhyCodeSublayerRawCountStatTxSES = _TnPhyCodeSublayerRawCountStatTxSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 34, 1, 8),
    _TnPhyCodeSublayerRawCountStatTxSES_Type()
)
tnPhyCodeSublayerRawCountStatTxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerRawCountStatTxSES.setStatus("current")
_TnPhyCodeSublayerRawCountStatTxSEFS_Type = Counter32
_TnPhyCodeSublayerRawCountStatTxSEFS_Object = MibTableColumn
tnPhyCodeSublayerRawCountStatTxSEFS = _TnPhyCodeSublayerRawCountStatTxSEFS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 34, 1, 9),
    _TnPhyCodeSublayerRawCountStatTxSEFS_Type()
)
tnPhyCodeSublayerRawCountStatTxSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerRawCountStatTxSEFS.setStatus("current")
_TnPhyCodeSublayerRawCountStatStartTime_Type = DateAndTime
_TnPhyCodeSublayerRawCountStatStartTime_Object = MibTableColumn
tnPhyCodeSublayerRawCountStatStartTime = _TnPhyCodeSublayerRawCountStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 34, 1, 10),
    _TnPhyCodeSublayerRawCountStatStartTime_Type()
)
tnPhyCodeSublayerRawCountStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPhyCodeSublayerRawCountStatStartTime.setStatus("current")
_TnDigitalWrapper64BitRawCountStatsTotalMembers_Type = Integer32
_TnDigitalWrapper64BitRawCountStatsTotalMembers_Object = MibScalar
tnDigitalWrapper64BitRawCountStatsTotalMembers = _TnDigitalWrapper64BitRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 35),
    _TnDigitalWrapper64BitRawCountStatsTotalMembers_Type()
)
tnDigitalWrapper64BitRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDigitalWrapper64BitRawCountStatsTotalMembers.setStatus("current")
_TnDigitalWrapper64BitRawCountStatsTable_Object = MibTable
tnDigitalWrapper64BitRawCountStatsTable = _TnDigitalWrapper64BitRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36)
)
if mibBuilder.loadTexts:
    tnDigitalWrapper64BitRawCountStatsTable.setStatus("current")
_TnDigitalWrapper64BitRawCountStatsEntry_Object = MibTableRow
tnDigitalWrapper64BitRawCountStatsEntry = _TnDigitalWrapper64BitRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1)
)
tnDigitalWrapper64BitRawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnDigitalWrapper64BitRawCountStatsEntry.setStatus("current")
_TnDw64BitRawCountStatsClear_Type = TnCommand
_TnDw64BitRawCountStatsClear_Object = MibTableColumn
tnDw64BitRawCountStatsClear = _TnDw64BitRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 1),
    _TnDw64BitRawCountStatsClear_Type()
)
tnDw64BitRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatsClear.setStatus("current")
_TnDw64BitRawCountStatRxRSCorrCnt_Type = Counter64
_TnDw64BitRawCountStatRxRSCorrCnt_Object = MibTableColumn
tnDw64BitRawCountStatRxRSCorrCnt = _TnDw64BitRawCountStatRxRSCorrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 2),
    _TnDw64BitRawCountStatRxRSCorrCnt_Type()
)
tnDw64BitRawCountStatRxRSCorrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxRSCorrCnt.setStatus("current")
_TnDw64BitRawCountStatRxRSUncorrCnt_Type = Counter64
_TnDw64BitRawCountStatRxRSUncorrCnt_Object = MibTableColumn
tnDw64BitRawCountStatRxRSUncorrCnt = _TnDw64BitRawCountStatRxRSUncorrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 3),
    _TnDw64BitRawCountStatRxRSUncorrCnt_Type()
)
tnDw64BitRawCountStatRxRSUncorrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxRSUncorrCnt.setStatus("current")
_TnDw64BitRawCountStatRxSMBIP8ErrCnt_Type = Counter64
_TnDw64BitRawCountStatRxSMBIP8ErrCnt_Object = MibTableColumn
tnDw64BitRawCountStatRxSMBIP8ErrCnt = _TnDw64BitRawCountStatRxSMBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 4),
    _TnDw64BitRawCountStatRxSMBIP8ErrCnt_Type()
)
tnDw64BitRawCountStatRxSMBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxSMBIP8ErrCnt.setStatus("current")
_TnDw64BitRawCountStatRxPMBIP8ErrCnt_Type = Counter64
_TnDw64BitRawCountStatRxPMBIP8ErrCnt_Object = MibTableColumn
tnDw64BitRawCountStatRxPMBIP8ErrCnt = _TnDw64BitRawCountStatRxPMBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 5),
    _TnDw64BitRawCountStatRxPMBIP8ErrCnt_Type()
)
tnDw64BitRawCountStatRxPMBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxPMBIP8ErrCnt.setStatus("current")
_TnDw64BitRawCountStatRxSMBEIErrCnt_Type = Counter64
_TnDw64BitRawCountStatRxSMBEIErrCnt_Object = MibTableColumn
tnDw64BitRawCountStatRxSMBEIErrCnt = _TnDw64BitRawCountStatRxSMBEIErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 6),
    _TnDw64BitRawCountStatRxSMBEIErrCnt_Type()
)
tnDw64BitRawCountStatRxSMBEIErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxSMBEIErrCnt.setStatus("current")
_TnDw64BitRawCountStatRxPMBEIErrCnt_Type = Counter64
_TnDw64BitRawCountStatRxPMBEIErrCnt_Object = MibTableColumn
tnDw64BitRawCountStatRxPMBEIErrCnt = _TnDw64BitRawCountStatRxPMBEIErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 7),
    _TnDw64BitRawCountStatRxPMBEIErrCnt_Type()
)
tnDw64BitRawCountStatRxPMBEIErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxPMBEIErrCnt.setStatus("current")
_TnDw64BitRawCountStatRxRSSES_Type = Counter64
_TnDw64BitRawCountStatRxRSSES_Object = MibTableColumn
tnDw64BitRawCountStatRxRSSES = _TnDw64BitRawCountStatRxRSSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 8),
    _TnDw64BitRawCountStatRxRSSES_Type()
)
tnDw64BitRawCountStatRxRSSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxRSSES.setStatus("current")
_TnDw64BitRawCountStatRxSMES_Type = Counter64
_TnDw64BitRawCountStatRxSMES_Object = MibTableColumn
tnDw64BitRawCountStatRxSMES = _TnDw64BitRawCountStatRxSMES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 9),
    _TnDw64BitRawCountStatRxSMES_Type()
)
tnDw64BitRawCountStatRxSMES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxSMES.setStatus("current")
_TnDw64BitRawCountStatRxPMES_Type = Counter64
_TnDw64BitRawCountStatRxPMES_Object = MibTableColumn
tnDw64BitRawCountStatRxPMES = _TnDw64BitRawCountStatRxPMES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 10),
    _TnDw64BitRawCountStatRxPMES_Type()
)
tnDw64BitRawCountStatRxPMES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxPMES.setStatus("current")
_TnDw64BitRawCountStatRxSMSES_Type = Counter64
_TnDw64BitRawCountStatRxSMSES_Object = MibTableColumn
tnDw64BitRawCountStatRxSMSES = _TnDw64BitRawCountStatRxSMSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 11),
    _TnDw64BitRawCountStatRxSMSES_Type()
)
tnDw64BitRawCountStatRxSMSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxSMSES.setStatus("current")
_TnDw64BitRawCountStatRxPMSES_Type = Counter64
_TnDw64BitRawCountStatRxPMSES_Object = MibTableColumn
tnDw64BitRawCountStatRxPMSES = _TnDw64BitRawCountStatRxPMSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 12),
    _TnDw64BitRawCountStatRxPMSES_Type()
)
tnDw64BitRawCountStatRxPMSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxPMSES.setStatus("current")
_TnDw64BitRawCountStatRxSMUAS_Type = Counter64
_TnDw64BitRawCountStatRxSMUAS_Object = MibTableColumn
tnDw64BitRawCountStatRxSMUAS = _TnDw64BitRawCountStatRxSMUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 13),
    _TnDw64BitRawCountStatRxSMUAS_Type()
)
tnDw64BitRawCountStatRxSMUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxSMUAS.setStatus("current")
_TnDw64BitRawCountStatRxPMUAS_Type = Counter64
_TnDw64BitRawCountStatRxPMUAS_Object = MibTableColumn
tnDw64BitRawCountStatRxPMUAS = _TnDw64BitRawCountStatRxPMUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 14),
    _TnDw64BitRawCountStatRxPMUAS_Type()
)
tnDw64BitRawCountStatRxPMUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxPMUAS.setStatus("current")
_TnDw64BitRawCountStatStartTime_Type = DateAndTime
_TnDw64BitRawCountStatStartTime_Object = MibTableColumn
tnDw64BitRawCountStatStartTime = _TnDw64BitRawCountStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 15),
    _TnDw64BitRawCountStatStartTime_Type()
)
tnDw64BitRawCountStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatStartTime.setStatus("current")
_TnDw64BitRawCountStatRxBERPreFEC_Type = Counter64
_TnDw64BitRawCountStatRxBERPreFEC_Object = MibTableColumn
tnDw64BitRawCountStatRxBERPreFEC = _TnDw64BitRawCountStatRxBERPreFEC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 16),
    _TnDw64BitRawCountStatRxBERPreFEC_Type()
)
tnDw64BitRawCountStatRxBERPreFEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxBERPreFEC.setStatus("current")
_TnDw64BitRawCountStatRxBERPostFEC_Type = Counter64
_TnDw64BitRawCountStatRxBERPostFEC_Object = MibTableColumn
tnDw64BitRawCountStatRxBERPostFEC = _TnDw64BitRawCountStatRxBERPostFEC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 17),
    _TnDw64BitRawCountStatRxBERPostFEC_Type()
)
tnDw64BitRawCountStatRxBERPostFEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxBERPostFEC.setStatus("current")
_TnDw64BitRawCountStatRxSMFEBIP8ErrCnt_Type = Counter64
_TnDw64BitRawCountStatRxSMFEBIP8ErrCnt_Object = MibTableColumn
tnDw64BitRawCountStatRxSMFEBIP8ErrCnt = _TnDw64BitRawCountStatRxSMFEBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 18),
    _TnDw64BitRawCountStatRxSMFEBIP8ErrCnt_Type()
)
tnDw64BitRawCountStatRxSMFEBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxSMFEBIP8ErrCnt.setStatus("current")
_TnDw64BitRawCountStatRxPMFEBIP8ErrCnt_Type = Counter64
_TnDw64BitRawCountStatRxPMFEBIP8ErrCnt_Object = MibTableColumn
tnDw64BitRawCountStatRxPMFEBIP8ErrCnt = _TnDw64BitRawCountStatRxPMFEBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 19),
    _TnDw64BitRawCountStatRxPMFEBIP8ErrCnt_Type()
)
tnDw64BitRawCountStatRxPMFEBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxPMFEBIP8ErrCnt.setStatus("current")
_TnDw64BitRawCountStatRxSMBIAESErrCnt_Type = Counter64
_TnDw64BitRawCountStatRxSMBIAESErrCnt_Object = MibTableColumn
tnDw64BitRawCountStatRxSMBIAESErrCnt = _TnDw64BitRawCountStatRxSMBIAESErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 20),
    _TnDw64BitRawCountStatRxSMBIAESErrCnt_Type()
)
tnDw64BitRawCountStatRxSMBIAESErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxSMBIAESErrCnt.setStatus("current")
_TnDw64BitRawCountStatRxSMIAESErrCnt_Type = Counter64
_TnDw64BitRawCountStatRxSMIAESErrCnt_Object = MibTableColumn
tnDw64BitRawCountStatRxSMIAESErrCnt = _TnDw64BitRawCountStatRxSMIAESErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 21),
    _TnDw64BitRawCountStatRxSMIAESErrCnt_Type()
)
tnDw64BitRawCountStatRxSMIAESErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxSMIAESErrCnt.setStatus("current")
_TnDw64BitRawCountStatRxSMFEES_Type = Counter64
_TnDw64BitRawCountStatRxSMFEES_Object = MibTableColumn
tnDw64BitRawCountStatRxSMFEES = _TnDw64BitRawCountStatRxSMFEES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 22),
    _TnDw64BitRawCountStatRxSMFEES_Type()
)
tnDw64BitRawCountStatRxSMFEES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxSMFEES.setStatus("current")
_TnDw64BitRawCountStatRxPMFEES_Type = Counter64
_TnDw64BitRawCountStatRxPMFEES_Object = MibTableColumn
tnDw64BitRawCountStatRxPMFEES = _TnDw64BitRawCountStatRxPMFEES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 23),
    _TnDw64BitRawCountStatRxPMFEES_Type()
)
tnDw64BitRawCountStatRxPMFEES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxPMFEES.setStatus("current")
_TnDw64BitRawCountStatRxSMFESES_Type = Counter64
_TnDw64BitRawCountStatRxSMFESES_Object = MibTableColumn
tnDw64BitRawCountStatRxSMFESES = _TnDw64BitRawCountStatRxSMFESES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 24),
    _TnDw64BitRawCountStatRxSMFESES_Type()
)
tnDw64BitRawCountStatRxSMFESES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxSMFESES.setStatus("current")
_TnDw64BitRawCountStatRxPMFESES_Type = Counter64
_TnDw64BitRawCountStatRxPMFESES_Object = MibTableColumn
tnDw64BitRawCountStatRxPMFESES = _TnDw64BitRawCountStatRxPMFESES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 25),
    _TnDw64BitRawCountStatRxPMFESES_Type()
)
tnDw64BitRawCountStatRxPMFESES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxPMFESES.setStatus("current")
_TnDw64BitRawCountStatRxSMFEUAS_Type = Counter64
_TnDw64BitRawCountStatRxSMFEUAS_Object = MibTableColumn
tnDw64BitRawCountStatRxSMFEUAS = _TnDw64BitRawCountStatRxSMFEUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 26),
    _TnDw64BitRawCountStatRxSMFEUAS_Type()
)
tnDw64BitRawCountStatRxSMFEUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxSMFEUAS.setStatus("current")
_TnDw64BitRawCountStatRxPMFEUAS_Type = Counter64
_TnDw64BitRawCountStatRxPMFEUAS_Object = MibTableColumn
tnDw64BitRawCountStatRxPMFEUAS = _TnDw64BitRawCountStatRxPMFEUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 36, 1, 27),
    _TnDw64BitRawCountStatRxPMFEUAS_Type()
)
tnDw64BitRawCountStatRxPMFEUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitRawCountStatRxPMFEUAS.setStatus("current")
_TnCdrRawCountStatsTotalMembers_Type = Integer32
_TnCdrRawCountStatsTotalMembers_Object = MibScalar
tnCdrRawCountStatsTotalMembers = _TnCdrRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 37),
    _TnCdrRawCountStatsTotalMembers_Type()
)
tnCdrRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCdrRawCountStatsTotalMembers.setStatus("current")
_TnCdrRawCountStatsTable_Object = MibTable
tnCdrRawCountStatsTable = _TnCdrRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 38)
)
if mibBuilder.loadTexts:
    tnCdrRawCountStatsTable.setStatus("current")
_TnCdrRawCountStatsEntry_Object = MibTableRow
tnCdrRawCountStatsEntry = _TnCdrRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 38, 1)
)
tnCdrRawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnCdrRawCountStatsEntry.setStatus("current")
_TnCdrRawCountStatsClear_Type = TnCommand
_TnCdrRawCountStatsClear_Object = MibTableColumn
tnCdrRawCountStatsClear = _TnCdrRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 38, 1, 1),
    _TnCdrRawCountStatsClear_Type()
)
tnCdrRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCdrRawCountStatsClear.setStatus("current")
_TnCdrRawCountStatMin_Type = Integer32
_TnCdrRawCountStatMin_Object = MibTableColumn
tnCdrRawCountStatMin = _TnCdrRawCountStatMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 38, 1, 2),
    _TnCdrRawCountStatMin_Type()
)
tnCdrRawCountStatMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCdrRawCountStatMin.setStatus("current")
if mibBuilder.loadTexts:
    tnCdrRawCountStatMin.setUnits("ps/nm")
_TnCdrRawCountStatMax_Type = Integer32
_TnCdrRawCountStatMax_Object = MibTableColumn
tnCdrRawCountStatMax = _TnCdrRawCountStatMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 38, 1, 3),
    _TnCdrRawCountStatMax_Type()
)
tnCdrRawCountStatMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCdrRawCountStatMax.setStatus("current")
if mibBuilder.loadTexts:
    tnCdrRawCountStatMax.setUnits("ps/nm")
_TnCdrRawCountStatAverage_Type = Integer32
_TnCdrRawCountStatAverage_Object = MibTableColumn
tnCdrRawCountStatAverage = _TnCdrRawCountStatAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 38, 1, 4),
    _TnCdrRawCountStatAverage_Type()
)
tnCdrRawCountStatAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCdrRawCountStatAverage.setStatus("current")
if mibBuilder.loadTexts:
    tnCdrRawCountStatAverage.setUnits("ps/nm")
_TnCdrRawCountStatStartTime_Type = DateAndTime
_TnCdrRawCountStatStartTime_Object = MibTableColumn
tnCdrRawCountStatStartTime = _TnCdrRawCountStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 38, 1, 5),
    _TnCdrRawCountStatStartTime_Type()
)
tnCdrRawCountStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCdrRawCountStatStartTime.setStatus("current")
_TnDgdrRawCountStatsTotalMembers_Type = Integer32
_TnDgdrRawCountStatsTotalMembers_Object = MibScalar
tnDgdrRawCountStatsTotalMembers = _TnDgdrRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 39),
    _TnDgdrRawCountStatsTotalMembers_Type()
)
tnDgdrRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDgdrRawCountStatsTotalMembers.setStatus("current")
_TnDgdrRawCountStatsTable_Object = MibTable
tnDgdrRawCountStatsTable = _TnDgdrRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 40)
)
if mibBuilder.loadTexts:
    tnDgdrRawCountStatsTable.setStatus("current")
_TnDgdrRawCountStatsEntry_Object = MibTableRow
tnDgdrRawCountStatsEntry = _TnDgdrRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 40, 1)
)
tnDgdrRawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnDgdrRawCountStatsEntry.setStatus("current")
_TnDgdrRawCountStatsClear_Type = TnCommand
_TnDgdrRawCountStatsClear_Object = MibTableColumn
tnDgdrRawCountStatsClear = _TnDgdrRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 40, 1, 1),
    _TnDgdrRawCountStatsClear_Type()
)
tnDgdrRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDgdrRawCountStatsClear.setStatus("current")
_TnDgdrRawCountStatMin_Type = Integer32
_TnDgdrRawCountStatMin_Object = MibTableColumn
tnDgdrRawCountStatMin = _TnDgdrRawCountStatMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 40, 1, 2),
    _TnDgdrRawCountStatMin_Type()
)
tnDgdrRawCountStatMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDgdrRawCountStatMin.setStatus("current")
if mibBuilder.loadTexts:
    tnDgdrRawCountStatMin.setUnits("ps")
_TnDgdrRawCountStatMax_Type = Integer32
_TnDgdrRawCountStatMax_Object = MibTableColumn
tnDgdrRawCountStatMax = _TnDgdrRawCountStatMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 40, 1, 3),
    _TnDgdrRawCountStatMax_Type()
)
tnDgdrRawCountStatMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDgdrRawCountStatMax.setStatus("current")
if mibBuilder.loadTexts:
    tnDgdrRawCountStatMax.setUnits("ps")
_TnDgdrRawCountStatAverage_Type = Integer32
_TnDgdrRawCountStatAverage_Object = MibTableColumn
tnDgdrRawCountStatAverage = _TnDgdrRawCountStatAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 40, 1, 4),
    _TnDgdrRawCountStatAverage_Type()
)
tnDgdrRawCountStatAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDgdrRawCountStatAverage.setStatus("current")
if mibBuilder.loadTexts:
    tnDgdrRawCountStatAverage.setUnits("ps")
_TnDgdrRawCountStatStartTime_Type = DateAndTime
_TnDgdrRawCountStatStartTime_Object = MibTableColumn
tnDgdrRawCountStatStartTime = _TnDgdrRawCountStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 40, 1, 5),
    _TnDgdrRawCountStatStartTime_Type()
)
tnDgdrRawCountStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDgdrRawCountStatStartTime.setStatus("current")
_TnFoffrRawCountStatsTotalMembers_Type = Integer32
_TnFoffrRawCountStatsTotalMembers_Object = MibScalar
tnFoffrRawCountStatsTotalMembers = _TnFoffrRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 41),
    _TnFoffrRawCountStatsTotalMembers_Type()
)
tnFoffrRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFoffrRawCountStatsTotalMembers.setStatus("current")
_TnFoffrRawCountStatsTable_Object = MibTable
tnFoffrRawCountStatsTable = _TnFoffrRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 42)
)
if mibBuilder.loadTexts:
    tnFoffrRawCountStatsTable.setStatus("current")
_TnFoffrRawCountStatsEntry_Object = MibTableRow
tnFoffrRawCountStatsEntry = _TnFoffrRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 42, 1)
)
tnFoffrRawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnFoffrRawCountStatsEntry.setStatus("current")
_TnFoffrRawCountStatsClear_Type = TnCommand
_TnFoffrRawCountStatsClear_Object = MibTableColumn
tnFoffrRawCountStatsClear = _TnFoffrRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 42, 1, 1),
    _TnFoffrRawCountStatsClear_Type()
)
tnFoffrRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnFoffrRawCountStatsClear.setStatus("current")
_TnFoffrRawCountStatMin_Type = Integer32
_TnFoffrRawCountStatMin_Object = MibTableColumn
tnFoffrRawCountStatMin = _TnFoffrRawCountStatMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 42, 1, 2),
    _TnFoffrRawCountStatMin_Type()
)
tnFoffrRawCountStatMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFoffrRawCountStatMin.setStatus("current")
if mibBuilder.loadTexts:
    tnFoffrRawCountStatMin.setUnits("GHz")
_TnFoffrRawCountStatMax_Type = Integer32
_TnFoffrRawCountStatMax_Object = MibTableColumn
tnFoffrRawCountStatMax = _TnFoffrRawCountStatMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 42, 1, 3),
    _TnFoffrRawCountStatMax_Type()
)
tnFoffrRawCountStatMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFoffrRawCountStatMax.setStatus("current")
if mibBuilder.loadTexts:
    tnFoffrRawCountStatMax.setUnits("GHz")
_TnFoffrRawCountStatAverage_Type = Integer32
_TnFoffrRawCountStatAverage_Object = MibTableColumn
tnFoffrRawCountStatAverage = _TnFoffrRawCountStatAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 42, 1, 4),
    _TnFoffrRawCountStatAverage_Type()
)
tnFoffrRawCountStatAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFoffrRawCountStatAverage.setStatus("current")
if mibBuilder.loadTexts:
    tnFoffrRawCountStatAverage.setUnits("GHz")
_TnFoffrRawCountStatStartTime_Type = DateAndTime
_TnFoffrRawCountStatStartTime_Object = MibTableColumn
tnFoffrRawCountStatStartTime = _TnFoffrRawCountStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 42, 1, 5),
    _TnFoffrRawCountStatStartTime_Type()
)
tnFoffrRawCountStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFoffrRawCountStatStartTime.setStatus("current")
_TnE1RawCountStatsTotalMembers_Type = Integer32
_TnE1RawCountStatsTotalMembers_Object = MibScalar
tnE1RawCountStatsTotalMembers = _TnE1RawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 43),
    _TnE1RawCountStatsTotalMembers_Type()
)
tnE1RawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1RawCountStatsTotalMembers.setStatus("current")
_TnE1RawCountStatsTable_Object = MibTable
tnE1RawCountStatsTable = _TnE1RawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 44)
)
if mibBuilder.loadTexts:
    tnE1RawCountStatsTable.setStatus("current")
_TnE1RawCountStatsEntry_Object = MibTableRow
tnE1RawCountStatsEntry = _TnE1RawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 44, 1)
)
tnE1RawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnE1RawCountStatsEntry.setStatus("current")
_TnE1RawCountStatsClear_Type = TnCommand
_TnE1RawCountStatsClear_Object = MibTableColumn
tnE1RawCountStatsClear = _TnE1RawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 44, 1, 1),
    _TnE1RawCountStatsClear_Type()
)
tnE1RawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnE1RawCountStatsClear.setStatus("current")
_TnE1RawCountStatRxBBEP_Type = Counter32
_TnE1RawCountStatRxBBEP_Object = MibTableColumn
tnE1RawCountStatRxBBEP = _TnE1RawCountStatRxBBEP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 44, 1, 2),
    _TnE1RawCountStatRxBBEP_Type()
)
tnE1RawCountStatRxBBEP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1RawCountStatRxBBEP.setStatus("current")
_TnE1RawCountStatRxESP_Type = Counter32
_TnE1RawCountStatRxESP_Object = MibTableColumn
tnE1RawCountStatRxESP = _TnE1RawCountStatRxESP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 44, 1, 3),
    _TnE1RawCountStatRxESP_Type()
)
tnE1RawCountStatRxESP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1RawCountStatRxESP.setStatus("current")
_TnE1RawCountStatRxSESP_Type = Counter32
_TnE1RawCountStatRxSESP_Object = MibTableColumn
tnE1RawCountStatRxSESP = _TnE1RawCountStatRxSESP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 44, 1, 4),
    _TnE1RawCountStatRxSESP_Type()
)
tnE1RawCountStatRxSESP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1RawCountStatRxSESP.setStatus("current")
_TnE1RawCountStatRxUASP_Type = Counter32
_TnE1RawCountStatRxUASP_Object = MibTableColumn
tnE1RawCountStatRxUASP = _TnE1RawCountStatRxUASP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 44, 1, 5),
    _TnE1RawCountStatRxUASP_Type()
)
tnE1RawCountStatRxUASP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1RawCountStatRxUASP.setStatus("current")
_TnE1RawCountStatRxESL_Type = Counter32
_TnE1RawCountStatRxESL_Object = MibTableColumn
tnE1RawCountStatRxESL = _TnE1RawCountStatRxESL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 44, 1, 6),
    _TnE1RawCountStatRxESL_Type()
)
tnE1RawCountStatRxESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1RawCountStatRxESL.setStatus("current")
_TnE1RawCountStatRxSESL_Type = Counter32
_TnE1RawCountStatRxSESL_Object = MibTableColumn
tnE1RawCountStatRxSESL = _TnE1RawCountStatRxSESL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 44, 1, 7),
    _TnE1RawCountStatRxSESL_Type()
)
tnE1RawCountStatRxSESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1RawCountStatRxSESL.setStatus("current")
_TnE1RawCountStatTxBBEP_Type = Counter32
_TnE1RawCountStatTxBBEP_Object = MibTableColumn
tnE1RawCountStatTxBBEP = _TnE1RawCountStatTxBBEP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 44, 1, 8),
    _TnE1RawCountStatTxBBEP_Type()
)
tnE1RawCountStatTxBBEP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1RawCountStatTxBBEP.setStatus("current")
_TnE1RawCountStatTxESP_Type = Counter32
_TnE1RawCountStatTxESP_Object = MibTableColumn
tnE1RawCountStatTxESP = _TnE1RawCountStatTxESP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 44, 1, 9),
    _TnE1RawCountStatTxESP_Type()
)
tnE1RawCountStatTxESP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1RawCountStatTxESP.setStatus("current")
_TnE1RawCountStatTxSESP_Type = Counter32
_TnE1RawCountStatTxSESP_Object = MibTableColumn
tnE1RawCountStatTxSESP = _TnE1RawCountStatTxSESP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 44, 1, 10),
    _TnE1RawCountStatTxSESP_Type()
)
tnE1RawCountStatTxSESP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1RawCountStatTxSESP.setStatus("current")
_TnE1RawCountStatTxUASP_Type = Counter32
_TnE1RawCountStatTxUASP_Object = MibTableColumn
tnE1RawCountStatTxUASP = _TnE1RawCountStatTxUASP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 44, 1, 11),
    _TnE1RawCountStatTxUASP_Type()
)
tnE1RawCountStatTxUASP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1RawCountStatTxUASP.setStatus("current")
_TnE1RawCountStatStartTime_Type = DateAndTime
_TnE1RawCountStatStartTime_Object = MibTableColumn
tnE1RawCountStatStartTime = _TnE1RawCountStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 44, 1, 12),
    _TnE1RawCountStatStartTime_Type()
)
tnE1RawCountStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnE1RawCountStatStartTime.setStatus("current")
_TnPreFECBitsRawCountStatsTotalMembers_Type = Integer32
_TnPreFECBitsRawCountStatsTotalMembers_Object = MibScalar
tnPreFECBitsRawCountStatsTotalMembers = _TnPreFECBitsRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 45),
    _TnPreFECBitsRawCountStatsTotalMembers_Type()
)
tnPreFECBitsRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPreFECBitsRawCountStatsTotalMembers.setStatus("current")
_TnPreFECBitsRawCountStatsTable_Object = MibTable
tnPreFECBitsRawCountStatsTable = _TnPreFECBitsRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 46)
)
if mibBuilder.loadTexts:
    tnPreFECBitsRawCountStatsTable.setStatus("current")
_TnPreFECBitsRawCountStatsEntry_Object = MibTableRow
tnPreFECBitsRawCountStatsEntry = _TnPreFECBitsRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 46, 1)
)
tnPreFECBitsRawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPreFECBitsRawCountStatsEntry.setStatus("current")
_TnPreFECBitsRawCountStatsClear_Type = TnCommand
_TnPreFECBitsRawCountStatsClear_Object = MibTableColumn
tnPreFECBitsRawCountStatsClear = _TnPreFECBitsRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 46, 1, 1),
    _TnPreFECBitsRawCountStatsClear_Type()
)
tnPreFECBitsRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPreFECBitsRawCountStatsClear.setStatus("current")
_TnPreFECBitsRawCountStatMin_Type = Counter64
_TnPreFECBitsRawCountStatMin_Object = MibTableColumn
tnPreFECBitsRawCountStatMin = _TnPreFECBitsRawCountStatMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 46, 1, 2),
    _TnPreFECBitsRawCountStatMin_Type()
)
tnPreFECBitsRawCountStatMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPreFECBitsRawCountStatMin.setStatus("current")
if mibBuilder.loadTexts:
    tnPreFECBitsRawCountStatMin.setUnits("Bits in 1-second")
_TnPreFECBitsRawCountStatMax_Type = Counter64
_TnPreFECBitsRawCountStatMax_Object = MibTableColumn
tnPreFECBitsRawCountStatMax = _TnPreFECBitsRawCountStatMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 46, 1, 3),
    _TnPreFECBitsRawCountStatMax_Type()
)
tnPreFECBitsRawCountStatMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPreFECBitsRawCountStatMax.setStatus("current")
if mibBuilder.loadTexts:
    tnPreFECBitsRawCountStatMax.setUnits("Bits in 1-second.")
_TnPreFECBitsRawCountStatAverage_Type = Counter64
_TnPreFECBitsRawCountStatAverage_Object = MibTableColumn
tnPreFECBitsRawCountStatAverage = _TnPreFECBitsRawCountStatAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 46, 1, 4),
    _TnPreFECBitsRawCountStatAverage_Type()
)
tnPreFECBitsRawCountStatAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPreFECBitsRawCountStatAverage.setStatus("current")
if mibBuilder.loadTexts:
    tnPreFECBitsRawCountStatAverage.setUnits("Bits in 1-second")
_TnPreFECBitsRawCountStatStartTime_Type = DateAndTime
_TnPreFECBitsRawCountStatStartTime_Object = MibTableColumn
tnPreFECBitsRawCountStatStartTime = _TnPreFECBitsRawCountStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 46, 1, 5),
    _TnPreFECBitsRawCountStatStartTime_Type()
)
tnPreFECBitsRawCountStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPreFECBitsRawCountStatStartTime.setStatus("current")
_TnEncrypt64BitRawCountStatsTotalMembers_Type = Integer32
_TnEncrypt64BitRawCountStatsTotalMembers_Object = MibScalar
tnEncrypt64BitRawCountStatsTotalMembers = _TnEncrypt64BitRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 49),
    _TnEncrypt64BitRawCountStatsTotalMembers_Type()
)
tnEncrypt64BitRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEncrypt64BitRawCountStatsTotalMembers.setStatus("current")
_TnEncrypt64BitRawCountStatsTable_Object = MibTable
tnEncrypt64BitRawCountStatsTable = _TnEncrypt64BitRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 50)
)
if mibBuilder.loadTexts:
    tnEncrypt64BitRawCountStatsTable.setStatus("current")
_TnEncrypt64BitRawCountStatsEntry_Object = MibTableRow
tnEncrypt64BitRawCountStatsEntry = _TnEncrypt64BitRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 50, 1)
)
tnEncrypt64BitRawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnEncrypt64BitRawCountStatsEntry.setStatus("current")
_TnEncrypt64BitRawCountStatsClear_Type = TnCommand
_TnEncrypt64BitRawCountStatsClear_Object = MibTableColumn
tnEncrypt64BitRawCountStatsClear = _TnEncrypt64BitRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 50, 1, 1),
    _TnEncrypt64BitRawCountStatsClear_Type()
)
tnEncrypt64BitRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEncrypt64BitRawCountStatsClear.setStatus("current")
_TnEncrypt64BitRawCountStatStartTime_Type = DateAndTime
_TnEncrypt64BitRawCountStatStartTime_Object = MibTableColumn
tnEncrypt64BitRawCountStatStartTime = _TnEncrypt64BitRawCountStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 50, 1, 2),
    _TnEncrypt64BitRawCountStatStartTime_Type()
)
tnEncrypt64BitRawCountStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEncrypt64BitRawCountStatStartTime.setStatus("current")
_TnEncrypt64BitRawCountStatTx128BitBlkCnt_Type = Counter64
_TnEncrypt64BitRawCountStatTx128BitBlkCnt_Object = MibTableColumn
tnEncrypt64BitRawCountStatTx128BitBlkCnt = _TnEncrypt64BitRawCountStatTx128BitBlkCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 50, 1, 3),
    _TnEncrypt64BitRawCountStatTx128BitBlkCnt_Type()
)
tnEncrypt64BitRawCountStatTx128BitBlkCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEncrypt64BitRawCountStatTx128BitBlkCnt.setStatus("current")
_TnEncrypt64BitRawCountStatRxFailToDecryptCnt_Type = Counter64
_TnEncrypt64BitRawCountStatRxFailToDecryptCnt_Object = MibTableColumn
tnEncrypt64BitRawCountStatRxFailToDecryptCnt = _TnEncrypt64BitRawCountStatRxFailToDecryptCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 50, 1, 4),
    _TnEncrypt64BitRawCountStatRxFailToDecryptCnt_Type()
)
tnEncrypt64BitRawCountStatRxFailToDecryptCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEncrypt64BitRawCountStatRxFailToDecryptCnt.setStatus("current")
_TnOthOdukRawCountStatsRxTotalMembers_Type = Integer32
_TnOthOdukRawCountStatsRxTotalMembers_Object = MibScalar
tnOthOdukRawCountStatsRxTotalMembers = _TnOthOdukRawCountStatsRxTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 51),
    _TnOthOdukRawCountStatsRxTotalMembers_Type()
)
tnOthOdukRawCountStatsRxTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsRxTotalMembers.setStatus("current")
_TnOthOdukRawCountStatsRxTable_Object = MibTable
tnOthOdukRawCountStatsRxTable = _TnOthOdukRawCountStatsRxTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 52)
)
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsRxTable.setStatus("current")
_TnOthOdukRawCountStatsRxEntry_Object = MibTableRow
tnOthOdukRawCountStatsRxEntry = _TnOthOdukRawCountStatsRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 52, 1)
)
tnOthOdukRawCountStatsRxEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsRxEntry.setStatus("current")
_TnOthOdukRawCountStatsRxClear_Type = TnCommand
_TnOthOdukRawCountStatsRxClear_Object = MibTableColumn
tnOthOdukRawCountStatsRxClear = _TnOthOdukRawCountStatsRxClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 52, 1, 1),
    _TnOthOdukRawCountStatsRxClear_Type()
)
tnOthOdukRawCountStatsRxClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsRxClear.setStatus("current")
_TnOthOdukRawCountStatsRxStartTime_Type = DateAndTime
_TnOthOdukRawCountStatsRxStartTime_Object = MibTableColumn
tnOthOdukRawCountStatsRxStartTime = _TnOthOdukRawCountStatsRxStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 52, 1, 2),
    _TnOthOdukRawCountStatsRxStartTime_Type()
)
tnOthOdukRawCountStatsRxStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsRxStartTime.setStatus("current")
_TnOthOdukRawCountStatRxNeBIP8ErrCnt_Type = Counter64
_TnOthOdukRawCountStatRxNeBIP8ErrCnt_Object = MibTableColumn
tnOthOdukRawCountStatRxNeBIP8ErrCnt = _TnOthOdukRawCountStatRxNeBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 52, 1, 3),
    _TnOthOdukRawCountStatRxNeBIP8ErrCnt_Type()
)
tnOthOdukRawCountStatRxNeBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatRxNeBIP8ErrCnt.setStatus("current")
_TnOthOdukRawCountStatRxNeES_Type = Counter64
_TnOthOdukRawCountStatRxNeES_Object = MibTableColumn
tnOthOdukRawCountStatRxNeES = _TnOthOdukRawCountStatRxNeES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 52, 1, 4),
    _TnOthOdukRawCountStatRxNeES_Type()
)
tnOthOdukRawCountStatRxNeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatRxNeES.setStatus("current")
_TnOthOdukRawCountStatRxNeSES_Type = Counter64
_TnOthOdukRawCountStatRxNeSES_Object = MibTableColumn
tnOthOdukRawCountStatRxNeSES = _TnOthOdukRawCountStatRxNeSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 52, 1, 5),
    _TnOthOdukRawCountStatRxNeSES_Type()
)
tnOthOdukRawCountStatRxNeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatRxNeSES.setStatus("current")
_TnOthOdukRawCountStatRxNeUAS_Type = Counter64
_TnOthOdukRawCountStatRxNeUAS_Object = MibTableColumn
tnOthOdukRawCountStatRxNeUAS = _TnOthOdukRawCountStatRxNeUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 52, 1, 6),
    _TnOthOdukRawCountStatRxNeUAS_Type()
)
tnOthOdukRawCountStatRxNeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatRxNeUAS.setStatus("current")
_TnOthOdukRawCountStatRxFeBIP8ErrCnt_Type = Counter64
_TnOthOdukRawCountStatRxFeBIP8ErrCnt_Object = MibTableColumn
tnOthOdukRawCountStatRxFeBIP8ErrCnt = _TnOthOdukRawCountStatRxFeBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 52, 1, 7),
    _TnOthOdukRawCountStatRxFeBIP8ErrCnt_Type()
)
tnOthOdukRawCountStatRxFeBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatRxFeBIP8ErrCnt.setStatus("current")
_TnOthOdukRawCountStatRxFeES_Type = Counter64
_TnOthOdukRawCountStatRxFeES_Object = MibTableColumn
tnOthOdukRawCountStatRxFeES = _TnOthOdukRawCountStatRxFeES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 52, 1, 8),
    _TnOthOdukRawCountStatRxFeES_Type()
)
tnOthOdukRawCountStatRxFeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatRxFeES.setStatus("current")
_TnOthOdukRawCountStatRxFeSES_Type = Counter64
_TnOthOdukRawCountStatRxFeSES_Object = MibTableColumn
tnOthOdukRawCountStatRxFeSES = _TnOthOdukRawCountStatRxFeSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 52, 1, 9),
    _TnOthOdukRawCountStatRxFeSES_Type()
)
tnOthOdukRawCountStatRxFeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatRxFeSES.setStatus("current")
_TnOthOdukRawCountStatRxFeUAS_Type = Counter64
_TnOthOdukRawCountStatRxFeUAS_Object = MibTableColumn
tnOthOdukRawCountStatRxFeUAS = _TnOthOdukRawCountStatRxFeUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 52, 1, 10),
    _TnOthOdukRawCountStatRxFeUAS_Type()
)
tnOthOdukRawCountStatRxFeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatRxFeUAS.setStatus("current")
_TnOthOdukRawCountStatsTxTotalMembers_Type = Integer32
_TnOthOdukRawCountStatsTxTotalMembers_Object = MibScalar
tnOthOdukRawCountStatsTxTotalMembers = _TnOthOdukRawCountStatsTxTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 53),
    _TnOthOdukRawCountStatsTxTotalMembers_Type()
)
tnOthOdukRawCountStatsTxTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsTxTotalMembers.setStatus("current")
_TnOthOdukRawCountStatsTxTable_Object = MibTable
tnOthOdukRawCountStatsTxTable = _TnOthOdukRawCountStatsTxTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 54)
)
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsTxTable.setStatus("current")
_TnOthOdukRawCountStatsTxEntry_Object = MibTableRow
tnOthOdukRawCountStatsTxEntry = _TnOthOdukRawCountStatsTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 54, 1)
)
tnOthOdukRawCountStatsTxEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsTxEntry.setStatus("current")
_TnOthOdukRawCountStatsTxClear_Type = TnCommand
_TnOthOdukRawCountStatsTxClear_Object = MibTableColumn
tnOthOdukRawCountStatsTxClear = _TnOthOdukRawCountStatsTxClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 54, 1, 1),
    _TnOthOdukRawCountStatsTxClear_Type()
)
tnOthOdukRawCountStatsTxClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsTxClear.setStatus("current")
_TnOthOdukRawCountStatsTxStartTime_Type = DateAndTime
_TnOthOdukRawCountStatsTxStartTime_Object = MibTableColumn
tnOthOdukRawCountStatsTxStartTime = _TnOthOdukRawCountStatsTxStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 54, 1, 2),
    _TnOthOdukRawCountStatsTxStartTime_Type()
)
tnOthOdukRawCountStatsTxStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsTxStartTime.setStatus("current")
_TnOthOdukRawCountStatTxNeBIP8ErrCnt_Type = Counter64
_TnOthOdukRawCountStatTxNeBIP8ErrCnt_Object = MibTableColumn
tnOthOdukRawCountStatTxNeBIP8ErrCnt = _TnOthOdukRawCountStatTxNeBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 54, 1, 3),
    _TnOthOdukRawCountStatTxNeBIP8ErrCnt_Type()
)
tnOthOdukRawCountStatTxNeBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatTxNeBIP8ErrCnt.setStatus("current")
_TnOthOdukRawCountStatTxNeES_Type = Counter64
_TnOthOdukRawCountStatTxNeES_Object = MibTableColumn
tnOthOdukRawCountStatTxNeES = _TnOthOdukRawCountStatTxNeES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 54, 1, 4),
    _TnOthOdukRawCountStatTxNeES_Type()
)
tnOthOdukRawCountStatTxNeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatTxNeES.setStatus("current")
_TnOthOdukRawCountStatTxNeSES_Type = Counter64
_TnOthOdukRawCountStatTxNeSES_Object = MibTableColumn
tnOthOdukRawCountStatTxNeSES = _TnOthOdukRawCountStatTxNeSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 54, 1, 5),
    _TnOthOdukRawCountStatTxNeSES_Type()
)
tnOthOdukRawCountStatTxNeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatTxNeSES.setStatus("current")
_TnOthOdukRawCountStatTxNeUAS_Type = Counter64
_TnOthOdukRawCountStatTxNeUAS_Object = MibTableColumn
tnOthOdukRawCountStatTxNeUAS = _TnOthOdukRawCountStatTxNeUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 54, 1, 6),
    _TnOthOdukRawCountStatTxNeUAS_Type()
)
tnOthOdukRawCountStatTxNeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatTxNeUAS.setStatus("current")
_TnOthOdukRawCountStatTxFeBIP8ErrCnt_Type = Counter64
_TnOthOdukRawCountStatTxFeBIP8ErrCnt_Object = MibTableColumn
tnOthOdukRawCountStatTxFeBIP8ErrCnt = _TnOthOdukRawCountStatTxFeBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 54, 1, 7),
    _TnOthOdukRawCountStatTxFeBIP8ErrCnt_Type()
)
tnOthOdukRawCountStatTxFeBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatTxFeBIP8ErrCnt.setStatus("current")
_TnOthOdukRawCountStatTxFeES_Type = Counter64
_TnOthOdukRawCountStatTxFeES_Object = MibTableColumn
tnOthOdukRawCountStatTxFeES = _TnOthOdukRawCountStatTxFeES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 54, 1, 8),
    _TnOthOdukRawCountStatTxFeES_Type()
)
tnOthOdukRawCountStatTxFeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatTxFeES.setStatus("current")
_TnOthOdukRawCountStatTxFeSES_Type = Counter64
_TnOthOdukRawCountStatTxFeSES_Object = MibTableColumn
tnOthOdukRawCountStatTxFeSES = _TnOthOdukRawCountStatTxFeSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 54, 1, 9),
    _TnOthOdukRawCountStatTxFeSES_Type()
)
tnOthOdukRawCountStatTxFeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatTxFeSES.setStatus("current")
_TnOthOdukRawCountStatTxFeUAS_Type = Counter64
_TnOthOdukRawCountStatTxFeUAS_Object = MibTableColumn
tnOthOdukRawCountStatTxFeUAS = _TnOthOdukRawCountStatTxFeUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 54, 1, 10),
    _TnOthOdukRawCountStatTxFeUAS_Type()
)
tnOthOdukRawCountStatTxFeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatTxFeUAS.setStatus("current")
_TnOthOtukRawCountStatsTotalMembers_Type = Integer32
_TnOthOtukRawCountStatsTotalMembers_Object = MibScalar
tnOthOtukRawCountStatsTotalMembers = _TnOthOtukRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 55),
    _TnOthOtukRawCountStatsTotalMembers_Type()
)
tnOthOtukRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatsTotalMembers.setStatus("current")
_TnOthOtukRawCountStatsTable_Object = MibTable
tnOthOtukRawCountStatsTable = _TnOthOtukRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 56)
)
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatsTable.setStatus("current")
_TnOthOtukRawCountStatsEntry_Object = MibTableRow
tnOthOtukRawCountStatsEntry = _TnOthOtukRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 56, 1)
)
tnOthOtukRawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatsEntry.setStatus("current")
_TnOthOtukRawCountStatsClear_Type = TnCommand
_TnOthOtukRawCountStatsClear_Object = MibTableColumn
tnOthOtukRawCountStatsClear = _TnOthOtukRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 56, 1, 1),
    _TnOthOtukRawCountStatsClear_Type()
)
tnOthOtukRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatsClear.setStatus("current")
_TnOthOtukRawCountStatsStartTime_Type = DateAndTime
_TnOthOtukRawCountStatsStartTime_Object = MibTableColumn
tnOthOtukRawCountStatsStartTime = _TnOthOtukRawCountStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 56, 1, 2),
    _TnOthOtukRawCountStatsStartTime_Type()
)
tnOthOtukRawCountStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatsStartTime.setStatus("current")
_TnOthOtukRawCountStatRxRsCorrCnt_Type = Counter64
_TnOthOtukRawCountStatRxRsCorrCnt_Object = MibTableColumn
tnOthOtukRawCountStatRxRsCorrCnt = _TnOthOtukRawCountStatRxRsCorrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 56, 1, 3),
    _TnOthOtukRawCountStatRxRsCorrCnt_Type()
)
tnOthOtukRawCountStatRxRsCorrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatRxRsCorrCnt.setStatus("current")
_TnOthOtukRawCountStatRxRsUncorrCnt_Type = Counter64
_TnOthOtukRawCountStatRxRsUncorrCnt_Object = MibTableColumn
tnOthOtukRawCountStatRxRsUncorrCnt = _TnOthOtukRawCountStatRxRsUncorrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 56, 1, 4),
    _TnOthOtukRawCountStatRxRsUncorrCnt_Type()
)
tnOthOtukRawCountStatRxRsUncorrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatRxRsUncorrCnt.setStatus("current")
_TnOthOtukRawCountStatRxBERPreFEC_Type = Counter64
_TnOthOtukRawCountStatRxBERPreFEC_Object = MibTableColumn
tnOthOtukRawCountStatRxBERPreFEC = _TnOthOtukRawCountStatRxBERPreFEC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 56, 1, 5),
    _TnOthOtukRawCountStatRxBERPreFEC_Type()
)
tnOthOtukRawCountStatRxBERPreFEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatRxBERPreFEC.setStatus("current")
_TnOthOtukRawCountStatRxBERPostFEC_Type = Counter64
_TnOthOtukRawCountStatRxBERPostFEC_Object = MibTableColumn
tnOthOtukRawCountStatRxBERPostFEC = _TnOthOtukRawCountStatRxBERPostFEC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 56, 1, 6),
    _TnOthOtukRawCountStatRxBERPostFEC_Type()
)
tnOthOtukRawCountStatRxBERPostFEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatRxBERPostFEC.setStatus("current")
_TnOthOtukRawCountStatRxNeSMBIP8ErrCnt_Type = Counter64
_TnOthOtukRawCountStatRxNeSMBIP8ErrCnt_Object = MibTableColumn
tnOthOtukRawCountStatRxNeSMBIP8ErrCnt = _TnOthOtukRawCountStatRxNeSMBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 56, 1, 7),
    _TnOthOtukRawCountStatRxNeSMBIP8ErrCnt_Type()
)
tnOthOtukRawCountStatRxNeSMBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatRxNeSMBIP8ErrCnt.setStatus("current")
_TnOthOtukRawCountStatRxNeSMES_Type = Counter64
_TnOthOtukRawCountStatRxNeSMES_Object = MibTableColumn
tnOthOtukRawCountStatRxNeSMES = _TnOthOtukRawCountStatRxNeSMES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 56, 1, 8),
    _TnOthOtukRawCountStatRxNeSMES_Type()
)
tnOthOtukRawCountStatRxNeSMES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatRxNeSMES.setStatus("current")
_TnOthOtukRawCountStatRxNeSMSES_Type = Counter64
_TnOthOtukRawCountStatRxNeSMSES_Object = MibTableColumn
tnOthOtukRawCountStatRxNeSMSES = _TnOthOtukRawCountStatRxNeSMSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 56, 1, 9),
    _TnOthOtukRawCountStatRxNeSMSES_Type()
)
tnOthOtukRawCountStatRxNeSMSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatRxNeSMSES.setStatus("current")
_TnOthOtukRawCountStatRxNeSMUAS_Type = Counter64
_TnOthOtukRawCountStatRxNeSMUAS_Object = MibTableColumn
tnOthOtukRawCountStatRxNeSMUAS = _TnOthOtukRawCountStatRxNeSMUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 56, 1, 10),
    _TnOthOtukRawCountStatRxNeSMUAS_Type()
)
tnOthOtukRawCountStatRxNeSMUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatRxNeSMUAS.setStatus("current")
_TnOthOtukRawCountStatRxNeIAES_Type = Counter64
_TnOthOtukRawCountStatRxNeIAES_Object = MibTableColumn
tnOthOtukRawCountStatRxNeIAES = _TnOthOtukRawCountStatRxNeIAES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 56, 1, 11),
    _TnOthOtukRawCountStatRxNeIAES_Type()
)
tnOthOtukRawCountStatRxNeIAES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatRxNeIAES.setStatus("current")
_TnOthOtukRawCountStatRxFeSMBIP8ErrCnt_Type = Counter64
_TnOthOtukRawCountStatRxFeSMBIP8ErrCnt_Object = MibTableColumn
tnOthOtukRawCountStatRxFeSMBIP8ErrCnt = _TnOthOtukRawCountStatRxFeSMBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 56, 1, 12),
    _TnOthOtukRawCountStatRxFeSMBIP8ErrCnt_Type()
)
tnOthOtukRawCountStatRxFeSMBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatRxFeSMBIP8ErrCnt.setStatus("current")
_TnOthOtukRawCountStatRxFeSMES_Type = Counter64
_TnOthOtukRawCountStatRxFeSMES_Object = MibTableColumn
tnOthOtukRawCountStatRxFeSMES = _TnOthOtukRawCountStatRxFeSMES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 56, 1, 13),
    _TnOthOtukRawCountStatRxFeSMES_Type()
)
tnOthOtukRawCountStatRxFeSMES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatRxFeSMES.setStatus("current")
_TnOthOtukRawCountStatRxFeSMSES_Type = Counter64
_TnOthOtukRawCountStatRxFeSMSES_Object = MibTableColumn
tnOthOtukRawCountStatRxFeSMSES = _TnOthOtukRawCountStatRxFeSMSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 56, 1, 14),
    _TnOthOtukRawCountStatRxFeSMSES_Type()
)
tnOthOtukRawCountStatRxFeSMSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatRxFeSMSES.setStatus("current")
_TnOthOtukRawCountStatRxFeSMUAS_Type = Counter64
_TnOthOtukRawCountStatRxFeSMUAS_Object = MibTableColumn
tnOthOtukRawCountStatRxFeSMUAS = _TnOthOtukRawCountStatRxFeSMUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 56, 1, 15),
    _TnOthOtukRawCountStatRxFeSMUAS_Type()
)
tnOthOtukRawCountStatRxFeSMUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatRxFeSMUAS.setStatus("current")
_TnOthOtukRawCountStatRxFeIAES_Type = Counter64
_TnOthOtukRawCountStatRxFeIAES_Object = MibTableColumn
tnOthOtukRawCountStatRxFeIAES = _TnOthOtukRawCountStatRxFeIAES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 56, 1, 16),
    _TnOthOtukRawCountStatRxFeIAES_Type()
)
tnOthOtukRawCountStatRxFeIAES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatRxFeIAES.setStatus("current")
_TnOthOtukRawCountStatRxNeBIAES_Type = Counter64
_TnOthOtukRawCountStatRxNeBIAES_Object = MibTableColumn
tnOthOtukRawCountStatRxNeBIAES = _TnOthOtukRawCountStatRxNeBIAES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 56, 1, 17),
    _TnOthOtukRawCountStatRxNeBIAES_Type()
)
tnOthOtukRawCountStatRxNeBIAES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatRxNeBIAES.setStatus("current")
_TnOsnrRawCountStatsTotalMembers_Type = Integer32
_TnOsnrRawCountStatsTotalMembers_Object = MibScalar
tnOsnrRawCountStatsTotalMembers = _TnOsnrRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 57),
    _TnOsnrRawCountStatsTotalMembers_Type()
)
tnOsnrRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOsnrRawCountStatsTotalMembers.setStatus("current")
_TnOsnrRawCountStatsTable_Object = MibTable
tnOsnrRawCountStatsTable = _TnOsnrRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 58)
)
if mibBuilder.loadTexts:
    tnOsnrRawCountStatsTable.setStatus("current")
_TnOsnrRawCountStatsEntry_Object = MibTableRow
tnOsnrRawCountStatsEntry = _TnOsnrRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 58, 1)
)
tnOsnrRawCountStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnOpticalStatsITUChannel"),
)
if mibBuilder.loadTexts:
    tnOsnrRawCountStatsEntry.setStatus("current")
_TnOsnrRawCountStatsClear_Type = TnCommand
_TnOsnrRawCountStatsClear_Object = MibTableColumn
tnOsnrRawCountStatsClear = _TnOsnrRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 58, 1, 1),
    _TnOsnrRawCountStatsClear_Type()
)
tnOsnrRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOsnrRawCountStatsClear.setStatus("current")
_TnOsnrRawCountStatStartTime_Type = DateAndTime
_TnOsnrRawCountStatStartTime_Object = MibTableColumn
tnOsnrRawCountStatStartTime = _TnOsnrRawCountStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 58, 1, 2),
    _TnOsnrRawCountStatStartTime_Type()
)
tnOsnrRawCountStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOsnrRawCountStatStartTime.setStatus("current")
_TnOsnrRawCountStatMinOSNR_Type = Integer32
_TnOsnrRawCountStatMinOSNR_Object = MibTableColumn
tnOsnrRawCountStatMinOSNR = _TnOsnrRawCountStatMinOSNR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 58, 1, 3),
    _TnOsnrRawCountStatMinOSNR_Type()
)
tnOsnrRawCountStatMinOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOsnrRawCountStatMinOSNR.setStatus("current")
if mibBuilder.loadTexts:
    tnOsnrRawCountStatMinOSNR.setUnits("mB")
_TnOsnrRawCountStatMaxOSNR_Type = Integer32
_TnOsnrRawCountStatMaxOSNR_Object = MibTableColumn
tnOsnrRawCountStatMaxOSNR = _TnOsnrRawCountStatMaxOSNR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 58, 1, 4),
    _TnOsnrRawCountStatMaxOSNR_Type()
)
tnOsnrRawCountStatMaxOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOsnrRawCountStatMaxOSNR.setStatus("current")
if mibBuilder.loadTexts:
    tnOsnrRawCountStatMaxOSNR.setUnits("mB")
_TnOsnrRawCountStatAverageOSNR_Type = Integer32
_TnOsnrRawCountStatAverageOSNR_Object = MibTableColumn
tnOsnrRawCountStatAverageOSNR = _TnOsnrRawCountStatAverageOSNR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 58, 1, 5),
    _TnOsnrRawCountStatAverageOSNR_Type()
)
tnOsnrRawCountStatAverageOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOsnrRawCountStatAverageOSNR.setStatus("current")
if mibBuilder.loadTexts:
    tnOsnrRawCountStatAverageOSNR.setUnits("mB")
_TnOthOdukRawCountStatsDMTotalMembers_Type = Integer32
_TnOthOdukRawCountStatsDMTotalMembers_Object = MibScalar
tnOthOdukRawCountStatsDMTotalMembers = _TnOthOdukRawCountStatsDMTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 59),
    _TnOthOdukRawCountStatsDMTotalMembers_Type()
)
tnOthOdukRawCountStatsDMTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsDMTotalMembers.setStatus("current")
_TnOthOdukRawCountStatsDMTable_Object = MibTable
tnOthOdukRawCountStatsDMTable = _TnOthOdukRawCountStatsDMTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 60)
)
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsDMTable.setStatus("current")
_TnOthOdukRawCountStatsDMEntry_Object = MibTableRow
tnOthOdukRawCountStatsDMEntry = _TnOthOdukRawCountStatsDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 60, 1)
)
tnOthOdukRawCountStatsDMEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsDMEntry.setStatus("current")
_TnOthOdukRawCountStatsDMClear_Type = TnCommand
_TnOthOdukRawCountStatsDMClear_Object = MibTableColumn
tnOthOdukRawCountStatsDMClear = _TnOthOdukRawCountStatsDMClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 60, 1, 1),
    _TnOthOdukRawCountStatsDMClear_Type()
)
tnOthOdukRawCountStatsDMClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsDMClear.setStatus("current")
_TnOthOdukRawCountStatsDMStartTime_Type = DateAndTime
_TnOthOdukRawCountStatsDMStartTime_Object = MibTableColumn
tnOthOdukRawCountStatsDMStartTime = _TnOthOdukRawCountStatsDMStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 60, 1, 2),
    _TnOthOdukRawCountStatsDMStartTime_Type()
)
tnOthOdukRawCountStatsDMStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsDMStartTime.setStatus("current")
_TnOthOdukRawCountStatsDMMinDm_Type = Integer32
_TnOthOdukRawCountStatsDMMinDm_Object = MibTableColumn
tnOthOdukRawCountStatsDMMinDm = _TnOthOdukRawCountStatsDMMinDm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 60, 1, 3),
    _TnOthOdukRawCountStatsDMMinDm_Type()
)
tnOthOdukRawCountStatsDMMinDm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsDMMinDm.setStatus("current")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsDMMinDm.setUnits("us")
_TnOthOdukRawCountStatsDMMaxDm_Type = Integer32
_TnOthOdukRawCountStatsDMMaxDm_Object = MibTableColumn
tnOthOdukRawCountStatsDMMaxDm = _TnOthOdukRawCountStatsDMMaxDm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 60, 1, 4),
    _TnOthOdukRawCountStatsDMMaxDm_Type()
)
tnOthOdukRawCountStatsDMMaxDm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsDMMaxDm.setStatus("current")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsDMMaxDm.setUnits("us")
_TnOthOdukRawCountStatsDMAverageDm_Type = Integer32
_TnOthOdukRawCountStatsDMAverageDm_Object = MibTableColumn
tnOthOdukRawCountStatsDMAverageDm = _TnOthOdukRawCountStatsDMAverageDm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 60, 1, 5),
    _TnOthOdukRawCountStatsDMAverageDm_Type()
)
tnOthOdukRawCountStatsDMAverageDm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsDMAverageDm.setStatus("current")
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsDMAverageDm.setUnits("us")
_TnOthOdukTcmRawCountStatsTotalMembers_Type = Integer32
_TnOthOdukTcmRawCountStatsTotalMembers_Object = MibScalar
tnOthOdukTcmRawCountStatsTotalMembers = _TnOthOdukTcmRawCountStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 61),
    _TnOthOdukTcmRawCountStatsTotalMembers_Type()
)
tnOthOdukTcmRawCountStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTcmRawCountStatsTotalMembers.setStatus("current")
_TnOthOdukTcmRawCountStatsTable_Object = MibTable
tnOthOdukTcmRawCountStatsTable = _TnOthOdukTcmRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 62)
)
if mibBuilder.loadTexts:
    tnOthOdukTcmRawCountStatsTable.setStatus("current")
_TnOthOdukTcmRawCountStatsEntry_Object = MibTableRow
tnOthOdukTcmRawCountStatsEntry = _TnOthOdukTcmRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 62, 1)
)
tnOthOdukTcmRawCountStatsEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthOdukTcmIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthOdukTcmIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnOthOdukTcmRawCountStatsEntry.setStatus("current")
_TnOthOdukTcmRawCountStatsClear_Type = TnCommand
_TnOthOdukTcmRawCountStatsClear_Object = MibTableColumn
tnOthOdukTcmRawCountStatsClear = _TnOthOdukTcmRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 62, 1, 1),
    _TnOthOdukTcmRawCountStatsClear_Type()
)
tnOthOdukTcmRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTcmRawCountStatsClear.setStatus("current")
_TnOthOdukTcmRawCountStatsNeRxBIP8ErrCnt_Type = Counter64
_TnOthOdukTcmRawCountStatsNeRxBIP8ErrCnt_Object = MibTableColumn
tnOthOdukTcmRawCountStatsNeRxBIP8ErrCnt = _TnOthOdukTcmRawCountStatsNeRxBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 62, 1, 2),
    _TnOthOdukTcmRawCountStatsNeRxBIP8ErrCnt_Type()
)
tnOthOdukTcmRawCountStatsNeRxBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTcmRawCountStatsNeRxBIP8ErrCnt.setStatus("current")
_TnOthOdukTcmRawCountStatsNeRxIAESErrCnt_Type = Counter64
_TnOthOdukTcmRawCountStatsNeRxIAESErrCnt_Object = MibTableColumn
tnOthOdukTcmRawCountStatsNeRxIAESErrCnt = _TnOthOdukTcmRawCountStatsNeRxIAESErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 62, 1, 3),
    _TnOthOdukTcmRawCountStatsNeRxIAESErrCnt_Type()
)
tnOthOdukTcmRawCountStatsNeRxIAESErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTcmRawCountStatsNeRxIAESErrCnt.setStatus("current")
_TnOthOdukTcmRawCountStatsNeRxES_Type = Counter64
_TnOthOdukTcmRawCountStatsNeRxES_Object = MibTableColumn
tnOthOdukTcmRawCountStatsNeRxES = _TnOthOdukTcmRawCountStatsNeRxES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 62, 1, 4),
    _TnOthOdukTcmRawCountStatsNeRxES_Type()
)
tnOthOdukTcmRawCountStatsNeRxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTcmRawCountStatsNeRxES.setStatus("current")
_TnOthOdukTcmRawCountStatsNeRxSES_Type = Counter64
_TnOthOdukTcmRawCountStatsNeRxSES_Object = MibTableColumn
tnOthOdukTcmRawCountStatsNeRxSES = _TnOthOdukTcmRawCountStatsNeRxSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 62, 1, 5),
    _TnOthOdukTcmRawCountStatsNeRxSES_Type()
)
tnOthOdukTcmRawCountStatsNeRxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTcmRawCountStatsNeRxSES.setStatus("current")
_TnOthOdukTcmRawCountStatsNeRxUAS_Type = Counter64
_TnOthOdukTcmRawCountStatsNeRxUAS_Object = MibTableColumn
tnOthOdukTcmRawCountStatsNeRxUAS = _TnOthOdukTcmRawCountStatsNeRxUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 62, 1, 6),
    _TnOthOdukTcmRawCountStatsNeRxUAS_Type()
)
tnOthOdukTcmRawCountStatsNeRxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTcmRawCountStatsNeRxUAS.setStatus("current")
_TnOthOdukTcmRawCountStatsFeRxBIP8ErrCnt_Type = Counter64
_TnOthOdukTcmRawCountStatsFeRxBIP8ErrCnt_Object = MibTableColumn
tnOthOdukTcmRawCountStatsFeRxBIP8ErrCnt = _TnOthOdukTcmRawCountStatsFeRxBIP8ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 62, 1, 7),
    _TnOthOdukTcmRawCountStatsFeRxBIP8ErrCnt_Type()
)
tnOthOdukTcmRawCountStatsFeRxBIP8ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTcmRawCountStatsFeRxBIP8ErrCnt.setStatus("current")
_TnOthOdukTcmRawCountStatsFeRxBIAESErrCnt_Type = Counter64
_TnOthOdukTcmRawCountStatsFeRxBIAESErrCnt_Object = MibTableColumn
tnOthOdukTcmRawCountStatsFeRxBIAESErrCnt = _TnOthOdukTcmRawCountStatsFeRxBIAESErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 62, 1, 8),
    _TnOthOdukTcmRawCountStatsFeRxBIAESErrCnt_Type()
)
tnOthOdukTcmRawCountStatsFeRxBIAESErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTcmRawCountStatsFeRxBIAESErrCnt.setStatus("current")
_TnOthOdukTcmRawCountStatsFeRxES_Type = Counter64
_TnOthOdukTcmRawCountStatsFeRxES_Object = MibTableColumn
tnOthOdukTcmRawCountStatsFeRxES = _TnOthOdukTcmRawCountStatsFeRxES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 62, 1, 9),
    _TnOthOdukTcmRawCountStatsFeRxES_Type()
)
tnOthOdukTcmRawCountStatsFeRxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTcmRawCountStatsFeRxES.setStatus("current")
_TnOthOdukTcmRawCountStatsFeRxSES_Type = Counter64
_TnOthOdukTcmRawCountStatsFeRxSES_Object = MibTableColumn
tnOthOdukTcmRawCountStatsFeRxSES = _TnOthOdukTcmRawCountStatsFeRxSES_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 62, 1, 10),
    _TnOthOdukTcmRawCountStatsFeRxSES_Type()
)
tnOthOdukTcmRawCountStatsFeRxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTcmRawCountStatsFeRxSES.setStatus("current")
_TnOthOdukTcmRawCountStatsFeRxUAS_Type = Counter64
_TnOthOdukTcmRawCountStatsFeRxUAS_Object = MibTableColumn
tnOthOdukTcmRawCountStatsFeRxUAS = _TnOthOdukTcmRawCountStatsFeRxUAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 62, 1, 11),
    _TnOthOdukTcmRawCountStatsFeRxUAS_Type()
)
tnOthOdukTcmRawCountStatsFeRxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTcmRawCountStatsFeRxUAS.setStatus("current")
_TnOthOdukTcmRawCountStatsStartTime_Type = DateAndTime
_TnOthOdukTcmRawCountStatsStartTime_Object = MibTableColumn
tnOthOdukTcmRawCountStatsStartTime = _TnOthOdukTcmRawCountStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 3, 62, 1, 12),
    _TnOthOdukTcmRawCountStatsStartTime_Type()
)
tnOthOdukTcmRawCountStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTcmRawCountStatsStartTime.setStatus("current")
_TnStatisticsBaseline_ObjectIdentity = ObjectIdentity
tnStatisticsBaseline = _TnStatisticsBaseline_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 4)
)
_TnStatsBaselineTable_Object = MibTable
tnStatsBaselineTable = _TnStatsBaselineTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tnStatsBaselineTable.setStatus("current")
_TnStatsBaselineEntry_Object = MibTableRow
tnStatsBaselineEntry = _TnStatsBaselineEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 4, 1, 1)
)
tnStatsBaselineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsGroupId"),
)
if mibBuilder.loadTexts:
    tnStatsBaselineEntry.setStatus("current")


class _TnStatsBaselineReason_Type(Integer32):
    """Custom type tnStatsBaselineReason based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("zero", 1),
          ("one", 2),
          ("two", 3),
          ("three", 4),
          ("four", 5),
          ("five", 6),
          ("six", 7),
          ("seven", 8),
          ("eight", 9),
          ("nine", 10),
          ("losClrd", 11),
          ("laserOn", 12),
          ("newSystem", 13),
          ("otReplaced", 14))
    )


_TnStatsBaselineReason_Type.__name__ = "Integer32"
_TnStatsBaselineReason_Object = MibTableColumn
tnStatsBaselineReason = _TnStatsBaselineReason_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 4, 1, 1, 1),
    _TnStatsBaselineReason_Type()
)
tnStatsBaselineReason.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnStatsBaselineReason.setStatus("current")
_TnStatsBaselineValue_Type = Integer32
_TnStatsBaselineValue_Object = MibTableColumn
tnStatsBaselineValue = _TnStatsBaselineValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 4, 1, 1, 2),
    _TnStatsBaselineValue_Type()
)
tnStatsBaselineValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsBaselineValue.setStatus("current")
if mibBuilder.loadTexts:
    tnStatsBaselineValue.setUnits("mBm")
_TnStatsBaselineTime_Type = DateAndTime
_TnStatsBaselineTime_Object = MibTableColumn
tnStatsBaselineTime = _TnStatsBaselineTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 4, 1, 1, 3),
    _TnStatsBaselineTime_Type()
)
tnStatsBaselineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsBaselineTime.setStatus("current")
_TnStatisticsOdukRxScalars_ObjectIdentity = ObjectIdentity
tnStatisticsOdukRxScalars = _TnStatisticsOdukRxScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5)
)
_TnOthOdu0StatRxNeBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu0StatRxNeBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu0StatRxNeBIP8ErrCnt15MinTr = _TnOthOdu0StatRxNeBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 1),
    _TnOthOdu0StatRxNeBIP8ErrCnt15MinTr_Type()
)
tnOthOdu0StatRxNeBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu0StatRxNeBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu0StatRxNeBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu0StatRxNeBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu0StatRxNeBIP8ErrCnt15MinRtr = _TnOthOdu0StatRxNeBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 2),
    _TnOthOdu0StatRxNeBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu0StatRxNeBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu0StatRxNeBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu0StatRxNeBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu0StatRxNeBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu0StatRxNeBIP8ErrCnt1DayTr = _TnOthOdu0StatRxNeBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 3),
    _TnOthOdu0StatRxNeBIP8ErrCnt1DayTr_Type()
)
tnOthOdu0StatRxNeBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu0StatRxNeBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu0StatRxFeBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu0StatRxFeBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu0StatRxFeBIP8ErrCnt15MinTr = _TnOthOdu0StatRxFeBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 4),
    _TnOthOdu0StatRxFeBIP8ErrCnt15MinTr_Type()
)
tnOthOdu0StatRxFeBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu0StatRxFeBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu0StatRxFeBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu0StatRxFeBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu0StatRxFeBIP8ErrCnt15MinRtr = _TnOthOdu0StatRxFeBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 5),
    _TnOthOdu0StatRxFeBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu0StatRxFeBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu0StatRxFeBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu0StatRxFeBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu0StatRxFeBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu0StatRxFeBIP8ErrCnt1DayTr = _TnOthOdu0StatRxFeBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 6),
    _TnOthOdu0StatRxFeBIP8ErrCnt1DayTr_Type()
)
tnOthOdu0StatRxFeBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu0StatRxFeBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu1StatRxNeBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu1StatRxNeBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu1StatRxNeBIP8ErrCnt15MinTr = _TnOthOdu1StatRxNeBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 7),
    _TnOthOdu1StatRxNeBIP8ErrCnt15MinTr_Type()
)
tnOthOdu1StatRxNeBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu1StatRxNeBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu1StatRxNeBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu1StatRxNeBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu1StatRxNeBIP8ErrCnt15MinRtr = _TnOthOdu1StatRxNeBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 8),
    _TnOthOdu1StatRxNeBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu1StatRxNeBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu1StatRxNeBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu1StatRxNeBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu1StatRxNeBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu1StatRxNeBIP8ErrCnt1DayTr = _TnOthOdu1StatRxNeBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 9),
    _TnOthOdu1StatRxNeBIP8ErrCnt1DayTr_Type()
)
tnOthOdu1StatRxNeBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu1StatRxNeBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu1StatRxFeBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu1StatRxFeBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu1StatRxFeBIP8ErrCnt15MinTr = _TnOthOdu1StatRxFeBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 10),
    _TnOthOdu1StatRxFeBIP8ErrCnt15MinTr_Type()
)
tnOthOdu1StatRxFeBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu1StatRxFeBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu1StatRxFeBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu1StatRxFeBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu1StatRxFeBIP8ErrCnt15MinRtr = _TnOthOdu1StatRxFeBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 11),
    _TnOthOdu1StatRxFeBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu1StatRxFeBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu1StatRxFeBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu1StatRxFeBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu1StatRxFeBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu1StatRxFeBIP8ErrCnt1DayTr = _TnOthOdu1StatRxFeBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 12),
    _TnOthOdu1StatRxFeBIP8ErrCnt1DayTr_Type()
)
tnOthOdu1StatRxFeBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu1StatRxFeBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu2StatRxNeBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu2StatRxNeBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu2StatRxNeBIP8ErrCnt15MinTr = _TnOthOdu2StatRxNeBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 13),
    _TnOthOdu2StatRxNeBIP8ErrCnt15MinTr_Type()
)
tnOthOdu2StatRxNeBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu2StatRxNeBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu2StatRxNeBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu2StatRxNeBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu2StatRxNeBIP8ErrCnt15MinRtr = _TnOthOdu2StatRxNeBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 14),
    _TnOthOdu2StatRxNeBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu2StatRxNeBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu2StatRxNeBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu2StatRxNeBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu2StatRxNeBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu2StatRxNeBIP8ErrCnt1DayTr = _TnOthOdu2StatRxNeBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 15),
    _TnOthOdu2StatRxNeBIP8ErrCnt1DayTr_Type()
)
tnOthOdu2StatRxNeBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu2StatRxNeBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu2StatRxFeBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu2StatRxFeBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu2StatRxFeBIP8ErrCnt15MinTr = _TnOthOdu2StatRxFeBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 16),
    _TnOthOdu2StatRxFeBIP8ErrCnt15MinTr_Type()
)
tnOthOdu2StatRxFeBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu2StatRxFeBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu2StatRxFeBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu2StatRxFeBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu2StatRxFeBIP8ErrCnt15MinRtr = _TnOthOdu2StatRxFeBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 17),
    _TnOthOdu2StatRxFeBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu2StatRxFeBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu2StatRxFeBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu2StatRxFeBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu2StatRxFeBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu2StatRxFeBIP8ErrCnt1DayTr = _TnOthOdu2StatRxFeBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 18),
    _TnOthOdu2StatRxFeBIP8ErrCnt1DayTr_Type()
)
tnOthOdu2StatRxFeBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu2StatRxFeBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu3StatRxNeBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu3StatRxNeBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu3StatRxNeBIP8ErrCnt15MinTr = _TnOthOdu3StatRxNeBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 19),
    _TnOthOdu3StatRxNeBIP8ErrCnt15MinTr_Type()
)
tnOthOdu3StatRxNeBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu3StatRxNeBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu3StatRxNeBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu3StatRxNeBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu3StatRxNeBIP8ErrCnt15MinRtr = _TnOthOdu3StatRxNeBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 20),
    _TnOthOdu3StatRxNeBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu3StatRxNeBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu3StatRxNeBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu3StatRxNeBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu3StatRxNeBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu3StatRxNeBIP8ErrCnt1DayTr = _TnOthOdu3StatRxNeBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 21),
    _TnOthOdu3StatRxNeBIP8ErrCnt1DayTr_Type()
)
tnOthOdu3StatRxNeBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu3StatRxNeBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu3StatRxFeBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu3StatRxFeBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu3StatRxFeBIP8ErrCnt15MinTr = _TnOthOdu3StatRxFeBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 22),
    _TnOthOdu3StatRxFeBIP8ErrCnt15MinTr_Type()
)
tnOthOdu3StatRxFeBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu3StatRxFeBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu3StatRxFeBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu3StatRxFeBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu3StatRxFeBIP8ErrCnt15MinRtr = _TnOthOdu3StatRxFeBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 23),
    _TnOthOdu3StatRxFeBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu3StatRxFeBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu3StatRxFeBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu3StatRxFeBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu3StatRxFeBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu3StatRxFeBIP8ErrCnt1DayTr = _TnOthOdu3StatRxFeBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 24),
    _TnOthOdu3StatRxFeBIP8ErrCnt1DayTr_Type()
)
tnOthOdu3StatRxFeBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu3StatRxFeBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu4StatRxNeBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu4StatRxNeBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu4StatRxNeBIP8ErrCnt15MinTr = _TnOthOdu4StatRxNeBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 25),
    _TnOthOdu4StatRxNeBIP8ErrCnt15MinTr_Type()
)
tnOthOdu4StatRxNeBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu4StatRxNeBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu4StatRxNeBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu4StatRxNeBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu4StatRxNeBIP8ErrCnt15MinRtr = _TnOthOdu4StatRxNeBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 26),
    _TnOthOdu4StatRxNeBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu4StatRxNeBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu4StatRxNeBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu4StatRxNeBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu4StatRxNeBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu4StatRxNeBIP8ErrCnt1DayTr = _TnOthOdu4StatRxNeBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 27),
    _TnOthOdu4StatRxNeBIP8ErrCnt1DayTr_Type()
)
tnOthOdu4StatRxNeBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu4StatRxNeBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu4StatRxFeBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu4StatRxFeBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu4StatRxFeBIP8ErrCnt15MinTr = _TnOthOdu4StatRxFeBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 28),
    _TnOthOdu4StatRxFeBIP8ErrCnt15MinTr_Type()
)
tnOthOdu4StatRxFeBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu4StatRxFeBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu4StatRxFeBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu4StatRxFeBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu4StatRxFeBIP8ErrCnt15MinRtr = _TnOthOdu4StatRxFeBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 29),
    _TnOthOdu4StatRxFeBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu4StatRxFeBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu4StatRxFeBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu4StatRxFeBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu4StatRxFeBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu4StatRxFeBIP8ErrCnt1DayTr = _TnOthOdu4StatRxFeBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 30),
    _TnOthOdu4StatRxFeBIP8ErrCnt1DayTr_Type()
)
tnOthOdu4StatRxFeBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu4StatRxFeBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdukStatRxNeES15MinTr_Type = Counter64
_TnOthOdukStatRxNeES15MinTr_Object = MibScalar
tnOthOdukStatRxNeES15MinTr = _TnOthOdukStatRxNeES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 31),
    _TnOthOdukStatRxNeES15MinTr_Type()
)
tnOthOdukStatRxNeES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatRxNeES15MinTr.setStatus("current")
_TnOthOdukStatRxNeES15MinRtr_Type = Counter64
_TnOthOdukStatRxNeES15MinRtr_Object = MibScalar
tnOthOdukStatRxNeES15MinRtr = _TnOthOdukStatRxNeES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 32),
    _TnOthOdukStatRxNeES15MinRtr_Type()
)
tnOthOdukStatRxNeES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatRxNeES15MinRtr.setStatus("current")
_TnOthOdukStatRxNeES1DayTr_Type = Counter64
_TnOthOdukStatRxNeES1DayTr_Object = MibScalar
tnOthOdukStatRxNeES1DayTr = _TnOthOdukStatRxNeES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 33),
    _TnOthOdukStatRxNeES1DayTr_Type()
)
tnOthOdukStatRxNeES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatRxNeES1DayTr.setStatus("current")
_TnOthOdukStatRxFeES15MinTr_Type = Counter64
_TnOthOdukStatRxFeES15MinTr_Object = MibScalar
tnOthOdukStatRxFeES15MinTr = _TnOthOdukStatRxFeES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 34),
    _TnOthOdukStatRxFeES15MinTr_Type()
)
tnOthOdukStatRxFeES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatRxFeES15MinTr.setStatus("current")
_TnOthOdukStatRxFeES15MinRtr_Type = Counter64
_TnOthOdukStatRxFeES15MinRtr_Object = MibScalar
tnOthOdukStatRxFeES15MinRtr = _TnOthOdukStatRxFeES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 35),
    _TnOthOdukStatRxFeES15MinRtr_Type()
)
tnOthOdukStatRxFeES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatRxFeES15MinRtr.setStatus("current")
_TnOthOdukStatRxFeES1DayTr_Type = Counter64
_TnOthOdukStatRxFeES1DayTr_Object = MibScalar
tnOthOdukStatRxFeES1DayTr = _TnOthOdukStatRxFeES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 36),
    _TnOthOdukStatRxFeES1DayTr_Type()
)
tnOthOdukStatRxFeES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatRxFeES1DayTr.setStatus("current")
_TnOthOdukStatRxNeSES15MinTr_Type = Counter64
_TnOthOdukStatRxNeSES15MinTr_Object = MibScalar
tnOthOdukStatRxNeSES15MinTr = _TnOthOdukStatRxNeSES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 37),
    _TnOthOdukStatRxNeSES15MinTr_Type()
)
tnOthOdukStatRxNeSES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatRxNeSES15MinTr.setStatus("current")
_TnOthOdukStatRxNeSES15MinRtr_Type = Counter64
_TnOthOdukStatRxNeSES15MinRtr_Object = MibScalar
tnOthOdukStatRxNeSES15MinRtr = _TnOthOdukStatRxNeSES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 38),
    _TnOthOdukStatRxNeSES15MinRtr_Type()
)
tnOthOdukStatRxNeSES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatRxNeSES15MinRtr.setStatus("current")
_TnOthOdukStatRxNeSES1DayTr_Type = Counter64
_TnOthOdukStatRxNeSES1DayTr_Object = MibScalar
tnOthOdukStatRxNeSES1DayTr = _TnOthOdukStatRxNeSES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 39),
    _TnOthOdukStatRxNeSES1DayTr_Type()
)
tnOthOdukStatRxNeSES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatRxNeSES1DayTr.setStatus("current")
_TnOthOdukStatRxFeSES15MinTr_Type = Counter64
_TnOthOdukStatRxFeSES15MinTr_Object = MibScalar
tnOthOdukStatRxFeSES15MinTr = _TnOthOdukStatRxFeSES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 40),
    _TnOthOdukStatRxFeSES15MinTr_Type()
)
tnOthOdukStatRxFeSES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatRxFeSES15MinTr.setStatus("current")
_TnOthOdukStatRxFeSES15MinRtr_Type = Counter64
_TnOthOdukStatRxFeSES15MinRtr_Object = MibScalar
tnOthOdukStatRxFeSES15MinRtr = _TnOthOdukStatRxFeSES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 41),
    _TnOthOdukStatRxFeSES15MinRtr_Type()
)
tnOthOdukStatRxFeSES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatRxFeSES15MinRtr.setStatus("current")
_TnOthOdukStatRxFeSES1DayTr_Type = Counter64
_TnOthOdukStatRxFeSES1DayTr_Object = MibScalar
tnOthOdukStatRxFeSES1DayTr = _TnOthOdukStatRxFeSES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 42),
    _TnOthOdukStatRxFeSES1DayTr_Type()
)
tnOthOdukStatRxFeSES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatRxFeSES1DayTr.setStatus("current")
_TnOthOdukStatRxNeUAS15MinTr_Type = Counter64
_TnOthOdukStatRxNeUAS15MinTr_Object = MibScalar
tnOthOdukStatRxNeUAS15MinTr = _TnOthOdukStatRxNeUAS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 43),
    _TnOthOdukStatRxNeUAS15MinTr_Type()
)
tnOthOdukStatRxNeUAS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatRxNeUAS15MinTr.setStatus("current")
_TnOthOdukStatRxNeUAS15MinRtr_Type = Counter64
_TnOthOdukStatRxNeUAS15MinRtr_Object = MibScalar
tnOthOdukStatRxNeUAS15MinRtr = _TnOthOdukStatRxNeUAS15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 44),
    _TnOthOdukStatRxNeUAS15MinRtr_Type()
)
tnOthOdukStatRxNeUAS15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatRxNeUAS15MinRtr.setStatus("current")
_TnOthOdukStatRxNeUAS1DayTr_Type = Counter64
_TnOthOdukStatRxNeUAS1DayTr_Object = MibScalar
tnOthOdukStatRxNeUAS1DayTr = _TnOthOdukStatRxNeUAS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 45),
    _TnOthOdukStatRxNeUAS1DayTr_Type()
)
tnOthOdukStatRxNeUAS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatRxNeUAS1DayTr.setStatus("current")
_TnOthOdukStatRxFeUAS15MinTr_Type = Counter64
_TnOthOdukStatRxFeUAS15MinTr_Object = MibScalar
tnOthOdukStatRxFeUAS15MinTr = _TnOthOdukStatRxFeUAS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 46),
    _TnOthOdukStatRxFeUAS15MinTr_Type()
)
tnOthOdukStatRxFeUAS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatRxFeUAS15MinTr.setStatus("current")
_TnOthOdukStatRxFeUAS15MinRtr_Type = Counter64
_TnOthOdukStatRxFeUAS15MinRtr_Object = MibScalar
tnOthOdukStatRxFeUAS15MinRtr = _TnOthOdukStatRxFeUAS15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 47),
    _TnOthOdukStatRxFeUAS15MinRtr_Type()
)
tnOthOdukStatRxFeUAS15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatRxFeUAS15MinRtr.setStatus("current")
_TnOthOdukStatRxFeUAS1DayTr_Type = Counter64
_TnOthOdukStatRxFeUAS1DayTr_Object = MibScalar
tnOthOdukStatRxFeUAS1DayTr = _TnOthOdukStatRxFeUAS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 5, 48),
    _TnOthOdukStatRxFeUAS1DayTr_Type()
)
tnOthOdukStatRxFeUAS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatRxFeUAS1DayTr.setStatus("current")
_TnStatisticsOdukTxScalars_ObjectIdentity = ObjectIdentity
tnStatisticsOdukTxScalars = _TnStatisticsOdukTxScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6)
)
_TnOthOdu0StatTxNeBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu0StatTxNeBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu0StatTxNeBIP8ErrCnt15MinTr = _TnOthOdu0StatTxNeBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 1),
    _TnOthOdu0StatTxNeBIP8ErrCnt15MinTr_Type()
)
tnOthOdu0StatTxNeBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu0StatTxNeBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu0StatTxNeBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu0StatTxNeBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu0StatTxNeBIP8ErrCnt15MinRtr = _TnOthOdu0StatTxNeBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 2),
    _TnOthOdu0StatTxNeBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu0StatTxNeBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu0StatTxNeBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu0StatTxNeBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu0StatTxNeBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu0StatTxNeBIP8ErrCnt1DayTr = _TnOthOdu0StatTxNeBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 3),
    _TnOthOdu0StatTxNeBIP8ErrCnt1DayTr_Type()
)
tnOthOdu0StatTxNeBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu0StatTxNeBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu0StatTxFeBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu0StatTxFeBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu0StatTxFeBIP8ErrCnt15MinTr = _TnOthOdu0StatTxFeBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 4),
    _TnOthOdu0StatTxFeBIP8ErrCnt15MinTr_Type()
)
tnOthOdu0StatTxFeBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu0StatTxFeBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu0StatTxFeBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu0StatTxFeBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu0StatTxFeBIP8ErrCnt15MinRtr = _TnOthOdu0StatTxFeBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 5),
    _TnOthOdu0StatTxFeBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu0StatTxFeBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu0StatTxFeBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu0StatTxFeBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu0StatTxFeBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu0StatTxFeBIP8ErrCnt1DayTr = _TnOthOdu0StatTxFeBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 6),
    _TnOthOdu0StatTxFeBIP8ErrCnt1DayTr_Type()
)
tnOthOdu0StatTxFeBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu0StatTxFeBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu1StatTxNeBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu1StatTxNeBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu1StatTxNeBIP8ErrCnt15MinTr = _TnOthOdu1StatTxNeBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 7),
    _TnOthOdu1StatTxNeBIP8ErrCnt15MinTr_Type()
)
tnOthOdu1StatTxNeBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu1StatTxNeBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu1StatTxNeBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu1StatTxNeBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu1StatTxNeBIP8ErrCnt15MinRtr = _TnOthOdu1StatTxNeBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 8),
    _TnOthOdu1StatTxNeBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu1StatTxNeBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu1StatTxNeBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu1StatTxNeBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu1StatTxNeBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu1StatTxNeBIP8ErrCnt1DayTr = _TnOthOdu1StatTxNeBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 9),
    _TnOthOdu1StatTxNeBIP8ErrCnt1DayTr_Type()
)
tnOthOdu1StatTxNeBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu1StatTxNeBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu1StatTxFeBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu1StatTxFeBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu1StatTxFeBIP8ErrCnt15MinTr = _TnOthOdu1StatTxFeBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 10),
    _TnOthOdu1StatTxFeBIP8ErrCnt15MinTr_Type()
)
tnOthOdu1StatTxFeBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu1StatTxFeBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu1StatTxFeBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu1StatTxFeBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu1StatTxFeBIP8ErrCnt15MinRtr = _TnOthOdu1StatTxFeBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 11),
    _TnOthOdu1StatTxFeBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu1StatTxFeBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu1StatTxFeBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu1StatTxFeBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu1StatTxFeBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu1StatTxFeBIP8ErrCnt1DayTr = _TnOthOdu1StatTxFeBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 12),
    _TnOthOdu1StatTxFeBIP8ErrCnt1DayTr_Type()
)
tnOthOdu1StatTxFeBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu1StatTxFeBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu2StatTxNeBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu2StatTxNeBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu2StatTxNeBIP8ErrCnt15MinTr = _TnOthOdu2StatTxNeBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 13),
    _TnOthOdu2StatTxNeBIP8ErrCnt15MinTr_Type()
)
tnOthOdu2StatTxNeBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu2StatTxNeBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu2StatTxNeBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu2StatTxNeBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu2StatTxNeBIP8ErrCnt15MinRtr = _TnOthOdu2StatTxNeBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 14),
    _TnOthOdu2StatTxNeBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu2StatTxNeBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu2StatTxNeBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu2StatTxNeBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu2StatTxNeBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu2StatTxNeBIP8ErrCnt1DayTr = _TnOthOdu2StatTxNeBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 15),
    _TnOthOdu2StatTxNeBIP8ErrCnt1DayTr_Type()
)
tnOthOdu2StatTxNeBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu2StatTxNeBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu2StatTxFeBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu2StatTxFeBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu2StatTxFeBIP8ErrCnt15MinTr = _TnOthOdu2StatTxFeBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 16),
    _TnOthOdu2StatTxFeBIP8ErrCnt15MinTr_Type()
)
tnOthOdu2StatTxFeBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu2StatTxFeBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu2StatTxFeBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu2StatTxFeBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu2StatTxFeBIP8ErrCnt15MinRtr = _TnOthOdu2StatTxFeBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 17),
    _TnOthOdu2StatTxFeBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu2StatTxFeBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu2StatTxFeBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu2StatTxFeBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu2StatTxFeBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu2StatTxFeBIP8ErrCnt1DayTr = _TnOthOdu2StatTxFeBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 18),
    _TnOthOdu2StatTxFeBIP8ErrCnt1DayTr_Type()
)
tnOthOdu2StatTxFeBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu2StatTxFeBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu3StatTxNeBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu3StatTxNeBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu3StatTxNeBIP8ErrCnt15MinTr = _TnOthOdu3StatTxNeBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 19),
    _TnOthOdu3StatTxNeBIP8ErrCnt15MinTr_Type()
)
tnOthOdu3StatTxNeBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu3StatTxNeBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu3StatTxNeBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu3StatTxNeBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu3StatTxNeBIP8ErrCnt15MinRtr = _TnOthOdu3StatTxNeBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 20),
    _TnOthOdu3StatTxNeBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu3StatTxNeBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu3StatTxNeBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu3StatTxNeBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu3StatTxNeBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu3StatTxNeBIP8ErrCnt1DayTr = _TnOthOdu3StatTxNeBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 21),
    _TnOthOdu3StatTxNeBIP8ErrCnt1DayTr_Type()
)
tnOthOdu3StatTxNeBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu3StatTxNeBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu3StatTxFeBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu3StatTxFeBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu3StatTxFeBIP8ErrCnt15MinTr = _TnOthOdu3StatTxFeBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 22),
    _TnOthOdu3StatTxFeBIP8ErrCnt15MinTr_Type()
)
tnOthOdu3StatTxFeBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu3StatTxFeBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu3StatTxFeBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu3StatTxFeBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu3StatTxFeBIP8ErrCnt15MinRtr = _TnOthOdu3StatTxFeBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 23),
    _TnOthOdu3StatTxFeBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu3StatTxFeBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu3StatTxFeBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu3StatTxFeBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu3StatTxFeBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu3StatTxFeBIP8ErrCnt1DayTr = _TnOthOdu3StatTxFeBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 24),
    _TnOthOdu3StatTxFeBIP8ErrCnt1DayTr_Type()
)
tnOthOdu3StatTxFeBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu3StatTxFeBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu4StatTxNeBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu4StatTxNeBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu4StatTxNeBIP8ErrCnt15MinTr = _TnOthOdu4StatTxNeBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 25),
    _TnOthOdu4StatTxNeBIP8ErrCnt15MinTr_Type()
)
tnOthOdu4StatTxNeBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu4StatTxNeBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu4StatTxNeBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu4StatTxNeBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu4StatTxNeBIP8ErrCnt15MinRtr = _TnOthOdu4StatTxNeBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 26),
    _TnOthOdu4StatTxNeBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu4StatTxNeBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu4StatTxNeBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu4StatTxNeBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu4StatTxNeBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu4StatTxNeBIP8ErrCnt1DayTr = _TnOthOdu4StatTxNeBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 27),
    _TnOthOdu4StatTxNeBIP8ErrCnt1DayTr_Type()
)
tnOthOdu4StatTxNeBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu4StatTxNeBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu4StatTxFeBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu4StatTxFeBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu4StatTxFeBIP8ErrCnt15MinTr = _TnOthOdu4StatTxFeBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 28),
    _TnOthOdu4StatTxFeBIP8ErrCnt15MinTr_Type()
)
tnOthOdu4StatTxFeBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu4StatTxFeBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu4StatTxFeBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu4StatTxFeBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu4StatTxFeBIP8ErrCnt15MinRtr = _TnOthOdu4StatTxFeBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 29),
    _TnOthOdu4StatTxFeBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu4StatTxFeBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu4StatTxFeBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu4StatTxFeBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu4StatTxFeBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu4StatTxFeBIP8ErrCnt1DayTr = _TnOthOdu4StatTxFeBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 30),
    _TnOthOdu4StatTxFeBIP8ErrCnt1DayTr_Type()
)
tnOthOdu4StatTxFeBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu4StatTxFeBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdukStatTxNeES15MinTr_Type = Counter64
_TnOthOdukStatTxNeES15MinTr_Object = MibScalar
tnOthOdukStatTxNeES15MinTr = _TnOthOdukStatTxNeES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 31),
    _TnOthOdukStatTxNeES15MinTr_Type()
)
tnOthOdukStatTxNeES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatTxNeES15MinTr.setStatus("current")
_TnOthOdukStatTxNeES15MinRtr_Type = Counter64
_TnOthOdukStatTxNeES15MinRtr_Object = MibScalar
tnOthOdukStatTxNeES15MinRtr = _TnOthOdukStatTxNeES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 32),
    _TnOthOdukStatTxNeES15MinRtr_Type()
)
tnOthOdukStatTxNeES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatTxNeES15MinRtr.setStatus("current")
_TnOthOdukStatTxNeES1DayTr_Type = Counter64
_TnOthOdukStatTxNeES1DayTr_Object = MibScalar
tnOthOdukStatTxNeES1DayTr = _TnOthOdukStatTxNeES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 33),
    _TnOthOdukStatTxNeES1DayTr_Type()
)
tnOthOdukStatTxNeES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatTxNeES1DayTr.setStatus("current")
_TnOthOdukStatTxFeES15MinTr_Type = Counter64
_TnOthOdukStatTxFeES15MinTr_Object = MibScalar
tnOthOdukStatTxFeES15MinTr = _TnOthOdukStatTxFeES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 34),
    _TnOthOdukStatTxFeES15MinTr_Type()
)
tnOthOdukStatTxFeES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatTxFeES15MinTr.setStatus("current")
_TnOthOdukStatTxFeES15MinRtr_Type = Counter64
_TnOthOdukStatTxFeES15MinRtr_Object = MibScalar
tnOthOdukStatTxFeES15MinRtr = _TnOthOdukStatTxFeES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 35),
    _TnOthOdukStatTxFeES15MinRtr_Type()
)
tnOthOdukStatTxFeES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatTxFeES15MinRtr.setStatus("current")
_TnOthOdukStatTxFeES1DayTr_Type = Counter64
_TnOthOdukStatTxFeES1DayTr_Object = MibScalar
tnOthOdukStatTxFeES1DayTr = _TnOthOdukStatTxFeES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 36),
    _TnOthOdukStatTxFeES1DayTr_Type()
)
tnOthOdukStatTxFeES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatTxFeES1DayTr.setStatus("current")
_TnOthOdukStatTxNeSES15MinTr_Type = Counter64
_TnOthOdukStatTxNeSES15MinTr_Object = MibScalar
tnOthOdukStatTxNeSES15MinTr = _TnOthOdukStatTxNeSES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 37),
    _TnOthOdukStatTxNeSES15MinTr_Type()
)
tnOthOdukStatTxNeSES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatTxNeSES15MinTr.setStatus("current")
_TnOthOdukStatTxNeSES15MinRtr_Type = Counter64
_TnOthOdukStatTxNeSES15MinRtr_Object = MibScalar
tnOthOdukStatTxNeSES15MinRtr = _TnOthOdukStatTxNeSES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 38),
    _TnOthOdukStatTxNeSES15MinRtr_Type()
)
tnOthOdukStatTxNeSES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatTxNeSES15MinRtr.setStatus("current")
_TnOthOdukStatTxNeSES1DayTr_Type = Counter64
_TnOthOdukStatTxNeSES1DayTr_Object = MibScalar
tnOthOdukStatTxNeSES1DayTr = _TnOthOdukStatTxNeSES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 39),
    _TnOthOdukStatTxNeSES1DayTr_Type()
)
tnOthOdukStatTxNeSES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatTxNeSES1DayTr.setStatus("current")
_TnOthOdukStatTxFeSES15MinTr_Type = Counter64
_TnOthOdukStatTxFeSES15MinTr_Object = MibScalar
tnOthOdukStatTxFeSES15MinTr = _TnOthOdukStatTxFeSES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 40),
    _TnOthOdukStatTxFeSES15MinTr_Type()
)
tnOthOdukStatTxFeSES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatTxFeSES15MinTr.setStatus("current")
_TnOthOdukStatTxFeSES15MinRtr_Type = Counter64
_TnOthOdukStatTxFeSES15MinRtr_Object = MibScalar
tnOthOdukStatTxFeSES15MinRtr = _TnOthOdukStatTxFeSES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 41),
    _TnOthOdukStatTxFeSES15MinRtr_Type()
)
tnOthOdukStatTxFeSES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatTxFeSES15MinRtr.setStatus("current")
_TnOthOdukStatTxFeSES1DayTr_Type = Counter64
_TnOthOdukStatTxFeSES1DayTr_Object = MibScalar
tnOthOdukStatTxFeSES1DayTr = _TnOthOdukStatTxFeSES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 42),
    _TnOthOdukStatTxFeSES1DayTr_Type()
)
tnOthOdukStatTxFeSES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatTxFeSES1DayTr.setStatus("current")
_TnOthOdukStatTxNeUAS15MinTr_Type = Counter64
_TnOthOdukStatTxNeUAS15MinTr_Object = MibScalar
tnOthOdukStatTxNeUAS15MinTr = _TnOthOdukStatTxNeUAS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 43),
    _TnOthOdukStatTxNeUAS15MinTr_Type()
)
tnOthOdukStatTxNeUAS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatTxNeUAS15MinTr.setStatus("current")
_TnOthOdukStatTxNeUAS15MinRtr_Type = Counter64
_TnOthOdukStatTxNeUAS15MinRtr_Object = MibScalar
tnOthOdukStatTxNeUAS15MinRtr = _TnOthOdukStatTxNeUAS15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 44),
    _TnOthOdukStatTxNeUAS15MinRtr_Type()
)
tnOthOdukStatTxNeUAS15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatTxNeUAS15MinRtr.setStatus("current")
_TnOthOdukStatTxNeUAS1DayTr_Type = Counter64
_TnOthOdukStatTxNeUAS1DayTr_Object = MibScalar
tnOthOdukStatTxNeUAS1DayTr = _TnOthOdukStatTxNeUAS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 45),
    _TnOthOdukStatTxNeUAS1DayTr_Type()
)
tnOthOdukStatTxNeUAS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatTxNeUAS1DayTr.setStatus("current")
_TnOthOdukStatTxFeUAS15MinTr_Type = Counter64
_TnOthOdukStatTxFeUAS15MinTr_Object = MibScalar
tnOthOdukStatTxFeUAS15MinTr = _TnOthOdukStatTxFeUAS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 46),
    _TnOthOdukStatTxFeUAS15MinTr_Type()
)
tnOthOdukStatTxFeUAS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatTxFeUAS15MinTr.setStatus("current")
_TnOthOdukStatTxFeUAS15MinRtr_Type = Counter64
_TnOthOdukStatTxFeUAS15MinRtr_Object = MibScalar
tnOthOdukStatTxFeUAS15MinRtr = _TnOthOdukStatTxFeUAS15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 47),
    _TnOthOdukStatTxFeUAS15MinRtr_Type()
)
tnOthOdukStatTxFeUAS15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatTxFeUAS15MinRtr.setStatus("current")
_TnOthOdukStatTxFeUAS1DayTr_Type = Counter64
_TnOthOdukStatTxFeUAS1DayTr_Object = MibScalar
tnOthOdukStatTxFeUAS1DayTr = _TnOthOdukStatTxFeUAS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 6, 48),
    _TnOthOdukStatTxFeUAS1DayTr_Type()
)
tnOthOdukStatTxFeUAS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatTxFeUAS1DayTr.setStatus("current")
_TnStatisticsOtukScalars_ObjectIdentity = ObjectIdentity
tnStatisticsOtukScalars = _TnStatisticsOtukScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7)
)
_TnOthOtu1StatRxRsCorrCnt15MinTr_Type = Counter64
_TnOthOtu1StatRxRsCorrCnt15MinTr_Object = MibScalar
tnOthOtu1StatRxRsCorrCnt15MinTr = _TnOthOtu1StatRxRsCorrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 1),
    _TnOthOtu1StatRxRsCorrCnt15MinTr_Type()
)
tnOthOtu1StatRxRsCorrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu1StatRxRsCorrCnt15MinTr.setStatus("current")
_TnOthOtu1StatRxRsCorrCnt15MinRtr_Type = Counter64
_TnOthOtu1StatRxRsCorrCnt15MinRtr_Object = MibScalar
tnOthOtu1StatRxRsCorrCnt15MinRtr = _TnOthOtu1StatRxRsCorrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 2),
    _TnOthOtu1StatRxRsCorrCnt15MinRtr_Type()
)
tnOthOtu1StatRxRsCorrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu1StatRxRsCorrCnt15MinRtr.setStatus("current")
_TnOthOtu1StatRxRsCorrCnt1DayTr_Type = Counter64
_TnOthOtu1StatRxRsCorrCnt1DayTr_Object = MibScalar
tnOthOtu1StatRxRsCorrCnt1DayTr = _TnOthOtu1StatRxRsCorrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 3),
    _TnOthOtu1StatRxRsCorrCnt1DayTr_Type()
)
tnOthOtu1StatRxRsCorrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu1StatRxRsCorrCnt1DayTr.setStatus("current")
_TnOthOtu1StatRxRsUncorrCnt15MinTr_Type = Counter64
_TnOthOtu1StatRxRsUncorrCnt15MinTr_Object = MibScalar
tnOthOtu1StatRxRsUncorrCnt15MinTr = _TnOthOtu1StatRxRsUncorrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 4),
    _TnOthOtu1StatRxRsUncorrCnt15MinTr_Type()
)
tnOthOtu1StatRxRsUncorrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu1StatRxRsUncorrCnt15MinTr.setStatus("current")
_TnOthOtu1StatRxRsUncorrCnt15MinRtr_Type = Counter64
_TnOthOtu1StatRxRsUncorrCnt15MinRtr_Object = MibScalar
tnOthOtu1StatRxRsUncorrCnt15MinRtr = _TnOthOtu1StatRxRsUncorrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 5),
    _TnOthOtu1StatRxRsUncorrCnt15MinRtr_Type()
)
tnOthOtu1StatRxRsUncorrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu1StatRxRsUncorrCnt15MinRtr.setStatus("current")
_TnOthOtu1StatRxRsUncorrCnt1DayTr_Type = Counter64
_TnOthOtu1StatRxRsUncorrCnt1DayTr_Object = MibScalar
tnOthOtu1StatRxRsUncorrCnt1DayTr = _TnOthOtu1StatRxRsUncorrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 6),
    _TnOthOtu1StatRxRsUncorrCnt1DayTr_Type()
)
tnOthOtu1StatRxRsUncorrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu1StatRxRsUncorrCnt1DayTr.setStatus("current")
_TnOthOtu1StatRxNeSMBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOtu1StatRxNeSMBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOtu1StatRxNeSMBIP8ErrCnt15MinTr = _TnOthOtu1StatRxNeSMBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 7),
    _TnOthOtu1StatRxNeSMBIP8ErrCnt15MinTr_Type()
)
tnOthOtu1StatRxNeSMBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu1StatRxNeSMBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOtu1StatRxNeSMBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOtu1StatRxNeSMBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOtu1StatRxNeSMBIP8ErrCnt15MinRtr = _TnOthOtu1StatRxNeSMBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 8),
    _TnOthOtu1StatRxNeSMBIP8ErrCnt15MinRtr_Type()
)
tnOthOtu1StatRxNeSMBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu1StatRxNeSMBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOtu1StatRxNeSMBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOtu1StatRxNeSMBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOtu1StatRxNeSMBIP8ErrCnt1DayTr = _TnOthOtu1StatRxNeSMBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 9),
    _TnOthOtu1StatRxNeSMBIP8ErrCnt1DayTr_Type()
)
tnOthOtu1StatRxNeSMBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu1StatRxNeSMBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOtu1StatRxFeSMBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOtu1StatRxFeSMBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOtu1StatRxFeSMBIP8ErrCnt15MinTr = _TnOthOtu1StatRxFeSMBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 10),
    _TnOthOtu1StatRxFeSMBIP8ErrCnt15MinTr_Type()
)
tnOthOtu1StatRxFeSMBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu1StatRxFeSMBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOtu1StatRxFeSMBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOtu1StatRxFeSMBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOtu1StatRxFeSMBIP8ErrCnt15MinRtr = _TnOthOtu1StatRxFeSMBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 11),
    _TnOthOtu1StatRxFeSMBIP8ErrCnt15MinRtr_Type()
)
tnOthOtu1StatRxFeSMBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu1StatRxFeSMBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOtu1StatRxFeSMBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOtu1StatRxFeSMBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOtu1StatRxFeSMBIP8ErrCnt1DayTr = _TnOthOtu1StatRxFeSMBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 12),
    _TnOthOtu1StatRxFeSMBIP8ErrCnt1DayTr_Type()
)
tnOthOtu1StatRxFeSMBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu1StatRxFeSMBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOtu2StatRxRsCorrCnt15MinTr_Type = Counter64
_TnOthOtu2StatRxRsCorrCnt15MinTr_Object = MibScalar
tnOthOtu2StatRxRsCorrCnt15MinTr = _TnOthOtu2StatRxRsCorrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 13),
    _TnOthOtu2StatRxRsCorrCnt15MinTr_Type()
)
tnOthOtu2StatRxRsCorrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu2StatRxRsCorrCnt15MinTr.setStatus("current")
_TnOthOtu2StatRxRsCorrCnt15MinRtr_Type = Counter64
_TnOthOtu2StatRxRsCorrCnt15MinRtr_Object = MibScalar
tnOthOtu2StatRxRsCorrCnt15MinRtr = _TnOthOtu2StatRxRsCorrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 14),
    _TnOthOtu2StatRxRsCorrCnt15MinRtr_Type()
)
tnOthOtu2StatRxRsCorrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu2StatRxRsCorrCnt15MinRtr.setStatus("current")
_TnOthOtu2StatRxRsCorrCnt1DayTr_Type = Counter64
_TnOthOtu2StatRxRsCorrCnt1DayTr_Object = MibScalar
tnOthOtu2StatRxRsCorrCnt1DayTr = _TnOthOtu2StatRxRsCorrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 15),
    _TnOthOtu2StatRxRsCorrCnt1DayTr_Type()
)
tnOthOtu2StatRxRsCorrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu2StatRxRsCorrCnt1DayTr.setStatus("current")
_TnOthOtu2StatRxRsUncorrCnt15MinTr_Type = Counter64
_TnOthOtu2StatRxRsUncorrCnt15MinTr_Object = MibScalar
tnOthOtu2StatRxRsUncorrCnt15MinTr = _TnOthOtu2StatRxRsUncorrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 16),
    _TnOthOtu2StatRxRsUncorrCnt15MinTr_Type()
)
tnOthOtu2StatRxRsUncorrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu2StatRxRsUncorrCnt15MinTr.setStatus("current")
_TnOthOtu2StatRxRsUncorrCnt15MinRtr_Type = Counter64
_TnOthOtu2StatRxRsUncorrCnt15MinRtr_Object = MibScalar
tnOthOtu2StatRxRsUncorrCnt15MinRtr = _TnOthOtu2StatRxRsUncorrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 17),
    _TnOthOtu2StatRxRsUncorrCnt15MinRtr_Type()
)
tnOthOtu2StatRxRsUncorrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu2StatRxRsUncorrCnt15MinRtr.setStatus("current")
_TnOthOtu2StatRxRsUncorrCnt1DayTr_Type = Counter64
_TnOthOtu2StatRxRsUncorrCnt1DayTr_Object = MibScalar
tnOthOtu2StatRxRsUncorrCnt1DayTr = _TnOthOtu2StatRxRsUncorrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 18),
    _TnOthOtu2StatRxRsUncorrCnt1DayTr_Type()
)
tnOthOtu2StatRxRsUncorrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu2StatRxRsUncorrCnt1DayTr.setStatus("current")
_TnOthOtu2StatRxNeSMBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOtu2StatRxNeSMBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOtu2StatRxNeSMBIP8ErrCnt15MinTr = _TnOthOtu2StatRxNeSMBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 19),
    _TnOthOtu2StatRxNeSMBIP8ErrCnt15MinTr_Type()
)
tnOthOtu2StatRxNeSMBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu2StatRxNeSMBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOtu2StatRxNeSMBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOtu2StatRxNeSMBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOtu2StatRxNeSMBIP8ErrCnt15MinRtr = _TnOthOtu2StatRxNeSMBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 20),
    _TnOthOtu2StatRxNeSMBIP8ErrCnt15MinRtr_Type()
)
tnOthOtu2StatRxNeSMBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu2StatRxNeSMBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOtu2StatRxNeSMBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOtu2StatRxNeSMBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOtu2StatRxNeSMBIP8ErrCnt1DayTr = _TnOthOtu2StatRxNeSMBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 21),
    _TnOthOtu2StatRxNeSMBIP8ErrCnt1DayTr_Type()
)
tnOthOtu2StatRxNeSMBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu2StatRxNeSMBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOtu2StatRxFeSMBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOtu2StatRxFeSMBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOtu2StatRxFeSMBIP8ErrCnt15MinTr = _TnOthOtu2StatRxFeSMBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 22),
    _TnOthOtu2StatRxFeSMBIP8ErrCnt15MinTr_Type()
)
tnOthOtu2StatRxFeSMBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu2StatRxFeSMBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOtu2StatRxFeSMBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOtu2StatRxFeSMBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOtu2StatRxFeSMBIP8ErrCnt15MinRtr = _TnOthOtu2StatRxFeSMBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 23),
    _TnOthOtu2StatRxFeSMBIP8ErrCnt15MinRtr_Type()
)
tnOthOtu2StatRxFeSMBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu2StatRxFeSMBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOtu2StatRxFeSMBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOtu2StatRxFeSMBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOtu2StatRxFeSMBIP8ErrCnt1DayTr = _TnOthOtu2StatRxFeSMBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 24),
    _TnOthOtu2StatRxFeSMBIP8ErrCnt1DayTr_Type()
)
tnOthOtu2StatRxFeSMBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu2StatRxFeSMBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOtu3StatRxRsCorrCnt15MinTr_Type = Counter64
_TnOthOtu3StatRxRsCorrCnt15MinTr_Object = MibScalar
tnOthOtu3StatRxRsCorrCnt15MinTr = _TnOthOtu3StatRxRsCorrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 25),
    _TnOthOtu3StatRxRsCorrCnt15MinTr_Type()
)
tnOthOtu3StatRxRsCorrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu3StatRxRsCorrCnt15MinTr.setStatus("current")
_TnOthOtu3StatRxRsCorrCnt15MinRtr_Type = Counter64
_TnOthOtu3StatRxRsCorrCnt15MinRtr_Object = MibScalar
tnOthOtu3StatRxRsCorrCnt15MinRtr = _TnOthOtu3StatRxRsCorrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 26),
    _TnOthOtu3StatRxRsCorrCnt15MinRtr_Type()
)
tnOthOtu3StatRxRsCorrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu3StatRxRsCorrCnt15MinRtr.setStatus("current")
_TnOthOtu3StatRxRsCorrCnt1DayTr_Type = Counter64
_TnOthOtu3StatRxRsCorrCnt1DayTr_Object = MibScalar
tnOthOtu3StatRxRsCorrCnt1DayTr = _TnOthOtu3StatRxRsCorrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 27),
    _TnOthOtu3StatRxRsCorrCnt1DayTr_Type()
)
tnOthOtu3StatRxRsCorrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu3StatRxRsCorrCnt1DayTr.setStatus("current")
_TnOthOtu3StatRxRsUncorrCnt15MinTr_Type = Counter64
_TnOthOtu3StatRxRsUncorrCnt15MinTr_Object = MibScalar
tnOthOtu3StatRxRsUncorrCnt15MinTr = _TnOthOtu3StatRxRsUncorrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 28),
    _TnOthOtu3StatRxRsUncorrCnt15MinTr_Type()
)
tnOthOtu3StatRxRsUncorrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu3StatRxRsUncorrCnt15MinTr.setStatus("current")
_TnOthOtu3StatRxRsUncorrCnt15MinRtr_Type = Counter64
_TnOthOtu3StatRxRsUncorrCnt15MinRtr_Object = MibScalar
tnOthOtu3StatRxRsUncorrCnt15MinRtr = _TnOthOtu3StatRxRsUncorrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 29),
    _TnOthOtu3StatRxRsUncorrCnt15MinRtr_Type()
)
tnOthOtu3StatRxRsUncorrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu3StatRxRsUncorrCnt15MinRtr.setStatus("current")
_TnOthOtu3StatRxRsUncorrCnt1DayTr_Type = Counter64
_TnOthOtu3StatRxRsUncorrCnt1DayTr_Object = MibScalar
tnOthOtu3StatRxRsUncorrCnt1DayTr = _TnOthOtu3StatRxRsUncorrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 30),
    _TnOthOtu3StatRxRsUncorrCnt1DayTr_Type()
)
tnOthOtu3StatRxRsUncorrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu3StatRxRsUncorrCnt1DayTr.setStatus("current")
_TnOthOtu3StatRxNeSMBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOtu3StatRxNeSMBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOtu3StatRxNeSMBIP8ErrCnt15MinTr = _TnOthOtu3StatRxNeSMBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 31),
    _TnOthOtu3StatRxNeSMBIP8ErrCnt15MinTr_Type()
)
tnOthOtu3StatRxNeSMBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu3StatRxNeSMBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOtu3StatRxNeSMBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOtu3StatRxNeSMBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOtu3StatRxNeSMBIP8ErrCnt15MinRtr = _TnOthOtu3StatRxNeSMBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 32),
    _TnOthOtu3StatRxNeSMBIP8ErrCnt15MinRtr_Type()
)
tnOthOtu3StatRxNeSMBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu3StatRxNeSMBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOtu3StatRxNeSMBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOtu3StatRxNeSMBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOtu3StatRxNeSMBIP8ErrCnt1DayTr = _TnOthOtu3StatRxNeSMBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 33),
    _TnOthOtu3StatRxNeSMBIP8ErrCnt1DayTr_Type()
)
tnOthOtu3StatRxNeSMBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu3StatRxNeSMBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOtu3StatRxFeSMBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOtu3StatRxFeSMBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOtu3StatRxFeSMBIP8ErrCnt15MinTr = _TnOthOtu3StatRxFeSMBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 34),
    _TnOthOtu3StatRxFeSMBIP8ErrCnt15MinTr_Type()
)
tnOthOtu3StatRxFeSMBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu3StatRxFeSMBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOtu3StatRxFeSMBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOtu3StatRxFeSMBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOtu3StatRxFeSMBIP8ErrCnt15MinRtr = _TnOthOtu3StatRxFeSMBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 35),
    _TnOthOtu3StatRxFeSMBIP8ErrCnt15MinRtr_Type()
)
tnOthOtu3StatRxFeSMBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu3StatRxFeSMBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOtu3StatRxFeSMBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOtu3StatRxFeSMBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOtu3StatRxFeSMBIP8ErrCnt1DayTr = _TnOthOtu3StatRxFeSMBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 36),
    _TnOthOtu3StatRxFeSMBIP8ErrCnt1DayTr_Type()
)
tnOthOtu3StatRxFeSMBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu3StatRxFeSMBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOtu4StatRxRsCorrCnt15MinTr_Type = Counter64
_TnOthOtu4StatRxRsCorrCnt15MinTr_Object = MibScalar
tnOthOtu4StatRxRsCorrCnt15MinTr = _TnOthOtu4StatRxRsCorrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 37),
    _TnOthOtu4StatRxRsCorrCnt15MinTr_Type()
)
tnOthOtu4StatRxRsCorrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu4StatRxRsCorrCnt15MinTr.setStatus("current")
_TnOthOtu4StatRxRsCorrCnt15MinRtr_Type = Counter64
_TnOthOtu4StatRxRsCorrCnt15MinRtr_Object = MibScalar
tnOthOtu4StatRxRsCorrCnt15MinRtr = _TnOthOtu4StatRxRsCorrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 38),
    _TnOthOtu4StatRxRsCorrCnt15MinRtr_Type()
)
tnOthOtu4StatRxRsCorrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu4StatRxRsCorrCnt15MinRtr.setStatus("current")
_TnOthOtu4StatRxRsCorrCnt1DayTr_Type = Counter64
_TnOthOtu4StatRxRsCorrCnt1DayTr_Object = MibScalar
tnOthOtu4StatRxRsCorrCnt1DayTr = _TnOthOtu4StatRxRsCorrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 39),
    _TnOthOtu4StatRxRsCorrCnt1DayTr_Type()
)
tnOthOtu4StatRxRsCorrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu4StatRxRsCorrCnt1DayTr.setStatus("current")
_TnOthOtu4StatRxRsUncorrCnt15MinTr_Type = Counter64
_TnOthOtu4StatRxRsUncorrCnt15MinTr_Object = MibScalar
tnOthOtu4StatRxRsUncorrCnt15MinTr = _TnOthOtu4StatRxRsUncorrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 40),
    _TnOthOtu4StatRxRsUncorrCnt15MinTr_Type()
)
tnOthOtu4StatRxRsUncorrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu4StatRxRsUncorrCnt15MinTr.setStatus("current")
_TnOthOtu4StatRxRsUncorrCnt15MinRtr_Type = Counter64
_TnOthOtu4StatRxRsUncorrCnt15MinRtr_Object = MibScalar
tnOthOtu4StatRxRsUncorrCnt15MinRtr = _TnOthOtu4StatRxRsUncorrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 41),
    _TnOthOtu4StatRxRsUncorrCnt15MinRtr_Type()
)
tnOthOtu4StatRxRsUncorrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu4StatRxRsUncorrCnt15MinRtr.setStatus("current")
_TnOthOtu4StatRxRsUncorrCnt1DayTr_Type = Counter64
_TnOthOtu4StatRxRsUncorrCnt1DayTr_Object = MibScalar
tnOthOtu4StatRxRsUncorrCnt1DayTr = _TnOthOtu4StatRxRsUncorrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 42),
    _TnOthOtu4StatRxRsUncorrCnt1DayTr_Type()
)
tnOthOtu4StatRxRsUncorrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu4StatRxRsUncorrCnt1DayTr.setStatus("current")
_TnOthOtu4StatRxNeSMBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOtu4StatRxNeSMBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOtu4StatRxNeSMBIP8ErrCnt15MinTr = _TnOthOtu4StatRxNeSMBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 43),
    _TnOthOtu4StatRxNeSMBIP8ErrCnt15MinTr_Type()
)
tnOthOtu4StatRxNeSMBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu4StatRxNeSMBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOtu4StatRxNeSMBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOtu4StatRxNeSMBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOtu4StatRxNeSMBIP8ErrCnt15MinRtr = _TnOthOtu4StatRxNeSMBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 44),
    _TnOthOtu4StatRxNeSMBIP8ErrCnt15MinRtr_Type()
)
tnOthOtu4StatRxNeSMBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu4StatRxNeSMBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOtu4StatRxNeSMBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOtu4StatRxNeSMBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOtu4StatRxNeSMBIP8ErrCnt1DayTr = _TnOthOtu4StatRxNeSMBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 45),
    _TnOthOtu4StatRxNeSMBIP8ErrCnt1DayTr_Type()
)
tnOthOtu4StatRxNeSMBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu4StatRxNeSMBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOtu4StatRxFeSMBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOtu4StatRxFeSMBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOtu4StatRxFeSMBIP8ErrCnt15MinTr = _TnOthOtu4StatRxFeSMBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 46),
    _TnOthOtu4StatRxFeSMBIP8ErrCnt15MinTr_Type()
)
tnOthOtu4StatRxFeSMBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu4StatRxFeSMBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOtu4StatRxFeSMBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOtu4StatRxFeSMBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOtu4StatRxFeSMBIP8ErrCnt15MinRtr = _TnOthOtu4StatRxFeSMBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 47),
    _TnOthOtu4StatRxFeSMBIP8ErrCnt15MinRtr_Type()
)
tnOthOtu4StatRxFeSMBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu4StatRxFeSMBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOtu4StatRxFeSMBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOtu4StatRxFeSMBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOtu4StatRxFeSMBIP8ErrCnt1DayTr = _TnOthOtu4StatRxFeSMBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 48),
    _TnOthOtu4StatRxFeSMBIP8ErrCnt1DayTr_Type()
)
tnOthOtu4StatRxFeSMBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtu4StatRxFeSMBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOtukStatRxBERPreFEC15MinTr_Type = Counter64
_TnOthOtukStatRxBERPreFEC15MinTr_Object = MibScalar
tnOthOtukStatRxBERPreFEC15MinTr = _TnOthOtukStatRxBERPreFEC15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 49),
    _TnOthOtukStatRxBERPreFEC15MinTr_Type()
)
tnOthOtukStatRxBERPreFEC15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxBERPreFEC15MinTr.setStatus("current")
_TnOthOtukStatRxBERPreFEC15MinRtr_Type = Counter64
_TnOthOtukStatRxBERPreFEC15MinRtr_Object = MibScalar
tnOthOtukStatRxBERPreFEC15MinRtr = _TnOthOtukStatRxBERPreFEC15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 50),
    _TnOthOtukStatRxBERPreFEC15MinRtr_Type()
)
tnOthOtukStatRxBERPreFEC15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxBERPreFEC15MinRtr.setStatus("current")
_TnOthOtukStatRxBERPreFEC1DayTr_Type = Counter64
_TnOthOtukStatRxBERPreFEC1DayTr_Object = MibScalar
tnOthOtukStatRxBERPreFEC1DayTr = _TnOthOtukStatRxBERPreFEC1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 51),
    _TnOthOtukStatRxBERPreFEC1DayTr_Type()
)
tnOthOtukStatRxBERPreFEC1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxBERPreFEC1DayTr.setStatus("current")
_TnOthOtukStatRxBERPostFEC15MinTr_Type = Counter64
_TnOthOtukStatRxBERPostFEC15MinTr_Object = MibScalar
tnOthOtukStatRxBERPostFEC15MinTr = _TnOthOtukStatRxBERPostFEC15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 52),
    _TnOthOtukStatRxBERPostFEC15MinTr_Type()
)
tnOthOtukStatRxBERPostFEC15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxBERPostFEC15MinTr.setStatus("current")
_TnOthOtukStatRxBERPostFEC15MinRtr_Type = Counter64
_TnOthOtukStatRxBERPostFEC15MinRtr_Object = MibScalar
tnOthOtukStatRxBERPostFEC15MinRtr = _TnOthOtukStatRxBERPostFEC15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 53),
    _TnOthOtukStatRxBERPostFEC15MinRtr_Type()
)
tnOthOtukStatRxBERPostFEC15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxBERPostFEC15MinRtr.setStatus("current")
_TnOthOtukStatRxBERPostFEC1DayTr_Type = Counter64
_TnOthOtukStatRxBERPostFEC1DayTr_Object = MibScalar
tnOthOtukStatRxBERPostFEC1DayTr = _TnOthOtukStatRxBERPostFEC1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 54),
    _TnOthOtukStatRxBERPostFEC1DayTr_Type()
)
tnOthOtukStatRxBERPostFEC1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxBERPostFEC1DayTr.setStatus("current")
_TnOthOtukStatRxNeSMES15MinTr_Type = Counter64
_TnOthOtukStatRxNeSMES15MinTr_Object = MibScalar
tnOthOtukStatRxNeSMES15MinTr = _TnOthOtukStatRxNeSMES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 55),
    _TnOthOtukStatRxNeSMES15MinTr_Type()
)
tnOthOtukStatRxNeSMES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxNeSMES15MinTr.setStatus("current")
_TnOthOtukStatRxNeSMES15MinRtr_Type = Counter64
_TnOthOtukStatRxNeSMES15MinRtr_Object = MibScalar
tnOthOtukStatRxNeSMES15MinRtr = _TnOthOtukStatRxNeSMES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 56),
    _TnOthOtukStatRxNeSMES15MinRtr_Type()
)
tnOthOtukStatRxNeSMES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxNeSMES15MinRtr.setStatus("current")
_TnOthOtukStatRxNeSMES1DayTr_Type = Counter64
_TnOthOtukStatRxNeSMES1DayTr_Object = MibScalar
tnOthOtukStatRxNeSMES1DayTr = _TnOthOtukStatRxNeSMES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 57),
    _TnOthOtukStatRxNeSMES1DayTr_Type()
)
tnOthOtukStatRxNeSMES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxNeSMES1DayTr.setStatus("current")
_TnOthOtukStatRxFeSMES15MinTr_Type = Counter64
_TnOthOtukStatRxFeSMES15MinTr_Object = MibScalar
tnOthOtukStatRxFeSMES15MinTr = _TnOthOtukStatRxFeSMES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 58),
    _TnOthOtukStatRxFeSMES15MinTr_Type()
)
tnOthOtukStatRxFeSMES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxFeSMES15MinTr.setStatus("current")
_TnOthOtukStatRxFeSMES15MinRtr_Type = Counter64
_TnOthOtukStatRxFeSMES15MinRtr_Object = MibScalar
tnOthOtukStatRxFeSMES15MinRtr = _TnOthOtukStatRxFeSMES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 59),
    _TnOthOtukStatRxFeSMES15MinRtr_Type()
)
tnOthOtukStatRxFeSMES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxFeSMES15MinRtr.setStatus("current")
_TnOthOtukStatRxFeSMES1DayTr_Type = Counter64
_TnOthOtukStatRxFeSMES1DayTr_Object = MibScalar
tnOthOtukStatRxFeSMES1DayTr = _TnOthOtukStatRxFeSMES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 60),
    _TnOthOtukStatRxFeSMES1DayTr_Type()
)
tnOthOtukStatRxFeSMES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxFeSMES1DayTr.setStatus("current")
_TnOthOtukStatRxNeSMSES15MinTr_Type = Counter64
_TnOthOtukStatRxNeSMSES15MinTr_Object = MibScalar
tnOthOtukStatRxNeSMSES15MinTr = _TnOthOtukStatRxNeSMSES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 61),
    _TnOthOtukStatRxNeSMSES15MinTr_Type()
)
tnOthOtukStatRxNeSMSES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxNeSMSES15MinTr.setStatus("current")
_TnOthOtukStatRxNeSMSES15MinRtr_Type = Counter64
_TnOthOtukStatRxNeSMSES15MinRtr_Object = MibScalar
tnOthOtukStatRxNeSMSES15MinRtr = _TnOthOtukStatRxNeSMSES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 62),
    _TnOthOtukStatRxNeSMSES15MinRtr_Type()
)
tnOthOtukStatRxNeSMSES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxNeSMSES15MinRtr.setStatus("current")
_TnOthOtukStatRxNeSMSES1DayTr_Type = Counter64
_TnOthOtukStatRxNeSMSES1DayTr_Object = MibScalar
tnOthOtukStatRxNeSMSES1DayTr = _TnOthOtukStatRxNeSMSES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 63),
    _TnOthOtukStatRxNeSMSES1DayTr_Type()
)
tnOthOtukStatRxNeSMSES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxNeSMSES1DayTr.setStatus("current")
_TnOthOtukStatRxFeSMSES15MinTr_Type = Counter64
_TnOthOtukStatRxFeSMSES15MinTr_Object = MibScalar
tnOthOtukStatRxFeSMSES15MinTr = _TnOthOtukStatRxFeSMSES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 64),
    _TnOthOtukStatRxFeSMSES15MinTr_Type()
)
tnOthOtukStatRxFeSMSES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxFeSMSES15MinTr.setStatus("current")
_TnOthOtukStatRxFeSMSES15MinRtr_Type = Counter64
_TnOthOtukStatRxFeSMSES15MinRtr_Object = MibScalar
tnOthOtukStatRxFeSMSES15MinRtr = _TnOthOtukStatRxFeSMSES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 65),
    _TnOthOtukStatRxFeSMSES15MinRtr_Type()
)
tnOthOtukStatRxFeSMSES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxFeSMSES15MinRtr.setStatus("current")
_TnOthOtukStatRxFeSMSES1DayTr_Type = Counter64
_TnOthOtukStatRxFeSMSES1DayTr_Object = MibScalar
tnOthOtukStatRxFeSMSES1DayTr = _TnOthOtukStatRxFeSMSES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 66),
    _TnOthOtukStatRxFeSMSES1DayTr_Type()
)
tnOthOtukStatRxFeSMSES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxFeSMSES1DayTr.setStatus("current")
_TnOthOtukStatRxNeSMUAS15MinTr_Type = Counter64
_TnOthOtukStatRxNeSMUAS15MinTr_Object = MibScalar
tnOthOtukStatRxNeSMUAS15MinTr = _TnOthOtukStatRxNeSMUAS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 67),
    _TnOthOtukStatRxNeSMUAS15MinTr_Type()
)
tnOthOtukStatRxNeSMUAS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxNeSMUAS15MinTr.setStatus("current")
_TnOthOtukStatRxNeSMUAS15MinRtr_Type = Counter64
_TnOthOtukStatRxNeSMUAS15MinRtr_Object = MibScalar
tnOthOtukStatRxNeSMUAS15MinRtr = _TnOthOtukStatRxNeSMUAS15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 68),
    _TnOthOtukStatRxNeSMUAS15MinRtr_Type()
)
tnOthOtukStatRxNeSMUAS15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxNeSMUAS15MinRtr.setStatus("current")
_TnOthOtukStatRxNeSMUAS1DayTr_Type = Counter64
_TnOthOtukStatRxNeSMUAS1DayTr_Object = MibScalar
tnOthOtukStatRxNeSMUAS1DayTr = _TnOthOtukStatRxNeSMUAS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 69),
    _TnOthOtukStatRxNeSMUAS1DayTr_Type()
)
tnOthOtukStatRxNeSMUAS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxNeSMUAS1DayTr.setStatus("current")
_TnOthOtukStatRxFeSMUAS15MinTr_Type = Counter64
_TnOthOtukStatRxFeSMUAS15MinTr_Object = MibScalar
tnOthOtukStatRxFeSMUAS15MinTr = _TnOthOtukStatRxFeSMUAS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 70),
    _TnOthOtukStatRxFeSMUAS15MinTr_Type()
)
tnOthOtukStatRxFeSMUAS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxFeSMUAS15MinTr.setStatus("current")
_TnOthOtukStatRxFeSMUAS15MinRtr_Type = Counter64
_TnOthOtukStatRxFeSMUAS15MinRtr_Object = MibScalar
tnOthOtukStatRxFeSMUAS15MinRtr = _TnOthOtukStatRxFeSMUAS15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 71),
    _TnOthOtukStatRxFeSMUAS15MinRtr_Type()
)
tnOthOtukStatRxFeSMUAS15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxFeSMUAS15MinRtr.setStatus("current")
_TnOthOtukStatRxFeSMUAS1DayTr_Type = Counter64
_TnOthOtukStatRxFeSMUAS1DayTr_Object = MibScalar
tnOthOtukStatRxFeSMUAS1DayTr = _TnOthOtukStatRxFeSMUAS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 72),
    _TnOthOtukStatRxFeSMUAS1DayTr_Type()
)
tnOthOtukStatRxFeSMUAS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxFeSMUAS1DayTr.setStatus("current")
_TnOthOtukStatRxNeIAES15MinTr_Type = Counter64
_TnOthOtukStatRxNeIAES15MinTr_Object = MibScalar
tnOthOtukStatRxNeIAES15MinTr = _TnOthOtukStatRxNeIAES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 73),
    _TnOthOtukStatRxNeIAES15MinTr_Type()
)
tnOthOtukStatRxNeIAES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxNeIAES15MinTr.setStatus("current")
_TnOthOtukStatRxNeIAES15MinRtr_Type = Counter64
_TnOthOtukStatRxNeIAES15MinRtr_Object = MibScalar
tnOthOtukStatRxNeIAES15MinRtr = _TnOthOtukStatRxNeIAES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 74),
    _TnOthOtukStatRxNeIAES15MinRtr_Type()
)
tnOthOtukStatRxNeIAES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxNeIAES15MinRtr.setStatus("current")
_TnOthOtukStatRxNeIAES1DayTr_Type = Counter64
_TnOthOtukStatRxNeIAES1DayTr_Object = MibScalar
tnOthOtukStatRxNeIAES1DayTr = _TnOthOtukStatRxNeIAES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 75),
    _TnOthOtukStatRxNeIAES1DayTr_Type()
)
tnOthOtukStatRxNeIAES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxNeIAES1DayTr.setStatus("current")
_TnOthOtukStatRxFeIAES15MinTr_Type = Counter64
_TnOthOtukStatRxFeIAES15MinTr_Object = MibScalar
tnOthOtukStatRxFeIAES15MinTr = _TnOthOtukStatRxFeIAES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 76),
    _TnOthOtukStatRxFeIAES15MinTr_Type()
)
tnOthOtukStatRxFeIAES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxFeIAES15MinTr.setStatus("current")
_TnOthOtukStatRxFeIAES15MinRtr_Type = Counter64
_TnOthOtukStatRxFeIAES15MinRtr_Object = MibScalar
tnOthOtukStatRxFeIAES15MinRtr = _TnOthOtukStatRxFeIAES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 77),
    _TnOthOtukStatRxFeIAES15MinRtr_Type()
)
tnOthOtukStatRxFeIAES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxFeIAES15MinRtr.setStatus("current")
_TnOthOtukStatRxFeIAES1DayTr_Type = Counter64
_TnOthOtukStatRxFeIAES1DayTr_Object = MibScalar
tnOthOtukStatRxFeIAES1DayTr = _TnOthOtukStatRxFeIAES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 7, 78),
    _TnOthOtukStatRxFeIAES1DayTr_Type()
)
tnOthOtukStatRxFeIAES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOtukStatRxFeIAES1DayTr.setStatus("current")
_TnStatisticsSonetScalars_ObjectIdentity = ObjectIdentity
tnStatisticsSonetScalars = _TnStatisticsSonetScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8)
)
_TnSonetStatsOC768RxCVS15MinTr_Type = Counter32
_TnSonetStatsOC768RxCVS15MinTr_Object = MibScalar
tnSonetStatsOC768RxCVS15MinTr = _TnSonetStatsOC768RxCVS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 1),
    _TnSonetStatsOC768RxCVS15MinTr_Type()
)
tnSonetStatsOC768RxCVS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC768RxCVS15MinTr.setStatus("current")
_TnSonetStatsOC192RxCVS15MinTr_Type = Counter32
_TnSonetStatsOC192RxCVS15MinTr_Object = MibScalar
tnSonetStatsOC192RxCVS15MinTr = _TnSonetStatsOC192RxCVS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 2),
    _TnSonetStatsOC192RxCVS15MinTr_Type()
)
tnSonetStatsOC192RxCVS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC192RxCVS15MinTr.setStatus("current")
_TnSonetStatsOC48RxCVS15MinTr_Type = Counter32
_TnSonetStatsOC48RxCVS15MinTr_Object = MibScalar
tnSonetStatsOC48RxCVS15MinTr = _TnSonetStatsOC48RxCVS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 3),
    _TnSonetStatsOC48RxCVS15MinTr_Type()
)
tnSonetStatsOC48RxCVS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC48RxCVS15MinTr.setStatus("current")
_TnSonetStatsOC12RxCVS15MinTr_Type = Counter32
_TnSonetStatsOC12RxCVS15MinTr_Object = MibScalar
tnSonetStatsOC12RxCVS15MinTr = _TnSonetStatsOC12RxCVS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 4),
    _TnSonetStatsOC12RxCVS15MinTr_Type()
)
tnSonetStatsOC12RxCVS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC12RxCVS15MinTr.setStatus("current")
_TnSonetStatsOC3RxCVS15MinTr_Type = Counter32
_TnSonetStatsOC3RxCVS15MinTr_Object = MibScalar
tnSonetStatsOC3RxCVS15MinTr = _TnSonetStatsOC3RxCVS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 5),
    _TnSonetStatsOC3RxCVS15MinTr_Type()
)
tnSonetStatsOC3RxCVS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC3RxCVS15MinTr.setStatus("current")
_TnSonetStatsRxESS15MinTr_Type = Counter32
_TnSonetStatsRxESS15MinTr_Object = MibScalar
tnSonetStatsRxESS15MinTr = _TnSonetStatsRxESS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 6),
    _TnSonetStatsRxESS15MinTr_Type()
)
tnSonetStatsRxESS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsRxESS15MinTr.setStatus("current")
_TnSonetStatsRxSESS15MinTr_Type = Counter32
_TnSonetStatsRxSESS15MinTr_Object = MibScalar
tnSonetStatsRxSESS15MinTr = _TnSonetStatsRxSESS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 7),
    _TnSonetStatsRxSESS15MinTr_Type()
)
tnSonetStatsRxSESS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsRxSESS15MinTr.setStatus("current")
_TnSonetStatsRxSEFSS15MinTr_Type = Counter32
_TnSonetStatsRxSEFSS15MinTr_Object = MibScalar
tnSonetStatsRxSEFSS15MinTr = _TnSonetStatsRxSEFSS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 8),
    _TnSonetStatsRxSEFSS15MinTr_Type()
)
tnSonetStatsRxSEFSS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsRxSEFSS15MinTr.setStatus("current")
_TnSonetStatsOC768RxCVL15MinTr_Type = Counter32
_TnSonetStatsOC768RxCVL15MinTr_Object = MibScalar
tnSonetStatsOC768RxCVL15MinTr = _TnSonetStatsOC768RxCVL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 9),
    _TnSonetStatsOC768RxCVL15MinTr_Type()
)
tnSonetStatsOC768RxCVL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC768RxCVL15MinTr.setStatus("current")
_TnSonetStatsOC192RxCVL15MinTr_Type = Counter32
_TnSonetStatsOC192RxCVL15MinTr_Object = MibScalar
tnSonetStatsOC192RxCVL15MinTr = _TnSonetStatsOC192RxCVL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 10),
    _TnSonetStatsOC192RxCVL15MinTr_Type()
)
tnSonetStatsOC192RxCVL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC192RxCVL15MinTr.setStatus("current")
_TnSonetStatsOC48RxCVL15MinTr_Type = Counter32
_TnSonetStatsOC48RxCVL15MinTr_Object = MibScalar
tnSonetStatsOC48RxCVL15MinTr = _TnSonetStatsOC48RxCVL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 11),
    _TnSonetStatsOC48RxCVL15MinTr_Type()
)
tnSonetStatsOC48RxCVL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC48RxCVL15MinTr.setStatus("current")
_TnSonetStatsOC12RxCVL15MinTr_Type = Counter32
_TnSonetStatsOC12RxCVL15MinTr_Object = MibScalar
tnSonetStatsOC12RxCVL15MinTr = _TnSonetStatsOC12RxCVL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 12),
    _TnSonetStatsOC12RxCVL15MinTr_Type()
)
tnSonetStatsOC12RxCVL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC12RxCVL15MinTr.setStatus("current")
_TnSonetStatsOC3RxCVL15MinTr_Type = Counter32
_TnSonetStatsOC3RxCVL15MinTr_Object = MibScalar
tnSonetStatsOC3RxCVL15MinTr = _TnSonetStatsOC3RxCVL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 13),
    _TnSonetStatsOC3RxCVL15MinTr_Type()
)
tnSonetStatsOC3RxCVL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC3RxCVL15MinTr.setStatus("current")
_TnSonetStatsRxESL15MinTr_Type = Counter32
_TnSonetStatsRxESL15MinTr_Object = MibScalar
tnSonetStatsRxESL15MinTr = _TnSonetStatsRxESL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 14),
    _TnSonetStatsRxESL15MinTr_Type()
)
tnSonetStatsRxESL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsRxESL15MinTr.setStatus("current")
_TnSonetStatsRxSESL15MinTr_Type = Counter32
_TnSonetStatsRxSESL15MinTr_Object = MibScalar
tnSonetStatsRxSESL15MinTr = _TnSonetStatsRxSESL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 15),
    _TnSonetStatsRxSESL15MinTr_Type()
)
tnSonetStatsRxSESL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsRxSESL15MinTr.setStatus("current")
_TnSonetStatsRxUASL15MinTr_Type = Counter32
_TnSonetStatsRxUASL15MinTr_Object = MibScalar
tnSonetStatsRxUASL15MinTr = _TnSonetStatsRxUASL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 16),
    _TnSonetStatsRxUASL15MinTr_Type()
)
tnSonetStatsRxUASL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsRxUASL15MinTr.setStatus("current")
_TnSonetStatsOC768TxCVS15MinTr_Type = Counter32
_TnSonetStatsOC768TxCVS15MinTr_Object = MibScalar
tnSonetStatsOC768TxCVS15MinTr = _TnSonetStatsOC768TxCVS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 17),
    _TnSonetStatsOC768TxCVS15MinTr_Type()
)
tnSonetStatsOC768TxCVS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC768TxCVS15MinTr.setStatus("current")
_TnSonetStatsOC192TxCVS15MinTr_Type = Counter32
_TnSonetStatsOC192TxCVS15MinTr_Object = MibScalar
tnSonetStatsOC192TxCVS15MinTr = _TnSonetStatsOC192TxCVS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 18),
    _TnSonetStatsOC192TxCVS15MinTr_Type()
)
tnSonetStatsOC192TxCVS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC192TxCVS15MinTr.setStatus("current")
_TnSonetStatsOC48TxCVS15MinTr_Type = Counter32
_TnSonetStatsOC48TxCVS15MinTr_Object = MibScalar
tnSonetStatsOC48TxCVS15MinTr = _TnSonetStatsOC48TxCVS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 19),
    _TnSonetStatsOC48TxCVS15MinTr_Type()
)
tnSonetStatsOC48TxCVS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC48TxCVS15MinTr.setStatus("current")
_TnSonetStatsOC12TxCVS15MinTr_Type = Counter32
_TnSonetStatsOC12TxCVS15MinTr_Object = MibScalar
tnSonetStatsOC12TxCVS15MinTr = _TnSonetStatsOC12TxCVS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 20),
    _TnSonetStatsOC12TxCVS15MinTr_Type()
)
tnSonetStatsOC12TxCVS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC12TxCVS15MinTr.setStatus("current")
_TnSonetStatsOC3TxCVS15MinTr_Type = Counter32
_TnSonetStatsOC3TxCVS15MinTr_Object = MibScalar
tnSonetStatsOC3TxCVS15MinTr = _TnSonetStatsOC3TxCVS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 21),
    _TnSonetStatsOC3TxCVS15MinTr_Type()
)
tnSonetStatsOC3TxCVS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC3TxCVS15MinTr.setStatus("current")
_TnSonetStatsTxESS15MinTr_Type = Counter32
_TnSonetStatsTxESS15MinTr_Object = MibScalar
tnSonetStatsTxESS15MinTr = _TnSonetStatsTxESS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 22),
    _TnSonetStatsTxESS15MinTr_Type()
)
tnSonetStatsTxESS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsTxESS15MinTr.setStatus("current")
_TnSonetStatsTxSESS15MinTr_Type = Counter32
_TnSonetStatsTxSESS15MinTr_Object = MibScalar
tnSonetStatsTxSESS15MinTr = _TnSonetStatsTxSESS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 23),
    _TnSonetStatsTxSESS15MinTr_Type()
)
tnSonetStatsTxSESS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsTxSESS15MinTr.setStatus("current")
_TnSonetStatsTxSEFSS15MinTr_Type = Counter32
_TnSonetStatsTxSEFSS15MinTr_Object = MibScalar
tnSonetStatsTxSEFSS15MinTr = _TnSonetStatsTxSEFSS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 24),
    _TnSonetStatsTxSEFSS15MinTr_Type()
)
tnSonetStatsTxSEFSS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsTxSEFSS15MinTr.setStatus("current")
_TnSonetStatsOC768TxCVL15MinTr_Type = Counter32
_TnSonetStatsOC768TxCVL15MinTr_Object = MibScalar
tnSonetStatsOC768TxCVL15MinTr = _TnSonetStatsOC768TxCVL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 25),
    _TnSonetStatsOC768TxCVL15MinTr_Type()
)
tnSonetStatsOC768TxCVL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC768TxCVL15MinTr.setStatus("current")
_TnSonetStatsOC192TxCVL15MinTr_Type = Counter32
_TnSonetStatsOC192TxCVL15MinTr_Object = MibScalar
tnSonetStatsOC192TxCVL15MinTr = _TnSonetStatsOC192TxCVL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 26),
    _TnSonetStatsOC192TxCVL15MinTr_Type()
)
tnSonetStatsOC192TxCVL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC192TxCVL15MinTr.setStatus("current")
_TnSonetStatsOC48TxCVL15MinTr_Type = Counter32
_TnSonetStatsOC48TxCVL15MinTr_Object = MibScalar
tnSonetStatsOC48TxCVL15MinTr = _TnSonetStatsOC48TxCVL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 27),
    _TnSonetStatsOC48TxCVL15MinTr_Type()
)
tnSonetStatsOC48TxCVL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC48TxCVL15MinTr.setStatus("current")
_TnSonetStatsOC12TxCVL15MinTr_Type = Counter32
_TnSonetStatsOC12TxCVL15MinTr_Object = MibScalar
tnSonetStatsOC12TxCVL15MinTr = _TnSonetStatsOC12TxCVL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 28),
    _TnSonetStatsOC12TxCVL15MinTr_Type()
)
tnSonetStatsOC12TxCVL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC12TxCVL15MinTr.setStatus("current")
_TnSonetStatsOC3TxCVL15MinTr_Type = Counter32
_TnSonetStatsOC3TxCVL15MinTr_Object = MibScalar
tnSonetStatsOC3TxCVL15MinTr = _TnSonetStatsOC3TxCVL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 29),
    _TnSonetStatsOC3TxCVL15MinTr_Type()
)
tnSonetStatsOC3TxCVL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC3TxCVL15MinTr.setStatus("current")
_TnSonetStatsTxESL15MinTr_Type = Counter32
_TnSonetStatsTxESL15MinTr_Object = MibScalar
tnSonetStatsTxESL15MinTr = _TnSonetStatsTxESL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 30),
    _TnSonetStatsTxESL15MinTr_Type()
)
tnSonetStatsTxESL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsTxESL15MinTr.setStatus("current")
_TnSonetStatsTxSESL15MinTr_Type = Counter32
_TnSonetStatsTxSESL15MinTr_Object = MibScalar
tnSonetStatsTxSESL15MinTr = _TnSonetStatsTxSESL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 31),
    _TnSonetStatsTxSESL15MinTr_Type()
)
tnSonetStatsTxSESL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsTxSESL15MinTr.setStatus("current")
_TnSonetStatsTxUASL15MinTr_Type = Counter32
_TnSonetStatsTxUASL15MinTr_Object = MibScalar
tnSonetStatsTxUASL15MinTr = _TnSonetStatsTxUASL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 32),
    _TnSonetStatsTxUASL15MinTr_Type()
)
tnSonetStatsTxUASL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsTxUASL15MinTr.setStatus("current")
_TnSonetStatsRxUASS15MinTr_Type = Counter32
_TnSonetStatsRxUASS15MinTr_Object = MibScalar
tnSonetStatsRxUASS15MinTr = _TnSonetStatsRxUASS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 33),
    _TnSonetStatsRxUASS15MinTr_Type()
)
tnSonetStatsRxUASS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsRxUASS15MinTr.setStatus("current")
_TnSonetStatsTxUASS15MinTr_Type = Counter32
_TnSonetStatsTxUASS15MinTr_Object = MibScalar
tnSonetStatsTxUASS15MinTr = _TnSonetStatsTxUASS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 34),
    _TnSonetStatsTxUASS15MinTr_Type()
)
tnSonetStatsTxUASS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsTxUASS15MinTr.setStatus("current")
_TnSonetStatsOC768RxCVS1DayTr_Type = Counter32
_TnSonetStatsOC768RxCVS1DayTr_Object = MibScalar
tnSonetStatsOC768RxCVS1DayTr = _TnSonetStatsOC768RxCVS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 35),
    _TnSonetStatsOC768RxCVS1DayTr_Type()
)
tnSonetStatsOC768RxCVS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC768RxCVS1DayTr.setStatus("current")
_TnSonetStatsOC192RxCVS1DayTr_Type = Counter32
_TnSonetStatsOC192RxCVS1DayTr_Object = MibScalar
tnSonetStatsOC192RxCVS1DayTr = _TnSonetStatsOC192RxCVS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 36),
    _TnSonetStatsOC192RxCVS1DayTr_Type()
)
tnSonetStatsOC192RxCVS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC192RxCVS1DayTr.setStatus("current")
_TnSonetStatsOC48RxCVS1DayTr_Type = Counter32
_TnSonetStatsOC48RxCVS1DayTr_Object = MibScalar
tnSonetStatsOC48RxCVS1DayTr = _TnSonetStatsOC48RxCVS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 37),
    _TnSonetStatsOC48RxCVS1DayTr_Type()
)
tnSonetStatsOC48RxCVS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC48RxCVS1DayTr.setStatus("current")
_TnSonetStatsOC12RxCVS1DayTr_Type = Counter32
_TnSonetStatsOC12RxCVS1DayTr_Object = MibScalar
tnSonetStatsOC12RxCVS1DayTr = _TnSonetStatsOC12RxCVS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 38),
    _TnSonetStatsOC12RxCVS1DayTr_Type()
)
tnSonetStatsOC12RxCVS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC12RxCVS1DayTr.setStatus("current")
_TnSonetStatsOC3RxCVS1DayTr_Type = Counter32
_TnSonetStatsOC3RxCVS1DayTr_Object = MibScalar
tnSonetStatsOC3RxCVS1DayTr = _TnSonetStatsOC3RxCVS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 39),
    _TnSonetStatsOC3RxCVS1DayTr_Type()
)
tnSonetStatsOC3RxCVS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC3RxCVS1DayTr.setStatus("current")
_TnSonetStatsRxESS1DayTr_Type = Counter32
_TnSonetStatsRxESS1DayTr_Object = MibScalar
tnSonetStatsRxESS1DayTr = _TnSonetStatsRxESS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 40),
    _TnSonetStatsRxESS1DayTr_Type()
)
tnSonetStatsRxESS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsRxESS1DayTr.setStatus("current")
_TnSonetStatsRxSESS1DayTr_Type = Counter32
_TnSonetStatsRxSESS1DayTr_Object = MibScalar
tnSonetStatsRxSESS1DayTr = _TnSonetStatsRxSESS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 41),
    _TnSonetStatsRxSESS1DayTr_Type()
)
tnSonetStatsRxSESS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsRxSESS1DayTr.setStatus("current")
_TnSonetStatsRxSEFSS1DayTr_Type = Counter32
_TnSonetStatsRxSEFSS1DayTr_Object = MibScalar
tnSonetStatsRxSEFSS1DayTr = _TnSonetStatsRxSEFSS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 42),
    _TnSonetStatsRxSEFSS1DayTr_Type()
)
tnSonetStatsRxSEFSS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsRxSEFSS1DayTr.setStatus("current")
_TnSonetStatsOC768RxCVL1DayTr_Type = Counter32
_TnSonetStatsOC768RxCVL1DayTr_Object = MibScalar
tnSonetStatsOC768RxCVL1DayTr = _TnSonetStatsOC768RxCVL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 43),
    _TnSonetStatsOC768RxCVL1DayTr_Type()
)
tnSonetStatsOC768RxCVL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC768RxCVL1DayTr.setStatus("current")
_TnSonetStatsOC192RxCVL1DayTr_Type = Counter32
_TnSonetStatsOC192RxCVL1DayTr_Object = MibScalar
tnSonetStatsOC192RxCVL1DayTr = _TnSonetStatsOC192RxCVL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 44),
    _TnSonetStatsOC192RxCVL1DayTr_Type()
)
tnSonetStatsOC192RxCVL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC192RxCVL1DayTr.setStatus("current")
_TnSonetStatsOC48RxCVL1DayTr_Type = Counter32
_TnSonetStatsOC48RxCVL1DayTr_Object = MibScalar
tnSonetStatsOC48RxCVL1DayTr = _TnSonetStatsOC48RxCVL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 45),
    _TnSonetStatsOC48RxCVL1DayTr_Type()
)
tnSonetStatsOC48RxCVL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC48RxCVL1DayTr.setStatus("current")
_TnSonetStatsOC12RxCVL1DayTr_Type = Counter32
_TnSonetStatsOC12RxCVL1DayTr_Object = MibScalar
tnSonetStatsOC12RxCVL1DayTr = _TnSonetStatsOC12RxCVL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 46),
    _TnSonetStatsOC12RxCVL1DayTr_Type()
)
tnSonetStatsOC12RxCVL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC12RxCVL1DayTr.setStatus("current")
_TnSonetStatsOC3RxCVL1DayTr_Type = Counter32
_TnSonetStatsOC3RxCVL1DayTr_Object = MibScalar
tnSonetStatsOC3RxCVL1DayTr = _TnSonetStatsOC3RxCVL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 47),
    _TnSonetStatsOC3RxCVL1DayTr_Type()
)
tnSonetStatsOC3RxCVL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC3RxCVL1DayTr.setStatus("current")
_TnSonetStatsRxESL1DayTr_Type = Counter32
_TnSonetStatsRxESL1DayTr_Object = MibScalar
tnSonetStatsRxESL1DayTr = _TnSonetStatsRxESL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 48),
    _TnSonetStatsRxESL1DayTr_Type()
)
tnSonetStatsRxESL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsRxESL1DayTr.setStatus("current")
_TnSonetStatsRxSESL1DayTr_Type = Counter32
_TnSonetStatsRxSESL1DayTr_Object = MibScalar
tnSonetStatsRxSESL1DayTr = _TnSonetStatsRxSESL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 49),
    _TnSonetStatsRxSESL1DayTr_Type()
)
tnSonetStatsRxSESL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsRxSESL1DayTr.setStatus("current")
_TnSonetStatsRxUASL1DayTr_Type = Counter32
_TnSonetStatsRxUASL1DayTr_Object = MibScalar
tnSonetStatsRxUASL1DayTr = _TnSonetStatsRxUASL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 50),
    _TnSonetStatsRxUASL1DayTr_Type()
)
tnSonetStatsRxUASL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsRxUASL1DayTr.setStatus("current")
_TnSonetStatsOC768TxCVS1DayTr_Type = Counter32
_TnSonetStatsOC768TxCVS1DayTr_Object = MibScalar
tnSonetStatsOC768TxCVS1DayTr = _TnSonetStatsOC768TxCVS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 51),
    _TnSonetStatsOC768TxCVS1DayTr_Type()
)
tnSonetStatsOC768TxCVS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC768TxCVS1DayTr.setStatus("current")
_TnSonetStatsOC192TxCVS1DayTr_Type = Counter32
_TnSonetStatsOC192TxCVS1DayTr_Object = MibScalar
tnSonetStatsOC192TxCVS1DayTr = _TnSonetStatsOC192TxCVS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 52),
    _TnSonetStatsOC192TxCVS1DayTr_Type()
)
tnSonetStatsOC192TxCVS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC192TxCVS1DayTr.setStatus("current")
_TnSonetStatsOC48TxCVS1DayTr_Type = Counter32
_TnSonetStatsOC48TxCVS1DayTr_Object = MibScalar
tnSonetStatsOC48TxCVS1DayTr = _TnSonetStatsOC48TxCVS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 53),
    _TnSonetStatsOC48TxCVS1DayTr_Type()
)
tnSonetStatsOC48TxCVS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC48TxCVS1DayTr.setStatus("current")
_TnSonetStatsOC12TxCVS1DayTr_Type = Counter32
_TnSonetStatsOC12TxCVS1DayTr_Object = MibScalar
tnSonetStatsOC12TxCVS1DayTr = _TnSonetStatsOC12TxCVS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 54),
    _TnSonetStatsOC12TxCVS1DayTr_Type()
)
tnSonetStatsOC12TxCVS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC12TxCVS1DayTr.setStatus("current")
_TnSonetStatsOC3TxCVS1DayTr_Type = Counter32
_TnSonetStatsOC3TxCVS1DayTr_Object = MibScalar
tnSonetStatsOC3TxCVS1DayTr = _TnSonetStatsOC3TxCVS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 55),
    _TnSonetStatsOC3TxCVS1DayTr_Type()
)
tnSonetStatsOC3TxCVS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC3TxCVS1DayTr.setStatus("current")
_TnSonetStatsTxESS1DayTr_Type = Counter32
_TnSonetStatsTxESS1DayTr_Object = MibScalar
tnSonetStatsTxESS1DayTr = _TnSonetStatsTxESS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 56),
    _TnSonetStatsTxESS1DayTr_Type()
)
tnSonetStatsTxESS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsTxESS1DayTr.setStatus("current")
_TnSonetStatsTxSESS1DayTr_Type = Counter32
_TnSonetStatsTxSESS1DayTr_Object = MibScalar
tnSonetStatsTxSESS1DayTr = _TnSonetStatsTxSESS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 57),
    _TnSonetStatsTxSESS1DayTr_Type()
)
tnSonetStatsTxSESS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsTxSESS1DayTr.setStatus("current")
_TnSonetStatsTxSEFSS1DayTr_Type = Counter32
_TnSonetStatsTxSEFSS1DayTr_Object = MibScalar
tnSonetStatsTxSEFSS1DayTr = _TnSonetStatsTxSEFSS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 58),
    _TnSonetStatsTxSEFSS1DayTr_Type()
)
tnSonetStatsTxSEFSS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsTxSEFSS1DayTr.setStatus("current")
_TnSonetStatsOC768TxCVL1DayTr_Type = Counter32
_TnSonetStatsOC768TxCVL1DayTr_Object = MibScalar
tnSonetStatsOC768TxCVL1DayTr = _TnSonetStatsOC768TxCVL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 59),
    _TnSonetStatsOC768TxCVL1DayTr_Type()
)
tnSonetStatsOC768TxCVL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC768TxCVL1DayTr.setStatus("current")
_TnSonetStatsOC192TxCVL1DayTr_Type = Counter32
_TnSonetStatsOC192TxCVL1DayTr_Object = MibScalar
tnSonetStatsOC192TxCVL1DayTr = _TnSonetStatsOC192TxCVL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 60),
    _TnSonetStatsOC192TxCVL1DayTr_Type()
)
tnSonetStatsOC192TxCVL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC192TxCVL1DayTr.setStatus("current")
_TnSonetStatsOC48TxCVL1DayTr_Type = Counter32
_TnSonetStatsOC48TxCVL1DayTr_Object = MibScalar
tnSonetStatsOC48TxCVL1DayTr = _TnSonetStatsOC48TxCVL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 61),
    _TnSonetStatsOC48TxCVL1DayTr_Type()
)
tnSonetStatsOC48TxCVL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC48TxCVL1DayTr.setStatus("current")
_TnSonetStatsOC12TxCVL1DayTr_Type = Counter32
_TnSonetStatsOC12TxCVL1DayTr_Object = MibScalar
tnSonetStatsOC12TxCVL1DayTr = _TnSonetStatsOC12TxCVL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 62),
    _TnSonetStatsOC12TxCVL1DayTr_Type()
)
tnSonetStatsOC12TxCVL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC12TxCVL1DayTr.setStatus("current")
_TnSonetStatsOC3TxCVL1DayTr_Type = Counter32
_TnSonetStatsOC3TxCVL1DayTr_Object = MibScalar
tnSonetStatsOC3TxCVL1DayTr = _TnSonetStatsOC3TxCVL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 63),
    _TnSonetStatsOC3TxCVL1DayTr_Type()
)
tnSonetStatsOC3TxCVL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC3TxCVL1DayTr.setStatus("current")
_TnSonetStatsTxESL1DayTr_Type = Counter32
_TnSonetStatsTxESL1DayTr_Object = MibScalar
tnSonetStatsTxESL1DayTr = _TnSonetStatsTxESL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 64),
    _TnSonetStatsTxESL1DayTr_Type()
)
tnSonetStatsTxESL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsTxESL1DayTr.setStatus("current")
_TnSonetStatsTxSESL1DayTr_Type = Counter32
_TnSonetStatsTxSESL1DayTr_Object = MibScalar
tnSonetStatsTxSESL1DayTr = _TnSonetStatsTxSESL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 65),
    _TnSonetStatsTxSESL1DayTr_Type()
)
tnSonetStatsTxSESL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsTxSESL1DayTr.setStatus("current")
_TnSonetStatsTxUASL1DayTr_Type = Counter32
_TnSonetStatsTxUASL1DayTr_Object = MibScalar
tnSonetStatsTxUASL1DayTr = _TnSonetStatsTxUASL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 66),
    _TnSonetStatsTxUASL1DayTr_Type()
)
tnSonetStatsTxUASL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsTxUASL1DayTr.setStatus("current")
_TnSonetStatsRxUASS1DayTr_Type = Counter32
_TnSonetStatsRxUASS1DayTr_Object = MibScalar
tnSonetStatsRxUASS1DayTr = _TnSonetStatsRxUASS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 67),
    _TnSonetStatsRxUASS1DayTr_Type()
)
tnSonetStatsRxUASS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsRxUASS1DayTr.setStatus("current")
_TnSonetStatsTxUASS1DayTr_Type = Counter32
_TnSonetStatsTxUASS1DayTr_Object = MibScalar
tnSonetStatsTxUASS1DayTr = _TnSonetStatsTxUASS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 68),
    _TnSonetStatsTxUASS1DayTr_Type()
)
tnSonetStatsTxUASS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsTxUASS1DayTr.setStatus("current")
_TnSonetStatsOC768RxFECVL15MinTr_Type = Counter32
_TnSonetStatsOC768RxFECVL15MinTr_Object = MibScalar
tnSonetStatsOC768RxFECVL15MinTr = _TnSonetStatsOC768RxFECVL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 69),
    _TnSonetStatsOC768RxFECVL15MinTr_Type()
)
tnSonetStatsOC768RxFECVL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC768RxFECVL15MinTr.setStatus("current")
_TnSonetStatsOC192RxFECVL15MinTr_Type = Counter32
_TnSonetStatsOC192RxFECVL15MinTr_Object = MibScalar
tnSonetStatsOC192RxFECVL15MinTr = _TnSonetStatsOC192RxFECVL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 70),
    _TnSonetStatsOC192RxFECVL15MinTr_Type()
)
tnSonetStatsOC192RxFECVL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC192RxFECVL15MinTr.setStatus("current")
_TnSonetStatsOC48RxFECVL15MinTr_Type = Counter32
_TnSonetStatsOC48RxFECVL15MinTr_Object = MibScalar
tnSonetStatsOC48RxFECVL15MinTr = _TnSonetStatsOC48RxFECVL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 71),
    _TnSonetStatsOC48RxFECVL15MinTr_Type()
)
tnSonetStatsOC48RxFECVL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC48RxFECVL15MinTr.setStatus("current")
_TnSonetStatsOC12RxFECVL15MinTr_Type = Counter32
_TnSonetStatsOC12RxFECVL15MinTr_Object = MibScalar
tnSonetStatsOC12RxFECVL15MinTr = _TnSonetStatsOC12RxFECVL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 72),
    _TnSonetStatsOC12RxFECVL15MinTr_Type()
)
tnSonetStatsOC12RxFECVL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC12RxFECVL15MinTr.setStatus("current")
_TnSonetStatsOC3RxFECVL15MinTr_Type = Counter32
_TnSonetStatsOC3RxFECVL15MinTr_Object = MibScalar
tnSonetStatsOC3RxFECVL15MinTr = _TnSonetStatsOC3RxFECVL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 73),
    _TnSonetStatsOC3RxFECVL15MinTr_Type()
)
tnSonetStatsOC3RxFECVL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC3RxFECVL15MinTr.setStatus("current")
_TnSonetStatsRxFEESL15MinTr_Type = Counter32
_TnSonetStatsRxFEESL15MinTr_Object = MibScalar
tnSonetStatsRxFEESL15MinTr = _TnSonetStatsRxFEESL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 74),
    _TnSonetStatsRxFEESL15MinTr_Type()
)
tnSonetStatsRxFEESL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsRxFEESL15MinTr.setStatus("current")
_TnSonetStatsRxFESESL15MinTr_Type = Counter32
_TnSonetStatsRxFESESL15MinTr_Object = MibScalar
tnSonetStatsRxFESESL15MinTr = _TnSonetStatsRxFESESL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 75),
    _TnSonetStatsRxFESESL15MinTr_Type()
)
tnSonetStatsRxFESESL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsRxFESESL15MinTr.setStatus("current")
_TnSonetStatsRxFEUASL15MinTr_Type = Counter32
_TnSonetStatsRxFEUASL15MinTr_Object = MibScalar
tnSonetStatsRxFEUASL15MinTr = _TnSonetStatsRxFEUASL15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 76),
    _TnSonetStatsRxFEUASL15MinTr_Type()
)
tnSonetStatsRxFEUASL15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsRxFEUASL15MinTr.setStatus("current")
_TnSonetStatsOC768RxFECVL1DayTr_Type = Counter32
_TnSonetStatsOC768RxFECVL1DayTr_Object = MibScalar
tnSonetStatsOC768RxFECVL1DayTr = _TnSonetStatsOC768RxFECVL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 77),
    _TnSonetStatsOC768RxFECVL1DayTr_Type()
)
tnSonetStatsOC768RxFECVL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC768RxFECVL1DayTr.setStatus("current")
_TnSonetStatsOC192RxFECVL1DayTr_Type = Counter32
_TnSonetStatsOC192RxFECVL1DayTr_Object = MibScalar
tnSonetStatsOC192RxFECVL1DayTr = _TnSonetStatsOC192RxFECVL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 78),
    _TnSonetStatsOC192RxFECVL1DayTr_Type()
)
tnSonetStatsOC192RxFECVL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC192RxFECVL1DayTr.setStatus("current")
_TnSonetStatsOC48RxFECVL1DayTr_Type = Counter32
_TnSonetStatsOC48RxFECVL1DayTr_Object = MibScalar
tnSonetStatsOC48RxFECVL1DayTr = _TnSonetStatsOC48RxFECVL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 79),
    _TnSonetStatsOC48RxFECVL1DayTr_Type()
)
tnSonetStatsOC48RxFECVL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC48RxFECVL1DayTr.setStatus("current")
_TnSonetStatsOC12RxFECVL1DayTr_Type = Counter32
_TnSonetStatsOC12RxFECVL1DayTr_Object = MibScalar
tnSonetStatsOC12RxFECVL1DayTr = _TnSonetStatsOC12RxFECVL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 80),
    _TnSonetStatsOC12RxFECVL1DayTr_Type()
)
tnSonetStatsOC12RxFECVL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC12RxFECVL1DayTr.setStatus("current")
_TnSonetStatsOC3RxFECVL1DayTr_Type = Counter32
_TnSonetStatsOC3RxFECVL1DayTr_Object = MibScalar
tnSonetStatsOC3RxFECVL1DayTr = _TnSonetStatsOC3RxFECVL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 81),
    _TnSonetStatsOC3RxFECVL1DayTr_Type()
)
tnSonetStatsOC3RxFECVL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsOC3RxFECVL1DayTr.setStatus("current")
_TnSonetStatsRxFEESL1DayTr_Type = Counter32
_TnSonetStatsRxFEESL1DayTr_Object = MibScalar
tnSonetStatsRxFEESL1DayTr = _TnSonetStatsRxFEESL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 82),
    _TnSonetStatsRxFEESL1DayTr_Type()
)
tnSonetStatsRxFEESL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsRxFEESL1DayTr.setStatus("current")
_TnSonetStatsRxFESESL1DayTr_Type = Counter32
_TnSonetStatsRxFESESL1DayTr_Object = MibScalar
tnSonetStatsRxFESESL1DayTr = _TnSonetStatsRxFESESL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 83),
    _TnSonetStatsRxFESESL1DayTr_Type()
)
tnSonetStatsRxFESESL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsRxFESESL1DayTr.setStatus("current")
_TnSonetStatsRxFEUASL1DayTr_Type = Counter32
_TnSonetStatsRxFEUASL1DayTr_Object = MibScalar
tnSonetStatsRxFEUASL1DayTr = _TnSonetStatsRxFEUASL1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 8, 84),
    _TnSonetStatsRxFEUASL1DayTr_Type()
)
tnSonetStatsRxFEUASL1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetStatsRxFEUASL1DayTr.setStatus("current")
_TnStatisticsSdhScalars_ObjectIdentity = ObjectIdentity
tnStatisticsSdhScalars = _TnStatisticsSdhScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9)
)
_TnSdhStatsSTM256RxRSEB15MinTr_Type = Counter32
_TnSdhStatsSTM256RxRSEB15MinTr_Object = MibScalar
tnSdhStatsSTM256RxRSEB15MinTr = _TnSdhStatsSTM256RxRSEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 1),
    _TnSdhStatsSTM256RxRSEB15MinTr_Type()
)
tnSdhStatsSTM256RxRSEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM256RxRSEB15MinTr.setStatus("current")
_TnSdhStatsSTM64RxRSEB15MinTr_Type = Counter32
_TnSdhStatsSTM64RxRSEB15MinTr_Object = MibScalar
tnSdhStatsSTM64RxRSEB15MinTr = _TnSdhStatsSTM64RxRSEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 2),
    _TnSdhStatsSTM64RxRSEB15MinTr_Type()
)
tnSdhStatsSTM64RxRSEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM64RxRSEB15MinTr.setStatus("current")
_TnSdhStatsSTM16RxRSEB15MinTr_Type = Counter32
_TnSdhStatsSTM16RxRSEB15MinTr_Object = MibScalar
tnSdhStatsSTM16RxRSEB15MinTr = _TnSdhStatsSTM16RxRSEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 3),
    _TnSdhStatsSTM16RxRSEB15MinTr_Type()
)
tnSdhStatsSTM16RxRSEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM16RxRSEB15MinTr.setStatus("current")
_TnSdhStatsSTM4RxRSEB15MinTr_Type = Counter32
_TnSdhStatsSTM4RxRSEB15MinTr_Object = MibScalar
tnSdhStatsSTM4RxRSEB15MinTr = _TnSdhStatsSTM4RxRSEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 4),
    _TnSdhStatsSTM4RxRSEB15MinTr_Type()
)
tnSdhStatsSTM4RxRSEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM4RxRSEB15MinTr.setStatus("current")
_TnSdhStatsSTM1RxRSEB15MinTr_Type = Counter32
_TnSdhStatsSTM1RxRSEB15MinTr_Object = MibScalar
tnSdhStatsSTM1RxRSEB15MinTr = _TnSdhStatsSTM1RxRSEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 5),
    _TnSdhStatsSTM1RxRSEB15MinTr_Type()
)
tnSdhStatsSTM1RxRSEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM1RxRSEB15MinTr.setStatus("current")
_TnSdhStatsRxRSES15MinTr_Type = Counter32
_TnSdhStatsRxRSES15MinTr_Object = MibScalar
tnSdhStatsRxRSES15MinTr = _TnSdhStatsRxRSES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 6),
    _TnSdhStatsRxRSES15MinTr_Type()
)
tnSdhStatsRxRSES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxRSES15MinTr.setStatus("current")
_TnSdhStatsRxRSSES15MinTr_Type = Counter32
_TnSdhStatsRxRSSES15MinTr_Object = MibScalar
tnSdhStatsRxRSSES15MinTr = _TnSdhStatsRxRSSES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 7),
    _TnSdhStatsRxRSSES15MinTr_Type()
)
tnSdhStatsRxRSSES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxRSSES15MinTr.setStatus("current")
_TnSdhStatsSTM256RxMSEB15MinTr_Type = Counter32
_TnSdhStatsSTM256RxMSEB15MinTr_Object = MibScalar
tnSdhStatsSTM256RxMSEB15MinTr = _TnSdhStatsSTM256RxMSEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 8),
    _TnSdhStatsSTM256RxMSEB15MinTr_Type()
)
tnSdhStatsSTM256RxMSEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM256RxMSEB15MinTr.setStatus("current")
_TnSdhStatsSTM64RxMSEB15MinTr_Type = Counter32
_TnSdhStatsSTM64RxMSEB15MinTr_Object = MibScalar
tnSdhStatsSTM64RxMSEB15MinTr = _TnSdhStatsSTM64RxMSEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 9),
    _TnSdhStatsSTM64RxMSEB15MinTr_Type()
)
tnSdhStatsSTM64RxMSEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM64RxMSEB15MinTr.setStatus("current")
_TnSdhStatsSTM16RxMSEB15MinTr_Type = Counter32
_TnSdhStatsSTM16RxMSEB15MinTr_Object = MibScalar
tnSdhStatsSTM16RxMSEB15MinTr = _TnSdhStatsSTM16RxMSEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 10),
    _TnSdhStatsSTM16RxMSEB15MinTr_Type()
)
tnSdhStatsSTM16RxMSEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM16RxMSEB15MinTr.setStatus("current")
_TnSdhStatsSTM4RxMSEB15MinTr_Type = Counter32
_TnSdhStatsSTM4RxMSEB15MinTr_Object = MibScalar
tnSdhStatsSTM4RxMSEB15MinTr = _TnSdhStatsSTM4RxMSEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 11),
    _TnSdhStatsSTM4RxMSEB15MinTr_Type()
)
tnSdhStatsSTM4RxMSEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM4RxMSEB15MinTr.setStatus("current")
_TnSdhStatsSTM1RxMSEB15MinTr_Type = Counter32
_TnSdhStatsSTM1RxMSEB15MinTr_Object = MibScalar
tnSdhStatsSTM1RxMSEB15MinTr = _TnSdhStatsSTM1RxMSEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 12),
    _TnSdhStatsSTM1RxMSEB15MinTr_Type()
)
tnSdhStatsSTM1RxMSEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM1RxMSEB15MinTr.setStatus("current")
_TnSdhStatsRxMSES15MinTr_Type = Counter32
_TnSdhStatsRxMSES15MinTr_Object = MibScalar
tnSdhStatsRxMSES15MinTr = _TnSdhStatsRxMSES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 13),
    _TnSdhStatsRxMSES15MinTr_Type()
)
tnSdhStatsRxMSES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxMSES15MinTr.setStatus("current")
_TnSdhStatsRxMSSES15MinTr_Type = Counter32
_TnSdhStatsRxMSSES15MinTr_Object = MibScalar
tnSdhStatsRxMSSES15MinTr = _TnSdhStatsRxMSSES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 14),
    _TnSdhStatsRxMSSES15MinTr_Type()
)
tnSdhStatsRxMSSES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxMSSES15MinTr.setStatus("current")
_TnSdhStatsRxMSUAS15MinTr_Type = Counter32
_TnSdhStatsRxMSUAS15MinTr_Object = MibScalar
tnSdhStatsRxMSUAS15MinTr = _TnSdhStatsRxMSUAS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 15),
    _TnSdhStatsRxMSUAS15MinTr_Type()
)
tnSdhStatsRxMSUAS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxMSUAS15MinTr.setStatus("current")
_TnSdhStatsSTM256TxRSEB15MinTr_Type = Counter32
_TnSdhStatsSTM256TxRSEB15MinTr_Object = MibScalar
tnSdhStatsSTM256TxRSEB15MinTr = _TnSdhStatsSTM256TxRSEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 16),
    _TnSdhStatsSTM256TxRSEB15MinTr_Type()
)
tnSdhStatsSTM256TxRSEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM256TxRSEB15MinTr.setStatus("current")
_TnSdhStatsSTM64TxRSEB15MinTr_Type = Counter32
_TnSdhStatsSTM64TxRSEB15MinTr_Object = MibScalar
tnSdhStatsSTM64TxRSEB15MinTr = _TnSdhStatsSTM64TxRSEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 17),
    _TnSdhStatsSTM64TxRSEB15MinTr_Type()
)
tnSdhStatsSTM64TxRSEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM64TxRSEB15MinTr.setStatus("current")
_TnSdhStatsSTM16TxRSEB15MinTr_Type = Counter32
_TnSdhStatsSTM16TxRSEB15MinTr_Object = MibScalar
tnSdhStatsSTM16TxRSEB15MinTr = _TnSdhStatsSTM16TxRSEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 18),
    _TnSdhStatsSTM16TxRSEB15MinTr_Type()
)
tnSdhStatsSTM16TxRSEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM16TxRSEB15MinTr.setStatus("current")
_TnSdhStatsSTM4TxRSEB15MinTr_Type = Counter32
_TnSdhStatsSTM4TxRSEB15MinTr_Object = MibScalar
tnSdhStatsSTM4TxRSEB15MinTr = _TnSdhStatsSTM4TxRSEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 19),
    _TnSdhStatsSTM4TxRSEB15MinTr_Type()
)
tnSdhStatsSTM4TxRSEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM4TxRSEB15MinTr.setStatus("current")
_TnSdhStatsSTM1TxRSEB15MinTr_Type = Counter32
_TnSdhStatsSTM1TxRSEB15MinTr_Object = MibScalar
tnSdhStatsSTM1TxRSEB15MinTr = _TnSdhStatsSTM1TxRSEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 20),
    _TnSdhStatsSTM1TxRSEB15MinTr_Type()
)
tnSdhStatsSTM1TxRSEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM1TxRSEB15MinTr.setStatus("current")
_TnSdhStatsTxRSES15MinTr_Type = Counter32
_TnSdhStatsTxRSES15MinTr_Object = MibScalar
tnSdhStatsTxRSES15MinTr = _TnSdhStatsTxRSES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 21),
    _TnSdhStatsTxRSES15MinTr_Type()
)
tnSdhStatsTxRSES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsTxRSES15MinTr.setStatus("current")
_TnSdhStatsTxRSSES15MinTr_Type = Counter32
_TnSdhStatsTxRSSES15MinTr_Object = MibScalar
tnSdhStatsTxRSSES15MinTr = _TnSdhStatsTxRSSES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 22),
    _TnSdhStatsTxRSSES15MinTr_Type()
)
tnSdhStatsTxRSSES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsTxRSSES15MinTr.setStatus("current")
_TnSdhStatsSTM256TxMSEB15MinTr_Type = Counter32
_TnSdhStatsSTM256TxMSEB15MinTr_Object = MibScalar
tnSdhStatsSTM256TxMSEB15MinTr = _TnSdhStatsSTM256TxMSEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 23),
    _TnSdhStatsSTM256TxMSEB15MinTr_Type()
)
tnSdhStatsSTM256TxMSEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM256TxMSEB15MinTr.setStatus("current")
_TnSdhStatsSTM64TxMSEB15MinTr_Type = Counter32
_TnSdhStatsSTM64TxMSEB15MinTr_Object = MibScalar
tnSdhStatsSTM64TxMSEB15MinTr = _TnSdhStatsSTM64TxMSEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 24),
    _TnSdhStatsSTM64TxMSEB15MinTr_Type()
)
tnSdhStatsSTM64TxMSEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM64TxMSEB15MinTr.setStatus("current")
_TnSdhStatsSTM16TxMSEB15MinTr_Type = Counter32
_TnSdhStatsSTM16TxMSEB15MinTr_Object = MibScalar
tnSdhStatsSTM16TxMSEB15MinTr = _TnSdhStatsSTM16TxMSEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 25),
    _TnSdhStatsSTM16TxMSEB15MinTr_Type()
)
tnSdhStatsSTM16TxMSEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM16TxMSEB15MinTr.setStatus("current")
_TnSdhStatsSTM4TxMSEB15MinTr_Type = Counter32
_TnSdhStatsSTM4TxMSEB15MinTr_Object = MibScalar
tnSdhStatsSTM4TxMSEB15MinTr = _TnSdhStatsSTM4TxMSEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 26),
    _TnSdhStatsSTM4TxMSEB15MinTr_Type()
)
tnSdhStatsSTM4TxMSEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM4TxMSEB15MinTr.setStatus("current")
_TnSdhStatsSTM1TxMSEB15MinTr_Type = Counter32
_TnSdhStatsSTM1TxMSEB15MinTr_Object = MibScalar
tnSdhStatsSTM1TxMSEB15MinTr = _TnSdhStatsSTM1TxMSEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 27),
    _TnSdhStatsSTM1TxMSEB15MinTr_Type()
)
tnSdhStatsSTM1TxMSEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM1TxMSEB15MinTr.setStatus("current")
_TnSdhStatsTxMSES15MinTr_Type = Counter32
_TnSdhStatsTxMSES15MinTr_Object = MibScalar
tnSdhStatsTxMSES15MinTr = _TnSdhStatsTxMSES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 28),
    _TnSdhStatsTxMSES15MinTr_Type()
)
tnSdhStatsTxMSES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsTxMSES15MinTr.setStatus("current")
_TnSdhStatsTxMSSES15MinTr_Type = Counter32
_TnSdhStatsTxMSSES15MinTr_Object = MibScalar
tnSdhStatsTxMSSES15MinTr = _TnSdhStatsTxMSSES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 29),
    _TnSdhStatsTxMSSES15MinTr_Type()
)
tnSdhStatsTxMSSES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsTxMSSES15MinTr.setStatus("current")
_TnSdhStatsTxMSUAS15MinTr_Type = Counter32
_TnSdhStatsTxMSUAS15MinTr_Object = MibScalar
tnSdhStatsTxMSUAS15MinTr = _TnSdhStatsTxMSUAS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 30),
    _TnSdhStatsTxMSUAS15MinTr_Type()
)
tnSdhStatsTxMSUAS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsTxMSUAS15MinTr.setStatus("current")
_TnSdhStatsRxRSUAS15MinTr_Type = Counter32
_TnSdhStatsRxRSUAS15MinTr_Object = MibScalar
tnSdhStatsRxRSUAS15MinTr = _TnSdhStatsRxRSUAS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 31),
    _TnSdhStatsRxRSUAS15MinTr_Type()
)
tnSdhStatsRxRSUAS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxRSUAS15MinTr.setStatus("current")
_TnSdhStatsTxRSUAS15MinTr_Type = Counter32
_TnSdhStatsTxRSUAS15MinTr_Object = MibScalar
tnSdhStatsTxRSUAS15MinTr = _TnSdhStatsTxRSUAS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 32),
    _TnSdhStatsTxRSUAS15MinTr_Type()
)
tnSdhStatsTxRSUAS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsTxRSUAS15MinTr.setStatus("current")
_TnSdhStatsSTM256RxRSEB1DayTr_Type = Counter32
_TnSdhStatsSTM256RxRSEB1DayTr_Object = MibScalar
tnSdhStatsSTM256RxRSEB1DayTr = _TnSdhStatsSTM256RxRSEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 33),
    _TnSdhStatsSTM256RxRSEB1DayTr_Type()
)
tnSdhStatsSTM256RxRSEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM256RxRSEB1DayTr.setStatus("current")
_TnSdhStatsSTM64RxRSEB1DayTr_Type = Counter32
_TnSdhStatsSTM64RxRSEB1DayTr_Object = MibScalar
tnSdhStatsSTM64RxRSEB1DayTr = _TnSdhStatsSTM64RxRSEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 34),
    _TnSdhStatsSTM64RxRSEB1DayTr_Type()
)
tnSdhStatsSTM64RxRSEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM64RxRSEB1DayTr.setStatus("current")
_TnSdhStatsSTM16RxRSEB1DayTr_Type = Counter32
_TnSdhStatsSTM16RxRSEB1DayTr_Object = MibScalar
tnSdhStatsSTM16RxRSEB1DayTr = _TnSdhStatsSTM16RxRSEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 35),
    _TnSdhStatsSTM16RxRSEB1DayTr_Type()
)
tnSdhStatsSTM16RxRSEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM16RxRSEB1DayTr.setStatus("current")
_TnSdhStatsSTM4RxRSEB1DayTr_Type = Counter32
_TnSdhStatsSTM4RxRSEB1DayTr_Object = MibScalar
tnSdhStatsSTM4RxRSEB1DayTr = _TnSdhStatsSTM4RxRSEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 36),
    _TnSdhStatsSTM4RxRSEB1DayTr_Type()
)
tnSdhStatsSTM4RxRSEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM4RxRSEB1DayTr.setStatus("current")
_TnSdhStatsSTM1RxRSEB1DayTr_Type = Counter32
_TnSdhStatsSTM1RxRSEB1DayTr_Object = MibScalar
tnSdhStatsSTM1RxRSEB1DayTr = _TnSdhStatsSTM1RxRSEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 37),
    _TnSdhStatsSTM1RxRSEB1DayTr_Type()
)
tnSdhStatsSTM1RxRSEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM1RxRSEB1DayTr.setStatus("current")
_TnSdhStatsRxRSES1DayTr_Type = Counter32
_TnSdhStatsRxRSES1DayTr_Object = MibScalar
tnSdhStatsRxRSES1DayTr = _TnSdhStatsRxRSES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 38),
    _TnSdhStatsRxRSES1DayTr_Type()
)
tnSdhStatsRxRSES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxRSES1DayTr.setStatus("current")
_TnSdhStatsRxRSSES1DayTr_Type = Counter32
_TnSdhStatsRxRSSES1DayTr_Object = MibScalar
tnSdhStatsRxRSSES1DayTr = _TnSdhStatsRxRSSES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 39),
    _TnSdhStatsRxRSSES1DayTr_Type()
)
tnSdhStatsRxRSSES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxRSSES1DayTr.setStatus("current")
_TnSdhStatsSTM256RxMSEB1DayTr_Type = Counter32
_TnSdhStatsSTM256RxMSEB1DayTr_Object = MibScalar
tnSdhStatsSTM256RxMSEB1DayTr = _TnSdhStatsSTM256RxMSEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 40),
    _TnSdhStatsSTM256RxMSEB1DayTr_Type()
)
tnSdhStatsSTM256RxMSEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM256RxMSEB1DayTr.setStatus("current")
_TnSdhStatsSTM64RxMSEB1DayTr_Type = Counter32
_TnSdhStatsSTM64RxMSEB1DayTr_Object = MibScalar
tnSdhStatsSTM64RxMSEB1DayTr = _TnSdhStatsSTM64RxMSEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 41),
    _TnSdhStatsSTM64RxMSEB1DayTr_Type()
)
tnSdhStatsSTM64RxMSEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM64RxMSEB1DayTr.setStatus("current")
_TnSdhStatsSTM16RxMSEB1DayTr_Type = Counter32
_TnSdhStatsSTM16RxMSEB1DayTr_Object = MibScalar
tnSdhStatsSTM16RxMSEB1DayTr = _TnSdhStatsSTM16RxMSEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 42),
    _TnSdhStatsSTM16RxMSEB1DayTr_Type()
)
tnSdhStatsSTM16RxMSEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM16RxMSEB1DayTr.setStatus("current")
_TnSdhStatsSTM4RxMSEB1DayTr_Type = Counter32
_TnSdhStatsSTM4RxMSEB1DayTr_Object = MibScalar
tnSdhStatsSTM4RxMSEB1DayTr = _TnSdhStatsSTM4RxMSEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 43),
    _TnSdhStatsSTM4RxMSEB1DayTr_Type()
)
tnSdhStatsSTM4RxMSEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM4RxMSEB1DayTr.setStatus("current")
_TnSdhStatsSTM1RxMSEB1DayTr_Type = Counter32
_TnSdhStatsSTM1RxMSEB1DayTr_Object = MibScalar
tnSdhStatsSTM1RxMSEB1DayTr = _TnSdhStatsSTM1RxMSEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 44),
    _TnSdhStatsSTM1RxMSEB1DayTr_Type()
)
tnSdhStatsSTM1RxMSEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM1RxMSEB1DayTr.setStatus("current")
_TnSdhStatsRxMSES1DayTr_Type = Counter32
_TnSdhStatsRxMSES1DayTr_Object = MibScalar
tnSdhStatsRxMSES1DayTr = _TnSdhStatsRxMSES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 45),
    _TnSdhStatsRxMSES1DayTr_Type()
)
tnSdhStatsRxMSES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxMSES1DayTr.setStatus("current")
_TnSdhStatsRxMSSES1DayTr_Type = Counter32
_TnSdhStatsRxMSSES1DayTr_Object = MibScalar
tnSdhStatsRxMSSES1DayTr = _TnSdhStatsRxMSSES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 46),
    _TnSdhStatsRxMSSES1DayTr_Type()
)
tnSdhStatsRxMSSES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxMSSES1DayTr.setStatus("current")
_TnSdhStatsRxMSUAS1DayTr_Type = Counter32
_TnSdhStatsRxMSUAS1DayTr_Object = MibScalar
tnSdhStatsRxMSUAS1DayTr = _TnSdhStatsRxMSUAS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 47),
    _TnSdhStatsRxMSUAS1DayTr_Type()
)
tnSdhStatsRxMSUAS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxMSUAS1DayTr.setStatus("current")
_TnSdhStatsSTM256TxRSEB1DayTr_Type = Counter32
_TnSdhStatsSTM256TxRSEB1DayTr_Object = MibScalar
tnSdhStatsSTM256TxRSEB1DayTr = _TnSdhStatsSTM256TxRSEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 48),
    _TnSdhStatsSTM256TxRSEB1DayTr_Type()
)
tnSdhStatsSTM256TxRSEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM256TxRSEB1DayTr.setStatus("current")
_TnSdhStatsSTM64TxRSEB1DayTr_Type = Counter32
_TnSdhStatsSTM64TxRSEB1DayTr_Object = MibScalar
tnSdhStatsSTM64TxRSEB1DayTr = _TnSdhStatsSTM64TxRSEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 49),
    _TnSdhStatsSTM64TxRSEB1DayTr_Type()
)
tnSdhStatsSTM64TxRSEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM64TxRSEB1DayTr.setStatus("current")
_TnSdhStatsSTM16TxRSEB1DayTr_Type = Counter32
_TnSdhStatsSTM16TxRSEB1DayTr_Object = MibScalar
tnSdhStatsSTM16TxRSEB1DayTr = _TnSdhStatsSTM16TxRSEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 50),
    _TnSdhStatsSTM16TxRSEB1DayTr_Type()
)
tnSdhStatsSTM16TxRSEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM16TxRSEB1DayTr.setStatus("current")
_TnSdhStatsSTM4TxRSEB1DayTr_Type = Counter32
_TnSdhStatsSTM4TxRSEB1DayTr_Object = MibScalar
tnSdhStatsSTM4TxRSEB1DayTr = _TnSdhStatsSTM4TxRSEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 51),
    _TnSdhStatsSTM4TxRSEB1DayTr_Type()
)
tnSdhStatsSTM4TxRSEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM4TxRSEB1DayTr.setStatus("current")
_TnSdhStatsSTM1TxRSEB1DayTr_Type = Counter32
_TnSdhStatsSTM1TxRSEB1DayTr_Object = MibScalar
tnSdhStatsSTM1TxRSEB1DayTr = _TnSdhStatsSTM1TxRSEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 52),
    _TnSdhStatsSTM1TxRSEB1DayTr_Type()
)
tnSdhStatsSTM1TxRSEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM1TxRSEB1DayTr.setStatus("current")
_TnSdhStatsTxRSES1DayTr_Type = Counter32
_TnSdhStatsTxRSES1DayTr_Object = MibScalar
tnSdhStatsTxRSES1DayTr = _TnSdhStatsTxRSES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 53),
    _TnSdhStatsTxRSES1DayTr_Type()
)
tnSdhStatsTxRSES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsTxRSES1DayTr.setStatus("current")
_TnSdhStatsTxRSSES1DayTr_Type = Counter32
_TnSdhStatsTxRSSES1DayTr_Object = MibScalar
tnSdhStatsTxRSSES1DayTr = _TnSdhStatsTxRSSES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 54),
    _TnSdhStatsTxRSSES1DayTr_Type()
)
tnSdhStatsTxRSSES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsTxRSSES1DayTr.setStatus("current")
_TnSdhStatsSTM256TxMSEB1DayTr_Type = Counter32
_TnSdhStatsSTM256TxMSEB1DayTr_Object = MibScalar
tnSdhStatsSTM256TxMSEB1DayTr = _TnSdhStatsSTM256TxMSEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 55),
    _TnSdhStatsSTM256TxMSEB1DayTr_Type()
)
tnSdhStatsSTM256TxMSEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM256TxMSEB1DayTr.setStatus("current")
_TnSdhStatsSTM64TxMSEB1DayTr_Type = Counter32
_TnSdhStatsSTM64TxMSEB1DayTr_Object = MibScalar
tnSdhStatsSTM64TxMSEB1DayTr = _TnSdhStatsSTM64TxMSEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 56),
    _TnSdhStatsSTM64TxMSEB1DayTr_Type()
)
tnSdhStatsSTM64TxMSEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM64TxMSEB1DayTr.setStatus("current")
_TnSdhStatsSTM16TxMSEB1DayTr_Type = Counter32
_TnSdhStatsSTM16TxMSEB1DayTr_Object = MibScalar
tnSdhStatsSTM16TxMSEB1DayTr = _TnSdhStatsSTM16TxMSEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 57),
    _TnSdhStatsSTM16TxMSEB1DayTr_Type()
)
tnSdhStatsSTM16TxMSEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM16TxMSEB1DayTr.setStatus("current")
_TnSdhStatsSTM4TxMSEB1DayTr_Type = Counter32
_TnSdhStatsSTM4TxMSEB1DayTr_Object = MibScalar
tnSdhStatsSTM4TxMSEB1DayTr = _TnSdhStatsSTM4TxMSEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 58),
    _TnSdhStatsSTM4TxMSEB1DayTr_Type()
)
tnSdhStatsSTM4TxMSEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM4TxMSEB1DayTr.setStatus("current")
_TnSdhStatsSTM1TxMSEB1DayTr_Type = Counter32
_TnSdhStatsSTM1TxMSEB1DayTr_Object = MibScalar
tnSdhStatsSTM1TxMSEB1DayTr = _TnSdhStatsSTM1TxMSEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 59),
    _TnSdhStatsSTM1TxMSEB1DayTr_Type()
)
tnSdhStatsSTM1TxMSEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM1TxMSEB1DayTr.setStatus("current")
_TnSdhStatsTxMSES1DayTr_Type = Counter32
_TnSdhStatsTxMSES1DayTr_Object = MibScalar
tnSdhStatsTxMSES1DayTr = _TnSdhStatsTxMSES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 60),
    _TnSdhStatsTxMSES1DayTr_Type()
)
tnSdhStatsTxMSES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsTxMSES1DayTr.setStatus("current")
_TnSdhStatsTxMSSES1DayTr_Type = Counter32
_TnSdhStatsTxMSSES1DayTr_Object = MibScalar
tnSdhStatsTxMSSES1DayTr = _TnSdhStatsTxMSSES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 61),
    _TnSdhStatsTxMSSES1DayTr_Type()
)
tnSdhStatsTxMSSES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsTxMSSES1DayTr.setStatus("current")
_TnSdhStatsTxMSUAS1DayTr_Type = Counter32
_TnSdhStatsTxMSUAS1DayTr_Object = MibScalar
tnSdhStatsTxMSUAS1DayTr = _TnSdhStatsTxMSUAS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 62),
    _TnSdhStatsTxMSUAS1DayTr_Type()
)
tnSdhStatsTxMSUAS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsTxMSUAS1DayTr.setStatus("current")
_TnSdhStatsRxRSUAS1DayTr_Type = Counter32
_TnSdhStatsRxRSUAS1DayTr_Object = MibScalar
tnSdhStatsRxRSUAS1DayTr = _TnSdhStatsRxRSUAS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 63),
    _TnSdhStatsRxRSUAS1DayTr_Type()
)
tnSdhStatsRxRSUAS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxRSUAS1DayTr.setStatus("current")
_TnSdhStatsTxRSUAS1DayTr_Type = Counter32
_TnSdhStatsTxRSUAS1DayTr_Object = MibScalar
tnSdhStatsTxRSUAS1DayTr = _TnSdhStatsTxRSUAS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 64),
    _TnSdhStatsTxRSUAS1DayTr_Type()
)
tnSdhStatsTxRSUAS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsTxRSUAS1DayTr.setStatus("current")
_TnSdhStatsSTM256RxRSEB15MinRtr_Type = Counter32
_TnSdhStatsSTM256RxRSEB15MinRtr_Object = MibScalar
tnSdhStatsSTM256RxRSEB15MinRtr = _TnSdhStatsSTM256RxRSEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 65),
    _TnSdhStatsSTM256RxRSEB15MinRtr_Type()
)
tnSdhStatsSTM256RxRSEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM256RxRSEB15MinRtr.setStatus("current")
_TnSdhStatsSTM64RxRSEB15MinRtr_Type = Counter32
_TnSdhStatsSTM64RxRSEB15MinRtr_Object = MibScalar
tnSdhStatsSTM64RxRSEB15MinRtr = _TnSdhStatsSTM64RxRSEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 66),
    _TnSdhStatsSTM64RxRSEB15MinRtr_Type()
)
tnSdhStatsSTM64RxRSEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM64RxRSEB15MinRtr.setStatus("current")
_TnSdhStatsSTM16RxRSEB15MinRtr_Type = Counter32
_TnSdhStatsSTM16RxRSEB15MinRtr_Object = MibScalar
tnSdhStatsSTM16RxRSEB15MinRtr = _TnSdhStatsSTM16RxRSEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 67),
    _TnSdhStatsSTM16RxRSEB15MinRtr_Type()
)
tnSdhStatsSTM16RxRSEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM16RxRSEB15MinRtr.setStatus("current")
_TnSdhStatsSTM4RxRSEB15MinRtr_Type = Counter32
_TnSdhStatsSTM4RxRSEB15MinRtr_Object = MibScalar
tnSdhStatsSTM4RxRSEB15MinRtr = _TnSdhStatsSTM4RxRSEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 68),
    _TnSdhStatsSTM4RxRSEB15MinRtr_Type()
)
tnSdhStatsSTM4RxRSEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM4RxRSEB15MinRtr.setStatus("current")
_TnSdhStatsSTM1RxRSEB15MinRtr_Type = Counter32
_TnSdhStatsSTM1RxRSEB15MinRtr_Object = MibScalar
tnSdhStatsSTM1RxRSEB15MinRtr = _TnSdhStatsSTM1RxRSEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 69),
    _TnSdhStatsSTM1RxRSEB15MinRtr_Type()
)
tnSdhStatsSTM1RxRSEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM1RxRSEB15MinRtr.setStatus("current")
_TnSdhStatsRxRSES15MinRtr_Type = Counter32
_TnSdhStatsRxRSES15MinRtr_Object = MibScalar
tnSdhStatsRxRSES15MinRtr = _TnSdhStatsRxRSES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 70),
    _TnSdhStatsRxRSES15MinRtr_Type()
)
tnSdhStatsRxRSES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxRSES15MinRtr.setStatus("current")
_TnSdhStatsRxRSSES15MinRtr_Type = Counter32
_TnSdhStatsRxRSSES15MinRtr_Object = MibScalar
tnSdhStatsRxRSSES15MinRtr = _TnSdhStatsRxRSSES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 71),
    _TnSdhStatsRxRSSES15MinRtr_Type()
)
tnSdhStatsRxRSSES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxRSSES15MinRtr.setStatus("current")
_TnSdhStatsSTM256RxMSEB15MinRtr_Type = Counter32
_TnSdhStatsSTM256RxMSEB15MinRtr_Object = MibScalar
tnSdhStatsSTM256RxMSEB15MinRtr = _TnSdhStatsSTM256RxMSEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 72),
    _TnSdhStatsSTM256RxMSEB15MinRtr_Type()
)
tnSdhStatsSTM256RxMSEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM256RxMSEB15MinRtr.setStatus("current")
_TnSdhStatsSTM64RxMSEB15MinRtr_Type = Counter32
_TnSdhStatsSTM64RxMSEB15MinRtr_Object = MibScalar
tnSdhStatsSTM64RxMSEB15MinRtr = _TnSdhStatsSTM64RxMSEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 73),
    _TnSdhStatsSTM64RxMSEB15MinRtr_Type()
)
tnSdhStatsSTM64RxMSEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM64RxMSEB15MinRtr.setStatus("current")
_TnSdhStatsSTM16RxMSEB15MinRtr_Type = Counter32
_TnSdhStatsSTM16RxMSEB15MinRtr_Object = MibScalar
tnSdhStatsSTM16RxMSEB15MinRtr = _TnSdhStatsSTM16RxMSEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 74),
    _TnSdhStatsSTM16RxMSEB15MinRtr_Type()
)
tnSdhStatsSTM16RxMSEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM16RxMSEB15MinRtr.setStatus("current")
_TnSdhStatsSTM4RxMSEB15MinRtr_Type = Counter32
_TnSdhStatsSTM4RxMSEB15MinRtr_Object = MibScalar
tnSdhStatsSTM4RxMSEB15MinRtr = _TnSdhStatsSTM4RxMSEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 75),
    _TnSdhStatsSTM4RxMSEB15MinRtr_Type()
)
tnSdhStatsSTM4RxMSEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM4RxMSEB15MinRtr.setStatus("current")
_TnSdhStatsSTM1RxMSEB15MinRtr_Type = Counter32
_TnSdhStatsSTM1RxMSEB15MinRtr_Object = MibScalar
tnSdhStatsSTM1RxMSEB15MinRtr = _TnSdhStatsSTM1RxMSEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 76),
    _TnSdhStatsSTM1RxMSEB15MinRtr_Type()
)
tnSdhStatsSTM1RxMSEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM1RxMSEB15MinRtr.setStatus("current")
_TnSdhStatsRxMSES15MinRtr_Type = Counter32
_TnSdhStatsRxMSES15MinRtr_Object = MibScalar
tnSdhStatsRxMSES15MinRtr = _TnSdhStatsRxMSES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 77),
    _TnSdhStatsRxMSES15MinRtr_Type()
)
tnSdhStatsRxMSES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxMSES15MinRtr.setStatus("current")
_TnSdhStatsRxMSSES15MinRtr_Type = Counter32
_TnSdhStatsRxMSSES15MinRtr_Object = MibScalar
tnSdhStatsRxMSSES15MinRtr = _TnSdhStatsRxMSSES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 78),
    _TnSdhStatsRxMSSES15MinRtr_Type()
)
tnSdhStatsRxMSSES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxMSSES15MinRtr.setStatus("current")
_TnSdhStatsRxMSUAS15MinRtr_Type = Counter32
_TnSdhStatsRxMSUAS15MinRtr_Object = MibScalar
tnSdhStatsRxMSUAS15MinRtr = _TnSdhStatsRxMSUAS15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 79),
    _TnSdhStatsRxMSUAS15MinRtr_Type()
)
tnSdhStatsRxMSUAS15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxMSUAS15MinRtr.setStatus("current")
_TnSdhStatsSTM256TxRSEB15MinRtr_Type = Counter32
_TnSdhStatsSTM256TxRSEB15MinRtr_Object = MibScalar
tnSdhStatsSTM256TxRSEB15MinRtr = _TnSdhStatsSTM256TxRSEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 80),
    _TnSdhStatsSTM256TxRSEB15MinRtr_Type()
)
tnSdhStatsSTM256TxRSEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM256TxRSEB15MinRtr.setStatus("current")
_TnSdhStatsSTM64TxRSEB15MinRtr_Type = Counter32
_TnSdhStatsSTM64TxRSEB15MinRtr_Object = MibScalar
tnSdhStatsSTM64TxRSEB15MinRtr = _TnSdhStatsSTM64TxRSEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 81),
    _TnSdhStatsSTM64TxRSEB15MinRtr_Type()
)
tnSdhStatsSTM64TxRSEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM64TxRSEB15MinRtr.setStatus("current")
_TnSdhStatsSTM16TxRSEB15MinRtr_Type = Counter32
_TnSdhStatsSTM16TxRSEB15MinRtr_Object = MibScalar
tnSdhStatsSTM16TxRSEB15MinRtr = _TnSdhStatsSTM16TxRSEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 82),
    _TnSdhStatsSTM16TxRSEB15MinRtr_Type()
)
tnSdhStatsSTM16TxRSEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM16TxRSEB15MinRtr.setStatus("current")
_TnSdhStatsSTM4TxRSEB15MinRtr_Type = Counter32
_TnSdhStatsSTM4TxRSEB15MinRtr_Object = MibScalar
tnSdhStatsSTM4TxRSEB15MinRtr = _TnSdhStatsSTM4TxRSEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 83),
    _TnSdhStatsSTM4TxRSEB15MinRtr_Type()
)
tnSdhStatsSTM4TxRSEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM4TxRSEB15MinRtr.setStatus("current")
_TnSdhStatsSTM1TxRSEB15MinRtr_Type = Counter32
_TnSdhStatsSTM1TxRSEB15MinRtr_Object = MibScalar
tnSdhStatsSTM1TxRSEB15MinRtr = _TnSdhStatsSTM1TxRSEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 84),
    _TnSdhStatsSTM1TxRSEB15MinRtr_Type()
)
tnSdhStatsSTM1TxRSEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM1TxRSEB15MinRtr.setStatus("current")
_TnSdhStatsTxRSES15MinRtr_Type = Counter32
_TnSdhStatsTxRSES15MinRtr_Object = MibScalar
tnSdhStatsTxRSES15MinRtr = _TnSdhStatsTxRSES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 85),
    _TnSdhStatsTxRSES15MinRtr_Type()
)
tnSdhStatsTxRSES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsTxRSES15MinRtr.setStatus("current")
_TnSdhStatsTxRSSES15MinRtr_Type = Counter32
_TnSdhStatsTxRSSES15MinRtr_Object = MibScalar
tnSdhStatsTxRSSES15MinRtr = _TnSdhStatsTxRSSES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 86),
    _TnSdhStatsTxRSSES15MinRtr_Type()
)
tnSdhStatsTxRSSES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsTxRSSES15MinRtr.setStatus("current")
_TnSdhStatsSTM256TxMSEB15MinRtr_Type = Counter32
_TnSdhStatsSTM256TxMSEB15MinRtr_Object = MibScalar
tnSdhStatsSTM256TxMSEB15MinRtr = _TnSdhStatsSTM256TxMSEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 87),
    _TnSdhStatsSTM256TxMSEB15MinRtr_Type()
)
tnSdhStatsSTM256TxMSEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM256TxMSEB15MinRtr.setStatus("current")
_TnSdhStatsSTM64TxMSEB15MinRtr_Type = Counter32
_TnSdhStatsSTM64TxMSEB15MinRtr_Object = MibScalar
tnSdhStatsSTM64TxMSEB15MinRtr = _TnSdhStatsSTM64TxMSEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 88),
    _TnSdhStatsSTM64TxMSEB15MinRtr_Type()
)
tnSdhStatsSTM64TxMSEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM64TxMSEB15MinRtr.setStatus("current")
_TnSdhStatsSTM16TxMSEB15MinRtr_Type = Counter32
_TnSdhStatsSTM16TxMSEB15MinRtr_Object = MibScalar
tnSdhStatsSTM16TxMSEB15MinRtr = _TnSdhStatsSTM16TxMSEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 89),
    _TnSdhStatsSTM16TxMSEB15MinRtr_Type()
)
tnSdhStatsSTM16TxMSEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM16TxMSEB15MinRtr.setStatus("current")
_TnSdhStatsSTM4TxMSEB15MinRtr_Type = Counter32
_TnSdhStatsSTM4TxMSEB15MinRtr_Object = MibScalar
tnSdhStatsSTM4TxMSEB15MinRtr = _TnSdhStatsSTM4TxMSEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 90),
    _TnSdhStatsSTM4TxMSEB15MinRtr_Type()
)
tnSdhStatsSTM4TxMSEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM4TxMSEB15MinRtr.setStatus("current")
_TnSdhStatsSTM1TxMSEB15MinRtr_Type = Counter32
_TnSdhStatsSTM1TxMSEB15MinRtr_Object = MibScalar
tnSdhStatsSTM1TxMSEB15MinRtr = _TnSdhStatsSTM1TxMSEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 91),
    _TnSdhStatsSTM1TxMSEB15MinRtr_Type()
)
tnSdhStatsSTM1TxMSEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM1TxMSEB15MinRtr.setStatus("current")
_TnSdhStatsTxMSES15MinRtr_Type = Counter32
_TnSdhStatsTxMSES15MinRtr_Object = MibScalar
tnSdhStatsTxMSES15MinRtr = _TnSdhStatsTxMSES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 92),
    _TnSdhStatsTxMSES15MinRtr_Type()
)
tnSdhStatsTxMSES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsTxMSES15MinRtr.setStatus("current")
_TnSdhStatsTxMSSES15MinRtr_Type = Counter32
_TnSdhStatsTxMSSES15MinRtr_Object = MibScalar
tnSdhStatsTxMSSES15MinRtr = _TnSdhStatsTxMSSES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 93),
    _TnSdhStatsTxMSSES15MinRtr_Type()
)
tnSdhStatsTxMSSES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsTxMSSES15MinRtr.setStatus("current")
_TnSdhStatsTxMSUAS15MinRtr_Type = Counter32
_TnSdhStatsTxMSUAS15MinRtr_Object = MibScalar
tnSdhStatsTxMSUAS15MinRtr = _TnSdhStatsTxMSUAS15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 94),
    _TnSdhStatsTxMSUAS15MinRtr_Type()
)
tnSdhStatsTxMSUAS15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsTxMSUAS15MinRtr.setStatus("current")
_TnSdhStatsRxRSUAS15MinRtr_Type = Counter32
_TnSdhStatsRxRSUAS15MinRtr_Object = MibScalar
tnSdhStatsRxRSUAS15MinRtr = _TnSdhStatsRxRSUAS15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 95),
    _TnSdhStatsRxRSUAS15MinRtr_Type()
)
tnSdhStatsRxRSUAS15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxRSUAS15MinRtr.setStatus("current")
_TnSdhStatsTxRSUAS15MinRtr_Type = Counter32
_TnSdhStatsTxRSUAS15MinRtr_Object = MibScalar
tnSdhStatsTxRSUAS15MinRtr = _TnSdhStatsTxRSUAS15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 96),
    _TnSdhStatsTxRSUAS15MinRtr_Type()
)
tnSdhStatsTxRSUAS15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsTxRSUAS15MinRtr.setStatus("current")
_TnSdhStatsSTM256RxMSFEEB15MinTr_Type = Counter32
_TnSdhStatsSTM256RxMSFEEB15MinTr_Object = MibScalar
tnSdhStatsSTM256RxMSFEEB15MinTr = _TnSdhStatsSTM256RxMSFEEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 97),
    _TnSdhStatsSTM256RxMSFEEB15MinTr_Type()
)
tnSdhStatsSTM256RxMSFEEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM256RxMSFEEB15MinTr.setStatus("current")
_TnSdhStatsSTM64RxMSFEEB15MinTr_Type = Counter32
_TnSdhStatsSTM64RxMSFEEB15MinTr_Object = MibScalar
tnSdhStatsSTM64RxMSFEEB15MinTr = _TnSdhStatsSTM64RxMSFEEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 98),
    _TnSdhStatsSTM64RxMSFEEB15MinTr_Type()
)
tnSdhStatsSTM64RxMSFEEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM64RxMSFEEB15MinTr.setStatus("current")
_TnSdhStatsSTM16RxMSFEEB15MinTr_Type = Counter32
_TnSdhStatsSTM16RxMSFEEB15MinTr_Object = MibScalar
tnSdhStatsSTM16RxMSFEEB15MinTr = _TnSdhStatsSTM16RxMSFEEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 99),
    _TnSdhStatsSTM16RxMSFEEB15MinTr_Type()
)
tnSdhStatsSTM16RxMSFEEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM16RxMSFEEB15MinTr.setStatus("current")
_TnSdhStatsSTM4RxMSFEEB15MinTr_Type = Counter32
_TnSdhStatsSTM4RxMSFEEB15MinTr_Object = MibScalar
tnSdhStatsSTM4RxMSFEEB15MinTr = _TnSdhStatsSTM4RxMSFEEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 100),
    _TnSdhStatsSTM4RxMSFEEB15MinTr_Type()
)
tnSdhStatsSTM4RxMSFEEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM4RxMSFEEB15MinTr.setStatus("current")
_TnSdhStatsSTM1RxMSFEEB15MinTr_Type = Counter32
_TnSdhStatsSTM1RxMSFEEB15MinTr_Object = MibScalar
tnSdhStatsSTM1RxMSFEEB15MinTr = _TnSdhStatsSTM1RxMSFEEB15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 101),
    _TnSdhStatsSTM1RxMSFEEB15MinTr_Type()
)
tnSdhStatsSTM1RxMSFEEB15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM1RxMSFEEB15MinTr.setStatus("current")
_TnSdhStatsRxMSFEES15MinTr_Type = Counter32
_TnSdhStatsRxMSFEES15MinTr_Object = MibScalar
tnSdhStatsRxMSFEES15MinTr = _TnSdhStatsRxMSFEES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 102),
    _TnSdhStatsRxMSFEES15MinTr_Type()
)
tnSdhStatsRxMSFEES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxMSFEES15MinTr.setStatus("current")
_TnSdhStatsRxMSFESES15MinTr_Type = Counter32
_TnSdhStatsRxMSFESES15MinTr_Object = MibScalar
tnSdhStatsRxMSFESES15MinTr = _TnSdhStatsRxMSFESES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 103),
    _TnSdhStatsRxMSFESES15MinTr_Type()
)
tnSdhStatsRxMSFESES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxMSFESES15MinTr.setStatus("current")
_TnSdhStatsRxMSFEUAS15MinTr_Type = Counter32
_TnSdhStatsRxMSFEUAS15MinTr_Object = MibScalar
tnSdhStatsRxMSFEUAS15MinTr = _TnSdhStatsRxMSFEUAS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 104),
    _TnSdhStatsRxMSFEUAS15MinTr_Type()
)
tnSdhStatsRxMSFEUAS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxMSFEUAS15MinTr.setStatus("current")
_TnSdhStatsSTM256RxMSFEEB1DayTr_Type = Counter32
_TnSdhStatsSTM256RxMSFEEB1DayTr_Object = MibScalar
tnSdhStatsSTM256RxMSFEEB1DayTr = _TnSdhStatsSTM256RxMSFEEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 105),
    _TnSdhStatsSTM256RxMSFEEB1DayTr_Type()
)
tnSdhStatsSTM256RxMSFEEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM256RxMSFEEB1DayTr.setStatus("current")
_TnSdhStatsSTM64RxMSFEEB1DayTr_Type = Counter32
_TnSdhStatsSTM64RxMSFEEB1DayTr_Object = MibScalar
tnSdhStatsSTM64RxMSFEEB1DayTr = _TnSdhStatsSTM64RxMSFEEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 106),
    _TnSdhStatsSTM64RxMSFEEB1DayTr_Type()
)
tnSdhStatsSTM64RxMSFEEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM64RxMSFEEB1DayTr.setStatus("current")
_TnSdhStatsSTM16RxMSFEEB1DayTr_Type = Counter32
_TnSdhStatsSTM16RxMSFEEB1DayTr_Object = MibScalar
tnSdhStatsSTM16RxMSFEEB1DayTr = _TnSdhStatsSTM16RxMSFEEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 107),
    _TnSdhStatsSTM16RxMSFEEB1DayTr_Type()
)
tnSdhStatsSTM16RxMSFEEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM16RxMSFEEB1DayTr.setStatus("current")
_TnSdhStatsSTM4RxMSFEEB1DayTr_Type = Counter32
_TnSdhStatsSTM4RxMSFEEB1DayTr_Object = MibScalar
tnSdhStatsSTM4RxMSFEEB1DayTr = _TnSdhStatsSTM4RxMSFEEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 108),
    _TnSdhStatsSTM4RxMSFEEB1DayTr_Type()
)
tnSdhStatsSTM4RxMSFEEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM4RxMSFEEB1DayTr.setStatus("current")
_TnSdhStatsSTM1RxMSFEEB1DayTr_Type = Counter32
_TnSdhStatsSTM1RxMSFEEB1DayTr_Object = MibScalar
tnSdhStatsSTM1RxMSFEEB1DayTr = _TnSdhStatsSTM1RxMSFEEB1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 109),
    _TnSdhStatsSTM1RxMSFEEB1DayTr_Type()
)
tnSdhStatsSTM1RxMSFEEB1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM1RxMSFEEB1DayTr.setStatus("current")
_TnSdhStatsRxMSFEES1DayTr_Type = Counter32
_TnSdhStatsRxMSFEES1DayTr_Object = MibScalar
tnSdhStatsRxMSFEES1DayTr = _TnSdhStatsRxMSFEES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 110),
    _TnSdhStatsRxMSFEES1DayTr_Type()
)
tnSdhStatsRxMSFEES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxMSFEES1DayTr.setStatus("current")
_TnSdhStatsRxMSFESES1DayTr_Type = Counter32
_TnSdhStatsRxMSFESES1DayTr_Object = MibScalar
tnSdhStatsRxMSFESES1DayTr = _TnSdhStatsRxMSFESES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 111),
    _TnSdhStatsRxMSFESES1DayTr_Type()
)
tnSdhStatsRxMSFESES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxMSFESES1DayTr.setStatus("current")
_TnSdhStatsRxMSFEUAS1DayTr_Type = Counter32
_TnSdhStatsRxMSFEUAS1DayTr_Object = MibScalar
tnSdhStatsRxMSFEUAS1DayTr = _TnSdhStatsRxMSFEUAS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 112),
    _TnSdhStatsRxMSFEUAS1DayTr_Type()
)
tnSdhStatsRxMSFEUAS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxMSFEUAS1DayTr.setStatus("current")
_TnSdhStatsSTM256RxMSFEEB15MinRtr_Type = Counter32
_TnSdhStatsSTM256RxMSFEEB15MinRtr_Object = MibScalar
tnSdhStatsSTM256RxMSFEEB15MinRtr = _TnSdhStatsSTM256RxMSFEEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 113),
    _TnSdhStatsSTM256RxMSFEEB15MinRtr_Type()
)
tnSdhStatsSTM256RxMSFEEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM256RxMSFEEB15MinRtr.setStatus("current")
_TnSdhStatsSTM64RxMSFEEB15MinRtr_Type = Counter32
_TnSdhStatsSTM64RxMSFEEB15MinRtr_Object = MibScalar
tnSdhStatsSTM64RxMSFEEB15MinRtr = _TnSdhStatsSTM64RxMSFEEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 114),
    _TnSdhStatsSTM64RxMSFEEB15MinRtr_Type()
)
tnSdhStatsSTM64RxMSFEEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM64RxMSFEEB15MinRtr.setStatus("current")
_TnSdhStatsSTM16RxMSFEEB15MinRtr_Type = Counter32
_TnSdhStatsSTM16RxMSFEEB15MinRtr_Object = MibScalar
tnSdhStatsSTM16RxMSFEEB15MinRtr = _TnSdhStatsSTM16RxMSFEEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 115),
    _TnSdhStatsSTM16RxMSFEEB15MinRtr_Type()
)
tnSdhStatsSTM16RxMSFEEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM16RxMSFEEB15MinRtr.setStatus("current")
_TnSdhStatsSTM4RxMSFEEB15MinRtr_Type = Counter32
_TnSdhStatsSTM4RxMSFEEB15MinRtr_Object = MibScalar
tnSdhStatsSTM4RxMSFEEB15MinRtr = _TnSdhStatsSTM4RxMSFEEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 116),
    _TnSdhStatsSTM4RxMSFEEB15MinRtr_Type()
)
tnSdhStatsSTM4RxMSFEEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM4RxMSFEEB15MinRtr.setStatus("current")
_TnSdhStatsSTM1RxMSFEEB15MinRtr_Type = Counter32
_TnSdhStatsSTM1RxMSFEEB15MinRtr_Object = MibScalar
tnSdhStatsSTM1RxMSFEEB15MinRtr = _TnSdhStatsSTM1RxMSFEEB15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 117),
    _TnSdhStatsSTM1RxMSFEEB15MinRtr_Type()
)
tnSdhStatsSTM1RxMSFEEB15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsSTM1RxMSFEEB15MinRtr.setStatus("current")
_TnSdhStatsRxMSFEES15MinRtr_Type = Counter32
_TnSdhStatsRxMSFEES15MinRtr_Object = MibScalar
tnSdhStatsRxMSFEES15MinRtr = _TnSdhStatsRxMSFEES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 118),
    _TnSdhStatsRxMSFEES15MinRtr_Type()
)
tnSdhStatsRxMSFEES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxMSFEES15MinRtr.setStatus("current")
_TnSdhStatsRxMSFESES15MinRtr_Type = Counter32
_TnSdhStatsRxMSFESES15MinRtr_Object = MibScalar
tnSdhStatsRxMSFESES15MinRtr = _TnSdhStatsRxMSFESES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 119),
    _TnSdhStatsRxMSFESES15MinRtr_Type()
)
tnSdhStatsRxMSFESES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxMSFESES15MinRtr.setStatus("current")
_TnSdhStatsRxMSFEUAS15MinRtr_Type = Counter32
_TnSdhStatsRxMSFEUAS15MinRtr_Object = MibScalar
tnSdhStatsRxMSFEUAS15MinRtr = _TnSdhStatsRxMSFEUAS15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 9, 120),
    _TnSdhStatsRxMSFEUAS15MinRtr_Type()
)
tnSdhStatsRxMSFEUAS15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSdhStatsRxMSFEUAS15MinRtr.setStatus("current")
_TnStatisticsDwScalars_ObjectIdentity = ObjectIdentity
tnStatisticsDwScalars = _TnStatisticsDwScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10)
)
_TnDw64BitStatsOtu1RxRSCorrCnt15MinTr_Type = Counter64
_TnDw64BitStatsOtu1RxRSCorrCnt15MinTr_Object = MibScalar
tnDw64BitStatsOtu1RxRSCorrCnt15MinTr = _TnDw64BitStatsOtu1RxRSCorrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 1),
    _TnDw64BitStatsOtu1RxRSCorrCnt15MinTr_Type()
)
tnDw64BitStatsOtu1RxRSCorrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu1RxRSCorrCnt15MinTr.setStatus("current")
_TnDw64BitStatsOtu2RxRSCorrCnt15MinTr_Type = Counter64
_TnDw64BitStatsOtu2RxRSCorrCnt15MinTr_Object = MibScalar
tnDw64BitStatsOtu2RxRSCorrCnt15MinTr = _TnDw64BitStatsOtu2RxRSCorrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 2),
    _TnDw64BitStatsOtu2RxRSCorrCnt15MinTr_Type()
)
tnDw64BitStatsOtu2RxRSCorrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu2RxRSCorrCnt15MinTr.setStatus("current")
_TnDw64BitStatsOtu3RxRSCorrCnt15MinTr_Type = Counter64
_TnDw64BitStatsOtu3RxRSCorrCnt15MinTr_Object = MibScalar
tnDw64BitStatsOtu3RxRSCorrCnt15MinTr = _TnDw64BitStatsOtu3RxRSCorrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 3),
    _TnDw64BitStatsOtu3RxRSCorrCnt15MinTr_Type()
)
tnDw64BitStatsOtu3RxRSCorrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu3RxRSCorrCnt15MinTr.setStatus("current")
_TnDw64BitStatsOtu4RxRSCorrCnt15MinTr_Type = Counter64
_TnDw64BitStatsOtu4RxRSCorrCnt15MinTr_Object = MibScalar
tnDw64BitStatsOtu4RxRSCorrCnt15MinTr = _TnDw64BitStatsOtu4RxRSCorrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 4),
    _TnDw64BitStatsOtu4RxRSCorrCnt15MinTr_Type()
)
tnDw64BitStatsOtu4RxRSCorrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu4RxRSCorrCnt15MinTr.setStatus("current")
_TnDw64BitStatsOtu1RxRSUncorrCnt15MinTr_Type = Counter64
_TnDw64BitStatsOtu1RxRSUncorrCnt15MinTr_Object = MibScalar
tnDw64BitStatsOtu1RxRSUncorrCnt15MinTr = _TnDw64BitStatsOtu1RxRSUncorrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 5),
    _TnDw64BitStatsOtu1RxRSUncorrCnt15MinTr_Type()
)
tnDw64BitStatsOtu1RxRSUncorrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu1RxRSUncorrCnt15MinTr.setStatus("current")
_TnDw64BitStatsOtu2RxRSUncorrCnt15MinTr_Type = Counter64
_TnDw64BitStatsOtu2RxRSUncorrCnt15MinTr_Object = MibScalar
tnDw64BitStatsOtu2RxRSUncorrCnt15MinTr = _TnDw64BitStatsOtu2RxRSUncorrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 6),
    _TnDw64BitStatsOtu2RxRSUncorrCnt15MinTr_Type()
)
tnDw64BitStatsOtu2RxRSUncorrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu2RxRSUncorrCnt15MinTr.setStatus("current")
_TnDw64BitStatsOtu3RxRSUncorrCnt15MinTr_Type = Counter64
_TnDw64BitStatsOtu3RxRSUncorrCnt15MinTr_Object = MibScalar
tnDw64BitStatsOtu3RxRSUncorrCnt15MinTr = _TnDw64BitStatsOtu3RxRSUncorrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 7),
    _TnDw64BitStatsOtu3RxRSUncorrCnt15MinTr_Type()
)
tnDw64BitStatsOtu3RxRSUncorrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu3RxRSUncorrCnt15MinTr.setStatus("current")
_TnDw64BitStatsOtu4RxRSUncorrCnt15MinTr_Type = Counter64
_TnDw64BitStatsOtu4RxRSUncorrCnt15MinTr_Object = MibScalar
tnDw64BitStatsOtu4RxRSUncorrCnt15MinTr = _TnDw64BitStatsOtu4RxRSUncorrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 8),
    _TnDw64BitStatsOtu4RxRSUncorrCnt15MinTr_Type()
)
tnDw64BitStatsOtu4RxRSUncorrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu4RxRSUncorrCnt15MinTr.setStatus("current")
_TnDw64BitStatsOtu1RxSMBIP8ErrCnt15MinTr_Type = Counter64
_TnDw64BitStatsOtu1RxSMBIP8ErrCnt15MinTr_Object = MibScalar
tnDw64BitStatsOtu1RxSMBIP8ErrCnt15MinTr = _TnDw64BitStatsOtu1RxSMBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 9),
    _TnDw64BitStatsOtu1RxSMBIP8ErrCnt15MinTr_Type()
)
tnDw64BitStatsOtu1RxSMBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu1RxSMBIP8ErrCnt15MinTr.setStatus("current")
_TnDw64BitStatsOtu2RxSMBIP8ErrCnt15MinTr_Type = Counter64
_TnDw64BitStatsOtu2RxSMBIP8ErrCnt15MinTr_Object = MibScalar
tnDw64BitStatsOtu2RxSMBIP8ErrCnt15MinTr = _TnDw64BitStatsOtu2RxSMBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 10),
    _TnDw64BitStatsOtu2RxSMBIP8ErrCnt15MinTr_Type()
)
tnDw64BitStatsOtu2RxSMBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu2RxSMBIP8ErrCnt15MinTr.setStatus("current")
_TnDw64BitStatsOtu3RxSMBIP8ErrCnt15MinTr_Type = Counter64
_TnDw64BitStatsOtu3RxSMBIP8ErrCnt15MinTr_Object = MibScalar
tnDw64BitStatsOtu3RxSMBIP8ErrCnt15MinTr = _TnDw64BitStatsOtu3RxSMBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 11),
    _TnDw64BitStatsOtu3RxSMBIP8ErrCnt15MinTr_Type()
)
tnDw64BitStatsOtu3RxSMBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu3RxSMBIP8ErrCnt15MinTr.setStatus("current")
_TnDw64BitStatsOtu4RxSMBIP8ErrCnt15MinTr_Type = Counter64
_TnDw64BitStatsOtu4RxSMBIP8ErrCnt15MinTr_Object = MibScalar
tnDw64BitStatsOtu4RxSMBIP8ErrCnt15MinTr = _TnDw64BitStatsOtu4RxSMBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 12),
    _TnDw64BitStatsOtu4RxSMBIP8ErrCnt15MinTr_Type()
)
tnDw64BitStatsOtu4RxSMBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu4RxSMBIP8ErrCnt15MinTr.setStatus("current")
_TnDw64BitStatsOdu1RxPMBIP8ErrCnt15MinTr_Type = Counter64
_TnDw64BitStatsOdu1RxPMBIP8ErrCnt15MinTr_Object = MibScalar
tnDw64BitStatsOdu1RxPMBIP8ErrCnt15MinTr = _TnDw64BitStatsOdu1RxPMBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 13),
    _TnDw64BitStatsOdu1RxPMBIP8ErrCnt15MinTr_Type()
)
tnDw64BitStatsOdu1RxPMBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOdu1RxPMBIP8ErrCnt15MinTr.setStatus("current")
_TnDw64BitStatsOdu2RxPMBIP8ErrCnt15MinTr_Type = Counter64
_TnDw64BitStatsOdu2RxPMBIP8ErrCnt15MinTr_Object = MibScalar
tnDw64BitStatsOdu2RxPMBIP8ErrCnt15MinTr = _TnDw64BitStatsOdu2RxPMBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 14),
    _TnDw64BitStatsOdu2RxPMBIP8ErrCnt15MinTr_Type()
)
tnDw64BitStatsOdu2RxPMBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOdu2RxPMBIP8ErrCnt15MinTr.setStatus("current")
_TnDw64BitStatsOdu3RxPMBIP8ErrCnt15MinTr_Type = Counter64
_TnDw64BitStatsOdu3RxPMBIP8ErrCnt15MinTr_Object = MibScalar
tnDw64BitStatsOdu3RxPMBIP8ErrCnt15MinTr = _TnDw64BitStatsOdu3RxPMBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 15),
    _TnDw64BitStatsOdu3RxPMBIP8ErrCnt15MinTr_Type()
)
tnDw64BitStatsOdu3RxPMBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOdu3RxPMBIP8ErrCnt15MinTr.setStatus("current")
_TnDw64BitStatsOdu4RxPMBIP8ErrCnt15MinTr_Type = Counter64
_TnDw64BitStatsOdu4RxPMBIP8ErrCnt15MinTr_Object = MibScalar
tnDw64BitStatsOdu4RxPMBIP8ErrCnt15MinTr = _TnDw64BitStatsOdu4RxPMBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 16),
    _TnDw64BitStatsOdu4RxPMBIP8ErrCnt15MinTr_Type()
)
tnDw64BitStatsOdu4RxPMBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOdu4RxPMBIP8ErrCnt15MinTr.setStatus("current")
_TnDw64BitStatsRxSMES15MinTr_Type = Counter64
_TnDw64BitStatsRxSMES15MinTr_Object = MibScalar
tnDw64BitStatsRxSMES15MinTr = _TnDw64BitStatsRxSMES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 17),
    _TnDw64BitStatsRxSMES15MinTr_Type()
)
tnDw64BitStatsRxSMES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsRxSMES15MinTr.setStatus("current")
_TnDw64BitStatsRxPMES15MinTr_Type = Counter64
_TnDw64BitStatsRxPMES15MinTr_Object = MibScalar
tnDw64BitStatsRxPMES15MinTr = _TnDw64BitStatsRxPMES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 18),
    _TnDw64BitStatsRxPMES15MinTr_Type()
)
tnDw64BitStatsRxPMES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsRxPMES15MinTr.setStatus("current")
_TnDw64BitStatsRxSMSES15MinTr_Type = Counter64
_TnDw64BitStatsRxSMSES15MinTr_Object = MibScalar
tnDw64BitStatsRxSMSES15MinTr = _TnDw64BitStatsRxSMSES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 19),
    _TnDw64BitStatsRxSMSES15MinTr_Type()
)
tnDw64BitStatsRxSMSES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsRxSMSES15MinTr.setStatus("current")
_TnDw64BitStatsRxPMSES15MinTr_Type = Counter64
_TnDw64BitStatsRxPMSES15MinTr_Object = MibScalar
tnDw64BitStatsRxPMSES15MinTr = _TnDw64BitStatsRxPMSES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 20),
    _TnDw64BitStatsRxPMSES15MinTr_Type()
)
tnDw64BitStatsRxPMSES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsRxPMSES15MinTr.setStatus("current")
_TnDw64BitStatsRxSMUAS15MinTr_Type = Counter64
_TnDw64BitStatsRxSMUAS15MinTr_Object = MibScalar
tnDw64BitStatsRxSMUAS15MinTr = _TnDw64BitStatsRxSMUAS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 21),
    _TnDw64BitStatsRxSMUAS15MinTr_Type()
)
tnDw64BitStatsRxSMUAS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsRxSMUAS15MinTr.setStatus("current")
_TnDw64BitStatsRxPMUAS15MinTr_Type = Counter64
_TnDw64BitStatsRxPMUAS15MinTr_Object = MibScalar
tnDw64BitStatsRxPMUAS15MinTr = _TnDw64BitStatsRxPMUAS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 22),
    _TnDw64BitStatsRxPMUAS15MinTr_Type()
)
tnDw64BitStatsRxPMUAS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsRxPMUAS15MinTr.setStatus("current")
_TnDw64BitStatsOtu1RxRSCorrCnt1DayTr_Type = Counter64
_TnDw64BitStatsOtu1RxRSCorrCnt1DayTr_Object = MibScalar
tnDw64BitStatsOtu1RxRSCorrCnt1DayTr = _TnDw64BitStatsOtu1RxRSCorrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 23),
    _TnDw64BitStatsOtu1RxRSCorrCnt1DayTr_Type()
)
tnDw64BitStatsOtu1RxRSCorrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu1RxRSCorrCnt1DayTr.setStatus("current")
_TnDw64BitStatsOtu2RxRSCorrCnt1DayTr_Type = Counter64
_TnDw64BitStatsOtu2RxRSCorrCnt1DayTr_Object = MibScalar
tnDw64BitStatsOtu2RxRSCorrCnt1DayTr = _TnDw64BitStatsOtu2RxRSCorrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 24),
    _TnDw64BitStatsOtu2RxRSCorrCnt1DayTr_Type()
)
tnDw64BitStatsOtu2RxRSCorrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu2RxRSCorrCnt1DayTr.setStatus("current")
_TnDw64BitStatsOtu3RxRSCorrCnt1DayTr_Type = Counter64
_TnDw64BitStatsOtu3RxRSCorrCnt1DayTr_Object = MibScalar
tnDw64BitStatsOtu3RxRSCorrCnt1DayTr = _TnDw64BitStatsOtu3RxRSCorrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 25),
    _TnDw64BitStatsOtu3RxRSCorrCnt1DayTr_Type()
)
tnDw64BitStatsOtu3RxRSCorrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu3RxRSCorrCnt1DayTr.setStatus("current")
_TnDw64BitStatsOtu4RxRSCorrCnt1DayTr_Type = Counter64
_TnDw64BitStatsOtu4RxRSCorrCnt1DayTr_Object = MibScalar
tnDw64BitStatsOtu4RxRSCorrCnt1DayTr = _TnDw64BitStatsOtu4RxRSCorrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 26),
    _TnDw64BitStatsOtu4RxRSCorrCnt1DayTr_Type()
)
tnDw64BitStatsOtu4RxRSCorrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu4RxRSCorrCnt1DayTr.setStatus("current")
_TnDw64BitStatsOtu1RxRSUncorrCnt1DayTr_Type = Counter64
_TnDw64BitStatsOtu1RxRSUncorrCnt1DayTr_Object = MibScalar
tnDw64BitStatsOtu1RxRSUncorrCnt1DayTr = _TnDw64BitStatsOtu1RxRSUncorrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 27),
    _TnDw64BitStatsOtu1RxRSUncorrCnt1DayTr_Type()
)
tnDw64BitStatsOtu1RxRSUncorrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu1RxRSUncorrCnt1DayTr.setStatus("current")
_TnDw64BitStatsOtu2RxRSUncorrCnt1DayTr_Type = Counter64
_TnDw64BitStatsOtu2RxRSUncorrCnt1DayTr_Object = MibScalar
tnDw64BitStatsOtu2RxRSUncorrCnt1DayTr = _TnDw64BitStatsOtu2RxRSUncorrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 28),
    _TnDw64BitStatsOtu2RxRSUncorrCnt1DayTr_Type()
)
tnDw64BitStatsOtu2RxRSUncorrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu2RxRSUncorrCnt1DayTr.setStatus("current")
_TnDw64BitStatsOtu3RxRSUncorrCnt1DayTr_Type = Counter64
_TnDw64BitStatsOtu3RxRSUncorrCnt1DayTr_Object = MibScalar
tnDw64BitStatsOtu3RxRSUncorrCnt1DayTr = _TnDw64BitStatsOtu3RxRSUncorrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 29),
    _TnDw64BitStatsOtu3RxRSUncorrCnt1DayTr_Type()
)
tnDw64BitStatsOtu3RxRSUncorrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu3RxRSUncorrCnt1DayTr.setStatus("current")
_TnDw64BitStatsOtu4RxRSUncorrCnt1DayTr_Type = Counter64
_TnDw64BitStatsOtu4RxRSUncorrCnt1DayTr_Object = MibScalar
tnDw64BitStatsOtu4RxRSUncorrCnt1DayTr = _TnDw64BitStatsOtu4RxRSUncorrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 30),
    _TnDw64BitStatsOtu4RxRSUncorrCnt1DayTr_Type()
)
tnDw64BitStatsOtu4RxRSUncorrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu4RxRSUncorrCnt1DayTr.setStatus("current")
_TnDw64BitStatsOtu1RxSMBIP8ErrCnt1DayTr_Type = Counter64
_TnDw64BitStatsOtu1RxSMBIP8ErrCnt1DayTr_Object = MibScalar
tnDw64BitStatsOtu1RxSMBIP8ErrCnt1DayTr = _TnDw64BitStatsOtu1RxSMBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 31),
    _TnDw64BitStatsOtu1RxSMBIP8ErrCnt1DayTr_Type()
)
tnDw64BitStatsOtu1RxSMBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu1RxSMBIP8ErrCnt1DayTr.setStatus("current")
_TnDw64BitStatsOtu2RxSMBIP8ErrCnt1DayTr_Type = Counter64
_TnDw64BitStatsOtu2RxSMBIP8ErrCnt1DayTr_Object = MibScalar
tnDw64BitStatsOtu2RxSMBIP8ErrCnt1DayTr = _TnDw64BitStatsOtu2RxSMBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 32),
    _TnDw64BitStatsOtu2RxSMBIP8ErrCnt1DayTr_Type()
)
tnDw64BitStatsOtu2RxSMBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu2RxSMBIP8ErrCnt1DayTr.setStatus("current")
_TnDw64BitStatsOtu3RxSMBIP8ErrCnt1DayTr_Type = Counter64
_TnDw64BitStatsOtu3RxSMBIP8ErrCnt1DayTr_Object = MibScalar
tnDw64BitStatsOtu3RxSMBIP8ErrCnt1DayTr = _TnDw64BitStatsOtu3RxSMBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 33),
    _TnDw64BitStatsOtu3RxSMBIP8ErrCnt1DayTr_Type()
)
tnDw64BitStatsOtu3RxSMBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu3RxSMBIP8ErrCnt1DayTr.setStatus("current")
_TnDw64BitStatsOtu4RxSMBIP8ErrCnt1DayTr_Type = Counter64
_TnDw64BitStatsOtu4RxSMBIP8ErrCnt1DayTr_Object = MibScalar
tnDw64BitStatsOtu4RxSMBIP8ErrCnt1DayTr = _TnDw64BitStatsOtu4RxSMBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 34),
    _TnDw64BitStatsOtu4RxSMBIP8ErrCnt1DayTr_Type()
)
tnDw64BitStatsOtu4RxSMBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu4RxSMBIP8ErrCnt1DayTr.setStatus("current")
_TnDw64BitStatsOdu1RxPMBIP8ErrCnt1DayTr_Type = Counter64
_TnDw64BitStatsOdu1RxPMBIP8ErrCnt1DayTr_Object = MibScalar
tnDw64BitStatsOdu1RxPMBIP8ErrCnt1DayTr = _TnDw64BitStatsOdu1RxPMBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 35),
    _TnDw64BitStatsOdu1RxPMBIP8ErrCnt1DayTr_Type()
)
tnDw64BitStatsOdu1RxPMBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOdu1RxPMBIP8ErrCnt1DayTr.setStatus("current")
_TnDw64BitStatsOdu2RxPMBIP8ErrCnt1DayTr_Type = Counter64
_TnDw64BitStatsOdu2RxPMBIP8ErrCnt1DayTr_Object = MibScalar
tnDw64BitStatsOdu2RxPMBIP8ErrCnt1DayTr = _TnDw64BitStatsOdu2RxPMBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 36),
    _TnDw64BitStatsOdu2RxPMBIP8ErrCnt1DayTr_Type()
)
tnDw64BitStatsOdu2RxPMBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOdu2RxPMBIP8ErrCnt1DayTr.setStatus("current")
_TnDw64BitStatsOdu3RxPMBIP8ErrCnt1DayTr_Type = Counter64
_TnDw64BitStatsOdu3RxPMBIP8ErrCnt1DayTr_Object = MibScalar
tnDw64BitStatsOdu3RxPMBIP8ErrCnt1DayTr = _TnDw64BitStatsOdu3RxPMBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 37),
    _TnDw64BitStatsOdu3RxPMBIP8ErrCnt1DayTr_Type()
)
tnDw64BitStatsOdu3RxPMBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOdu3RxPMBIP8ErrCnt1DayTr.setStatus("current")
_TnDw64BitStatsOdu4RxPMBIP8ErrCnt1DayTr_Type = Counter64
_TnDw64BitStatsOdu4RxPMBIP8ErrCnt1DayTr_Object = MibScalar
tnDw64BitStatsOdu4RxPMBIP8ErrCnt1DayTr = _TnDw64BitStatsOdu4RxPMBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 38),
    _TnDw64BitStatsOdu4RxPMBIP8ErrCnt1DayTr_Type()
)
tnDw64BitStatsOdu4RxPMBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOdu4RxPMBIP8ErrCnt1DayTr.setStatus("current")
_TnDw64BitStatsRxSMES1DayTr_Type = Counter64
_TnDw64BitStatsRxSMES1DayTr_Object = MibScalar
tnDw64BitStatsRxSMES1DayTr = _TnDw64BitStatsRxSMES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 39),
    _TnDw64BitStatsRxSMES1DayTr_Type()
)
tnDw64BitStatsRxSMES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsRxSMES1DayTr.setStatus("current")
_TnDw64BitStatsRxPMES1DayTr_Type = Counter64
_TnDw64BitStatsRxPMES1DayTr_Object = MibScalar
tnDw64BitStatsRxPMES1DayTr = _TnDw64BitStatsRxPMES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 40),
    _TnDw64BitStatsRxPMES1DayTr_Type()
)
tnDw64BitStatsRxPMES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsRxPMES1DayTr.setStatus("current")
_TnDw64BitStatsRxSMSES1DayTr_Type = Counter64
_TnDw64BitStatsRxSMSES1DayTr_Object = MibScalar
tnDw64BitStatsRxSMSES1DayTr = _TnDw64BitStatsRxSMSES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 41),
    _TnDw64BitStatsRxSMSES1DayTr_Type()
)
tnDw64BitStatsRxSMSES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsRxSMSES1DayTr.setStatus("current")
_TnDw64BitStatsRxPMSES1DayTr_Type = Counter64
_TnDw64BitStatsRxPMSES1DayTr_Object = MibScalar
tnDw64BitStatsRxPMSES1DayTr = _TnDw64BitStatsRxPMSES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 42),
    _TnDw64BitStatsRxPMSES1DayTr_Type()
)
tnDw64BitStatsRxPMSES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsRxPMSES1DayTr.setStatus("current")
_TnDw64BitStatsRxSMUAS1DayTr_Type = Counter64
_TnDw64BitStatsRxSMUAS1DayTr_Object = MibScalar
tnDw64BitStatsRxSMUAS1DayTr = _TnDw64BitStatsRxSMUAS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 43),
    _TnDw64BitStatsRxSMUAS1DayTr_Type()
)
tnDw64BitStatsRxSMUAS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsRxSMUAS1DayTr.setStatus("current")
_TnDw64BitStatsRxPMUAS1DayTr_Type = Counter64
_TnDw64BitStatsRxPMUAS1DayTr_Object = MibScalar
tnDw64BitStatsRxPMUAS1DayTr = _TnDw64BitStatsRxPMUAS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 44),
    _TnDw64BitStatsRxPMUAS1DayTr_Type()
)
tnDw64BitStatsRxPMUAS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsRxPMUAS1DayTr.setStatus("current")
_TnDw64BitStatsOtu1RxRSCorrCnt15MinRtr_Type = Counter64
_TnDw64BitStatsOtu1RxRSCorrCnt15MinRtr_Object = MibScalar
tnDw64BitStatsOtu1RxRSCorrCnt15MinRtr = _TnDw64BitStatsOtu1RxRSCorrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 45),
    _TnDw64BitStatsOtu1RxRSCorrCnt15MinRtr_Type()
)
tnDw64BitStatsOtu1RxRSCorrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu1RxRSCorrCnt15MinRtr.setStatus("current")
_TnDw64BitStatsOtu2RxRSCorrCnt15MinRtr_Type = Counter64
_TnDw64BitStatsOtu2RxRSCorrCnt15MinRtr_Object = MibScalar
tnDw64BitStatsOtu2RxRSCorrCnt15MinRtr = _TnDw64BitStatsOtu2RxRSCorrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 46),
    _TnDw64BitStatsOtu2RxRSCorrCnt15MinRtr_Type()
)
tnDw64BitStatsOtu2RxRSCorrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu2RxRSCorrCnt15MinRtr.setStatus("current")
_TnDw64BitStatsOtu3RxRSCorrCnt15MinRtr_Type = Counter64
_TnDw64BitStatsOtu3RxRSCorrCnt15MinRtr_Object = MibScalar
tnDw64BitStatsOtu3RxRSCorrCnt15MinRtr = _TnDw64BitStatsOtu3RxRSCorrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 47),
    _TnDw64BitStatsOtu3RxRSCorrCnt15MinRtr_Type()
)
tnDw64BitStatsOtu3RxRSCorrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu3RxRSCorrCnt15MinRtr.setStatus("current")
_TnDw64BitStatsOtu4RxRSCorrCnt15MinRtr_Type = Counter64
_TnDw64BitStatsOtu4RxRSCorrCnt15MinRtr_Object = MibScalar
tnDw64BitStatsOtu4RxRSCorrCnt15MinRtr = _TnDw64BitStatsOtu4RxRSCorrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 48),
    _TnDw64BitStatsOtu4RxRSCorrCnt15MinRtr_Type()
)
tnDw64BitStatsOtu4RxRSCorrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu4RxRSCorrCnt15MinRtr.setStatus("current")
_TnDw64BitStatsOtu1RxRSUncorrCnt15MinRtr_Type = Counter64
_TnDw64BitStatsOtu1RxRSUncorrCnt15MinRtr_Object = MibScalar
tnDw64BitStatsOtu1RxRSUncorrCnt15MinRtr = _TnDw64BitStatsOtu1RxRSUncorrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 49),
    _TnDw64BitStatsOtu1RxRSUncorrCnt15MinRtr_Type()
)
tnDw64BitStatsOtu1RxRSUncorrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu1RxRSUncorrCnt15MinRtr.setStatus("current")
_TnDw64BitStatsOtu2RxRSUncorrCnt15MinRtr_Type = Counter64
_TnDw64BitStatsOtu2RxRSUncorrCnt15MinRtr_Object = MibScalar
tnDw64BitStatsOtu2RxRSUncorrCnt15MinRtr = _TnDw64BitStatsOtu2RxRSUncorrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 50),
    _TnDw64BitStatsOtu2RxRSUncorrCnt15MinRtr_Type()
)
tnDw64BitStatsOtu2RxRSUncorrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu2RxRSUncorrCnt15MinRtr.setStatus("current")
_TnDw64BitStatsOtu3RxRSUncorrCnt15MinRtr_Type = Counter64
_TnDw64BitStatsOtu3RxRSUncorrCnt15MinRtr_Object = MibScalar
tnDw64BitStatsOtu3RxRSUncorrCnt15MinRtr = _TnDw64BitStatsOtu3RxRSUncorrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 51),
    _TnDw64BitStatsOtu3RxRSUncorrCnt15MinRtr_Type()
)
tnDw64BitStatsOtu3RxRSUncorrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu3RxRSUncorrCnt15MinRtr.setStatus("current")
_TnDw64BitStatsOtu4RxRSUncorrCnt15MinRtr_Type = Counter64
_TnDw64BitStatsOtu4RxRSUncorrCnt15MinRtr_Object = MibScalar
tnDw64BitStatsOtu4RxRSUncorrCnt15MinRtr = _TnDw64BitStatsOtu4RxRSUncorrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 52),
    _TnDw64BitStatsOtu4RxRSUncorrCnt15MinRtr_Type()
)
tnDw64BitStatsOtu4RxRSUncorrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu4RxRSUncorrCnt15MinRtr.setStatus("current")
_TnDw64BitStatsOtu1RxSMBIP8ErrCnt15MinRtr_Type = Counter64
_TnDw64BitStatsOtu1RxSMBIP8ErrCnt15MinRtr_Object = MibScalar
tnDw64BitStatsOtu1RxSMBIP8ErrCnt15MinRtr = _TnDw64BitStatsOtu1RxSMBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 53),
    _TnDw64BitStatsOtu1RxSMBIP8ErrCnt15MinRtr_Type()
)
tnDw64BitStatsOtu1RxSMBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu1RxSMBIP8ErrCnt15MinRtr.setStatus("current")
_TnDw64BitStatsOtu2RxSMBIP8ErrCnt15MinRtr_Type = Counter64
_TnDw64BitStatsOtu2RxSMBIP8ErrCnt15MinRtr_Object = MibScalar
tnDw64BitStatsOtu2RxSMBIP8ErrCnt15MinRtr = _TnDw64BitStatsOtu2RxSMBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 54),
    _TnDw64BitStatsOtu2RxSMBIP8ErrCnt15MinRtr_Type()
)
tnDw64BitStatsOtu2RxSMBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu2RxSMBIP8ErrCnt15MinRtr.setStatus("current")
_TnDw64BitStatsOtu3RxSMBIP8ErrCnt15MinRtr_Type = Counter64
_TnDw64BitStatsOtu3RxSMBIP8ErrCnt15MinRtr_Object = MibScalar
tnDw64BitStatsOtu3RxSMBIP8ErrCnt15MinRtr = _TnDw64BitStatsOtu3RxSMBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 55),
    _TnDw64BitStatsOtu3RxSMBIP8ErrCnt15MinRtr_Type()
)
tnDw64BitStatsOtu3RxSMBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu3RxSMBIP8ErrCnt15MinRtr.setStatus("current")
_TnDw64BitStatsOtu4RxSMBIP8ErrCnt15MinRtr_Type = Counter64
_TnDw64BitStatsOtu4RxSMBIP8ErrCnt15MinRtr_Object = MibScalar
tnDw64BitStatsOtu4RxSMBIP8ErrCnt15MinRtr = _TnDw64BitStatsOtu4RxSMBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 56),
    _TnDw64BitStatsOtu4RxSMBIP8ErrCnt15MinRtr_Type()
)
tnDw64BitStatsOtu4RxSMBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOtu4RxSMBIP8ErrCnt15MinRtr.setStatus("current")
_TnDw64BitStatsOdu1RxPMBIP8ErrCnt15MinRtr_Type = Counter64
_TnDw64BitStatsOdu1RxPMBIP8ErrCnt15MinRtr_Object = MibScalar
tnDw64BitStatsOdu1RxPMBIP8ErrCnt15MinRtr = _TnDw64BitStatsOdu1RxPMBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 57),
    _TnDw64BitStatsOdu1RxPMBIP8ErrCnt15MinRtr_Type()
)
tnDw64BitStatsOdu1RxPMBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOdu1RxPMBIP8ErrCnt15MinRtr.setStatus("current")
_TnDw64BitStatsOdu2RxPMBIP8ErrCnt15MinRtr_Type = Counter64
_TnDw64BitStatsOdu2RxPMBIP8ErrCnt15MinRtr_Object = MibScalar
tnDw64BitStatsOdu2RxPMBIP8ErrCnt15MinRtr = _TnDw64BitStatsOdu2RxPMBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 58),
    _TnDw64BitStatsOdu2RxPMBIP8ErrCnt15MinRtr_Type()
)
tnDw64BitStatsOdu2RxPMBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOdu2RxPMBIP8ErrCnt15MinRtr.setStatus("current")
_TnDw64BitStatsOdu3RxPMBIP8ErrCnt15MinRtr_Type = Counter64
_TnDw64BitStatsOdu3RxPMBIP8ErrCnt15MinRtr_Object = MibScalar
tnDw64BitStatsOdu3RxPMBIP8ErrCnt15MinRtr = _TnDw64BitStatsOdu3RxPMBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 59),
    _TnDw64BitStatsOdu3RxPMBIP8ErrCnt15MinRtr_Type()
)
tnDw64BitStatsOdu3RxPMBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOdu3RxPMBIP8ErrCnt15MinRtr.setStatus("current")
_TnDw64BitStatsOdu4RxPMBIP8ErrCnt15MinRtr_Type = Counter64
_TnDw64BitStatsOdu4RxPMBIP8ErrCnt15MinRtr_Object = MibScalar
tnDw64BitStatsOdu4RxPMBIP8ErrCnt15MinRtr = _TnDw64BitStatsOdu4RxPMBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 60),
    _TnDw64BitStatsOdu4RxPMBIP8ErrCnt15MinRtr_Type()
)
tnDw64BitStatsOdu4RxPMBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsOdu4RxPMBIP8ErrCnt15MinRtr.setStatus("current")
_TnDw64BitStatsRxSMES15MinRtr_Type = Counter64
_TnDw64BitStatsRxSMES15MinRtr_Object = MibScalar
tnDw64BitStatsRxSMES15MinRtr = _TnDw64BitStatsRxSMES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 61),
    _TnDw64BitStatsRxSMES15MinRtr_Type()
)
tnDw64BitStatsRxSMES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsRxSMES15MinRtr.setStatus("current")
_TnDw64BitStatsRxPMES15MinRtr_Type = Counter64
_TnDw64BitStatsRxPMES15MinRtr_Object = MibScalar
tnDw64BitStatsRxPMES15MinRtr = _TnDw64BitStatsRxPMES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 62),
    _TnDw64BitStatsRxPMES15MinRtr_Type()
)
tnDw64BitStatsRxPMES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsRxPMES15MinRtr.setStatus("current")
_TnDw64BitStatsRxSMSES15MinRtr_Type = Counter64
_TnDw64BitStatsRxSMSES15MinRtr_Object = MibScalar
tnDw64BitStatsRxSMSES15MinRtr = _TnDw64BitStatsRxSMSES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 63),
    _TnDw64BitStatsRxSMSES15MinRtr_Type()
)
tnDw64BitStatsRxSMSES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsRxSMSES15MinRtr.setStatus("current")
_TnDw64BitStatsRxPMSES15MinRtr_Type = Counter64
_TnDw64BitStatsRxPMSES15MinRtr_Object = MibScalar
tnDw64BitStatsRxPMSES15MinRtr = _TnDw64BitStatsRxPMSES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 64),
    _TnDw64BitStatsRxPMSES15MinRtr_Type()
)
tnDw64BitStatsRxPMSES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsRxPMSES15MinRtr.setStatus("current")
_TnDw64BitStatsRxSMUAS15MinRtr_Type = Counter64
_TnDw64BitStatsRxSMUAS15MinRtr_Object = MibScalar
tnDw64BitStatsRxSMUAS15MinRtr = _TnDw64BitStatsRxSMUAS15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 65),
    _TnDw64BitStatsRxSMUAS15MinRtr_Type()
)
tnDw64BitStatsRxSMUAS15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsRxSMUAS15MinRtr.setStatus("current")
_TnDw64BitStatsRxPMUAS15MinRtr_Type = Counter64
_TnDw64BitStatsRxPMUAS15MinRtr_Object = MibScalar
tnDw64BitStatsRxPMUAS15MinRtr = _TnDw64BitStatsRxPMUAS15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 66),
    _TnDw64BitStatsRxPMUAS15MinRtr_Type()
)
tnDw64BitStatsRxPMUAS15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDw64BitStatsRxPMUAS15MinRtr.setStatus("current")
_TnDwStatsOtu1RxSMFEBIP8ErrCnt15MinTr_Type = Counter64
_TnDwStatsOtu1RxSMFEBIP8ErrCnt15MinTr_Object = MibScalar
tnDwStatsOtu1RxSMFEBIP8ErrCnt15MinTr = _TnDwStatsOtu1RxSMFEBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 67),
    _TnDwStatsOtu1RxSMFEBIP8ErrCnt15MinTr_Type()
)
tnDwStatsOtu1RxSMFEBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOtu1RxSMFEBIP8ErrCnt15MinTr.setStatus("current")
_TnDwStatsOtu2RxSMFEBIP8ErrCnt15MinTr_Type = Counter64
_TnDwStatsOtu2RxSMFEBIP8ErrCnt15MinTr_Object = MibScalar
tnDwStatsOtu2RxSMFEBIP8ErrCnt15MinTr = _TnDwStatsOtu2RxSMFEBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 68),
    _TnDwStatsOtu2RxSMFEBIP8ErrCnt15MinTr_Type()
)
tnDwStatsOtu2RxSMFEBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOtu2RxSMFEBIP8ErrCnt15MinTr.setStatus("current")
_TnDwStatsOtu3RxSMFEBIP8ErrCnt15MinTr_Type = Counter64
_TnDwStatsOtu3RxSMFEBIP8ErrCnt15MinTr_Object = MibScalar
tnDwStatsOtu3RxSMFEBIP8ErrCnt15MinTr = _TnDwStatsOtu3RxSMFEBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 69),
    _TnDwStatsOtu3RxSMFEBIP8ErrCnt15MinTr_Type()
)
tnDwStatsOtu3RxSMFEBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOtu3RxSMFEBIP8ErrCnt15MinTr.setStatus("current")
_TnDwStatsOtu4RxSMFEBIP8ErrCnt15MinTr_Type = Counter64
_TnDwStatsOtu4RxSMFEBIP8ErrCnt15MinTr_Object = MibScalar
tnDwStatsOtu4RxSMFEBIP8ErrCnt15MinTr = _TnDwStatsOtu4RxSMFEBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 70),
    _TnDwStatsOtu4RxSMFEBIP8ErrCnt15MinTr_Type()
)
tnDwStatsOtu4RxSMFEBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOtu4RxSMFEBIP8ErrCnt15MinTr.setStatus("current")
_TnDwStatsOdu1RxPMFEBIP8ErrCnt15MinTr_Type = Counter64
_TnDwStatsOdu1RxPMFEBIP8ErrCnt15MinTr_Object = MibScalar
tnDwStatsOdu1RxPMFEBIP8ErrCnt15MinTr = _TnDwStatsOdu1RxPMFEBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 71),
    _TnDwStatsOdu1RxPMFEBIP8ErrCnt15MinTr_Type()
)
tnDwStatsOdu1RxPMFEBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOdu1RxPMFEBIP8ErrCnt15MinTr.setStatus("current")
_TnDwStatsOdu2RxPMFEBIP8ErrCnt15MinTr_Type = Counter64
_TnDwStatsOdu2RxPMFEBIP8ErrCnt15MinTr_Object = MibScalar
tnDwStatsOdu2RxPMFEBIP8ErrCnt15MinTr = _TnDwStatsOdu2RxPMFEBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 72),
    _TnDwStatsOdu2RxPMFEBIP8ErrCnt15MinTr_Type()
)
tnDwStatsOdu2RxPMFEBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOdu2RxPMFEBIP8ErrCnt15MinTr.setStatus("current")
_TnDwStatsOdu3RxPMFEBIP8ErrCnt15MinTr_Type = Counter64
_TnDwStatsOdu3RxPMFEBIP8ErrCnt15MinTr_Object = MibScalar
tnDwStatsOdu3RxPMFEBIP8ErrCnt15MinTr = _TnDwStatsOdu3RxPMFEBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 73),
    _TnDwStatsOdu3RxPMFEBIP8ErrCnt15MinTr_Type()
)
tnDwStatsOdu3RxPMFEBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOdu3RxPMFEBIP8ErrCnt15MinTr.setStatus("current")
_TnDwStatsOdu4RxPMFEBIP8ErrCnt15MinTr_Type = Counter64
_TnDwStatsOdu4RxPMFEBIP8ErrCnt15MinTr_Object = MibScalar
tnDwStatsOdu4RxPMFEBIP8ErrCnt15MinTr = _TnDwStatsOdu4RxPMFEBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 74),
    _TnDwStatsOdu4RxPMFEBIP8ErrCnt15MinTr_Type()
)
tnDwStatsOdu4RxPMFEBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOdu4RxPMFEBIP8ErrCnt15MinTr.setStatus("current")
_TnDwStatsRxSMFEES15MinTr_Type = Counter64
_TnDwStatsRxSMFEES15MinTr_Object = MibScalar
tnDwStatsRxSMFEES15MinTr = _TnDwStatsRxSMFEES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 75),
    _TnDwStatsRxSMFEES15MinTr_Type()
)
tnDwStatsRxSMFEES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxSMFEES15MinTr.setStatus("current")
_TnDwStatsRxPMFEES15MinTr_Type = Counter64
_TnDwStatsRxPMFEES15MinTr_Object = MibScalar
tnDwStatsRxPMFEES15MinTr = _TnDwStatsRxPMFEES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 76),
    _TnDwStatsRxPMFEES15MinTr_Type()
)
tnDwStatsRxPMFEES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxPMFEES15MinTr.setStatus("current")
_TnDwStatsRxSMFESES15MinTr_Type = Counter64
_TnDwStatsRxSMFESES15MinTr_Object = MibScalar
tnDwStatsRxSMFESES15MinTr = _TnDwStatsRxSMFESES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 77),
    _TnDwStatsRxSMFESES15MinTr_Type()
)
tnDwStatsRxSMFESES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxSMFESES15MinTr.setStatus("current")
_TnDwStatsRxPMFESES15MinTr_Type = Counter64
_TnDwStatsRxPMFESES15MinTr_Object = MibScalar
tnDwStatsRxPMFESES15MinTr = _TnDwStatsRxPMFESES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 78),
    _TnDwStatsRxPMFESES15MinTr_Type()
)
tnDwStatsRxPMFESES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxPMFESES15MinTr.setStatus("current")
_TnDwStatsRxSMFEUAS15MinTr_Type = Counter64
_TnDwStatsRxSMFEUAS15MinTr_Object = MibScalar
tnDwStatsRxSMFEUAS15MinTr = _TnDwStatsRxSMFEUAS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 79),
    _TnDwStatsRxSMFEUAS15MinTr_Type()
)
tnDwStatsRxSMFEUAS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxSMFEUAS15MinTr.setStatus("current")
_TnDwStatsRxPMFEUAS15MinTr_Type = Counter64
_TnDwStatsRxPMFEUAS15MinTr_Object = MibScalar
tnDwStatsRxPMFEUAS15MinTr = _TnDwStatsRxPMFEUAS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 80),
    _TnDwStatsRxPMFEUAS15MinTr_Type()
)
tnDwStatsRxPMFEUAS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxPMFEUAS15MinTr.setStatus("current")
_TnDwStatsRxSMBIAES15MinTr_Type = Counter64
_TnDwStatsRxSMBIAES15MinTr_Object = MibScalar
tnDwStatsRxSMBIAES15MinTr = _TnDwStatsRxSMBIAES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 81),
    _TnDwStatsRxSMBIAES15MinTr_Type()
)
tnDwStatsRxSMBIAES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxSMBIAES15MinTr.setStatus("current")
_TnDwStatsRxSMIAES15MinTr_Type = Counter64
_TnDwStatsRxSMIAES15MinTr_Object = MibScalar
tnDwStatsRxSMIAES15MinTr = _TnDwStatsRxSMIAES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 82),
    _TnDwStatsRxSMIAES15MinTr_Type()
)
tnDwStatsRxSMIAES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxSMIAES15MinTr.setStatus("current")
_TnDwStatsRxBERPreFEC15MinTr_Type = Counter64
_TnDwStatsRxBERPreFEC15MinTr_Object = MibScalar
tnDwStatsRxBERPreFEC15MinTr = _TnDwStatsRxBERPreFEC15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 83),
    _TnDwStatsRxBERPreFEC15MinTr_Type()
)
tnDwStatsRxBERPreFEC15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxBERPreFEC15MinTr.setStatus("current")
_TnDwStatsRxBERPostFEC15MinTr_Type = Counter64
_TnDwStatsRxBERPostFEC15MinTr_Object = MibScalar
tnDwStatsRxBERPostFEC15MinTr = _TnDwStatsRxBERPostFEC15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 84),
    _TnDwStatsRxBERPostFEC15MinTr_Type()
)
tnDwStatsRxBERPostFEC15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxBERPostFEC15MinTr.setStatus("current")
_TnDwStatsOtu1RxSMFEBIP8ErrCnt1DayTr_Type = Counter64
_TnDwStatsOtu1RxSMFEBIP8ErrCnt1DayTr_Object = MibScalar
tnDwStatsOtu1RxSMFEBIP8ErrCnt1DayTr = _TnDwStatsOtu1RxSMFEBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 85),
    _TnDwStatsOtu1RxSMFEBIP8ErrCnt1DayTr_Type()
)
tnDwStatsOtu1RxSMFEBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOtu1RxSMFEBIP8ErrCnt1DayTr.setStatus("current")
_TnDwStatsOtu2RxSMFEBIP8ErrCnt1DayTr_Type = Counter64
_TnDwStatsOtu2RxSMFEBIP8ErrCnt1DayTr_Object = MibScalar
tnDwStatsOtu2RxSMFEBIP8ErrCnt1DayTr = _TnDwStatsOtu2RxSMFEBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 86),
    _TnDwStatsOtu2RxSMFEBIP8ErrCnt1DayTr_Type()
)
tnDwStatsOtu2RxSMFEBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOtu2RxSMFEBIP8ErrCnt1DayTr.setStatus("current")
_TnDwStatsOtu3RxSMFEBIP8ErrCnt1DayTr_Type = Counter64
_TnDwStatsOtu3RxSMFEBIP8ErrCnt1DayTr_Object = MibScalar
tnDwStatsOtu3RxSMFEBIP8ErrCnt1DayTr = _TnDwStatsOtu3RxSMFEBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 87),
    _TnDwStatsOtu3RxSMFEBIP8ErrCnt1DayTr_Type()
)
tnDwStatsOtu3RxSMFEBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOtu3RxSMFEBIP8ErrCnt1DayTr.setStatus("current")
_TnDwStatsOtu4RxSMFEBIP8ErrCnt1DayTr_Type = Counter64
_TnDwStatsOtu4RxSMFEBIP8ErrCnt1DayTr_Object = MibScalar
tnDwStatsOtu4RxSMFEBIP8ErrCnt1DayTr = _TnDwStatsOtu4RxSMFEBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 88),
    _TnDwStatsOtu4RxSMFEBIP8ErrCnt1DayTr_Type()
)
tnDwStatsOtu4RxSMFEBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOtu4RxSMFEBIP8ErrCnt1DayTr.setStatus("current")
_TnDwStatsOdu1RxPMFEBIP8ErrCnt1DayTr_Type = Counter64
_TnDwStatsOdu1RxPMFEBIP8ErrCnt1DayTr_Object = MibScalar
tnDwStatsOdu1RxPMFEBIP8ErrCnt1DayTr = _TnDwStatsOdu1RxPMFEBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 89),
    _TnDwStatsOdu1RxPMFEBIP8ErrCnt1DayTr_Type()
)
tnDwStatsOdu1RxPMFEBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOdu1RxPMFEBIP8ErrCnt1DayTr.setStatus("current")
_TnDwStatsOdu2RxPMFEBIP8ErrCnt1DayTr_Type = Counter64
_TnDwStatsOdu2RxPMFEBIP8ErrCnt1DayTr_Object = MibScalar
tnDwStatsOdu2RxPMFEBIP8ErrCnt1DayTr = _TnDwStatsOdu2RxPMFEBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 90),
    _TnDwStatsOdu2RxPMFEBIP8ErrCnt1DayTr_Type()
)
tnDwStatsOdu2RxPMFEBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOdu2RxPMFEBIP8ErrCnt1DayTr.setStatus("current")
_TnDwStatsOdu3RxPMFEBIP8ErrCnt1DayTr_Type = Counter64
_TnDwStatsOdu3RxPMFEBIP8ErrCnt1DayTr_Object = MibScalar
tnDwStatsOdu3RxPMFEBIP8ErrCnt1DayTr = _TnDwStatsOdu3RxPMFEBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 91),
    _TnDwStatsOdu3RxPMFEBIP8ErrCnt1DayTr_Type()
)
tnDwStatsOdu3RxPMFEBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOdu3RxPMFEBIP8ErrCnt1DayTr.setStatus("current")
_TnDwStatsOdu4RxPMFEBIP8ErrCnt1DayTr_Type = Counter64
_TnDwStatsOdu4RxPMFEBIP8ErrCnt1DayTr_Object = MibScalar
tnDwStatsOdu4RxPMFEBIP8ErrCnt1DayTr = _TnDwStatsOdu4RxPMFEBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 92),
    _TnDwStatsOdu4RxPMFEBIP8ErrCnt1DayTr_Type()
)
tnDwStatsOdu4RxPMFEBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOdu4RxPMFEBIP8ErrCnt1DayTr.setStatus("current")
_TnDwStatsRxSMFEES1DayTr_Type = Counter64
_TnDwStatsRxSMFEES1DayTr_Object = MibScalar
tnDwStatsRxSMFEES1DayTr = _TnDwStatsRxSMFEES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 93),
    _TnDwStatsRxSMFEES1DayTr_Type()
)
tnDwStatsRxSMFEES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxSMFEES1DayTr.setStatus("current")
_TnDwStatsRxPMFEES1DayTr_Type = Counter64
_TnDwStatsRxPMFEES1DayTr_Object = MibScalar
tnDwStatsRxPMFEES1DayTr = _TnDwStatsRxPMFEES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 94),
    _TnDwStatsRxPMFEES1DayTr_Type()
)
tnDwStatsRxPMFEES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxPMFEES1DayTr.setStatus("current")
_TnDwStatsRxSMFESES1DayTr_Type = Counter64
_TnDwStatsRxSMFESES1DayTr_Object = MibScalar
tnDwStatsRxSMFESES1DayTr = _TnDwStatsRxSMFESES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 95),
    _TnDwStatsRxSMFESES1DayTr_Type()
)
tnDwStatsRxSMFESES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxSMFESES1DayTr.setStatus("current")
_TnDwStatsRxPMFESES1DayTr_Type = Counter64
_TnDwStatsRxPMFESES1DayTr_Object = MibScalar
tnDwStatsRxPMFESES1DayTr = _TnDwStatsRxPMFESES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 96),
    _TnDwStatsRxPMFESES1DayTr_Type()
)
tnDwStatsRxPMFESES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxPMFESES1DayTr.setStatus("current")
_TnDwStatsRxSMFEUAS1DayTr_Type = Counter64
_TnDwStatsRxSMFEUAS1DayTr_Object = MibScalar
tnDwStatsRxSMFEUAS1DayTr = _TnDwStatsRxSMFEUAS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 97),
    _TnDwStatsRxSMFEUAS1DayTr_Type()
)
tnDwStatsRxSMFEUAS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxSMFEUAS1DayTr.setStatus("current")
_TnDwStatsRxPMFEUAS1DayTr_Type = Counter64
_TnDwStatsRxPMFEUAS1DayTr_Object = MibScalar
tnDwStatsRxPMFEUAS1DayTr = _TnDwStatsRxPMFEUAS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 98),
    _TnDwStatsRxPMFEUAS1DayTr_Type()
)
tnDwStatsRxPMFEUAS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxPMFEUAS1DayTr.setStatus("current")
_TnDwStatsRxSMBIAES1DayTr_Type = Counter64
_TnDwStatsRxSMBIAES1DayTr_Object = MibScalar
tnDwStatsRxSMBIAES1DayTr = _TnDwStatsRxSMBIAES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 99),
    _TnDwStatsRxSMBIAES1DayTr_Type()
)
tnDwStatsRxSMBIAES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxSMBIAES1DayTr.setStatus("current")
_TnDwStatsRxSMIAES1DayTr_Type = Counter64
_TnDwStatsRxSMIAES1DayTr_Object = MibScalar
tnDwStatsRxSMIAES1DayTr = _TnDwStatsRxSMIAES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 100),
    _TnDwStatsRxSMIAES1DayTr_Type()
)
tnDwStatsRxSMIAES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxSMIAES1DayTr.setStatus("current")
_TnDwStatsRxBERPreFEC1DayTr_Type = Counter64
_TnDwStatsRxBERPreFEC1DayTr_Object = MibScalar
tnDwStatsRxBERPreFEC1DayTr = _TnDwStatsRxBERPreFEC1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 101),
    _TnDwStatsRxBERPreFEC1DayTr_Type()
)
tnDwStatsRxBERPreFEC1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxBERPreFEC1DayTr.setStatus("current")
_TnDwStatsRxBERPostFEC1DayTr_Type = Counter64
_TnDwStatsRxBERPostFEC1DayTr_Object = MibScalar
tnDwStatsRxBERPostFEC1DayTr = _TnDwStatsRxBERPostFEC1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 102),
    _TnDwStatsRxBERPostFEC1DayTr_Type()
)
tnDwStatsRxBERPostFEC1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxBERPostFEC1DayTr.setStatus("current")
_TnDwStatsOtu1RxSMFEBIP8ErrCnt15MinRtr_Type = Counter64
_TnDwStatsOtu1RxSMFEBIP8ErrCnt15MinRtr_Object = MibScalar
tnDwStatsOtu1RxSMFEBIP8ErrCnt15MinRtr = _TnDwStatsOtu1RxSMFEBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 103),
    _TnDwStatsOtu1RxSMFEBIP8ErrCnt15MinRtr_Type()
)
tnDwStatsOtu1RxSMFEBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOtu1RxSMFEBIP8ErrCnt15MinRtr.setStatus("current")
_TnDwStatsOtu2RxSMFEBIP8ErrCnt15MinRtr_Type = Counter64
_TnDwStatsOtu2RxSMFEBIP8ErrCnt15MinRtr_Object = MibScalar
tnDwStatsOtu2RxSMFEBIP8ErrCnt15MinRtr = _TnDwStatsOtu2RxSMFEBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 104),
    _TnDwStatsOtu2RxSMFEBIP8ErrCnt15MinRtr_Type()
)
tnDwStatsOtu2RxSMFEBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOtu2RxSMFEBIP8ErrCnt15MinRtr.setStatus("current")
_TnDwStatsOtu3RxSMFEBIP8ErrCnt15MinRtr_Type = Counter64
_TnDwStatsOtu3RxSMFEBIP8ErrCnt15MinRtr_Object = MibScalar
tnDwStatsOtu3RxSMFEBIP8ErrCnt15MinRtr = _TnDwStatsOtu3RxSMFEBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 105),
    _TnDwStatsOtu3RxSMFEBIP8ErrCnt15MinRtr_Type()
)
tnDwStatsOtu3RxSMFEBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOtu3RxSMFEBIP8ErrCnt15MinRtr.setStatus("current")
_TnDwStatsOtu4RxSMFEBIP8ErrCnt15MinRtr_Type = Counter64
_TnDwStatsOtu4RxSMFEBIP8ErrCnt15MinRtr_Object = MibScalar
tnDwStatsOtu4RxSMFEBIP8ErrCnt15MinRtr = _TnDwStatsOtu4RxSMFEBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 106),
    _TnDwStatsOtu4RxSMFEBIP8ErrCnt15MinRtr_Type()
)
tnDwStatsOtu4RxSMFEBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOtu4RxSMFEBIP8ErrCnt15MinRtr.setStatus("current")
_TnDwStatsOdu1RxPMFEBIP8ErrCnt15MinRtr_Type = Counter64
_TnDwStatsOdu1RxPMFEBIP8ErrCnt15MinRtr_Object = MibScalar
tnDwStatsOdu1RxPMFEBIP8ErrCnt15MinRtr = _TnDwStatsOdu1RxPMFEBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 107),
    _TnDwStatsOdu1RxPMFEBIP8ErrCnt15MinRtr_Type()
)
tnDwStatsOdu1RxPMFEBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOdu1RxPMFEBIP8ErrCnt15MinRtr.setStatus("current")
_TnDwStatsOdu2RxPMFEBIP8ErrCnt15MinRtr_Type = Counter64
_TnDwStatsOdu2RxPMFEBIP8ErrCnt15MinRtr_Object = MibScalar
tnDwStatsOdu2RxPMFEBIP8ErrCnt15MinRtr = _TnDwStatsOdu2RxPMFEBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 108),
    _TnDwStatsOdu2RxPMFEBIP8ErrCnt15MinRtr_Type()
)
tnDwStatsOdu2RxPMFEBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOdu2RxPMFEBIP8ErrCnt15MinRtr.setStatus("current")
_TnDwStatsOdu3RxPMFEBIP8ErrCnt15MinRtr_Type = Counter64
_TnDwStatsOdu3RxPMFEBIP8ErrCnt15MinRtr_Object = MibScalar
tnDwStatsOdu3RxPMFEBIP8ErrCnt15MinRtr = _TnDwStatsOdu3RxPMFEBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 109),
    _TnDwStatsOdu3RxPMFEBIP8ErrCnt15MinRtr_Type()
)
tnDwStatsOdu3RxPMFEBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOdu3RxPMFEBIP8ErrCnt15MinRtr.setStatus("current")
_TnDwStatsOdu4RxPMFEBIP8ErrCnt15MinRtr_Type = Counter64
_TnDwStatsOdu4RxPMFEBIP8ErrCnt15MinRtr_Object = MibScalar
tnDwStatsOdu4RxPMFEBIP8ErrCnt15MinRtr = _TnDwStatsOdu4RxPMFEBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 110),
    _TnDwStatsOdu4RxPMFEBIP8ErrCnt15MinRtr_Type()
)
tnDwStatsOdu4RxPMFEBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsOdu4RxPMFEBIP8ErrCnt15MinRtr.setStatus("current")
_TnDwStatsRxSMFEES15MinRtr_Type = Counter64
_TnDwStatsRxSMFEES15MinRtr_Object = MibScalar
tnDwStatsRxSMFEES15MinRtr = _TnDwStatsRxSMFEES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 111),
    _TnDwStatsRxSMFEES15MinRtr_Type()
)
tnDwStatsRxSMFEES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxSMFEES15MinRtr.setStatus("current")
_TnDwStatsRxPMFEES15MinRtr_Type = Counter64
_TnDwStatsRxPMFEES15MinRtr_Object = MibScalar
tnDwStatsRxPMFEES15MinRtr = _TnDwStatsRxPMFEES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 112),
    _TnDwStatsRxPMFEES15MinRtr_Type()
)
tnDwStatsRxPMFEES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxPMFEES15MinRtr.setStatus("current")
_TnDwStatsRxSMFESES15MinRtr_Type = Counter64
_TnDwStatsRxSMFESES15MinRtr_Object = MibScalar
tnDwStatsRxSMFESES15MinRtr = _TnDwStatsRxSMFESES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 113),
    _TnDwStatsRxSMFESES15MinRtr_Type()
)
tnDwStatsRxSMFESES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxSMFESES15MinRtr.setStatus("current")
_TnDwStatsRxPMFESES15MinRtr_Type = Counter64
_TnDwStatsRxPMFESES15MinRtr_Object = MibScalar
tnDwStatsRxPMFESES15MinRtr = _TnDwStatsRxPMFESES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 114),
    _TnDwStatsRxPMFESES15MinRtr_Type()
)
tnDwStatsRxPMFESES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxPMFESES15MinRtr.setStatus("current")
_TnDwStatsRxSMFEUAS15MinRtr_Type = Counter64
_TnDwStatsRxSMFEUAS15MinRtr_Object = MibScalar
tnDwStatsRxSMFEUAS15MinRtr = _TnDwStatsRxSMFEUAS15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 115),
    _TnDwStatsRxSMFEUAS15MinRtr_Type()
)
tnDwStatsRxSMFEUAS15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxSMFEUAS15MinRtr.setStatus("current")
_TnDwStatsRxPMFEUAS15MinRtr_Type = Counter64
_TnDwStatsRxPMFEUAS15MinRtr_Object = MibScalar
tnDwStatsRxPMFEUAS15MinRtr = _TnDwStatsRxPMFEUAS15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 116),
    _TnDwStatsRxPMFEUAS15MinRtr_Type()
)
tnDwStatsRxPMFEUAS15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxPMFEUAS15MinRtr.setStatus("current")
_TnDwStatsRxSMBIAES15MinRtr_Type = Counter64
_TnDwStatsRxSMBIAES15MinRtr_Object = MibScalar
tnDwStatsRxSMBIAES15MinRtr = _TnDwStatsRxSMBIAES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 117),
    _TnDwStatsRxSMBIAES15MinRtr_Type()
)
tnDwStatsRxSMBIAES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxSMBIAES15MinRtr.setStatus("current")
_TnDwStatsRxSMIAES15MinRtr_Type = Counter64
_TnDwStatsRxSMIAES15MinRtr_Object = MibScalar
tnDwStatsRxSMIAES15MinRtr = _TnDwStatsRxSMIAES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 118),
    _TnDwStatsRxSMIAES15MinRtr_Type()
)
tnDwStatsRxSMIAES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxSMIAES15MinRtr.setStatus("current")
_TnDwStatsRxBERPreFEC15MinRtr_Type = Counter64
_TnDwStatsRxBERPreFEC15MinRtr_Object = MibScalar
tnDwStatsRxBERPreFEC15MinRtr = _TnDwStatsRxBERPreFEC15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 119),
    _TnDwStatsRxBERPreFEC15MinRtr_Type()
)
tnDwStatsRxBERPreFEC15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxBERPreFEC15MinRtr.setStatus("current")
_TnDwStatsRxBERPostFEC15MinRtr_Type = Counter64
_TnDwStatsRxBERPostFEC15MinRtr_Object = MibScalar
tnDwStatsRxBERPostFEC15MinRtr = _TnDwStatsRxBERPostFEC15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 10, 120),
    _TnDwStatsRxBERPostFEC15MinRtr_Type()
)
tnDwStatsRxBERPostFEC15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDwStatsRxBERPostFEC15MinRtr.setStatus("current")
_TnStatisticsPcsScalars_ObjectIdentity = ObjectIdentity
tnStatisticsPcsScalars = _TnStatisticsPcsScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11)
)
_TnPcsStats100GBERxCV15MinTr_Type = Counter32
_TnPcsStats100GBERxCV15MinTr_Object = MibScalar
tnPcsStats100GBERxCV15MinTr = _TnPcsStats100GBERxCV15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 1),
    _TnPcsStats100GBERxCV15MinTr_Type()
)
tnPcsStats100GBERxCV15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats100GBERxCV15MinTr.setStatus("current")
_TnPcsStats40GBERxCV15MinTr_Type = Counter32
_TnPcsStats40GBERxCV15MinTr_Object = MibScalar
tnPcsStats40GBERxCV15MinTr = _TnPcsStats40GBERxCV15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 2),
    _TnPcsStats40GBERxCV15MinTr_Type()
)
tnPcsStats40GBERxCV15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats40GBERxCV15MinTr.setStatus("current")
_TnPcsStats10GBERxCV15MinTr_Type = Counter32
_TnPcsStats10GBERxCV15MinTr_Object = MibScalar
tnPcsStats10GBERxCV15MinTr = _TnPcsStats10GBERxCV15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 3),
    _TnPcsStats10GBERxCV15MinTr_Type()
)
tnPcsStats10GBERxCV15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats10GBERxCV15MinTr.setStatus("current")
_TnPcsStatsGBERxCV15MinTr_Type = Counter32
_TnPcsStatsGBERxCV15MinTr_Object = MibScalar
tnPcsStatsGBERxCV15MinTr = _TnPcsStatsGBERxCV15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 4),
    _TnPcsStatsGBERxCV15MinTr_Type()
)
tnPcsStatsGBERxCV15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsGBERxCV15MinTr.setStatus("current")
_TnPcsStats16GFCRxCV15MinTr_Type = Counter32
_TnPcsStats16GFCRxCV15MinTr_Object = MibScalar
tnPcsStats16GFCRxCV15MinTr = _TnPcsStats16GFCRxCV15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 5),
    _TnPcsStats16GFCRxCV15MinTr_Type()
)
tnPcsStats16GFCRxCV15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats16GFCRxCV15MinTr.setStatus("current")
_TnPcsStats10GFCRxCV15MinTr_Type = Counter32
_TnPcsStats10GFCRxCV15MinTr_Object = MibScalar
tnPcsStats10GFCRxCV15MinTr = _TnPcsStats10GFCRxCV15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 6),
    _TnPcsStats10GFCRxCV15MinTr_Type()
)
tnPcsStats10GFCRxCV15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats10GFCRxCV15MinTr.setStatus("current")
_TnPcsStats8GFCRxCV15MinTr_Type = Counter32
_TnPcsStats8GFCRxCV15MinTr_Object = MibScalar
tnPcsStats8GFCRxCV15MinTr = _TnPcsStats8GFCRxCV15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 7),
    _TnPcsStats8GFCRxCV15MinTr_Type()
)
tnPcsStats8GFCRxCV15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats8GFCRxCV15MinTr.setStatus("current")
_TnPcsStats4GFCRxCV15MinTr_Type = Counter32
_TnPcsStats4GFCRxCV15MinTr_Object = MibScalar
tnPcsStats4GFCRxCV15MinTr = _TnPcsStats4GFCRxCV15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 8),
    _TnPcsStats4GFCRxCV15MinTr_Type()
)
tnPcsStats4GFCRxCV15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats4GFCRxCV15MinTr.setStatus("current")
_TnPcsStats2GFCRxCV15MinTr_Type = Counter32
_TnPcsStats2GFCRxCV15MinTr_Object = MibScalar
tnPcsStats2GFCRxCV15MinTr = _TnPcsStats2GFCRxCV15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 9),
    _TnPcsStats2GFCRxCV15MinTr_Type()
)
tnPcsStats2GFCRxCV15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats2GFCRxCV15MinTr.setStatus("current")
_TnPcsStatsGFCRxCV15MinTr_Type = Counter32
_TnPcsStatsGFCRxCV15MinTr_Object = MibScalar
tnPcsStatsGFCRxCV15MinTr = _TnPcsStatsGFCRxCV15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 10),
    _TnPcsStatsGFCRxCV15MinTr_Type()
)
tnPcsStatsGFCRxCV15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsGFCRxCV15MinTr.setStatus("current")
_TnPcsStatsRxES15MinTr_Type = Counter32
_TnPcsStatsRxES15MinTr_Object = MibScalar
tnPcsStatsRxES15MinTr = _TnPcsStatsRxES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 11),
    _TnPcsStatsRxES15MinTr_Type()
)
tnPcsStatsRxES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsRxES15MinTr.setStatus("current")
_TnPcsStatsRxSES15MinTr_Type = Counter32
_TnPcsStatsRxSES15MinTr_Object = MibScalar
tnPcsStatsRxSES15MinTr = _TnPcsStatsRxSES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 12),
    _TnPcsStatsRxSES15MinTr_Type()
)
tnPcsStatsRxSES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsRxSES15MinTr.setStatus("current")
_TnPcsStatsRxSEFS15MinTr_Type = Counter32
_TnPcsStatsRxSEFS15MinTr_Object = MibScalar
tnPcsStatsRxSEFS15MinTr = _TnPcsStatsRxSEFS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 13),
    _TnPcsStatsRxSEFS15MinTr_Type()
)
tnPcsStatsRxSEFS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsRxSEFS15MinTr.setStatus("current")
_TnPcsStats100GBERxCV1DayTr_Type = Counter32
_TnPcsStats100GBERxCV1DayTr_Object = MibScalar
tnPcsStats100GBERxCV1DayTr = _TnPcsStats100GBERxCV1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 14),
    _TnPcsStats100GBERxCV1DayTr_Type()
)
tnPcsStats100GBERxCV1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats100GBERxCV1DayTr.setStatus("current")
_TnPcsStats40GBERxCV1DayTr_Type = Counter32
_TnPcsStats40GBERxCV1DayTr_Object = MibScalar
tnPcsStats40GBERxCV1DayTr = _TnPcsStats40GBERxCV1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 15),
    _TnPcsStats40GBERxCV1DayTr_Type()
)
tnPcsStats40GBERxCV1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats40GBERxCV1DayTr.setStatus("current")
_TnPcsStats10GBERxCV1DayTr_Type = Counter32
_TnPcsStats10GBERxCV1DayTr_Object = MibScalar
tnPcsStats10GBERxCV1DayTr = _TnPcsStats10GBERxCV1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 16),
    _TnPcsStats10GBERxCV1DayTr_Type()
)
tnPcsStats10GBERxCV1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats10GBERxCV1DayTr.setStatus("current")
_TnPcsStatsGBERxCV1DayTr_Type = Counter32
_TnPcsStatsGBERxCV1DayTr_Object = MibScalar
tnPcsStatsGBERxCV1DayTr = _TnPcsStatsGBERxCV1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 17),
    _TnPcsStatsGBERxCV1DayTr_Type()
)
tnPcsStatsGBERxCV1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsGBERxCV1DayTr.setStatus("current")
_TnPcsStats16GFCRxCV1DayTr_Type = Counter32
_TnPcsStats16GFCRxCV1DayTr_Object = MibScalar
tnPcsStats16GFCRxCV1DayTr = _TnPcsStats16GFCRxCV1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 18),
    _TnPcsStats16GFCRxCV1DayTr_Type()
)
tnPcsStats16GFCRxCV1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats16GFCRxCV1DayTr.setStatus("current")
_TnPcsStats10GFCRxCV1DayTr_Type = Counter32
_TnPcsStats10GFCRxCV1DayTr_Object = MibScalar
tnPcsStats10GFCRxCV1DayTr = _TnPcsStats10GFCRxCV1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 19),
    _TnPcsStats10GFCRxCV1DayTr_Type()
)
tnPcsStats10GFCRxCV1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats10GFCRxCV1DayTr.setStatus("current")
_TnPcsStats8GFCRxCV1DayTr_Type = Counter32
_TnPcsStats8GFCRxCV1DayTr_Object = MibScalar
tnPcsStats8GFCRxCV1DayTr = _TnPcsStats8GFCRxCV1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 20),
    _TnPcsStats8GFCRxCV1DayTr_Type()
)
tnPcsStats8GFCRxCV1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats8GFCRxCV1DayTr.setStatus("current")
_TnPcsStats4GFCRxCV1DayTr_Type = Counter32
_TnPcsStats4GFCRxCV1DayTr_Object = MibScalar
tnPcsStats4GFCRxCV1DayTr = _TnPcsStats4GFCRxCV1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 21),
    _TnPcsStats4GFCRxCV1DayTr_Type()
)
tnPcsStats4GFCRxCV1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats4GFCRxCV1DayTr.setStatus("current")
_TnPcsStats2GFCRxCV1DayTr_Type = Counter32
_TnPcsStats2GFCRxCV1DayTr_Object = MibScalar
tnPcsStats2GFCRxCV1DayTr = _TnPcsStats2GFCRxCV1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 22),
    _TnPcsStats2GFCRxCV1DayTr_Type()
)
tnPcsStats2GFCRxCV1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats2GFCRxCV1DayTr.setStatus("current")
_TnPcsStatsGFCRxCV1DayTr_Type = Counter32
_TnPcsStatsGFCRxCV1DayTr_Object = MibScalar
tnPcsStatsGFCRxCV1DayTr = _TnPcsStatsGFCRxCV1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 23),
    _TnPcsStatsGFCRxCV1DayTr_Type()
)
tnPcsStatsGFCRxCV1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsGFCRxCV1DayTr.setStatus("current")
_TnPcsStatsRxES1DayTr_Type = Counter32
_TnPcsStatsRxES1DayTr_Object = MibScalar
tnPcsStatsRxES1DayTr = _TnPcsStatsRxES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 24),
    _TnPcsStatsRxES1DayTr_Type()
)
tnPcsStatsRxES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsRxES1DayTr.setStatus("current")
_TnPcsStatsRxSES1DayTr_Type = Counter32
_TnPcsStatsRxSES1DayTr_Object = MibScalar
tnPcsStatsRxSES1DayTr = _TnPcsStatsRxSES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 25),
    _TnPcsStatsRxSES1DayTr_Type()
)
tnPcsStatsRxSES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsRxSES1DayTr.setStatus("current")
_TnPcsStatsRxSEFS1DayTr_Type = Counter32
_TnPcsStatsRxSEFS1DayTr_Object = MibScalar
tnPcsStatsRxSEFS1DayTr = _TnPcsStatsRxSEFS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 26),
    _TnPcsStatsRxSEFS1DayTr_Type()
)
tnPcsStatsRxSEFS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsRxSEFS1DayTr.setStatus("current")
_TnPcsStats100GBERxCV15MinRtr_Type = Counter32
_TnPcsStats100GBERxCV15MinRtr_Object = MibScalar
tnPcsStats100GBERxCV15MinRtr = _TnPcsStats100GBERxCV15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 27),
    _TnPcsStats100GBERxCV15MinRtr_Type()
)
tnPcsStats100GBERxCV15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats100GBERxCV15MinRtr.setStatus("current")
_TnPcsStats40GBERxCV15MinRtr_Type = Counter32
_TnPcsStats40GBERxCV15MinRtr_Object = MibScalar
tnPcsStats40GBERxCV15MinRtr = _TnPcsStats40GBERxCV15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 28),
    _TnPcsStats40GBERxCV15MinRtr_Type()
)
tnPcsStats40GBERxCV15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats40GBERxCV15MinRtr.setStatus("current")
_TnPcsStats10GBERxCV15MinRtr_Type = Counter32
_TnPcsStats10GBERxCV15MinRtr_Object = MibScalar
tnPcsStats10GBERxCV15MinRtr = _TnPcsStats10GBERxCV15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 29),
    _TnPcsStats10GBERxCV15MinRtr_Type()
)
tnPcsStats10GBERxCV15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats10GBERxCV15MinRtr.setStatus("current")
_TnPcsStatsGBERxCV15MinRtr_Type = Counter32
_TnPcsStatsGBERxCV15MinRtr_Object = MibScalar
tnPcsStatsGBERxCV15MinRtr = _TnPcsStatsGBERxCV15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 30),
    _TnPcsStatsGBERxCV15MinRtr_Type()
)
tnPcsStatsGBERxCV15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsGBERxCV15MinRtr.setStatus("current")
_TnPcsStats16GFCRxCV15MinRtr_Type = Counter32
_TnPcsStats16GFCRxCV15MinRtr_Object = MibScalar
tnPcsStats16GFCRxCV15MinRtr = _TnPcsStats16GFCRxCV15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 31),
    _TnPcsStats16GFCRxCV15MinRtr_Type()
)
tnPcsStats16GFCRxCV15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats16GFCRxCV15MinRtr.setStatus("current")
_TnPcsStats10GFCRxCV15MinRtr_Type = Counter32
_TnPcsStats10GFCRxCV15MinRtr_Object = MibScalar
tnPcsStats10GFCRxCV15MinRtr = _TnPcsStats10GFCRxCV15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 32),
    _TnPcsStats10GFCRxCV15MinRtr_Type()
)
tnPcsStats10GFCRxCV15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats10GFCRxCV15MinRtr.setStatus("current")
_TnPcsStats8GFCRxCV15MinRtr_Type = Counter32
_TnPcsStats8GFCRxCV15MinRtr_Object = MibScalar
tnPcsStats8GFCRxCV15MinRtr = _TnPcsStats8GFCRxCV15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 33),
    _TnPcsStats8GFCRxCV15MinRtr_Type()
)
tnPcsStats8GFCRxCV15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats8GFCRxCV15MinRtr.setStatus("current")
_TnPcsStats4GFCRxCV15MinRtr_Type = Counter32
_TnPcsStats4GFCRxCV15MinRtr_Object = MibScalar
tnPcsStats4GFCRxCV15MinRtr = _TnPcsStats4GFCRxCV15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 34),
    _TnPcsStats4GFCRxCV15MinRtr_Type()
)
tnPcsStats4GFCRxCV15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats4GFCRxCV15MinRtr.setStatus("current")
_TnPcsStats2GFCRxCV15MinRtr_Type = Counter32
_TnPcsStats2GFCRxCV15MinRtr_Object = MibScalar
tnPcsStats2GFCRxCV15MinRtr = _TnPcsStats2GFCRxCV15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 35),
    _TnPcsStats2GFCRxCV15MinRtr_Type()
)
tnPcsStats2GFCRxCV15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats2GFCRxCV15MinRtr.setStatus("current")
_TnPcsStatsGFCRxCV15MinRtr_Type = Counter32
_TnPcsStatsGFCRxCV15MinRtr_Object = MibScalar
tnPcsStatsGFCRxCV15MinRtr = _TnPcsStatsGFCRxCV15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 36),
    _TnPcsStatsGFCRxCV15MinRtr_Type()
)
tnPcsStatsGFCRxCV15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsGFCRxCV15MinRtr.setStatus("current")
_TnPcsStatsRxES15MinRtr_Type = Counter32
_TnPcsStatsRxES15MinRtr_Object = MibScalar
tnPcsStatsRxES15MinRtr = _TnPcsStatsRxES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 37),
    _TnPcsStatsRxES15MinRtr_Type()
)
tnPcsStatsRxES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsRxES15MinRtr.setStatus("current")
_TnPcsStatsRxSES15MinRtr_Type = Counter32
_TnPcsStatsRxSES15MinRtr_Object = MibScalar
tnPcsStatsRxSES15MinRtr = _TnPcsStatsRxSES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 38),
    _TnPcsStatsRxSES15MinRtr_Type()
)
tnPcsStatsRxSES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsRxSES15MinRtr.setStatus("current")
_TnPcsStatsRxSEFS15MinRtr_Type = Counter32
_TnPcsStatsRxSEFS15MinRtr_Object = MibScalar
tnPcsStatsRxSEFS15MinRtr = _TnPcsStatsRxSEFS15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 39),
    _TnPcsStatsRxSEFS15MinRtr_Type()
)
tnPcsStatsRxSEFS15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsRxSEFS15MinRtr.setStatus("current")
_TnPcsStats100GBETxCV15MinTr_Type = Counter32
_TnPcsStats100GBETxCV15MinTr_Object = MibScalar
tnPcsStats100GBETxCV15MinTr = _TnPcsStats100GBETxCV15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 40),
    _TnPcsStats100GBETxCV15MinTr_Type()
)
tnPcsStats100GBETxCV15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats100GBETxCV15MinTr.setStatus("current")
_TnPcsStats40GBETxCV15MinTr_Type = Counter32
_TnPcsStats40GBETxCV15MinTr_Object = MibScalar
tnPcsStats40GBETxCV15MinTr = _TnPcsStats40GBETxCV15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 41),
    _TnPcsStats40GBETxCV15MinTr_Type()
)
tnPcsStats40GBETxCV15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats40GBETxCV15MinTr.setStatus("current")
_TnPcsStats10GBETxCV15MinTr_Type = Counter32
_TnPcsStats10GBETxCV15MinTr_Object = MibScalar
tnPcsStats10GBETxCV15MinTr = _TnPcsStats10GBETxCV15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 42),
    _TnPcsStats10GBETxCV15MinTr_Type()
)
tnPcsStats10GBETxCV15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats10GBETxCV15MinTr.setStatus("current")
_TnPcsStatsGBETxCV15MinTr_Type = Counter32
_TnPcsStatsGBETxCV15MinTr_Object = MibScalar
tnPcsStatsGBETxCV15MinTr = _TnPcsStatsGBETxCV15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 43),
    _TnPcsStatsGBETxCV15MinTr_Type()
)
tnPcsStatsGBETxCV15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsGBETxCV15MinTr.setStatus("current")
_TnPcsStats16GFCTxCV15MinTr_Type = Counter32
_TnPcsStats16GFCTxCV15MinTr_Object = MibScalar
tnPcsStats16GFCTxCV15MinTr = _TnPcsStats16GFCTxCV15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 44),
    _TnPcsStats16GFCTxCV15MinTr_Type()
)
tnPcsStats16GFCTxCV15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats16GFCTxCV15MinTr.setStatus("current")
_TnPcsStats10GFCTxCV15MinTr_Type = Counter32
_TnPcsStats10GFCTxCV15MinTr_Object = MibScalar
tnPcsStats10GFCTxCV15MinTr = _TnPcsStats10GFCTxCV15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 45),
    _TnPcsStats10GFCTxCV15MinTr_Type()
)
tnPcsStats10GFCTxCV15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats10GFCTxCV15MinTr.setStatus("current")
_TnPcsStats8GFCTxCV15MinTr_Type = Counter32
_TnPcsStats8GFCTxCV15MinTr_Object = MibScalar
tnPcsStats8GFCTxCV15MinTr = _TnPcsStats8GFCTxCV15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 46),
    _TnPcsStats8GFCTxCV15MinTr_Type()
)
tnPcsStats8GFCTxCV15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats8GFCTxCV15MinTr.setStatus("current")
_TnPcsStats4GFCTxCV15MinTr_Type = Counter32
_TnPcsStats4GFCTxCV15MinTr_Object = MibScalar
tnPcsStats4GFCTxCV15MinTr = _TnPcsStats4GFCTxCV15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 47),
    _TnPcsStats4GFCTxCV15MinTr_Type()
)
tnPcsStats4GFCTxCV15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats4GFCTxCV15MinTr.setStatus("current")
_TnPcsStats2GFCTxCV15MinTr_Type = Counter32
_TnPcsStats2GFCTxCV15MinTr_Object = MibScalar
tnPcsStats2GFCTxCV15MinTr = _TnPcsStats2GFCTxCV15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 48),
    _TnPcsStats2GFCTxCV15MinTr_Type()
)
tnPcsStats2GFCTxCV15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats2GFCTxCV15MinTr.setStatus("current")
_TnPcsStatsGFCTxCV15MinTr_Type = Counter32
_TnPcsStatsGFCTxCV15MinTr_Object = MibScalar
tnPcsStatsGFCTxCV15MinTr = _TnPcsStatsGFCTxCV15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 49),
    _TnPcsStatsGFCTxCV15MinTr_Type()
)
tnPcsStatsGFCTxCV15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsGFCTxCV15MinTr.setStatus("current")
_TnPcsStatsTxES15MinTr_Type = Counter32
_TnPcsStatsTxES15MinTr_Object = MibScalar
tnPcsStatsTxES15MinTr = _TnPcsStatsTxES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 50),
    _TnPcsStatsTxES15MinTr_Type()
)
tnPcsStatsTxES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsTxES15MinTr.setStatus("current")
_TnPcsStatsTxSES15MinTr_Type = Counter32
_TnPcsStatsTxSES15MinTr_Object = MibScalar
tnPcsStatsTxSES15MinTr = _TnPcsStatsTxSES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 51),
    _TnPcsStatsTxSES15MinTr_Type()
)
tnPcsStatsTxSES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsTxSES15MinTr.setStatus("current")
_TnPcsStatsTxSEFS15MinTr_Type = Counter32
_TnPcsStatsTxSEFS15MinTr_Object = MibScalar
tnPcsStatsTxSEFS15MinTr = _TnPcsStatsTxSEFS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 52),
    _TnPcsStatsTxSEFS15MinTr_Type()
)
tnPcsStatsTxSEFS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsTxSEFS15MinTr.setStatus("current")
_TnPcsStats100GBETxCV1DayTr_Type = Counter32
_TnPcsStats100GBETxCV1DayTr_Object = MibScalar
tnPcsStats100GBETxCV1DayTr = _TnPcsStats100GBETxCV1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 53),
    _TnPcsStats100GBETxCV1DayTr_Type()
)
tnPcsStats100GBETxCV1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats100GBETxCV1DayTr.setStatus("current")
_TnPcsStats40GBETxCV1DayTr_Type = Counter32
_TnPcsStats40GBETxCV1DayTr_Object = MibScalar
tnPcsStats40GBETxCV1DayTr = _TnPcsStats40GBETxCV1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 54),
    _TnPcsStats40GBETxCV1DayTr_Type()
)
tnPcsStats40GBETxCV1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats40GBETxCV1DayTr.setStatus("current")
_TnPcsStats10GBETxCV1DayTr_Type = Counter32
_TnPcsStats10GBETxCV1DayTr_Object = MibScalar
tnPcsStats10GBETxCV1DayTr = _TnPcsStats10GBETxCV1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 55),
    _TnPcsStats10GBETxCV1DayTr_Type()
)
tnPcsStats10GBETxCV1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats10GBETxCV1DayTr.setStatus("current")
_TnPcsStatsGBETxCV1DayTr_Type = Counter32
_TnPcsStatsGBETxCV1DayTr_Object = MibScalar
tnPcsStatsGBETxCV1DayTr = _TnPcsStatsGBETxCV1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 56),
    _TnPcsStatsGBETxCV1DayTr_Type()
)
tnPcsStatsGBETxCV1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsGBETxCV1DayTr.setStatus("current")
_TnPcsStats16GFCTxCV1DayTr_Type = Counter32
_TnPcsStats16GFCTxCV1DayTr_Object = MibScalar
tnPcsStats16GFCTxCV1DayTr = _TnPcsStats16GFCTxCV1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 57),
    _TnPcsStats16GFCTxCV1DayTr_Type()
)
tnPcsStats16GFCTxCV1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats16GFCTxCV1DayTr.setStatus("current")
_TnPcsStats10GFCTxCV1DayTr_Type = Counter32
_TnPcsStats10GFCTxCV1DayTr_Object = MibScalar
tnPcsStats10GFCTxCV1DayTr = _TnPcsStats10GFCTxCV1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 58),
    _TnPcsStats10GFCTxCV1DayTr_Type()
)
tnPcsStats10GFCTxCV1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats10GFCTxCV1DayTr.setStatus("current")
_TnPcsStats8GFCTxCV1DayTr_Type = Counter32
_TnPcsStats8GFCTxCV1DayTr_Object = MibScalar
tnPcsStats8GFCTxCV1DayTr = _TnPcsStats8GFCTxCV1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 59),
    _TnPcsStats8GFCTxCV1DayTr_Type()
)
tnPcsStats8GFCTxCV1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats8GFCTxCV1DayTr.setStatus("current")
_TnPcsStats4GFCTxCV1DayTr_Type = Counter32
_TnPcsStats4GFCTxCV1DayTr_Object = MibScalar
tnPcsStats4GFCTxCV1DayTr = _TnPcsStats4GFCTxCV1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 60),
    _TnPcsStats4GFCTxCV1DayTr_Type()
)
tnPcsStats4GFCTxCV1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats4GFCTxCV1DayTr.setStatus("current")
_TnPcsStats2GFCTxCV1DayTr_Type = Counter32
_TnPcsStats2GFCTxCV1DayTr_Object = MibScalar
tnPcsStats2GFCTxCV1DayTr = _TnPcsStats2GFCTxCV1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 61),
    _TnPcsStats2GFCTxCV1DayTr_Type()
)
tnPcsStats2GFCTxCV1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats2GFCTxCV1DayTr.setStatus("current")
_TnPcsStatsGFCTxCV1DayTr_Type = Counter32
_TnPcsStatsGFCTxCV1DayTr_Object = MibScalar
tnPcsStatsGFCTxCV1DayTr = _TnPcsStatsGFCTxCV1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 62),
    _TnPcsStatsGFCTxCV1DayTr_Type()
)
tnPcsStatsGFCTxCV1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsGFCTxCV1DayTr.setStatus("current")
_TnPcsStatsTxES1DayTr_Type = Counter32
_TnPcsStatsTxES1DayTr_Object = MibScalar
tnPcsStatsTxES1DayTr = _TnPcsStatsTxES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 63),
    _TnPcsStatsTxES1DayTr_Type()
)
tnPcsStatsTxES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsTxES1DayTr.setStatus("current")
_TnPcsStatsTxSES1DayTr_Type = Counter32
_TnPcsStatsTxSES1DayTr_Object = MibScalar
tnPcsStatsTxSES1DayTr = _TnPcsStatsTxSES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 64),
    _TnPcsStatsTxSES1DayTr_Type()
)
tnPcsStatsTxSES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsTxSES1DayTr.setStatus("current")
_TnPcsStatsTxSEFS1DayTr_Type = Counter32
_TnPcsStatsTxSEFS1DayTr_Object = MibScalar
tnPcsStatsTxSEFS1DayTr = _TnPcsStatsTxSEFS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 65),
    _TnPcsStatsTxSEFS1DayTr_Type()
)
tnPcsStatsTxSEFS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsTxSEFS1DayTr.setStatus("current")
_TnPcsStats100GBETxCV15MinRtr_Type = Counter32
_TnPcsStats100GBETxCV15MinRtr_Object = MibScalar
tnPcsStats100GBETxCV15MinRtr = _TnPcsStats100GBETxCV15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 66),
    _TnPcsStats100GBETxCV15MinRtr_Type()
)
tnPcsStats100GBETxCV15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats100GBETxCV15MinRtr.setStatus("current")
_TnPcsStats40GBETxCV15MinRtr_Type = Counter32
_TnPcsStats40GBETxCV15MinRtr_Object = MibScalar
tnPcsStats40GBETxCV15MinRtr = _TnPcsStats40GBETxCV15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 67),
    _TnPcsStats40GBETxCV15MinRtr_Type()
)
tnPcsStats40GBETxCV15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats40GBETxCV15MinRtr.setStatus("current")
_TnPcsStats10GBETxCV15MinRtr_Type = Counter32
_TnPcsStats10GBETxCV15MinRtr_Object = MibScalar
tnPcsStats10GBETxCV15MinRtr = _TnPcsStats10GBETxCV15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 68),
    _TnPcsStats10GBETxCV15MinRtr_Type()
)
tnPcsStats10GBETxCV15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats10GBETxCV15MinRtr.setStatus("current")
_TnPcsStatsGBETxCV15MinRtr_Type = Counter32
_TnPcsStatsGBETxCV15MinRtr_Object = MibScalar
tnPcsStatsGBETxCV15MinRtr = _TnPcsStatsGBETxCV15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 69),
    _TnPcsStatsGBETxCV15MinRtr_Type()
)
tnPcsStatsGBETxCV15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsGBETxCV15MinRtr.setStatus("current")
_TnPcsStats16GFCTxCV15MinRtr_Type = Counter32
_TnPcsStats16GFCTxCV15MinRtr_Object = MibScalar
tnPcsStats16GFCTxCV15MinRtr = _TnPcsStats16GFCTxCV15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 70),
    _TnPcsStats16GFCTxCV15MinRtr_Type()
)
tnPcsStats16GFCTxCV15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats16GFCTxCV15MinRtr.setStatus("current")
_TnPcsStats10GFCTxCV15MinRtr_Type = Counter32
_TnPcsStats10GFCTxCV15MinRtr_Object = MibScalar
tnPcsStats10GFCTxCV15MinRtr = _TnPcsStats10GFCTxCV15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 71),
    _TnPcsStats10GFCTxCV15MinRtr_Type()
)
tnPcsStats10GFCTxCV15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats10GFCTxCV15MinRtr.setStatus("current")
_TnPcsStats8GFCTxCV15MinRtr_Type = Counter32
_TnPcsStats8GFCTxCV15MinRtr_Object = MibScalar
tnPcsStats8GFCTxCV15MinRtr = _TnPcsStats8GFCTxCV15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 72),
    _TnPcsStats8GFCTxCV15MinRtr_Type()
)
tnPcsStats8GFCTxCV15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats8GFCTxCV15MinRtr.setStatus("current")
_TnPcsStats4GFCTxCV15MinRtr_Type = Counter32
_TnPcsStats4GFCTxCV15MinRtr_Object = MibScalar
tnPcsStats4GFCTxCV15MinRtr = _TnPcsStats4GFCTxCV15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 73),
    _TnPcsStats4GFCTxCV15MinRtr_Type()
)
tnPcsStats4GFCTxCV15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats4GFCTxCV15MinRtr.setStatus("current")
_TnPcsStats2GFCTxCV15MinRtr_Type = Counter32
_TnPcsStats2GFCTxCV15MinRtr_Object = MibScalar
tnPcsStats2GFCTxCV15MinRtr = _TnPcsStats2GFCTxCV15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 74),
    _TnPcsStats2GFCTxCV15MinRtr_Type()
)
tnPcsStats2GFCTxCV15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStats2GFCTxCV15MinRtr.setStatus("current")
_TnPcsStatsGFCTxCV15MinRtr_Type = Counter32
_TnPcsStatsGFCTxCV15MinRtr_Object = MibScalar
tnPcsStatsGFCTxCV15MinRtr = _TnPcsStatsGFCTxCV15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 75),
    _TnPcsStatsGFCTxCV15MinRtr_Type()
)
tnPcsStatsGFCTxCV15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsGFCTxCV15MinRtr.setStatus("current")
_TnPcsStatsTxES15MinRtr_Type = Counter32
_TnPcsStatsTxES15MinRtr_Object = MibScalar
tnPcsStatsTxES15MinRtr = _TnPcsStatsTxES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 76),
    _TnPcsStatsTxES15MinRtr_Type()
)
tnPcsStatsTxES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsTxES15MinRtr.setStatus("current")
_TnPcsStatsTxSES15MinRtr_Type = Counter32
_TnPcsStatsTxSES15MinRtr_Object = MibScalar
tnPcsStatsTxSES15MinRtr = _TnPcsStatsTxSES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 77),
    _TnPcsStatsTxSES15MinRtr_Type()
)
tnPcsStatsTxSES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsTxSES15MinRtr.setStatus("current")
_TnPcsStatsTxSEFS15MinRtr_Type = Counter32
_TnPcsStatsTxSEFS15MinRtr_Object = MibScalar
tnPcsStatsTxSEFS15MinRtr = _TnPcsStatsTxSEFS15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 11, 78),
    _TnPcsStatsTxSEFS15MinRtr_Type()
)
tnPcsStatsTxSEFS15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsStatsTxSEFS15MinRtr.setStatus("current")
_TnStatisticsOthOduTcmScalars_ObjectIdentity = ObjectIdentity
tnStatisticsOthOduTcmScalars = _TnStatisticsOthOduTcmScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12)
)
_TnOthOdu0StatsTcmNeRxBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu0StatsTcmNeRxBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu0StatsTcmNeRxBIP8ErrCnt15MinTr = _TnOthOdu0StatsTcmNeRxBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 1),
    _TnOthOdu0StatsTcmNeRxBIP8ErrCnt15MinTr_Type()
)
tnOthOdu0StatsTcmNeRxBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu0StatsTcmNeRxBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu0StatsTcmNeRxBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu0StatsTcmNeRxBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu0StatsTcmNeRxBIP8ErrCnt15MinRtr = _TnOthOdu0StatsTcmNeRxBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 2),
    _TnOthOdu0StatsTcmNeRxBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu0StatsTcmNeRxBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu0StatsTcmNeRxBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu0StatsTcmNeRxBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu0StatsTcmNeRxBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu0StatsTcmNeRxBIP8ErrCnt1DayTr = _TnOthOdu0StatsTcmNeRxBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 3),
    _TnOthOdu0StatsTcmNeRxBIP8ErrCnt1DayTr_Type()
)
tnOthOdu0StatsTcmNeRxBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu0StatsTcmNeRxBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu0StatsTcmFeRxBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu0StatsTcmFeRxBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu0StatsTcmFeRxBIP8ErrCnt15MinTr = _TnOthOdu0StatsTcmFeRxBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 4),
    _TnOthOdu0StatsTcmFeRxBIP8ErrCnt15MinTr_Type()
)
tnOthOdu0StatsTcmFeRxBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu0StatsTcmFeRxBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu0StatsTcmFeRxBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu0StatsTcmFeRxBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu0StatsTcmFeRxBIP8ErrCnt15MinRtr = _TnOthOdu0StatsTcmFeRxBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 5),
    _TnOthOdu0StatsTcmFeRxBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu0StatsTcmFeRxBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu0StatsTcmFeRxBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu0StatsTcmFeRxBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu0StatsTcmFeRxBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu0StatsTcmFeRxBIP8ErrCnt1DayTr = _TnOthOdu0StatsTcmFeRxBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 6),
    _TnOthOdu0StatsTcmFeRxBIP8ErrCnt1DayTr_Type()
)
tnOthOdu0StatsTcmFeRxBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu0StatsTcmFeRxBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu1StatsTcmNeRxBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu1StatsTcmNeRxBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu1StatsTcmNeRxBIP8ErrCnt15MinTr = _TnOthOdu1StatsTcmNeRxBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 7),
    _TnOthOdu1StatsTcmNeRxBIP8ErrCnt15MinTr_Type()
)
tnOthOdu1StatsTcmNeRxBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu1StatsTcmNeRxBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu1StatsTcmNeRxBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu1StatsTcmNeRxBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu1StatsTcmNeRxBIP8ErrCnt15MinRtr = _TnOthOdu1StatsTcmNeRxBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 8),
    _TnOthOdu1StatsTcmNeRxBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu1StatsTcmNeRxBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu1StatsTcmNeRxBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu1StatsTcmNeRxBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu1StatsTcmNeRxBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu1StatsTcmNeRxBIP8ErrCnt1DayTr = _TnOthOdu1StatsTcmNeRxBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 9),
    _TnOthOdu1StatsTcmNeRxBIP8ErrCnt1DayTr_Type()
)
tnOthOdu1StatsTcmNeRxBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu1StatsTcmNeRxBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu1StatsTcmFeRxBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu1StatsTcmFeRxBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu1StatsTcmFeRxBIP8ErrCnt15MinTr = _TnOthOdu1StatsTcmFeRxBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 10),
    _TnOthOdu1StatsTcmFeRxBIP8ErrCnt15MinTr_Type()
)
tnOthOdu1StatsTcmFeRxBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu1StatsTcmFeRxBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu1StatsTcmFeRxBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu1StatsTcmFeRxBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu1StatsTcmFeRxBIP8ErrCnt15MinRtr = _TnOthOdu1StatsTcmFeRxBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 11),
    _TnOthOdu1StatsTcmFeRxBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu1StatsTcmFeRxBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu1StatsTcmFeRxBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu1StatsTcmFeRxBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu1StatsTcmFeRxBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu1StatsTcmFeRxBIP8ErrCnt1DayTr = _TnOthOdu1StatsTcmFeRxBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 12),
    _TnOthOdu1StatsTcmFeRxBIP8ErrCnt1DayTr_Type()
)
tnOthOdu1StatsTcmFeRxBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu1StatsTcmFeRxBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu2StatsTcmNeRxBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu2StatsTcmNeRxBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu2StatsTcmNeRxBIP8ErrCnt15MinTr = _TnOthOdu2StatsTcmNeRxBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 13),
    _TnOthOdu2StatsTcmNeRxBIP8ErrCnt15MinTr_Type()
)
tnOthOdu2StatsTcmNeRxBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu2StatsTcmNeRxBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu2StatsTcmNeRxBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu2StatsTcmNeRxBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu2StatsTcmNeRxBIP8ErrCnt15MinRtr = _TnOthOdu2StatsTcmNeRxBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 14),
    _TnOthOdu2StatsTcmNeRxBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu2StatsTcmNeRxBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu2StatsTcmNeRxBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu2StatsTcmNeRxBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu2StatsTcmNeRxBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu2StatsTcmNeRxBIP8ErrCnt1DayTr = _TnOthOdu2StatsTcmNeRxBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 15),
    _TnOthOdu2StatsTcmNeRxBIP8ErrCnt1DayTr_Type()
)
tnOthOdu2StatsTcmNeRxBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu2StatsTcmNeRxBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu2StatsTcmFeRxBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu2StatsTcmFeRxBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu2StatsTcmFeRxBIP8ErrCnt15MinTr = _TnOthOdu2StatsTcmFeRxBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 16),
    _TnOthOdu2StatsTcmFeRxBIP8ErrCnt15MinTr_Type()
)
tnOthOdu2StatsTcmFeRxBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu2StatsTcmFeRxBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu2StatsTcmFeRxBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu2StatsTcmFeRxBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu2StatsTcmFeRxBIP8ErrCnt15MinRtr = _TnOthOdu2StatsTcmFeRxBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 17),
    _TnOthOdu2StatsTcmFeRxBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu2StatsTcmFeRxBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu2StatsTcmFeRxBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu2StatsTcmFeRxBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu2StatsTcmFeRxBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu2StatsTcmFeRxBIP8ErrCnt1DayTr = _TnOthOdu2StatsTcmFeRxBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 18),
    _TnOthOdu2StatsTcmFeRxBIP8ErrCnt1DayTr_Type()
)
tnOthOdu2StatsTcmFeRxBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu2StatsTcmFeRxBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu3StatsTcmNeRxBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu3StatsTcmNeRxBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu3StatsTcmNeRxBIP8ErrCnt15MinTr = _TnOthOdu3StatsTcmNeRxBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 19),
    _TnOthOdu3StatsTcmNeRxBIP8ErrCnt15MinTr_Type()
)
tnOthOdu3StatsTcmNeRxBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu3StatsTcmNeRxBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu3StatsTcmNeRxBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu3StatsTcmNeRxBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu3StatsTcmNeRxBIP8ErrCnt15MinRtr = _TnOthOdu3StatsTcmNeRxBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 20),
    _TnOthOdu3StatsTcmNeRxBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu3StatsTcmNeRxBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu3StatsTcmNeRxBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu3StatsTcmNeRxBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu3StatsTcmNeRxBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu3StatsTcmNeRxBIP8ErrCnt1DayTr = _TnOthOdu3StatsTcmNeRxBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 21),
    _TnOthOdu3StatsTcmNeRxBIP8ErrCnt1DayTr_Type()
)
tnOthOdu3StatsTcmNeRxBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu3StatsTcmNeRxBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu3StatsTcmFeRxBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu3StatsTcmFeRxBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu3StatsTcmFeRxBIP8ErrCnt15MinTr = _TnOthOdu3StatsTcmFeRxBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 22),
    _TnOthOdu3StatsTcmFeRxBIP8ErrCnt15MinTr_Type()
)
tnOthOdu3StatsTcmFeRxBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu3StatsTcmFeRxBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu3StatsTcmFeRxBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu3StatsTcmFeRxBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu3StatsTcmFeRxBIP8ErrCnt15MinRtr = _TnOthOdu3StatsTcmFeRxBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 23),
    _TnOthOdu3StatsTcmFeRxBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu3StatsTcmFeRxBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu3StatsTcmFeRxBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu3StatsTcmFeRxBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu3StatsTcmFeRxBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu3StatsTcmFeRxBIP8ErrCnt1DayTr = _TnOthOdu3StatsTcmFeRxBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 24),
    _TnOthOdu3StatsTcmFeRxBIP8ErrCnt1DayTr_Type()
)
tnOthOdu3StatsTcmFeRxBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu3StatsTcmFeRxBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu4StatsTcmNeRxBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu4StatsTcmNeRxBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu4StatsTcmNeRxBIP8ErrCnt15MinTr = _TnOthOdu4StatsTcmNeRxBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 25),
    _TnOthOdu4StatsTcmNeRxBIP8ErrCnt15MinTr_Type()
)
tnOthOdu4StatsTcmNeRxBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu4StatsTcmNeRxBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu4StatsTcmNeRxBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu4StatsTcmNeRxBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu4StatsTcmNeRxBIP8ErrCnt15MinRtr = _TnOthOdu4StatsTcmNeRxBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 26),
    _TnOthOdu4StatsTcmNeRxBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu4StatsTcmNeRxBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu4StatsTcmNeRxBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu4StatsTcmNeRxBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu4StatsTcmNeRxBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu4StatsTcmNeRxBIP8ErrCnt1DayTr = _TnOthOdu4StatsTcmNeRxBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 27),
    _TnOthOdu4StatsTcmNeRxBIP8ErrCnt1DayTr_Type()
)
tnOthOdu4StatsTcmNeRxBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu4StatsTcmNeRxBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdu4StatsTcmFeRxBIP8ErrCnt15MinTr_Type = Counter64
_TnOthOdu4StatsTcmFeRxBIP8ErrCnt15MinTr_Object = MibScalar
tnOthOdu4StatsTcmFeRxBIP8ErrCnt15MinTr = _TnOthOdu4StatsTcmFeRxBIP8ErrCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 28),
    _TnOthOdu4StatsTcmFeRxBIP8ErrCnt15MinTr_Type()
)
tnOthOdu4StatsTcmFeRxBIP8ErrCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu4StatsTcmFeRxBIP8ErrCnt15MinTr.setStatus("current")
_TnOthOdu4StatsTcmFeRxBIP8ErrCnt15MinRtr_Type = Counter64
_TnOthOdu4StatsTcmFeRxBIP8ErrCnt15MinRtr_Object = MibScalar
tnOthOdu4StatsTcmFeRxBIP8ErrCnt15MinRtr = _TnOthOdu4StatsTcmFeRxBIP8ErrCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 29),
    _TnOthOdu4StatsTcmFeRxBIP8ErrCnt15MinRtr_Type()
)
tnOthOdu4StatsTcmFeRxBIP8ErrCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu4StatsTcmFeRxBIP8ErrCnt15MinRtr.setStatus("current")
_TnOthOdu4StatsTcmFeRxBIP8ErrCnt1DayTr_Type = Counter64
_TnOthOdu4StatsTcmFeRxBIP8ErrCnt1DayTr_Object = MibScalar
tnOthOdu4StatsTcmFeRxBIP8ErrCnt1DayTr = _TnOthOdu4StatsTcmFeRxBIP8ErrCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 30),
    _TnOthOdu4StatsTcmFeRxBIP8ErrCnt1DayTr_Type()
)
tnOthOdu4StatsTcmFeRxBIP8ErrCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdu4StatsTcmFeRxBIP8ErrCnt1DayTr.setStatus("current")
_TnOthOdukStatsTcmNeRxES15MinTr_Type = Counter64
_TnOthOdukStatsTcmNeRxES15MinTr_Object = MibScalar
tnOthOdukStatsTcmNeRxES15MinTr = _TnOthOdukStatsTcmNeRxES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 31),
    _TnOthOdukStatsTcmNeRxES15MinTr_Type()
)
tnOthOdukStatsTcmNeRxES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmNeRxES15MinTr.setStatus("current")
_TnOthOdukStatsTcmNeRxES15MinRtr_Type = Counter64
_TnOthOdukStatsTcmNeRxES15MinRtr_Object = MibScalar
tnOthOdukStatsTcmNeRxES15MinRtr = _TnOthOdukStatsTcmNeRxES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 32),
    _TnOthOdukStatsTcmNeRxES15MinRtr_Type()
)
tnOthOdukStatsTcmNeRxES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmNeRxES15MinRtr.setStatus("current")
_TnOthOdukStatsTcmNeRxES1DayTr_Type = Counter64
_TnOthOdukStatsTcmNeRxES1DayTr_Object = MibScalar
tnOthOdukStatsTcmNeRxES1DayTr = _TnOthOdukStatsTcmNeRxES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 33),
    _TnOthOdukStatsTcmNeRxES1DayTr_Type()
)
tnOthOdukStatsTcmNeRxES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmNeRxES1DayTr.setStatus("current")
_TnOthOdukStatsTcmFeRxES15MinTr_Type = Counter64
_TnOthOdukStatsTcmFeRxES15MinTr_Object = MibScalar
tnOthOdukStatsTcmFeRxES15MinTr = _TnOthOdukStatsTcmFeRxES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 34),
    _TnOthOdukStatsTcmFeRxES15MinTr_Type()
)
tnOthOdukStatsTcmFeRxES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmFeRxES15MinTr.setStatus("current")
_TnOthOdukStatsTcmFeRxES15MinRtr_Type = Counter64
_TnOthOdukStatsTcmFeRxES15MinRtr_Object = MibScalar
tnOthOdukStatsTcmFeRxES15MinRtr = _TnOthOdukStatsTcmFeRxES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 35),
    _TnOthOdukStatsTcmFeRxES15MinRtr_Type()
)
tnOthOdukStatsTcmFeRxES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmFeRxES15MinRtr.setStatus("current")
_TnOthOdukStatsTcmFeRxES1DayTr_Type = Counter64
_TnOthOdukStatsTcmFeRxES1DayTr_Object = MibScalar
tnOthOdukStatsTcmFeRxES1DayTr = _TnOthOdukStatsTcmFeRxES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 36),
    _TnOthOdukStatsTcmFeRxES1DayTr_Type()
)
tnOthOdukStatsTcmFeRxES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmFeRxES1DayTr.setStatus("current")
_TnOthOdukStatsTcmNeRxSES15MinTr_Type = Counter64
_TnOthOdukStatsTcmNeRxSES15MinTr_Object = MibScalar
tnOthOdukStatsTcmNeRxSES15MinTr = _TnOthOdukStatsTcmNeRxSES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 37),
    _TnOthOdukStatsTcmNeRxSES15MinTr_Type()
)
tnOthOdukStatsTcmNeRxSES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmNeRxSES15MinTr.setStatus("current")
_TnOthOdukStatsTcmNeRxSES15MinRtr_Type = Counter64
_TnOthOdukStatsTcmNeRxSES15MinRtr_Object = MibScalar
tnOthOdukStatsTcmNeRxSES15MinRtr = _TnOthOdukStatsTcmNeRxSES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 38),
    _TnOthOdukStatsTcmNeRxSES15MinRtr_Type()
)
tnOthOdukStatsTcmNeRxSES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmNeRxSES15MinRtr.setStatus("current")
_TnOthOdukStatsTcmNeRxSES1DayTr_Type = Counter64
_TnOthOdukStatsTcmNeRxSES1DayTr_Object = MibScalar
tnOthOdukStatsTcmNeRxSES1DayTr = _TnOthOdukStatsTcmNeRxSES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 39),
    _TnOthOdukStatsTcmNeRxSES1DayTr_Type()
)
tnOthOdukStatsTcmNeRxSES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmNeRxSES1DayTr.setStatus("current")
_TnOthOdukStatsTcmFeRxSES15MinTr_Type = Counter64
_TnOthOdukStatsTcmFeRxSES15MinTr_Object = MibScalar
tnOthOdukStatsTcmFeRxSES15MinTr = _TnOthOdukStatsTcmFeRxSES15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 40),
    _TnOthOdukStatsTcmFeRxSES15MinTr_Type()
)
tnOthOdukStatsTcmFeRxSES15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmFeRxSES15MinTr.setStatus("current")
_TnOthOdukStatsTcmFeRxSES15MinRtr_Type = Counter64
_TnOthOdukStatsTcmFeRxSES15MinRtr_Object = MibScalar
tnOthOdukStatsTcmFeRxSES15MinRtr = _TnOthOdukStatsTcmFeRxSES15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 41),
    _TnOthOdukStatsTcmFeRxSES15MinRtr_Type()
)
tnOthOdukStatsTcmFeRxSES15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmFeRxSES15MinRtr.setStatus("current")
_TnOthOdukStatsTcmFeRxSES1DayTr_Type = Counter64
_TnOthOdukStatsTcmFeRxSES1DayTr_Object = MibScalar
tnOthOdukStatsTcmFeRxSES1DayTr = _TnOthOdukStatsTcmFeRxSES1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 42),
    _TnOthOdukStatsTcmFeRxSES1DayTr_Type()
)
tnOthOdukStatsTcmFeRxSES1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmFeRxSES1DayTr.setStatus("current")
_TnOthOdukStatsTcmNeRxUAS15MinTr_Type = Counter64
_TnOthOdukStatsTcmNeRxUAS15MinTr_Object = MibScalar
tnOthOdukStatsTcmNeRxUAS15MinTr = _TnOthOdukStatsTcmNeRxUAS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 43),
    _TnOthOdukStatsTcmNeRxUAS15MinTr_Type()
)
tnOthOdukStatsTcmNeRxUAS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmNeRxUAS15MinTr.setStatus("current")
_TnOthOdukStatsTcmNeRxUAS15MinRtr_Type = Counter64
_TnOthOdukStatsTcmNeRxUAS15MinRtr_Object = MibScalar
tnOthOdukStatsTcmNeRxUAS15MinRtr = _TnOthOdukStatsTcmNeRxUAS15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 44),
    _TnOthOdukStatsTcmNeRxUAS15MinRtr_Type()
)
tnOthOdukStatsTcmNeRxUAS15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmNeRxUAS15MinRtr.setStatus("current")
_TnOthOdukStatsTcmNeRxUAS1DayTr_Type = Counter64
_TnOthOdukStatsTcmNeRxUAS1DayTr_Object = MibScalar
tnOthOdukStatsTcmNeRxUAS1DayTr = _TnOthOdukStatsTcmNeRxUAS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 45),
    _TnOthOdukStatsTcmNeRxUAS1DayTr_Type()
)
tnOthOdukStatsTcmNeRxUAS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmNeRxUAS1DayTr.setStatus("current")
_TnOthOdukStatsTcmFeRxUAS15MinTr_Type = Counter64
_TnOthOdukStatsTcmFeRxUAS15MinTr_Object = MibScalar
tnOthOdukStatsTcmFeRxUAS15MinTr = _TnOthOdukStatsTcmFeRxUAS15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 46),
    _TnOthOdukStatsTcmFeRxUAS15MinTr_Type()
)
tnOthOdukStatsTcmFeRxUAS15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmFeRxUAS15MinTr.setStatus("current")
_TnOthOdukStatsTcmFeRxUAS15MinRtr_Type = Counter64
_TnOthOdukStatsTcmFeRxUAS15MinRtr_Object = MibScalar
tnOthOdukStatsTcmFeRxUAS15MinRtr = _TnOthOdukStatsTcmFeRxUAS15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 47),
    _TnOthOdukStatsTcmFeRxUAS15MinRtr_Type()
)
tnOthOdukStatsTcmFeRxUAS15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmFeRxUAS15MinRtr.setStatus("current")
_TnOthOdukStatsTcmFeRxUAS1DayTr_Type = Counter64
_TnOthOdukStatsTcmFeRxUAS1DayTr_Object = MibScalar
tnOthOdukStatsTcmFeRxUAS1DayTr = _TnOthOdukStatsTcmFeRxUAS1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 12, 48),
    _TnOthOdukStatsTcmFeRxUAS1DayTr_Type()
)
tnOthOdukStatsTcmFeRxUAS1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmFeRxUAS1DayTr.setStatus("current")
_TnStatisticsLanePowerScalars_ObjectIdentity = ObjectIdentity
tnStatisticsLanePowerScalars = _TnStatisticsLanePowerScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 13)
)
_TnOprLaneStatMaxPowerTr_Type = Integer32
_TnOprLaneStatMaxPowerTr_Object = MibScalar
tnOprLaneStatMaxPowerTr = _TnOprLaneStatMaxPowerTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 13, 1),
    _TnOprLaneStatMaxPowerTr_Type()
)
tnOprLaneStatMaxPowerTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOprLaneStatMaxPowerTr.setStatus("current")
if mibBuilder.loadTexts:
    tnOprLaneStatMaxPowerTr.setUnits("mBm")
_TnOprLaneStatMinPowerTr_Type = Integer32
_TnOprLaneStatMinPowerTr_Object = MibScalar
tnOprLaneStatMinPowerTr = _TnOprLaneStatMinPowerTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 13, 2),
    _TnOprLaneStatMinPowerTr_Type()
)
tnOprLaneStatMinPowerTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOprLaneStatMinPowerTr.setStatus("current")
if mibBuilder.loadTexts:
    tnOprLaneStatMinPowerTr.setUnits("mBm")
_TnOptLaneStatMaxPowerTr_Type = Integer32
_TnOptLaneStatMaxPowerTr_Object = MibScalar
tnOptLaneStatMaxPowerTr = _TnOptLaneStatMaxPowerTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 13, 3),
    _TnOptLaneStatMaxPowerTr_Type()
)
tnOptLaneStatMaxPowerTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOptLaneStatMaxPowerTr.setStatus("current")
if mibBuilder.loadTexts:
    tnOptLaneStatMaxPowerTr.setUnits("mBm")
_TnOptLaneStatMinPowerTr_Type = Integer32
_TnOptLaneStatMinPowerTr_Object = MibScalar
tnOptLaneStatMinPowerTr = _TnOptLaneStatMinPowerTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 13, 4),
    _TnOptLaneStatMinPowerTr_Type()
)
tnOptLaneStatMinPowerTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOptLaneStatMinPowerTr.setStatus("current")
if mibBuilder.loadTexts:
    tnOptLaneStatMinPowerTr.setUnits("mBm")
_TnStatisticsEncryptRxFTDScalars_ObjectIdentity = ObjectIdentity
tnStatisticsEncryptRxFTDScalars = _TnStatisticsEncryptRxFTDScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 14)
)
_TnEncryptRxFailToDecryptCnt15MinTr_Type = Counter64
_TnEncryptRxFailToDecryptCnt15MinTr_Object = MibScalar
tnEncryptRxFailToDecryptCnt15MinTr = _TnEncryptRxFailToDecryptCnt15MinTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 14, 1),
    _TnEncryptRxFailToDecryptCnt15MinTr_Type()
)
tnEncryptRxFailToDecryptCnt15MinTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEncryptRxFailToDecryptCnt15MinTr.setStatus("current")
_TnEncryptRxFailToDecryptCnt15MinRtr_Type = Counter64
_TnEncryptRxFailToDecryptCnt15MinRtr_Object = MibScalar
tnEncryptRxFailToDecryptCnt15MinRtr = _TnEncryptRxFailToDecryptCnt15MinRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 14, 2),
    _TnEncryptRxFailToDecryptCnt15MinRtr_Type()
)
tnEncryptRxFailToDecryptCnt15MinRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEncryptRxFailToDecryptCnt15MinRtr.setStatus("current")
_TnEncryptRxFailToDecryptCnt1DayTr_Type = Counter64
_TnEncryptRxFailToDecryptCnt1DayTr_Object = MibScalar
tnEncryptRxFailToDecryptCnt1DayTr = _TnEncryptRxFailToDecryptCnt1DayTr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 14, 3),
    _TnEncryptRxFailToDecryptCnt1DayTr_Type()
)
tnEncryptRxFailToDecryptCnt1DayTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEncryptRxFailToDecryptCnt1DayTr.setStatus("current")
_TnEncryptRxFailToDecryptCnt1DayRtr_Type = Counter64
_TnEncryptRxFailToDecryptCnt1DayRtr_Object = MibScalar
tnEncryptRxFailToDecryptCnt1DayRtr = _TnEncryptRxFailToDecryptCnt1DayRtr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 2, 14, 4),
    _TnEncryptRxFailToDecryptCnt1DayRtr_Type()
)
tnEncryptRxFailToDecryptCnt1DayRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEncryptRxFailToDecryptCnt1DayRtr.setStatus("current")

# Managed Objects groups

tnStatsPortIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 1)
)
tnStatsPortIntervalGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnStatsPortNumberOfIntervals")
)
if mibBuilder.loadTexts:
    tnStatsPortIntervalGroup.setStatus("current")

tnStatsCardIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 2)
)
tnStatsCardIntervalGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnStatsCardNumberOfIntervals")
)
if mibBuilder.loadTexts:
    tnStatsCardIntervalGroup.setStatus("current")

tnStatsPortConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 3)
)
tnStatsPortConfGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnStatsPortIntervalLength"),
        ("TROPIC-STATISTICS-MIB", "tnStatsPortNumberOfBins"),
        ("TROPIC-STATISTICS-MIB", "tnStatsPortProfileId"),
        ("TROPIC-STATISTICS-MIB", "tnStatsPortClear"))
)
if mibBuilder.loadTexts:
    tnStatsPortConfGroup.setStatus("current")

tnStatsCardConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 4)
)
tnStatsCardConfGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnStatsCardIntervalLength"),
        ("TROPIC-STATISTICS-MIB", "tnStatsCardNumberOfBins"),
        ("TROPIC-STATISTICS-MIB", "tnStatsCardProfileId"),
        ("TROPIC-STATISTICS-MIB", "tnStatsCardClear"))
)
if mibBuilder.loadTexts:
    tnStatsCardConfGroup.setStatus("current")

tnStatsTCAProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 5)
)
tnStatsTCAProfileGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnStatsTCAProfileDescr")
)
if mibBuilder.loadTexts:
    tnStatsTCAProfileGroup.setStatus("current")

tnStatsTCAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 6)
)
tnStatsTCAGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnStatsTCAVariable"),
        ("TROPIC-STATISTICS-MIB", "tnStatsTCAValue"))
)
if mibBuilder.loadTexts:
    tnStatsTCAGroup.setStatus("current")

tnCardStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 7)
)
tnCardStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnCardStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnCardStatsScalarsGroup.setStatus("current")

tnCardStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 8)
)
tnCardStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnCardStatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnCardStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnCardStatCpuAverage"),
        ("TROPIC-STATISTICS-MIB", "tnCardStatHeapUsage"),
        ("TROPIC-STATISTICS-MIB", "tnCardStatPoolUsage"))
)
if mibBuilder.loadTexts:
    tnCardStatsGroup.setStatus("current")

tnInterfaceStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 9)
)
tnInterfaceStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnInterfaceStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnInterfaceStatsScalarsGroup.setStatus("current")

tnInterfaceStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 10)
)
tnInterfaceStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnIfStatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnIfStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnIfStatInOctets"),
        ("TROPIC-STATISTICS-MIB", "tnIfStatInUcastPkts"),
        ("TROPIC-STATISTICS-MIB", "tnIfStatInDiscards"),
        ("TROPIC-STATISTICS-MIB", "tnIfStatInErrors"),
        ("TROPIC-STATISTICS-MIB", "tnIfStatInUnknownProtos"),
        ("TROPIC-STATISTICS-MIB", "tnIfStatOutOctets"),
        ("TROPIC-STATISTICS-MIB", "tnIfStatOutUcastPkts"),
        ("TROPIC-STATISTICS-MIB", "tnIfStatOutDiscards"),
        ("TROPIC-STATISTICS-MIB", "tnIfStatOutErrors"),
        ("TROPIC-STATISTICS-MIB", "tnIfStatInMulticastPkts"),
        ("TROPIC-STATISTICS-MIB", "tnIfStatInBroadcastPkts"),
        ("TROPIC-STATISTICS-MIB", "tnIfStatOutMulticastPkts"),
        ("TROPIC-STATISTICS-MIB", "tnIfStatOutBroadcastPkts"),
        ("TROPIC-STATISTICS-MIB", "tnIfStatInPacketsNotClassified"))
)
if mibBuilder.loadTexts:
    tnInterfaceStatsGroup.setStatus("current")

tnEtherStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 11)
)
tnEtherStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnEtherStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnEtherStatsScalarsGroup.setStatus("current")

tnEtherStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 12)
)
tnEtherStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnEtherStatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxDropEvents"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxFragments"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxJabbers"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxMcastPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxOctets"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxOversizedPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxPktsSize1024to1518"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxPktsSize128to255"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxPktsSize256to511"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxPktsSize512to1023"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxPktsSize65to127"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxUndersizedPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxBcastPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxCrcAlignErrs"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxDropEvents"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxFragments"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxJabbers"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxMcastPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxOctets"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxOversizedPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxPktsSize1024to1518"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxPktsSize128to255"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxPktsSize256to511"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxPktsSize512to1023"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxPktsSize65to127"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxUndersizedPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxBcastPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxCrcAlignErrs"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxCollisions"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxJumboPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxCollisions"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxJumboPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxPktsSize64"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxPktsSize64"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxPktErrRatio"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxPktErrRatio"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxPktErrRatio15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxPktErrRatio15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxPktErrRatio1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxPktErrRatio1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatRxPktErrRatio15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatTxPktErrRatio15MinRtr"))
)
if mibBuilder.loadTexts:
    tnEtherStatsGroup.setStatus("current")

tnSonetStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 13)
)
tnSonetStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnSonetStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnSonetStatsScalarsGroup.setStatus("current")

tnSonetStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 14)
)
tnSonetStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnSonetStatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatRxCVS"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatRxESS"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatRxSESS"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatRxSEFSS"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatRxCVL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatRxESL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatRxSESL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatRxUASL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatRxFCL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatTxCVS"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatTxESS"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatTxSESS"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatTxSEFSS"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatTxCVL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatTxESL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatTxSESL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatTxUASL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatTxFCL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatRxUASS"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatTxUASS"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatRxFECVL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatRxFEESL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatRxFESESL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatRxFEUASL"))
)
if mibBuilder.loadTexts:
    tnSonetStatsGroup.setStatus("current")

tnControlNetworkLinkRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 19)
)
tnControlNetworkLinkRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnControlNetworkLinkRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnControlNetworkLinkRawCountStatsScalarsGroup.setStatus("current")

tnControlNetworkLinkRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 20)
)
tnControlNetworkLinkRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnCNLinkRawCountStatIpInReceives"),
        ("TROPIC-STATISTICS-MIB", "tnCNLinkRawCountStatIpInDiscards"),
        ("TROPIC-STATISTICS-MIB", "tnCNLinkRawCountStatIpOutRequests"),
        ("TROPIC-STATISTICS-MIB", "tnCNLinkRawCountStatIpOutDiscards"),
        ("TROPIC-STATISTICS-MIB", "tnCNLinkRawCountStatIpForwDatagrams"))
)
if mibBuilder.loadTexts:
    tnControlNetworkLinkRawCountStatsGroup.setStatus("current")

tnCardRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 21)
)
tnCardRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnCardRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnCardRawCountStatsScalarsGroup.setStatus("current")

tnCardRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 22)
)
tnCardRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnCardRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnCardRawCountStatCpuAverage"),
        ("TROPIC-STATISTICS-MIB", "tnCardRawCountStatHeapUsage"),
        ("TROPIC-STATISTICS-MIB", "tnCardRawCountStatPoolUsage"),
        ("TROPIC-STATISTICS-MIB", "tnCardRawCountStatStartTime"))
)
if mibBuilder.loadTexts:
    tnCardRawCountStatsGroup.setStatus("current")

tnInterfaceRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 23)
)
tnInterfaceRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnInterfaceRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnInterfaceRawCountStatsScalarsGroup.setStatus("current")

tnInterfaceRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 24)
)
tnInterfaceRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnIfRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnIfRawCountStatInOctets"),
        ("TROPIC-STATISTICS-MIB", "tnIfRawCountStatInUcastPkts"),
        ("TROPIC-STATISTICS-MIB", "tnIfRawCountStatInDiscards"),
        ("TROPIC-STATISTICS-MIB", "tnIfRawCountStatInErrors"),
        ("TROPIC-STATISTICS-MIB", "tnIfRawCountStatInUnknownProtos"),
        ("TROPIC-STATISTICS-MIB", "tnIfRawCountStatOutOctets"),
        ("TROPIC-STATISTICS-MIB", "tnIfRawCountStatOutUcastPkts"),
        ("TROPIC-STATISTICS-MIB", "tnIfRawCountStatOutDiscards"),
        ("TROPIC-STATISTICS-MIB", "tnIfRawCountStatOutErrors"),
        ("TROPIC-STATISTICS-MIB", "tnIfRawCountStatInMulticastPkts"),
        ("TROPIC-STATISTICS-MIB", "tnIfRawCountStatInBroadcastPkts"),
        ("TROPIC-STATISTICS-MIB", "tnIfRawCountStatOutMulticastPkts"),
        ("TROPIC-STATISTICS-MIB", "tnIfRawCountStatOutBroadcastPkts"),
        ("TROPIC-STATISTICS-MIB", "tnIfRawCountStatInPacketsNotClassified"),
        ("TROPIC-STATISTICS-MIB", "tnIfRawCountStatStartTime"))
)
if mibBuilder.loadTexts:
    tnInterfaceRawCountStatsGroup.setStatus("current")

tnEtherRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 25)
)
tnEtherRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnEtherRawCountStatsScalarsGroup.setStatus("current")

tnEtherRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 26)
)
tnEtherRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatRxDropEvents"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatRxFragments"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatRxJabbers"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatRxMcastPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatRxOctets"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatRxOversizedPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatRxPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatRxPktsSize1024to1518"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatRxPktsSize128to255"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatRxPktsSize256to511"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatRxPktsSize512to1023"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatRxPktsSize65to127"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatRxUndersizedPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatTxBcastPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatTxCrcAlignErrs"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatTxDropEvents"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatTxFragments"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatTxJabbers"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatTxMcastPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatTxOctets"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatTxOversizedPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatTxPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatTxPktsSize1024to1518"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatTxPktsSize128to255"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatTxPktsSize256to511"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatTxPktsSize512to1023"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatTxPktsSize65to127"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatTxUndersizedPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatRxBcastPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatRxCrcAlignErrs"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatRxCollisions"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatRxJumboPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatTxCollisions"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatTxJumboPkts"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatRmonIndex"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatRxPktsSize64"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatTxPktsSize64"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatRxPktErrRatio"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatTxPktErrRatio"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatStartTime"))
)
if mibBuilder.loadTexts:
    tnEtherRawCountStatsGroup.setStatus("current")

tnSonetRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 27)
)
tnSonetRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnSonetRawCountStatsScalarsGroup.setStatus("current")

tnSonetRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 28)
)
tnSonetRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatRxCVS"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatRxESS"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatRxSESS"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatRxSEFSS"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatRxCVL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatRxESL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatRxSESL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatRxUASL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatRxFCL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatTxCVS"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatTxESS"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatTxSESS"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatTxSEFSS"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatTxCVL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatTxESL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatTxSESL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatTxUASL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatTxFCL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatRxUASS"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatTxUASS"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatRxFECVL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatRxFEESL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatRxFESESL"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatRxFEUASL"))
)
if mibBuilder.loadTexts:
    tnSonetRawCountStatsGroup.setStatus("current")

tnOptStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 33)
)
tnOptStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOptStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnOptStatsScalarsGroup.setStatus("current")

tnOptStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 34)
)
tnOptStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOptStatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnOptStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnOptStatMinPower"),
        ("TROPIC-STATISTICS-MIB", "tnOptStatMaxPower"),
        ("TROPIC-STATISTICS-MIB", "tnOptStatAveragePower"),
        ("TROPIC-STATISTICS-MIB", "tnOptStatMinPowerTr"),
        ("TROPIC-STATISTICS-MIB", "tnOptStatMaxPowerTr"),
        ("TROPIC-STATISTICS-MIB", "tnOptStatMinPowerRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOptStatMaxPowerRtr"))
)
if mibBuilder.loadTexts:
    tnOptStatsGroup.setStatus("current")

tnOprStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 35)
)
tnOprStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOprStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnOprStatsScalarsGroup.setStatus("current")

tnOprStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 36)
)
tnOprStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOprStatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnOprStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnOprStatMinPower"),
        ("TROPIC-STATISTICS-MIB", "tnOprStatMaxPower"),
        ("TROPIC-STATISTICS-MIB", "tnOprStatAveragePower"),
        ("TROPIC-STATISTICS-MIB", "tnOprStatMinPowerTr"),
        ("TROPIC-STATISTICS-MIB", "tnOprStatMaxPowerTr"),
        ("TROPIC-STATISTICS-MIB", "tnOprStatMinPowerRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOprStatMaxPowerRtr"))
)
if mibBuilder.loadTexts:
    tnOprStatsGroup.setStatus("current")

tnOptRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 37)
)
tnOptRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOptRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnOptRawCountStatsScalarsGroup.setStatus("current")

tnOptRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 38)
)
tnOptRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOptRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnOptRawCountStatMinPower"),
        ("TROPIC-STATISTICS-MIB", "tnOptRawCountStatMaxPower"),
        ("TROPIC-STATISTICS-MIB", "tnOptRawCountStatAveragePower"),
        ("TROPIC-STATISTICS-MIB", "tnOptRawCountStatStartTime"))
)
if mibBuilder.loadTexts:
    tnOptRawCountStatsGroup.setStatus("current")

tnOprRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 39)
)
tnOprRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOprRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnOprRawCountStatsScalarsGroup.setStatus("current")

tnOprRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 40)
)
tnOprRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOprRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnOprRawCountStatMinPower"),
        ("TROPIC-STATISTICS-MIB", "tnOprRawCountStatMaxPower"),
        ("TROPIC-STATISTICS-MIB", "tnOprRawCountStatAveragePower"),
        ("TROPIC-STATISTICS-MIB", "tnOprRawCountStatStartTime"))
)
if mibBuilder.loadTexts:
    tnOprRawCountStatsGroup.setStatus("current")

tnOpOutStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 41)
)
tnOpOutStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOpOutStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnOpOutStatsScalarsGroup.setStatus("current")

tnOpOutStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 42)
)
tnOpOutStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOpOutStatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnOpOutStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnOpOutStatMinPower"),
        ("TROPIC-STATISTICS-MIB", "tnOpOutStatMaxPower"),
        ("TROPIC-STATISTICS-MIB", "tnOpOutStatAveragePower"))
)
if mibBuilder.loadTexts:
    tnOpOutStatsGroup.setStatus("current")

tnOpInStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 43)
)
tnOpInStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOpInStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnOpInStatsScalarsGroup.setStatus("current")

tnOpInStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 44)
)
tnOpInStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOpInStatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnOpInStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnOpInStatMinPower"),
        ("TROPIC-STATISTICS-MIB", "tnOpInStatMaxPower"),
        ("TROPIC-STATISTICS-MIB", "tnOpInStatAveragePower"))
)
if mibBuilder.loadTexts:
    tnOpInStatsGroup.setStatus("current")

tnOpOutRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 45)
)
tnOpOutRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOpOutRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnOpOutRawCountStatsScalarsGroup.setStatus("current")

tnOpOutRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 46)
)
tnOpOutRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOpOutRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnOpOutRawCountStatMinPower"),
        ("TROPIC-STATISTICS-MIB", "tnOpOutRawCountStatMaxPower"),
        ("TROPIC-STATISTICS-MIB", "tnOpOutRawCountStatAveragePower"),
        ("TROPIC-STATISTICS-MIB", "tnOpOutRawCountStatStartTime"))
)
if mibBuilder.loadTexts:
    tnOpOutRawCountStatsGroup.setStatus("current")

tnOpInRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 47)
)
tnOpInRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOpInRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnOpInRawCountStatsScalarsGroup.setStatus("current")

tnOpInRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 48)
)
tnOpInRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOpInRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnOpInRawCountStatMinPower"),
        ("TROPIC-STATISTICS-MIB", "tnOpInRawCountStatMaxPower"),
        ("TROPIC-STATISTICS-MIB", "tnOpInRawCountStatAveragePower"),
        ("TROPIC-STATISTICS-MIB", "tnOpInRawCountStatStartTime"))
)
if mibBuilder.loadTexts:
    tnOpInRawCountStatsGroup.setStatus("current")

tnOpOchOutStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 50)
)
tnOpOchOutStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOpOchOutStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnOpOchOutStatsScalarsGroup.setStatus("current")

tnOpOchOutStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 51)
)
tnOpOchOutStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOpOchOutStatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchOutStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchOutStatMinPower"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchOutStatMaxPower"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchOutStatAveragePower"))
)
if mibBuilder.loadTexts:
    tnOpOchOutStatsGroup.setStatus("current")

tnOpOchInStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 52)
)
tnOpOchInStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOpOchInStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnOpOchInStatsScalarsGroup.setStatus("current")

tnOpOchInStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 53)
)
tnOpOchInStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOpOchInStatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchInStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchInStatMinPower"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchInStatMaxPower"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchInStatAveragePower"))
)
if mibBuilder.loadTexts:
    tnOpOchInStatsGroup.setStatus("current")

tnOpOchOutRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 54)
)
tnOpOchOutRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOpOchOutRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnOpOchOutRawCountStatsScalarsGroup.setStatus("current")

tnOpOchOutRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 55)
)
tnOpOchOutRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOpOchOutRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchOutRawCountStatMinPower"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchOutRawCountStatMaxPower"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchOutRawCountStatAveragePower"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchOutRawCountStatStartTime"))
)
if mibBuilder.loadTexts:
    tnOpOchOutRawCountStatsGroup.setStatus("current")

tnOpOchInRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 56)
)
tnOpOchInRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOpOchInRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnOpOchInRawCountStatsScalarsGroup.setStatus("current")

tnOpOchInRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 57)
)
tnOpOchInRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOpOchInRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchInRawCountStatMinPower"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchInRawCountStatMaxPower"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchInRawCountStatAveragePower"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchInRawCountStatStartTime"))
)
if mibBuilder.loadTexts:
    tnOpOchInRawCountStatsGroup.setStatus("current")

tnStatsPortClearAllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 58)
)
tnStatsPortClearAllGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnStatsPortClearAll")
)
if mibBuilder.loadTexts:
    tnStatsPortClearAllGroup.setStatus("current")

tnStatsTCAScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 59)
)
tnStatsTCAScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnStatsClearAll")
)
if mibBuilder.loadTexts:
    tnStatsTCAScalarsGroup.setStatus("current")

tnSdhStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 60)
)
tnSdhStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnSdhStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnSdhStatsScalarsGroup.setStatus("current")

tnSdhStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 61)
)
tnSdhStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnSdhStatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatRxRSEB"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatRxRSES"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatRxRSSES"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatRxMSEB"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatRxMSES"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatRxMSSES"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatRxMSUAS"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatTxRSEB"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatTxRSES"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatTxRSSES"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatTxMSEB"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatTxMSES"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatTxMSSES"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatTxMSUAS"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatRxRSUAS"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatTxRSUAS"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatRxMSFEEB"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatRxMSFEES"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatRxMSFESES"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatRxMSFEUAS"))
)
if mibBuilder.loadTexts:
    tnSdhStatsGroup.setStatus("current")

tnSdhRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 62)
)
tnSdhRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnSdhRawCountStatsScalarsGroup.setStatus("current")

tnSdhRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 63)
)
tnSdhRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatRxRSEB"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatRxRSES"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatRxRSSES"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatRxMSEB"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatRxMSES"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatRxMSSES"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatRxMSUAS"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatTxRSEB"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatTxRSES"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatTxRSSES"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatTxMSEB"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatTxMSES"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatTxMSSES"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatTxMSUAS"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatRxRSUAS"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatTxRSUAS"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatRxMSFEEB"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatRxMSFEES"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatRxMSFESES"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatRxMSFEUAS"))
)
if mibBuilder.loadTexts:
    tnSdhRawCountStatsGroup.setStatus("current")

tnPhyCodeSublayerStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 72)
)
tnPhyCodeSublayerStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnPhyCodeSublayerStatsScalarsGroup.setStatus("current")

tnPhyCodeSublayerStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 73)
)
tnPhyCodeSublayerStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerStatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerStatRxCV"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerStatRxES"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerStatRxSES"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerStatRxSEFS"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerStatTxCV"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerStatTxES"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerStatTxSES"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerStatTxSEFS"))
)
if mibBuilder.loadTexts:
    tnPhyCodeSublayerStatsGroup.setStatus("current")

tnPhyCodeSublayerRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 74)
)
tnPhyCodeSublayerRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnPhyCodeSublayerRawCountStatsScalarsGroup.setStatus("current")

tnPhyCodeSublayerRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 75)
)
tnPhyCodeSublayerRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerRawCountStatRxCV"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerRawCountStatRxES"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerRawCountStatRxSES"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerRawCountStatRxSEFS"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerRawCountStatTxCV"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerRawCountStatTxES"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerRawCountStatTxSES"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerRawCountStatTxSEFS"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerRawCountStatStartTime"))
)
if mibBuilder.loadTexts:
    tnPhyCodeSublayerRawCountStatsGroup.setStatus("current")

tnDigitalWrapper64BitStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 76)
)
tnDigitalWrapper64BitStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnDigitalWrapper64BitStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnDigitalWrapper64BitStatsScalarsGroup.setStatus("current")

tnDigitalWrapper64BitStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 77)
)
tnDigitalWrapper64BitStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnDw64BitStatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxRSCorrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxRSUncorrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxSMBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxPMBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxSMES"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxPMES"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxSMSES"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxPMSES"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxSMUAS"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxPMUAS"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxBERPreFEC"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxBERPostFEC"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxSMFEBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxPMFEBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxSMBIAESErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxSMIAESErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxSMFEES"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxPMFEES"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxSMFESES"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxPMFESES"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxSMFEUAS"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatRxPMFEUAS"))
)
if mibBuilder.loadTexts:
    tnDigitalWrapper64BitStatsGroup.setStatus("current")

tnDigitalWrapper64BitRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 78)
)
tnDigitalWrapper64BitRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnDigitalWrapper64BitRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnDigitalWrapper64BitRawCountStatsScalarsGroup.setStatus("current")

tnDigitalWrapper64BitRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 79)
)
tnDigitalWrapper64BitRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxRSCorrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxRSUncorrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxSMBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxPMBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxSMBEIErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxPMBEIErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxRSSES"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxSMES"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxPMES"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxSMSES"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxPMSES"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxSMUAS"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxPMUAS"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxBERPreFEC"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxBERPostFEC"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxSMFEBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxPMFEBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxSMBIAESErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxSMIAESErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxSMFEES"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxPMFEES"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxSMFESES"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxPMFESES"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxSMFEUAS"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitRawCountStatRxPMFEUAS"))
)
if mibBuilder.loadTexts:
    tnDigitalWrapper64BitRawCountStatsGroup.setStatus("current")

tnStatsBaselineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 80)
)
tnStatsBaselineGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnStatsBaselineReason"),
        ("TROPIC-STATISTICS-MIB", "tnStatsBaselineValue"),
        ("TROPIC-STATISTICS-MIB", "tnStatsBaselineTime"))
)
if mibBuilder.loadTexts:
    tnStatsBaselineGroup.setStatus("current")

tnCdrStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 81)
)
tnCdrStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnCdrStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnCdrStatsScalarsGroup.setStatus("current")

tnCdrStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 82)
)
tnCdrStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnCdrStatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnCdrStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnCdrStatMin"),
        ("TROPIC-STATISTICS-MIB", "tnCdrStatMax"),
        ("TROPIC-STATISTICS-MIB", "tnCdrStatAverage"))
)
if mibBuilder.loadTexts:
    tnCdrStatsGroup.setStatus("current")

tnCdrRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 83)
)
tnCdrRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnCdrRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnCdrRawCountStatsScalarsGroup.setStatus("current")

tnCdrRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 84)
)
tnCdrRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnCdrRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnCdrRawCountStatMin"),
        ("TROPIC-STATISTICS-MIB", "tnCdrRawCountStatMax"),
        ("TROPIC-STATISTICS-MIB", "tnCdrRawCountStatAverage"),
        ("TROPIC-STATISTICS-MIB", "tnCdrRawCountStatStartTime"))
)
if mibBuilder.loadTexts:
    tnCdrRawCountStatsGroup.setStatus("current")

tnDgdrStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 85)
)
tnDgdrStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnDgdrStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnDgdrStatsScalarsGroup.setStatus("current")

tnDgdrStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 86)
)
tnDgdrStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnDgdrStatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnDgdrStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnDgdrStatMin"),
        ("TROPIC-STATISTICS-MIB", "tnDgdrStatMax"),
        ("TROPIC-STATISTICS-MIB", "tnDgdrStatAverage"))
)
if mibBuilder.loadTexts:
    tnDgdrStatsGroup.setStatus("current")

tnDgdrRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 87)
)
tnDgdrRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnDgdrRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnDgdrRawCountStatsScalarsGroup.setStatus("current")

tnDgdrRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 88)
)
tnDgdrRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnDgdrRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnDgdrRawCountStatMin"),
        ("TROPIC-STATISTICS-MIB", "tnDgdrRawCountStatMax"),
        ("TROPIC-STATISTICS-MIB", "tnDgdrRawCountStatAverage"),
        ("TROPIC-STATISTICS-MIB", "tnDgdrRawCountStatStartTime"))
)
if mibBuilder.loadTexts:
    tnDgdrRawCountStatsGroup.setStatus("current")

tnFoffrStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 89)
)
tnFoffrStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnFoffrStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnFoffrStatsScalarsGroup.setStatus("current")

tnFoffrStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 90)
)
tnFoffrStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnFoffrStatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnFoffrStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnFoffrStatMin"),
        ("TROPIC-STATISTICS-MIB", "tnFoffrStatMax"),
        ("TROPIC-STATISTICS-MIB", "tnFoffrStatAverage"))
)
if mibBuilder.loadTexts:
    tnFoffrStatsGroup.setStatus("current")

tnFoffrRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 91)
)
tnFoffrRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnFoffrRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnFoffrRawCountStatsScalarsGroup.setStatus("current")

tnFoffrRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 92)
)
tnFoffrRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnFoffrRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnFoffrRawCountStatMin"),
        ("TROPIC-STATISTICS-MIB", "tnFoffrRawCountStatMax"),
        ("TROPIC-STATISTICS-MIB", "tnFoffrRawCountStatAverage"),
        ("TROPIC-STATISTICS-MIB", "tnFoffrRawCountStatStartTime"))
)
if mibBuilder.loadTexts:
    tnFoffrRawCountStatsGroup.setStatus("current")

tnE1StatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 93)
)
tnE1StatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnE1StatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnE1StatsScalarsGroup.setStatus("current")

tnE1StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 94)
)
tnE1StatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnE1StatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxBBEP"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxESP"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxSESP"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxUASP"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxESL"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxSESL"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatTxBBEP"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatTxESP"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatTxSESP"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatTxUASP"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxBBEP15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxESP15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxSESP15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxUASP15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxESL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxSESL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatTxBBEP15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatTxESP15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatTxSESP15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatTxUASP15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxBBEP1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxESP1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxSESP1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxUASP1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxESL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxSESL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatTxBBEP1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatTxESP1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatTxSESP1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatTxUASP1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxBBEP15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxESP15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxSESP15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxUASP15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxESL15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatRxSESL15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatTxBBEP15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatTxESP15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatTxSESP15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatTxUASP15MinRtr"))
)
if mibBuilder.loadTexts:
    tnE1StatsGroup.setStatus("current")

tnE1RawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 95)
)
tnE1RawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnE1RawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnE1RawCountStatsScalarsGroup.setStatus("current")

tnE1RawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 96)
)
tnE1RawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnE1RawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnE1RawCountStatRxBBEP"),
        ("TROPIC-STATISTICS-MIB", "tnE1RawCountStatRxESP"),
        ("TROPIC-STATISTICS-MIB", "tnE1RawCountStatRxSESP"),
        ("TROPIC-STATISTICS-MIB", "tnE1RawCountStatRxUASP"),
        ("TROPIC-STATISTICS-MIB", "tnE1RawCountStatRxESL"),
        ("TROPIC-STATISTICS-MIB", "tnE1RawCountStatRxSESL"),
        ("TROPIC-STATISTICS-MIB", "tnE1RawCountStatTxBBEP"),
        ("TROPIC-STATISTICS-MIB", "tnE1RawCountStatTxESP"),
        ("TROPIC-STATISTICS-MIB", "tnE1RawCountStatTxSESP"),
        ("TROPIC-STATISTICS-MIB", "tnE1RawCountStatTxUASP"),
        ("TROPIC-STATISTICS-MIB", "tnE1RawCountStatStartTime"))
)
if mibBuilder.loadTexts:
    tnE1RawCountStatsGroup.setStatus("current")

tnPreFECBitsStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 97)
)
tnPreFECBitsStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnPreFECBitsStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnPreFECBitsStatsScalarsGroup.setStatus("current")

tnPreFECBitsStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 98)
)
tnPreFECBitsStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnPreFECBitsStatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnPreFECBitsStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnPreFECBitsStatMin"),
        ("TROPIC-STATISTICS-MIB", "tnPreFECBitsStatMax"),
        ("TROPIC-STATISTICS-MIB", "tnPreFECBitsStatAverage"))
)
if mibBuilder.loadTexts:
    tnPreFECBitsStatsGroup.setStatus("current")

tnPreFECBitsRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 99)
)
tnPreFECBitsRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnPreFECBitsRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnPreFECBitsRawCountStatsScalarsGroup.setStatus("current")

tnPreFECBitsRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 100)
)
tnPreFECBitsRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnPreFECBitsRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnPreFECBitsRawCountStatMin"),
        ("TROPIC-STATISTICS-MIB", "tnPreFECBitsRawCountStatMax"),
        ("TROPIC-STATISTICS-MIB", "tnPreFECBitsRawCountStatAverage"),
        ("TROPIC-STATISTICS-MIB", "tnPreFECBitsRawCountStatStartTime"))
)
if mibBuilder.loadTexts:
    tnPreFECBitsRawCountStatsGroup.setStatus("current")

tnEncrypt64BitStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 108)
)
tnEncrypt64BitStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnEncrypt64BitStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnEncrypt64BitStatsScalarsGroup.setStatus("current")

tnEncrypt64BitStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 109)
)
tnEncrypt64BitStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnEncrypt64BitStatsBin"),
        ("TROPIC-STATISTICS-MIB", "tnEncrypt64BitStatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnEncrypt64BitStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnEncrypt64BitStatTx128BitBlkCnt"),
        ("TROPIC-STATISTICS-MIB", "tnEncrypt64BitStatRxFailToDecryptCnt"))
)
if mibBuilder.loadTexts:
    tnEncrypt64BitStatsGroup.setStatus("current")

tnEncrypt64BitRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 110)
)
tnEncrypt64BitRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnEncrypt64BitRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnEncrypt64BitRawCountStatsScalarsGroup.setStatus("current")

tnEncrypt64BitRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 111)
)
tnEncrypt64BitRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnEncrypt64BitRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnEncrypt64BitRawCountStatTx128BitBlkCnt"),
        ("TROPIC-STATISTICS-MIB", "tnEncrypt64BitRawCountStatRxFailToDecryptCnt"),
        ("TROPIC-STATISTICS-MIB", "tnEncrypt64BitRawCountStatStartTime"))
)
if mibBuilder.loadTexts:
    tnEncrypt64BitRawCountStatsGroup.setStatus("current")

tnOthOdukStatsRxConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 112)
)
tnOthOdukStatsRxConfigScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnOthOdukStatsRxConfigScalarsGroup.setStatus("current")

tnOthOdukStatsRxConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 113)
)
tnOthOdukStatsRxConfigGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxNumberofBins"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxProfileid"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxClear"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxIntervalLength"))
)
if mibBuilder.loadTexts:
    tnOthOdukStatsRxConfigGroup.setStatus("current")

tnOthOdukStatsTxConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 114)
)
tnOthOdukStatsTxConfigScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTxConfigScalarsGroup.setStatus("current")

tnOthOdukStatsTxConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 115)
)
tnOthOdukStatsTxConfigGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxNumberofBins"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxProfileid"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxClear"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxIntervalLength"))
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTxConfigGroup.setStatus("current")

tnOthOdukStatsControlScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 116)
)
tnOthOdukStatsControlScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsControlAttributeTotal")
)
if mibBuilder.loadTexts:
    tnOthOdukStatsControlScalarsGroup.setStatus("current")

tnOthOdukStatsControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 117)
)
tnOthOdukStatsControlGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOthOdukStatsClearAll"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxEnable"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxEnable"))
)
if mibBuilder.loadTexts:
    tnOthOdukStatsControlGroup.setStatus("current")

tnOthOdukStatsRxScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 118)
)
tnOthOdukStatsRxScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxTotalMembers")
)
if mibBuilder.loadTexts:
    tnOthOdukStatsRxScalarsGroup.setStatus("current")

tnOthOdukStatsRxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 119)
)
tnOthOdukStatsRxGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOthOdukStatsBin"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxNeBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxNeES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxNeSES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxNeUAS"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxFeBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxFeES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxFeSES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxFeUAS"))
)
if mibBuilder.loadTexts:
    tnOthOdukStatsRxGroup.setStatus("current")

tnOthOdukStatsTxScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 120)
)
tnOthOdukStatsTxScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxTotalMembers")
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTxScalarsGroup.setStatus("current")

tnOthOdukStatsTxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 121)
)
tnOthOdukStatsTxGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxNeBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxNeES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxNeSES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxNeUAS"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxFeBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxFeES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxFeSES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxFeUAS"))
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTxGroup.setStatus("current")

tnOthOtukStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 122)
)
tnOthOtukStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxTotalMembers")
)
if mibBuilder.loadTexts:
    tnOthOtukStatsScalarsGroup.setStatus("current")

tnOthOtukStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 123)
)
tnOthOtukStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOthOtukStatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxRsCorrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxRsUncorrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxBERPreFEC"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxBERPostFEC"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatNeRxSMBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatNeRxBIAESErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatNeRxSMES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatNeRxSMSES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatNeRxSMUAS"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatNeRxIAES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatFeRxSMBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatFeRxSMES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatFeRxSMSES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatFeRxSMUAS"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatFeRxIAES"))
)
if mibBuilder.loadTexts:
    tnOthOtukStatsGroup.setStatus("current")

tnOthOdukStatsRxThresholdScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 124)
)
tnOthOdukStatsRxThresholdScalarsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOthOdu0StatRxNeBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu0StatRxNeBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu0StatRxNeBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu0StatRxFeBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu0StatRxFeBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu0StatRxFeBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu1StatRxNeBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu1StatRxNeBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu1StatRxNeBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu1StatRxFeBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu1StatRxFeBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu1StatRxFeBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu2StatRxNeBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu2StatRxNeBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu2StatRxNeBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu2StatRxFeBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu2StatRxFeBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu2StatRxFeBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu3StatRxNeBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu3StatRxNeBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu3StatRxNeBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu3StatRxFeBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu3StatRxFeBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu3StatRxFeBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu4StatRxNeBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu4StatRxNeBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu4StatRxNeBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu4StatRxFeBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu4StatRxFeBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu4StatRxFeBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatRxNeES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatRxNeES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatRxNeES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatRxFeES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatRxFeES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatRxFeES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatRxNeSES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatRxNeSES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatRxNeSES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatRxFeSES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatRxFeSES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatRxFeSES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatRxNeUAS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatRxNeUAS15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatRxNeUAS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatRxFeUAS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatRxFeUAS15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatRxFeUAS1DayTr"))
)
if mibBuilder.loadTexts:
    tnOthOdukStatsRxThresholdScalarsGroup.setStatus("current")

tnOthOdukStatsTxThresholdScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 125)
)
tnOthOdukStatsTxThresholdScalarsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOthOdu0StatTxNeBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu0StatTxNeBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu0StatTxNeBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu0StatTxFeBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu0StatTxFeBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu0StatTxFeBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu1StatTxNeBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu1StatTxNeBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu1StatTxNeBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu1StatTxFeBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu1StatTxFeBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu1StatTxFeBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu2StatTxNeBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu2StatTxNeBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu2StatTxNeBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu2StatTxFeBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu2StatTxFeBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu2StatTxFeBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu3StatTxNeBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu3StatTxNeBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu3StatTxNeBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu3StatTxFeBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu3StatTxFeBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu3StatTxFeBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu4StatTxNeBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu4StatTxNeBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu4StatTxNeBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu4StatTxFeBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu4StatTxFeBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu4StatTxFeBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatTxNeES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatTxNeES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatTxNeES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatTxFeES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatTxFeES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatTxFeES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatTxNeSES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatTxNeSES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatTxNeSES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatTxFeSES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatTxFeSES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatTxFeSES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatTxNeUAS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatTxNeUAS15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatTxNeUAS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatTxFeUAS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatTxFeUAS15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatTxFeUAS1DayTr"))
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTxThresholdScalarsGroup.setStatus("current")

tnOthOtukStatsThresholdScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 126)
)
tnOthOtukStatsThresholdScalarsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOthOtu1StatRxRsCorrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu1StatRxRsCorrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu1StatRxRsCorrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu1StatRxRsUncorrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu1StatRxRsUncorrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu1StatRxRsUncorrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu1StatRxNeSMBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu1StatRxNeSMBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu1StatRxNeSMBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu1StatRxFeSMBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu1StatRxFeSMBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu1StatRxFeSMBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu2StatRxRsCorrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu2StatRxRsCorrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu2StatRxRsCorrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu2StatRxRsUncorrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu2StatRxRsUncorrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu2StatRxRsUncorrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu2StatRxNeSMBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu2StatRxNeSMBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu2StatRxNeSMBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu2StatRxFeSMBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu2StatRxFeSMBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu2StatRxFeSMBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu3StatRxRsCorrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu3StatRxRsCorrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu3StatRxRsCorrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu3StatRxRsUncorrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu3StatRxRsUncorrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu3StatRxRsUncorrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu3StatRxNeSMBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu3StatRxNeSMBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu3StatRxNeSMBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu3StatRxFeSMBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu3StatRxFeSMBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu3StatRxFeSMBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu4StatRxRsCorrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu4StatRxRsCorrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu4StatRxRsCorrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu4StatRxRsUncorrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu4StatRxRsUncorrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu4StatRxRsUncorrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu4StatRxNeSMBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu4StatRxNeSMBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu4StatRxNeSMBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu4StatRxFeSMBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu4StatRxFeSMBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtu4StatRxFeSMBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxBERPreFEC15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxBERPreFEC15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxBERPreFEC1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxBERPostFEC15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxBERPostFEC15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxBERPostFEC1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxNeSMES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxNeSMES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxNeSMES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxFeSMES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxFeSMES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxFeSMES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxNeSMSES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxNeSMSES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxNeSMSES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxFeSMSES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxFeSMSES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxFeSMSES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxNeSMUAS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxNeSMUAS15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxNeSMUAS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxFeSMUAS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxFeSMUAS15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxFeSMUAS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxNeIAES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxNeIAES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxNeIAES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxFeIAES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxFeIAES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatRxFeIAES1DayTr"))
)
if mibBuilder.loadTexts:
    tnOthOtukStatsThresholdScalarsGroup.setStatus("current")

tnOthOdukRawCountStatsRxScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 127)
)
tnOthOdukRawCountStatsRxScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatsRxTotalMembers")
)
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsRxScalarsGroup.setStatus("current")

tnOthOdukRawCountStatsRxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 128)
)
tnOthOdukRawCountStatsRxGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatsRxClear"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatsRxStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatRxNeBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatRxNeES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatRxNeSES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatRxNeUAS"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatRxFeBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatRxFeES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatRxFeSES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatRxFeUAS"))
)
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsRxGroup.setStatus("current")

tnOthOdukRawCountStatsTxScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 129)
)
tnOthOdukRawCountStatsTxScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatsTxTotalMembers")
)
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsTxScalarsGroup.setStatus("current")

tnOthOdukRawCountStatsTxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 130)
)
tnOthOdukRawCountStatsTxGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatsTxClear"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatsTxStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatTxNeBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatTxNeES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatTxNeSES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatTxNeUAS"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatTxFeBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatTxFeES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatTxFeSES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatTxFeUAS"))
)
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsTxGroup.setStatus("current")

tnOthOtukRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 131)
)
tnOthOtukRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOthOtukRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatsScalarsGroup.setStatus("current")

tnOthOtukRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 132)
)
tnOthOtukRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOthOtukRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukRawCountStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukRawCountStatRxRsCorrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukRawCountStatRxRsUncorrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukRawCountStatRxBERPreFEC"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukRawCountStatRxBERPostFEC"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukRawCountStatRxNeSMBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukRawCountStatRxNeSMES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukRawCountStatRxNeSMSES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukRawCountStatRxNeSMUAS"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukRawCountStatRxNeIAES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukRawCountStatRxFeSMBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukRawCountStatRxFeSMES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukRawCountStatRxFeSMSES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukRawCountStatRxFeSMUAS"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukRawCountStatRxFeIAES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukRawCountStatRxNeBIAES"))
)
if mibBuilder.loadTexts:
    tnOthOtukRawCountStatsGroup.setStatus("current")

tnOsnrStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 133)
)
tnOsnrStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOsnrStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnOsnrStatsScalarsGroup.setStatus("current")

tnOsnrStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 134)
)
tnOsnrStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOsnrStatsBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnOsnrStatsStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnOsnrStatMinOSNR"),
        ("TROPIC-STATISTICS-MIB", "tnOsnrStatMaxOSNR"),
        ("TROPIC-STATISTICS-MIB", "tnOsnrStatAverageOSNR"),
        ("TROPIC-STATISTICS-MIB", "tnOsnrStatStatusOSNR"))
)
if mibBuilder.loadTexts:
    tnOsnrStatsGroup.setStatus("current")

tnOsnrRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 135)
)
tnOsnrRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOsnrRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnOsnrRawCountStatsScalarsGroup.setStatus("current")

tnOsnrRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 136)
)
tnOsnrRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOsnrRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnOsnrRawCountStatStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnOsnrRawCountStatMinOSNR"),
        ("TROPIC-STATISTICS-MIB", "tnOsnrRawCountStatMaxOSNR"),
        ("TROPIC-STATISTICS-MIB", "tnOsnrRawCountStatAverageOSNR"))
)
if mibBuilder.loadTexts:
    tnOsnrRawCountStatsGroup.setStatus("current")

tnSonetStatsThresholdScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 137)
)
tnSonetStatsThresholdScalarsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnSonetStatsOC768RxCVS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC192RxCVS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC48RxCVS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC12RxCVS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC3RxCVS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsRxESS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsRxSESS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsRxSEFSS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC768RxCVL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC192RxCVL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC48RxCVL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC12RxCVL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC3RxCVL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsRxESL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsRxSESL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsRxUASL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC768TxCVS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC192TxCVS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC48TxCVS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC12TxCVS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC3TxCVS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsTxESS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsTxSESS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsTxSEFSS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC768TxCVL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC192TxCVL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC48TxCVL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC12TxCVL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC3TxCVL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsTxESL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsTxSESL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsTxUASL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsRxUASS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsTxUASS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC768RxCVS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC192RxCVS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC48RxCVS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC12RxCVS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC3RxCVS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsRxESS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsRxSESS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsRxSEFSS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC768RxCVL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC192RxCVL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC48RxCVL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC12RxCVL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC3RxCVL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsRxESL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsRxSESL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsRxUASL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC768TxCVS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC192TxCVS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC48TxCVS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC12TxCVS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC3TxCVS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsTxESS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsTxSESS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsTxSEFSS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC768TxCVL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC192TxCVL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC48TxCVL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC12TxCVL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC3TxCVL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsTxESL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsTxSESL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsTxUASL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsRxUASS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsTxUASS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC768RxFECVL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC192RxFECVL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC48RxFECVL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC12RxFECVL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC3RxFECVL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsRxFEESL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsRxFESESL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsRxFEUASL15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC768RxFECVL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC192RxFECVL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC48RxFECVL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC12RxFECVL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsOC3RxFECVL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsRxFEESL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsRxFESESL1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsRxFEUASL1DayTr"))
)
if mibBuilder.loadTexts:
    tnSonetStatsThresholdScalarsGroup.setStatus("current")

tnSdhStatsThresholdScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 138)
)
tnSdhStatsThresholdScalarsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM256RxRSEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM64RxRSEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM16RxRSEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM4RxRSEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM1RxRSEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxRSES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxRSSES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM256RxMSEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM64RxMSEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM16RxMSEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM4RxMSEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM1RxMSEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxMSES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxMSSES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxMSUAS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM256TxRSEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM64TxRSEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM16TxRSEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM4TxRSEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM1TxRSEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsTxRSES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsTxRSSES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM256TxMSEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM64TxMSEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM16TxMSEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM4TxMSEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM1TxMSEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsTxMSES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsTxMSSES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsTxMSUAS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxRSUAS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsTxRSUAS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM256RxRSEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM64RxRSEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM16RxRSEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM4RxRSEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM1RxRSEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxRSES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxRSSES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM256RxMSEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM64RxMSEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM16RxMSEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM4RxMSEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM1RxMSEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxMSES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxMSSES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxMSUAS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM256TxRSEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM64TxRSEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM16TxRSEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM4TxRSEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM1TxRSEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsTxRSES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsTxRSSES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM256TxMSEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM64TxMSEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM16TxMSEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM4TxMSEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM1TxMSEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsTxMSES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsTxMSSES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsTxMSUAS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxRSUAS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsTxRSUAS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM256RxRSEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM64RxRSEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM16RxRSEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM4RxRSEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM1RxRSEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxRSES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxRSSES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM256RxMSEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM64RxMSEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM16RxMSEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM4RxMSEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM1RxMSEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxMSES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxMSSES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxMSUAS15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM256TxRSEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM64TxRSEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM16TxRSEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM4TxRSEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM1TxRSEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsTxRSES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsTxRSSES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM256TxMSEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM64TxMSEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM16TxMSEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM4TxMSEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM1TxMSEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsTxMSES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsTxMSSES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsTxMSUAS15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxRSUAS15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsTxRSUAS15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM256RxMSFEEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM64RxMSFEEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM16RxMSFEEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM4RxMSFEEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM1RxMSFEEB15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxMSFEES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxMSFESES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxMSFEUAS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM256RxMSFEEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM64RxMSFEEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM16RxMSFEEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM4RxMSFEEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM1RxMSFEEB1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxMSFEES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxMSFESES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxMSFEUAS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM256RxMSFEEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM64RxMSFEEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM16RxMSFEEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM4RxMSFEEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsSTM1RxMSFEEB15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxMSFEES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxMSFESES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsRxMSFEUAS15MinRtr"))
)
if mibBuilder.loadTexts:
    tnSdhStatsThresholdScalarsGroup.setStatus("current")

tnDwStatsThresholdScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 139)
)
tnDwStatsThresholdScalarsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu1RxRSCorrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu2RxRSCorrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu3RxRSCorrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu4RxRSCorrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu1RxRSUncorrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu2RxRSUncorrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu3RxRSUncorrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu4RxRSUncorrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu1RxSMBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu2RxSMBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu3RxSMBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu4RxSMBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOdu1RxPMBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOdu2RxPMBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOdu3RxPMBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOdu4RxPMBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsRxSMES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsRxPMES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsRxSMSES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsRxPMSES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsRxSMUAS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsRxPMUAS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu1RxRSCorrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu2RxRSCorrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu3RxRSCorrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu4RxRSCorrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu1RxRSUncorrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu2RxRSUncorrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu3RxRSUncorrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu4RxRSUncorrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu1RxSMBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu2RxSMBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu3RxSMBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu4RxSMBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOdu1RxPMBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOdu2RxPMBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOdu3RxPMBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOdu4RxPMBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsRxSMES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsRxPMES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsRxSMSES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsRxPMSES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsRxSMUAS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsRxPMUAS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu1RxRSCorrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu2RxRSCorrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu3RxRSCorrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu4RxRSCorrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu1RxRSUncorrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu2RxRSUncorrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu3RxRSUncorrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu4RxRSUncorrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu1RxSMBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu2RxSMBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu3RxSMBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOtu4RxSMBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOdu1RxPMBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOdu2RxPMBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOdu3RxPMBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsOdu4RxPMBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsRxSMES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsRxPMES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsRxSMSES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsRxPMSES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsRxSMUAS15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDw64BitStatsRxPMUAS15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOtu1RxSMFEBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOtu2RxSMFEBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOtu3RxSMFEBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOtu4RxSMFEBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOdu1RxPMFEBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOdu2RxPMFEBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOdu3RxPMFEBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOdu4RxPMFEBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxSMFEES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxPMFEES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxSMFESES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxPMFESES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxSMFEUAS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxPMFEUAS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxSMBIAES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxSMIAES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxBERPreFEC15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxBERPostFEC15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOtu1RxSMFEBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOtu2RxSMFEBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOtu3RxSMFEBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOtu4RxSMFEBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOdu1RxPMFEBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOdu2RxPMFEBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOdu3RxPMFEBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOdu4RxPMFEBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxSMFEES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxPMFEES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxSMFESES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxPMFESES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxSMFEUAS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxPMFEUAS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxSMBIAES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxSMIAES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxBERPreFEC1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxBERPostFEC1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOtu1RxSMFEBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOtu2RxSMFEBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOtu3RxSMFEBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOtu4RxSMFEBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOdu1RxPMFEBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOdu2RxPMFEBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOdu3RxPMFEBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsOdu4RxPMFEBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxSMFEES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxPMFEES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxSMFESES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxPMFESES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxSMFEUAS15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxPMFEUAS15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxSMBIAES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxSMIAES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxBERPreFEC15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsRxBERPostFEC15MinRtr"))
)
if mibBuilder.loadTexts:
    tnDwStatsThresholdScalarsGroup.setStatus("current")

tnPcsStatsThresholdScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 140)
)
tnPcsStatsThresholdScalarsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnPcsStats100GBERxCV15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats40GBERxCV15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats10GBERxCV15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsGBERxCV15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats16GFCRxCV15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats10GFCRxCV15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats8GFCRxCV15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats4GFCRxCV15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats2GFCRxCV15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsGFCRxCV15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsRxES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsRxSES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsRxSEFS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats100GBERxCV1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats40GBERxCV1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats10GBERxCV1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsGBERxCV1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats16GFCRxCV1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats10GFCRxCV1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats8GFCRxCV1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats4GFCRxCV1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats2GFCRxCV1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsGFCRxCV1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsRxES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsRxSES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsRxSEFS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats100GBERxCV15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats40GBERxCV15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats10GBERxCV15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsGBERxCV15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats16GFCRxCV15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats10GFCRxCV15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats8GFCRxCV15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats4GFCRxCV15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats2GFCRxCV15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsGFCRxCV15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsRxES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsRxSES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsRxSEFS15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats100GBETxCV15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats40GBETxCV15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats10GBETxCV15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsGBETxCV15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats16GFCTxCV15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats10GFCTxCV15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats8GFCTxCV15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats4GFCTxCV15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats2GFCTxCV15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsGFCTxCV15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsTxES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsTxSES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsTxSEFS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats100GBETxCV1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats40GBETxCV1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats10GBETxCV1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsGBETxCV1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats16GFCTxCV1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats10GFCTxCV1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats8GFCTxCV1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats4GFCTxCV1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats2GFCTxCV1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsGFCTxCV1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsTxES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsTxSES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsTxSEFS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats100GBETxCV15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats40GBETxCV15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats10GBETxCV15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsGBETxCV15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats16GFCTxCV15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats10GFCTxCV15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats8GFCTxCV15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats4GFCTxCV15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStats2GFCTxCV15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsGFCTxCV15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsTxES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsTxSES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsTxSEFS15MinRtr"))
)
if mibBuilder.loadTexts:
    tnPcsStatsThresholdScalarsGroup.setStatus("current")

tnOthOdukStatsDMConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 141)
)
tnOthOdukStatsDMConfigScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsDMConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnOthOdukStatsDMConfigScalarsGroup.setStatus("current")

tnOthOdukStatsDMConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 142)
)
tnOthOdukStatsDMConfigGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOthOdukStatsDMNumberofBins"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsDMProfileid"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsDMClear"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsDMIntervalLength"))
)
if mibBuilder.loadTexts:
    tnOthOdukStatsDMConfigGroup.setStatus("current")

tnOthOdukStatsDMScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 143)
)
tnOthOdukStatsDMScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsDMTotalMembers")
)
if mibBuilder.loadTexts:
    tnOthOdukStatsDMScalarsGroup.setStatus("current")

tnOthOdukStatsDMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 144)
)
tnOthOdukStatsDMGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOthOdukStatsDMBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsDMStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsDMMinDm"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsDMMaxDm"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsDMAverageDm"))
)
if mibBuilder.loadTexts:
    tnOthOdukStatsDMGroup.setStatus("current")

tnOthOdukRawCountStatsDMScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 145)
)
tnOthOdukRawCountStatsDMScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatsDMTotalMembers")
)
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsDMScalarsGroup.setStatus("current")

tnOthOdukRawCountStatsDMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 146)
)
tnOthOdukRawCountStatsDMGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatsDMClear"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatsDMStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatsDMMinDm"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatsDMMaxDm"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatsDMAverageDm"))
)
if mibBuilder.loadTexts:
    tnOthOdukRawCountStatsDMGroup.setStatus("current")

tnOthOdukStatsTcmConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 147)
)
tnOthOdukStatsTcmConfigScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmConfigScalarsGroup.setStatus("current")

tnOthOdukStatsTcmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 148)
)
tnOthOdukStatsTcmConfigGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmConfigNumberOfBins"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmConfigProfileId"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmConfigClear"))
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmConfigGroup.setStatus("current")

tnOthOdukStatsTcmEnableScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 149)
)
tnOthOdukStatsTcmEnableScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmEnableAttributeTotal")
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmEnableScalarsGroup.setStatus("current")

tnOthOdukStatsTcmEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 150)
)
tnOthOdukStatsTcmEnableGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmClearAll"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmEnable"))
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmEnableGroup.setStatus("current")

tnStatsLanePwrsConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 151)
)
tnStatsLanePwrsConfigScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnStatsLanePwrsConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnStatsLanePwrsConfigScalarsGroup.setStatus("current")

tnStatsLanePwrsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 152)
)
tnStatsLanePwrsConfigGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnStatsLanePwrsConfigProfileId")
)
if mibBuilder.loadTexts:
    tnStatsLanePwrsConfigGroup.setStatus("current")

tnOthOdukStatsTcmScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 153)
)
tnOthOdukStatsTcmScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmTotalMembers")
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmScalarsGroup.setStatus("current")

tnOthOdukStatsTcmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 154)
)
tnOthOdukStatsTcmGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmBinStatus"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmStartTime"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmNeRxBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmNeRxIAESErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmNeRxES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmNeRxSES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmNeRxUAS"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmFeRxBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmFeRxBIAESErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmFeRxES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmFeRxSES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmFeRxUAS"))
)
if mibBuilder.loadTexts:
    tnOthOdukStatsTcmGroup.setStatus("current")

tnTcmStatsThresholdScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 155)
)
tnTcmStatsThresholdScalarsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOthOdu0StatsTcmNeRxBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu0StatsTcmNeRxBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu0StatsTcmNeRxBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu0StatsTcmFeRxBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu0StatsTcmFeRxBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu0StatsTcmFeRxBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu1StatsTcmNeRxBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu1StatsTcmNeRxBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu1StatsTcmNeRxBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu1StatsTcmFeRxBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu1StatsTcmFeRxBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu1StatsTcmFeRxBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu2StatsTcmNeRxBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu2StatsTcmNeRxBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu2StatsTcmNeRxBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu2StatsTcmFeRxBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu2StatsTcmFeRxBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu2StatsTcmFeRxBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu3StatsTcmNeRxBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu3StatsTcmNeRxBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu3StatsTcmNeRxBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu3StatsTcmFeRxBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu3StatsTcmFeRxBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu3StatsTcmFeRxBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu4StatsTcmNeRxBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu4StatsTcmNeRxBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu4StatsTcmNeRxBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu4StatsTcmFeRxBIP8ErrCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu4StatsTcmFeRxBIP8ErrCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdu4StatsTcmFeRxBIP8ErrCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmNeRxES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmNeRxES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmNeRxES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmFeRxES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmFeRxES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmFeRxES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmNeRxSES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmNeRxSES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmNeRxSES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmFeRxSES15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmFeRxSES15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmFeRxSES1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmNeRxUAS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmNeRxUAS15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmNeRxUAS1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmFeRxUAS15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmFeRxUAS15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmFeRxUAS1DayTr"))
)
if mibBuilder.loadTexts:
    tnTcmStatsThresholdScalarsGroup.setStatus("current")

tnOpticalLaneStatPowerScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 156)
)
tnOpticalLaneStatPowerScalarsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOprLaneStatMaxPowerTr"),
        ("TROPIC-STATISTICS-MIB", "tnOprLaneStatMinPowerTr"),
        ("TROPIC-STATISTICS-MIB", "tnOptLaneStatMaxPowerTr"),
        ("TROPIC-STATISTICS-MIB", "tnOptLaneStatMinPowerTr"))
)
if mibBuilder.loadTexts:
    tnOpticalLaneStatPowerScalarsGroup.setStatus("current")

tnTcmRawCountStatsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 157)
)
tnTcmRawCountStatsScalarsGroup.setObjects(
    ("TROPIC-STATISTICS-MIB", "tnOthOdukTcmRawCountStatsTotalMembers")
)
if mibBuilder.loadTexts:
    tnTcmRawCountStatsScalarsGroup.setStatus("current")

tnTcmRawCountStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 158)
)
tnTcmRawCountStatsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnOthOdukTcmRawCountStatsClear"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukTcmRawCountStatsNeRxBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukTcmRawCountStatsNeRxIAESErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukTcmRawCountStatsNeRxES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukTcmRawCountStatsNeRxSES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukTcmRawCountStatsNeRxUAS"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukTcmRawCountStatsFeRxBIP8ErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukTcmRawCountStatsFeRxBIAESErrCnt"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukTcmRawCountStatsFeRxES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukTcmRawCountStatsFeRxSES"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukTcmRawCountStatsFeRxUAS"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukTcmRawCountStatsStartTime"))
)
if mibBuilder.loadTexts:
    tnTcmRawCountStatsGroup.setStatus("current")

tnEncryptionFailToDecryptScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 1, 159)
)
tnEncryptionFailToDecryptScalarsGroup.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnEncryptRxFailToDecryptCnt15MinTr"),
        ("TROPIC-STATISTICS-MIB", "tnEncryptRxFailToDecryptCnt15MinRtr"),
        ("TROPIC-STATISTICS-MIB", "tnEncryptRxFailToDecryptCnt1DayTr"),
        ("TROPIC-STATISTICS-MIB", "tnEncryptRxFailToDecryptCnt1DayRtr"))
)
if mibBuilder.loadTexts:
    tnEncryptionFailToDecryptScalarsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnStatisticsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1, 1, 2, 1)
)
tnStatisticsCompliance.setObjects(
      *(("TROPIC-STATISTICS-MIB", "tnStatsPortIntervalGroup"),
        ("TROPIC-STATISTICS-MIB", "tnStatsCardIntervalGroup"),
        ("TROPIC-STATISTICS-MIB", "tnStatsPortConfGroup"),
        ("TROPIC-STATISTICS-MIB", "tnStatsCardConfGroup"),
        ("TROPIC-STATISTICS-MIB", "tnStatsTCAProfileGroup"),
        ("TROPIC-STATISTICS-MIB", "tnStatsTCAGroup"),
        ("TROPIC-STATISTICS-MIB", "tnCardStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnCardStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnInterfaceStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnInterfaceStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnEtherStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnControlNetworkLinkRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnControlNetworkLinkRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnCardRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnCardRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnInterfaceRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnInterfaceRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnEtherRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnSonetRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOptStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOptStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOprStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOprStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOptRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOptRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOprRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOprRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOpOutStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOpOutStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOpInStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOpInStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOpOutRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOpOutRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOpInRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOpInRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchOutStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchOutStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchInStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchInStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchOutRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchOutRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchInRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOpOchInRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnStatsPortClearAllGroup"),
        ("TROPIC-STATISTICS-MIB", "tnStatsTCAScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnSdhRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnPhyCodeSublayerRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnDigitalWrapper64BitStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnDigitalWrapper64BitStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnDigitalWrapper64BitRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnDigitalWrapper64BitRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnStatsBaselineGroup"),
        ("TROPIC-STATISTICS-MIB", "tnCdrStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnCdrStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnCdrRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnCdrRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnDgdrStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnDgdrStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnDgdrRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnDgdrRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnFoffrStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnFoffrStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnFoffrRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnFoffrRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnE1StatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnE1RawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnE1RawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnPreFECBitsStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnPreFECBitsStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnPreFECBitsRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnPreFECBitsRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnEncrypt64BitStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnEncrypt64BitStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnEncrypt64BitRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnEncrypt64BitRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxConfigScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxConfigGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxConfigScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxConfigGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsControlScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsControlGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsRxThresholdScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTxThresholdScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukStatsThresholdScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatsRxScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatsRxGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatsTxScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatsTxGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOtukRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOsnrStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOsnrStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOsnrRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOsnrRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnSonetStatsThresholdScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnSdhStatsThresholdScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnDwStatsThresholdScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnPcsStatsThresholdScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsDMConfigScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsDMConfigGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsDMScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsDMGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatsDMScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukRawCountStatsDMGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmConfigScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmConfigGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmEnableScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmEnableGroup"),
        ("TROPIC-STATISTICS-MIB", "tnStatsLanePwrsConfigScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnStatsLanePwrsConfigGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOthOdukStatsTcmGroup"),
        ("TROPIC-STATISTICS-MIB", "tnTcmStatsThresholdScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnOpticalLaneStatPowerScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnTcmRawCountStatsScalarsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnTcmRawCountStatsGroup"),
        ("TROPIC-STATISTICS-MIB", "tnEncryptionFailToDecryptScalarsGroup"))
)
if mibBuilder.loadTexts:
    tnStatisticsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-STATISTICS-MIB",
    **{"TnStatsGroupId": TnStatsGroupId,
       "TnStatsIntervalType": TnStatsIntervalType,
       "TnStatsBinType": TnStatsBinType,
       "TnStatsBinStatus": TnStatsBinStatus,
       "tnStatisticsMibModule": tnStatisticsMibModule,
       "tnStatisticsConf": tnStatisticsConf,
       "tnStatisticsGroups": tnStatisticsGroups,
       "tnStatsPortIntervalGroup": tnStatsPortIntervalGroup,
       "tnStatsCardIntervalGroup": tnStatsCardIntervalGroup,
       "tnStatsPortConfGroup": tnStatsPortConfGroup,
       "tnStatsCardConfGroup": tnStatsCardConfGroup,
       "tnStatsTCAProfileGroup": tnStatsTCAProfileGroup,
       "tnStatsTCAGroup": tnStatsTCAGroup,
       "tnCardStatsScalarsGroup": tnCardStatsScalarsGroup,
       "tnCardStatsGroup": tnCardStatsGroup,
       "tnInterfaceStatsScalarsGroup": tnInterfaceStatsScalarsGroup,
       "tnInterfaceStatsGroup": tnInterfaceStatsGroup,
       "tnEtherStatsScalarsGroup": tnEtherStatsScalarsGroup,
       "tnEtherStatsGroup": tnEtherStatsGroup,
       "tnSonetStatsScalarsGroup": tnSonetStatsScalarsGroup,
       "tnSonetStatsGroup": tnSonetStatsGroup,
       "tnControlNetworkLinkRawCountStatsScalarsGroup": tnControlNetworkLinkRawCountStatsScalarsGroup,
       "tnControlNetworkLinkRawCountStatsGroup": tnControlNetworkLinkRawCountStatsGroup,
       "tnCardRawCountStatsScalarsGroup": tnCardRawCountStatsScalarsGroup,
       "tnCardRawCountStatsGroup": tnCardRawCountStatsGroup,
       "tnInterfaceRawCountStatsScalarsGroup": tnInterfaceRawCountStatsScalarsGroup,
       "tnInterfaceRawCountStatsGroup": tnInterfaceRawCountStatsGroup,
       "tnEtherRawCountStatsScalarsGroup": tnEtherRawCountStatsScalarsGroup,
       "tnEtherRawCountStatsGroup": tnEtherRawCountStatsGroup,
       "tnSonetRawCountStatsScalarsGroup": tnSonetRawCountStatsScalarsGroup,
       "tnSonetRawCountStatsGroup": tnSonetRawCountStatsGroup,
       "tnOptStatsScalarsGroup": tnOptStatsScalarsGroup,
       "tnOptStatsGroup": tnOptStatsGroup,
       "tnOprStatsScalarsGroup": tnOprStatsScalarsGroup,
       "tnOprStatsGroup": tnOprStatsGroup,
       "tnOptRawCountStatsScalarsGroup": tnOptRawCountStatsScalarsGroup,
       "tnOptRawCountStatsGroup": tnOptRawCountStatsGroup,
       "tnOprRawCountStatsScalarsGroup": tnOprRawCountStatsScalarsGroup,
       "tnOprRawCountStatsGroup": tnOprRawCountStatsGroup,
       "tnOpOutStatsScalarsGroup": tnOpOutStatsScalarsGroup,
       "tnOpOutStatsGroup": tnOpOutStatsGroup,
       "tnOpInStatsScalarsGroup": tnOpInStatsScalarsGroup,
       "tnOpInStatsGroup": tnOpInStatsGroup,
       "tnOpOutRawCountStatsScalarsGroup": tnOpOutRawCountStatsScalarsGroup,
       "tnOpOutRawCountStatsGroup": tnOpOutRawCountStatsGroup,
       "tnOpInRawCountStatsScalarsGroup": tnOpInRawCountStatsScalarsGroup,
       "tnOpInRawCountStatsGroup": tnOpInRawCountStatsGroup,
       "tnOpOchOutStatsScalarsGroup": tnOpOchOutStatsScalarsGroup,
       "tnOpOchOutStatsGroup": tnOpOchOutStatsGroup,
       "tnOpOchInStatsScalarsGroup": tnOpOchInStatsScalarsGroup,
       "tnOpOchInStatsGroup": tnOpOchInStatsGroup,
       "tnOpOchOutRawCountStatsScalarsGroup": tnOpOchOutRawCountStatsScalarsGroup,
       "tnOpOchOutRawCountStatsGroup": tnOpOchOutRawCountStatsGroup,
       "tnOpOchInRawCountStatsScalarsGroup": tnOpOchInRawCountStatsScalarsGroup,
       "tnOpOchInRawCountStatsGroup": tnOpOchInRawCountStatsGroup,
       "tnStatsPortClearAllGroup": tnStatsPortClearAllGroup,
       "tnStatsTCAScalarsGroup": tnStatsTCAScalarsGroup,
       "tnSdhStatsScalarsGroup": tnSdhStatsScalarsGroup,
       "tnSdhStatsGroup": tnSdhStatsGroup,
       "tnSdhRawCountStatsScalarsGroup": tnSdhRawCountStatsScalarsGroup,
       "tnSdhRawCountStatsGroup": tnSdhRawCountStatsGroup,
       "tnPhyCodeSublayerStatsScalarsGroup": tnPhyCodeSublayerStatsScalarsGroup,
       "tnPhyCodeSublayerStatsGroup": tnPhyCodeSublayerStatsGroup,
       "tnPhyCodeSublayerRawCountStatsScalarsGroup": tnPhyCodeSublayerRawCountStatsScalarsGroup,
       "tnPhyCodeSublayerRawCountStatsGroup": tnPhyCodeSublayerRawCountStatsGroup,
       "tnDigitalWrapper64BitStatsScalarsGroup": tnDigitalWrapper64BitStatsScalarsGroup,
       "tnDigitalWrapper64BitStatsGroup": tnDigitalWrapper64BitStatsGroup,
       "tnDigitalWrapper64BitRawCountStatsScalarsGroup": tnDigitalWrapper64BitRawCountStatsScalarsGroup,
       "tnDigitalWrapper64BitRawCountStatsGroup": tnDigitalWrapper64BitRawCountStatsGroup,
       "tnStatsBaselineGroup": tnStatsBaselineGroup,
       "tnCdrStatsScalarsGroup": tnCdrStatsScalarsGroup,
       "tnCdrStatsGroup": tnCdrStatsGroup,
       "tnCdrRawCountStatsScalarsGroup": tnCdrRawCountStatsScalarsGroup,
       "tnCdrRawCountStatsGroup": tnCdrRawCountStatsGroup,
       "tnDgdrStatsScalarsGroup": tnDgdrStatsScalarsGroup,
       "tnDgdrStatsGroup": tnDgdrStatsGroup,
       "tnDgdrRawCountStatsScalarsGroup": tnDgdrRawCountStatsScalarsGroup,
       "tnDgdrRawCountStatsGroup": tnDgdrRawCountStatsGroup,
       "tnFoffrStatsScalarsGroup": tnFoffrStatsScalarsGroup,
       "tnFoffrStatsGroup": tnFoffrStatsGroup,
       "tnFoffrRawCountStatsScalarsGroup": tnFoffrRawCountStatsScalarsGroup,
       "tnFoffrRawCountStatsGroup": tnFoffrRawCountStatsGroup,
       "tnE1StatsScalarsGroup": tnE1StatsScalarsGroup,
       "tnE1StatsGroup": tnE1StatsGroup,
       "tnE1RawCountStatsScalarsGroup": tnE1RawCountStatsScalarsGroup,
       "tnE1RawCountStatsGroup": tnE1RawCountStatsGroup,
       "tnPreFECBitsStatsScalarsGroup": tnPreFECBitsStatsScalarsGroup,
       "tnPreFECBitsStatsGroup": tnPreFECBitsStatsGroup,
       "tnPreFECBitsRawCountStatsScalarsGroup": tnPreFECBitsRawCountStatsScalarsGroup,
       "tnPreFECBitsRawCountStatsGroup": tnPreFECBitsRawCountStatsGroup,
       "tnEncrypt64BitStatsScalarsGroup": tnEncrypt64BitStatsScalarsGroup,
       "tnEncrypt64BitStatsGroup": tnEncrypt64BitStatsGroup,
       "tnEncrypt64BitRawCountStatsScalarsGroup": tnEncrypt64BitRawCountStatsScalarsGroup,
       "tnEncrypt64BitRawCountStatsGroup": tnEncrypt64BitRawCountStatsGroup,
       "tnOthOdukStatsRxConfigScalarsGroup": tnOthOdukStatsRxConfigScalarsGroup,
       "tnOthOdukStatsRxConfigGroup": tnOthOdukStatsRxConfigGroup,
       "tnOthOdukStatsTxConfigScalarsGroup": tnOthOdukStatsTxConfigScalarsGroup,
       "tnOthOdukStatsTxConfigGroup": tnOthOdukStatsTxConfigGroup,
       "tnOthOdukStatsControlScalarsGroup": tnOthOdukStatsControlScalarsGroup,
       "tnOthOdukStatsControlGroup": tnOthOdukStatsControlGroup,
       "tnOthOdukStatsRxScalarsGroup": tnOthOdukStatsRxScalarsGroup,
       "tnOthOdukStatsRxGroup": tnOthOdukStatsRxGroup,
       "tnOthOdukStatsTxScalarsGroup": tnOthOdukStatsTxScalarsGroup,
       "tnOthOdukStatsTxGroup": tnOthOdukStatsTxGroup,
       "tnOthOtukStatsScalarsGroup": tnOthOtukStatsScalarsGroup,
       "tnOthOtukStatsGroup": tnOthOtukStatsGroup,
       "tnOthOdukStatsRxThresholdScalarsGroup": tnOthOdukStatsRxThresholdScalarsGroup,
       "tnOthOdukStatsTxThresholdScalarsGroup": tnOthOdukStatsTxThresholdScalarsGroup,
       "tnOthOtukStatsThresholdScalarsGroup": tnOthOtukStatsThresholdScalarsGroup,
       "tnOthOdukRawCountStatsRxScalarsGroup": tnOthOdukRawCountStatsRxScalarsGroup,
       "tnOthOdukRawCountStatsRxGroup": tnOthOdukRawCountStatsRxGroup,
       "tnOthOdukRawCountStatsTxScalarsGroup": tnOthOdukRawCountStatsTxScalarsGroup,
       "tnOthOdukRawCountStatsTxGroup": tnOthOdukRawCountStatsTxGroup,
       "tnOthOtukRawCountStatsScalarsGroup": tnOthOtukRawCountStatsScalarsGroup,
       "tnOthOtukRawCountStatsGroup": tnOthOtukRawCountStatsGroup,
       "tnOsnrStatsScalarsGroup": tnOsnrStatsScalarsGroup,
       "tnOsnrStatsGroup": tnOsnrStatsGroup,
       "tnOsnrRawCountStatsScalarsGroup": tnOsnrRawCountStatsScalarsGroup,
       "tnOsnrRawCountStatsGroup": tnOsnrRawCountStatsGroup,
       "tnSonetStatsThresholdScalarsGroup": tnSonetStatsThresholdScalarsGroup,
       "tnSdhStatsThresholdScalarsGroup": tnSdhStatsThresholdScalarsGroup,
       "tnDwStatsThresholdScalarsGroup": tnDwStatsThresholdScalarsGroup,
       "tnPcsStatsThresholdScalarsGroup": tnPcsStatsThresholdScalarsGroup,
       "tnOthOdukStatsDMConfigScalarsGroup": tnOthOdukStatsDMConfigScalarsGroup,
       "tnOthOdukStatsDMConfigGroup": tnOthOdukStatsDMConfigGroup,
       "tnOthOdukStatsDMScalarsGroup": tnOthOdukStatsDMScalarsGroup,
       "tnOthOdukStatsDMGroup": tnOthOdukStatsDMGroup,
       "tnOthOdukRawCountStatsDMScalarsGroup": tnOthOdukRawCountStatsDMScalarsGroup,
       "tnOthOdukRawCountStatsDMGroup": tnOthOdukRawCountStatsDMGroup,
       "tnOthOdukStatsTcmConfigScalarsGroup": tnOthOdukStatsTcmConfigScalarsGroup,
       "tnOthOdukStatsTcmConfigGroup": tnOthOdukStatsTcmConfigGroup,
       "tnOthOdukStatsTcmEnableScalarsGroup": tnOthOdukStatsTcmEnableScalarsGroup,
       "tnOthOdukStatsTcmEnableGroup": tnOthOdukStatsTcmEnableGroup,
       "tnStatsLanePwrsConfigScalarsGroup": tnStatsLanePwrsConfigScalarsGroup,
       "tnStatsLanePwrsConfigGroup": tnStatsLanePwrsConfigGroup,
       "tnOthOdukStatsTcmScalarsGroup": tnOthOdukStatsTcmScalarsGroup,
       "tnOthOdukStatsTcmGroup": tnOthOdukStatsTcmGroup,
       "tnTcmStatsThresholdScalarsGroup": tnTcmStatsThresholdScalarsGroup,
       "tnOpticalLaneStatPowerScalarsGroup": tnOpticalLaneStatPowerScalarsGroup,
       "tnTcmRawCountStatsScalarsGroup": tnTcmRawCountStatsScalarsGroup,
       "tnTcmRawCountStatsGroup": tnTcmRawCountStatsGroup,
       "tnEncryptionFailToDecryptScalarsGroup": tnEncryptionFailToDecryptScalarsGroup,
       "tnStatisticsCompliances": tnStatisticsCompliances,
       "tnStatisticsCompliance": tnStatisticsCompliance,
       "tnStatisticsObjs": tnStatisticsObjs,
       "tnStatisticsTCA": tnStatisticsTCA,
       "tnStatsPortIntervalTable": tnStatsPortIntervalTable,
       "tnStatsPortIntervalEntry": tnStatsPortIntervalEntry,
       "tnStatsPortNumberOfIntervals": tnStatsPortNumberOfIntervals,
       "tnStatsCardIntervalTable": tnStatsCardIntervalTable,
       "tnStatsCardIntervalEntry": tnStatsCardIntervalEntry,
       "tnStatsCardNumberOfIntervals": tnStatsCardNumberOfIntervals,
       "tnStatsPortTable": tnStatsPortTable,
       "tnStatsPortEntry": tnStatsPortEntry,
       "tnStatsInterval": tnStatsInterval,
       "tnStatsPortIntervalLength": tnStatsPortIntervalLength,
       "tnStatsPortNumberOfBins": tnStatsPortNumberOfBins,
       "tnStatsPortProfileId": tnStatsPortProfileId,
       "tnStatsPortClear": tnStatsPortClear,
       "tnStatsCardTable": tnStatsCardTable,
       "tnStatsCardEntry": tnStatsCardEntry,
       "tnStatsCardIntervalLength": tnStatsCardIntervalLength,
       "tnStatsCardNumberOfBins": tnStatsCardNumberOfBins,
       "tnStatsCardProfileId": tnStatsCardProfileId,
       "tnStatsCardClear": tnStatsCardClear,
       "tnStatsTCAProfileTable": tnStatsTCAProfileTable,
       "tnStatsTCAProfileEntry": tnStatsTCAProfileEntry,
       "tnStatsGroupId": tnStatsGroupId,
       "tnStatsTCAProfileId": tnStatsTCAProfileId,
       "tnStatsTCAProfileDescr": tnStatsTCAProfileDescr,
       "tnStatsTCATable": tnStatsTCATable,
       "tnStatsTCAEntry": tnStatsTCAEntry,
       "tnStatsTCAVariableId": tnStatsTCAVariableId,
       "tnStatsTCAVariable": tnStatsTCAVariable,
       "tnStatsTCAValue": tnStatsTCAValue,
       "tnStatsTCAItuTable": tnStatsTCAItuTable,
       "tnStatsTCAItuEntry": tnStatsTCAItuEntry,
       "tnOpticalStatsITUChannel": tnOpticalStatsITUChannel,
       "tnStatsPortClearAllTable": tnStatsPortClearAllTable,
       "tnStatsPortClearAllEntry": tnStatsPortClearAllEntry,
       "tnStatsPortClearAll": tnStatsPortClearAll,
       "tnStatsClearAll": tnStatsClearAll,
       "tnOthOdukStatsRxConfigAttributeTotal": tnOthOdukStatsRxConfigAttributeTotal,
       "tnOthOdukStatsRxConfigTable": tnOthOdukStatsRxConfigTable,
       "tnOthOdukStatsRxConfigEntry": tnOthOdukStatsRxConfigEntry,
       "tnOthOdukStatsRxNumberofBins": tnOthOdukStatsRxNumberofBins,
       "tnOthOdukStatsRxProfileid": tnOthOdukStatsRxProfileid,
       "tnOthOdukStatsRxClear": tnOthOdukStatsRxClear,
       "tnOthOdukStatsRxIntervalLength": tnOthOdukStatsRxIntervalLength,
       "tnOthOdukStatsTxConfigAttributeTotal": tnOthOdukStatsTxConfigAttributeTotal,
       "tnOthOdukStatsTxConfigTable": tnOthOdukStatsTxConfigTable,
       "tnOthOdukStatsTxConfigEntry": tnOthOdukStatsTxConfigEntry,
       "tnOthOdukStatsTxNumberofBins": tnOthOdukStatsTxNumberofBins,
       "tnOthOdukStatsTxProfileid": tnOthOdukStatsTxProfileid,
       "tnOthOdukStatsTxClear": tnOthOdukStatsTxClear,
       "tnOthOdukStatsTxIntervalLength": tnOthOdukStatsTxIntervalLength,
       "tnOthOdukStatsControlAttributeTotal": tnOthOdukStatsControlAttributeTotal,
       "tnOthOdukStatsControlTable": tnOthOdukStatsControlTable,
       "tnOthOdukStatsControlEntry": tnOthOdukStatsControlEntry,
       "tnOthOdukStatsClearAll": tnOthOdukStatsClearAll,
       "tnOthOdukStatsRxEnable": tnOthOdukStatsRxEnable,
       "tnOthOdukStatsTxEnable": tnOthOdukStatsTxEnable,
       "tnOthOdukStatsDMConfigAttributeTotal": tnOthOdukStatsDMConfigAttributeTotal,
       "tnOthOdukStatsDMConfigTable": tnOthOdukStatsDMConfigTable,
       "tnOthOdukStatsDMConfigEntry": tnOthOdukStatsDMConfigEntry,
       "tnOthOdukStatsDMNumberofBins": tnOthOdukStatsDMNumberofBins,
       "tnOthOdukStatsDMProfileid": tnOthOdukStatsDMProfileid,
       "tnOthOdukStatsDMClear": tnOthOdukStatsDMClear,
       "tnOthOdukStatsDMIntervalLength": tnOthOdukStatsDMIntervalLength,
       "tnOthOdukStatsTcmConfigAttributeTotal": tnOthOdukStatsTcmConfigAttributeTotal,
       "tnOthOdukStatsTcmConfigTable": tnOthOdukStatsTcmConfigTable,
       "tnOthOdukStatsTcmConfigEntry": tnOthOdukStatsTcmConfigEntry,
       "tnOthOdukStatsTcmConfigNumberOfBins": tnOthOdukStatsTcmConfigNumberOfBins,
       "tnOthOdukStatsTcmConfigProfileId": tnOthOdukStatsTcmConfigProfileId,
       "tnOthOdukStatsTcmConfigClear": tnOthOdukStatsTcmConfigClear,
       "tnOthOdukStatsTcmEnableAttributeTotal": tnOthOdukStatsTcmEnableAttributeTotal,
       "tnOthOdukStatsTcmEnableTable": tnOthOdukStatsTcmEnableTable,
       "tnOthOdukStatsTcmEnableEntry": tnOthOdukStatsTcmEnableEntry,
       "tnOthOdukStatsTcmClearAll": tnOthOdukStatsTcmClearAll,
       "tnOthOdukStatsTcmEnable": tnOthOdukStatsTcmEnable,
       "tnStatsLanePwrsConfigAttributeTotal": tnStatsLanePwrsConfigAttributeTotal,
       "tnStatsLanePwrsConfigTable": tnStatsLanePwrsConfigTable,
       "tnStatsLanePwrsConfigEntry": tnStatsLanePwrsConfigEntry,
       "tnStatsLanePwrsConfigProfileId": tnStatsLanePwrsConfigProfileId,
       "tnStatisticsGrouping": tnStatisticsGrouping,
       "tnCardStatsTotalMembers": tnCardStatsTotalMembers,
       "tnCardStatsTable": tnCardStatsTable,
       "tnCardStatsEntry": tnCardStatsEntry,
       "tnCardStatsProcessor": tnCardStatsProcessor,
       "tnCardStatsBin": tnCardStatsBin,
       "tnCardStatsBinStatus": tnCardStatsBinStatus,
       "tnCardStatsStartTime": tnCardStatsStartTime,
       "tnCardStatCpuAverage": tnCardStatCpuAverage,
       "tnCardStatHeapUsage": tnCardStatHeapUsage,
       "tnCardStatPoolUsage": tnCardStatPoolUsage,
       "tnInterfaceStatsTotalMembers": tnInterfaceStatsTotalMembers,
       "tnInterfaceStatsTable": tnInterfaceStatsTable,
       "tnInterfaceStatsEntry": tnInterfaceStatsEntry,
       "tnIfStatsBin": tnIfStatsBin,
       "tnIfStatsBinStatus": tnIfStatsBinStatus,
       "tnIfStatsStartTime": tnIfStatsStartTime,
       "tnIfStatInOctets": tnIfStatInOctets,
       "tnIfStatInUcastPkts": tnIfStatInUcastPkts,
       "tnIfStatInDiscards": tnIfStatInDiscards,
       "tnIfStatInErrors": tnIfStatInErrors,
       "tnIfStatInUnknownProtos": tnIfStatInUnknownProtos,
       "tnIfStatOutOctets": tnIfStatOutOctets,
       "tnIfStatOutUcastPkts": tnIfStatOutUcastPkts,
       "tnIfStatOutDiscards": tnIfStatOutDiscards,
       "tnIfStatOutErrors": tnIfStatOutErrors,
       "tnIfStatInMulticastPkts": tnIfStatInMulticastPkts,
       "tnIfStatInBroadcastPkts": tnIfStatInBroadcastPkts,
       "tnIfStatOutMulticastPkts": tnIfStatOutMulticastPkts,
       "tnIfStatOutBroadcastPkts": tnIfStatOutBroadcastPkts,
       "tnIfStatInPacketsNotClassified": tnIfStatInPacketsNotClassified,
       "tnEtherStatsTotalMembers": tnEtherStatsTotalMembers,
       "tnEtherStatsTable": tnEtherStatsTable,
       "tnEtherStatsEntry": tnEtherStatsEntry,
       "tnEtherStatsBin": tnEtherStatsBin,
       "tnEtherStatsBinStatus": tnEtherStatsBinStatus,
       "tnEtherStatsStartTime": tnEtherStatsStartTime,
       "tnEtherStatRxDropEvents": tnEtherStatRxDropEvents,
       "tnEtherStatRxFragments": tnEtherStatRxFragments,
       "tnEtherStatRxJabbers": tnEtherStatRxJabbers,
       "tnEtherStatRxMcastPkts": tnEtherStatRxMcastPkts,
       "tnEtherStatRxOctets": tnEtherStatRxOctets,
       "tnEtherStatRxOversizedPkts": tnEtherStatRxOversizedPkts,
       "tnEtherStatRxPkts": tnEtherStatRxPkts,
       "tnEtherStatRxPktsSize1024to1518": tnEtherStatRxPktsSize1024to1518,
       "tnEtherStatRxPktsSize128to255": tnEtherStatRxPktsSize128to255,
       "tnEtherStatRxPktsSize256to511": tnEtherStatRxPktsSize256to511,
       "tnEtherStatRxPktsSize512to1023": tnEtherStatRxPktsSize512to1023,
       "tnEtherStatRxPktsSize65to127": tnEtherStatRxPktsSize65to127,
       "tnEtherStatRxUndersizedPkts": tnEtherStatRxUndersizedPkts,
       "tnEtherStatTxBcastPkts": tnEtherStatTxBcastPkts,
       "tnEtherStatTxCrcAlignErrs": tnEtherStatTxCrcAlignErrs,
       "tnEtherStatTxDropEvents": tnEtherStatTxDropEvents,
       "tnEtherStatTxFragments": tnEtherStatTxFragments,
       "tnEtherStatTxJabbers": tnEtherStatTxJabbers,
       "tnEtherStatTxMcastPkts": tnEtherStatTxMcastPkts,
       "tnEtherStatTxOctets": tnEtherStatTxOctets,
       "tnEtherStatTxOversizedPkts": tnEtherStatTxOversizedPkts,
       "tnEtherStatTxPkts": tnEtherStatTxPkts,
       "tnEtherStatTxPktsSize1024to1518": tnEtherStatTxPktsSize1024to1518,
       "tnEtherStatTxPktsSize128to255": tnEtherStatTxPktsSize128to255,
       "tnEtherStatTxPktsSize256to511": tnEtherStatTxPktsSize256to511,
       "tnEtherStatTxPktsSize512to1023": tnEtherStatTxPktsSize512to1023,
       "tnEtherStatTxPktsSize65to127": tnEtherStatTxPktsSize65to127,
       "tnEtherStatTxUndersizedPkts": tnEtherStatTxUndersizedPkts,
       "tnEtherStatRxBcastPkts": tnEtherStatRxBcastPkts,
       "tnEtherStatRxCrcAlignErrs": tnEtherStatRxCrcAlignErrs,
       "tnEtherStatRxCollisions": tnEtherStatRxCollisions,
       "tnEtherStatRxJumboPkts": tnEtherStatRxJumboPkts,
       "tnEtherStatTxCollisions": tnEtherStatTxCollisions,
       "tnEtherStatTxJumboPkts": tnEtherStatTxJumboPkts,
       "tnEtherStatRxPktsSize64": tnEtherStatRxPktsSize64,
       "tnEtherStatTxPktsSize64": tnEtherStatTxPktsSize64,
       "tnEtherStatRxPktErrRatio": tnEtherStatRxPktErrRatio,
       "tnEtherStatTxPktErrRatio": tnEtherStatTxPktErrRatio,
       "tnEtherStatRxPktErrRatio15MinTr": tnEtherStatRxPktErrRatio15MinTr,
       "tnEtherStatTxPktErrRatio15MinTr": tnEtherStatTxPktErrRatio15MinTr,
       "tnEtherStatRxPktErrRatio1DayTr": tnEtherStatRxPktErrRatio1DayTr,
       "tnEtherStatTxPktErrRatio1DayTr": tnEtherStatTxPktErrRatio1DayTr,
       "tnEtherStatRxPktErrRatio15MinRtr": tnEtherStatRxPktErrRatio15MinRtr,
       "tnEtherStatTxPktErrRatio15MinRtr": tnEtherStatTxPktErrRatio15MinRtr,
       "tnSonetStatsTotalMembers": tnSonetStatsTotalMembers,
       "tnSonetStatsTable": tnSonetStatsTable,
       "tnSonetStatsEntry": tnSonetStatsEntry,
       "tnSonetStatsBin": tnSonetStatsBin,
       "tnSonetStatsBinStatus": tnSonetStatsBinStatus,
       "tnSonetStatsStartTime": tnSonetStatsStartTime,
       "tnSonetStatRxCVS": tnSonetStatRxCVS,
       "tnSonetStatRxESS": tnSonetStatRxESS,
       "tnSonetStatRxSESS": tnSonetStatRxSESS,
       "tnSonetStatRxSEFSS": tnSonetStatRxSEFSS,
       "tnSonetStatRxCVL": tnSonetStatRxCVL,
       "tnSonetStatRxESL": tnSonetStatRxESL,
       "tnSonetStatRxSESL": tnSonetStatRxSESL,
       "tnSonetStatRxUASL": tnSonetStatRxUASL,
       "tnSonetStatRxFCL": tnSonetStatRxFCL,
       "tnSonetStatTxCVS": tnSonetStatTxCVS,
       "tnSonetStatTxESS": tnSonetStatTxESS,
       "tnSonetStatTxSESS": tnSonetStatTxSESS,
       "tnSonetStatTxSEFSS": tnSonetStatTxSEFSS,
       "tnSonetStatTxCVL": tnSonetStatTxCVL,
       "tnSonetStatTxESL": tnSonetStatTxESL,
       "tnSonetStatTxSESL": tnSonetStatTxSESL,
       "tnSonetStatTxUASL": tnSonetStatTxUASL,
       "tnSonetStatTxFCL": tnSonetStatTxFCL,
       "tnSonetStatRxUASS": tnSonetStatRxUASS,
       "tnSonetStatTxUASS": tnSonetStatTxUASS,
       "tnSonetStatRxFECVL": tnSonetStatRxFECVL,
       "tnSonetStatRxFEESL": tnSonetStatRxFEESL,
       "tnSonetStatRxFESESL": tnSonetStatRxFESESL,
       "tnSonetStatRxFEUASL": tnSonetStatRxFEUASL,
       "tnOptStatsTotalMembers": tnOptStatsTotalMembers,
       "tnOptStatsTable": tnOptStatsTable,
       "tnOptStatsEntry": tnOptStatsEntry,
       "tnOptStatsBin": tnOptStatsBin,
       "tnOptStatsBinStatus": tnOptStatsBinStatus,
       "tnOptStatsStartTime": tnOptStatsStartTime,
       "tnOptStatMinPower": tnOptStatMinPower,
       "tnOptStatMaxPower": tnOptStatMaxPower,
       "tnOptStatAveragePower": tnOptStatAveragePower,
       "tnOptStatMinPowerTr": tnOptStatMinPowerTr,
       "tnOptStatMaxPowerTr": tnOptStatMaxPowerTr,
       "tnOptStatMinPowerRtr": tnOptStatMinPowerRtr,
       "tnOptStatMaxPowerRtr": tnOptStatMaxPowerRtr,
       "tnOprStatsTotalMembers": tnOprStatsTotalMembers,
       "tnOprStatsTable": tnOprStatsTable,
       "tnOprStatsEntry": tnOprStatsEntry,
       "tnOprStatsBin": tnOprStatsBin,
       "tnOprStatsBinStatus": tnOprStatsBinStatus,
       "tnOprStatsStartTime": tnOprStatsStartTime,
       "tnOprStatMinPower": tnOprStatMinPower,
       "tnOprStatMaxPower": tnOprStatMaxPower,
       "tnOprStatAveragePower": tnOprStatAveragePower,
       "tnOprStatMinPowerTr": tnOprStatMinPowerTr,
       "tnOprStatMaxPowerTr": tnOprStatMaxPowerTr,
       "tnOprStatMinPowerRtr": tnOprStatMinPowerRtr,
       "tnOprStatMaxPowerRtr": tnOprStatMaxPowerRtr,
       "tnOpOutStatsTotalMembers": tnOpOutStatsTotalMembers,
       "tnOpOutStatsTable": tnOpOutStatsTable,
       "tnOpOutStatsEntry": tnOpOutStatsEntry,
       "tnOpOutStatsBin": tnOpOutStatsBin,
       "tnOpOutStatsBinStatus": tnOpOutStatsBinStatus,
       "tnOpOutStatsStartTime": tnOpOutStatsStartTime,
       "tnOpOutStatMinPower": tnOpOutStatMinPower,
       "tnOpOutStatMaxPower": tnOpOutStatMaxPower,
       "tnOpOutStatAveragePower": tnOpOutStatAveragePower,
       "tnOpInStatsTotalMembers": tnOpInStatsTotalMembers,
       "tnOpInStatsTable": tnOpInStatsTable,
       "tnOpInStatsEntry": tnOpInStatsEntry,
       "tnOpInStatsBin": tnOpInStatsBin,
       "tnOpInStatsBinStatus": tnOpInStatsBinStatus,
       "tnOpInStatsStartTime": tnOpInStatsStartTime,
       "tnOpInStatMinPower": tnOpInStatMinPower,
       "tnOpInStatMaxPower": tnOpInStatMaxPower,
       "tnOpInStatAveragePower": tnOpInStatAveragePower,
       "tnOpOchOutStatsTotalMembers": tnOpOchOutStatsTotalMembers,
       "tnOpOchOutStatsTable": tnOpOchOutStatsTable,
       "tnOpOchOutStatsEntry": tnOpOchOutStatsEntry,
       "tnOpOchOutStatsBin": tnOpOchOutStatsBin,
       "tnOpOchOutStatsBinStatus": tnOpOchOutStatsBinStatus,
       "tnOpOchOutStatsStartTime": tnOpOchOutStatsStartTime,
       "tnOpOchOutStatMinPower": tnOpOchOutStatMinPower,
       "tnOpOchOutStatMaxPower": tnOpOchOutStatMaxPower,
       "tnOpOchOutStatAveragePower": tnOpOchOutStatAveragePower,
       "tnOpOchInStatsTotalMembers": tnOpOchInStatsTotalMembers,
       "tnOpOchInStatsTable": tnOpOchInStatsTable,
       "tnOpOchInStatsEntry": tnOpOchInStatsEntry,
       "tnOpOchInStatsBin": tnOpOchInStatsBin,
       "tnOpOchInStatsBinStatus": tnOpOchInStatsBinStatus,
       "tnOpOchInStatsStartTime": tnOpOchInStatsStartTime,
       "tnOpOchInStatMinPower": tnOpOchInStatMinPower,
       "tnOpOchInStatMaxPower": tnOpOchInStatMaxPower,
       "tnOpOchInStatAveragePower": tnOpOchInStatAveragePower,
       "tnSdhStatsTotalMembers": tnSdhStatsTotalMembers,
       "tnSdhStatsTable": tnSdhStatsTable,
       "tnSdhStatsEntry": tnSdhStatsEntry,
       "tnSdhStatsBin": tnSdhStatsBin,
       "tnSdhStatsBinStatus": tnSdhStatsBinStatus,
       "tnSdhStatsStartTime": tnSdhStatsStartTime,
       "tnSdhStatRxRSEB": tnSdhStatRxRSEB,
       "tnSdhStatRxRSES": tnSdhStatRxRSES,
       "tnSdhStatRxRSSES": tnSdhStatRxRSSES,
       "tnSdhStatRxMSEB": tnSdhStatRxMSEB,
       "tnSdhStatRxMSES": tnSdhStatRxMSES,
       "tnSdhStatRxMSSES": tnSdhStatRxMSSES,
       "tnSdhStatRxMSUAS": tnSdhStatRxMSUAS,
       "tnSdhStatTxRSEB": tnSdhStatTxRSEB,
       "tnSdhStatTxRSES": tnSdhStatTxRSES,
       "tnSdhStatTxRSSES": tnSdhStatTxRSSES,
       "tnSdhStatTxMSEB": tnSdhStatTxMSEB,
       "tnSdhStatTxMSES": tnSdhStatTxMSES,
       "tnSdhStatTxMSSES": tnSdhStatTxMSSES,
       "tnSdhStatTxMSUAS": tnSdhStatTxMSUAS,
       "tnSdhStatRxRSUAS": tnSdhStatRxRSUAS,
       "tnSdhStatTxRSUAS": tnSdhStatTxRSUAS,
       "tnSdhStatRxMSFEEB": tnSdhStatRxMSFEEB,
       "tnSdhStatRxMSFEES": tnSdhStatRxMSFEES,
       "tnSdhStatRxMSFESES": tnSdhStatRxMSFESES,
       "tnSdhStatRxMSFEUAS": tnSdhStatRxMSFEUAS,
       "tnPhyCodeSublayerStatsTotalMembers": tnPhyCodeSublayerStatsTotalMembers,
       "tnPhyCodeSublayerStatsTable": tnPhyCodeSublayerStatsTable,
       "tnPhyCodeSublayerStatsEntry": tnPhyCodeSublayerStatsEntry,
       "tnPhyCodeSublayerStatsBin": tnPhyCodeSublayerStatsBin,
       "tnPhyCodeSublayerStatsBinStatus": tnPhyCodeSublayerStatsBinStatus,
       "tnPhyCodeSublayerStatsStartTime": tnPhyCodeSublayerStatsStartTime,
       "tnPhyCodeSublayerStatRxCV": tnPhyCodeSublayerStatRxCV,
       "tnPhyCodeSublayerStatRxES": tnPhyCodeSublayerStatRxES,
       "tnPhyCodeSublayerStatRxSES": tnPhyCodeSublayerStatRxSES,
       "tnPhyCodeSublayerStatRxSEFS": tnPhyCodeSublayerStatRxSEFS,
       "tnPhyCodeSublayerStatTxCV": tnPhyCodeSublayerStatTxCV,
       "tnPhyCodeSublayerStatTxES": tnPhyCodeSublayerStatTxES,
       "tnPhyCodeSublayerStatTxSES": tnPhyCodeSublayerStatTxSES,
       "tnPhyCodeSublayerStatTxSEFS": tnPhyCodeSublayerStatTxSEFS,
       "tnDigitalWrapper64BitStatsTotalMembers": tnDigitalWrapper64BitStatsTotalMembers,
       "tnDigitalWrapper64BitStatsTable": tnDigitalWrapper64BitStatsTable,
       "tnDigitalWrapper64BitStatsEntry": tnDigitalWrapper64BitStatsEntry,
       "tnDw64BitStatsBin": tnDw64BitStatsBin,
       "tnDw64BitStatsBinStatus": tnDw64BitStatsBinStatus,
       "tnDw64BitStatsStartTime": tnDw64BitStatsStartTime,
       "tnDw64BitStatRxRSCorrCnt": tnDw64BitStatRxRSCorrCnt,
       "tnDw64BitStatRxRSUncorrCnt": tnDw64BitStatRxRSUncorrCnt,
       "tnDw64BitStatRxSMBIP8ErrCnt": tnDw64BitStatRxSMBIP8ErrCnt,
       "tnDw64BitStatRxPMBIP8ErrCnt": tnDw64BitStatRxPMBIP8ErrCnt,
       "tnDw64BitStatRxSMES": tnDw64BitStatRxSMES,
       "tnDw64BitStatRxPMES": tnDw64BitStatRxPMES,
       "tnDw64BitStatRxSMSES": tnDw64BitStatRxSMSES,
       "tnDw64BitStatRxPMSES": tnDw64BitStatRxPMSES,
       "tnDw64BitStatRxSMUAS": tnDw64BitStatRxSMUAS,
       "tnDw64BitStatRxPMUAS": tnDw64BitStatRxPMUAS,
       "tnDw64BitStatRxBERPreFEC": tnDw64BitStatRxBERPreFEC,
       "tnDw64BitStatRxBERPostFEC": tnDw64BitStatRxBERPostFEC,
       "tnDw64BitStatRxSMFEBIP8ErrCnt": tnDw64BitStatRxSMFEBIP8ErrCnt,
       "tnDw64BitStatRxPMFEBIP8ErrCnt": tnDw64BitStatRxPMFEBIP8ErrCnt,
       "tnDw64BitStatRxSMBIAESErrCnt": tnDw64BitStatRxSMBIAESErrCnt,
       "tnDw64BitStatRxSMIAESErrCnt": tnDw64BitStatRxSMIAESErrCnt,
       "tnDw64BitStatRxSMFEES": tnDw64BitStatRxSMFEES,
       "tnDw64BitStatRxPMFEES": tnDw64BitStatRxPMFEES,
       "tnDw64BitStatRxSMFESES": tnDw64BitStatRxSMFESES,
       "tnDw64BitStatRxPMFESES": tnDw64BitStatRxPMFESES,
       "tnDw64BitStatRxSMFEUAS": tnDw64BitStatRxSMFEUAS,
       "tnDw64BitStatRxPMFEUAS": tnDw64BitStatRxPMFEUAS,
       "tnCdrStatsTotalMembers": tnCdrStatsTotalMembers,
       "tnCdrStatsTable": tnCdrStatsTable,
       "tnCdrStatsEntry": tnCdrStatsEntry,
       "tnCdrStatsBin": tnCdrStatsBin,
       "tnCdrStatsBinStatus": tnCdrStatsBinStatus,
       "tnCdrStatsStartTime": tnCdrStatsStartTime,
       "tnCdrStatMin": tnCdrStatMin,
       "tnCdrStatMax": tnCdrStatMax,
       "tnCdrStatAverage": tnCdrStatAverage,
       "tnDgdrStatsTotalMembers": tnDgdrStatsTotalMembers,
       "tnDgdrStatsTable": tnDgdrStatsTable,
       "tnDgdrStatsEntry": tnDgdrStatsEntry,
       "tnDgdrStatsBin": tnDgdrStatsBin,
       "tnDgdrStatsBinStatus": tnDgdrStatsBinStatus,
       "tnDgdrStatsStartTime": tnDgdrStatsStartTime,
       "tnDgdrStatMin": tnDgdrStatMin,
       "tnDgdrStatMax": tnDgdrStatMax,
       "tnDgdrStatAverage": tnDgdrStatAverage,
       "tnFoffrStatsTotalMembers": tnFoffrStatsTotalMembers,
       "tnFoffrStatsTable": tnFoffrStatsTable,
       "tnFoffrStatsEntry": tnFoffrStatsEntry,
       "tnFoffrStatsBin": tnFoffrStatsBin,
       "tnFoffrStatsBinStatus": tnFoffrStatsBinStatus,
       "tnFoffrStatsStartTime": tnFoffrStatsStartTime,
       "tnFoffrStatMin": tnFoffrStatMin,
       "tnFoffrStatMax": tnFoffrStatMax,
       "tnFoffrStatAverage": tnFoffrStatAverage,
       "tnE1StatsTotalMembers": tnE1StatsTotalMembers,
       "tnE1StatsTable": tnE1StatsTable,
       "tnE1StatsEntry": tnE1StatsEntry,
       "tnE1StatsBin": tnE1StatsBin,
       "tnE1StatsBinStatus": tnE1StatsBinStatus,
       "tnE1StatsStartTime": tnE1StatsStartTime,
       "tnE1StatRxBBEP": tnE1StatRxBBEP,
       "tnE1StatRxESP": tnE1StatRxESP,
       "tnE1StatRxSESP": tnE1StatRxSESP,
       "tnE1StatRxUASP": tnE1StatRxUASP,
       "tnE1StatRxESL": tnE1StatRxESL,
       "tnE1StatRxSESL": tnE1StatRxSESL,
       "tnE1StatTxBBEP": tnE1StatTxBBEP,
       "tnE1StatTxESP": tnE1StatTxESP,
       "tnE1StatTxSESP": tnE1StatTxSESP,
       "tnE1StatTxUASP": tnE1StatTxUASP,
       "tnE1StatRxBBEP15MinTr": tnE1StatRxBBEP15MinTr,
       "tnE1StatRxESP15MinTr": tnE1StatRxESP15MinTr,
       "tnE1StatRxSESP15MinTr": tnE1StatRxSESP15MinTr,
       "tnE1StatRxUASP15MinTr": tnE1StatRxUASP15MinTr,
       "tnE1StatRxESL15MinTr": tnE1StatRxESL15MinTr,
       "tnE1StatRxSESL15MinTr": tnE1StatRxSESL15MinTr,
       "tnE1StatTxBBEP15MinTr": tnE1StatTxBBEP15MinTr,
       "tnE1StatTxESP15MinTr": tnE1StatTxESP15MinTr,
       "tnE1StatTxSESP15MinTr": tnE1StatTxSESP15MinTr,
       "tnE1StatTxUASP15MinTr": tnE1StatTxUASP15MinTr,
       "tnE1StatRxBBEP1DayTr": tnE1StatRxBBEP1DayTr,
       "tnE1StatRxESP1DayTr": tnE1StatRxESP1DayTr,
       "tnE1StatRxSESP1DayTr": tnE1StatRxSESP1DayTr,
       "tnE1StatRxUASP1DayTr": tnE1StatRxUASP1DayTr,
       "tnE1StatRxESL1DayTr": tnE1StatRxESL1DayTr,
       "tnE1StatRxSESL1DayTr": tnE1StatRxSESL1DayTr,
       "tnE1StatTxBBEP1DayTr": tnE1StatTxBBEP1DayTr,
       "tnE1StatTxESP1DayTr": tnE1StatTxESP1DayTr,
       "tnE1StatTxSESP1DayTr": tnE1StatTxSESP1DayTr,
       "tnE1StatTxUASP1DayTr": tnE1StatTxUASP1DayTr,
       "tnE1StatRxBBEP15MinRtr": tnE1StatRxBBEP15MinRtr,
       "tnE1StatRxESP15MinRtr": tnE1StatRxESP15MinRtr,
       "tnE1StatRxSESP15MinRtr": tnE1StatRxSESP15MinRtr,
       "tnE1StatRxUASP15MinRtr": tnE1StatRxUASP15MinRtr,
       "tnE1StatRxESL15MinRtr": tnE1StatRxESL15MinRtr,
       "tnE1StatRxSESL15MinRtr": tnE1StatRxSESL15MinRtr,
       "tnE1StatTxBBEP15MinRtr": tnE1StatTxBBEP15MinRtr,
       "tnE1StatTxESP15MinRtr": tnE1StatTxESP15MinRtr,
       "tnE1StatTxSESP15MinRtr": tnE1StatTxSESP15MinRtr,
       "tnE1StatTxUASP15MinRtr": tnE1StatTxUASP15MinRtr,
       "tnPreFECBitsStatsTotalMembers": tnPreFECBitsStatsTotalMembers,
       "tnPreFECBitsStatsTable": tnPreFECBitsStatsTable,
       "tnPreFECBitsStatsEntry": tnPreFECBitsStatsEntry,
       "tnPreFECBitsStatsBin": tnPreFECBitsStatsBin,
       "tnPreFECBitsStatsBinStatus": tnPreFECBitsStatsBinStatus,
       "tnPreFECBitsStatsStartTime": tnPreFECBitsStatsStartTime,
       "tnPreFECBitsStatMin": tnPreFECBitsStatMin,
       "tnPreFECBitsStatMax": tnPreFECBitsStatMax,
       "tnPreFECBitsStatAverage": tnPreFECBitsStatAverage,
       "tnEncrypt64BitStatsTotalMembers": tnEncrypt64BitStatsTotalMembers,
       "tnEncrypt64BitStatsTable": tnEncrypt64BitStatsTable,
       "tnEncrypt64BitStatsEntry": tnEncrypt64BitStatsEntry,
       "tnEncrypt64BitStatsBin": tnEncrypt64BitStatsBin,
       "tnEncrypt64BitStatsBinStatus": tnEncrypt64BitStatsBinStatus,
       "tnEncrypt64BitStatsStartTime": tnEncrypt64BitStatsStartTime,
       "tnEncrypt64BitStatTx128BitBlkCnt": tnEncrypt64BitStatTx128BitBlkCnt,
       "tnEncrypt64BitStatRxFailToDecryptCnt": tnEncrypt64BitStatRxFailToDecryptCnt,
       "tnOthOdukStatsRxTotalMembers": tnOthOdukStatsRxTotalMembers,
       "tnOthOdukStatsRxTable": tnOthOdukStatsRxTable,
       "tnOthOdukStatsRxEntry": tnOthOdukStatsRxEntry,
       "tnOthOdukStatsBin": tnOthOdukStatsBin,
       "tnOthOdukStatsRxBinStatus": tnOthOdukStatsRxBinStatus,
       "tnOthOdukStatsRxStartTime": tnOthOdukStatsRxStartTime,
       "tnOthOdukStatsRxNeBIP8ErrCnt": tnOthOdukStatsRxNeBIP8ErrCnt,
       "tnOthOdukStatsRxNeES": tnOthOdukStatsRxNeES,
       "tnOthOdukStatsRxNeSES": tnOthOdukStatsRxNeSES,
       "tnOthOdukStatsRxNeUAS": tnOthOdukStatsRxNeUAS,
       "tnOthOdukStatsRxFeBIP8ErrCnt": tnOthOdukStatsRxFeBIP8ErrCnt,
       "tnOthOdukStatsRxFeES": tnOthOdukStatsRxFeES,
       "tnOthOdukStatsRxFeSES": tnOthOdukStatsRxFeSES,
       "tnOthOdukStatsRxFeUAS": tnOthOdukStatsRxFeUAS,
       "tnOthOdukStatsTxTotalMembers": tnOthOdukStatsTxTotalMembers,
       "tnOthOdukStatsTxTable": tnOthOdukStatsTxTable,
       "tnOthOdukStatsTxEntry": tnOthOdukStatsTxEntry,
       "tnOthOdukStatsTxBinStatus": tnOthOdukStatsTxBinStatus,
       "tnOthOdukStatsTxStartTime": tnOthOdukStatsTxStartTime,
       "tnOthOdukStatsTxNeBIP8ErrCnt": tnOthOdukStatsTxNeBIP8ErrCnt,
       "tnOthOdukStatsTxNeES": tnOthOdukStatsTxNeES,
       "tnOthOdukStatsTxNeSES": tnOthOdukStatsTxNeSES,
       "tnOthOdukStatsTxNeUAS": tnOthOdukStatsTxNeUAS,
       "tnOthOdukStatsTxFeBIP8ErrCnt": tnOthOdukStatsTxFeBIP8ErrCnt,
       "tnOthOdukStatsTxFeES": tnOthOdukStatsTxFeES,
       "tnOthOdukStatsTxFeSES": tnOthOdukStatsTxFeSES,
       "tnOthOdukStatsTxFeUAS": tnOthOdukStatsTxFeUAS,
       "tnOthOtukStatsTotalMembers": tnOthOtukStatsTotalMembers,
       "tnOthOtukStatsTable": tnOthOtukStatsTable,
       "tnOthOtukStatsEntry": tnOthOtukStatsEntry,
       "tnOthOtukStatsBin": tnOthOtukStatsBin,
       "tnOthOtukStatsBinStatus": tnOthOtukStatsBinStatus,
       "tnOthOtukStatsStartTime": tnOthOtukStatsStartTime,
       "tnOthOtukStatRxRsCorrCnt": tnOthOtukStatRxRsCorrCnt,
       "tnOthOtukStatRxRsUncorrCnt": tnOthOtukStatRxRsUncorrCnt,
       "tnOthOtukStatRxBERPreFEC": tnOthOtukStatRxBERPreFEC,
       "tnOthOtukStatRxBERPostFEC": tnOthOtukStatRxBERPostFEC,
       "tnOthOtukStatNeRxSMBIP8ErrCnt": tnOthOtukStatNeRxSMBIP8ErrCnt,
       "tnOthOtukStatNeRxBIAESErrCnt": tnOthOtukStatNeRxBIAESErrCnt,
       "tnOthOtukStatNeRxSMES": tnOthOtukStatNeRxSMES,
       "tnOthOtukStatNeRxSMSES": tnOthOtukStatNeRxSMSES,
       "tnOthOtukStatNeRxSMUAS": tnOthOtukStatNeRxSMUAS,
       "tnOthOtukStatNeRxIAES": tnOthOtukStatNeRxIAES,
       "tnOthOtukStatFeRxSMBIP8ErrCnt": tnOthOtukStatFeRxSMBIP8ErrCnt,
       "tnOthOtukStatFeRxSMES": tnOthOtukStatFeRxSMES,
       "tnOthOtukStatFeRxSMSES": tnOthOtukStatFeRxSMSES,
       "tnOthOtukStatFeRxSMUAS": tnOthOtukStatFeRxSMUAS,
       "tnOthOtukStatFeRxIAES": tnOthOtukStatFeRxIAES,
       "tnOsnrStatsTotalMembers": tnOsnrStatsTotalMembers,
       "tnOsnrStatsTable": tnOsnrStatsTable,
       "tnOsnrStatsEntry": tnOsnrStatsEntry,
       "tnOsnrStatsBin": tnOsnrStatsBin,
       "tnOsnrStatsBinStatus": tnOsnrStatsBinStatus,
       "tnOsnrStatsStartTime": tnOsnrStatsStartTime,
       "tnOsnrStatMinOSNR": tnOsnrStatMinOSNR,
       "tnOsnrStatMaxOSNR": tnOsnrStatMaxOSNR,
       "tnOsnrStatAverageOSNR": tnOsnrStatAverageOSNR,
       "tnOsnrStatStatusOSNR": tnOsnrStatStatusOSNR,
       "tnOthOdukStatsDMTotalMembers": tnOthOdukStatsDMTotalMembers,
       "tnOthOdukStatsDMTable": tnOthOdukStatsDMTable,
       "tnOthOdukStatsDMEntry": tnOthOdukStatsDMEntry,
       "tnOthOdukStatsDMBinStatus": tnOthOdukStatsDMBinStatus,
       "tnOthOdukStatsDMStartTime": tnOthOdukStatsDMStartTime,
       "tnOthOdukStatsDMMinDm": tnOthOdukStatsDMMinDm,
       "tnOthOdukStatsDMMaxDm": tnOthOdukStatsDMMaxDm,
       "tnOthOdukStatsDMAverageDm": tnOthOdukStatsDMAverageDm,
       "tnOthOdukStatsTcmTotalMembers": tnOthOdukStatsTcmTotalMembers,
       "tnOthOdukStatsTcmTable": tnOthOdukStatsTcmTable,
       "tnOthOdukStatsTcmEntry": tnOthOdukStatsTcmEntry,
       "tnOthOdukStatsTcmBin": tnOthOdukStatsTcmBin,
       "tnOthOdukStatsTcmBinStatus": tnOthOdukStatsTcmBinStatus,
       "tnOthOdukStatsTcmStartTime": tnOthOdukStatsTcmStartTime,
       "tnOthOdukStatsTcmNeRxBIP8ErrCnt": tnOthOdukStatsTcmNeRxBIP8ErrCnt,
       "tnOthOdukStatsTcmNeRxIAESErrCnt": tnOthOdukStatsTcmNeRxIAESErrCnt,
       "tnOthOdukStatsTcmNeRxES": tnOthOdukStatsTcmNeRxES,
       "tnOthOdukStatsTcmNeRxSES": tnOthOdukStatsTcmNeRxSES,
       "tnOthOdukStatsTcmNeRxUAS": tnOthOdukStatsTcmNeRxUAS,
       "tnOthOdukStatsTcmFeRxBIP8ErrCnt": tnOthOdukStatsTcmFeRxBIP8ErrCnt,
       "tnOthOdukStatsTcmFeRxBIAESErrCnt": tnOthOdukStatsTcmFeRxBIAESErrCnt,
       "tnOthOdukStatsTcmFeRxES": tnOthOdukStatsTcmFeRxES,
       "tnOthOdukStatsTcmFeRxSES": tnOthOdukStatsTcmFeRxSES,
       "tnOthOdukStatsTcmFeRxUAS": tnOthOdukStatsTcmFeRxUAS,
       "tnStatisticsRawCounts": tnStatisticsRawCounts,
       "tnControlNetworkLinkRawCountStatsTotalMembers": tnControlNetworkLinkRawCountStatsTotalMembers,
       "tnControlNetworkLinkRawCountStatsTable": tnControlNetworkLinkRawCountStatsTable,
       "tnControlNetworkLinkRawCountStatsEntry": tnControlNetworkLinkRawCountStatsEntry,
       "tnCNLinkRawCountStatIpInReceives": tnCNLinkRawCountStatIpInReceives,
       "tnCNLinkRawCountStatIpInDiscards": tnCNLinkRawCountStatIpInDiscards,
       "tnCNLinkRawCountStatIpOutRequests": tnCNLinkRawCountStatIpOutRequests,
       "tnCNLinkRawCountStatIpOutDiscards": tnCNLinkRawCountStatIpOutDiscards,
       "tnCNLinkRawCountStatIpForwDatagrams": tnCNLinkRawCountStatIpForwDatagrams,
       "tnCardRawCountStatsTotalMembers": tnCardRawCountStatsTotalMembers,
       "tnCardRawCountStatsTable": tnCardRawCountStatsTable,
       "tnCardRawCountStatsEntry": tnCardRawCountStatsEntry,
       "tnCardRawCountStatsClear": tnCardRawCountStatsClear,
       "tnCardRawCountStatCpuAverage": tnCardRawCountStatCpuAverage,
       "tnCardRawCountStatHeapUsage": tnCardRawCountStatHeapUsage,
       "tnCardRawCountStatPoolUsage": tnCardRawCountStatPoolUsage,
       "tnCardRawCountStatStartTime": tnCardRawCountStatStartTime,
       "tnInterfaceRawCountStatsTotalMembers": tnInterfaceRawCountStatsTotalMembers,
       "tnInterfaceRawCountStatsTable": tnInterfaceRawCountStatsTable,
       "tnInterfaceRawCountStatsEntry": tnInterfaceRawCountStatsEntry,
       "tnIfRawCountStatsClear": tnIfRawCountStatsClear,
       "tnIfRawCountStatInOctets": tnIfRawCountStatInOctets,
       "tnIfRawCountStatInUcastPkts": tnIfRawCountStatInUcastPkts,
       "tnIfRawCountStatInDiscards": tnIfRawCountStatInDiscards,
       "tnIfRawCountStatInErrors": tnIfRawCountStatInErrors,
       "tnIfRawCountStatInUnknownProtos": tnIfRawCountStatInUnknownProtos,
       "tnIfRawCountStatOutOctets": tnIfRawCountStatOutOctets,
       "tnIfRawCountStatOutUcastPkts": tnIfRawCountStatOutUcastPkts,
       "tnIfRawCountStatOutDiscards": tnIfRawCountStatOutDiscards,
       "tnIfRawCountStatOutErrors": tnIfRawCountStatOutErrors,
       "tnIfRawCountStatInMulticastPkts": tnIfRawCountStatInMulticastPkts,
       "tnIfRawCountStatInBroadcastPkts": tnIfRawCountStatInBroadcastPkts,
       "tnIfRawCountStatOutMulticastPkts": tnIfRawCountStatOutMulticastPkts,
       "tnIfRawCountStatOutBroadcastPkts": tnIfRawCountStatOutBroadcastPkts,
       "tnIfRawCountStatInPacketsNotClassified": tnIfRawCountStatInPacketsNotClassified,
       "tnIfRawCountStatStartTime": tnIfRawCountStatStartTime,
       "tnEtherRawCountStatsTotalMembers": tnEtherRawCountStatsTotalMembers,
       "tnEtherRawCountStatsTable": tnEtherRawCountStatsTable,
       "tnEtherRawCountStatsEntry": tnEtherRawCountStatsEntry,
       "tnEtherRawCountStatsClear": tnEtherRawCountStatsClear,
       "tnEtherRawCountStatRxDropEvents": tnEtherRawCountStatRxDropEvents,
       "tnEtherRawCountStatRxFragments": tnEtherRawCountStatRxFragments,
       "tnEtherRawCountStatRxJabbers": tnEtherRawCountStatRxJabbers,
       "tnEtherRawCountStatRxMcastPkts": tnEtherRawCountStatRxMcastPkts,
       "tnEtherRawCountStatRxOctets": tnEtherRawCountStatRxOctets,
       "tnEtherRawCountStatRxOversizedPkts": tnEtherRawCountStatRxOversizedPkts,
       "tnEtherRawCountStatRxPkts": tnEtherRawCountStatRxPkts,
       "tnEtherRawCountStatRxPktsSize1024to1518": tnEtherRawCountStatRxPktsSize1024to1518,
       "tnEtherRawCountStatRxPktsSize128to255": tnEtherRawCountStatRxPktsSize128to255,
       "tnEtherRawCountStatRxPktsSize256to511": tnEtherRawCountStatRxPktsSize256to511,
       "tnEtherRawCountStatRxPktsSize512to1023": tnEtherRawCountStatRxPktsSize512to1023,
       "tnEtherRawCountStatRxPktsSize65to127": tnEtherRawCountStatRxPktsSize65to127,
       "tnEtherRawCountStatRxUndersizedPkts": tnEtherRawCountStatRxUndersizedPkts,
       "tnEtherRawCountStatTxBcastPkts": tnEtherRawCountStatTxBcastPkts,
       "tnEtherRawCountStatTxCrcAlignErrs": tnEtherRawCountStatTxCrcAlignErrs,
       "tnEtherRawCountStatTxDropEvents": tnEtherRawCountStatTxDropEvents,
       "tnEtherRawCountStatTxFragments": tnEtherRawCountStatTxFragments,
       "tnEtherRawCountStatTxJabbers": tnEtherRawCountStatTxJabbers,
       "tnEtherRawCountStatTxMcastPkts": tnEtherRawCountStatTxMcastPkts,
       "tnEtherRawCountStatTxOctets": tnEtherRawCountStatTxOctets,
       "tnEtherRawCountStatTxOversizedPkts": tnEtherRawCountStatTxOversizedPkts,
       "tnEtherRawCountStatTxPkts": tnEtherRawCountStatTxPkts,
       "tnEtherRawCountStatTxPktsSize1024to1518": tnEtherRawCountStatTxPktsSize1024to1518,
       "tnEtherRawCountStatTxPktsSize128to255": tnEtherRawCountStatTxPktsSize128to255,
       "tnEtherRawCountStatTxPktsSize256to511": tnEtherRawCountStatTxPktsSize256to511,
       "tnEtherRawCountStatTxPktsSize512to1023": tnEtherRawCountStatTxPktsSize512to1023,
       "tnEtherRawCountStatTxPktsSize65to127": tnEtherRawCountStatTxPktsSize65to127,
       "tnEtherRawCountStatTxUndersizedPkts": tnEtherRawCountStatTxUndersizedPkts,
       "tnEtherRawCountStatRxBcastPkts": tnEtherRawCountStatRxBcastPkts,
       "tnEtherRawCountStatRxCrcAlignErrs": tnEtherRawCountStatRxCrcAlignErrs,
       "tnEtherRawCountStatRxCollisions": tnEtherRawCountStatRxCollisions,
       "tnEtherRawCountStatRxJumboPkts": tnEtherRawCountStatRxJumboPkts,
       "tnEtherRawCountStatTxCollisions": tnEtherRawCountStatTxCollisions,
       "tnEtherRawCountStatTxJumboPkts": tnEtherRawCountStatTxJumboPkts,
       "tnEtherRawCountStatRmonIndex": tnEtherRawCountStatRmonIndex,
       "tnEtherRawCountStatRxPktsSize64": tnEtherRawCountStatRxPktsSize64,
       "tnEtherRawCountStatTxPktsSize64": tnEtherRawCountStatTxPktsSize64,
       "tnEtherRawCountStatRxPktErrRatio": tnEtherRawCountStatRxPktErrRatio,
       "tnEtherRawCountStatTxPktErrRatio": tnEtherRawCountStatTxPktErrRatio,
       "tnEtherRawCountStatStartTime": tnEtherRawCountStatStartTime,
       "tnSonetRawCountStatsTotalMembers": tnSonetRawCountStatsTotalMembers,
       "tnSonetRawCountStatsTable": tnSonetRawCountStatsTable,
       "tnSonetRawCountStatsEntry": tnSonetRawCountStatsEntry,
       "tnSonetRawCountStatsClear": tnSonetRawCountStatsClear,
       "tnSonetRawCountStatRxCVS": tnSonetRawCountStatRxCVS,
       "tnSonetRawCountStatRxESS": tnSonetRawCountStatRxESS,
       "tnSonetRawCountStatRxSESS": tnSonetRawCountStatRxSESS,
       "tnSonetRawCountStatRxSEFSS": tnSonetRawCountStatRxSEFSS,
       "tnSonetRawCountStatRxCVL": tnSonetRawCountStatRxCVL,
       "tnSonetRawCountStatRxESL": tnSonetRawCountStatRxESL,
       "tnSonetRawCountStatRxSESL": tnSonetRawCountStatRxSESL,
       "tnSonetRawCountStatRxUASL": tnSonetRawCountStatRxUASL,
       "tnSonetRawCountStatRxFCL": tnSonetRawCountStatRxFCL,
       "tnSonetRawCountStatTxCVS": tnSonetRawCountStatTxCVS,
       "tnSonetRawCountStatTxESS": tnSonetRawCountStatTxESS,
       "tnSonetRawCountStatTxSESS": tnSonetRawCountStatTxSESS,
       "tnSonetRawCountStatTxSEFSS": tnSonetRawCountStatTxSEFSS,
       "tnSonetRawCountStatTxCVL": tnSonetRawCountStatTxCVL,
       "tnSonetRawCountStatTxESL": tnSonetRawCountStatTxESL,
       "tnSonetRawCountStatTxSESL": tnSonetRawCountStatTxSESL,
       "tnSonetRawCountStatTxUASL": tnSonetRawCountStatTxUASL,
       "tnSonetRawCountStatTxFCL": tnSonetRawCountStatTxFCL,
       "tnSonetRawCountStatRxUASS": tnSonetRawCountStatRxUASS,
       "tnSonetRawCountStatTxUASS": tnSonetRawCountStatTxUASS,
       "tnSonetRawCountStatStartTime": tnSonetRawCountStatStartTime,
       "tnSonetRawCountStatRxFECVL": tnSonetRawCountStatRxFECVL,
       "tnSonetRawCountStatRxFEESL": tnSonetRawCountStatRxFEESL,
       "tnSonetRawCountStatRxFESESL": tnSonetRawCountStatRxFESESL,
       "tnSonetRawCountStatRxFEUASL": tnSonetRawCountStatRxFEUASL,
       "tnOptRawCountStatsTotalMembers": tnOptRawCountStatsTotalMembers,
       "tnOptRawCountStatsTable": tnOptRawCountStatsTable,
       "tnOptRawCountStatsEntry": tnOptRawCountStatsEntry,
       "tnOptRawCountStatsClear": tnOptRawCountStatsClear,
       "tnOptRawCountStatMinPower": tnOptRawCountStatMinPower,
       "tnOptRawCountStatMaxPower": tnOptRawCountStatMaxPower,
       "tnOptRawCountStatAveragePower": tnOptRawCountStatAveragePower,
       "tnOptRawCountStatStartTime": tnOptRawCountStatStartTime,
       "tnOprRawCountStatsTotalMembers": tnOprRawCountStatsTotalMembers,
       "tnOprRawCountStatsTable": tnOprRawCountStatsTable,
       "tnOprRawCountStatsEntry": tnOprRawCountStatsEntry,
       "tnOprRawCountStatsClear": tnOprRawCountStatsClear,
       "tnOprRawCountStatMinPower": tnOprRawCountStatMinPower,
       "tnOprRawCountStatMaxPower": tnOprRawCountStatMaxPower,
       "tnOprRawCountStatAveragePower": tnOprRawCountStatAveragePower,
       "tnOprRawCountStatStartTime": tnOprRawCountStatStartTime,
       "tnOpOutRawCountStatsTotalMembers": tnOpOutRawCountStatsTotalMembers,
       "tnOpOutRawCountStatsTable": tnOpOutRawCountStatsTable,
       "tnOpOutRawCountStatsEntry": tnOpOutRawCountStatsEntry,
       "tnOpOutRawCountStatsClear": tnOpOutRawCountStatsClear,
       "tnOpOutRawCountStatMinPower": tnOpOutRawCountStatMinPower,
       "tnOpOutRawCountStatMaxPower": tnOpOutRawCountStatMaxPower,
       "tnOpOutRawCountStatAveragePower": tnOpOutRawCountStatAveragePower,
       "tnOpOutRawCountStatStartTime": tnOpOutRawCountStatStartTime,
       "tnOpInRawCountStatsTotalMembers": tnOpInRawCountStatsTotalMembers,
       "tnOpInRawCountStatsTable": tnOpInRawCountStatsTable,
       "tnOpInRawCountStatsEntry": tnOpInRawCountStatsEntry,
       "tnOpInRawCountStatsClear": tnOpInRawCountStatsClear,
       "tnOpInRawCountStatMinPower": tnOpInRawCountStatMinPower,
       "tnOpInRawCountStatMaxPower": tnOpInRawCountStatMaxPower,
       "tnOpInRawCountStatAveragePower": tnOpInRawCountStatAveragePower,
       "tnOpInRawCountStatStartTime": tnOpInRawCountStatStartTime,
       "tnOpOchOutRawCountStatsTotalMembers": tnOpOchOutRawCountStatsTotalMembers,
       "tnOpOchOutRawCountStatsTable": tnOpOchOutRawCountStatsTable,
       "tnOpOchOutRawCountStatsEntry": tnOpOchOutRawCountStatsEntry,
       "tnOpOchOutRawCountStatsClear": tnOpOchOutRawCountStatsClear,
       "tnOpOchOutRawCountStatMinPower": tnOpOchOutRawCountStatMinPower,
       "tnOpOchOutRawCountStatMaxPower": tnOpOchOutRawCountStatMaxPower,
       "tnOpOchOutRawCountStatAveragePower": tnOpOchOutRawCountStatAveragePower,
       "tnOpOchOutRawCountStatStartTime": tnOpOchOutRawCountStatStartTime,
       "tnOpOchInRawCountStatsTotalMembers": tnOpOchInRawCountStatsTotalMembers,
       "tnOpOchInRawCountStatsTable": tnOpOchInRawCountStatsTable,
       "tnOpOchInRawCountStatsEntry": tnOpOchInRawCountStatsEntry,
       "tnOpOchInRawCountStatsClear": tnOpOchInRawCountStatsClear,
       "tnOpOchInRawCountStatMinPower": tnOpOchInRawCountStatMinPower,
       "tnOpOchInRawCountStatMaxPower": tnOpOchInRawCountStatMaxPower,
       "tnOpOchInRawCountStatAveragePower": tnOpOchInRawCountStatAveragePower,
       "tnOpOchInRawCountStatStartTime": tnOpOchInRawCountStatStartTime,
       "tnSdhRawCountStatsTotalMembers": tnSdhRawCountStatsTotalMembers,
       "tnSdhRawCountStatsTable": tnSdhRawCountStatsTable,
       "tnSdhRawCountStatsEntry": tnSdhRawCountStatsEntry,
       "tnSdhRawCountStatsClear": tnSdhRawCountStatsClear,
       "tnSdhRawCountStatRxRSEB": tnSdhRawCountStatRxRSEB,
       "tnSdhRawCountStatRxRSES": tnSdhRawCountStatRxRSES,
       "tnSdhRawCountStatRxRSSES": tnSdhRawCountStatRxRSSES,
       "tnSdhRawCountStatRxMSEB": tnSdhRawCountStatRxMSEB,
       "tnSdhRawCountStatRxMSES": tnSdhRawCountStatRxMSES,
       "tnSdhRawCountStatRxMSSES": tnSdhRawCountStatRxMSSES,
       "tnSdhRawCountStatRxMSUAS": tnSdhRawCountStatRxMSUAS,
       "tnSdhRawCountStatTxRSEB": tnSdhRawCountStatTxRSEB,
       "tnSdhRawCountStatTxRSES": tnSdhRawCountStatTxRSES,
       "tnSdhRawCountStatTxRSSES": tnSdhRawCountStatTxRSSES,
       "tnSdhRawCountStatTxMSEB": tnSdhRawCountStatTxMSEB,
       "tnSdhRawCountStatTxMSES": tnSdhRawCountStatTxMSES,
       "tnSdhRawCountStatTxMSSES": tnSdhRawCountStatTxMSSES,
       "tnSdhRawCountStatTxMSUAS": tnSdhRawCountStatTxMSUAS,
       "tnSdhRawCountStatRxRSUAS": tnSdhRawCountStatRxRSUAS,
       "tnSdhRawCountStatTxRSUAS": tnSdhRawCountStatTxRSUAS,
       "tnSdhRawCountStatStartTime": tnSdhRawCountStatStartTime,
       "tnSdhRawCountStatRxMSFEEB": tnSdhRawCountStatRxMSFEEB,
       "tnSdhRawCountStatRxMSFEES": tnSdhRawCountStatRxMSFEES,
       "tnSdhRawCountStatRxMSFESES": tnSdhRawCountStatRxMSFESES,
       "tnSdhRawCountStatRxMSFEUAS": tnSdhRawCountStatRxMSFEUAS,
       "tnPhyCodeSublayerRawCountStatsTotalMembers": tnPhyCodeSublayerRawCountStatsTotalMembers,
       "tnPhyCodeSublayerRawCountStatsTable": tnPhyCodeSublayerRawCountStatsTable,
       "tnPhyCodeSublayerRawCountStatsEntry": tnPhyCodeSublayerRawCountStatsEntry,
       "tnPhyCodeSublayerRawCountStatsClear": tnPhyCodeSublayerRawCountStatsClear,
       "tnPhyCodeSublayerRawCountStatRxCV": tnPhyCodeSublayerRawCountStatRxCV,
       "tnPhyCodeSublayerRawCountStatRxES": tnPhyCodeSublayerRawCountStatRxES,
       "tnPhyCodeSublayerRawCountStatRxSES": tnPhyCodeSublayerRawCountStatRxSES,
       "tnPhyCodeSublayerRawCountStatRxSEFS": tnPhyCodeSublayerRawCountStatRxSEFS,
       "tnPhyCodeSublayerRawCountStatTxCV": tnPhyCodeSublayerRawCountStatTxCV,
       "tnPhyCodeSublayerRawCountStatTxES": tnPhyCodeSublayerRawCountStatTxES,
       "tnPhyCodeSublayerRawCountStatTxSES": tnPhyCodeSublayerRawCountStatTxSES,
       "tnPhyCodeSublayerRawCountStatTxSEFS": tnPhyCodeSublayerRawCountStatTxSEFS,
       "tnPhyCodeSublayerRawCountStatStartTime": tnPhyCodeSublayerRawCountStatStartTime,
       "tnDigitalWrapper64BitRawCountStatsTotalMembers": tnDigitalWrapper64BitRawCountStatsTotalMembers,
       "tnDigitalWrapper64BitRawCountStatsTable": tnDigitalWrapper64BitRawCountStatsTable,
       "tnDigitalWrapper64BitRawCountStatsEntry": tnDigitalWrapper64BitRawCountStatsEntry,
       "tnDw64BitRawCountStatsClear": tnDw64BitRawCountStatsClear,
       "tnDw64BitRawCountStatRxRSCorrCnt": tnDw64BitRawCountStatRxRSCorrCnt,
       "tnDw64BitRawCountStatRxRSUncorrCnt": tnDw64BitRawCountStatRxRSUncorrCnt,
       "tnDw64BitRawCountStatRxSMBIP8ErrCnt": tnDw64BitRawCountStatRxSMBIP8ErrCnt,
       "tnDw64BitRawCountStatRxPMBIP8ErrCnt": tnDw64BitRawCountStatRxPMBIP8ErrCnt,
       "tnDw64BitRawCountStatRxSMBEIErrCnt": tnDw64BitRawCountStatRxSMBEIErrCnt,
       "tnDw64BitRawCountStatRxPMBEIErrCnt": tnDw64BitRawCountStatRxPMBEIErrCnt,
       "tnDw64BitRawCountStatRxRSSES": tnDw64BitRawCountStatRxRSSES,
       "tnDw64BitRawCountStatRxSMES": tnDw64BitRawCountStatRxSMES,
       "tnDw64BitRawCountStatRxPMES": tnDw64BitRawCountStatRxPMES,
       "tnDw64BitRawCountStatRxSMSES": tnDw64BitRawCountStatRxSMSES,
       "tnDw64BitRawCountStatRxPMSES": tnDw64BitRawCountStatRxPMSES,
       "tnDw64BitRawCountStatRxSMUAS": tnDw64BitRawCountStatRxSMUAS,
       "tnDw64BitRawCountStatRxPMUAS": tnDw64BitRawCountStatRxPMUAS,
       "tnDw64BitRawCountStatStartTime": tnDw64BitRawCountStatStartTime,
       "tnDw64BitRawCountStatRxBERPreFEC": tnDw64BitRawCountStatRxBERPreFEC,
       "tnDw64BitRawCountStatRxBERPostFEC": tnDw64BitRawCountStatRxBERPostFEC,
       "tnDw64BitRawCountStatRxSMFEBIP8ErrCnt": tnDw64BitRawCountStatRxSMFEBIP8ErrCnt,
       "tnDw64BitRawCountStatRxPMFEBIP8ErrCnt": tnDw64BitRawCountStatRxPMFEBIP8ErrCnt,
       "tnDw64BitRawCountStatRxSMBIAESErrCnt": tnDw64BitRawCountStatRxSMBIAESErrCnt,
       "tnDw64BitRawCountStatRxSMIAESErrCnt": tnDw64BitRawCountStatRxSMIAESErrCnt,
       "tnDw64BitRawCountStatRxSMFEES": tnDw64BitRawCountStatRxSMFEES,
       "tnDw64BitRawCountStatRxPMFEES": tnDw64BitRawCountStatRxPMFEES,
       "tnDw64BitRawCountStatRxSMFESES": tnDw64BitRawCountStatRxSMFESES,
       "tnDw64BitRawCountStatRxPMFESES": tnDw64BitRawCountStatRxPMFESES,
       "tnDw64BitRawCountStatRxSMFEUAS": tnDw64BitRawCountStatRxSMFEUAS,
       "tnDw64BitRawCountStatRxPMFEUAS": tnDw64BitRawCountStatRxPMFEUAS,
       "tnCdrRawCountStatsTotalMembers": tnCdrRawCountStatsTotalMembers,
       "tnCdrRawCountStatsTable": tnCdrRawCountStatsTable,
       "tnCdrRawCountStatsEntry": tnCdrRawCountStatsEntry,
       "tnCdrRawCountStatsClear": tnCdrRawCountStatsClear,
       "tnCdrRawCountStatMin": tnCdrRawCountStatMin,
       "tnCdrRawCountStatMax": tnCdrRawCountStatMax,
       "tnCdrRawCountStatAverage": tnCdrRawCountStatAverage,
       "tnCdrRawCountStatStartTime": tnCdrRawCountStatStartTime,
       "tnDgdrRawCountStatsTotalMembers": tnDgdrRawCountStatsTotalMembers,
       "tnDgdrRawCountStatsTable": tnDgdrRawCountStatsTable,
       "tnDgdrRawCountStatsEntry": tnDgdrRawCountStatsEntry,
       "tnDgdrRawCountStatsClear": tnDgdrRawCountStatsClear,
       "tnDgdrRawCountStatMin": tnDgdrRawCountStatMin,
       "tnDgdrRawCountStatMax": tnDgdrRawCountStatMax,
       "tnDgdrRawCountStatAverage": tnDgdrRawCountStatAverage,
       "tnDgdrRawCountStatStartTime": tnDgdrRawCountStatStartTime,
       "tnFoffrRawCountStatsTotalMembers": tnFoffrRawCountStatsTotalMembers,
       "tnFoffrRawCountStatsTable": tnFoffrRawCountStatsTable,
       "tnFoffrRawCountStatsEntry": tnFoffrRawCountStatsEntry,
       "tnFoffrRawCountStatsClear": tnFoffrRawCountStatsClear,
       "tnFoffrRawCountStatMin": tnFoffrRawCountStatMin,
       "tnFoffrRawCountStatMax": tnFoffrRawCountStatMax,
       "tnFoffrRawCountStatAverage": tnFoffrRawCountStatAverage,
       "tnFoffrRawCountStatStartTime": tnFoffrRawCountStatStartTime,
       "tnE1RawCountStatsTotalMembers": tnE1RawCountStatsTotalMembers,
       "tnE1RawCountStatsTable": tnE1RawCountStatsTable,
       "tnE1RawCountStatsEntry": tnE1RawCountStatsEntry,
       "tnE1RawCountStatsClear": tnE1RawCountStatsClear,
       "tnE1RawCountStatRxBBEP": tnE1RawCountStatRxBBEP,
       "tnE1RawCountStatRxESP": tnE1RawCountStatRxESP,
       "tnE1RawCountStatRxSESP": tnE1RawCountStatRxSESP,
       "tnE1RawCountStatRxUASP": tnE1RawCountStatRxUASP,
       "tnE1RawCountStatRxESL": tnE1RawCountStatRxESL,
       "tnE1RawCountStatRxSESL": tnE1RawCountStatRxSESL,
       "tnE1RawCountStatTxBBEP": tnE1RawCountStatTxBBEP,
       "tnE1RawCountStatTxESP": tnE1RawCountStatTxESP,
       "tnE1RawCountStatTxSESP": tnE1RawCountStatTxSESP,
       "tnE1RawCountStatTxUASP": tnE1RawCountStatTxUASP,
       "tnE1RawCountStatStartTime": tnE1RawCountStatStartTime,
       "tnPreFECBitsRawCountStatsTotalMembers": tnPreFECBitsRawCountStatsTotalMembers,
       "tnPreFECBitsRawCountStatsTable": tnPreFECBitsRawCountStatsTable,
       "tnPreFECBitsRawCountStatsEntry": tnPreFECBitsRawCountStatsEntry,
       "tnPreFECBitsRawCountStatsClear": tnPreFECBitsRawCountStatsClear,
       "tnPreFECBitsRawCountStatMin": tnPreFECBitsRawCountStatMin,
       "tnPreFECBitsRawCountStatMax": tnPreFECBitsRawCountStatMax,
       "tnPreFECBitsRawCountStatAverage": tnPreFECBitsRawCountStatAverage,
       "tnPreFECBitsRawCountStatStartTime": tnPreFECBitsRawCountStatStartTime,
       "tnEncrypt64BitRawCountStatsTotalMembers": tnEncrypt64BitRawCountStatsTotalMembers,
       "tnEncrypt64BitRawCountStatsTable": tnEncrypt64BitRawCountStatsTable,
       "tnEncrypt64BitRawCountStatsEntry": tnEncrypt64BitRawCountStatsEntry,
       "tnEncrypt64BitRawCountStatsClear": tnEncrypt64BitRawCountStatsClear,
       "tnEncrypt64BitRawCountStatStartTime": tnEncrypt64BitRawCountStatStartTime,
       "tnEncrypt64BitRawCountStatTx128BitBlkCnt": tnEncrypt64BitRawCountStatTx128BitBlkCnt,
       "tnEncrypt64BitRawCountStatRxFailToDecryptCnt": tnEncrypt64BitRawCountStatRxFailToDecryptCnt,
       "tnOthOdukRawCountStatsRxTotalMembers": tnOthOdukRawCountStatsRxTotalMembers,
       "tnOthOdukRawCountStatsRxTable": tnOthOdukRawCountStatsRxTable,
       "tnOthOdukRawCountStatsRxEntry": tnOthOdukRawCountStatsRxEntry,
       "tnOthOdukRawCountStatsRxClear": tnOthOdukRawCountStatsRxClear,
       "tnOthOdukRawCountStatsRxStartTime": tnOthOdukRawCountStatsRxStartTime,
       "tnOthOdukRawCountStatRxNeBIP8ErrCnt": tnOthOdukRawCountStatRxNeBIP8ErrCnt,
       "tnOthOdukRawCountStatRxNeES": tnOthOdukRawCountStatRxNeES,
       "tnOthOdukRawCountStatRxNeSES": tnOthOdukRawCountStatRxNeSES,
       "tnOthOdukRawCountStatRxNeUAS": tnOthOdukRawCountStatRxNeUAS,
       "tnOthOdukRawCountStatRxFeBIP8ErrCnt": tnOthOdukRawCountStatRxFeBIP8ErrCnt,
       "tnOthOdukRawCountStatRxFeES": tnOthOdukRawCountStatRxFeES,
       "tnOthOdukRawCountStatRxFeSES": tnOthOdukRawCountStatRxFeSES,
       "tnOthOdukRawCountStatRxFeUAS": tnOthOdukRawCountStatRxFeUAS,
       "tnOthOdukRawCountStatsTxTotalMembers": tnOthOdukRawCountStatsTxTotalMembers,
       "tnOthOdukRawCountStatsTxTable": tnOthOdukRawCountStatsTxTable,
       "tnOthOdukRawCountStatsTxEntry": tnOthOdukRawCountStatsTxEntry,
       "tnOthOdukRawCountStatsTxClear": tnOthOdukRawCountStatsTxClear,
       "tnOthOdukRawCountStatsTxStartTime": tnOthOdukRawCountStatsTxStartTime,
       "tnOthOdukRawCountStatTxNeBIP8ErrCnt": tnOthOdukRawCountStatTxNeBIP8ErrCnt,
       "tnOthOdukRawCountStatTxNeES": tnOthOdukRawCountStatTxNeES,
       "tnOthOdukRawCountStatTxNeSES": tnOthOdukRawCountStatTxNeSES,
       "tnOthOdukRawCountStatTxNeUAS": tnOthOdukRawCountStatTxNeUAS,
       "tnOthOdukRawCountStatTxFeBIP8ErrCnt": tnOthOdukRawCountStatTxFeBIP8ErrCnt,
       "tnOthOdukRawCountStatTxFeES": tnOthOdukRawCountStatTxFeES,
       "tnOthOdukRawCountStatTxFeSES": tnOthOdukRawCountStatTxFeSES,
       "tnOthOdukRawCountStatTxFeUAS": tnOthOdukRawCountStatTxFeUAS,
       "tnOthOtukRawCountStatsTotalMembers": tnOthOtukRawCountStatsTotalMembers,
       "tnOthOtukRawCountStatsTable": tnOthOtukRawCountStatsTable,
       "tnOthOtukRawCountStatsEntry": tnOthOtukRawCountStatsEntry,
       "tnOthOtukRawCountStatsClear": tnOthOtukRawCountStatsClear,
       "tnOthOtukRawCountStatsStartTime": tnOthOtukRawCountStatsStartTime,
       "tnOthOtukRawCountStatRxRsCorrCnt": tnOthOtukRawCountStatRxRsCorrCnt,
       "tnOthOtukRawCountStatRxRsUncorrCnt": tnOthOtukRawCountStatRxRsUncorrCnt,
       "tnOthOtukRawCountStatRxBERPreFEC": tnOthOtukRawCountStatRxBERPreFEC,
       "tnOthOtukRawCountStatRxBERPostFEC": tnOthOtukRawCountStatRxBERPostFEC,
       "tnOthOtukRawCountStatRxNeSMBIP8ErrCnt": tnOthOtukRawCountStatRxNeSMBIP8ErrCnt,
       "tnOthOtukRawCountStatRxNeSMES": tnOthOtukRawCountStatRxNeSMES,
       "tnOthOtukRawCountStatRxNeSMSES": tnOthOtukRawCountStatRxNeSMSES,
       "tnOthOtukRawCountStatRxNeSMUAS": tnOthOtukRawCountStatRxNeSMUAS,
       "tnOthOtukRawCountStatRxNeIAES": tnOthOtukRawCountStatRxNeIAES,
       "tnOthOtukRawCountStatRxFeSMBIP8ErrCnt": tnOthOtukRawCountStatRxFeSMBIP8ErrCnt,
       "tnOthOtukRawCountStatRxFeSMES": tnOthOtukRawCountStatRxFeSMES,
       "tnOthOtukRawCountStatRxFeSMSES": tnOthOtukRawCountStatRxFeSMSES,
       "tnOthOtukRawCountStatRxFeSMUAS": tnOthOtukRawCountStatRxFeSMUAS,
       "tnOthOtukRawCountStatRxFeIAES": tnOthOtukRawCountStatRxFeIAES,
       "tnOthOtukRawCountStatRxNeBIAES": tnOthOtukRawCountStatRxNeBIAES,
       "tnOsnrRawCountStatsTotalMembers": tnOsnrRawCountStatsTotalMembers,
       "tnOsnrRawCountStatsTable": tnOsnrRawCountStatsTable,
       "tnOsnrRawCountStatsEntry": tnOsnrRawCountStatsEntry,
       "tnOsnrRawCountStatsClear": tnOsnrRawCountStatsClear,
       "tnOsnrRawCountStatStartTime": tnOsnrRawCountStatStartTime,
       "tnOsnrRawCountStatMinOSNR": tnOsnrRawCountStatMinOSNR,
       "tnOsnrRawCountStatMaxOSNR": tnOsnrRawCountStatMaxOSNR,
       "tnOsnrRawCountStatAverageOSNR": tnOsnrRawCountStatAverageOSNR,
       "tnOthOdukRawCountStatsDMTotalMembers": tnOthOdukRawCountStatsDMTotalMembers,
       "tnOthOdukRawCountStatsDMTable": tnOthOdukRawCountStatsDMTable,
       "tnOthOdukRawCountStatsDMEntry": tnOthOdukRawCountStatsDMEntry,
       "tnOthOdukRawCountStatsDMClear": tnOthOdukRawCountStatsDMClear,
       "tnOthOdukRawCountStatsDMStartTime": tnOthOdukRawCountStatsDMStartTime,
       "tnOthOdukRawCountStatsDMMinDm": tnOthOdukRawCountStatsDMMinDm,
       "tnOthOdukRawCountStatsDMMaxDm": tnOthOdukRawCountStatsDMMaxDm,
       "tnOthOdukRawCountStatsDMAverageDm": tnOthOdukRawCountStatsDMAverageDm,
       "tnOthOdukTcmRawCountStatsTotalMembers": tnOthOdukTcmRawCountStatsTotalMembers,
       "tnOthOdukTcmRawCountStatsTable": tnOthOdukTcmRawCountStatsTable,
       "tnOthOdukTcmRawCountStatsEntry": tnOthOdukTcmRawCountStatsEntry,
       "tnOthOdukTcmRawCountStatsClear": tnOthOdukTcmRawCountStatsClear,
       "tnOthOdukTcmRawCountStatsNeRxBIP8ErrCnt": tnOthOdukTcmRawCountStatsNeRxBIP8ErrCnt,
       "tnOthOdukTcmRawCountStatsNeRxIAESErrCnt": tnOthOdukTcmRawCountStatsNeRxIAESErrCnt,
       "tnOthOdukTcmRawCountStatsNeRxES": tnOthOdukTcmRawCountStatsNeRxES,
       "tnOthOdukTcmRawCountStatsNeRxSES": tnOthOdukTcmRawCountStatsNeRxSES,
       "tnOthOdukTcmRawCountStatsNeRxUAS": tnOthOdukTcmRawCountStatsNeRxUAS,
       "tnOthOdukTcmRawCountStatsFeRxBIP8ErrCnt": tnOthOdukTcmRawCountStatsFeRxBIP8ErrCnt,
       "tnOthOdukTcmRawCountStatsFeRxBIAESErrCnt": tnOthOdukTcmRawCountStatsFeRxBIAESErrCnt,
       "tnOthOdukTcmRawCountStatsFeRxES": tnOthOdukTcmRawCountStatsFeRxES,
       "tnOthOdukTcmRawCountStatsFeRxSES": tnOthOdukTcmRawCountStatsFeRxSES,
       "tnOthOdukTcmRawCountStatsFeRxUAS": tnOthOdukTcmRawCountStatsFeRxUAS,
       "tnOthOdukTcmRawCountStatsStartTime": tnOthOdukTcmRawCountStatsStartTime,
       "tnStatisticsBaseline": tnStatisticsBaseline,
       "tnStatsBaselineTable": tnStatsBaselineTable,
       "tnStatsBaselineEntry": tnStatsBaselineEntry,
       "tnStatsBaselineReason": tnStatsBaselineReason,
       "tnStatsBaselineValue": tnStatsBaselineValue,
       "tnStatsBaselineTime": tnStatsBaselineTime,
       "tnStatisticsOdukRxScalars": tnStatisticsOdukRxScalars,
       "tnOthOdu0StatRxNeBIP8ErrCnt15MinTr": tnOthOdu0StatRxNeBIP8ErrCnt15MinTr,
       "tnOthOdu0StatRxNeBIP8ErrCnt15MinRtr": tnOthOdu0StatRxNeBIP8ErrCnt15MinRtr,
       "tnOthOdu0StatRxNeBIP8ErrCnt1DayTr": tnOthOdu0StatRxNeBIP8ErrCnt1DayTr,
       "tnOthOdu0StatRxFeBIP8ErrCnt15MinTr": tnOthOdu0StatRxFeBIP8ErrCnt15MinTr,
       "tnOthOdu0StatRxFeBIP8ErrCnt15MinRtr": tnOthOdu0StatRxFeBIP8ErrCnt15MinRtr,
       "tnOthOdu0StatRxFeBIP8ErrCnt1DayTr": tnOthOdu0StatRxFeBIP8ErrCnt1DayTr,
       "tnOthOdu1StatRxNeBIP8ErrCnt15MinTr": tnOthOdu1StatRxNeBIP8ErrCnt15MinTr,
       "tnOthOdu1StatRxNeBIP8ErrCnt15MinRtr": tnOthOdu1StatRxNeBIP8ErrCnt15MinRtr,
       "tnOthOdu1StatRxNeBIP8ErrCnt1DayTr": tnOthOdu1StatRxNeBIP8ErrCnt1DayTr,
       "tnOthOdu1StatRxFeBIP8ErrCnt15MinTr": tnOthOdu1StatRxFeBIP8ErrCnt15MinTr,
       "tnOthOdu1StatRxFeBIP8ErrCnt15MinRtr": tnOthOdu1StatRxFeBIP8ErrCnt15MinRtr,
       "tnOthOdu1StatRxFeBIP8ErrCnt1DayTr": tnOthOdu1StatRxFeBIP8ErrCnt1DayTr,
       "tnOthOdu2StatRxNeBIP8ErrCnt15MinTr": tnOthOdu2StatRxNeBIP8ErrCnt15MinTr,
       "tnOthOdu2StatRxNeBIP8ErrCnt15MinRtr": tnOthOdu2StatRxNeBIP8ErrCnt15MinRtr,
       "tnOthOdu2StatRxNeBIP8ErrCnt1DayTr": tnOthOdu2StatRxNeBIP8ErrCnt1DayTr,
       "tnOthOdu2StatRxFeBIP8ErrCnt15MinTr": tnOthOdu2StatRxFeBIP8ErrCnt15MinTr,
       "tnOthOdu2StatRxFeBIP8ErrCnt15MinRtr": tnOthOdu2StatRxFeBIP8ErrCnt15MinRtr,
       "tnOthOdu2StatRxFeBIP8ErrCnt1DayTr": tnOthOdu2StatRxFeBIP8ErrCnt1DayTr,
       "tnOthOdu3StatRxNeBIP8ErrCnt15MinTr": tnOthOdu3StatRxNeBIP8ErrCnt15MinTr,
       "tnOthOdu3StatRxNeBIP8ErrCnt15MinRtr": tnOthOdu3StatRxNeBIP8ErrCnt15MinRtr,
       "tnOthOdu3StatRxNeBIP8ErrCnt1DayTr": tnOthOdu3StatRxNeBIP8ErrCnt1DayTr,
       "tnOthOdu3StatRxFeBIP8ErrCnt15MinTr": tnOthOdu3StatRxFeBIP8ErrCnt15MinTr,
       "tnOthOdu3StatRxFeBIP8ErrCnt15MinRtr": tnOthOdu3StatRxFeBIP8ErrCnt15MinRtr,
       "tnOthOdu3StatRxFeBIP8ErrCnt1DayTr": tnOthOdu3StatRxFeBIP8ErrCnt1DayTr,
       "tnOthOdu4StatRxNeBIP8ErrCnt15MinTr": tnOthOdu4StatRxNeBIP8ErrCnt15MinTr,
       "tnOthOdu4StatRxNeBIP8ErrCnt15MinRtr": tnOthOdu4StatRxNeBIP8ErrCnt15MinRtr,
       "tnOthOdu4StatRxNeBIP8ErrCnt1DayTr": tnOthOdu4StatRxNeBIP8ErrCnt1DayTr,
       "tnOthOdu4StatRxFeBIP8ErrCnt15MinTr": tnOthOdu4StatRxFeBIP8ErrCnt15MinTr,
       "tnOthOdu4StatRxFeBIP8ErrCnt15MinRtr": tnOthOdu4StatRxFeBIP8ErrCnt15MinRtr,
       "tnOthOdu4StatRxFeBIP8ErrCnt1DayTr": tnOthOdu4StatRxFeBIP8ErrCnt1DayTr,
       "tnOthOdukStatRxNeES15MinTr": tnOthOdukStatRxNeES15MinTr,
       "tnOthOdukStatRxNeES15MinRtr": tnOthOdukStatRxNeES15MinRtr,
       "tnOthOdukStatRxNeES1DayTr": tnOthOdukStatRxNeES1DayTr,
       "tnOthOdukStatRxFeES15MinTr": tnOthOdukStatRxFeES15MinTr,
       "tnOthOdukStatRxFeES15MinRtr": tnOthOdukStatRxFeES15MinRtr,
       "tnOthOdukStatRxFeES1DayTr": tnOthOdukStatRxFeES1DayTr,
       "tnOthOdukStatRxNeSES15MinTr": tnOthOdukStatRxNeSES15MinTr,
       "tnOthOdukStatRxNeSES15MinRtr": tnOthOdukStatRxNeSES15MinRtr,
       "tnOthOdukStatRxNeSES1DayTr": tnOthOdukStatRxNeSES1DayTr,
       "tnOthOdukStatRxFeSES15MinTr": tnOthOdukStatRxFeSES15MinTr,
       "tnOthOdukStatRxFeSES15MinRtr": tnOthOdukStatRxFeSES15MinRtr,
       "tnOthOdukStatRxFeSES1DayTr": tnOthOdukStatRxFeSES1DayTr,
       "tnOthOdukStatRxNeUAS15MinTr": tnOthOdukStatRxNeUAS15MinTr,
       "tnOthOdukStatRxNeUAS15MinRtr": tnOthOdukStatRxNeUAS15MinRtr,
       "tnOthOdukStatRxNeUAS1DayTr": tnOthOdukStatRxNeUAS1DayTr,
       "tnOthOdukStatRxFeUAS15MinTr": tnOthOdukStatRxFeUAS15MinTr,
       "tnOthOdukStatRxFeUAS15MinRtr": tnOthOdukStatRxFeUAS15MinRtr,
       "tnOthOdukStatRxFeUAS1DayTr": tnOthOdukStatRxFeUAS1DayTr,
       "tnStatisticsOdukTxScalars": tnStatisticsOdukTxScalars,
       "tnOthOdu0StatTxNeBIP8ErrCnt15MinTr": tnOthOdu0StatTxNeBIP8ErrCnt15MinTr,
       "tnOthOdu0StatTxNeBIP8ErrCnt15MinRtr": tnOthOdu0StatTxNeBIP8ErrCnt15MinRtr,
       "tnOthOdu0StatTxNeBIP8ErrCnt1DayTr": tnOthOdu0StatTxNeBIP8ErrCnt1DayTr,
       "tnOthOdu0StatTxFeBIP8ErrCnt15MinTr": tnOthOdu0StatTxFeBIP8ErrCnt15MinTr,
       "tnOthOdu0StatTxFeBIP8ErrCnt15MinRtr": tnOthOdu0StatTxFeBIP8ErrCnt15MinRtr,
       "tnOthOdu0StatTxFeBIP8ErrCnt1DayTr": tnOthOdu0StatTxFeBIP8ErrCnt1DayTr,
       "tnOthOdu1StatTxNeBIP8ErrCnt15MinTr": tnOthOdu1StatTxNeBIP8ErrCnt15MinTr,
       "tnOthOdu1StatTxNeBIP8ErrCnt15MinRtr": tnOthOdu1StatTxNeBIP8ErrCnt15MinRtr,
       "tnOthOdu1StatTxNeBIP8ErrCnt1DayTr": tnOthOdu1StatTxNeBIP8ErrCnt1DayTr,
       "tnOthOdu1StatTxFeBIP8ErrCnt15MinTr": tnOthOdu1StatTxFeBIP8ErrCnt15MinTr,
       "tnOthOdu1StatTxFeBIP8ErrCnt15MinRtr": tnOthOdu1StatTxFeBIP8ErrCnt15MinRtr,
       "tnOthOdu1StatTxFeBIP8ErrCnt1DayTr": tnOthOdu1StatTxFeBIP8ErrCnt1DayTr,
       "tnOthOdu2StatTxNeBIP8ErrCnt15MinTr": tnOthOdu2StatTxNeBIP8ErrCnt15MinTr,
       "tnOthOdu2StatTxNeBIP8ErrCnt15MinRtr": tnOthOdu2StatTxNeBIP8ErrCnt15MinRtr,
       "tnOthOdu2StatTxNeBIP8ErrCnt1DayTr": tnOthOdu2StatTxNeBIP8ErrCnt1DayTr,
       "tnOthOdu2StatTxFeBIP8ErrCnt15MinTr": tnOthOdu2StatTxFeBIP8ErrCnt15MinTr,
       "tnOthOdu2StatTxFeBIP8ErrCnt15MinRtr": tnOthOdu2StatTxFeBIP8ErrCnt15MinRtr,
       "tnOthOdu2StatTxFeBIP8ErrCnt1DayTr": tnOthOdu2StatTxFeBIP8ErrCnt1DayTr,
       "tnOthOdu3StatTxNeBIP8ErrCnt15MinTr": tnOthOdu3StatTxNeBIP8ErrCnt15MinTr,
       "tnOthOdu3StatTxNeBIP8ErrCnt15MinRtr": tnOthOdu3StatTxNeBIP8ErrCnt15MinRtr,
       "tnOthOdu3StatTxNeBIP8ErrCnt1DayTr": tnOthOdu3StatTxNeBIP8ErrCnt1DayTr,
       "tnOthOdu3StatTxFeBIP8ErrCnt15MinTr": tnOthOdu3StatTxFeBIP8ErrCnt15MinTr,
       "tnOthOdu3StatTxFeBIP8ErrCnt15MinRtr": tnOthOdu3StatTxFeBIP8ErrCnt15MinRtr,
       "tnOthOdu3StatTxFeBIP8ErrCnt1DayTr": tnOthOdu3StatTxFeBIP8ErrCnt1DayTr,
       "tnOthOdu4StatTxNeBIP8ErrCnt15MinTr": tnOthOdu4StatTxNeBIP8ErrCnt15MinTr,
       "tnOthOdu4StatTxNeBIP8ErrCnt15MinRtr": tnOthOdu4StatTxNeBIP8ErrCnt15MinRtr,
       "tnOthOdu4StatTxNeBIP8ErrCnt1DayTr": tnOthOdu4StatTxNeBIP8ErrCnt1DayTr,
       "tnOthOdu4StatTxFeBIP8ErrCnt15MinTr": tnOthOdu4StatTxFeBIP8ErrCnt15MinTr,
       "tnOthOdu4StatTxFeBIP8ErrCnt15MinRtr": tnOthOdu4StatTxFeBIP8ErrCnt15MinRtr,
       "tnOthOdu4StatTxFeBIP8ErrCnt1DayTr": tnOthOdu4StatTxFeBIP8ErrCnt1DayTr,
       "tnOthOdukStatTxNeES15MinTr": tnOthOdukStatTxNeES15MinTr,
       "tnOthOdukStatTxNeES15MinRtr": tnOthOdukStatTxNeES15MinRtr,
       "tnOthOdukStatTxNeES1DayTr": tnOthOdukStatTxNeES1DayTr,
       "tnOthOdukStatTxFeES15MinTr": tnOthOdukStatTxFeES15MinTr,
       "tnOthOdukStatTxFeES15MinRtr": tnOthOdukStatTxFeES15MinRtr,
       "tnOthOdukStatTxFeES1DayTr": tnOthOdukStatTxFeES1DayTr,
       "tnOthOdukStatTxNeSES15MinTr": tnOthOdukStatTxNeSES15MinTr,
       "tnOthOdukStatTxNeSES15MinRtr": tnOthOdukStatTxNeSES15MinRtr,
       "tnOthOdukStatTxNeSES1DayTr": tnOthOdukStatTxNeSES1DayTr,
       "tnOthOdukStatTxFeSES15MinTr": tnOthOdukStatTxFeSES15MinTr,
       "tnOthOdukStatTxFeSES15MinRtr": tnOthOdukStatTxFeSES15MinRtr,
       "tnOthOdukStatTxFeSES1DayTr": tnOthOdukStatTxFeSES1DayTr,
       "tnOthOdukStatTxNeUAS15MinTr": tnOthOdukStatTxNeUAS15MinTr,
       "tnOthOdukStatTxNeUAS15MinRtr": tnOthOdukStatTxNeUAS15MinRtr,
       "tnOthOdukStatTxNeUAS1DayTr": tnOthOdukStatTxNeUAS1DayTr,
       "tnOthOdukStatTxFeUAS15MinTr": tnOthOdukStatTxFeUAS15MinTr,
       "tnOthOdukStatTxFeUAS15MinRtr": tnOthOdukStatTxFeUAS15MinRtr,
       "tnOthOdukStatTxFeUAS1DayTr": tnOthOdukStatTxFeUAS1DayTr,
       "tnStatisticsOtukScalars": tnStatisticsOtukScalars,
       "tnOthOtu1StatRxRsCorrCnt15MinTr": tnOthOtu1StatRxRsCorrCnt15MinTr,
       "tnOthOtu1StatRxRsCorrCnt15MinRtr": tnOthOtu1StatRxRsCorrCnt15MinRtr,
       "tnOthOtu1StatRxRsCorrCnt1DayTr": tnOthOtu1StatRxRsCorrCnt1DayTr,
       "tnOthOtu1StatRxRsUncorrCnt15MinTr": tnOthOtu1StatRxRsUncorrCnt15MinTr,
       "tnOthOtu1StatRxRsUncorrCnt15MinRtr": tnOthOtu1StatRxRsUncorrCnt15MinRtr,
       "tnOthOtu1StatRxRsUncorrCnt1DayTr": tnOthOtu1StatRxRsUncorrCnt1DayTr,
       "tnOthOtu1StatRxNeSMBIP8ErrCnt15MinTr": tnOthOtu1StatRxNeSMBIP8ErrCnt15MinTr,
       "tnOthOtu1StatRxNeSMBIP8ErrCnt15MinRtr": tnOthOtu1StatRxNeSMBIP8ErrCnt15MinRtr,
       "tnOthOtu1StatRxNeSMBIP8ErrCnt1DayTr": tnOthOtu1StatRxNeSMBIP8ErrCnt1DayTr,
       "tnOthOtu1StatRxFeSMBIP8ErrCnt15MinTr": tnOthOtu1StatRxFeSMBIP8ErrCnt15MinTr,
       "tnOthOtu1StatRxFeSMBIP8ErrCnt15MinRtr": tnOthOtu1StatRxFeSMBIP8ErrCnt15MinRtr,
       "tnOthOtu1StatRxFeSMBIP8ErrCnt1DayTr": tnOthOtu1StatRxFeSMBIP8ErrCnt1DayTr,
       "tnOthOtu2StatRxRsCorrCnt15MinTr": tnOthOtu2StatRxRsCorrCnt15MinTr,
       "tnOthOtu2StatRxRsCorrCnt15MinRtr": tnOthOtu2StatRxRsCorrCnt15MinRtr,
       "tnOthOtu2StatRxRsCorrCnt1DayTr": tnOthOtu2StatRxRsCorrCnt1DayTr,
       "tnOthOtu2StatRxRsUncorrCnt15MinTr": tnOthOtu2StatRxRsUncorrCnt15MinTr,
       "tnOthOtu2StatRxRsUncorrCnt15MinRtr": tnOthOtu2StatRxRsUncorrCnt15MinRtr,
       "tnOthOtu2StatRxRsUncorrCnt1DayTr": tnOthOtu2StatRxRsUncorrCnt1DayTr,
       "tnOthOtu2StatRxNeSMBIP8ErrCnt15MinTr": tnOthOtu2StatRxNeSMBIP8ErrCnt15MinTr,
       "tnOthOtu2StatRxNeSMBIP8ErrCnt15MinRtr": tnOthOtu2StatRxNeSMBIP8ErrCnt15MinRtr,
       "tnOthOtu2StatRxNeSMBIP8ErrCnt1DayTr": tnOthOtu2StatRxNeSMBIP8ErrCnt1DayTr,
       "tnOthOtu2StatRxFeSMBIP8ErrCnt15MinTr": tnOthOtu2StatRxFeSMBIP8ErrCnt15MinTr,
       "tnOthOtu2StatRxFeSMBIP8ErrCnt15MinRtr": tnOthOtu2StatRxFeSMBIP8ErrCnt15MinRtr,
       "tnOthOtu2StatRxFeSMBIP8ErrCnt1DayTr": tnOthOtu2StatRxFeSMBIP8ErrCnt1DayTr,
       "tnOthOtu3StatRxRsCorrCnt15MinTr": tnOthOtu3StatRxRsCorrCnt15MinTr,
       "tnOthOtu3StatRxRsCorrCnt15MinRtr": tnOthOtu3StatRxRsCorrCnt15MinRtr,
       "tnOthOtu3StatRxRsCorrCnt1DayTr": tnOthOtu3StatRxRsCorrCnt1DayTr,
       "tnOthOtu3StatRxRsUncorrCnt15MinTr": tnOthOtu3StatRxRsUncorrCnt15MinTr,
       "tnOthOtu3StatRxRsUncorrCnt15MinRtr": tnOthOtu3StatRxRsUncorrCnt15MinRtr,
       "tnOthOtu3StatRxRsUncorrCnt1DayTr": tnOthOtu3StatRxRsUncorrCnt1DayTr,
       "tnOthOtu3StatRxNeSMBIP8ErrCnt15MinTr": tnOthOtu3StatRxNeSMBIP8ErrCnt15MinTr,
       "tnOthOtu3StatRxNeSMBIP8ErrCnt15MinRtr": tnOthOtu3StatRxNeSMBIP8ErrCnt15MinRtr,
       "tnOthOtu3StatRxNeSMBIP8ErrCnt1DayTr": tnOthOtu3StatRxNeSMBIP8ErrCnt1DayTr,
       "tnOthOtu3StatRxFeSMBIP8ErrCnt15MinTr": tnOthOtu3StatRxFeSMBIP8ErrCnt15MinTr,
       "tnOthOtu3StatRxFeSMBIP8ErrCnt15MinRtr": tnOthOtu3StatRxFeSMBIP8ErrCnt15MinRtr,
       "tnOthOtu3StatRxFeSMBIP8ErrCnt1DayTr": tnOthOtu3StatRxFeSMBIP8ErrCnt1DayTr,
       "tnOthOtu4StatRxRsCorrCnt15MinTr": tnOthOtu4StatRxRsCorrCnt15MinTr,
       "tnOthOtu4StatRxRsCorrCnt15MinRtr": tnOthOtu4StatRxRsCorrCnt15MinRtr,
       "tnOthOtu4StatRxRsCorrCnt1DayTr": tnOthOtu4StatRxRsCorrCnt1DayTr,
       "tnOthOtu4StatRxRsUncorrCnt15MinTr": tnOthOtu4StatRxRsUncorrCnt15MinTr,
       "tnOthOtu4StatRxRsUncorrCnt15MinRtr": tnOthOtu4StatRxRsUncorrCnt15MinRtr,
       "tnOthOtu4StatRxRsUncorrCnt1DayTr": tnOthOtu4StatRxRsUncorrCnt1DayTr,
       "tnOthOtu4StatRxNeSMBIP8ErrCnt15MinTr": tnOthOtu4StatRxNeSMBIP8ErrCnt15MinTr,
       "tnOthOtu4StatRxNeSMBIP8ErrCnt15MinRtr": tnOthOtu4StatRxNeSMBIP8ErrCnt15MinRtr,
       "tnOthOtu4StatRxNeSMBIP8ErrCnt1DayTr": tnOthOtu4StatRxNeSMBIP8ErrCnt1DayTr,
       "tnOthOtu4StatRxFeSMBIP8ErrCnt15MinTr": tnOthOtu4StatRxFeSMBIP8ErrCnt15MinTr,
       "tnOthOtu4StatRxFeSMBIP8ErrCnt15MinRtr": tnOthOtu4StatRxFeSMBIP8ErrCnt15MinRtr,
       "tnOthOtu4StatRxFeSMBIP8ErrCnt1DayTr": tnOthOtu4StatRxFeSMBIP8ErrCnt1DayTr,
       "tnOthOtukStatRxBERPreFEC15MinTr": tnOthOtukStatRxBERPreFEC15MinTr,
       "tnOthOtukStatRxBERPreFEC15MinRtr": tnOthOtukStatRxBERPreFEC15MinRtr,
       "tnOthOtukStatRxBERPreFEC1DayTr": tnOthOtukStatRxBERPreFEC1DayTr,
       "tnOthOtukStatRxBERPostFEC15MinTr": tnOthOtukStatRxBERPostFEC15MinTr,
       "tnOthOtukStatRxBERPostFEC15MinRtr": tnOthOtukStatRxBERPostFEC15MinRtr,
       "tnOthOtukStatRxBERPostFEC1DayTr": tnOthOtukStatRxBERPostFEC1DayTr,
       "tnOthOtukStatRxNeSMES15MinTr": tnOthOtukStatRxNeSMES15MinTr,
       "tnOthOtukStatRxNeSMES15MinRtr": tnOthOtukStatRxNeSMES15MinRtr,
       "tnOthOtukStatRxNeSMES1DayTr": tnOthOtukStatRxNeSMES1DayTr,
       "tnOthOtukStatRxFeSMES15MinTr": tnOthOtukStatRxFeSMES15MinTr,
       "tnOthOtukStatRxFeSMES15MinRtr": tnOthOtukStatRxFeSMES15MinRtr,
       "tnOthOtukStatRxFeSMES1DayTr": tnOthOtukStatRxFeSMES1DayTr,
       "tnOthOtukStatRxNeSMSES15MinTr": tnOthOtukStatRxNeSMSES15MinTr,
       "tnOthOtukStatRxNeSMSES15MinRtr": tnOthOtukStatRxNeSMSES15MinRtr,
       "tnOthOtukStatRxNeSMSES1DayTr": tnOthOtukStatRxNeSMSES1DayTr,
       "tnOthOtukStatRxFeSMSES15MinTr": tnOthOtukStatRxFeSMSES15MinTr,
       "tnOthOtukStatRxFeSMSES15MinRtr": tnOthOtukStatRxFeSMSES15MinRtr,
       "tnOthOtukStatRxFeSMSES1DayTr": tnOthOtukStatRxFeSMSES1DayTr,
       "tnOthOtukStatRxNeSMUAS15MinTr": tnOthOtukStatRxNeSMUAS15MinTr,
       "tnOthOtukStatRxNeSMUAS15MinRtr": tnOthOtukStatRxNeSMUAS15MinRtr,
       "tnOthOtukStatRxNeSMUAS1DayTr": tnOthOtukStatRxNeSMUAS1DayTr,
       "tnOthOtukStatRxFeSMUAS15MinTr": tnOthOtukStatRxFeSMUAS15MinTr,
       "tnOthOtukStatRxFeSMUAS15MinRtr": tnOthOtukStatRxFeSMUAS15MinRtr,
       "tnOthOtukStatRxFeSMUAS1DayTr": tnOthOtukStatRxFeSMUAS1DayTr,
       "tnOthOtukStatRxNeIAES15MinTr": tnOthOtukStatRxNeIAES15MinTr,
       "tnOthOtukStatRxNeIAES15MinRtr": tnOthOtukStatRxNeIAES15MinRtr,
       "tnOthOtukStatRxNeIAES1DayTr": tnOthOtukStatRxNeIAES1DayTr,
       "tnOthOtukStatRxFeIAES15MinTr": tnOthOtukStatRxFeIAES15MinTr,
       "tnOthOtukStatRxFeIAES15MinRtr": tnOthOtukStatRxFeIAES15MinRtr,
       "tnOthOtukStatRxFeIAES1DayTr": tnOthOtukStatRxFeIAES1DayTr,
       "tnStatisticsSonetScalars": tnStatisticsSonetScalars,
       "tnSonetStatsOC768RxCVS15MinTr": tnSonetStatsOC768RxCVS15MinTr,
       "tnSonetStatsOC192RxCVS15MinTr": tnSonetStatsOC192RxCVS15MinTr,
       "tnSonetStatsOC48RxCVS15MinTr": tnSonetStatsOC48RxCVS15MinTr,
       "tnSonetStatsOC12RxCVS15MinTr": tnSonetStatsOC12RxCVS15MinTr,
       "tnSonetStatsOC3RxCVS15MinTr": tnSonetStatsOC3RxCVS15MinTr,
       "tnSonetStatsRxESS15MinTr": tnSonetStatsRxESS15MinTr,
       "tnSonetStatsRxSESS15MinTr": tnSonetStatsRxSESS15MinTr,
       "tnSonetStatsRxSEFSS15MinTr": tnSonetStatsRxSEFSS15MinTr,
       "tnSonetStatsOC768RxCVL15MinTr": tnSonetStatsOC768RxCVL15MinTr,
       "tnSonetStatsOC192RxCVL15MinTr": tnSonetStatsOC192RxCVL15MinTr,
       "tnSonetStatsOC48RxCVL15MinTr": tnSonetStatsOC48RxCVL15MinTr,
       "tnSonetStatsOC12RxCVL15MinTr": tnSonetStatsOC12RxCVL15MinTr,
       "tnSonetStatsOC3RxCVL15MinTr": tnSonetStatsOC3RxCVL15MinTr,
       "tnSonetStatsRxESL15MinTr": tnSonetStatsRxESL15MinTr,
       "tnSonetStatsRxSESL15MinTr": tnSonetStatsRxSESL15MinTr,
       "tnSonetStatsRxUASL15MinTr": tnSonetStatsRxUASL15MinTr,
       "tnSonetStatsOC768TxCVS15MinTr": tnSonetStatsOC768TxCVS15MinTr,
       "tnSonetStatsOC192TxCVS15MinTr": tnSonetStatsOC192TxCVS15MinTr,
       "tnSonetStatsOC48TxCVS15MinTr": tnSonetStatsOC48TxCVS15MinTr,
       "tnSonetStatsOC12TxCVS15MinTr": tnSonetStatsOC12TxCVS15MinTr,
       "tnSonetStatsOC3TxCVS15MinTr": tnSonetStatsOC3TxCVS15MinTr,
       "tnSonetStatsTxESS15MinTr": tnSonetStatsTxESS15MinTr,
       "tnSonetStatsTxSESS15MinTr": tnSonetStatsTxSESS15MinTr,
       "tnSonetStatsTxSEFSS15MinTr": tnSonetStatsTxSEFSS15MinTr,
       "tnSonetStatsOC768TxCVL15MinTr": tnSonetStatsOC768TxCVL15MinTr,
       "tnSonetStatsOC192TxCVL15MinTr": tnSonetStatsOC192TxCVL15MinTr,
       "tnSonetStatsOC48TxCVL15MinTr": tnSonetStatsOC48TxCVL15MinTr,
       "tnSonetStatsOC12TxCVL15MinTr": tnSonetStatsOC12TxCVL15MinTr,
       "tnSonetStatsOC3TxCVL15MinTr": tnSonetStatsOC3TxCVL15MinTr,
       "tnSonetStatsTxESL15MinTr": tnSonetStatsTxESL15MinTr,
       "tnSonetStatsTxSESL15MinTr": tnSonetStatsTxSESL15MinTr,
       "tnSonetStatsTxUASL15MinTr": tnSonetStatsTxUASL15MinTr,
       "tnSonetStatsRxUASS15MinTr": tnSonetStatsRxUASS15MinTr,
       "tnSonetStatsTxUASS15MinTr": tnSonetStatsTxUASS15MinTr,
       "tnSonetStatsOC768RxCVS1DayTr": tnSonetStatsOC768RxCVS1DayTr,
       "tnSonetStatsOC192RxCVS1DayTr": tnSonetStatsOC192RxCVS1DayTr,
       "tnSonetStatsOC48RxCVS1DayTr": tnSonetStatsOC48RxCVS1DayTr,
       "tnSonetStatsOC12RxCVS1DayTr": tnSonetStatsOC12RxCVS1DayTr,
       "tnSonetStatsOC3RxCVS1DayTr": tnSonetStatsOC3RxCVS1DayTr,
       "tnSonetStatsRxESS1DayTr": tnSonetStatsRxESS1DayTr,
       "tnSonetStatsRxSESS1DayTr": tnSonetStatsRxSESS1DayTr,
       "tnSonetStatsRxSEFSS1DayTr": tnSonetStatsRxSEFSS1DayTr,
       "tnSonetStatsOC768RxCVL1DayTr": tnSonetStatsOC768RxCVL1DayTr,
       "tnSonetStatsOC192RxCVL1DayTr": tnSonetStatsOC192RxCVL1DayTr,
       "tnSonetStatsOC48RxCVL1DayTr": tnSonetStatsOC48RxCVL1DayTr,
       "tnSonetStatsOC12RxCVL1DayTr": tnSonetStatsOC12RxCVL1DayTr,
       "tnSonetStatsOC3RxCVL1DayTr": tnSonetStatsOC3RxCVL1DayTr,
       "tnSonetStatsRxESL1DayTr": tnSonetStatsRxESL1DayTr,
       "tnSonetStatsRxSESL1DayTr": tnSonetStatsRxSESL1DayTr,
       "tnSonetStatsRxUASL1DayTr": tnSonetStatsRxUASL1DayTr,
       "tnSonetStatsOC768TxCVS1DayTr": tnSonetStatsOC768TxCVS1DayTr,
       "tnSonetStatsOC192TxCVS1DayTr": tnSonetStatsOC192TxCVS1DayTr,
       "tnSonetStatsOC48TxCVS1DayTr": tnSonetStatsOC48TxCVS1DayTr,
       "tnSonetStatsOC12TxCVS1DayTr": tnSonetStatsOC12TxCVS1DayTr,
       "tnSonetStatsOC3TxCVS1DayTr": tnSonetStatsOC3TxCVS1DayTr,
       "tnSonetStatsTxESS1DayTr": tnSonetStatsTxESS1DayTr,
       "tnSonetStatsTxSESS1DayTr": tnSonetStatsTxSESS1DayTr,
       "tnSonetStatsTxSEFSS1DayTr": tnSonetStatsTxSEFSS1DayTr,
       "tnSonetStatsOC768TxCVL1DayTr": tnSonetStatsOC768TxCVL1DayTr,
       "tnSonetStatsOC192TxCVL1DayTr": tnSonetStatsOC192TxCVL1DayTr,
       "tnSonetStatsOC48TxCVL1DayTr": tnSonetStatsOC48TxCVL1DayTr,
       "tnSonetStatsOC12TxCVL1DayTr": tnSonetStatsOC12TxCVL1DayTr,
       "tnSonetStatsOC3TxCVL1DayTr": tnSonetStatsOC3TxCVL1DayTr,
       "tnSonetStatsTxESL1DayTr": tnSonetStatsTxESL1DayTr,
       "tnSonetStatsTxSESL1DayTr": tnSonetStatsTxSESL1DayTr,
       "tnSonetStatsTxUASL1DayTr": tnSonetStatsTxUASL1DayTr,
       "tnSonetStatsRxUASS1DayTr": tnSonetStatsRxUASS1DayTr,
       "tnSonetStatsTxUASS1DayTr": tnSonetStatsTxUASS1DayTr,
       "tnSonetStatsOC768RxFECVL15MinTr": tnSonetStatsOC768RxFECVL15MinTr,
       "tnSonetStatsOC192RxFECVL15MinTr": tnSonetStatsOC192RxFECVL15MinTr,
       "tnSonetStatsOC48RxFECVL15MinTr": tnSonetStatsOC48RxFECVL15MinTr,
       "tnSonetStatsOC12RxFECVL15MinTr": tnSonetStatsOC12RxFECVL15MinTr,
       "tnSonetStatsOC3RxFECVL15MinTr": tnSonetStatsOC3RxFECVL15MinTr,
       "tnSonetStatsRxFEESL15MinTr": tnSonetStatsRxFEESL15MinTr,
       "tnSonetStatsRxFESESL15MinTr": tnSonetStatsRxFESESL15MinTr,
       "tnSonetStatsRxFEUASL15MinTr": tnSonetStatsRxFEUASL15MinTr,
       "tnSonetStatsOC768RxFECVL1DayTr": tnSonetStatsOC768RxFECVL1DayTr,
       "tnSonetStatsOC192RxFECVL1DayTr": tnSonetStatsOC192RxFECVL1DayTr,
       "tnSonetStatsOC48RxFECVL1DayTr": tnSonetStatsOC48RxFECVL1DayTr,
       "tnSonetStatsOC12RxFECVL1DayTr": tnSonetStatsOC12RxFECVL1DayTr,
       "tnSonetStatsOC3RxFECVL1DayTr": tnSonetStatsOC3RxFECVL1DayTr,
       "tnSonetStatsRxFEESL1DayTr": tnSonetStatsRxFEESL1DayTr,
       "tnSonetStatsRxFESESL1DayTr": tnSonetStatsRxFESESL1DayTr,
       "tnSonetStatsRxFEUASL1DayTr": tnSonetStatsRxFEUASL1DayTr,
       "tnStatisticsSdhScalars": tnStatisticsSdhScalars,
       "tnSdhStatsSTM256RxRSEB15MinTr": tnSdhStatsSTM256RxRSEB15MinTr,
       "tnSdhStatsSTM64RxRSEB15MinTr": tnSdhStatsSTM64RxRSEB15MinTr,
       "tnSdhStatsSTM16RxRSEB15MinTr": tnSdhStatsSTM16RxRSEB15MinTr,
       "tnSdhStatsSTM4RxRSEB15MinTr": tnSdhStatsSTM4RxRSEB15MinTr,
       "tnSdhStatsSTM1RxRSEB15MinTr": tnSdhStatsSTM1RxRSEB15MinTr,
       "tnSdhStatsRxRSES15MinTr": tnSdhStatsRxRSES15MinTr,
       "tnSdhStatsRxRSSES15MinTr": tnSdhStatsRxRSSES15MinTr,
       "tnSdhStatsSTM256RxMSEB15MinTr": tnSdhStatsSTM256RxMSEB15MinTr,
       "tnSdhStatsSTM64RxMSEB15MinTr": tnSdhStatsSTM64RxMSEB15MinTr,
       "tnSdhStatsSTM16RxMSEB15MinTr": tnSdhStatsSTM16RxMSEB15MinTr,
       "tnSdhStatsSTM4RxMSEB15MinTr": tnSdhStatsSTM4RxMSEB15MinTr,
       "tnSdhStatsSTM1RxMSEB15MinTr": tnSdhStatsSTM1RxMSEB15MinTr,
       "tnSdhStatsRxMSES15MinTr": tnSdhStatsRxMSES15MinTr,
       "tnSdhStatsRxMSSES15MinTr": tnSdhStatsRxMSSES15MinTr,
       "tnSdhStatsRxMSUAS15MinTr": tnSdhStatsRxMSUAS15MinTr,
       "tnSdhStatsSTM256TxRSEB15MinTr": tnSdhStatsSTM256TxRSEB15MinTr,
       "tnSdhStatsSTM64TxRSEB15MinTr": tnSdhStatsSTM64TxRSEB15MinTr,
       "tnSdhStatsSTM16TxRSEB15MinTr": tnSdhStatsSTM16TxRSEB15MinTr,
       "tnSdhStatsSTM4TxRSEB15MinTr": tnSdhStatsSTM4TxRSEB15MinTr,
       "tnSdhStatsSTM1TxRSEB15MinTr": tnSdhStatsSTM1TxRSEB15MinTr,
       "tnSdhStatsTxRSES15MinTr": tnSdhStatsTxRSES15MinTr,
       "tnSdhStatsTxRSSES15MinTr": tnSdhStatsTxRSSES15MinTr,
       "tnSdhStatsSTM256TxMSEB15MinTr": tnSdhStatsSTM256TxMSEB15MinTr,
       "tnSdhStatsSTM64TxMSEB15MinTr": tnSdhStatsSTM64TxMSEB15MinTr,
       "tnSdhStatsSTM16TxMSEB15MinTr": tnSdhStatsSTM16TxMSEB15MinTr,
       "tnSdhStatsSTM4TxMSEB15MinTr": tnSdhStatsSTM4TxMSEB15MinTr,
       "tnSdhStatsSTM1TxMSEB15MinTr": tnSdhStatsSTM1TxMSEB15MinTr,
       "tnSdhStatsTxMSES15MinTr": tnSdhStatsTxMSES15MinTr,
       "tnSdhStatsTxMSSES15MinTr": tnSdhStatsTxMSSES15MinTr,
       "tnSdhStatsTxMSUAS15MinTr": tnSdhStatsTxMSUAS15MinTr,
       "tnSdhStatsRxRSUAS15MinTr": tnSdhStatsRxRSUAS15MinTr,
       "tnSdhStatsTxRSUAS15MinTr": tnSdhStatsTxRSUAS15MinTr,
       "tnSdhStatsSTM256RxRSEB1DayTr": tnSdhStatsSTM256RxRSEB1DayTr,
       "tnSdhStatsSTM64RxRSEB1DayTr": tnSdhStatsSTM64RxRSEB1DayTr,
       "tnSdhStatsSTM16RxRSEB1DayTr": tnSdhStatsSTM16RxRSEB1DayTr,
       "tnSdhStatsSTM4RxRSEB1DayTr": tnSdhStatsSTM4RxRSEB1DayTr,
       "tnSdhStatsSTM1RxRSEB1DayTr": tnSdhStatsSTM1RxRSEB1DayTr,
       "tnSdhStatsRxRSES1DayTr": tnSdhStatsRxRSES1DayTr,
       "tnSdhStatsRxRSSES1DayTr": tnSdhStatsRxRSSES1DayTr,
       "tnSdhStatsSTM256RxMSEB1DayTr": tnSdhStatsSTM256RxMSEB1DayTr,
       "tnSdhStatsSTM64RxMSEB1DayTr": tnSdhStatsSTM64RxMSEB1DayTr,
       "tnSdhStatsSTM16RxMSEB1DayTr": tnSdhStatsSTM16RxMSEB1DayTr,
       "tnSdhStatsSTM4RxMSEB1DayTr": tnSdhStatsSTM4RxMSEB1DayTr,
       "tnSdhStatsSTM1RxMSEB1DayTr": tnSdhStatsSTM1RxMSEB1DayTr,
       "tnSdhStatsRxMSES1DayTr": tnSdhStatsRxMSES1DayTr,
       "tnSdhStatsRxMSSES1DayTr": tnSdhStatsRxMSSES1DayTr,
       "tnSdhStatsRxMSUAS1DayTr": tnSdhStatsRxMSUAS1DayTr,
       "tnSdhStatsSTM256TxRSEB1DayTr": tnSdhStatsSTM256TxRSEB1DayTr,
       "tnSdhStatsSTM64TxRSEB1DayTr": tnSdhStatsSTM64TxRSEB1DayTr,
       "tnSdhStatsSTM16TxRSEB1DayTr": tnSdhStatsSTM16TxRSEB1DayTr,
       "tnSdhStatsSTM4TxRSEB1DayTr": tnSdhStatsSTM4TxRSEB1DayTr,
       "tnSdhStatsSTM1TxRSEB1DayTr": tnSdhStatsSTM1TxRSEB1DayTr,
       "tnSdhStatsTxRSES1DayTr": tnSdhStatsTxRSES1DayTr,
       "tnSdhStatsTxRSSES1DayTr": tnSdhStatsTxRSSES1DayTr,
       "tnSdhStatsSTM256TxMSEB1DayTr": tnSdhStatsSTM256TxMSEB1DayTr,
       "tnSdhStatsSTM64TxMSEB1DayTr": tnSdhStatsSTM64TxMSEB1DayTr,
       "tnSdhStatsSTM16TxMSEB1DayTr": tnSdhStatsSTM16TxMSEB1DayTr,
       "tnSdhStatsSTM4TxMSEB1DayTr": tnSdhStatsSTM4TxMSEB1DayTr,
       "tnSdhStatsSTM1TxMSEB1DayTr": tnSdhStatsSTM1TxMSEB1DayTr,
       "tnSdhStatsTxMSES1DayTr": tnSdhStatsTxMSES1DayTr,
       "tnSdhStatsTxMSSES1DayTr": tnSdhStatsTxMSSES1DayTr,
       "tnSdhStatsTxMSUAS1DayTr": tnSdhStatsTxMSUAS1DayTr,
       "tnSdhStatsRxRSUAS1DayTr": tnSdhStatsRxRSUAS1DayTr,
       "tnSdhStatsTxRSUAS1DayTr": tnSdhStatsTxRSUAS1DayTr,
       "tnSdhStatsSTM256RxRSEB15MinRtr": tnSdhStatsSTM256RxRSEB15MinRtr,
       "tnSdhStatsSTM64RxRSEB15MinRtr": tnSdhStatsSTM64RxRSEB15MinRtr,
       "tnSdhStatsSTM16RxRSEB15MinRtr": tnSdhStatsSTM16RxRSEB15MinRtr,
       "tnSdhStatsSTM4RxRSEB15MinRtr": tnSdhStatsSTM4RxRSEB15MinRtr,
       "tnSdhStatsSTM1RxRSEB15MinRtr": tnSdhStatsSTM1RxRSEB15MinRtr,
       "tnSdhStatsRxRSES15MinRtr": tnSdhStatsRxRSES15MinRtr,
       "tnSdhStatsRxRSSES15MinRtr": tnSdhStatsRxRSSES15MinRtr,
       "tnSdhStatsSTM256RxMSEB15MinRtr": tnSdhStatsSTM256RxMSEB15MinRtr,
       "tnSdhStatsSTM64RxMSEB15MinRtr": tnSdhStatsSTM64RxMSEB15MinRtr,
       "tnSdhStatsSTM16RxMSEB15MinRtr": tnSdhStatsSTM16RxMSEB15MinRtr,
       "tnSdhStatsSTM4RxMSEB15MinRtr": tnSdhStatsSTM4RxMSEB15MinRtr,
       "tnSdhStatsSTM1RxMSEB15MinRtr": tnSdhStatsSTM1RxMSEB15MinRtr,
       "tnSdhStatsRxMSES15MinRtr": tnSdhStatsRxMSES15MinRtr,
       "tnSdhStatsRxMSSES15MinRtr": tnSdhStatsRxMSSES15MinRtr,
       "tnSdhStatsRxMSUAS15MinRtr": tnSdhStatsRxMSUAS15MinRtr,
       "tnSdhStatsSTM256TxRSEB15MinRtr": tnSdhStatsSTM256TxRSEB15MinRtr,
       "tnSdhStatsSTM64TxRSEB15MinRtr": tnSdhStatsSTM64TxRSEB15MinRtr,
       "tnSdhStatsSTM16TxRSEB15MinRtr": tnSdhStatsSTM16TxRSEB15MinRtr,
       "tnSdhStatsSTM4TxRSEB15MinRtr": tnSdhStatsSTM4TxRSEB15MinRtr,
       "tnSdhStatsSTM1TxRSEB15MinRtr": tnSdhStatsSTM1TxRSEB15MinRtr,
       "tnSdhStatsTxRSES15MinRtr": tnSdhStatsTxRSES15MinRtr,
       "tnSdhStatsTxRSSES15MinRtr": tnSdhStatsTxRSSES15MinRtr,
       "tnSdhStatsSTM256TxMSEB15MinRtr": tnSdhStatsSTM256TxMSEB15MinRtr,
       "tnSdhStatsSTM64TxMSEB15MinRtr": tnSdhStatsSTM64TxMSEB15MinRtr,
       "tnSdhStatsSTM16TxMSEB15MinRtr": tnSdhStatsSTM16TxMSEB15MinRtr,
       "tnSdhStatsSTM4TxMSEB15MinRtr": tnSdhStatsSTM4TxMSEB15MinRtr,
       "tnSdhStatsSTM1TxMSEB15MinRtr": tnSdhStatsSTM1TxMSEB15MinRtr,
       "tnSdhStatsTxMSES15MinRtr": tnSdhStatsTxMSES15MinRtr,
       "tnSdhStatsTxMSSES15MinRtr": tnSdhStatsTxMSSES15MinRtr,
       "tnSdhStatsTxMSUAS15MinRtr": tnSdhStatsTxMSUAS15MinRtr,
       "tnSdhStatsRxRSUAS15MinRtr": tnSdhStatsRxRSUAS15MinRtr,
       "tnSdhStatsTxRSUAS15MinRtr": tnSdhStatsTxRSUAS15MinRtr,
       "tnSdhStatsSTM256RxMSFEEB15MinTr": tnSdhStatsSTM256RxMSFEEB15MinTr,
       "tnSdhStatsSTM64RxMSFEEB15MinTr": tnSdhStatsSTM64RxMSFEEB15MinTr,
       "tnSdhStatsSTM16RxMSFEEB15MinTr": tnSdhStatsSTM16RxMSFEEB15MinTr,
       "tnSdhStatsSTM4RxMSFEEB15MinTr": tnSdhStatsSTM4RxMSFEEB15MinTr,
       "tnSdhStatsSTM1RxMSFEEB15MinTr": tnSdhStatsSTM1RxMSFEEB15MinTr,
       "tnSdhStatsRxMSFEES15MinTr": tnSdhStatsRxMSFEES15MinTr,
       "tnSdhStatsRxMSFESES15MinTr": tnSdhStatsRxMSFESES15MinTr,
       "tnSdhStatsRxMSFEUAS15MinTr": tnSdhStatsRxMSFEUAS15MinTr,
       "tnSdhStatsSTM256RxMSFEEB1DayTr": tnSdhStatsSTM256RxMSFEEB1DayTr,
       "tnSdhStatsSTM64RxMSFEEB1DayTr": tnSdhStatsSTM64RxMSFEEB1DayTr,
       "tnSdhStatsSTM16RxMSFEEB1DayTr": tnSdhStatsSTM16RxMSFEEB1DayTr,
       "tnSdhStatsSTM4RxMSFEEB1DayTr": tnSdhStatsSTM4RxMSFEEB1DayTr,
       "tnSdhStatsSTM1RxMSFEEB1DayTr": tnSdhStatsSTM1RxMSFEEB1DayTr,
       "tnSdhStatsRxMSFEES1DayTr": tnSdhStatsRxMSFEES1DayTr,
       "tnSdhStatsRxMSFESES1DayTr": tnSdhStatsRxMSFESES1DayTr,
       "tnSdhStatsRxMSFEUAS1DayTr": tnSdhStatsRxMSFEUAS1DayTr,
       "tnSdhStatsSTM256RxMSFEEB15MinRtr": tnSdhStatsSTM256RxMSFEEB15MinRtr,
       "tnSdhStatsSTM64RxMSFEEB15MinRtr": tnSdhStatsSTM64RxMSFEEB15MinRtr,
       "tnSdhStatsSTM16RxMSFEEB15MinRtr": tnSdhStatsSTM16RxMSFEEB15MinRtr,
       "tnSdhStatsSTM4RxMSFEEB15MinRtr": tnSdhStatsSTM4RxMSFEEB15MinRtr,
       "tnSdhStatsSTM1RxMSFEEB15MinRtr": tnSdhStatsSTM1RxMSFEEB15MinRtr,
       "tnSdhStatsRxMSFEES15MinRtr": tnSdhStatsRxMSFEES15MinRtr,
       "tnSdhStatsRxMSFESES15MinRtr": tnSdhStatsRxMSFESES15MinRtr,
       "tnSdhStatsRxMSFEUAS15MinRtr": tnSdhStatsRxMSFEUAS15MinRtr,
       "tnStatisticsDwScalars": tnStatisticsDwScalars,
       "tnDw64BitStatsOtu1RxRSCorrCnt15MinTr": tnDw64BitStatsOtu1RxRSCorrCnt15MinTr,
       "tnDw64BitStatsOtu2RxRSCorrCnt15MinTr": tnDw64BitStatsOtu2RxRSCorrCnt15MinTr,
       "tnDw64BitStatsOtu3RxRSCorrCnt15MinTr": tnDw64BitStatsOtu3RxRSCorrCnt15MinTr,
       "tnDw64BitStatsOtu4RxRSCorrCnt15MinTr": tnDw64BitStatsOtu4RxRSCorrCnt15MinTr,
       "tnDw64BitStatsOtu1RxRSUncorrCnt15MinTr": tnDw64BitStatsOtu1RxRSUncorrCnt15MinTr,
       "tnDw64BitStatsOtu2RxRSUncorrCnt15MinTr": tnDw64BitStatsOtu2RxRSUncorrCnt15MinTr,
       "tnDw64BitStatsOtu3RxRSUncorrCnt15MinTr": tnDw64BitStatsOtu3RxRSUncorrCnt15MinTr,
       "tnDw64BitStatsOtu4RxRSUncorrCnt15MinTr": tnDw64BitStatsOtu4RxRSUncorrCnt15MinTr,
       "tnDw64BitStatsOtu1RxSMBIP8ErrCnt15MinTr": tnDw64BitStatsOtu1RxSMBIP8ErrCnt15MinTr,
       "tnDw64BitStatsOtu2RxSMBIP8ErrCnt15MinTr": tnDw64BitStatsOtu2RxSMBIP8ErrCnt15MinTr,
       "tnDw64BitStatsOtu3RxSMBIP8ErrCnt15MinTr": tnDw64BitStatsOtu3RxSMBIP8ErrCnt15MinTr,
       "tnDw64BitStatsOtu4RxSMBIP8ErrCnt15MinTr": tnDw64BitStatsOtu4RxSMBIP8ErrCnt15MinTr,
       "tnDw64BitStatsOdu1RxPMBIP8ErrCnt15MinTr": tnDw64BitStatsOdu1RxPMBIP8ErrCnt15MinTr,
       "tnDw64BitStatsOdu2RxPMBIP8ErrCnt15MinTr": tnDw64BitStatsOdu2RxPMBIP8ErrCnt15MinTr,
       "tnDw64BitStatsOdu3RxPMBIP8ErrCnt15MinTr": tnDw64BitStatsOdu3RxPMBIP8ErrCnt15MinTr,
       "tnDw64BitStatsOdu4RxPMBIP8ErrCnt15MinTr": tnDw64BitStatsOdu4RxPMBIP8ErrCnt15MinTr,
       "tnDw64BitStatsRxSMES15MinTr": tnDw64BitStatsRxSMES15MinTr,
       "tnDw64BitStatsRxPMES15MinTr": tnDw64BitStatsRxPMES15MinTr,
       "tnDw64BitStatsRxSMSES15MinTr": tnDw64BitStatsRxSMSES15MinTr,
       "tnDw64BitStatsRxPMSES15MinTr": tnDw64BitStatsRxPMSES15MinTr,
       "tnDw64BitStatsRxSMUAS15MinTr": tnDw64BitStatsRxSMUAS15MinTr,
       "tnDw64BitStatsRxPMUAS15MinTr": tnDw64BitStatsRxPMUAS15MinTr,
       "tnDw64BitStatsOtu1RxRSCorrCnt1DayTr": tnDw64BitStatsOtu1RxRSCorrCnt1DayTr,
       "tnDw64BitStatsOtu2RxRSCorrCnt1DayTr": tnDw64BitStatsOtu2RxRSCorrCnt1DayTr,
       "tnDw64BitStatsOtu3RxRSCorrCnt1DayTr": tnDw64BitStatsOtu3RxRSCorrCnt1DayTr,
       "tnDw64BitStatsOtu4RxRSCorrCnt1DayTr": tnDw64BitStatsOtu4RxRSCorrCnt1DayTr,
       "tnDw64BitStatsOtu1RxRSUncorrCnt1DayTr": tnDw64BitStatsOtu1RxRSUncorrCnt1DayTr,
       "tnDw64BitStatsOtu2RxRSUncorrCnt1DayTr": tnDw64BitStatsOtu2RxRSUncorrCnt1DayTr,
       "tnDw64BitStatsOtu3RxRSUncorrCnt1DayTr": tnDw64BitStatsOtu3RxRSUncorrCnt1DayTr,
       "tnDw64BitStatsOtu4RxRSUncorrCnt1DayTr": tnDw64BitStatsOtu4RxRSUncorrCnt1DayTr,
       "tnDw64BitStatsOtu1RxSMBIP8ErrCnt1DayTr": tnDw64BitStatsOtu1RxSMBIP8ErrCnt1DayTr,
       "tnDw64BitStatsOtu2RxSMBIP8ErrCnt1DayTr": tnDw64BitStatsOtu2RxSMBIP8ErrCnt1DayTr,
       "tnDw64BitStatsOtu3RxSMBIP8ErrCnt1DayTr": tnDw64BitStatsOtu3RxSMBIP8ErrCnt1DayTr,
       "tnDw64BitStatsOtu4RxSMBIP8ErrCnt1DayTr": tnDw64BitStatsOtu4RxSMBIP8ErrCnt1DayTr,
       "tnDw64BitStatsOdu1RxPMBIP8ErrCnt1DayTr": tnDw64BitStatsOdu1RxPMBIP8ErrCnt1DayTr,
       "tnDw64BitStatsOdu2RxPMBIP8ErrCnt1DayTr": tnDw64BitStatsOdu2RxPMBIP8ErrCnt1DayTr,
       "tnDw64BitStatsOdu3RxPMBIP8ErrCnt1DayTr": tnDw64BitStatsOdu3RxPMBIP8ErrCnt1DayTr,
       "tnDw64BitStatsOdu4RxPMBIP8ErrCnt1DayTr": tnDw64BitStatsOdu4RxPMBIP8ErrCnt1DayTr,
       "tnDw64BitStatsRxSMES1DayTr": tnDw64BitStatsRxSMES1DayTr,
       "tnDw64BitStatsRxPMES1DayTr": tnDw64BitStatsRxPMES1DayTr,
       "tnDw64BitStatsRxSMSES1DayTr": tnDw64BitStatsRxSMSES1DayTr,
       "tnDw64BitStatsRxPMSES1DayTr": tnDw64BitStatsRxPMSES1DayTr,
       "tnDw64BitStatsRxSMUAS1DayTr": tnDw64BitStatsRxSMUAS1DayTr,
       "tnDw64BitStatsRxPMUAS1DayTr": tnDw64BitStatsRxPMUAS1DayTr,
       "tnDw64BitStatsOtu1RxRSCorrCnt15MinRtr": tnDw64BitStatsOtu1RxRSCorrCnt15MinRtr,
       "tnDw64BitStatsOtu2RxRSCorrCnt15MinRtr": tnDw64BitStatsOtu2RxRSCorrCnt15MinRtr,
       "tnDw64BitStatsOtu3RxRSCorrCnt15MinRtr": tnDw64BitStatsOtu3RxRSCorrCnt15MinRtr,
       "tnDw64BitStatsOtu4RxRSCorrCnt15MinRtr": tnDw64BitStatsOtu4RxRSCorrCnt15MinRtr,
       "tnDw64BitStatsOtu1RxRSUncorrCnt15MinRtr": tnDw64BitStatsOtu1RxRSUncorrCnt15MinRtr,
       "tnDw64BitStatsOtu2RxRSUncorrCnt15MinRtr": tnDw64BitStatsOtu2RxRSUncorrCnt15MinRtr,
       "tnDw64BitStatsOtu3RxRSUncorrCnt15MinRtr": tnDw64BitStatsOtu3RxRSUncorrCnt15MinRtr,
       "tnDw64BitStatsOtu4RxRSUncorrCnt15MinRtr": tnDw64BitStatsOtu4RxRSUncorrCnt15MinRtr,
       "tnDw64BitStatsOtu1RxSMBIP8ErrCnt15MinRtr": tnDw64BitStatsOtu1RxSMBIP8ErrCnt15MinRtr,
       "tnDw64BitStatsOtu2RxSMBIP8ErrCnt15MinRtr": tnDw64BitStatsOtu2RxSMBIP8ErrCnt15MinRtr,
       "tnDw64BitStatsOtu3RxSMBIP8ErrCnt15MinRtr": tnDw64BitStatsOtu3RxSMBIP8ErrCnt15MinRtr,
       "tnDw64BitStatsOtu4RxSMBIP8ErrCnt15MinRtr": tnDw64BitStatsOtu4RxSMBIP8ErrCnt15MinRtr,
       "tnDw64BitStatsOdu1RxPMBIP8ErrCnt15MinRtr": tnDw64BitStatsOdu1RxPMBIP8ErrCnt15MinRtr,
       "tnDw64BitStatsOdu2RxPMBIP8ErrCnt15MinRtr": tnDw64BitStatsOdu2RxPMBIP8ErrCnt15MinRtr,
       "tnDw64BitStatsOdu3RxPMBIP8ErrCnt15MinRtr": tnDw64BitStatsOdu3RxPMBIP8ErrCnt15MinRtr,
       "tnDw64BitStatsOdu4RxPMBIP8ErrCnt15MinRtr": tnDw64BitStatsOdu4RxPMBIP8ErrCnt15MinRtr,
       "tnDw64BitStatsRxSMES15MinRtr": tnDw64BitStatsRxSMES15MinRtr,
       "tnDw64BitStatsRxPMES15MinRtr": tnDw64BitStatsRxPMES15MinRtr,
       "tnDw64BitStatsRxSMSES15MinRtr": tnDw64BitStatsRxSMSES15MinRtr,
       "tnDw64BitStatsRxPMSES15MinRtr": tnDw64BitStatsRxPMSES15MinRtr,
       "tnDw64BitStatsRxSMUAS15MinRtr": tnDw64BitStatsRxSMUAS15MinRtr,
       "tnDw64BitStatsRxPMUAS15MinRtr": tnDw64BitStatsRxPMUAS15MinRtr,
       "tnDwStatsOtu1RxSMFEBIP8ErrCnt15MinTr": tnDwStatsOtu1RxSMFEBIP8ErrCnt15MinTr,
       "tnDwStatsOtu2RxSMFEBIP8ErrCnt15MinTr": tnDwStatsOtu2RxSMFEBIP8ErrCnt15MinTr,
       "tnDwStatsOtu3RxSMFEBIP8ErrCnt15MinTr": tnDwStatsOtu3RxSMFEBIP8ErrCnt15MinTr,
       "tnDwStatsOtu4RxSMFEBIP8ErrCnt15MinTr": tnDwStatsOtu4RxSMFEBIP8ErrCnt15MinTr,
       "tnDwStatsOdu1RxPMFEBIP8ErrCnt15MinTr": tnDwStatsOdu1RxPMFEBIP8ErrCnt15MinTr,
       "tnDwStatsOdu2RxPMFEBIP8ErrCnt15MinTr": tnDwStatsOdu2RxPMFEBIP8ErrCnt15MinTr,
       "tnDwStatsOdu3RxPMFEBIP8ErrCnt15MinTr": tnDwStatsOdu3RxPMFEBIP8ErrCnt15MinTr,
       "tnDwStatsOdu4RxPMFEBIP8ErrCnt15MinTr": tnDwStatsOdu4RxPMFEBIP8ErrCnt15MinTr,
       "tnDwStatsRxSMFEES15MinTr": tnDwStatsRxSMFEES15MinTr,
       "tnDwStatsRxPMFEES15MinTr": tnDwStatsRxPMFEES15MinTr,
       "tnDwStatsRxSMFESES15MinTr": tnDwStatsRxSMFESES15MinTr,
       "tnDwStatsRxPMFESES15MinTr": tnDwStatsRxPMFESES15MinTr,
       "tnDwStatsRxSMFEUAS15MinTr": tnDwStatsRxSMFEUAS15MinTr,
       "tnDwStatsRxPMFEUAS15MinTr": tnDwStatsRxPMFEUAS15MinTr,
       "tnDwStatsRxSMBIAES15MinTr": tnDwStatsRxSMBIAES15MinTr,
       "tnDwStatsRxSMIAES15MinTr": tnDwStatsRxSMIAES15MinTr,
       "tnDwStatsRxBERPreFEC15MinTr": tnDwStatsRxBERPreFEC15MinTr,
       "tnDwStatsRxBERPostFEC15MinTr": tnDwStatsRxBERPostFEC15MinTr,
       "tnDwStatsOtu1RxSMFEBIP8ErrCnt1DayTr": tnDwStatsOtu1RxSMFEBIP8ErrCnt1DayTr,
       "tnDwStatsOtu2RxSMFEBIP8ErrCnt1DayTr": tnDwStatsOtu2RxSMFEBIP8ErrCnt1DayTr,
       "tnDwStatsOtu3RxSMFEBIP8ErrCnt1DayTr": tnDwStatsOtu3RxSMFEBIP8ErrCnt1DayTr,
       "tnDwStatsOtu4RxSMFEBIP8ErrCnt1DayTr": tnDwStatsOtu4RxSMFEBIP8ErrCnt1DayTr,
       "tnDwStatsOdu1RxPMFEBIP8ErrCnt1DayTr": tnDwStatsOdu1RxPMFEBIP8ErrCnt1DayTr,
       "tnDwStatsOdu2RxPMFEBIP8ErrCnt1DayTr": tnDwStatsOdu2RxPMFEBIP8ErrCnt1DayTr,
       "tnDwStatsOdu3RxPMFEBIP8ErrCnt1DayTr": tnDwStatsOdu3RxPMFEBIP8ErrCnt1DayTr,
       "tnDwStatsOdu4RxPMFEBIP8ErrCnt1DayTr": tnDwStatsOdu4RxPMFEBIP8ErrCnt1DayTr,
       "tnDwStatsRxSMFEES1DayTr": tnDwStatsRxSMFEES1DayTr,
       "tnDwStatsRxPMFEES1DayTr": tnDwStatsRxPMFEES1DayTr,
       "tnDwStatsRxSMFESES1DayTr": tnDwStatsRxSMFESES1DayTr,
       "tnDwStatsRxPMFESES1DayTr": tnDwStatsRxPMFESES1DayTr,
       "tnDwStatsRxSMFEUAS1DayTr": tnDwStatsRxSMFEUAS1DayTr,
       "tnDwStatsRxPMFEUAS1DayTr": tnDwStatsRxPMFEUAS1DayTr,
       "tnDwStatsRxSMBIAES1DayTr": tnDwStatsRxSMBIAES1DayTr,
       "tnDwStatsRxSMIAES1DayTr": tnDwStatsRxSMIAES1DayTr,
       "tnDwStatsRxBERPreFEC1DayTr": tnDwStatsRxBERPreFEC1DayTr,
       "tnDwStatsRxBERPostFEC1DayTr": tnDwStatsRxBERPostFEC1DayTr,
       "tnDwStatsOtu1RxSMFEBIP8ErrCnt15MinRtr": tnDwStatsOtu1RxSMFEBIP8ErrCnt15MinRtr,
       "tnDwStatsOtu2RxSMFEBIP8ErrCnt15MinRtr": tnDwStatsOtu2RxSMFEBIP8ErrCnt15MinRtr,
       "tnDwStatsOtu3RxSMFEBIP8ErrCnt15MinRtr": tnDwStatsOtu3RxSMFEBIP8ErrCnt15MinRtr,
       "tnDwStatsOtu4RxSMFEBIP8ErrCnt15MinRtr": tnDwStatsOtu4RxSMFEBIP8ErrCnt15MinRtr,
       "tnDwStatsOdu1RxPMFEBIP8ErrCnt15MinRtr": tnDwStatsOdu1RxPMFEBIP8ErrCnt15MinRtr,
       "tnDwStatsOdu2RxPMFEBIP8ErrCnt15MinRtr": tnDwStatsOdu2RxPMFEBIP8ErrCnt15MinRtr,
       "tnDwStatsOdu3RxPMFEBIP8ErrCnt15MinRtr": tnDwStatsOdu3RxPMFEBIP8ErrCnt15MinRtr,
       "tnDwStatsOdu4RxPMFEBIP8ErrCnt15MinRtr": tnDwStatsOdu4RxPMFEBIP8ErrCnt15MinRtr,
       "tnDwStatsRxSMFEES15MinRtr": tnDwStatsRxSMFEES15MinRtr,
       "tnDwStatsRxPMFEES15MinRtr": tnDwStatsRxPMFEES15MinRtr,
       "tnDwStatsRxSMFESES15MinRtr": tnDwStatsRxSMFESES15MinRtr,
       "tnDwStatsRxPMFESES15MinRtr": tnDwStatsRxPMFESES15MinRtr,
       "tnDwStatsRxSMFEUAS15MinRtr": tnDwStatsRxSMFEUAS15MinRtr,
       "tnDwStatsRxPMFEUAS15MinRtr": tnDwStatsRxPMFEUAS15MinRtr,
       "tnDwStatsRxSMBIAES15MinRtr": tnDwStatsRxSMBIAES15MinRtr,
       "tnDwStatsRxSMIAES15MinRtr": tnDwStatsRxSMIAES15MinRtr,
       "tnDwStatsRxBERPreFEC15MinRtr": tnDwStatsRxBERPreFEC15MinRtr,
       "tnDwStatsRxBERPostFEC15MinRtr": tnDwStatsRxBERPostFEC15MinRtr,
       "tnStatisticsPcsScalars": tnStatisticsPcsScalars,
       "tnPcsStats100GBERxCV15MinTr": tnPcsStats100GBERxCV15MinTr,
       "tnPcsStats40GBERxCV15MinTr": tnPcsStats40GBERxCV15MinTr,
       "tnPcsStats10GBERxCV15MinTr": tnPcsStats10GBERxCV15MinTr,
       "tnPcsStatsGBERxCV15MinTr": tnPcsStatsGBERxCV15MinTr,
       "tnPcsStats16GFCRxCV15MinTr": tnPcsStats16GFCRxCV15MinTr,
       "tnPcsStats10GFCRxCV15MinTr": tnPcsStats10GFCRxCV15MinTr,
       "tnPcsStats8GFCRxCV15MinTr": tnPcsStats8GFCRxCV15MinTr,
       "tnPcsStats4GFCRxCV15MinTr": tnPcsStats4GFCRxCV15MinTr,
       "tnPcsStats2GFCRxCV15MinTr": tnPcsStats2GFCRxCV15MinTr,
       "tnPcsStatsGFCRxCV15MinTr": tnPcsStatsGFCRxCV15MinTr,
       "tnPcsStatsRxES15MinTr": tnPcsStatsRxES15MinTr,
       "tnPcsStatsRxSES15MinTr": tnPcsStatsRxSES15MinTr,
       "tnPcsStatsRxSEFS15MinTr": tnPcsStatsRxSEFS15MinTr,
       "tnPcsStats100GBERxCV1DayTr": tnPcsStats100GBERxCV1DayTr,
       "tnPcsStats40GBERxCV1DayTr": tnPcsStats40GBERxCV1DayTr,
       "tnPcsStats10GBERxCV1DayTr": tnPcsStats10GBERxCV1DayTr,
       "tnPcsStatsGBERxCV1DayTr": tnPcsStatsGBERxCV1DayTr,
       "tnPcsStats16GFCRxCV1DayTr": tnPcsStats16GFCRxCV1DayTr,
       "tnPcsStats10GFCRxCV1DayTr": tnPcsStats10GFCRxCV1DayTr,
       "tnPcsStats8GFCRxCV1DayTr": tnPcsStats8GFCRxCV1DayTr,
       "tnPcsStats4GFCRxCV1DayTr": tnPcsStats4GFCRxCV1DayTr,
       "tnPcsStats2GFCRxCV1DayTr": tnPcsStats2GFCRxCV1DayTr,
       "tnPcsStatsGFCRxCV1DayTr": tnPcsStatsGFCRxCV1DayTr,
       "tnPcsStatsRxES1DayTr": tnPcsStatsRxES1DayTr,
       "tnPcsStatsRxSES1DayTr": tnPcsStatsRxSES1DayTr,
       "tnPcsStatsRxSEFS1DayTr": tnPcsStatsRxSEFS1DayTr,
       "tnPcsStats100GBERxCV15MinRtr": tnPcsStats100GBERxCV15MinRtr,
       "tnPcsStats40GBERxCV15MinRtr": tnPcsStats40GBERxCV15MinRtr,
       "tnPcsStats10GBERxCV15MinRtr": tnPcsStats10GBERxCV15MinRtr,
       "tnPcsStatsGBERxCV15MinRtr": tnPcsStatsGBERxCV15MinRtr,
       "tnPcsStats16GFCRxCV15MinRtr": tnPcsStats16GFCRxCV15MinRtr,
       "tnPcsStats10GFCRxCV15MinRtr": tnPcsStats10GFCRxCV15MinRtr,
       "tnPcsStats8GFCRxCV15MinRtr": tnPcsStats8GFCRxCV15MinRtr,
       "tnPcsStats4GFCRxCV15MinRtr": tnPcsStats4GFCRxCV15MinRtr,
       "tnPcsStats2GFCRxCV15MinRtr": tnPcsStats2GFCRxCV15MinRtr,
       "tnPcsStatsGFCRxCV15MinRtr": tnPcsStatsGFCRxCV15MinRtr,
       "tnPcsStatsRxES15MinRtr": tnPcsStatsRxES15MinRtr,
       "tnPcsStatsRxSES15MinRtr": tnPcsStatsRxSES15MinRtr,
       "tnPcsStatsRxSEFS15MinRtr": tnPcsStatsRxSEFS15MinRtr,
       "tnPcsStats100GBETxCV15MinTr": tnPcsStats100GBETxCV15MinTr,
       "tnPcsStats40GBETxCV15MinTr": tnPcsStats40GBETxCV15MinTr,
       "tnPcsStats10GBETxCV15MinTr": tnPcsStats10GBETxCV15MinTr,
       "tnPcsStatsGBETxCV15MinTr": tnPcsStatsGBETxCV15MinTr,
       "tnPcsStats16GFCTxCV15MinTr": tnPcsStats16GFCTxCV15MinTr,
       "tnPcsStats10GFCTxCV15MinTr": tnPcsStats10GFCTxCV15MinTr,
       "tnPcsStats8GFCTxCV15MinTr": tnPcsStats8GFCTxCV15MinTr,
       "tnPcsStats4GFCTxCV15MinTr": tnPcsStats4GFCTxCV15MinTr,
       "tnPcsStats2GFCTxCV15MinTr": tnPcsStats2GFCTxCV15MinTr,
       "tnPcsStatsGFCTxCV15MinTr": tnPcsStatsGFCTxCV15MinTr,
       "tnPcsStatsTxES15MinTr": tnPcsStatsTxES15MinTr,
       "tnPcsStatsTxSES15MinTr": tnPcsStatsTxSES15MinTr,
       "tnPcsStatsTxSEFS15MinTr": tnPcsStatsTxSEFS15MinTr,
       "tnPcsStats100GBETxCV1DayTr": tnPcsStats100GBETxCV1DayTr,
       "tnPcsStats40GBETxCV1DayTr": tnPcsStats40GBETxCV1DayTr,
       "tnPcsStats10GBETxCV1DayTr": tnPcsStats10GBETxCV1DayTr,
       "tnPcsStatsGBETxCV1DayTr": tnPcsStatsGBETxCV1DayTr,
       "tnPcsStats16GFCTxCV1DayTr": tnPcsStats16GFCTxCV1DayTr,
       "tnPcsStats10GFCTxCV1DayTr": tnPcsStats10GFCTxCV1DayTr,
       "tnPcsStats8GFCTxCV1DayTr": tnPcsStats8GFCTxCV1DayTr,
       "tnPcsStats4GFCTxCV1DayTr": tnPcsStats4GFCTxCV1DayTr,
       "tnPcsStats2GFCTxCV1DayTr": tnPcsStats2GFCTxCV1DayTr,
       "tnPcsStatsGFCTxCV1DayTr": tnPcsStatsGFCTxCV1DayTr,
       "tnPcsStatsTxES1DayTr": tnPcsStatsTxES1DayTr,
       "tnPcsStatsTxSES1DayTr": tnPcsStatsTxSES1DayTr,
       "tnPcsStatsTxSEFS1DayTr": tnPcsStatsTxSEFS1DayTr,
       "tnPcsStats100GBETxCV15MinRtr": tnPcsStats100GBETxCV15MinRtr,
       "tnPcsStats40GBETxCV15MinRtr": tnPcsStats40GBETxCV15MinRtr,
       "tnPcsStats10GBETxCV15MinRtr": tnPcsStats10GBETxCV15MinRtr,
       "tnPcsStatsGBETxCV15MinRtr": tnPcsStatsGBETxCV15MinRtr,
       "tnPcsStats16GFCTxCV15MinRtr": tnPcsStats16GFCTxCV15MinRtr,
       "tnPcsStats10GFCTxCV15MinRtr": tnPcsStats10GFCTxCV15MinRtr,
       "tnPcsStats8GFCTxCV15MinRtr": tnPcsStats8GFCTxCV15MinRtr,
       "tnPcsStats4GFCTxCV15MinRtr": tnPcsStats4GFCTxCV15MinRtr,
       "tnPcsStats2GFCTxCV15MinRtr": tnPcsStats2GFCTxCV15MinRtr,
       "tnPcsStatsGFCTxCV15MinRtr": tnPcsStatsGFCTxCV15MinRtr,
       "tnPcsStatsTxES15MinRtr": tnPcsStatsTxES15MinRtr,
       "tnPcsStatsTxSES15MinRtr": tnPcsStatsTxSES15MinRtr,
       "tnPcsStatsTxSEFS15MinRtr": tnPcsStatsTxSEFS15MinRtr,
       "tnStatisticsOthOduTcmScalars": tnStatisticsOthOduTcmScalars,
       "tnOthOdu0StatsTcmNeRxBIP8ErrCnt15MinTr": tnOthOdu0StatsTcmNeRxBIP8ErrCnt15MinTr,
       "tnOthOdu0StatsTcmNeRxBIP8ErrCnt15MinRtr": tnOthOdu0StatsTcmNeRxBIP8ErrCnt15MinRtr,
       "tnOthOdu0StatsTcmNeRxBIP8ErrCnt1DayTr": tnOthOdu0StatsTcmNeRxBIP8ErrCnt1DayTr,
       "tnOthOdu0StatsTcmFeRxBIP8ErrCnt15MinTr": tnOthOdu0StatsTcmFeRxBIP8ErrCnt15MinTr,
       "tnOthOdu0StatsTcmFeRxBIP8ErrCnt15MinRtr": tnOthOdu0StatsTcmFeRxBIP8ErrCnt15MinRtr,
       "tnOthOdu0StatsTcmFeRxBIP8ErrCnt1DayTr": tnOthOdu0StatsTcmFeRxBIP8ErrCnt1DayTr,
       "tnOthOdu1StatsTcmNeRxBIP8ErrCnt15MinTr": tnOthOdu1StatsTcmNeRxBIP8ErrCnt15MinTr,
       "tnOthOdu1StatsTcmNeRxBIP8ErrCnt15MinRtr": tnOthOdu1StatsTcmNeRxBIP8ErrCnt15MinRtr,
       "tnOthOdu1StatsTcmNeRxBIP8ErrCnt1DayTr": tnOthOdu1StatsTcmNeRxBIP8ErrCnt1DayTr,
       "tnOthOdu1StatsTcmFeRxBIP8ErrCnt15MinTr": tnOthOdu1StatsTcmFeRxBIP8ErrCnt15MinTr,
       "tnOthOdu1StatsTcmFeRxBIP8ErrCnt15MinRtr": tnOthOdu1StatsTcmFeRxBIP8ErrCnt15MinRtr,
       "tnOthOdu1StatsTcmFeRxBIP8ErrCnt1DayTr": tnOthOdu1StatsTcmFeRxBIP8ErrCnt1DayTr,
       "tnOthOdu2StatsTcmNeRxBIP8ErrCnt15MinTr": tnOthOdu2StatsTcmNeRxBIP8ErrCnt15MinTr,
       "tnOthOdu2StatsTcmNeRxBIP8ErrCnt15MinRtr": tnOthOdu2StatsTcmNeRxBIP8ErrCnt15MinRtr,
       "tnOthOdu2StatsTcmNeRxBIP8ErrCnt1DayTr": tnOthOdu2StatsTcmNeRxBIP8ErrCnt1DayTr,
       "tnOthOdu2StatsTcmFeRxBIP8ErrCnt15MinTr": tnOthOdu2StatsTcmFeRxBIP8ErrCnt15MinTr,
       "tnOthOdu2StatsTcmFeRxBIP8ErrCnt15MinRtr": tnOthOdu2StatsTcmFeRxBIP8ErrCnt15MinRtr,
       "tnOthOdu2StatsTcmFeRxBIP8ErrCnt1DayTr": tnOthOdu2StatsTcmFeRxBIP8ErrCnt1DayTr,
       "tnOthOdu3StatsTcmNeRxBIP8ErrCnt15MinTr": tnOthOdu3StatsTcmNeRxBIP8ErrCnt15MinTr,
       "tnOthOdu3StatsTcmNeRxBIP8ErrCnt15MinRtr": tnOthOdu3StatsTcmNeRxBIP8ErrCnt15MinRtr,
       "tnOthOdu3StatsTcmNeRxBIP8ErrCnt1DayTr": tnOthOdu3StatsTcmNeRxBIP8ErrCnt1DayTr,
       "tnOthOdu3StatsTcmFeRxBIP8ErrCnt15MinTr": tnOthOdu3StatsTcmFeRxBIP8ErrCnt15MinTr,
       "tnOthOdu3StatsTcmFeRxBIP8ErrCnt15MinRtr": tnOthOdu3StatsTcmFeRxBIP8ErrCnt15MinRtr,
       "tnOthOdu3StatsTcmFeRxBIP8ErrCnt1DayTr": tnOthOdu3StatsTcmFeRxBIP8ErrCnt1DayTr,
       "tnOthOdu4StatsTcmNeRxBIP8ErrCnt15MinTr": tnOthOdu4StatsTcmNeRxBIP8ErrCnt15MinTr,
       "tnOthOdu4StatsTcmNeRxBIP8ErrCnt15MinRtr": tnOthOdu4StatsTcmNeRxBIP8ErrCnt15MinRtr,
       "tnOthOdu4StatsTcmNeRxBIP8ErrCnt1DayTr": tnOthOdu4StatsTcmNeRxBIP8ErrCnt1DayTr,
       "tnOthOdu4StatsTcmFeRxBIP8ErrCnt15MinTr": tnOthOdu4StatsTcmFeRxBIP8ErrCnt15MinTr,
       "tnOthOdu4StatsTcmFeRxBIP8ErrCnt15MinRtr": tnOthOdu4StatsTcmFeRxBIP8ErrCnt15MinRtr,
       "tnOthOdu4StatsTcmFeRxBIP8ErrCnt1DayTr": tnOthOdu4StatsTcmFeRxBIP8ErrCnt1DayTr,
       "tnOthOdukStatsTcmNeRxES15MinTr": tnOthOdukStatsTcmNeRxES15MinTr,
       "tnOthOdukStatsTcmNeRxES15MinRtr": tnOthOdukStatsTcmNeRxES15MinRtr,
       "tnOthOdukStatsTcmNeRxES1DayTr": tnOthOdukStatsTcmNeRxES1DayTr,
       "tnOthOdukStatsTcmFeRxES15MinTr": tnOthOdukStatsTcmFeRxES15MinTr,
       "tnOthOdukStatsTcmFeRxES15MinRtr": tnOthOdukStatsTcmFeRxES15MinRtr,
       "tnOthOdukStatsTcmFeRxES1DayTr": tnOthOdukStatsTcmFeRxES1DayTr,
       "tnOthOdukStatsTcmNeRxSES15MinTr": tnOthOdukStatsTcmNeRxSES15MinTr,
       "tnOthOdukStatsTcmNeRxSES15MinRtr": tnOthOdukStatsTcmNeRxSES15MinRtr,
       "tnOthOdukStatsTcmNeRxSES1DayTr": tnOthOdukStatsTcmNeRxSES1DayTr,
       "tnOthOdukStatsTcmFeRxSES15MinTr": tnOthOdukStatsTcmFeRxSES15MinTr,
       "tnOthOdukStatsTcmFeRxSES15MinRtr": tnOthOdukStatsTcmFeRxSES15MinRtr,
       "tnOthOdukStatsTcmFeRxSES1DayTr": tnOthOdukStatsTcmFeRxSES1DayTr,
       "tnOthOdukStatsTcmNeRxUAS15MinTr": tnOthOdukStatsTcmNeRxUAS15MinTr,
       "tnOthOdukStatsTcmNeRxUAS15MinRtr": tnOthOdukStatsTcmNeRxUAS15MinRtr,
       "tnOthOdukStatsTcmNeRxUAS1DayTr": tnOthOdukStatsTcmNeRxUAS1DayTr,
       "tnOthOdukStatsTcmFeRxUAS15MinTr": tnOthOdukStatsTcmFeRxUAS15MinTr,
       "tnOthOdukStatsTcmFeRxUAS15MinRtr": tnOthOdukStatsTcmFeRxUAS15MinRtr,
       "tnOthOdukStatsTcmFeRxUAS1DayTr": tnOthOdukStatsTcmFeRxUAS1DayTr,
       "tnStatisticsLanePowerScalars": tnStatisticsLanePowerScalars,
       "tnOprLaneStatMaxPowerTr": tnOprLaneStatMaxPowerTr,
       "tnOprLaneStatMinPowerTr": tnOprLaneStatMinPowerTr,
       "tnOptLaneStatMaxPowerTr": tnOptLaneStatMaxPowerTr,
       "tnOptLaneStatMinPowerTr": tnOptLaneStatMinPowerTr,
       "tnStatisticsEncryptRxFTDScalars": tnStatisticsEncryptRxFTDScalars,
       "tnEncryptRxFailToDecryptCnt15MinTr": tnEncryptRxFailToDecryptCnt15MinTr,
       "tnEncryptRxFailToDecryptCnt15MinRtr": tnEncryptRxFailToDecryptCnt15MinRtr,
       "tnEncryptRxFailToDecryptCnt1DayTr": tnEncryptRxFailToDecryptCnt1DayTr,
       "tnEncryptRxFailToDecryptCnt1DayRtr": tnEncryptRxFailToDecryptCnt1DayRtr}
)

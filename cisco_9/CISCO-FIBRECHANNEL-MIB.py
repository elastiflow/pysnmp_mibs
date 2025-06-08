# SNMP MIB module (CISCO-FIBRECHANNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIBRECHANNEL-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:15:13 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoFibreChanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CoiIntervalType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMin", 1),
          ("oneDay", 2),
          ("thirtySeconds", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoFibreChanMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoFibreChanMIBNotifs = _CiscoFibreChanMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 0)
)
_CiscoFibreChanMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFibreChanMIBObjects = _CiscoFibreChanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1)
)
_CoiFibreChanController_ObjectIdentity = ObjectIdentity
coiFibreChanController = _CoiFibreChanController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 1)
)
_CoiFibreChanControllerTable_Object = MibTable
coiFibreChanControllerTable = _CoiFibreChanControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 1, 1)
)
if mibBuilder.loadTexts:
    coiFibreChanControllerTable.setStatus("current")
_CoiFibreChanControllerEntry_Object = MibTableRow
coiFibreChanControllerEntry = _CoiFibreChanControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 1, 1, 1)
)
coiFibreChanControllerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    coiFibreChanControllerEntry.setStatus("current")


class _CoiFibreChanControllerAdminStatus_Type(Integer32):
    """Custom type coiFibreChanControllerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_CoiFibreChanControllerAdminStatus_Type.__name__ = "Integer32"
_CoiFibreChanControllerAdminStatus_Object = MibTableColumn
coiFibreChanControllerAdminStatus = _CoiFibreChanControllerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 1, 1, 1, 1),
    _CoiFibreChanControllerAdminStatus_Type()
)
coiFibreChanControllerAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFibreChanControllerAdminStatus.setStatus("current")


class _CoiFibreChanControllerOperStatus_Type(Integer32):
    """Custom type coiFibreChanControllerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_CoiFibreChanControllerOperStatus_Type.__name__ = "Integer32"
_CoiFibreChanControllerOperStatus_Object = MibTableColumn
coiFibreChanControllerOperStatus = _CoiFibreChanControllerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 1, 1, 1, 2),
    _CoiFibreChanControllerOperStatus_Type()
)
coiFibreChanControllerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFibreChanControllerOperStatus.setStatus("current")


class _CoiFibreChanControllerLoopbackInfo_Type(Integer32):
    """Custom type coiFibreChanControllerLoopbackInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopbackNone", 0),
          ("loopbackLine", 1),
          ("loopbackInternal", 2))
    )


_CoiFibreChanControllerLoopbackInfo_Type.__name__ = "Integer32"
_CoiFibreChanControllerLoopbackInfo_Object = MibTableColumn
coiFibreChanControllerLoopbackInfo = _CoiFibreChanControllerLoopbackInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 1, 1, 1, 3),
    _CoiFibreChanControllerLoopbackInfo_Type()
)
coiFibreChanControllerLoopbackInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFibreChanControllerLoopbackInfo.setStatus("current")


class _CoiFibreChanControllerAlarmStatus_Type(Bits):
    """Custom type coiFibreChanControllerAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("los", 1),
          ("syncLoss", 2),
          ("pcsErr", 3),
          ("hiBer", 4),
          ("localFault", 5),
          ("remoteFault", 6),
          ("nos", 7),
          ("squelch", 8))
    )

_CoiFibreChanControllerAlarmStatus_Type.__name__ = "Bits"
_CoiFibreChanControllerAlarmStatus_Object = MibTableColumn
coiFibreChanControllerAlarmStatus = _CoiFibreChanControllerAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 1, 1, 1, 4),
    _CoiFibreChanControllerAlarmStatus_Type()
)
coiFibreChanControllerAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFibreChanControllerAlarmStatus.setStatus("current")
_CoiFcPm_ObjectIdentity = ObjectIdentity
coiFcPm = _CoiFcPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2)
)
_CoiFcPmCurrentTable_ObjectIdentity = ObjectIdentity
coiFcPmCurrentTable = _CoiFcPmCurrentTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 1)
)
_CoiFcPmCurrentEntry_Object = MibTableRow
coiFcPmCurrentEntry = _CoiFcPmCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 1, 1)
)
coiFcPmCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-FIBRECHANNEL-MIB", "coiFcPmCurrentIntervalType"),
)
if mibBuilder.loadTexts:
    coiFcPmCurrentEntry.setStatus("current")
_CoiFcPmCurrentIntervalType_Type = CoiIntervalType
_CoiFcPmCurrentIntervalType_Object = MibTableColumn
coiFcPmCurrentIntervalType = _CoiFcPmCurrentIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 1, 1, 1),
    _CoiFcPmCurrentIntervalType_Type()
)
coiFcPmCurrentIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmCurrentIntervalType.setStatus("current")
_CoiFcPmIfInOctets_Type = Counter64
_CoiFcPmIfInOctets_Object = MibTableColumn
coiFcPmIfInOctets = _CoiFcPmIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 1, 1, 2),
    _CoiFcPmIfInOctets_Type()
)
coiFcPmIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmIfInOctets.setStatus("current")
_CoiFcPmRxTotalPkts_Type = Counter64
_CoiFcPmRxTotalPkts_Object = MibTableColumn
coiFcPmRxTotalPkts = _CoiFcPmRxTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 1, 1, 3),
    _CoiFcPmRxTotalPkts_Type()
)
coiFcPmRxTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmRxTotalPkts.setStatus("current")
_CoiFcPmIfInErrors_Type = Counter64
_CoiFcPmIfInErrors_Object = MibTableColumn
coiFcPmIfInErrors = _CoiFcPmIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 1, 1, 4),
    _CoiFcPmIfInErrors_Type()
)
coiFcPmIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmIfInErrors.setStatus("current")
_CoiFcPmRxBadFcs_Type = Counter64
_CoiFcPmRxBadFcs_Object = MibTableColumn
coiFcPmRxBadFcs = _CoiFcPmRxBadFcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 1, 1, 5),
    _CoiFcPmRxBadFcs_Type()
)
coiFcPmRxBadFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmRxBadFcs.setStatus("current")
_CoiFcPmRxFramesTooShort_Type = Counter64
_CoiFcPmRxFramesTooShort_Object = MibTableColumn
coiFcPmRxFramesTooShort = _CoiFcPmRxFramesTooShort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 1, 1, 6),
    _CoiFcPmRxFramesTooShort_Type()
)
coiFcPmRxFramesTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmRxFramesTooShort.setStatus("current")
_CoiFcPmRxFramesTooLong_Type = Counter64
_CoiFcPmRxFramesTooLong_Object = MibTableColumn
coiFcPmRxFramesTooLong = _CoiFcPmRxFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 1, 1, 7),
    _CoiFcPmRxFramesTooLong_Type()
)
coiFcPmRxFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmRxFramesTooLong.setStatus("current")
_CoiFcPmIfOutOctets_Type = Counter64
_CoiFcPmIfOutOctets_Object = MibTableColumn
coiFcPmIfOutOctets = _CoiFcPmIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 1, 1, 8),
    _CoiFcPmIfOutOctets_Type()
)
coiFcPmIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmIfOutOctets.setStatus("current")
_CoiFcPmTxTotalPkts_Type = Counter64
_CoiFcPmTxTotalPkts_Object = MibTableColumn
coiFcPmTxTotalPkts = _CoiFcPmTxTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 1, 1, 9),
    _CoiFcPmTxTotalPkts_Type()
)
coiFcPmTxTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmTxTotalPkts.setStatus("current")
_CoiFcPmTxBadFcs_Type = Counter64
_CoiFcPmTxBadFcs_Object = MibTableColumn
coiFcPmTxBadFcs = _CoiFcPmTxBadFcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 1, 1, 10),
    _CoiFcPmTxBadFcs_Type()
)
coiFcPmTxBadFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmTxBadFcs.setStatus("current")
_CoiFcPmTxFramesTooShort_Type = Counter64
_CoiFcPmTxFramesTooShort_Object = MibTableColumn
coiFcPmTxFramesTooShort = _CoiFcPmTxFramesTooShort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 1, 1, 11),
    _CoiFcPmTxFramesTooShort_Type()
)
coiFcPmTxFramesTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmTxFramesTooShort.setStatus("current")
_CoiFcPmTxFramesTooLong_Type = Counter64
_CoiFcPmTxFramesTooLong_Object = MibTableColumn
coiFcPmTxFramesTooLong = _CoiFcPmTxFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 1, 1, 12),
    _CoiFcPmTxFramesTooLong_Type()
)
coiFcPmTxFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmTxFramesTooLong.setStatus("current")
_CoiFcCurrentPmValidData_Type = TruthValue
_CoiFcCurrentPmValidData_Object = MibTableColumn
coiFcCurrentPmValidData = _CoiFcCurrentPmValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 1, 1, 13),
    _CoiFcCurrentPmValidData_Type()
)
coiFcCurrentPmValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcCurrentPmValidData.setStatus("current")
_CoiFcPmHistoryTable_ObjectIdentity = ObjectIdentity
coiFcPmHistoryTable = _CoiFcPmHistoryTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 2)
)
_CoiFcPmHistoryEntry_Object = MibTableRow
coiFcPmHistoryEntry = _CoiFcPmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 2, 1)
)
coiFcPmHistoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-FIBRECHANNEL-MIB", "coiFcPmHistoryIntervalType"),
    (0, "CISCO-FIBRECHANNEL-MIB", "coiFcPmIntervalNumber"),
)
if mibBuilder.loadTexts:
    coiFcPmHistoryEntry.setStatus("current")
_CoiFcPmHistoryIntervalType_Type = CoiIntervalType
_CoiFcPmHistoryIntervalType_Object = MibTableColumn
coiFcPmHistoryIntervalType = _CoiFcPmHistoryIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 2, 1, 1),
    _CoiFcPmHistoryIntervalType_Type()
)
coiFcPmHistoryIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmHistoryIntervalType.setStatus("current")


class _CoiFcPmIntervalNumber_Type(Unsigned32):
    """Custom type coiFcPmIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CoiFcPmIntervalNumber_Type.__name__ = "Unsigned32"
_CoiFcPmIntervalNumber_Object = MibTableColumn
coiFcPmIntervalNumber = _CoiFcPmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 2, 1, 2),
    _CoiFcPmIntervalNumber_Type()
)
coiFcPmIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiFcPmIntervalNumber.setStatus("current")
_CoiFcPmHistoryIfInOctets_Type = Counter64
_CoiFcPmHistoryIfInOctets_Object = MibTableColumn
coiFcPmHistoryIfInOctets = _CoiFcPmHistoryIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 2, 1, 3),
    _CoiFcPmHistoryIfInOctets_Type()
)
coiFcPmHistoryIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmHistoryIfInOctets.setStatus("current")
_CoiFcPmHistoryRxTotalPkts_Type = Counter64
_CoiFcPmHistoryRxTotalPkts_Object = MibTableColumn
coiFcPmHistoryRxTotalPkts = _CoiFcPmHistoryRxTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 2, 1, 4),
    _CoiFcPmHistoryRxTotalPkts_Type()
)
coiFcPmHistoryRxTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmHistoryRxTotalPkts.setStatus("current")
_CoiFcPmHistoryIfInErrors_Type = Counter64
_CoiFcPmHistoryIfInErrors_Object = MibTableColumn
coiFcPmHistoryIfInErrors = _CoiFcPmHistoryIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 2, 1, 5),
    _CoiFcPmHistoryIfInErrors_Type()
)
coiFcPmHistoryIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmHistoryIfInErrors.setStatus("current")
_CoiFcPmHistoryRxBadFcs_Type = Counter64
_CoiFcPmHistoryRxBadFcs_Object = MibTableColumn
coiFcPmHistoryRxBadFcs = _CoiFcPmHistoryRxBadFcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 2, 1, 6),
    _CoiFcPmHistoryRxBadFcs_Type()
)
coiFcPmHistoryRxBadFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmHistoryRxBadFcs.setStatus("current")
_CoiFcPmHistoryRxFramesTooShort_Type = Counter64
_CoiFcPmHistoryRxFramesTooShort_Object = MibTableColumn
coiFcPmHistoryRxFramesTooShort = _CoiFcPmHistoryRxFramesTooShort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 2, 1, 7),
    _CoiFcPmHistoryRxFramesTooShort_Type()
)
coiFcPmHistoryRxFramesTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmHistoryRxFramesTooShort.setStatus("current")
_CoiFcPmHistoryRxFramesTooLong_Type = Counter64
_CoiFcPmHistoryRxFramesTooLong_Object = MibTableColumn
coiFcPmHistoryRxFramesTooLong = _CoiFcPmHistoryRxFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 2, 1, 8),
    _CoiFcPmHistoryRxFramesTooLong_Type()
)
coiFcPmHistoryRxFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmHistoryRxFramesTooLong.setStatus("current")
_CoiFcPmHistoryIfOutOctets_Type = Counter64
_CoiFcPmHistoryIfOutOctets_Object = MibTableColumn
coiFcPmHistoryIfOutOctets = _CoiFcPmHistoryIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 2, 1, 9),
    _CoiFcPmHistoryIfOutOctets_Type()
)
coiFcPmHistoryIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmHistoryIfOutOctets.setStatus("current")
_CoiFcPmHistoryTxTotalPkts_Type = Counter64
_CoiFcPmHistoryTxTotalPkts_Object = MibTableColumn
coiFcPmHistoryTxTotalPkts = _CoiFcPmHistoryTxTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 2, 1, 10),
    _CoiFcPmHistoryTxTotalPkts_Type()
)
coiFcPmHistoryTxTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmHistoryTxTotalPkts.setStatus("current")
_CoiFcPmHistoryTxBadFcs_Type = Counter64
_CoiFcPmHistoryTxBadFcs_Object = MibTableColumn
coiFcPmHistoryTxBadFcs = _CoiFcPmHistoryTxBadFcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 2, 1, 11),
    _CoiFcPmHistoryTxBadFcs_Type()
)
coiFcPmHistoryTxBadFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmHistoryTxBadFcs.setStatus("current")
_CoiFcPmHistoryTxFramesTooShort_Type = Counter64
_CoiFcPmHistoryTxFramesTooShort_Object = MibTableColumn
coiFcPmHistoryTxFramesTooShort = _CoiFcPmHistoryTxFramesTooShort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 2, 1, 12),
    _CoiFcPmHistoryTxFramesTooShort_Type()
)
coiFcPmHistoryTxFramesTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmHistoryTxFramesTooShort.setStatus("current")
_CoiFcPmHistoryTxFramesTooLong_Type = Counter64
_CoiFcPmHistoryTxFramesTooLong_Object = MibTableColumn
coiFcPmHistoryTxFramesTooLong = _CoiFcPmHistoryTxFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 2, 1, 13),
    _CoiFcPmHistoryTxFramesTooLong_Type()
)
coiFcPmHistoryTxFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmHistoryTxFramesTooLong.setStatus("current")
_CoiFcPmHistoryValidData_Type = TruthValue
_CoiFcPmHistoryValidData_Object = MibTableColumn
coiFcPmHistoryValidData = _CoiFcPmHistoryValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 2, 2, 1, 14),
    _CoiFcPmHistoryValidData_Type()
)
coiFcPmHistoryValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFcPmHistoryValidData.setStatus("current")
_CoiFecPm_ObjectIdentity = ObjectIdentity
coiFecPm = _CoiFecPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3)
)
_CoiFecPmCurrentTable_ObjectIdentity = ObjectIdentity
coiFecPmCurrentTable = _CoiFecPmCurrentTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1)
)
_CoiFecPmCurrentEntry_Object = MibTableRow
coiFecPmCurrentEntry = _CoiFecPmCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1, 1)
)
coiFecPmCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-FIBRECHANNEL-MIB", "coiFecPmCurrentIntervalType"),
)
if mibBuilder.loadTexts:
    coiFecPmCurrentEntry.setStatus("current")
_CoiFecPmCurrentIntervalType_Type = CoiIntervalType
_CoiFecPmCurrentIntervalType_Object = MibTableColumn
coiFecPmCurrentIntervalType = _CoiFecPmCurrentIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1, 1, 1),
    _CoiFecPmCurrentIntervalType_Type()
)
coiFecPmCurrentIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmCurrentIntervalType.setStatus("current")
_CoiFecPmCorWordErrs_Type = Counter64
_CoiFecPmCorWordErrs_Object = MibTableColumn
coiFecPmCorWordErrs = _CoiFecPmCorWordErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1, 1, 2),
    _CoiFecPmCorWordErrs_Type()
)
coiFecPmCorWordErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmCorWordErrs.setStatus("current")
_CoiFecPmUncorWords_Type = Counter64
_CoiFecPmUncorWords_Object = MibTableColumn
coiFecPmUncorWords = _CoiFecPmUncorWords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1, 1, 3),
    _CoiFecPmUncorWords_Type()
)
coiFecPmUncorWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmUncorWords.setStatus("current")
_CoiFecPmPreFECMin_Type = DisplayString
_CoiFecPmPreFECMin_Object = MibTableColumn
coiFecPmPreFECMin = _CoiFecPmPreFECMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1, 1, 4),
    _CoiFecPmPreFECMin_Type()
)
coiFecPmPreFECMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmPreFECMin.setStatus("current")
_CoiFecPmPreFECMax_Type = DisplayString
_CoiFecPmPreFECMax_Object = MibTableColumn
coiFecPmPreFECMax = _CoiFecPmPreFECMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1, 1, 5),
    _CoiFecPmPreFECMax_Type()
)
coiFecPmPreFECMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmPreFECMax.setStatus("current")
_CoiFecPmPreFECAvg_Type = DisplayString
_CoiFecPmPreFECAvg_Object = MibTableColumn
coiFecPmPreFECAvg = _CoiFecPmPreFECAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1, 1, 6),
    _CoiFecPmPreFECAvg_Type()
)
coiFecPmPreFECAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmPreFECAvg.setStatus("current")
_CoiFecPmPostFECMin_Type = DisplayString
_CoiFecPmPostFECMin_Object = MibTableColumn
coiFecPmPostFECMin = _CoiFecPmPostFECMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1, 1, 7),
    _CoiFecPmPostFECMin_Type()
)
coiFecPmPostFECMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmPostFECMin.setStatus("current")
_CoiFecPmPostFECMax_Type = DisplayString
_CoiFecPmPostFECMax_Object = MibTableColumn
coiFecPmPostFECMax = _CoiFecPmPostFECMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1, 1, 8),
    _CoiFecPmPostFECMax_Type()
)
coiFecPmPostFECMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmPostFECMax.setStatus("current")
_CoiFecPmPostFECAvg_Type = DisplayString
_CoiFecPmPostFECAvg_Object = MibTableColumn
coiFecPmPostFECAvg = _CoiFecPmPostFECAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1, 1, 9),
    _CoiFecPmPostFECAvg_Type()
)
coiFecPmPostFECAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmPostFECAvg.setStatus("current")
_CoiFecPmQFactorMin_Type = DisplayString
_CoiFecPmQFactorMin_Object = MibTableColumn
coiFecPmQFactorMin = _CoiFecPmQFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1, 1, 10),
    _CoiFecPmQFactorMin_Type()
)
coiFecPmQFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmQFactorMin.setStatus("current")
_CoiFecPmQFactorMax_Type = DisplayString
_CoiFecPmQFactorMax_Object = MibTableColumn
coiFecPmQFactorMax = _CoiFecPmQFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1, 1, 11),
    _CoiFecPmQFactorMax_Type()
)
coiFecPmQFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmQFactorMax.setStatus("current")
_CoiFecPmQFactorAvg_Type = DisplayString
_CoiFecPmQFactorAvg_Object = MibTableColumn
coiFecPmQFactorAvg = _CoiFecPmQFactorAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1, 1, 12),
    _CoiFecPmQFactorAvg_Type()
)
coiFecPmQFactorAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmQFactorAvg.setStatus("current")
_CoiFecPmQMarginMin_Type = DisplayString
_CoiFecPmQMarginMin_Object = MibTableColumn
coiFecPmQMarginMin = _CoiFecPmQMarginMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1, 1, 13),
    _CoiFecPmQMarginMin_Type()
)
coiFecPmQMarginMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmQMarginMin.setStatus("current")
_CoiFecPmQMarginMax_Type = DisplayString
_CoiFecPmQMarginMax_Object = MibTableColumn
coiFecPmQMarginMax = _CoiFecPmQMarginMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1, 1, 14),
    _CoiFecPmQMarginMax_Type()
)
coiFecPmQMarginMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmQMarginMax.setStatus("current")
_CoiFecPmQMarginAvg_Type = DisplayString
_CoiFecPmQMarginAvg_Object = MibTableColumn
coiFecPmQMarginAvg = _CoiFecPmQMarginAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1, 1, 15),
    _CoiFecPmQMarginAvg_Type()
)
coiFecPmQMarginAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmQMarginAvg.setStatus("current")
_CoiFecPmInstQMarginMin_Type = DisplayString
_CoiFecPmInstQMarginMin_Object = MibTableColumn
coiFecPmInstQMarginMin = _CoiFecPmInstQMarginMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1, 1, 16),
    _CoiFecPmInstQMarginMin_Type()
)
coiFecPmInstQMarginMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmInstQMarginMin.setStatus("current")
_CoiFecPmInstQMarginMax_Type = DisplayString
_CoiFecPmInstQMarginMax_Object = MibTableColumn
coiFecPmInstQMarginMax = _CoiFecPmInstQMarginMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1, 1, 17),
    _CoiFecPmInstQMarginMax_Type()
)
coiFecPmInstQMarginMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmInstQMarginMax.setStatus("current")
_CoiFecPmInstQMarginAvg_Type = DisplayString
_CoiFecPmInstQMarginAvg_Object = MibTableColumn
coiFecPmInstQMarginAvg = _CoiFecPmInstQMarginAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1, 1, 18),
    _CoiFecPmInstQMarginAvg_Type()
)
coiFecPmInstQMarginAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmInstQMarginAvg.setStatus("current")
_CoiFecCurrentPmValidData_Type = TruthValue
_CoiFecCurrentPmValidData_Object = MibTableColumn
coiFecCurrentPmValidData = _CoiFecCurrentPmValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 1, 1, 19),
    _CoiFecCurrentPmValidData_Type()
)
coiFecCurrentPmValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecCurrentPmValidData.setStatus("current")
_CoiFecPmHistoryTable_ObjectIdentity = ObjectIdentity
coiFecPmHistoryTable = _CoiFecPmHistoryTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2)
)
_CoiFecPmHistoryEntry_Object = MibTableRow
coiFecPmHistoryEntry = _CoiFecPmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1)
)
coiFecPmHistoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-FIBRECHANNEL-MIB", "coiFecPmHistoryIntervalType"),
    (0, "CISCO-FIBRECHANNEL-MIB", "coiFecPmIntervalNumber"),
)
if mibBuilder.loadTexts:
    coiFecPmHistoryEntry.setStatus("current")
_CoiFecPmHistoryIntervalType_Type = CoiIntervalType
_CoiFecPmHistoryIntervalType_Object = MibTableColumn
coiFecPmHistoryIntervalType = _CoiFecPmHistoryIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1, 1),
    _CoiFecPmHistoryIntervalType_Type()
)
coiFecPmHistoryIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmHistoryIntervalType.setStatus("current")


class _CoiFecPmIntervalNumber_Type(Unsigned32):
    """Custom type coiFecPmIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CoiFecPmIntervalNumber_Type.__name__ = "Unsigned32"
_CoiFecPmIntervalNumber_Object = MibTableColumn
coiFecPmIntervalNumber = _CoiFecPmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1, 2),
    _CoiFecPmIntervalNumber_Type()
)
coiFecPmIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiFecPmIntervalNumber.setStatus("current")
_CoiFecPmHistoryCorWordErrs_Type = Counter64
_CoiFecPmHistoryCorWordErrs_Object = MibTableColumn
coiFecPmHistoryCorWordErrs = _CoiFecPmHistoryCorWordErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1, 3),
    _CoiFecPmHistoryCorWordErrs_Type()
)
coiFecPmHistoryCorWordErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmHistoryCorWordErrs.setStatus("current")
_CoiFecPmHistoryUncorWords_Type = Counter64
_CoiFecPmHistoryUncorWords_Object = MibTableColumn
coiFecPmHistoryUncorWords = _CoiFecPmHistoryUncorWords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1, 4),
    _CoiFecPmHistoryUncorWords_Type()
)
coiFecPmHistoryUncorWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmHistoryUncorWords.setStatus("current")
_CoiFecPmHistoryPreFECMin_Type = DisplayString
_CoiFecPmHistoryPreFECMin_Object = MibTableColumn
coiFecPmHistoryPreFECMin = _CoiFecPmHistoryPreFECMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1, 5),
    _CoiFecPmHistoryPreFECMin_Type()
)
coiFecPmHistoryPreFECMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmHistoryPreFECMin.setStatus("current")
_CoiFecPmHistoryPreFECMax_Type = DisplayString
_CoiFecPmHistoryPreFECMax_Object = MibTableColumn
coiFecPmHistoryPreFECMax = _CoiFecPmHistoryPreFECMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1, 6),
    _CoiFecPmHistoryPreFECMax_Type()
)
coiFecPmHistoryPreFECMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmHistoryPreFECMax.setStatus("current")
_CoiFecPmHistoryPreFECAvg_Type = DisplayString
_CoiFecPmHistoryPreFECAvg_Object = MibTableColumn
coiFecPmHistoryPreFECAvg = _CoiFecPmHistoryPreFECAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1, 7),
    _CoiFecPmHistoryPreFECAvg_Type()
)
coiFecPmHistoryPreFECAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmHistoryPreFECAvg.setStatus("current")
_CoiFecPmHistoryPostFECMin_Type = DisplayString
_CoiFecPmHistoryPostFECMin_Object = MibTableColumn
coiFecPmHistoryPostFECMin = _CoiFecPmHistoryPostFECMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1, 8),
    _CoiFecPmHistoryPostFECMin_Type()
)
coiFecPmHistoryPostFECMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmHistoryPostFECMin.setStatus("current")
_CoiFecPmHistoryPostFECMax_Type = DisplayString
_CoiFecPmHistoryPostFECMax_Object = MibTableColumn
coiFecPmHistoryPostFECMax = _CoiFecPmHistoryPostFECMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1, 9),
    _CoiFecPmHistoryPostFECMax_Type()
)
coiFecPmHistoryPostFECMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmHistoryPostFECMax.setStatus("current")
_CoiFecPmHistoryPostFECAvg_Type = DisplayString
_CoiFecPmHistoryPostFECAvg_Object = MibTableColumn
coiFecPmHistoryPostFECAvg = _CoiFecPmHistoryPostFECAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1, 10),
    _CoiFecPmHistoryPostFECAvg_Type()
)
coiFecPmHistoryPostFECAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmHistoryPostFECAvg.setStatus("current")
_CoiFecPmHistoryQFactorMin_Type = DisplayString
_CoiFecPmHistoryQFactorMin_Object = MibTableColumn
coiFecPmHistoryQFactorMin = _CoiFecPmHistoryQFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1, 11),
    _CoiFecPmHistoryQFactorMin_Type()
)
coiFecPmHistoryQFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmHistoryQFactorMin.setStatus("current")
_CoiFecPmHistoryQFactorMax_Type = DisplayString
_CoiFecPmHistoryQFactorMax_Object = MibTableColumn
coiFecPmHistoryQFactorMax = _CoiFecPmHistoryQFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1, 12),
    _CoiFecPmHistoryQFactorMax_Type()
)
coiFecPmHistoryQFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmHistoryQFactorMax.setStatus("current")
_CoiFecPmHistoryQFactorAvg_Type = DisplayString
_CoiFecPmHistoryQFactorAvg_Object = MibTableColumn
coiFecPmHistoryQFactorAvg = _CoiFecPmHistoryQFactorAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1, 13),
    _CoiFecPmHistoryQFactorAvg_Type()
)
coiFecPmHistoryQFactorAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmHistoryQFactorAvg.setStatus("current")
_CoiFecPmHistoryQMarginMin_Type = DisplayString
_CoiFecPmHistoryQMarginMin_Object = MibTableColumn
coiFecPmHistoryQMarginMin = _CoiFecPmHistoryQMarginMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1, 14),
    _CoiFecPmHistoryQMarginMin_Type()
)
coiFecPmHistoryQMarginMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmHistoryQMarginMin.setStatus("current")
_CoiFecPmHistoryQMarginMax_Type = DisplayString
_CoiFecPmHistoryQMarginMax_Object = MibTableColumn
coiFecPmHistoryQMarginMax = _CoiFecPmHistoryQMarginMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1, 15),
    _CoiFecPmHistoryQMarginMax_Type()
)
coiFecPmHistoryQMarginMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmHistoryQMarginMax.setStatus("current")
_CoiFecPmHistoryQMarginAvg_Type = DisplayString
_CoiFecPmHistoryQMarginAvg_Object = MibTableColumn
coiFecPmHistoryQMarginAvg = _CoiFecPmHistoryQMarginAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1, 16),
    _CoiFecPmHistoryQMarginAvg_Type()
)
coiFecPmHistoryQMarginAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmHistoryQMarginAvg.setStatus("current")
_CoiFecPmHistoryInstQMarginMin_Type = DisplayString
_CoiFecPmHistoryInstQMarginMin_Object = MibTableColumn
coiFecPmHistoryInstQMarginMin = _CoiFecPmHistoryInstQMarginMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1, 17),
    _CoiFecPmHistoryInstQMarginMin_Type()
)
coiFecPmHistoryInstQMarginMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmHistoryInstQMarginMin.setStatus("current")
_CoiFecPmHistoryInstQMarginMax_Type = DisplayString
_CoiFecPmHistoryInstQMarginMax_Object = MibTableColumn
coiFecPmHistoryInstQMarginMax = _CoiFecPmHistoryInstQMarginMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1, 18),
    _CoiFecPmHistoryInstQMarginMax_Type()
)
coiFecPmHistoryInstQMarginMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmHistoryInstQMarginMax.setStatus("current")
_CoiFecPmHistoryInstQMarginAvg_Type = DisplayString
_CoiFecPmHistoryInstQMarginAvg_Object = MibTableColumn
coiFecPmHistoryInstQMarginAvg = _CoiFecPmHistoryInstQMarginAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1, 19),
    _CoiFecPmHistoryInstQMarginAvg_Type()
)
coiFecPmHistoryInstQMarginAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmHistoryInstQMarginAvg.setStatus("current")
_CoiFecPmHistoryValidData_Type = TruthValue
_CoiFecPmHistoryValidData_Object = MibTableColumn
coiFecPmHistoryValidData = _CoiFecPmHistoryValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 3, 2, 1, 20),
    _CoiFecPmHistoryValidData_Type()
)
coiFecPmHistoryValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFecPmHistoryValidData.setStatus("current")
_CoiPcsPm_ObjectIdentity = ObjectIdentity
coiPcsPm = _CoiPcsPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4)
)
_CoiPcsPmCurrentTable_ObjectIdentity = ObjectIdentity
coiPcsPmCurrentTable = _CoiPcsPmCurrentTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 1)
)
_CoiPcsPmCurrentEntry_Object = MibTableRow
coiPcsPmCurrentEntry = _CoiPcsPmCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 1, 1)
)
coiPcsPmCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-FIBRECHANNEL-MIB", "coiPcsPmCurrentIntervalType"),
)
if mibBuilder.loadTexts:
    coiPcsPmCurrentEntry.setStatus("current")
_CoiPcsPmCurrentIntervalType_Type = CoiIntervalType
_CoiPcsPmCurrentIntervalType_Object = MibTableColumn
coiPcsPmCurrentIntervalType = _CoiPcsPmCurrentIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 1, 1, 1),
    _CoiPcsPmCurrentIntervalType_Type()
)
coiPcsPmCurrentIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmCurrentIntervalType.setStatus("current")
_CoiPcsPmCumBip_Type = Counter64
_CoiPcsPmCumBip_Object = MibTableColumn
coiPcsPmCumBip = _CoiPcsPmCumBip_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 1, 1, 2),
    _CoiPcsPmCumBip_Type()
)
coiPcsPmCumBip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmCumBip.setStatus("current")
_CoiPcsPmCumFrmError_Type = Counter64
_CoiPcsPmCumFrmError_Object = MibTableColumn
coiPcsPmCumFrmError = _CoiPcsPmCumFrmError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 1, 1, 3),
    _CoiPcsPmCumFrmError_Type()
)
coiPcsPmCumFrmError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmCumFrmError.setStatus("current")
_CoiPcsPmCumBadSh_Type = Counter64
_CoiPcsPmCumBadSh_Object = MibTableColumn
coiPcsPmCumBadSh = _CoiPcsPmCumBadSh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 1, 1, 4),
    _CoiPcsPmCumBadSh_Type()
)
coiPcsPmCumBadSh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmCumBadSh.setStatus("current")
_CoiPcsPmEs_Type = Counter64
_CoiPcsPmEs_Object = MibTableColumn
coiPcsPmEs = _CoiPcsPmEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 1, 1, 5),
    _CoiPcsPmEs_Type()
)
coiPcsPmEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmEs.setStatus("current")
_CoiPcsPmSes_Type = Counter64
_CoiPcsPmSes_Object = MibTableColumn
coiPcsPmSes = _CoiPcsPmSes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 1, 1, 6),
    _CoiPcsPmSes_Type()
)
coiPcsPmSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmSes.setStatus("current")
_CoiPcsPmUas_Type = Counter64
_CoiPcsPmUas_Object = MibTableColumn
coiPcsPmUas = _CoiPcsPmUas_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 1, 1, 7),
    _CoiPcsPmUas_Type()
)
coiPcsPmUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmUas.setStatus("current")
_CoiPcsPmFarEndEs_Type = Counter64
_CoiPcsPmFarEndEs_Object = MibTableColumn
coiPcsPmFarEndEs = _CoiPcsPmFarEndEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 1, 1, 8),
    _CoiPcsPmFarEndEs_Type()
)
coiPcsPmFarEndEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmFarEndEs.setStatus("current")
_CoiPcsPmFarEndSes_Type = Counter64
_CoiPcsPmFarEndSes_Object = MibTableColumn
coiPcsPmFarEndSes = _CoiPcsPmFarEndSes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 1, 1, 9),
    _CoiPcsPmFarEndSes_Type()
)
coiPcsPmFarEndSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmFarEndSes.setStatus("current")
_CoiPcsPmFarEndUas_Type = Counter64
_CoiPcsPmFarEndUas_Object = MibTableColumn
coiPcsPmFarEndUas = _CoiPcsPmFarEndUas_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 1, 1, 10),
    _CoiPcsPmFarEndUas_Type()
)
coiPcsPmFarEndUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmFarEndUas.setStatus("current")
_CoiPcsCurrentPmValidData_Type = TruthValue
_CoiPcsCurrentPmValidData_Object = MibTableColumn
coiPcsCurrentPmValidData = _CoiPcsCurrentPmValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 1, 1, 11),
    _CoiPcsCurrentPmValidData_Type()
)
coiPcsCurrentPmValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsCurrentPmValidData.setStatus("current")
_CoiPcsPmHistoryTable_ObjectIdentity = ObjectIdentity
coiPcsPmHistoryTable = _CoiPcsPmHistoryTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 2)
)
_CoiPcsPmHistoryEntry_Object = MibTableRow
coiPcsPmHistoryEntry = _CoiPcsPmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 2, 1)
)
coiPcsPmHistoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-FIBRECHANNEL-MIB", "coiPcsPmHistoryIntervalType"),
    (0, "CISCO-FIBRECHANNEL-MIB", "coiPcsPmIntervalNumber"),
)
if mibBuilder.loadTexts:
    coiPcsPmHistoryEntry.setStatus("current")
_CoiPcsPmHistoryIntervalType_Type = CoiIntervalType
_CoiPcsPmHistoryIntervalType_Object = MibTableColumn
coiPcsPmHistoryIntervalType = _CoiPcsPmHistoryIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 2, 1, 1),
    _CoiPcsPmHistoryIntervalType_Type()
)
coiPcsPmHistoryIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmHistoryIntervalType.setStatus("current")


class _CoiPcsPmIntervalNumber_Type(Unsigned32):
    """Custom type coiPcsPmIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CoiPcsPmIntervalNumber_Type.__name__ = "Unsigned32"
_CoiPcsPmIntervalNumber_Object = MibTableColumn
coiPcsPmIntervalNumber = _CoiPcsPmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 2, 1, 2),
    _CoiPcsPmIntervalNumber_Type()
)
coiPcsPmIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiPcsPmIntervalNumber.setStatus("current")
_CoiPcsPmHistoryCumBip_Type = Counter64
_CoiPcsPmHistoryCumBip_Object = MibTableColumn
coiPcsPmHistoryCumBip = _CoiPcsPmHistoryCumBip_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 2, 1, 3),
    _CoiPcsPmHistoryCumBip_Type()
)
coiPcsPmHistoryCumBip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmHistoryCumBip.setStatus("current")
_CoiPcsPmHistoryCumFrmError_Type = Counter64
_CoiPcsPmHistoryCumFrmError_Object = MibTableColumn
coiPcsPmHistoryCumFrmError = _CoiPcsPmHistoryCumFrmError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 2, 1, 4),
    _CoiPcsPmHistoryCumFrmError_Type()
)
coiPcsPmHistoryCumFrmError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmHistoryCumFrmError.setStatus("current")
_CoiPcsPmHistoryCumBadSh_Type = Counter64
_CoiPcsPmHistoryCumBadSh_Object = MibTableColumn
coiPcsPmHistoryCumBadSh = _CoiPcsPmHistoryCumBadSh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 2, 1, 5),
    _CoiPcsPmHistoryCumBadSh_Type()
)
coiPcsPmHistoryCumBadSh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmHistoryCumBadSh.setStatus("current")
_CoiPcsPmHistoryEs_Type = Counter64
_CoiPcsPmHistoryEs_Object = MibTableColumn
coiPcsPmHistoryEs = _CoiPcsPmHistoryEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 2, 1, 6),
    _CoiPcsPmHistoryEs_Type()
)
coiPcsPmHistoryEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmHistoryEs.setStatus("current")
_CoiPcsPmHistorySes_Type = Counter64
_CoiPcsPmHistorySes_Object = MibTableColumn
coiPcsPmHistorySes = _CoiPcsPmHistorySes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 2, 1, 7),
    _CoiPcsPmHistorySes_Type()
)
coiPcsPmHistorySes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmHistorySes.setStatus("current")
_CoiPcsPmHistoryUas_Type = Counter64
_CoiPcsPmHistoryUas_Object = MibTableColumn
coiPcsPmHistoryUas = _CoiPcsPmHistoryUas_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 2, 1, 8),
    _CoiPcsPmHistoryUas_Type()
)
coiPcsPmHistoryUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmHistoryUas.setStatus("current")
_CoiPcsPmHistoryEsFe_Type = Counter64
_CoiPcsPmHistoryEsFe_Object = MibTableColumn
coiPcsPmHistoryEsFe = _CoiPcsPmHistoryEsFe_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 2, 1, 9),
    _CoiPcsPmHistoryEsFe_Type()
)
coiPcsPmHistoryEsFe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmHistoryEsFe.setStatus("current")
_CoiPcsPmHistorySesFe_Type = Counter64
_CoiPcsPmHistorySesFe_Object = MibTableColumn
coiPcsPmHistorySesFe = _CoiPcsPmHistorySesFe_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 2, 1, 10),
    _CoiPcsPmHistorySesFe_Type()
)
coiPcsPmHistorySesFe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmHistorySesFe.setStatus("current")
_CoiPcsPmHistoryUasFe_Type = Counter64
_CoiPcsPmHistoryUasFe_Object = MibTableColumn
coiPcsPmHistoryUasFe = _CoiPcsPmHistoryUasFe_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 2, 1, 11),
    _CoiPcsPmHistoryUasFe_Type()
)
coiPcsPmHistoryUasFe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmHistoryUasFe.setStatus("current")
_CoiPcsPmHistoryValidData_Type = TruthValue
_CoiPcsPmHistoryValidData_Object = MibTableColumn
coiPcsPmHistoryValidData = _CoiPcsPmHistoryValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 1, 4, 2, 1, 12),
    _CoiPcsPmHistoryValidData_Type()
)
coiPcsPmHistoryValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiPcsPmHistoryValidData.setStatus("current")
_CiscoFibreChanMIBConformance_ObjectIdentity = ObjectIdentity
ciscoFibreChanMIBConformance = _CiscoFibreChanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 2)
)
_CiscoFibreChanMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoFibreChanMIBCompliances = _CiscoFibreChanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 2, 1)
)
_CiscoFibreChanMIBGroups_ObjectIdentity = ObjectIdentity
ciscoFibreChanMIBGroups = _CiscoFibreChanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1053, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIBRECHANNEL-MIB",
    **{"CoiIntervalType": CoiIntervalType,
       "ciscoFibreChanMIB": ciscoFibreChanMIB,
       "ciscoFibreChanMIBNotifs": ciscoFibreChanMIBNotifs,
       "ciscoFibreChanMIBObjects": ciscoFibreChanMIBObjects,
       "coiFibreChanController": coiFibreChanController,
       "coiFibreChanControllerTable": coiFibreChanControllerTable,
       "coiFibreChanControllerEntry": coiFibreChanControllerEntry,
       "coiFibreChanControllerAdminStatus": coiFibreChanControllerAdminStatus,
       "coiFibreChanControllerOperStatus": coiFibreChanControllerOperStatus,
       "coiFibreChanControllerLoopbackInfo": coiFibreChanControllerLoopbackInfo,
       "coiFibreChanControllerAlarmStatus": coiFibreChanControllerAlarmStatus,
       "coiFcPm": coiFcPm,
       "coiFcPmCurrentTable": coiFcPmCurrentTable,
       "coiFcPmCurrentEntry": coiFcPmCurrentEntry,
       "coiFcPmCurrentIntervalType": coiFcPmCurrentIntervalType,
       "coiFcPmIfInOctets": coiFcPmIfInOctets,
       "coiFcPmRxTotalPkts": coiFcPmRxTotalPkts,
       "coiFcPmIfInErrors": coiFcPmIfInErrors,
       "coiFcPmRxBadFcs": coiFcPmRxBadFcs,
       "coiFcPmRxFramesTooShort": coiFcPmRxFramesTooShort,
       "coiFcPmRxFramesTooLong": coiFcPmRxFramesTooLong,
       "coiFcPmIfOutOctets": coiFcPmIfOutOctets,
       "coiFcPmTxTotalPkts": coiFcPmTxTotalPkts,
       "coiFcPmTxBadFcs": coiFcPmTxBadFcs,
       "coiFcPmTxFramesTooShort": coiFcPmTxFramesTooShort,
       "coiFcPmTxFramesTooLong": coiFcPmTxFramesTooLong,
       "coiFcCurrentPmValidData": coiFcCurrentPmValidData,
       "coiFcPmHistoryTable": coiFcPmHistoryTable,
       "coiFcPmHistoryEntry": coiFcPmHistoryEntry,
       "coiFcPmHistoryIntervalType": coiFcPmHistoryIntervalType,
       "coiFcPmIntervalNumber": coiFcPmIntervalNumber,
       "coiFcPmHistoryIfInOctets": coiFcPmHistoryIfInOctets,
       "coiFcPmHistoryRxTotalPkts": coiFcPmHistoryRxTotalPkts,
       "coiFcPmHistoryIfInErrors": coiFcPmHistoryIfInErrors,
       "coiFcPmHistoryRxBadFcs": coiFcPmHistoryRxBadFcs,
       "coiFcPmHistoryRxFramesTooShort": coiFcPmHistoryRxFramesTooShort,
       "coiFcPmHistoryRxFramesTooLong": coiFcPmHistoryRxFramesTooLong,
       "coiFcPmHistoryIfOutOctets": coiFcPmHistoryIfOutOctets,
       "coiFcPmHistoryTxTotalPkts": coiFcPmHistoryTxTotalPkts,
       "coiFcPmHistoryTxBadFcs": coiFcPmHistoryTxBadFcs,
       "coiFcPmHistoryTxFramesTooShort": coiFcPmHistoryTxFramesTooShort,
       "coiFcPmHistoryTxFramesTooLong": coiFcPmHistoryTxFramesTooLong,
       "coiFcPmHistoryValidData": coiFcPmHistoryValidData,
       "coiFecPm": coiFecPm,
       "coiFecPmCurrentTable": coiFecPmCurrentTable,
       "coiFecPmCurrentEntry": coiFecPmCurrentEntry,
       "coiFecPmCurrentIntervalType": coiFecPmCurrentIntervalType,
       "coiFecPmCorWordErrs": coiFecPmCorWordErrs,
       "coiFecPmUncorWords": coiFecPmUncorWords,
       "coiFecPmPreFECMin": coiFecPmPreFECMin,
       "coiFecPmPreFECMax": coiFecPmPreFECMax,
       "coiFecPmPreFECAvg": coiFecPmPreFECAvg,
       "coiFecPmPostFECMin": coiFecPmPostFECMin,
       "coiFecPmPostFECMax": coiFecPmPostFECMax,
       "coiFecPmPostFECAvg": coiFecPmPostFECAvg,
       "coiFecPmQFactorMin": coiFecPmQFactorMin,
       "coiFecPmQFactorMax": coiFecPmQFactorMax,
       "coiFecPmQFactorAvg": coiFecPmQFactorAvg,
       "coiFecPmQMarginMin": coiFecPmQMarginMin,
       "coiFecPmQMarginMax": coiFecPmQMarginMax,
       "coiFecPmQMarginAvg": coiFecPmQMarginAvg,
       "coiFecPmInstQMarginMin": coiFecPmInstQMarginMin,
       "coiFecPmInstQMarginMax": coiFecPmInstQMarginMax,
       "coiFecPmInstQMarginAvg": coiFecPmInstQMarginAvg,
       "coiFecCurrentPmValidData": coiFecCurrentPmValidData,
       "coiFecPmHistoryTable": coiFecPmHistoryTable,
       "coiFecPmHistoryEntry": coiFecPmHistoryEntry,
       "coiFecPmHistoryIntervalType": coiFecPmHistoryIntervalType,
       "coiFecPmIntervalNumber": coiFecPmIntervalNumber,
       "coiFecPmHistoryCorWordErrs": coiFecPmHistoryCorWordErrs,
       "coiFecPmHistoryUncorWords": coiFecPmHistoryUncorWords,
       "coiFecPmHistoryPreFECMin": coiFecPmHistoryPreFECMin,
       "coiFecPmHistoryPreFECMax": coiFecPmHistoryPreFECMax,
       "coiFecPmHistoryPreFECAvg": coiFecPmHistoryPreFECAvg,
       "coiFecPmHistoryPostFECMin": coiFecPmHistoryPostFECMin,
       "coiFecPmHistoryPostFECMax": coiFecPmHistoryPostFECMax,
       "coiFecPmHistoryPostFECAvg": coiFecPmHistoryPostFECAvg,
       "coiFecPmHistoryQFactorMin": coiFecPmHistoryQFactorMin,
       "coiFecPmHistoryQFactorMax": coiFecPmHistoryQFactorMax,
       "coiFecPmHistoryQFactorAvg": coiFecPmHistoryQFactorAvg,
       "coiFecPmHistoryQMarginMin": coiFecPmHistoryQMarginMin,
       "coiFecPmHistoryQMarginMax": coiFecPmHistoryQMarginMax,
       "coiFecPmHistoryQMarginAvg": coiFecPmHistoryQMarginAvg,
       "coiFecPmHistoryInstQMarginMin": coiFecPmHistoryInstQMarginMin,
       "coiFecPmHistoryInstQMarginMax": coiFecPmHistoryInstQMarginMax,
       "coiFecPmHistoryInstQMarginAvg": coiFecPmHistoryInstQMarginAvg,
       "coiFecPmHistoryValidData": coiFecPmHistoryValidData,
       "coiPcsPm": coiPcsPm,
       "coiPcsPmCurrentTable": coiPcsPmCurrentTable,
       "coiPcsPmCurrentEntry": coiPcsPmCurrentEntry,
       "coiPcsPmCurrentIntervalType": coiPcsPmCurrentIntervalType,
       "coiPcsPmCumBip": coiPcsPmCumBip,
       "coiPcsPmCumFrmError": coiPcsPmCumFrmError,
       "coiPcsPmCumBadSh": coiPcsPmCumBadSh,
       "coiPcsPmEs": coiPcsPmEs,
       "coiPcsPmSes": coiPcsPmSes,
       "coiPcsPmUas": coiPcsPmUas,
       "coiPcsPmFarEndEs": coiPcsPmFarEndEs,
       "coiPcsPmFarEndSes": coiPcsPmFarEndSes,
       "coiPcsPmFarEndUas": coiPcsPmFarEndUas,
       "coiPcsCurrentPmValidData": coiPcsCurrentPmValidData,
       "coiPcsPmHistoryTable": coiPcsPmHistoryTable,
       "coiPcsPmHistoryEntry": coiPcsPmHistoryEntry,
       "coiPcsPmHistoryIntervalType": coiPcsPmHistoryIntervalType,
       "coiPcsPmIntervalNumber": coiPcsPmIntervalNumber,
       "coiPcsPmHistoryCumBip": coiPcsPmHistoryCumBip,
       "coiPcsPmHistoryCumFrmError": coiPcsPmHistoryCumFrmError,
       "coiPcsPmHistoryCumBadSh": coiPcsPmHistoryCumBadSh,
       "coiPcsPmHistoryEs": coiPcsPmHistoryEs,
       "coiPcsPmHistorySes": coiPcsPmHistorySes,
       "coiPcsPmHistoryUas": coiPcsPmHistoryUas,
       "coiPcsPmHistoryEsFe": coiPcsPmHistoryEsFe,
       "coiPcsPmHistorySesFe": coiPcsPmHistorySesFe,
       "coiPcsPmHistoryUasFe": coiPcsPmHistoryUasFe,
       "coiPcsPmHistoryValidData": coiPcsPmHistoryValidData,
       "ciscoFibreChanMIBConformance": ciscoFibreChanMIBConformance,
       "ciscoFibreChanMIBCompliances": ciscoFibreChanMIBCompliances,
       "ciscoFibreChanMIBGroups": ciscoFibreChanMIBGroups}
)

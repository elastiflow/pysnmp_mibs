# SNMP MIB module (CISCO-CPRI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-CPRI-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:55:32 2025
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
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoCpriMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999)
)
if mibBuilder.loadTexts:
    ciscoCpriMIB.setRevisions(
        ("2020-09-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCpriMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCpriMIBNotifs = _CiscoCpriMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 0)
)
_CiscoCpriMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCpriMIBObjects = _CiscoCpriMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1)
)
_CoiCpriController_ObjectIdentity = ObjectIdentity
coiCpriController = _CoiCpriController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1)
)
_CoiCpriControllerTable_Object = MibTable
coiCpriControllerTable = _CoiCpriControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1)
)
if mibBuilder.loadTexts:
    coiCpriControllerTable.setStatus("current")
_CoiCpriControllerEntry_Object = MibTableRow
coiCpriControllerEntry = _CoiCpriControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1)
)
coiCpriControllerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    coiCpriControllerEntry.setStatus("current")


class _CoiCpriControllerSupportedRateList_Type(Bits):
    """Custom type coiCpriControllerSupportedRateList based on Bits"""
    namedValues = NamedValues(
        *(("rate614Mbps", 0),
          ("rate1228Mbps", 1),
          ("rate2457Mbps", 2),
          ("rate3072Mbps", 3),
          ("rate4915Mbps", 4),
          ("rate6144Mbps", 5),
          ("rate9830Mbps", 6),
          ("rate8110Mbps", 7),
          ("rate10137Mbps", 8),
          ("rate12165Mbps", 9),
          ("rate24330Mbps", 10))
    )

_CoiCpriControllerSupportedRateList_Type.__name__ = "Bits"
_CoiCpriControllerSupportedRateList_Object = MibTableColumn
coiCpriControllerSupportedRateList = _CoiCpriControllerSupportedRateList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1),
    _CoiCpriControllerSupportedRateList_Type()
)
coiCpriControllerSupportedRateList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriControllerSupportedRateList.setStatus("current")


class _CoiCpriControllerConfiguredRateList_Type(Bits):
    """Custom type coiCpriControllerConfiguredRateList based on Bits"""
    namedValues = NamedValues(
        *(("rate614Mbps", 0),
          ("rate1228Mbps", 1),
          ("rate2457Mbps", 2),
          ("rate3072Mbps", 3),
          ("rate4915Mbps", 4),
          ("rate6144Mbps", 5),
          ("rate9830Mbps", 6),
          ("rate8110Mbps", 7),
          ("rate10137Mbps", 8),
          ("rate12165Mbps", 9),
          ("rate24330Mbps", 10))
    )

_CoiCpriControllerConfiguredRateList_Type.__name__ = "Bits"
_CoiCpriControllerConfiguredRateList_Object = MibTableColumn
coiCpriControllerConfiguredRateList = _CoiCpriControllerConfiguredRateList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 2),
    _CoiCpriControllerConfiguredRateList_Type()
)
coiCpriControllerConfiguredRateList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriControllerConfiguredRateList.setStatus("current")


class _CoiCpriControllerNegotiatedRate_Type(Integer32):
    """Custom type coiCpriControllerNegotiatedRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("rateNone", 0),
          ("rate614Mbps", 1),
          ("rate1228Mbps", 2),
          ("rate2457Mbps", 3),
          ("rate3072Mbps", 4),
          ("rate4915Mbps", 5),
          ("rate6144Mbps", 6),
          ("rate9830Mbps", 7),
          ("rate8110Mbps", 8),
          ("rate10137Mbps", 9),
          ("rate12165Mbps", 10),
          ("rate24330Mbps", 11))
    )


_CoiCpriControllerNegotiatedRate_Type.__name__ = "Integer32"
_CoiCpriControllerNegotiatedRate_Object = MibTableColumn
coiCpriControllerNegotiatedRate = _CoiCpriControllerNegotiatedRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 3),
    _CoiCpriControllerNegotiatedRate_Type()
)
coiCpriControllerNegotiatedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriControllerNegotiatedRate.setStatus("current")


class _CoiCpriControllerPortRole_Type(Integer32):
    """Custom type coiCpriControllerPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("slave", 0),
          ("master", 1))
    )


_CoiCpriControllerPortRole_Type.__name__ = "Integer32"
_CoiCpriControllerPortRole_Object = MibTableColumn
coiCpriControllerPortRole = _CoiCpriControllerPortRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 4),
    _CoiCpriControllerPortRole_Type()
)
coiCpriControllerPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriControllerPortRole.setStatus("current")
_CoiCpriControllerL1StartupTimer_Type = Unsigned32
_CoiCpriControllerL1StartupTimer_Object = MibTableColumn
coiCpriControllerL1StartupTimer = _CoiCpriControllerL1StartupTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 5),
    _CoiCpriControllerL1StartupTimer_Type()
)
coiCpriControllerL1StartupTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriControllerL1StartupTimer.setStatus("current")


class _CoiCpriControllerAdminStatus_Type(Integer32):
    """Custom type coiCpriControllerAdminStatus based on Integer32"""
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


_CoiCpriControllerAdminStatus_Type.__name__ = "Integer32"
_CoiCpriControllerAdminStatus_Object = MibTableColumn
coiCpriControllerAdminStatus = _CoiCpriControllerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 6),
    _CoiCpriControllerAdminStatus_Type()
)
coiCpriControllerAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriControllerAdminStatus.setStatus("current")


class _CoiCpriControllerOperStatus_Type(Integer32):
    """Custom type coiCpriControllerOperStatus based on Integer32"""
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


_CoiCpriControllerOperStatus_Type.__name__ = "Integer32"
_CoiCpriControllerOperStatus_Object = MibTableColumn
coiCpriControllerOperStatus = _CoiCpriControllerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 7),
    _CoiCpriControllerOperStatus_Type()
)
coiCpriControllerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriControllerOperStatus.setStatus("current")


class _CoiCpriControllerLoopbackInfo_Type(Integer32):
    """Custom type coiCpriControllerLoopbackInfo based on Integer32"""
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


_CoiCpriControllerLoopbackInfo_Type.__name__ = "Integer32"
_CoiCpriControllerLoopbackInfo_Object = MibTableColumn
coiCpriControllerLoopbackInfo = _CoiCpriControllerLoopbackInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 8),
    _CoiCpriControllerLoopbackInfo_Type()
)
coiCpriControllerLoopbackInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriControllerLoopbackInfo.setStatus("current")


class _CoiCpriControllerAlarmStatus_Type(Bits):
    """Custom type coiCpriControllerAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("los", 1),
          ("lof", 2),
          ("rai", 3),
          ("sdi", 4))
    )

_CoiCpriControllerAlarmStatus_Type.__name__ = "Bits"
_CoiCpriControllerAlarmStatus_Object = MibTableColumn
coiCpriControllerAlarmStatus = _CoiCpriControllerAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 9),
    _CoiCpriControllerAlarmStatus_Type()
)
coiCpriControllerAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriControllerAlarmStatus.setStatus("current")
_CoiCpriRoeStats_ObjectIdentity = ObjectIdentity
coiCpriRoeStats = _CoiCpriRoeStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 2)
)
_CoiCpriRoeStatsTable_ObjectIdentity = ObjectIdentity
coiCpriRoeStatsTable = _CoiCpriRoeStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 2, 1)
)
_CoiCpriRoeStatsEntry_Object = MibTableRow
coiCpriRoeStatsEntry = _CoiCpriRoeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 2, 1, 1)
)
coiCpriRoeStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    coiCpriRoeStatsEntry.setStatus("current")
_CoiCpriRoeRxFrames_Type = Counter64
_CoiCpriRoeRxFrames_Object = MibTableColumn
coiCpriRoeRxFrames = _CoiCpriRoeRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 2, 1, 1, 1),
    _CoiCpriRoeRxFrames_Type()
)
coiCpriRoeRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriRoeRxFrames.setStatus("current")
_CoiCpriRoeDroppedFramesDetected_Type = Counter64
_CoiCpriRoeDroppedFramesDetected_Object = MibTableColumn
coiCpriRoeDroppedFramesDetected = _CoiCpriRoeDroppedFramesDetected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 2, 1, 1, 2),
    _CoiCpriRoeDroppedFramesDetected_Type()
)
coiCpriRoeDroppedFramesDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriRoeDroppedFramesDetected.setStatus("current")
_CoiCpriRoeStrayFramesDetected_Type = Counter64
_CoiCpriRoeStrayFramesDetected_Object = MibTableColumn
coiCpriRoeStrayFramesDetected = _CoiCpriRoeStrayFramesDetected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 2, 1, 1, 3),
    _CoiCpriRoeStrayFramesDetected_Type()
)
coiCpriRoeStrayFramesDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriRoeStrayFramesDetected.setStatus("current")
_CoiCpriRoeDuplicateFramesDetected_Type = Counter64
_CoiCpriRoeDuplicateFramesDetected_Object = MibTableColumn
coiCpriRoeDuplicateFramesDetected = _CoiCpriRoeDuplicateFramesDetected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 2, 1, 1, 4),
    _CoiCpriRoeDuplicateFramesDetected_Type()
)
coiCpriRoeDuplicateFramesDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriRoeDuplicateFramesDetected.setStatus("current")
_CoiCpriRoeOutOfSeqFramesDetected_Type = Counter64
_CoiCpriRoeOutOfSeqFramesDetected_Object = MibTableColumn
coiCpriRoeOutOfSeqFramesDetected = _CoiCpriRoeOutOfSeqFramesDetected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 2, 1, 1, 5),
    _CoiCpriRoeOutOfSeqFramesDetected_Type()
)
coiCpriRoeOutOfSeqFramesDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriRoeOutOfSeqFramesDetected.setStatus("current")
_CoiCpriRoeOutOfSeqFramesDropped_Type = Counter64
_CoiCpriRoeOutOfSeqFramesDropped_Object = MibTableColumn
coiCpriRoeOutOfSeqFramesDropped = _CoiCpriRoeOutOfSeqFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 2, 1, 1, 6),
    _CoiCpriRoeOutOfSeqFramesDropped_Type()
)
coiCpriRoeOutOfSeqFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriRoeOutOfSeqFramesDropped.setStatus("current")
_CoiCpriRoeTxFrames_Type = Counter64
_CoiCpriRoeTxFrames_Object = MibTableColumn
coiCpriRoeTxFrames = _CoiCpriRoeTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 2, 1, 1, 7),
    _CoiCpriRoeTxFrames_Type()
)
coiCpriRoeTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriRoeTxFrames.setStatus("current")
_CoiCpriRoeIdleFramesSent_Type = Counter64
_CoiCpriRoeIdleFramesSent_Object = MibTableColumn
coiCpriRoeIdleFramesSent = _CoiCpriRoeIdleFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 2, 1, 1, 8),
    _CoiCpriRoeIdleFramesSent_Type()
)
coiCpriRoeIdleFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriRoeIdleFramesSent.setStatus("current")
_CoiCpriRoePktDelayVarMinVal_Type = Counter64
_CoiCpriRoePktDelayVarMinVal_Object = MibTableColumn
coiCpriRoePktDelayVarMinVal = _CoiCpriRoePktDelayVarMinVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 2, 1, 1, 9),
    _CoiCpriRoePktDelayVarMinVal_Type()
)
coiCpriRoePktDelayVarMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriRoePktDelayVarMinVal.setStatus("current")
_CoiCpriRoePktDelayVarMaxVal_Type = Counter64
_CoiCpriRoePktDelayVarMaxVal_Object = MibTableColumn
coiCpriRoePktDelayVarMaxVal = _CoiCpriRoePktDelayVarMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 2, 1, 1, 10),
    _CoiCpriRoePktDelayVarMaxVal_Type()
)
coiCpriRoePktDelayVarMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriRoePktDelayVarMaxVal.setStatus("current")
_CoiCpriRoePktDelayVarAvgVal_Type = Counter64
_CoiCpriRoePktDelayVarAvgVal_Object = MibTableColumn
coiCpriRoePktDelayVarAvgVal = _CoiCpriRoePktDelayVarAvgVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 2, 1, 1, 11),
    _CoiCpriRoePktDelayVarAvgVal_Type()
)
coiCpriRoePktDelayVarAvgVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriRoePktDelayVarAvgVal.setStatus("current")
_CoiCpriRoeLineCodeViolationDetected_Type = Counter64
_CoiCpriRoeLineCodeViolationDetected_Object = MibTableColumn
coiCpriRoeLineCodeViolationDetected = _CoiCpriRoeLineCodeViolationDetected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 2, 1, 1, 12),
    _CoiCpriRoeLineCodeViolationDetected_Type()
)
coiCpriRoeLineCodeViolationDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriRoeLineCodeViolationDetected.setStatus("current")
_CoiCpriRoeLineCodeViolationPropagated_Type = Counter64
_CoiCpriRoeLineCodeViolationPropagated_Object = MibTableColumn
coiCpriRoeLineCodeViolationPropagated = _CoiCpriRoeLineCodeViolationPropagated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 2, 1, 1, 13),
    _CoiCpriRoeLineCodeViolationPropagated_Type()
)
coiCpriRoeLineCodeViolationPropagated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriRoeLineCodeViolationPropagated.setStatus("current")
_CoiCpriRoeErroredLengthFrames_Type = Counter64
_CoiCpriRoeErroredLengthFrames_Object = MibTableColumn
coiCpriRoeErroredLengthFrames = _CoiCpriRoeErroredLengthFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 2, 1, 1, 14),
    _CoiCpriRoeErroredLengthFrames_Type()
)
coiCpriRoeErroredLengthFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiCpriRoeErroredLengthFrames.setStatus("current")
_CiscoCpriMIBConformance_ObjectIdentity = ObjectIdentity
ciscoCpriMIBConformance = _CiscoCpriMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2)
)
_CiscoCpriMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCpriMIBCompliances = _CiscoCpriMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1)
)
_CiscoCpriMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCpriMIBGroups = _CiscoCpriMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CPRI-MIB",
    **{"ciscoCpriMIB": ciscoCpriMIB,
       "ciscoCpriMIBNotifs": ciscoCpriMIBNotifs,
       "ciscoCpriMIBObjects": ciscoCpriMIBObjects,
       "coiCpriController": coiCpriController,
       "coiCpriControllerTable": coiCpriControllerTable,
       "coiCpriControllerEntry": coiCpriControllerEntry,
       "coiCpriControllerSupportedRateList": coiCpriControllerSupportedRateList,
       "coiCpriControllerConfiguredRateList": coiCpriControllerConfiguredRateList,
       "coiCpriControllerNegotiatedRate": coiCpriControllerNegotiatedRate,
       "coiCpriControllerPortRole": coiCpriControllerPortRole,
       "coiCpriControllerL1StartupTimer": coiCpriControllerL1StartupTimer,
       "coiCpriControllerAdminStatus": coiCpriControllerAdminStatus,
       "coiCpriControllerOperStatus": coiCpriControllerOperStatus,
       "coiCpriControllerLoopbackInfo": coiCpriControllerLoopbackInfo,
       "coiCpriControllerAlarmStatus": coiCpriControllerAlarmStatus,
       "coiCpriRoeStats": coiCpriRoeStats,
       "coiCpriRoeStatsTable": coiCpriRoeStatsTable,
       "coiCpriRoeStatsEntry": coiCpriRoeStatsEntry,
       "coiCpriRoeRxFrames": coiCpriRoeRxFrames,
       "coiCpriRoeDroppedFramesDetected": coiCpriRoeDroppedFramesDetected,
       "coiCpriRoeStrayFramesDetected": coiCpriRoeStrayFramesDetected,
       "coiCpriRoeDuplicateFramesDetected": coiCpriRoeDuplicateFramesDetected,
       "coiCpriRoeOutOfSeqFramesDetected": coiCpriRoeOutOfSeqFramesDetected,
       "coiCpriRoeOutOfSeqFramesDropped": coiCpriRoeOutOfSeqFramesDropped,
       "coiCpriRoeTxFrames": coiCpriRoeTxFrames,
       "coiCpriRoeIdleFramesSent": coiCpriRoeIdleFramesSent,
       "coiCpriRoePktDelayVarMinVal": coiCpriRoePktDelayVarMinVal,
       "coiCpriRoePktDelayVarMaxVal": coiCpriRoePktDelayVarMaxVal,
       "coiCpriRoePktDelayVarAvgVal": coiCpriRoePktDelayVarAvgVal,
       "coiCpriRoeLineCodeViolationDetected": coiCpriRoeLineCodeViolationDetected,
       "coiCpriRoeLineCodeViolationPropagated": coiCpriRoeLineCodeViolationPropagated,
       "coiCpriRoeErroredLengthFrames": coiCpriRoeErroredLengthFrames,
       "ciscoCpriMIBConformance": ciscoCpriMIBConformance,
       "ciscoCpriMIBCompliances": ciscoCpriMIBCompliances,
       "ciscoCpriMIBGroups": ciscoCpriMIBGroups}
)

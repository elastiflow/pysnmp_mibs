# SNMP MIB module (EXTREME-ERPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-ERPS-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:22:53 2025
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeErps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46)
)
if mibBuilder.loadTexts:
    extremeErps.setRevisions(
        ("2018-01-18 00:00",
         "2017-03-27 00:00",
         "2015-05-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RingMonitorMechanismType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("cfm", 1)
    )



class VlanType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unassigned", 0),
          ("control", 1),
          ("protected", 2))
    )



# MIB Managed Objects in the order of their OIDs

_ExtremeErpsNotifications_ObjectIdentity = ObjectIdentity
extremeErpsNotifications = _ExtremeErpsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 0)
)
_ExtremeErpsTraps_ObjectIdentity = ObjectIdentity
extremeErpsTraps = _ExtremeErpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 0, 0)
)


class _ExtremeErpsTypeOfFailure_Type(DisplayString):
    """Custom type extremeErpsTypeOfFailure based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeErpsTypeOfFailure_Type.__name__ = "DisplayString"
_ExtremeErpsTypeOfFailure_Object = MibScalar
extremeErpsTypeOfFailure = _ExtremeErpsTypeOfFailure_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 0, 1),
    _ExtremeErpsTypeOfFailure_Type()
)
extremeErpsTypeOfFailure.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeErpsTypeOfFailure.setStatus("current")
_ExtremeErpsProtectedVlanTable_Object = MibTable
extremeErpsProtectedVlanTable = _ExtremeErpsProtectedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 1)
)
if mibBuilder.loadTexts:
    extremeErpsProtectedVlanTable.setStatus("current")
_ExtremeErpsProtectedVlanEntry_Object = MibTableRow
extremeErpsProtectedVlanEntry = _ExtremeErpsProtectedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 1, 1)
)
extremeErpsProtectedVlanEntry.setIndexNames(
    (0, "EXTREME-ERPS-MIB", "extremeErpsRingName"),
    (0, "EXTREME-ERPS-MIB", "extremeErpsProtectedVlanName"),
)
if mibBuilder.loadTexts:
    extremeErpsProtectedVlanEntry.setStatus("current")


class _ExtremeErpsProtectedVlanName_Type(DisplayString):
    """Custom type extremeErpsProtectedVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeErpsProtectedVlanName_Type.__name__ = "DisplayString"
_ExtremeErpsProtectedVlanName_Object = MibTableColumn
extremeErpsProtectedVlanName = _ExtremeErpsProtectedVlanName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 1, 1, 1),
    _ExtremeErpsProtectedVlanName_Type()
)
extremeErpsProtectedVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsProtectedVlanName.setStatus("current")
_ExtremeErpsProtectedVlanId_Type = VlanId
_ExtremeErpsProtectedVlanId_Object = MibTableColumn
extremeErpsProtectedVlanId = _ExtremeErpsProtectedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 1, 1, 2),
    _ExtremeErpsProtectedVlanId_Type()
)
extremeErpsProtectedVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsProtectedVlanId.setStatus("current")
_ExtremeErpsProtectedVlanRowStatus_Type = RowStatus
_ExtremeErpsProtectedVlanRowStatus_Object = MibTableColumn
extremeErpsProtectedVlanRowStatus = _ExtremeErpsProtectedVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 1, 1, 3),
    _ExtremeErpsProtectedVlanRowStatus_Type()
)
extremeErpsProtectedVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeErpsProtectedVlanRowStatus.setStatus("current")
_ExtremeErpsRingTable_Object = MibTable
extremeErpsRingTable = _ExtremeErpsRingTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 2)
)
if mibBuilder.loadTexts:
    extremeErpsRingTable.setStatus("current")
_ExtremeErpsRingEntry_Object = MibTableRow
extremeErpsRingEntry = _ExtremeErpsRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 2, 1)
)
extremeErpsRingEntry.setIndexNames(
    (0, "EXTREME-ERPS-MIB", "extremeErpsRingName"),
)
if mibBuilder.loadTexts:
    extremeErpsRingEntry.setStatus("current")


class _ExtremeErpsRingName_Type(DisplayString):
    """Custom type extremeErpsRingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeErpsRingName_Type.__name__ = "DisplayString"
_ExtremeErpsRingName_Object = MibTableColumn
extremeErpsRingName = _ExtremeErpsRingName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 2, 1, 1),
    _ExtremeErpsRingName_Type()
)
extremeErpsRingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingName.setStatus("current")
_ExtremeErpsRingVlanId_Type = VlanId
_ExtremeErpsRingVlanId_Object = MibTableColumn
extremeErpsRingVlanId = _ExtremeErpsRingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 2, 1, 2),
    _ExtremeErpsRingVlanId_Type()
)
extremeErpsRingVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeErpsRingVlanId.setStatus("current")
_ExtremeErpsRingEast_Type = InterfaceIndex
_ExtremeErpsRingEast_Object = MibTableColumn
extremeErpsRingEast = _ExtremeErpsRingEast_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 2, 1, 3),
    _ExtremeErpsRingEast_Type()
)
extremeErpsRingEast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeErpsRingEast.setStatus("current")
_ExtremeErpsRingWest_Type = InterfaceIndexOrZero
_ExtremeErpsRingWest_Object = MibTableColumn
extremeErpsRingWest = _ExtremeErpsRingWest_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 2, 1, 4),
    _ExtremeErpsRingWest_Type()
)
extremeErpsRingWest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeErpsRingWest.setStatus("current")


class _ExtremeErpsRingRplPort_Type(InterfaceIndexOrZero):
    """Custom type extremeErpsRingRplPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_ExtremeErpsRingRplPort_Type.__name__ = "InterfaceIndexOrZero"
_ExtremeErpsRingRplPort_Object = MibTableColumn
extremeErpsRingRplPort = _ExtremeErpsRingRplPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 2, 1, 5),
    _ExtremeErpsRingRplPort_Type()
)
extremeErpsRingRplPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeErpsRingRplPort.setStatus("current")


class _ExtremeErpsRingPortBlockingOnVcRecovery_Type(TruthValue):
    """Custom type extremeErpsRingPortBlockingOnVcRecovery based on TruthValue"""
    defaultValue = 2


_ExtremeErpsRingPortBlockingOnVcRecovery_Type.__name__ = "TruthValue"
_ExtremeErpsRingPortBlockingOnVcRecovery_Object = MibTableColumn
extremeErpsRingPortBlockingOnVcRecovery = _ExtremeErpsRingPortBlockingOnVcRecovery_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 2, 1, 6),
    _ExtremeErpsRingPortBlockingOnVcRecovery_Type()
)
extremeErpsRingPortBlockingOnVcRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeErpsRingPortBlockingOnVcRecovery.setStatus("current")


class _ExtremeErpsRingNodeType_Type(Integer32):
    """Custom type extremeErpsRingNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rplOwner", 1),
          ("nonRplOwner", 2),
          ("interConnectionNode", 3))
    )


_ExtremeErpsRingNodeType_Type.__name__ = "Integer32"
_ExtremeErpsRingNodeType_Object = MibTableColumn
extremeErpsRingNodeType = _ExtremeErpsRingNodeType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 2, 1, 7),
    _ExtremeErpsRingNodeType_Type()
)
extremeErpsRingNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingNodeType.setStatus("current")


class _ExtremeErpsRingOperatingMode_Type(Integer32):
    """Custom type extremeErpsRingOperatingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("revertive", 1),
          ("nonRevertive", 2))
    )


_ExtremeErpsRingOperatingMode_Type.__name__ = "Integer32"
_ExtremeErpsRingOperatingMode_Object = MibTableColumn
extremeErpsRingOperatingMode = _ExtremeErpsRingOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 2, 1, 8),
    _ExtremeErpsRingOperatingMode_Type()
)
extremeErpsRingOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeErpsRingOperatingMode.setStatus("current")
_ExtremeErpsRingMonitorMechanism_Type = RingMonitorMechanismType
_ExtremeErpsRingMonitorMechanism_Object = MibTableColumn
extremeErpsRingMonitorMechanism = _ExtremeErpsRingMonitorMechanism_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 2, 1, 9),
    _ExtremeErpsRingMonitorMechanism_Type()
)
extremeErpsRingMonitorMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingMonitorMechanism.setStatus("current")


class _ExtremeErpsRingEastStatus_Type(Integer32):
    """Custom type extremeErpsRingEastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("unblocked", 2))
    )


_ExtremeErpsRingEastStatus_Type.__name__ = "Integer32"
_ExtremeErpsRingEastStatus_Object = MibTableColumn
extremeErpsRingEastStatus = _ExtremeErpsRingEastStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 2, 1, 10),
    _ExtremeErpsRingEastStatus_Type()
)
extremeErpsRingEastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingEastStatus.setStatus("current")


class _ExtremeErpsRingWestStatus_Type(Integer32):
    """Custom type extremeErpsRingWestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("unblocked", 2))
    )


_ExtremeErpsRingWestStatus_Type.__name__ = "Integer32"
_ExtremeErpsRingWestStatus_Object = MibTableColumn
extremeErpsRingWestStatus = _ExtremeErpsRingWestStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 2, 1, 11),
    _ExtremeErpsRingWestStatus_Type()
)
extremeErpsRingWestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingWestStatus.setStatus("current")


class _ExtremeErpsRingSemState_Type(Integer32):
    """Custom type extremeErpsRingSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("idle", 1),
          ("protection", 2),
          ("manualswitch", 3),
          ("forcedswitch", 4),
          ("pending", 5))
    )


_ExtremeErpsRingSemState_Type.__name__ = "Integer32"
_ExtremeErpsRingSemState_Object = MibTableColumn
extremeErpsRingSemState = _ExtremeErpsRingSemState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 2, 1, 12),
    _ExtremeErpsRingSemState_Type()
)
extremeErpsRingSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingSemState.setStatus("current")


class _ExtremeErpsRingNodeStatus_Type(Bits):
    """Custom type extremeErpsRingNodeStatus based on Bits"""
    namedValues = NamedValues(
        *(("signalFailOnEast", 0),
          ("signalFailOnWest", 1),
          ("remoteSignalFailOnEast", 2),
          ("remoteSignalFailOnWest", 3),
          ("rplBlocked", 4),
          ("waitToRestoreTimerRunning", 5),
          ("holdTimerRunning", 6),
          ("guardTimerRunning", 7))
    )

_ExtremeErpsRingNodeStatus_Type.__name__ = "Bits"
_ExtremeErpsRingNodeStatus_Object = MibTableColumn
extremeErpsRingNodeStatus = _ExtremeErpsRingNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 2, 1, 13),
    _ExtremeErpsRingNodeStatus_Type()
)
extremeErpsRingNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingNodeStatus.setStatus("current")


class _ExtremeErpsRingRplNeighbourPort_Type(InterfaceIndexOrZero):
    """Custom type extremeErpsRingRplNeighbourPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_ExtremeErpsRingRplNeighbourPort_Type.__name__ = "InterfaceIndexOrZero"
_ExtremeErpsRingRplNeighbourPort_Object = MibTableColumn
extremeErpsRingRplNeighbourPort = _ExtremeErpsRingRplNeighbourPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 2, 1, 14),
    _ExtremeErpsRingRplNeighbourPort_Type()
)
extremeErpsRingRplNeighbourPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeErpsRingRplNeighbourPort.setStatus("current")


class _ExtremeErpsRingProtectionType_Type(Integer32):
    """Custom type extremeErpsRingProtectionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portBased", 1),
          ("serviceBased", 2))
    )


_ExtremeErpsRingProtectionType_Type.__name__ = "Integer32"
_ExtremeErpsRingProtectionType_Object = MibTableColumn
extremeErpsRingProtectionType = _ExtremeErpsRingProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 2, 1, 15),
    _ExtremeErpsRingProtectionType_Type()
)
extremeErpsRingProtectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingProtectionType.setStatus("current")


class _ExtremeRingCfmGroup1_Type(DisplayString):
    """Custom type extremeRingCfmGroup1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtremeRingCfmGroup1_Type.__name__ = "DisplayString"
_ExtremeRingCfmGroup1_Object = MibTableColumn
extremeRingCfmGroup1 = _ExtremeRingCfmGroup1_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 2, 1, 16),
    _ExtremeRingCfmGroup1_Type()
)
extremeRingCfmGroup1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeRingCfmGroup1.setStatus("current")


class _ExtremeRingCfmGroup2_Type(DisplayString):
    """Custom type extremeRingCfmGroup2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtremeRingCfmGroup2_Type.__name__ = "DisplayString"
_ExtremeRingCfmGroup2_Object = MibTableColumn
extremeRingCfmGroup2 = _ExtremeRingCfmGroup2_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 2, 1, 17),
    _ExtremeRingCfmGroup2_Type()
)
extremeRingCfmGroup2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeRingCfmGroup2.setStatus("current")
_ExtremeErpsRingCfmRowStatus_Type = RowStatus
_ExtremeErpsRingCfmRowStatus_Object = MibTableColumn
extremeErpsRingCfmRowStatus = _ExtremeErpsRingCfmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 2, 1, 18),
    _ExtremeErpsRingCfmRowStatus_Type()
)
extremeErpsRingCfmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeErpsRingCfmRowStatus.setStatus("current")
_ExtremeErpsRingStatsTable_Object = MibTable
extremeErpsRingStatsTable = _ExtremeErpsRingStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 4)
)
if mibBuilder.loadTexts:
    extremeErpsRingStatsTable.setStatus("current")
_ExtremeErpsRingStatsEntry_Object = MibTableRow
extremeErpsRingStatsEntry = _ExtremeErpsRingStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 4, 1)
)
extremeErpsRingStatsEntry.setIndexNames(
    (0, "EXTREME-ERPS-MIB", "extremeErpsRingName"),
)
if mibBuilder.loadTexts:
    extremeErpsRingStatsEntry.setStatus("current")
_ExtremeErpsRingEastRapsPduSentCount_Type = Counter32
_ExtremeErpsRingEastRapsPduSentCount_Object = MibTableColumn
extremeErpsRingEastRapsPduSentCount = _ExtremeErpsRingEastRapsPduSentCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 4, 1, 1),
    _ExtremeErpsRingEastRapsPduSentCount_Type()
)
extremeErpsRingEastRapsPduSentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingEastRapsPduSentCount.setStatus("current")
_ExtremeErpsRingWestRapsPduSentCount_Type = Counter32
_ExtremeErpsRingWestRapsPduSentCount_Object = MibTableColumn
extremeErpsRingWestRapsPduSentCount = _ExtremeErpsRingWestRapsPduSentCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 4, 1, 2),
    _ExtremeErpsRingWestRapsPduSentCount_Type()
)
extremeErpsRingWestRapsPduSentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingWestRapsPduSentCount.setStatus("current")
_ExtremeErpsRingEastRapsPduRcvdCount_Type = Counter32
_ExtremeErpsRingEastRapsPduRcvdCount_Object = MibTableColumn
extremeErpsRingEastRapsPduRcvdCount = _ExtremeErpsRingEastRapsPduRcvdCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 4, 1, 3),
    _ExtremeErpsRingEastRapsPduRcvdCount_Type()
)
extremeErpsRingEastRapsPduRcvdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingEastRapsPduRcvdCount.setStatus("current")
_ExtremeErpsRingWestRapsPduRcvdCount_Type = Counter32
_ExtremeErpsRingWestRapsPduRcvdCount_Object = MibTableColumn
extremeErpsRingWestRapsPduRcvdCount = _ExtremeErpsRingWestRapsPduRcvdCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 4, 1, 4),
    _ExtremeErpsRingWestRapsPduRcvdCount_Type()
)
extremeErpsRingWestRapsPduRcvdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingWestRapsPduRcvdCount.setStatus("current")
_ExtremeErpsRingEastRapsPduDiscardCount_Type = Counter32
_ExtremeErpsRingEastRapsPduDiscardCount_Object = MibTableColumn
extremeErpsRingEastRapsPduDiscardCount = _ExtremeErpsRingEastRapsPduDiscardCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 4, 1, 5),
    _ExtremeErpsRingEastRapsPduDiscardCount_Type()
)
extremeErpsRingEastRapsPduDiscardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingEastRapsPduDiscardCount.setStatus("current")
_ExtremeErpsRingWestRapsPduDiscardCount_Type = Counter32
_ExtremeErpsRingWestRapsPduDiscardCount_Object = MibTableColumn
extremeErpsRingWestRapsPduDiscardCount = _ExtremeErpsRingWestRapsPduDiscardCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 4, 1, 6),
    _ExtremeErpsRingWestRapsPduDiscardCount_Type()
)
extremeErpsRingWestRapsPduDiscardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingWestRapsPduDiscardCount.setStatus("current")
_ExtremeErpsRingEastBlockedCount_Type = Counter32
_ExtremeErpsRingEastBlockedCount_Object = MibTableColumn
extremeErpsRingEastBlockedCount = _ExtremeErpsRingEastBlockedCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 4, 1, 7),
    _ExtremeErpsRingEastBlockedCount_Type()
)
extremeErpsRingEastBlockedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingEastBlockedCount.setStatus("current")
_ExtremeErpsRingWestBlockedCount_Type = Counter32
_ExtremeErpsRingWestBlockedCount_Object = MibTableColumn
extremeErpsRingWestBlockedCount = _ExtremeErpsRingWestBlockedCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 4, 1, 8),
    _ExtremeErpsRingWestBlockedCount_Type()
)
extremeErpsRingWestBlockedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingWestBlockedCount.setStatus("current")
_ExtremeErpsRingEastUnblockedCount_Type = Counter32
_ExtremeErpsRingEastUnblockedCount_Object = MibTableColumn
extremeErpsRingEastUnblockedCount = _ExtremeErpsRingEastUnblockedCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 4, 1, 9),
    _ExtremeErpsRingEastUnblockedCount_Type()
)
extremeErpsRingEastUnblockedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingEastUnblockedCount.setStatus("current")
_ExtremeErpsRingWestUnblockedCount_Type = Counter32
_ExtremeErpsRingWestUnblockedCount_Object = MibTableColumn
extremeErpsRingWestUnblockedCount = _ExtremeErpsRingWestUnblockedCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 4, 1, 10),
    _ExtremeErpsRingWestUnblockedCount_Type()
)
extremeErpsRingWestUnblockedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingWestUnblockedCount.setStatus("current")
_ExtremeErpsRingEastFailedCount_Type = Counter32
_ExtremeErpsRingEastFailedCount_Object = MibTableColumn
extremeErpsRingEastFailedCount = _ExtremeErpsRingEastFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 4, 1, 11),
    _ExtremeErpsRingEastFailedCount_Type()
)
extremeErpsRingEastFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingEastFailedCount.setStatus("current")
_ExtremeErpsRingWestFailedCount_Type = Counter32
_ExtremeErpsRingWestFailedCount_Object = MibTableColumn
extremeErpsRingWestFailedCount = _ExtremeErpsRingWestFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 4, 1, 12),
    _ExtremeErpsRingWestFailedCount_Type()
)
extremeErpsRingWestFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingWestFailedCount.setStatus("current")
_ExtremeErpsRingEastRecoveredCount_Type = Counter32
_ExtremeErpsRingEastRecoveredCount_Object = MibTableColumn
extremeErpsRingEastRecoveredCount = _ExtremeErpsRingEastRecoveredCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 4, 1, 13),
    _ExtremeErpsRingEastRecoveredCount_Type()
)
extremeErpsRingEastRecoveredCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingEastRecoveredCount.setStatus("current")
_ExtremeErpsRingWestRecoveredCount_Type = Counter32
_ExtremeErpsRingWestRecoveredCount_Object = MibTableColumn
extremeErpsRingWestRecoveredCount = _ExtremeErpsRingWestRecoveredCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 4, 1, 14),
    _ExtremeErpsRingWestRecoveredCount_Type()
)
extremeErpsRingWestRecoveredCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsRingWestRecoveredCount.setStatus("current")
_ExtremeErpsGlobalInfo_ObjectIdentity = ObjectIdentity
extremeErpsGlobalInfo = _ExtremeErpsGlobalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 5)
)
_ExtremeErpsGlobalEnabled_Type = TruthValue
_ExtremeErpsGlobalEnabled_Object = MibScalar
extremeErpsGlobalEnabled = _ExtremeErpsGlobalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 5, 1),
    _ExtremeErpsGlobalEnabled_Type()
)
extremeErpsGlobalEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsGlobalEnabled.setStatus("current")
_ExtremeErpsGlobalDisplayConfigWarnings_Type = TruthValue
_ExtremeErpsGlobalDisplayConfigWarnings_Object = MibScalar
extremeErpsGlobalDisplayConfigWarnings = _ExtremeErpsGlobalDisplayConfigWarnings_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 5, 2),
    _ExtremeErpsGlobalDisplayConfigWarnings_Type()
)
extremeErpsGlobalDisplayConfigWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsGlobalDisplayConfigWarnings.setStatus("current")
_ExtremeErpsGlobalMulticastAddRingPorts_Type = TruthValue
_ExtremeErpsGlobalMulticastAddRingPorts_Object = MibScalar
extremeErpsGlobalMulticastAddRingPorts = _ExtremeErpsGlobalMulticastAddRingPorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 5, 3),
    _ExtremeErpsGlobalMulticastAddRingPorts_Type()
)
extremeErpsGlobalMulticastAddRingPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsGlobalMulticastAddRingPorts.setStatus("current")
_ExtremeErpsGlobalMulticastSendIGMPAndMLDQuery_Type = TruthValue
_ExtremeErpsGlobalMulticastSendIGMPAndMLDQuery_Object = MibScalar
extremeErpsGlobalMulticastSendIGMPAndMLDQuery = _ExtremeErpsGlobalMulticastSendIGMPAndMLDQuery_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 5, 4),
    _ExtremeErpsGlobalMulticastSendIGMPAndMLDQuery_Type()
)
extremeErpsGlobalMulticastSendIGMPAndMLDQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsGlobalMulticastSendIGMPAndMLDQuery.setStatus("current")
_ExtremeErpsGlobalMulticastTemporaryFlooding_Type = TruthValue
_ExtremeErpsGlobalMulticastTemporaryFlooding_Object = MibScalar
extremeErpsGlobalMulticastTemporaryFlooding = _ExtremeErpsGlobalMulticastTemporaryFlooding_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 5, 5),
    _ExtremeErpsGlobalMulticastTemporaryFlooding_Type()
)
extremeErpsGlobalMulticastTemporaryFlooding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsGlobalMulticastTemporaryFlooding.setStatus("current")
_ExtremeErpsGlobalMulticastTemporaryFloodingDuration_Type = Counter32
_ExtremeErpsGlobalMulticastTemporaryFloodingDuration_Object = MibScalar
extremeErpsGlobalMulticastTemporaryFloodingDuration = _ExtremeErpsGlobalMulticastTemporaryFloodingDuration_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 5, 6),
    _ExtremeErpsGlobalMulticastTemporaryFloodingDuration_Type()
)
extremeErpsGlobalMulticastTemporaryFloodingDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsGlobalMulticastTemporaryFloodingDuration.setStatus("current")
_ExtremeErpsGlobalNumberOfERPSInstances_Type = Counter32
_ExtremeErpsGlobalNumberOfERPSInstances_Object = MibScalar
extremeErpsGlobalNumberOfERPSInstances = _ExtremeErpsGlobalNumberOfERPSInstances_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 5, 7),
    _ExtremeErpsGlobalNumberOfERPSInstances_Type()
)
extremeErpsGlobalNumberOfERPSInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeErpsGlobalNumberOfERPSInstances.setStatus("current")
_ExtremeErpsMIBConformance_ObjectIdentity = ObjectIdentity
extremeErpsMIBConformance = _ExtremeErpsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 6)
)
_ExtremeErpsMIBCompliances_ObjectIdentity = ObjectIdentity
extremeErpsMIBCompliances = _ExtremeErpsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 6, 1)
)
_ExtremeErpsMIBGroups_ObjectIdentity = ObjectIdentity
extremeErpsMIBGroups = _ExtremeErpsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 6, 2)
)

# Managed Objects groups

extremeErpsProtectedVlanEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 6, 2, 1)
)
extremeErpsProtectedVlanEntryGroup.setObjects(
      *(("EXTREME-ERPS-MIB", "extremeErpsProtectedVlanId"),
        ("EXTREME-ERPS-MIB", "extremeErpsProtectedVlanRowStatus"))
)
if mibBuilder.loadTexts:
    extremeErpsProtectedVlanEntryGroup.setStatus("deprecated")

extremeErpsRingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 6, 2, 2)
)
extremeErpsRingGroup.setObjects(
      *(("EXTREME-ERPS-MIB", "extremeErpsRingVlanId"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingEast"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingWest"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingRplPort"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingPortBlockingOnVcRecovery"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingNodeType"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingOperatingMode"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingMonitorMechanism"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingEastStatus"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingWestStatus"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingSemState"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingNodeStatus"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingRplNeighbourPort"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingProtectionType"))
)
if mibBuilder.loadTexts:
    extremeErpsRingGroup.setStatus("deprecated")

extremeErpsRingCfmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 6, 2, 3)
)
extremeErpsRingCfmGroup.setObjects(
      *(("EXTREME-ERPS-MIB", "extremeRingCfmGroup1"),
        ("EXTREME-ERPS-MIB", "extremeRingCfmGroup2"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingCfmRowStatus"))
)
if mibBuilder.loadTexts:
    extremeErpsRingCfmGroup.setStatus("current")

extremeErpsRingStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 6, 2, 4)
)
extremeErpsRingStatsGroup.setObjects(
      *(("EXTREME-ERPS-MIB", "extremeErpsRingEastRapsPduSentCount"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingWestRapsPduSentCount"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingEastRapsPduRcvdCount"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingWestRapsPduRcvdCount"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingEastRapsPduDiscardCount"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingWestRapsPduDiscardCount"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingEastBlockedCount"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingWestBlockedCount"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingEastUnblockedCount"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingWestUnblockedCount"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingEastFailedCount"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingWestFailedCount"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingEastRecoveredCount"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingWestRecoveredCount"))
)
if mibBuilder.loadTexts:
    extremeErpsRingStatsGroup.setStatus("current")

extremeErpsGlobalInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 6, 2, 5)
)
extremeErpsGlobalInfoGroup.setObjects(
      *(("EXTREME-ERPS-MIB", "extremeErpsGlobalEnabled"),
        ("EXTREME-ERPS-MIB", "extremeErpsGlobalDisplayConfigWarnings"),
        ("EXTREME-ERPS-MIB", "extremeErpsGlobalMulticastAddRingPorts"),
        ("EXTREME-ERPS-MIB", "extremeErpsGlobalMulticastSendIGMPAndMLDQuery"),
        ("EXTREME-ERPS-MIB", "extremeErpsGlobalMulticastTemporaryFlooding"),
        ("EXTREME-ERPS-MIB", "extremeErpsGlobalMulticastTemporaryFloodingDuration"),
        ("EXTREME-ERPS-MIB", "extremeErpsGlobalNumberOfERPSInstances"),
        ("EXTREME-ERPS-MIB", "extremeErpsTypeOfFailure"))
)
if mibBuilder.loadTexts:
    extremeErpsGlobalInfoGroup.setStatus("current")

extremeErpsProtectedVlanEntryGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 6, 2, 7)
)
extremeErpsProtectedVlanEntryGroup2.setObjects(
      *(("EXTREME-ERPS-MIB", "extremeErpsProtectedVlanName"),
        ("EXTREME-ERPS-MIB", "extremeErpsProtectedVlanId"),
        ("EXTREME-ERPS-MIB", "extremeErpsProtectedVlanRowStatus"))
)
if mibBuilder.loadTexts:
    extremeErpsProtectedVlanEntryGroup2.setStatus("current")

extremeErpsRingGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 6, 2, 8)
)
extremeErpsRingGroup2.setObjects(
      *(("EXTREME-ERPS-MIB", "extremeErpsRingName"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingVlanId"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingEast"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingWest"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingRplPort"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingPortBlockingOnVcRecovery"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingNodeType"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingOperatingMode"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingMonitorMechanism"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingEastStatus"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingWestStatus"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingSemState"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingNodeStatus"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingRplNeighbourPort"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingProtectionType"))
)
if mibBuilder.loadTexts:
    extremeErpsRingGroup2.setStatus("current")


# Notification objects

extremeErpsStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 0, 0, 1)
)
extremeErpsStateChangeTrap.setObjects(
      *(("EXTREME-ERPS-MIB", "extremeErpsRingName"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingSemState"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingNodeStatus"))
)
if mibBuilder.loadTexts:
    extremeErpsStateChangeTrap.setStatus(
        "current"
    )

extremeErpsFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 0, 0, 2)
)
extremeErpsFailureTrap.setObjects(
      *(("EXTREME-ERPS-MIB", "extremeErpsRingName"),
        ("EXTREME-ERPS-MIB", "extremeErpsTypeOfFailure"))
)
if mibBuilder.loadTexts:
    extremeErpsFailureTrap.setStatus(
        "current"
    )


# Notifications groups

extremeErpsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 6, 2, 6)
)
extremeErpsNotificationGroup.setObjects(
      *(("EXTREME-ERPS-MIB", "extremeErpsStateChangeTrap"),
        ("EXTREME-ERPS-MIB", "extremeErpsFailureTrap"))
)
if mibBuilder.loadTexts:
    extremeErpsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

extremeErpsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 6, 1, 1)
)
extremeErpsMIBCompliance.setObjects(
      *(("EXTREME-ERPS-MIB", "extremeErpsProtectedVlanEntryGroup"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingGroup"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingCfmGroup"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingStatsGroup"),
        ("EXTREME-ERPS-MIB", "extremeErpsGlobalInfoGroup"))
)
if mibBuilder.loadTexts:
    extremeErpsMIBCompliance.setStatus(
        "deprecated"
    )

extremeErpsMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46, 6, 1, 2)
)
extremeErpsMIBCompliance2.setObjects(
      *(("EXTREME-ERPS-MIB", "extremeErpsProtectedVlanEntryGroup2"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingGroup2"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingCfmGroup"),
        ("EXTREME-ERPS-MIB", "extremeErpsRingStatsGroup"),
        ("EXTREME-ERPS-MIB", "extremeErpsGlobalInfoGroup"))
)
if mibBuilder.loadTexts:
    extremeErpsMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-ERPS-MIB",
    **{"RingMonitorMechanismType": RingMonitorMechanismType,
       "VlanType": VlanType,
       "extremeErps": extremeErps,
       "extremeErpsNotifications": extremeErpsNotifications,
       "extremeErpsTraps": extremeErpsTraps,
       "extremeErpsStateChangeTrap": extremeErpsStateChangeTrap,
       "extremeErpsFailureTrap": extremeErpsFailureTrap,
       "extremeErpsTypeOfFailure": extremeErpsTypeOfFailure,
       "extremeErpsProtectedVlanTable": extremeErpsProtectedVlanTable,
       "extremeErpsProtectedVlanEntry": extremeErpsProtectedVlanEntry,
       "extremeErpsProtectedVlanName": extremeErpsProtectedVlanName,
       "extremeErpsProtectedVlanId": extremeErpsProtectedVlanId,
       "extremeErpsProtectedVlanRowStatus": extremeErpsProtectedVlanRowStatus,
       "extremeErpsRingTable": extremeErpsRingTable,
       "extremeErpsRingEntry": extremeErpsRingEntry,
       "extremeErpsRingName": extremeErpsRingName,
       "extremeErpsRingVlanId": extremeErpsRingVlanId,
       "extremeErpsRingEast": extremeErpsRingEast,
       "extremeErpsRingWest": extremeErpsRingWest,
       "extremeErpsRingRplPort": extremeErpsRingRplPort,
       "extremeErpsRingPortBlockingOnVcRecovery": extremeErpsRingPortBlockingOnVcRecovery,
       "extremeErpsRingNodeType": extremeErpsRingNodeType,
       "extremeErpsRingOperatingMode": extremeErpsRingOperatingMode,
       "extremeErpsRingMonitorMechanism": extremeErpsRingMonitorMechanism,
       "extremeErpsRingEastStatus": extremeErpsRingEastStatus,
       "extremeErpsRingWestStatus": extremeErpsRingWestStatus,
       "extremeErpsRingSemState": extremeErpsRingSemState,
       "extremeErpsRingNodeStatus": extremeErpsRingNodeStatus,
       "extremeErpsRingRplNeighbourPort": extremeErpsRingRplNeighbourPort,
       "extremeErpsRingProtectionType": extremeErpsRingProtectionType,
       "extremeRingCfmGroup1": extremeRingCfmGroup1,
       "extremeRingCfmGroup2": extremeRingCfmGroup2,
       "extremeErpsRingCfmRowStatus": extremeErpsRingCfmRowStatus,
       "extremeErpsRingStatsTable": extremeErpsRingStatsTable,
       "extremeErpsRingStatsEntry": extremeErpsRingStatsEntry,
       "extremeErpsRingEastRapsPduSentCount": extremeErpsRingEastRapsPduSentCount,
       "extremeErpsRingWestRapsPduSentCount": extremeErpsRingWestRapsPduSentCount,
       "extremeErpsRingEastRapsPduRcvdCount": extremeErpsRingEastRapsPduRcvdCount,
       "extremeErpsRingWestRapsPduRcvdCount": extremeErpsRingWestRapsPduRcvdCount,
       "extremeErpsRingEastRapsPduDiscardCount": extremeErpsRingEastRapsPduDiscardCount,
       "extremeErpsRingWestRapsPduDiscardCount": extremeErpsRingWestRapsPduDiscardCount,
       "extremeErpsRingEastBlockedCount": extremeErpsRingEastBlockedCount,
       "extremeErpsRingWestBlockedCount": extremeErpsRingWestBlockedCount,
       "extremeErpsRingEastUnblockedCount": extremeErpsRingEastUnblockedCount,
       "extremeErpsRingWestUnblockedCount": extremeErpsRingWestUnblockedCount,
       "extremeErpsRingEastFailedCount": extremeErpsRingEastFailedCount,
       "extremeErpsRingWestFailedCount": extremeErpsRingWestFailedCount,
       "extremeErpsRingEastRecoveredCount": extremeErpsRingEastRecoveredCount,
       "extremeErpsRingWestRecoveredCount": extremeErpsRingWestRecoveredCount,
       "extremeErpsGlobalInfo": extremeErpsGlobalInfo,
       "extremeErpsGlobalEnabled": extremeErpsGlobalEnabled,
       "extremeErpsGlobalDisplayConfigWarnings": extremeErpsGlobalDisplayConfigWarnings,
       "extremeErpsGlobalMulticastAddRingPorts": extremeErpsGlobalMulticastAddRingPorts,
       "extremeErpsGlobalMulticastSendIGMPAndMLDQuery": extremeErpsGlobalMulticastSendIGMPAndMLDQuery,
       "extremeErpsGlobalMulticastTemporaryFlooding": extremeErpsGlobalMulticastTemporaryFlooding,
       "extremeErpsGlobalMulticastTemporaryFloodingDuration": extremeErpsGlobalMulticastTemporaryFloodingDuration,
       "extremeErpsGlobalNumberOfERPSInstances": extremeErpsGlobalNumberOfERPSInstances,
       "extremeErpsMIBConformance": extremeErpsMIBConformance,
       "extremeErpsMIBCompliances": extremeErpsMIBCompliances,
       "extremeErpsMIBCompliance": extremeErpsMIBCompliance,
       "extremeErpsMIBCompliance2": extremeErpsMIBCompliance2,
       "extremeErpsMIBGroups": extremeErpsMIBGroups,
       "extremeErpsProtectedVlanEntryGroup": extremeErpsProtectedVlanEntryGroup,
       "extremeErpsRingGroup": extremeErpsRingGroup,
       "extremeErpsRingCfmGroup": extremeErpsRingCfmGroup,
       "extremeErpsRingStatsGroup": extremeErpsRingStatsGroup,
       "extremeErpsGlobalInfoGroup": extremeErpsGlobalInfoGroup,
       "extremeErpsNotificationGroup": extremeErpsNotificationGroup,
       "extremeErpsProtectedVlanEntryGroup2": extremeErpsProtectedVlanEntryGroup2,
       "extremeErpsRingGroup2": extremeErpsRingGroup2}
)

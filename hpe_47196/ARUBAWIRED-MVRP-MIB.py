# SNMP MIB module (ARUBAWIRED-MVRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/hpe_47196/ARUBAWIRED-MVRP-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 22:01:05 2025
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

(wndFeatures,) = mibBuilder.importSymbols(
    "ARUBAWIRED-NETWORKING-OID",
    "wndFeatures")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

arubaWiredMvrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    arubaWiredMvrpMIB.setRevisions(
        ("2017-11-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredMvrpNotifications_ObjectIdentity = ObjectIdentity
arubaWiredMvrpNotifications = _ArubaWiredMvrpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 0)
)
_ArubaWiredMvrpObjects_ObjectIdentity = ObjectIdentity
arubaWiredMvrpObjects = _ArubaWiredMvrpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1)
)
_ArubaWiredMvrpConfig_ObjectIdentity = ObjectIdentity
arubaWiredMvrpConfig = _ArubaWiredMvrpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 1)
)
_ArubaWiredMvrpGlobalClearStats_Type = TruthValue
_ArubaWiredMvrpGlobalClearStats_Object = MibScalar
arubaWiredMvrpGlobalClearStats = _ArubaWiredMvrpGlobalClearStats_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 1, 1),
    _ArubaWiredMvrpGlobalClearStats_Type()
)
arubaWiredMvrpGlobalClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMvrpGlobalClearStats.setStatus("current")
_ArubaWiredMvrpMaxVlanLimit_Type = Integer32
_ArubaWiredMvrpMaxVlanLimit_Object = MibScalar
arubaWiredMvrpMaxVlanLimit = _ArubaWiredMvrpMaxVlanLimit_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 1, 2),
    _ArubaWiredMvrpMaxVlanLimit_Type()
)
arubaWiredMvrpMaxVlanLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMvrpMaxVlanLimit.setStatus("current")
_ArubaWiredMvrpPortConfigTable_Object = MibTable
arubaWiredMvrpPortConfigTable = _ArubaWiredMvrpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    arubaWiredMvrpPortConfigTable.setStatus("current")
_ArubaWiredMvrpPortConfigEntry_Object = MibTableRow
arubaWiredMvrpPortConfigEntry = _ArubaWiredMvrpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 1, 3, 1)
)
arubaWiredMvrpPortConfigEntry.setIndexNames(
    (0, "ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortConfigifIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredMvrpPortConfigEntry.setStatus("current")
_ArubaWiredMvrpPortConfigifIndex_Type = InterfaceIndex
_ArubaWiredMvrpPortConfigifIndex_Object = MibTableColumn
arubaWiredMvrpPortConfigifIndex = _ArubaWiredMvrpPortConfigifIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 1, 3, 1, 1),
    _ArubaWiredMvrpPortConfigifIndex_Type()
)
arubaWiredMvrpPortConfigifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortConfigifIndex.setStatus("current")


class _ArubaWiredMvrpPortConfigRegistrarMode_Type(Integer32):
    """Custom type arubaWiredMvrpPortConfigRegistrarMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("fixed", 2))
    )


_ArubaWiredMvrpPortConfigRegistrarMode_Type.__name__ = "Integer32"
_ArubaWiredMvrpPortConfigRegistrarMode_Object = MibTableColumn
arubaWiredMvrpPortConfigRegistrarMode = _ArubaWiredMvrpPortConfigRegistrarMode_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 1, 3, 1, 2),
    _ArubaWiredMvrpPortConfigRegistrarMode_Type()
)
arubaWiredMvrpPortConfigRegistrarMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortConfigRegistrarMode.setStatus("current")


class _ArubaWiredMvrpPortConfigPeriodicTimer_Type(Gauge32):
    """Custom type arubaWiredMvrpPortConfigPeriodicTimer based on Gauge32"""
    defaultValue = 100

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_ArubaWiredMvrpPortConfigPeriodicTimer_Type.__name__ = "Gauge32"
_ArubaWiredMvrpPortConfigPeriodicTimer_Object = MibTableColumn
arubaWiredMvrpPortConfigPeriodicTimer = _ArubaWiredMvrpPortConfigPeriodicTimer_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 1, 3, 1, 3),
    _ArubaWiredMvrpPortConfigPeriodicTimer_Type()
)
arubaWiredMvrpPortConfigPeriodicTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortConfigPeriodicTimer.setStatus("current")


class _ArubaWiredMvrpPortConfigPeriodicTransmissionStatus_Type(EnabledStatus):
    """Custom type arubaWiredMvrpPortConfigPeriodicTransmissionStatus based on EnabledStatus"""
    defaultValue = 1


_ArubaWiredMvrpPortConfigPeriodicTransmissionStatus_Type.__name__ = "EnabledStatus"
_ArubaWiredMvrpPortConfigPeriodicTransmissionStatus_Object = MibTableColumn
arubaWiredMvrpPortConfigPeriodicTransmissionStatus = _ArubaWiredMvrpPortConfigPeriodicTransmissionStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 1, 3, 1, 4),
    _ArubaWiredMvrpPortConfigPeriodicTransmissionStatus_Type()
)
arubaWiredMvrpPortConfigPeriodicTransmissionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortConfigPeriodicTransmissionStatus.setStatus("current")
_ArubaWiredMvrpPortStatsClearStats_Type = TruthValue
_ArubaWiredMvrpPortStatsClearStats_Object = MibTableColumn
arubaWiredMvrpPortStatsClearStats = _ArubaWiredMvrpPortStatsClearStats_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 1, 3, 1, 5),
    _ArubaWiredMvrpPortStatsClearStats_Type()
)
arubaWiredMvrpPortStatsClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsClearStats.setStatus("current")
_ArubaWiredMvrpStats_ObjectIdentity = ObjectIdentity
arubaWiredMvrpStats = _ArubaWiredMvrpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2)
)
_ArubaWiredMvrpPortStatsTable_Object = MibTable
arubaWiredMvrpPortStatsTable = _ArubaWiredMvrpPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsTable.setStatus("current")
_ArubaWiredMvrpPortStatsEntry_Object = MibTableRow
arubaWiredMvrpPortStatsEntry = _ArubaWiredMvrpPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 1, 1)
)
arubaWiredMvrpPortStatsEntry.setIndexNames(
    (0, "ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStatsifIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsEntry.setStatus("current")
_ArubaWiredMvrpPortStatsifIndex_Type = InterfaceIndex
_ArubaWiredMvrpPortStatsifIndex_Object = MibTableColumn
arubaWiredMvrpPortStatsifIndex = _ArubaWiredMvrpPortStatsifIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 1, 1, 1),
    _ArubaWiredMvrpPortStatsifIndex_Type()
)
arubaWiredMvrpPortStatsifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsifIndex.setStatus("current")
_ArubaWiredMvrpPortStatsNewReceived_Type = Counter32
_ArubaWiredMvrpPortStatsNewReceived_Object = MibTableColumn
arubaWiredMvrpPortStatsNewReceived = _ArubaWiredMvrpPortStatsNewReceived_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 1, 1, 2),
    _ArubaWiredMvrpPortStatsNewReceived_Type()
)
arubaWiredMvrpPortStatsNewReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsNewReceived.setStatus("current")
_ArubaWiredMvrpPortStatsJoinInReceived_Type = Counter32
_ArubaWiredMvrpPortStatsJoinInReceived_Object = MibTableColumn
arubaWiredMvrpPortStatsJoinInReceived = _ArubaWiredMvrpPortStatsJoinInReceived_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 1, 1, 3),
    _ArubaWiredMvrpPortStatsJoinInReceived_Type()
)
arubaWiredMvrpPortStatsJoinInReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsJoinInReceived.setStatus("current")
_ArubaWiredMvrpPortStatsJoinEmptyReceived_Type = Counter32
_ArubaWiredMvrpPortStatsJoinEmptyReceived_Object = MibTableColumn
arubaWiredMvrpPortStatsJoinEmptyReceived = _ArubaWiredMvrpPortStatsJoinEmptyReceived_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 1, 1, 4),
    _ArubaWiredMvrpPortStatsJoinEmptyReceived_Type()
)
arubaWiredMvrpPortStatsJoinEmptyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsJoinEmptyReceived.setStatus("current")
_ArubaWiredMvrpPortStatsLeaveReceived_Type = Counter32
_ArubaWiredMvrpPortStatsLeaveReceived_Object = MibTableColumn
arubaWiredMvrpPortStatsLeaveReceived = _ArubaWiredMvrpPortStatsLeaveReceived_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 1, 1, 5),
    _ArubaWiredMvrpPortStatsLeaveReceived_Type()
)
arubaWiredMvrpPortStatsLeaveReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsLeaveReceived.setStatus("current")
_ArubaWiredMvrpPortStatsInReceived_Type = Counter32
_ArubaWiredMvrpPortStatsInReceived_Object = MibTableColumn
arubaWiredMvrpPortStatsInReceived = _ArubaWiredMvrpPortStatsInReceived_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 1, 1, 6),
    _ArubaWiredMvrpPortStatsInReceived_Type()
)
arubaWiredMvrpPortStatsInReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsInReceived.setStatus("current")
_ArubaWiredMvrpPortStatsEmptyReceived_Type = Counter32
_ArubaWiredMvrpPortStatsEmptyReceived_Object = MibTableColumn
arubaWiredMvrpPortStatsEmptyReceived = _ArubaWiredMvrpPortStatsEmptyReceived_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 1, 1, 7),
    _ArubaWiredMvrpPortStatsEmptyReceived_Type()
)
arubaWiredMvrpPortStatsEmptyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsEmptyReceived.setStatus("current")
_ArubaWiredMvrpPortStatsLeaveAllReceived_Type = Counter32
_ArubaWiredMvrpPortStatsLeaveAllReceived_Object = MibTableColumn
arubaWiredMvrpPortStatsLeaveAllReceived = _ArubaWiredMvrpPortStatsLeaveAllReceived_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 1, 1, 8),
    _ArubaWiredMvrpPortStatsLeaveAllReceived_Type()
)
arubaWiredMvrpPortStatsLeaveAllReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsLeaveAllReceived.setStatus("current")
_ArubaWiredMvrpPortStatsNewTransmitted_Type = Counter32
_ArubaWiredMvrpPortStatsNewTransmitted_Object = MibTableColumn
arubaWiredMvrpPortStatsNewTransmitted = _ArubaWiredMvrpPortStatsNewTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 1, 1, 9),
    _ArubaWiredMvrpPortStatsNewTransmitted_Type()
)
arubaWiredMvrpPortStatsNewTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsNewTransmitted.setStatus("current")
_ArubaWiredMvrpPortStatsJoinInTransmitted_Type = Counter32
_ArubaWiredMvrpPortStatsJoinInTransmitted_Object = MibTableColumn
arubaWiredMvrpPortStatsJoinInTransmitted = _ArubaWiredMvrpPortStatsJoinInTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 1, 1, 10),
    _ArubaWiredMvrpPortStatsJoinInTransmitted_Type()
)
arubaWiredMvrpPortStatsJoinInTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsJoinInTransmitted.setStatus("current")
_ArubaWiredMvrpPortStatsJoinEmptyTransmitted_Type = Counter32
_ArubaWiredMvrpPortStatsJoinEmptyTransmitted_Object = MibTableColumn
arubaWiredMvrpPortStatsJoinEmptyTransmitted = _ArubaWiredMvrpPortStatsJoinEmptyTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 1, 1, 11),
    _ArubaWiredMvrpPortStatsJoinEmptyTransmitted_Type()
)
arubaWiredMvrpPortStatsJoinEmptyTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsJoinEmptyTransmitted.setStatus("current")
_ArubaWiredMvrpPortStatsLeaveTransmitted_Type = Counter32
_ArubaWiredMvrpPortStatsLeaveTransmitted_Object = MibTableColumn
arubaWiredMvrpPortStatsLeaveTransmitted = _ArubaWiredMvrpPortStatsLeaveTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 1, 1, 12),
    _ArubaWiredMvrpPortStatsLeaveTransmitted_Type()
)
arubaWiredMvrpPortStatsLeaveTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsLeaveTransmitted.setStatus("current")
_ArubaWiredMvrpPortStatsInTransmitted_Type = Counter32
_ArubaWiredMvrpPortStatsInTransmitted_Object = MibTableColumn
arubaWiredMvrpPortStatsInTransmitted = _ArubaWiredMvrpPortStatsInTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 1, 1, 13),
    _ArubaWiredMvrpPortStatsInTransmitted_Type()
)
arubaWiredMvrpPortStatsInTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsInTransmitted.setStatus("current")
_ArubaWiredMvrpPortStatsEmptyTransmitted_Type = Counter32
_ArubaWiredMvrpPortStatsEmptyTransmitted_Object = MibTableColumn
arubaWiredMvrpPortStatsEmptyTransmitted = _ArubaWiredMvrpPortStatsEmptyTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 1, 1, 14),
    _ArubaWiredMvrpPortStatsEmptyTransmitted_Type()
)
arubaWiredMvrpPortStatsEmptyTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsEmptyTransmitted.setStatus("current")
_ArubaWiredMvrpPortStatsLeaveAllTransmitted_Type = Counter32
_ArubaWiredMvrpPortStatsLeaveAllTransmitted_Object = MibTableColumn
arubaWiredMvrpPortStatsLeaveAllTransmitted = _ArubaWiredMvrpPortStatsLeaveAllTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 1, 1, 15),
    _ArubaWiredMvrpPortStatsLeaveAllTransmitted_Type()
)
arubaWiredMvrpPortStatsLeaveAllTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsLeaveAllTransmitted.setStatus("current")
_ArubaWiredMvrpPortStatsTotalPDUReceived_Type = Counter32
_ArubaWiredMvrpPortStatsTotalPDUReceived_Object = MibTableColumn
arubaWiredMvrpPortStatsTotalPDUReceived = _ArubaWiredMvrpPortStatsTotalPDUReceived_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 1, 1, 16),
    _ArubaWiredMvrpPortStatsTotalPDUReceived_Type()
)
arubaWiredMvrpPortStatsTotalPDUReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsTotalPDUReceived.setStatus("current")
_ArubaWiredMvrpPortStatsTotalPDUTransmitted_Type = Counter32
_ArubaWiredMvrpPortStatsTotalPDUTransmitted_Object = MibTableColumn
arubaWiredMvrpPortStatsTotalPDUTransmitted = _ArubaWiredMvrpPortStatsTotalPDUTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 1, 1, 17),
    _ArubaWiredMvrpPortStatsTotalPDUTransmitted_Type()
)
arubaWiredMvrpPortStatsTotalPDUTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsTotalPDUTransmitted.setStatus("current")
_ArubaWiredMvrpPortStatsFramesDiscarded_Type = Counter32
_ArubaWiredMvrpPortStatsFramesDiscarded_Object = MibTableColumn
arubaWiredMvrpPortStatsFramesDiscarded = _ArubaWiredMvrpPortStatsFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 1, 1, 18),
    _ArubaWiredMvrpPortStatsFramesDiscarded_Type()
)
arubaWiredMvrpPortStatsFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsFramesDiscarded.setStatus("current")
_ArubaWiredMvrpStateTable_Object = MibTable
arubaWiredMvrpStateTable = _ArubaWiredMvrpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    arubaWiredMvrpStateTable.setStatus("current")
_ArubaWiredMvrpStateEntry_Object = MibTableRow
arubaWiredMvrpStateEntry = _ArubaWiredMvrpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 2, 1)
)
arubaWiredMvrpStateEntry.setIndexNames(
    (0, "ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpVlanId"),
    (0, "ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpStateifIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredMvrpStateEntry.setStatus("current")
_ArubaWiredMvrpVlanId_Type = VlanId
_ArubaWiredMvrpVlanId_Object = MibTableColumn
arubaWiredMvrpVlanId = _ArubaWiredMvrpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 2, 1, 1),
    _ArubaWiredMvrpVlanId_Type()
)
arubaWiredMvrpVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMvrpVlanId.setStatus("current")
_ArubaWiredMvrpStateifIndex_Type = InterfaceIndex
_ArubaWiredMvrpStateifIndex_Object = MibTableColumn
arubaWiredMvrpStateifIndex = _ArubaWiredMvrpStateifIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 2, 1, 2),
    _ArubaWiredMvrpStateifIndex_Type()
)
arubaWiredMvrpStateifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMvrpStateifIndex.setStatus("current")


class _ArubaWiredMvrpApplicantState_Type(Integer32):
    """Custom type arubaWiredMvrpApplicantState based on Integer32"""
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
        *(("aa", 0),
          ("qa", 1),
          ("la", 2),
          ("vp", 3),
          ("ap", 4),
          ("qp", 5),
          ("vo", 6),
          ("ao", 7),
          ("qo", 8),
          ("lo", 9),
          ("vn", 10),
          ("an", 11))
    )


_ArubaWiredMvrpApplicantState_Type.__name__ = "Integer32"
_ArubaWiredMvrpApplicantState_Object = MibTableColumn
arubaWiredMvrpApplicantState = _ArubaWiredMvrpApplicantState_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 2, 1, 3),
    _ArubaWiredMvrpApplicantState_Type()
)
arubaWiredMvrpApplicantState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMvrpApplicantState.setStatus("current")


class _ArubaWiredMvrpRegistrarState_Type(Integer32):
    """Custom type arubaWiredMvrpRegistrarState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("lv", 2),
          ("mt", 3))
    )


_ArubaWiredMvrpRegistrarState_Type.__name__ = "Integer32"
_ArubaWiredMvrpRegistrarState_Object = MibTableColumn
arubaWiredMvrpRegistrarState = _ArubaWiredMvrpRegistrarState_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 1, 2, 2, 1, 4),
    _ArubaWiredMvrpRegistrarState_Type()
)
arubaWiredMvrpRegistrarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMvrpRegistrarState.setStatus("current")
_ArubaWiredMvrpConformance_ObjectIdentity = ObjectIdentity
arubaWiredMvrpConformance = _ArubaWiredMvrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 3)
)
_ArubaWiredMvrpCompliances_ObjectIdentity = ObjectIdentity
arubaWiredMvrpCompliances = _ArubaWiredMvrpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 3, 1)
)
_ArubaWiredMvrpGroups_ObjectIdentity = ObjectIdentity
arubaWiredMvrpGroups = _ArubaWiredMvrpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 3, 2)
)

# Managed Objects groups

arubaWiredMvrpBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 3, 2, 1)
)
arubaWiredMvrpBaseGroup.setObjects(
      *(("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpGlobalClearStats"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpMaxVlanLimit"))
)
if mibBuilder.loadTexts:
    arubaWiredMvrpBaseGroup.setStatus("current")

arubaWiredMvrpPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 3, 2, 2)
)
arubaWiredMvrpPortConfigGroup.setObjects(
      *(("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortConfigRegistrarMode"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortConfigPeriodicTimer"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortConfigPeriodicTransmissionStatus"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStatsClearStats"))
)
if mibBuilder.loadTexts:
    arubaWiredMvrpPortConfigGroup.setStatus("current")

arubaWiredMvrpPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 3, 2, 3)
)
arubaWiredMvrpPortStatsGroup.setObjects(
      *(("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStatsNewReceived"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStatsJoinInReceived"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStatsJoinEmptyReceived"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStatsLeaveReceived"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStatsInReceived"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStatsEmptyReceived"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStatsLeaveAllReceived"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStatsNewTransmitted"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStatsJoinInTransmitted"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStatsJoinEmptyTransmitted"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStatsLeaveTransmitted"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStatsInTransmitted"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStatsEmptyTransmitted"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStatsLeaveAllTransmitted"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStatsTotalPDUReceived"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStatsTotalPDUTransmitted"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStatsFramesDiscarded"))
)
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStatsGroup.setStatus("current")

arubaWiredMvrpPortStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 3, 2, 4)
)
arubaWiredMvrpPortStateGroup.setObjects(
      *(("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpApplicantState"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpRegistrarState"))
)
if mibBuilder.loadTexts:
    arubaWiredMvrpPortStateGroup.setStatus("current")


# Notification objects

arubaWiredMvrpVlanLimitReachedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 0, 1)
)
arubaWiredMvrpVlanLimitReachedEvent.setObjects(
    ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpMaxVlanLimit")
)
if mibBuilder.loadTexts:
    arubaWiredMvrpVlanLimitReachedEvent.setStatus(
        "current"
    )


# Notifications groups

arubaWiredMvrpNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 3, 2, 5)
)
arubaWiredMvrpNotifyGroup.setObjects(
    ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpVlanLimitReachedEvent")
)
if mibBuilder.loadTexts:
    arubaWiredMvrpNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

arubaWiredMvrpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6, 3, 1, 1)
)
arubaWiredMvrpCompliance.setObjects(
      *(("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpBaseGroup"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortConfigGroup"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStatsGroup"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpPortStateGroup"),
        ("ARUBAWIRED-MVRP-MIB", "arubaWiredMvrpNotifyGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredMvrpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-MVRP-MIB",
    **{"arubaWiredMvrpMIB": arubaWiredMvrpMIB,
       "arubaWiredMvrpNotifications": arubaWiredMvrpNotifications,
       "arubaWiredMvrpVlanLimitReachedEvent": arubaWiredMvrpVlanLimitReachedEvent,
       "arubaWiredMvrpObjects": arubaWiredMvrpObjects,
       "arubaWiredMvrpConfig": arubaWiredMvrpConfig,
       "arubaWiredMvrpGlobalClearStats": arubaWiredMvrpGlobalClearStats,
       "arubaWiredMvrpMaxVlanLimit": arubaWiredMvrpMaxVlanLimit,
       "arubaWiredMvrpPortConfigTable": arubaWiredMvrpPortConfigTable,
       "arubaWiredMvrpPortConfigEntry": arubaWiredMvrpPortConfigEntry,
       "arubaWiredMvrpPortConfigifIndex": arubaWiredMvrpPortConfigifIndex,
       "arubaWiredMvrpPortConfigRegistrarMode": arubaWiredMvrpPortConfigRegistrarMode,
       "arubaWiredMvrpPortConfigPeriodicTimer": arubaWiredMvrpPortConfigPeriodicTimer,
       "arubaWiredMvrpPortConfigPeriodicTransmissionStatus": arubaWiredMvrpPortConfigPeriodicTransmissionStatus,
       "arubaWiredMvrpPortStatsClearStats": arubaWiredMvrpPortStatsClearStats,
       "arubaWiredMvrpStats": arubaWiredMvrpStats,
       "arubaWiredMvrpPortStatsTable": arubaWiredMvrpPortStatsTable,
       "arubaWiredMvrpPortStatsEntry": arubaWiredMvrpPortStatsEntry,
       "arubaWiredMvrpPortStatsifIndex": arubaWiredMvrpPortStatsifIndex,
       "arubaWiredMvrpPortStatsNewReceived": arubaWiredMvrpPortStatsNewReceived,
       "arubaWiredMvrpPortStatsJoinInReceived": arubaWiredMvrpPortStatsJoinInReceived,
       "arubaWiredMvrpPortStatsJoinEmptyReceived": arubaWiredMvrpPortStatsJoinEmptyReceived,
       "arubaWiredMvrpPortStatsLeaveReceived": arubaWiredMvrpPortStatsLeaveReceived,
       "arubaWiredMvrpPortStatsInReceived": arubaWiredMvrpPortStatsInReceived,
       "arubaWiredMvrpPortStatsEmptyReceived": arubaWiredMvrpPortStatsEmptyReceived,
       "arubaWiredMvrpPortStatsLeaveAllReceived": arubaWiredMvrpPortStatsLeaveAllReceived,
       "arubaWiredMvrpPortStatsNewTransmitted": arubaWiredMvrpPortStatsNewTransmitted,
       "arubaWiredMvrpPortStatsJoinInTransmitted": arubaWiredMvrpPortStatsJoinInTransmitted,
       "arubaWiredMvrpPortStatsJoinEmptyTransmitted": arubaWiredMvrpPortStatsJoinEmptyTransmitted,
       "arubaWiredMvrpPortStatsLeaveTransmitted": arubaWiredMvrpPortStatsLeaveTransmitted,
       "arubaWiredMvrpPortStatsInTransmitted": arubaWiredMvrpPortStatsInTransmitted,
       "arubaWiredMvrpPortStatsEmptyTransmitted": arubaWiredMvrpPortStatsEmptyTransmitted,
       "arubaWiredMvrpPortStatsLeaveAllTransmitted": arubaWiredMvrpPortStatsLeaveAllTransmitted,
       "arubaWiredMvrpPortStatsTotalPDUReceived": arubaWiredMvrpPortStatsTotalPDUReceived,
       "arubaWiredMvrpPortStatsTotalPDUTransmitted": arubaWiredMvrpPortStatsTotalPDUTransmitted,
       "arubaWiredMvrpPortStatsFramesDiscarded": arubaWiredMvrpPortStatsFramesDiscarded,
       "arubaWiredMvrpStateTable": arubaWiredMvrpStateTable,
       "arubaWiredMvrpStateEntry": arubaWiredMvrpStateEntry,
       "arubaWiredMvrpVlanId": arubaWiredMvrpVlanId,
       "arubaWiredMvrpStateifIndex": arubaWiredMvrpStateifIndex,
       "arubaWiredMvrpApplicantState": arubaWiredMvrpApplicantState,
       "arubaWiredMvrpRegistrarState": arubaWiredMvrpRegistrarState,
       "arubaWiredMvrpConformance": arubaWiredMvrpConformance,
       "arubaWiredMvrpCompliances": arubaWiredMvrpCompliances,
       "arubaWiredMvrpCompliance": arubaWiredMvrpCompliance,
       "arubaWiredMvrpGroups": arubaWiredMvrpGroups,
       "arubaWiredMvrpBaseGroup": arubaWiredMvrpBaseGroup,
       "arubaWiredMvrpPortConfigGroup": arubaWiredMvrpPortConfigGroup,
       "arubaWiredMvrpPortStatsGroup": arubaWiredMvrpPortStatsGroup,
       "arubaWiredMvrpPortStateGroup": arubaWiredMvrpPortStateGroup,
       "arubaWiredMvrpNotifyGroup": arubaWiredMvrpNotifyGroup}
)

# SNMP MIB module (ALU-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/ALU-PORT-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:55:46 2025
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

(aluHwConformance,
 aluHwNotification,
 aluHwObjs) = mibBuilder.importSymbols(
    "ALU-CHASSIS-MIB",
    "aluHwConformance",
    "aluHwNotification",
    "aluHwObjs")

(aluSARMIBModules,) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARMIBModules")

(frCircuitEntry,) = mibBuilder.importSymbols(
    "FRAME-RELAY-DTE-MIB",
    "frCircuitEntry")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tmnxChassisIndex,) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxChassisIndex")

(TmnxDSXClockSource,
 TmnxDSXIdleCycleFlags,
 TmnxDSXIdleFillType,
 TmnxDs0ChannelList,
 tmnxDS0ChanGroupEntry,
 tmnxDS1Entry,
 tmnxDS1PortEntry,
 tmnxFrIntfEntry,
 tmnxPortEtherEntry,
 tmnxPortNotifyPortId,
 tmnxPortPortID) = mibBuilder.importSymbols(
    "TIMETRA-PORT-MIB",
    "TmnxDSXClockSource",
    "TmnxDSXIdleCycleFlags",
    "TmnxDSXIdleFillType",
    "TmnxDs0ChannelList",
    "tmnxDS0ChanGroupEntry",
    "tmnxDS1Entry",
    "tmnxDS1PortEntry",
    "tmnxFrIntfEntry",
    "tmnxPortEtherEntry",
    "tmnxPortNotifyPortId",
    "tmnxPortPortID")

(TmnxEnabledDisabled,
 TmnxPortID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TmnxEnabledDisabled",
    "TmnxPortID")


# MODULE-IDENTITY

aluPortMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    aluPortMIBModule.setRevisions(
        ("1908-01-09 00:00",
         "1908-09-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluRS232ReportStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("notUsed", 0),
          ("hcmOof", 1),
          ("hcmRai", 2))
    )


class AluRS232ControlLead(TextualConvention, Integer32):
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
        *(("high", 1),
          ("low", 2),
          ("end-to-end", 3))
    )



class AluVoicePortTlp(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-160, 70),
    )



class AluVoiceSignalingLead(TextualConvention, Integer32):
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
        *(("high", 1),
          ("low", 2),
          ("end-to-end", 3))
    )



class AluDslTpsTcType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("efm", 2),
          ("atm", 4))
    )



class AluDslAdminState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("outOfService", 0),
          ("inService", 1))
    )



class AluDataReportStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("notUsed", 0),
          ("ais", 1),
          ("los", 2),
          ("rai", 3))
    )


# MIB Managed Objects in the order of their OIDs

_AluPortConformance_ObjectIdentity = ObjectIdentity
aluPortConformance = _AluPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4)
)
_AluPortCompliances_ObjectIdentity = ObjectIdentity
aluPortCompliances = _AluPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 1)
)
_AluPortComp7705_ObjectIdentity = ObjectIdentity
aluPortComp7705 = _AluPortComp7705_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 1, 1)
)
_AluPortGroups_ObjectIdentity = ObjectIdentity
aluPortGroups = _AluPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2)
)
_AluPortObjs_ObjectIdentity = ObjectIdentity
aluPortObjs = _AluPortObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4)
)
_AluExtTmnxDS1PortTable_Object = MibTable
aluExtTmnxDS1PortTable = _AluExtTmnxDS1PortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    aluExtTmnxDS1PortTable.setStatus("current")
_AluExtTmnxDS1PortEntry_Object = MibTableRow
aluExtTmnxDS1PortEntry = _AluExtTmnxDS1PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    aluExtTmnxDS1PortEntry.setStatus("current")


class _AluExtDS1PortLineImpedance_Type(Integer32):
    """Custom type aluExtDS1PortLineImpedance based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("impedance75Ohms", 1),
          ("impedance100Ohms", 2),
          ("impedance120Ohms", 3))
    )


_AluExtDS1PortLineImpedance_Type.__name__ = "Integer32"
_AluExtDS1PortLineImpedance_Object = MibTableColumn
aluExtDS1PortLineImpedance = _AluExtDS1PortLineImpedance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 1, 1, 1),
    _AluExtDS1PortLineImpedance_Type()
)
aluExtDS1PortLineImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtDS1PortLineImpedance.setStatus("current")
_AluExtTmnxPortEtherTable_Object = MibTable
aluExtTmnxPortEtherTable = _AluExtTmnxPortEtherTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    aluExtTmnxPortEtherTable.setStatus("current")
_AluExtTmnxPortEtherEntry_Object = MibTableRow
aluExtTmnxPortEtherEntry = _AluExtTmnxPortEtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    aluExtTmnxPortEtherEntry.setStatus("current")


class _AluExtPortEtherSfpSyncEStatus_Type(Integer32):
    """Custom type aluExtPortEtherSfpSyncEStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("capable", 1),
          ("incapable", 2))
    )


_AluExtPortEtherSfpSyncEStatus_Type.__name__ = "Integer32"
_AluExtPortEtherSfpSyncEStatus_Object = MibTableColumn
aluExtPortEtherSfpSyncEStatus = _AluExtPortEtherSfpSyncEStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 2, 1, 1),
    _AluExtPortEtherSfpSyncEStatus_Type()
)
aluExtPortEtherSfpSyncEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtPortEtherSfpSyncEStatus.setStatus("current")


class _AluExtPortEtherLoopback_Type(Integer32):
    """Custom type aluExtPortEtherLoopback based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("line", 1),
          ("internal", 2))
    )


_AluExtPortEtherLoopback_Type.__name__ = "Integer32"
_AluExtPortEtherLoopback_Object = MibTableColumn
aluExtPortEtherLoopback = _AluExtPortEtherLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 2, 1, 2),
    _AluExtPortEtherLoopback_Type()
)
aluExtPortEtherLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtPortEtherLoopback.setStatus("current")


class _AluExtPortEtherLoopbackTimer_Type(Unsigned32):
    """Custom type aluExtPortEtherLoopbackTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 86400),
    )


_AluExtPortEtherLoopbackTimer_Type.__name__ = "Unsigned32"
_AluExtPortEtherLoopbackTimer_Object = MibTableColumn
aluExtPortEtherLoopbackTimer = _AluExtPortEtherLoopbackTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 2, 1, 3),
    _AluExtPortEtherLoopbackTimer_Type()
)
aluExtPortEtherLoopbackTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtPortEtherLoopbackTimer.setStatus("current")


class _AluExtPortEtherLoopbackTimeLeft_Type(Unsigned32):
    """Custom type aluExtPortEtherLoopbackTimeLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AluExtPortEtherLoopbackTimeLeft_Type.__name__ = "Unsigned32"
_AluExtPortEtherLoopbackTimeLeft_Object = MibTableColumn
aluExtPortEtherLoopbackTimeLeft = _AluExtPortEtherLoopbackTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 2, 1, 4),
    _AluExtPortEtherLoopbackTimeLeft_Type()
)
aluExtPortEtherLoopbackTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtPortEtherLoopbackTimeLeft.setStatus("current")


class _AluExtPortEtherNwSchedulerMode_Type(Integer32):
    """Custom type aluExtPortEtherNwSchedulerMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("profile", 0),
          ("four-priority", 1),
          ("sixteen-priority", 2))
    )


_AluExtPortEtherNwSchedulerMode_Type.__name__ = "Integer32"
_AluExtPortEtherNwSchedulerMode_Object = MibTableColumn
aluExtPortEtherNwSchedulerMode = _AluExtPortEtherNwSchedulerMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 2, 1, 5),
    _AluExtPortEtherNwSchedulerMode_Type()
)
aluExtPortEtherNwSchedulerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtPortEtherNwSchedulerMode.setStatus("current")


class _AluExtPortEtherLoopbackCfmLbMode_Type(Integer32):
    """Custom type aluExtPortEtherLoopbackCfmLbMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("priority-low", 1),
          ("priority-high", 2))
    )


_AluExtPortEtherLoopbackCfmLbMode_Type.__name__ = "Integer32"
_AluExtPortEtherLoopbackCfmLbMode_Object = MibTableColumn
aluExtPortEtherLoopbackCfmLbMode = _AluExtPortEtherLoopbackCfmLbMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 2, 1, 6),
    _AluExtPortEtherLoopbackCfmLbMode_Type()
)
aluExtPortEtherLoopbackCfmLbMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtPortEtherLoopbackCfmLbMode.setStatus("current")
_AluExtPortEtherCfmLbmRx_Type = Counter64
_AluExtPortEtherCfmLbmRx_Object = MibTableColumn
aluExtPortEtherCfmLbmRx = _AluExtPortEtherCfmLbmRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 2, 1, 7),
    _AluExtPortEtherCfmLbmRx_Type()
)
aluExtPortEtherCfmLbmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtPortEtherCfmLbmRx.setStatus("current")
_AluExtPortEtherCfmLbmDropped_Type = Counter64
_AluExtPortEtherCfmLbmDropped_Object = MibTableColumn
aluExtPortEtherCfmLbmDropped = _AluExtPortEtherCfmLbmDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 2, 1, 8),
    _AluExtPortEtherCfmLbmDropped_Type()
)
aluExtPortEtherCfmLbmDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtPortEtherCfmLbmDropped.setStatus("current")
_AluExtPortEtherCfmLbrTx_Type = Counter64
_AluExtPortEtherCfmLbrTx_Object = MibTableColumn
aluExtPortEtherCfmLbrTx = _AluExtPortEtherCfmLbrTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 2, 1, 9),
    _AluExtPortEtherCfmLbrTx_Type()
)
aluExtPortEtherCfmLbrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtPortEtherCfmLbrTx.setStatus("current")


class _AluExtPortEtherLoopbackSwapMacAddr_Type(TruthValue):
    """Custom type aluExtPortEtherLoopbackSwapMacAddr based on TruthValue"""
    defaultValue = 2


_AluExtPortEtherLoopbackSwapMacAddr_Type.__name__ = "TruthValue"
_AluExtPortEtherLoopbackSwapMacAddr_Object = MibTableColumn
aluExtPortEtherLoopbackSwapMacAddr = _AluExtPortEtherLoopbackSwapMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 2, 1, 10),
    _AluExtPortEtherLoopbackSwapMacAddr_Type()
)
aluExtPortEtherLoopbackSwapMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtPortEtherLoopbackSwapMacAddr.setStatus("current")


class _AluExtPortEtherAdminPhyTxClock_Type(Integer32):
    """Custom type aluExtPortEtherAdminPhyTxClock based on Integer32"""
    defaultValue = 3

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
        *(("notApplicable", 0),
          ("slave", 1),
          ("master", 2),
          ("auto-pref-slave", 3),
          ("auto-pref-master", 4))
    )


_AluExtPortEtherAdminPhyTxClock_Type.__name__ = "Integer32"
_AluExtPortEtherAdminPhyTxClock_Object = MibTableColumn
aluExtPortEtherAdminPhyTxClock = _AluExtPortEtherAdminPhyTxClock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 2, 1, 11),
    _AluExtPortEtherAdminPhyTxClock_Type()
)
aluExtPortEtherAdminPhyTxClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtPortEtherAdminPhyTxClock.setStatus("current")


class _AluExtPortEtherOperPhyTxClock_Type(Integer32):
    """Custom type aluExtPortEtherOperPhyTxClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("slave", 1),
          ("master", 2))
    )


_AluExtPortEtherOperPhyTxClock_Type.__name__ = "Integer32"
_AluExtPortEtherOperPhyTxClock_Object = MibTableColumn
aluExtPortEtherOperPhyTxClock = _AluExtPortEtherOperPhyTxClock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 2, 1, 12),
    _AluExtPortEtherOperPhyTxClock_Type()
)
aluExtPortEtherOperPhyTxClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtPortEtherOperPhyTxClock.setStatus("current")
_AluEthPtpTimestampCapable_Type = TruthValue
_AluEthPtpTimestampCapable_Object = MibTableColumn
aluEthPtpTimestampCapable = _AluEthPtpTimestampCapable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 2, 1, 13),
    _AluEthPtpTimestampCapable_Type()
)
aluEthPtpTimestampCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluEthPtpTimestampCapable.setStatus("current")
_AluEthPtpTimestampEnable_Type = TruthValue
_AluEthPtpTimestampEnable_Object = MibTableColumn
aluEthPtpTimestampEnable = _AluEthPtpTimestampEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 2, 1, 14),
    _AluEthPtpTimestampEnable_Type()
)
aluEthPtpTimestampEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluEthPtpTimestampEnable.setStatus("current")


class _AluEthPtpAsymmetry_Type(Integer32):
    """Custom type aluEthPtpAsymmetry based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-8388608, 8388607),
    )


_AluEthPtpAsymmetry_Type.__name__ = "Integer32"
_AluEthPtpAsymmetry_Object = MibTableColumn
aluEthPtpAsymmetry = _AluEthPtpAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 2, 1, 15),
    _AluEthPtpAsymmetry_Type()
)
aluEthPtpAsymmetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluEthPtpAsymmetry.setStatus("current")
if mibBuilder.loadTexts:
    aluEthPtpAsymmetry.setUnits("nanoseconds")
_AluExtTmnxDS1Table_Object = MibTable
aluExtTmnxDS1Table = _AluExtTmnxDS1Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 3)
)
if mibBuilder.loadTexts:
    aluExtTmnxDS1Table.setStatus("current")
_AluExtTmnxDS1Entry_Object = MibTableRow
aluExtTmnxDS1Entry = _AluExtTmnxDS1Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    aluExtTmnxDS1Entry.setStatus("current")


class _AluExtDS1HoldTimeUp_Type(Unsigned32):
    """Custom type aluExtDS1HoldTimeUp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluExtDS1HoldTimeUp_Type.__name__ = "Unsigned32"
_AluExtDS1HoldTimeUp_Object = MibTableColumn
aluExtDS1HoldTimeUp = _AluExtDS1HoldTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 3, 1, 1),
    _AluExtDS1HoldTimeUp_Type()
)
aluExtDS1HoldTimeUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtDS1HoldTimeUp.setStatus("current")
if mibBuilder.loadTexts:
    aluExtDS1HoldTimeUp.setUnits("deci-seconds")


class _AluExtDS1HoldTimeDown_Type(Unsigned32):
    """Custom type aluExtDS1HoldTimeDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluExtDS1HoldTimeDown_Type.__name__ = "Unsigned32"
_AluExtDS1HoldTimeDown_Object = MibTableColumn
aluExtDS1HoldTimeDown = _AluExtDS1HoldTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 3, 1, 2),
    _AluExtDS1HoldTimeDown_Type()
)
aluExtDS1HoldTimeDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtDS1HoldTimeDown.setStatus("current")
if mibBuilder.loadTexts:
    aluExtDS1HoldTimeDown.setUnits("deci-seconds")


class _AluExtDS1SignalBitsState_Type(OctetString):
    """Custom type aluExtDS1SignalBitsState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_AluExtDS1SignalBitsState_Type.__name__ = "OctetString"
_AluExtDS1SignalBitsState_Object = MibTableColumn
aluExtDS1SignalBitsState = _AluExtDS1SignalBitsState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 3, 1, 3),
    _AluExtDS1SignalBitsState_Type()
)
aluExtDS1SignalBitsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtDS1SignalBitsState.setStatus("current")
_AluRS232PortTable_Object = MibTable
aluRS232PortTable = _AluRS232PortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 4)
)
if mibBuilder.loadTexts:
    aluRS232PortTable.setStatus("current")
_AluRS232PortEntry_Object = MibTableRow
aluRS232PortEntry = _AluRS232PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 4, 1)
)
aluRS232PortEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    aluRS232PortEntry.setStatus("current")
_AluRS232PortLastChangeTime_Type = TimeStamp
_AluRS232PortLastChangeTime_Object = MibTableColumn
aluRS232PortLastChangeTime = _AluRS232PortLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 4, 1, 1),
    _AluRS232PortLastChangeTime_Type()
)
aluRS232PortLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluRS232PortLastChangeTime.setStatus("current")


class _AluRS232PortType_Type(Integer32):
    """Custom type aluRS232PortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rs232", 1),
          ("v35", 2),
          ("x21", 3))
    )


_AluRS232PortType_Type.__name__ = "Integer32"
_AluRS232PortType_Object = MibTableColumn
aluRS232PortType = _AluRS232PortType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 4, 1, 2),
    _AluRS232PortType_Type()
)
aluRS232PortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232PortType.setStatus("current")
_AluRS232Table_Object = MibTable
aluRS232Table = _AluRS232Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5)
)
if mibBuilder.loadTexts:
    aluRS232Table.setStatus("current")
_AluRS232Entry_Object = MibTableRow
aluRS232Entry = _AluRS232Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1)
)
aluRS232Entry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    aluRS232Entry.setStatus("current")
_AluRS232RowStatus_Type = RowStatus
_AluRS232RowStatus_Object = MibTableColumn
aluRS232RowStatus = _AluRS232RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 1),
    _AluRS232RowStatus_Type()
)
aluRS232RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232RowStatus.setStatus("current")
_AluRS232LastChangeTime_Type = TimeStamp
_AluRS232LastChangeTime_Object = MibTableColumn
aluRS232LastChangeTime = _AluRS232LastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 2),
    _AluRS232LastChangeTime_Type()
)
aluRS232LastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluRS232LastChangeTime.setStatus("current")


class _AluRS232Type_Type(Integer32):
    """Custom type aluRS232Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rs232", 1),
          ("v35", 2),
          ("x21", 3))
    )


_AluRS232Type_Type.__name__ = "Integer32"
_AluRS232Type_Object = MibTableColumn
aluRS232Type = _AluRS232Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 3),
    _AluRS232Type_Type()
)
aluRS232Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluRS232Type.setStatus("current")


class _AluRS232DeviceMode_Type(Integer32):
    """Custom type aluRS232DeviceMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("synchronous", 1),
          ("asynchronous", 2))
    )


_AluRS232DeviceMode_Type.__name__ = "Integer32"
_AluRS232DeviceMode_Object = MibTableColumn
aluRS232DeviceMode = _AluRS232DeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 4),
    _AluRS232DeviceMode_Type()
)
aluRS232DeviceMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232DeviceMode.setStatus("current")


class _AluRS232DeviceGender_Type(Integer32):
    """Custom type aluRS232DeviceGender based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dte", 1),
          ("dce", 2))
    )


_AluRS232DeviceGender_Type.__name__ = "Integer32"
_AluRS232DeviceGender_Object = MibTableColumn
aluRS232DeviceGender = _AluRS232DeviceGender_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 5),
    _AluRS232DeviceGender_Type()
)
aluRS232DeviceGender.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232DeviceGender.setStatus("current")


class _AluRS232Duplex_Type(Integer32):
    """Custom type aluRS232Duplex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_AluRS232Duplex_Type.__name__ = "Integer32"
_AluRS232Duplex_Object = MibTableColumn
aluRS232Duplex = _AluRS232Duplex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 6),
    _AluRS232Duplex_Type()
)
aluRS232Duplex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232Duplex.setStatus("current")


class _AluRS232Speed_Type(Integer32):
    """Custom type aluRS232Speed based on Integer32"""
    defaultValue = 3

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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("speed1200", 1),
          ("speed2400", 2),
          ("speed9600", 3),
          ("speed19200", 4),
          ("speed38400", 5),
          ("speed56000", 6),
          ("speed64k", 7),
          ("speed128k", 8),
          ("speed256k", 9),
          ("speed384k", 10),
          ("speed512k", 11),
          ("speed640k", 12),
          ("speed768k", 13),
          ("speed896k", 14),
          ("speed1024k", 15),
          ("speed1152k", 16),
          ("speed1280k", 17),
          ("speed1408k", 18),
          ("speed1536k", 19),
          ("speed1664k", 20),
          ("speed1792k", 21),
          ("speed1920k", 22),
          ("speed4800", 23),
          ("speed600", 24))
    )


_AluRS232Speed_Type.__name__ = "Integer32"
_AluRS232Speed_Object = MibTableColumn
aluRS232Speed = _AluRS232Speed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 7),
    _AluRS232Speed_Type()
)
aluRS232Speed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232Speed.setStatus("current")


class _AluRS232ClockSource_Type(Integer32):
    """Custom type aluRS232ClockSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slave", 1),
          ("external", 2))
    )


_AluRS232ClockSource_Type.__name__ = "Integer32"
_AluRS232ClockSource_Object = MibTableColumn
aluRS232ClockSource = _AluRS232ClockSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 8),
    _AluRS232ClockSource_Type()
)
aluRS232ClockSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232ClockSource.setStatus("current")


class _AluRS232Loopback_Type(Integer32):
    """Custom type aluRS232Loopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("bidirB", 2),
          ("bidirE", 3))
    )


_AluRS232Loopback_Type.__name__ = "Integer32"
_AluRS232Loopback_Object = MibTableColumn
aluRS232Loopback = _AluRS232Loopback_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 9),
    _AluRS232Loopback_Type()
)
aluRS232Loopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232Loopback.setStatus("current")


class _AluRS232CharacterLength_Type(Integer32):
    """Custom type aluRS232CharacterLength based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 8),
    )


_AluRS232CharacterLength_Type.__name__ = "Integer32"
_AluRS232CharacterLength_Object = MibTableColumn
aluRS232CharacterLength = _AluRS232CharacterLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 10),
    _AluRS232CharacterLength_Type()
)
aluRS232CharacterLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232CharacterLength.setStatus("current")


class _AluRS232Parity_Type(Integer32):
    """Custom type aluRS232Parity based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("odd", 2),
          ("even", 3),
          ("mark", 4),
          ("space", 5))
    )


_AluRS232Parity_Type.__name__ = "Integer32"
_AluRS232Parity_Object = MibTableColumn
aluRS232Parity = _AluRS232Parity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 11),
    _AluRS232Parity_Type()
)
aluRS232Parity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232Parity.setStatus("current")


class _AluRS232StopBits_Type(Integer32):
    """Custom type aluRS232StopBits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AluRS232StopBits_Type.__name__ = "Integer32"
_AluRS232StopBits_Object = MibTableColumn
aluRS232StopBits = _AluRS232StopBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 12),
    _AluRS232StopBits_Type()
)
aluRS232StopBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232StopBits.setStatus("current")


class _AluRS232ReportAlarm_Type(AluRS232ReportStatus):
    """Custom type aluRS232ReportAlarm based on AluRS232ReportStatus"""
    defaultBinValue = "011"


_AluRS232ReportAlarm_Type.__name__ = "AluRS232ReportStatus"
_AluRS232ReportAlarm_Object = MibTableColumn
aluRS232ReportAlarm = _AluRS232ReportAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 13),
    _AluRS232ReportAlarm_Type()
)
aluRS232ReportAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232ReportAlarm.setStatus("current")
_AluRS232ReportAlarmStatus_Type = AluRS232ReportStatus
_AluRS232ReportAlarmStatus_Object = MibTableColumn
aluRS232ReportAlarmStatus = _AluRS232ReportAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 14),
    _AluRS232ReportAlarmStatus_Type()
)
aluRS232ReportAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluRS232ReportAlarmStatus.setStatus("current")


class _AluRS232ControlLeadDtrDsr_Type(AluRS232ControlLead):
    """Custom type aluRS232ControlLeadDtrDsr based on AluRS232ControlLead"""
    defaultValue = 1


_AluRS232ControlLeadDtrDsr_Type.__name__ = "AluRS232ControlLead"
_AluRS232ControlLeadDtrDsr_Object = MibTableColumn
aluRS232ControlLeadDtrDsr = _AluRS232ControlLeadDtrDsr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 15),
    _AluRS232ControlLeadDtrDsr_Type()
)
aluRS232ControlLeadDtrDsr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232ControlLeadDtrDsr.setStatus("current")


class _AluRS232ControlLeadRtsDcdC_Type(AluRS232ControlLead):
    """Custom type aluRS232ControlLeadRtsDcdC based on AluRS232ControlLead"""
    defaultValue = 1


_AluRS232ControlLeadRtsDcdC_Type.__name__ = "AluRS232ControlLead"
_AluRS232ControlLeadRtsDcdC_Object = MibTableColumn
aluRS232ControlLeadRtsDcdC = _AluRS232ControlLeadRtsDcdC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 16),
    _AluRS232ControlLeadRtsDcdC_Type()
)
aluRS232ControlLeadRtsDcdC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232ControlLeadRtsDcdC.setStatus("current")


class _AluRS232ControlLeadAlbCts_Type(AluRS232ControlLead):
    """Custom type aluRS232ControlLeadAlbCts based on AluRS232ControlLead"""
    defaultValue = 1


_AluRS232ControlLeadAlbCts_Type.__name__ = "AluRS232ControlLead"
_AluRS232ControlLeadAlbCts_Object = MibTableColumn
aluRS232ControlLeadAlbCts = _AluRS232ControlLeadAlbCts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 17),
    _AluRS232ControlLeadAlbCts_Type()
)
aluRS232ControlLeadAlbCts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232ControlLeadAlbCts.setStatus("current")


class _AluRS232ControlLeadRdlRi_Type(AluRS232ControlLead):
    """Custom type aluRS232ControlLeadRdlRi based on AluRS232ControlLead"""
    defaultValue = 1


_AluRS232ControlLeadRdlRi_Type.__name__ = "AluRS232ControlLead"
_AluRS232ControlLeadRdlRi_Object = MibTableColumn
aluRS232ControlLeadRdlRi = _AluRS232ControlLeadRdlRi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 18),
    _AluRS232ControlLeadRdlRi_Type()
)
aluRS232ControlLeadRdlRi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232ControlLeadRdlRi.setStatus("current")


class _AluRS232ControlLeadDsrDtr_Type(AluRS232ControlLead):
    """Custom type aluRS232ControlLeadDsrDtr based on AluRS232ControlLead"""
    defaultValue = 1


_AluRS232ControlLeadDsrDtr_Type.__name__ = "AluRS232ControlLead"
_AluRS232ControlLeadDsrDtr_Object = MibTableColumn
aluRS232ControlLeadDsrDtr = _AluRS232ControlLeadDsrDtr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 19),
    _AluRS232ControlLeadDsrDtr_Type()
)
aluRS232ControlLeadDsrDtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232ControlLeadDsrDtr.setStatus("current")


class _AluRS232ControlLeadDcdRtsI_Type(AluRS232ControlLead):
    """Custom type aluRS232ControlLeadDcdRtsI based on AluRS232ControlLead"""
    defaultValue = 1


_AluRS232ControlLeadDcdRtsI_Type.__name__ = "AluRS232ControlLead"
_AluRS232ControlLeadDcdRtsI_Object = MibTableColumn
aluRS232ControlLeadDcdRtsI = _AluRS232ControlLeadDcdRtsI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 20),
    _AluRS232ControlLeadDcdRtsI_Type()
)
aluRS232ControlLeadDcdRtsI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232ControlLeadDcdRtsI.setStatus("current")


class _AluRS232ControlLeadCtsAlb_Type(AluRS232ControlLead):
    """Custom type aluRS232ControlLeadCtsAlb based on AluRS232ControlLead"""
    defaultValue = 1


_AluRS232ControlLeadCtsAlb_Type.__name__ = "AluRS232ControlLead"
_AluRS232ControlLeadCtsAlb_Object = MibTableColumn
aluRS232ControlLeadCtsAlb = _AluRS232ControlLeadCtsAlb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 21),
    _AluRS232ControlLeadCtsAlb_Type()
)
aluRS232ControlLeadCtsAlb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232ControlLeadCtsAlb.setStatus("current")


class _AluRS232ControlLeadRiRdl_Type(AluRS232ControlLead):
    """Custom type aluRS232ControlLeadRiRdl based on AluRS232ControlLead"""
    defaultValue = 1


_AluRS232ControlLeadRiRdl_Type.__name__ = "AluRS232ControlLead"
_AluRS232ControlLeadRiRdl_Object = MibTableColumn
aluRS232ControlLeadRiRdl = _AluRS232ControlLeadRiRdl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 22),
    _AluRS232ControlLeadRiRdl_Type()
)
aluRS232ControlLeadRiRdl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232ControlLeadRiRdl.setStatus("current")


class _AluRS232ControlLeadsState_Type(OctetString):
    """Custom type aluRS232ControlLeadsState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_AluRS232ControlLeadsState_Type.__name__ = "OctetString"
_AluRS232ControlLeadsState_Object = MibTableColumn
aluRS232ControlLeadsState = _AluRS232ControlLeadsState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 23),
    _AluRS232ControlLeadsState_Type()
)
aluRS232ControlLeadsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluRS232ControlLeadsState.setStatus("current")


class _AluRS232MultiDrop_Type(Integer32):
    """Custom type aluRS232MultiDrop based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("slave", 2))
    )


_AluRS232MultiDrop_Type.__name__ = "Integer32"
_AluRS232MultiDrop_Object = MibTableColumn
aluRS232MultiDrop = _AluRS232MultiDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 24),
    _AluRS232MultiDrop_Type()
)
aluRS232MultiDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232MultiDrop.setStatus("current")


class _AluRS232SBitSignaling_Type(Integer32):
    """Custom type aluRS232SBitSignaling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_AluRS232SBitSignaling_Type.__name__ = "Integer32"
_AluRS232SBitSignaling_Object = MibTableColumn
aluRS232SBitSignaling = _AluRS232SBitSignaling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 25),
    _AluRS232SBitSignaling_Type()
)
aluRS232SBitSignaling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232SBitSignaling.setStatus("current")


class _AluRS232DataPosition_Type(Integer32):
    """Custom type aluRS232DataPosition based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("f0b5", 1),
          ("f0b6", 2))
    )


_AluRS232DataPosition_Type.__name__ = "Integer32"
_AluRS232DataPosition_Object = MibTableColumn
aluRS232DataPosition = _AluRS232DataPosition_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 5, 1, 26),
    _AluRS232DataPosition_Type()
)
aluRS232DataPosition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232DataPosition.setStatus("current")
_AluRS232ChanGroupTable_Object = MibTable
aluRS232ChanGroupTable = _AluRS232ChanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 6)
)
if mibBuilder.loadTexts:
    aluRS232ChanGroupTable.setStatus("current")
_AluRS232ChanGroupEntry_Object = MibTableRow
aluRS232ChanGroupEntry = _AluRS232ChanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 6, 1)
)
aluRS232ChanGroupEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    aluRS232ChanGroupEntry.setStatus("current")
_AluRS232ChanGroupRowStatus_Type = RowStatus
_AluRS232ChanGroupRowStatus_Object = MibTableColumn
aluRS232ChanGroupRowStatus = _AluRS232ChanGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 6, 1, 1),
    _AluRS232ChanGroupRowStatus_Type()
)
aluRS232ChanGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232ChanGroupRowStatus.setStatus("current")
_AluRS232ChanGroupTimeSlots_Type = TmnxDs0ChannelList
_AluRS232ChanGroupTimeSlots_Object = MibTableColumn
aluRS232ChanGroupTimeSlots = _AluRS232ChanGroupTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 6, 1, 2),
    _AluRS232ChanGroupTimeSlots_Type()
)
aluRS232ChanGroupTimeSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluRS232ChanGroupTimeSlots.setStatus("current")


class _AluRS232ChanGroupMTU_Type(Unsigned32):
    """Custom type aluRS232ChanGroupMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(578, 9208),
    )


_AluRS232ChanGroupMTU_Type.__name__ = "Unsigned32"
_AluRS232ChanGroupMTU_Object = MibTableColumn
aluRS232ChanGroupMTU = _AluRS232ChanGroupMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 6, 1, 3),
    _AluRS232ChanGroupMTU_Type()
)
aluRS232ChanGroupMTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232ChanGroupMTU.setStatus("current")
if mibBuilder.loadTexts:
    aluRS232ChanGroupMTU.setUnits("bytes")
_AluRS232ChanGroupOperMTU_Type = Unsigned32
_AluRS232ChanGroupOperMTU_Object = MibTableColumn
aluRS232ChanGroupOperMTU = _AluRS232ChanGroupOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 6, 1, 4),
    _AluRS232ChanGroupOperMTU_Type()
)
aluRS232ChanGroupOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluRS232ChanGroupOperMTU.setStatus("current")
if mibBuilder.loadTexts:
    aluRS232ChanGroupOperMTU.setUnits("bytes")


class _AluRS232ChanGroupCRC_Type(Integer32):
    """Custom type aluRS232ChanGroupCRC based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crc32", 2))
    )


_AluRS232ChanGroupCRC_Type.__name__ = "Integer32"
_AluRS232ChanGroupCRC_Object = MibTableColumn
aluRS232ChanGroupCRC = _AluRS232ChanGroupCRC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 6, 1, 5),
    _AluRS232ChanGroupCRC_Type()
)
aluRS232ChanGroupCRC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232ChanGroupCRC.setStatus("current")


class _AluRS232ChanGroupIdleCycleFlags_Type(TmnxDSXIdleCycleFlags):
    """Custom type aluRS232ChanGroupIdleCycleFlags based on TmnxDSXIdleCycleFlags"""
    defaultValue = 1


_AluRS232ChanGroupIdleCycleFlags_Type.__name__ = "TmnxDSXIdleCycleFlags"
_AluRS232ChanGroupIdleCycleFlags_Object = MibTableColumn
aluRS232ChanGroupIdleCycleFlags = _AluRS232ChanGroupIdleCycleFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 6, 1, 6),
    _AluRS232ChanGroupIdleCycleFlags_Type()
)
aluRS232ChanGroupIdleCycleFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232ChanGroupIdleCycleFlags.setStatus("current")


class _AluRS232ChanGroupPayloadFillType_Type(TmnxDSXIdleFillType):
    """Custom type aluRS232ChanGroupPayloadFillType based on TmnxDSXIdleFillType"""
    defaultValue = 0


_AluRS232ChanGroupPayloadFillType_Type.__name__ = "TmnxDSXIdleFillType"
_AluRS232ChanGroupPayloadFillType_Object = MibTableColumn
aluRS232ChanGroupPayloadFillType = _AluRS232ChanGroupPayloadFillType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 6, 1, 7),
    _AluRS232ChanGroupPayloadFillType_Type()
)
aluRS232ChanGroupPayloadFillType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232ChanGroupPayloadFillType.setStatus("current")


class _AluRS232ChanGroupPayloadPattern_Type(Unsigned32):
    """Custom type aluRS232ChanGroupPayloadPattern based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AluRS232ChanGroupPayloadPattern_Type.__name__ = "Unsigned32"
_AluRS232ChanGroupPayloadPattern_Object = MibTableColumn
aluRS232ChanGroupPayloadPattern = _AluRS232ChanGroupPayloadPattern_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 6, 1, 8),
    _AluRS232ChanGroupPayloadPattern_Type()
)
aluRS232ChanGroupPayloadPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRS232ChanGroupPayloadPattern.setStatus("current")
_AluVoicePortTable_Object = MibTable
aluVoicePortTable = _AluVoicePortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 7)
)
if mibBuilder.loadTexts:
    aluVoicePortTable.setStatus("current")
_AluVoicePortEntry_Object = MibTableRow
aluVoicePortEntry = _AluVoicePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 7, 1)
)
aluVoicePortEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    aluVoicePortEntry.setStatus("current")
_AluVoicePortLastChangeTime_Type = TimeStamp
_AluVoicePortLastChangeTime_Object = MibTableColumn
aluVoicePortLastChangeTime = _AluVoicePortLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 7, 1, 1),
    _AluVoicePortLastChangeTime_Type()
)
aluVoicePortLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoicePortLastChangeTime.setStatus("current")


class _AluVoicePortType_Type(Integer32):
    """Custom type aluVoicePortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("em", 1),
          ("fxo", 2),
          ("fxs", 3))
    )


_AluVoicePortType_Type.__name__ = "Integer32"
_AluVoicePortType_Object = MibTableColumn
aluVoicePortType = _AluVoicePortType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 7, 1, 2),
    _AluVoicePortType_Type()
)
aluVoicePortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVoicePortType.setStatus("current")


class _AluVoicePortAudioWires_Type(Integer32):
    """Custom type aluVoicePortAudioWires based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twoWires", 1),
          ("fourWires", 2))
    )


_AluVoicePortAudioWires_Type.__name__ = "Integer32"
_AluVoicePortAudioWires_Object = MibTableColumn
aluVoicePortAudioWires = _AluVoicePortAudioWires_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 7, 1, 3),
    _AluVoicePortAudioWires_Type()
)
aluVoicePortAudioWires.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVoicePortAudioWires.setStatus("current")


class _AluVoicePortTlpRx_Type(AluVoicePortTlp):
    """Custom type aluVoicePortTlpRx based on AluVoicePortTlp"""
    defaultValue = 0


_AluVoicePortTlpRx_Type.__name__ = "AluVoicePortTlp"
_AluVoicePortTlpRx_Object = MibTableColumn
aluVoicePortTlpRx = _AluVoicePortTlpRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 7, 1, 4),
    _AluVoicePortTlpRx_Type()
)
aluVoicePortTlpRx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVoicePortTlpRx.setStatus("current")
if mibBuilder.loadTexts:
    aluVoicePortTlpRx.setUnits("tenths of decibels")


class _AluVoicePortTlpTx_Type(AluVoicePortTlp):
    """Custom type aluVoicePortTlpTx based on AluVoicePortTlp"""
    defaultValue = 0


_AluVoicePortTlpTx_Type.__name__ = "AluVoicePortTlp"
_AluVoicePortTlpTx_Object = MibTableColumn
aluVoicePortTlpTx = _AluVoicePortTlpTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 7, 1, 5),
    _AluVoicePortTlpTx_Type()
)
aluVoicePortTlpTx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVoicePortTlpTx.setStatus("current")
if mibBuilder.loadTexts:
    aluVoicePortTlpTx.setUnits("tenths of decibels")


class _AluVoicePortLineBalance_Type(Integer32):
    """Custom type aluVoicePortLineBalance based on Integer32"""
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
        *(("short", 1),
          ("long", 2),
          ("nominal", 3),
          ("eightHundred", 4))
    )


_AluVoicePortLineBalance_Type.__name__ = "Integer32"
_AluVoicePortLineBalance_Object = MibTableColumn
aluVoicePortLineBalance = _AluVoicePortLineBalance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 7, 1, 6),
    _AluVoicePortLineBalance_Type()
)
aluVoicePortLineBalance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVoicePortLineBalance.setStatus("current")


class _AluVoicePortRingGeneration_Type(Integer32):
    """Custom type aluVoicePortRingGeneration based on Integer32"""
    defaultValue = 2

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
        *(("none", 1),
          ("freq16", 2),
          ("freq20", 3),
          ("freq25", 4))
    )


_AluVoicePortRingGeneration_Type.__name__ = "Integer32"
_AluVoicePortRingGeneration_Object = MibTableColumn
aluVoicePortRingGeneration = _AluVoicePortRingGeneration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 7, 1, 7),
    _AluVoicePortRingGeneration_Type()
)
aluVoicePortRingGeneration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVoicePortRingGeneration.setStatus("current")


class _AluVoicePortSignalingType_Type(Integer32):
    """Custom type aluVoicePortSignalingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loopStart", 1),
          ("loopCallingDisconnectClear", 2),
          ("privateLineAutomaticRingdown", 3))
    )


_AluVoicePortSignalingType_Type.__name__ = "Integer32"
_AluVoicePortSignalingType_Object = MibTableColumn
aluVoicePortSignalingType = _AluVoicePortSignalingType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 7, 1, 8),
    _AluVoicePortSignalingType_Type()
)
aluVoicePortSignalingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVoicePortSignalingType.setStatus("current")
_AluVoiceTable_Object = MibTable
aluVoiceTable = _AluVoiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8)
)
if mibBuilder.loadTexts:
    aluVoiceTable.setStatus("current")
_AluVoiceEntry_Object = MibTableRow
aluVoiceEntry = _AluVoiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1)
)
aluVoiceEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    aluVoiceEntry.setStatus("current")
_AluVoiceRowStatus_Type = RowStatus
_AluVoiceRowStatus_Object = MibTableColumn
aluVoiceRowStatus = _AluVoiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 1),
    _AluVoiceRowStatus_Type()
)
aluVoiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVoiceRowStatus.setStatus("current")
_AluVoiceLastChangeTime_Type = TimeStamp
_AluVoiceLastChangeTime_Object = MibTableColumn
aluVoiceLastChangeTime = _AluVoiceLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 2),
    _AluVoiceLastChangeTime_Type()
)
aluVoiceLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceLastChangeTime.setStatus("current")


class _AluVoiceType_Type(Integer32):
    """Custom type aluVoiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("em", 1),
          ("fxo", 2),
          ("fxs", 3))
    )


_AluVoiceType_Type.__name__ = "Integer32"
_AluVoiceType_Object = MibTableColumn
aluVoiceType = _AluVoiceType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 3),
    _AluVoiceType_Type()
)
aluVoiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceType.setStatus("current")


class _AluVoiceSignalingMode_Type(Integer32):
    """Custom type aluVoiceSignalingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("em", 1),
          ("transmissionOnly", 2))
    )


_AluVoiceSignalingMode_Type.__name__ = "Integer32"
_AluVoiceSignalingMode_Object = MibTableColumn
aluVoiceSignalingMode = _AluVoiceSignalingMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 4),
    _AluVoiceSignalingMode_Type()
)
aluVoiceSignalingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVoiceSignalingMode.setStatus("current")


class _AluVoiceLoopback_Type(Integer32):
    """Custom type aluVoiceLoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("internalAnalog", 2),
          ("internalDigital", 3))
    )


_AluVoiceLoopback_Type.__name__ = "Integer32"
_AluVoiceLoopback_Object = MibTableColumn
aluVoiceLoopback = _AluVoiceLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 5),
    _AluVoiceLoopback_Type()
)
aluVoiceLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVoiceLoopback.setStatus("current")


class _AluVoiceFaultSignaling_Type(Integer32):
    """Custom type aluVoiceFaultSignaling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("seized", 2))
    )


_AluVoiceFaultSignaling_Type.__name__ = "Integer32"
_AluVoiceFaultSignaling_Object = MibTableColumn
aluVoiceFaultSignaling = _AluVoiceFaultSignaling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 6),
    _AluVoiceFaultSignaling_Type()
)
aluVoiceFaultSignaling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVoiceFaultSignaling.setStatus("current")


class _AluVoiceSignalBitsState_Type(OctetString):
    """Custom type aluVoiceSignalBitsState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_AluVoiceSignalBitsState_Type.__name__ = "OctetString"
_AluVoiceSignalBitsState_Object = MibTableColumn
aluVoiceSignalBitsState = _AluVoiceSignalBitsState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 7),
    _AluVoiceSignalBitsState_Type()
)
aluVoiceSignalBitsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceSignalBitsState.setStatus("current")
_AluVoiceClockSource_Type = TmnxDSXClockSource
_AluVoiceClockSource_Object = MibTableColumn
aluVoiceClockSource = _AluVoiceClockSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 8),
    _AluVoiceClockSource_Type()
)
aluVoiceClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceClockSource.setStatus("current")


class _AluVoiceSignalingLeadE_Type(AluVoiceSignalingLead):
    """Custom type aluVoiceSignalingLeadE based on AluVoiceSignalingLead"""
    defaultValue = 3


_AluVoiceSignalingLeadE_Type.__name__ = "AluVoiceSignalingLead"
_AluVoiceSignalingLeadE_Object = MibTableColumn
aluVoiceSignalingLeadE = _AluVoiceSignalingLeadE_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 9),
    _AluVoiceSignalingLeadE_Type()
)
aluVoiceSignalingLeadE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVoiceSignalingLeadE.setStatus("current")


class _AluVoiceSignalingLeadM_Type(AluVoiceSignalingLead):
    """Custom type aluVoiceSignalingLeadM based on AluVoiceSignalingLead"""
    defaultValue = 3


_AluVoiceSignalingLeadM_Type.__name__ = "AluVoiceSignalingLead"
_AluVoiceSignalingLeadM_Object = MibTableColumn
aluVoiceSignalingLeadM = _AluVoiceSignalingLeadM_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 10),
    _AluVoiceSignalingLeadM_Type()
)
aluVoiceSignalingLeadM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVoiceSignalingLeadM.setStatus("current")


class _AluVoiceSignalingLeadsState_Type(OctetString):
    """Custom type aluVoiceSignalingLeadsState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_AluVoiceSignalingLeadsState_Type.__name__ = "OctetString"
_AluVoiceSignalingLeadsState_Object = MibTableColumn
aluVoiceSignalingLeadsState = _AluVoiceSignalingLeadsState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 11),
    _AluVoiceSignalingLeadsState_Type()
)
aluVoiceSignalingLeadsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceSignalingLeadsState.setStatus("current")


class _AluVoiceSignalMode_Type(Integer32):
    """Custom type aluVoiceSignalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("cas", 2))
    )


_AluVoiceSignalMode_Type.__name__ = "Integer32"
_AluVoiceSignalMode_Object = MibTableColumn
aluVoiceSignalMode = _AluVoiceSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 12),
    _AluVoiceSignalMode_Type()
)
aluVoiceSignalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceSignalMode.setStatus("current")


class _AluVoiceCallState_Type(Integer32):
    """Custom type aluVoiceCallState based on Integer32"""
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
        *(("outOfService", 1),
          ("idle", 2),
          ("incoming", 3),
          ("outgoing", 4),
          ("nonForwarding", 5))
    )


_AluVoiceCallState_Type.__name__ = "Integer32"
_AluVoiceCallState_Object = MibTableColumn
aluVoiceCallState = _AluVoiceCallState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 13),
    _AluVoiceCallState_Type()
)
aluVoiceCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceCallState.setStatus("current")
_AluVoiceIncomingCallCount_Type = Counter32
_AluVoiceIncomingCallCount_Object = MibTableColumn
aluVoiceIncomingCallCount = _AluVoiceIncomingCallCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 14),
    _AluVoiceIncomingCallCount_Type()
)
aluVoiceIncomingCallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceIncomingCallCount.setStatus("current")
_AluVoiceIncomingCallCountAns_Type = Counter32
_AluVoiceIncomingCallCountAns_Object = MibTableColumn
aluVoiceIncomingCallCountAns = _AluVoiceIncomingCallCountAns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 15),
    _AluVoiceIncomingCallCountAns_Type()
)
aluVoiceIncomingCallCountAns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceIncomingCallCountAns.setStatus("current")
_AluVoiceIncomingCallTime_Type = Counter32
_AluVoiceIncomingCallTime_Object = MibTableColumn
aluVoiceIncomingCallTime = _AluVoiceIncomingCallTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 16),
    _AluVoiceIncomingCallTime_Type()
)
aluVoiceIncomingCallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceIncomingCallTime.setStatus("current")
if mibBuilder.loadTexts:
    aluVoiceIncomingCallTime.setUnits("seconds")
_AluVoiceIncomingCallTimeAns_Type = Counter32
_AluVoiceIncomingCallTimeAns_Object = MibTableColumn
aluVoiceIncomingCallTimeAns = _AluVoiceIncomingCallTimeAns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 17),
    _AluVoiceIncomingCallTimeAns_Type()
)
aluVoiceIncomingCallTimeAns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceIncomingCallTimeAns.setStatus("current")
if mibBuilder.loadTexts:
    aluVoiceIncomingCallTimeAns.setUnits("seconds")
_AluVoiceOutgoingCallCount_Type = Counter32
_AluVoiceOutgoingCallCount_Object = MibTableColumn
aluVoiceOutgoingCallCount = _AluVoiceOutgoingCallCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 18),
    _AluVoiceOutgoingCallCount_Type()
)
aluVoiceOutgoingCallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceOutgoingCallCount.setStatus("current")
_AluVoiceOutgoingCallCountAns_Type = Counter32
_AluVoiceOutgoingCallCountAns_Object = MibTableColumn
aluVoiceOutgoingCallCountAns = _AluVoiceOutgoingCallCountAns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 19),
    _AluVoiceOutgoingCallCountAns_Type()
)
aluVoiceOutgoingCallCountAns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceOutgoingCallCountAns.setStatus("current")
_AluVoiceOutgoingCallTime_Type = Counter32
_AluVoiceOutgoingCallTime_Object = MibTableColumn
aluVoiceOutgoingCallTime = _AluVoiceOutgoingCallTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 20),
    _AluVoiceOutgoingCallTime_Type()
)
aluVoiceOutgoingCallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceOutgoingCallTime.setStatus("current")
if mibBuilder.loadTexts:
    aluVoiceOutgoingCallTime.setUnits("seconds")
_AluVoiceOutgoingCallTimeAns_Type = Counter32
_AluVoiceOutgoingCallTimeAns_Object = MibTableColumn
aluVoiceOutgoingCallTimeAns = _AluVoiceOutgoingCallTimeAns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 21),
    _AluVoiceOutgoingCallTimeAns_Type()
)
aluVoiceOutgoingCallTimeAns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceOutgoingCallTimeAns.setStatus("current")
if mibBuilder.loadTexts:
    aluVoiceOutgoingCallTimeAns.setUnits("seconds")
_AluVoiceOutOfServiceTime_Type = Counter32
_AluVoiceOutOfServiceTime_Object = MibTableColumn
aluVoiceOutOfServiceTime = _AluVoiceOutOfServiceTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 22),
    _AluVoiceOutOfServiceTime_Type()
)
aluVoiceOutOfServiceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceOutOfServiceTime.setStatus("current")
if mibBuilder.loadTexts:
    aluVoiceOutOfServiceTime.setUnits("seconds")
_AluVoiceIdleTime_Type = Counter32
_AluVoiceIdleTime_Object = MibTableColumn
aluVoiceIdleTime = _AluVoiceIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 23),
    _AluVoiceIdleTime_Type()
)
aluVoiceIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    aluVoiceIdleTime.setUnits("seconds")
_AluVoiceTotalCallCount_Type = Counter32
_AluVoiceTotalCallCount_Object = MibTableColumn
aluVoiceTotalCallCount = _AluVoiceTotalCallCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 24),
    _AluVoiceTotalCallCount_Type()
)
aluVoiceTotalCallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceTotalCallCount.setStatus("current")
_AluVoiceTotalCallTime_Type = Counter32
_AluVoiceTotalCallTime_Object = MibTableColumn
aluVoiceTotalCallTime = _AluVoiceTotalCallTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 25),
    _AluVoiceTotalCallTime_Type()
)
aluVoiceTotalCallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceTotalCallTime.setStatus("current")
if mibBuilder.loadTexts:
    aluVoiceTotalCallTime.setUnits("seconds")


class _AluVoiceIdleCode_Type(Unsigned32):
    """Custom type aluVoiceIdleCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AluVoiceIdleCode_Type.__name__ = "Unsigned32"
_AluVoiceIdleCode_Object = MibTableColumn
aluVoiceIdleCode = _AluVoiceIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 26),
    _AluVoiceIdleCode_Type()
)
aluVoiceIdleCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVoiceIdleCode.setStatus("current")


class _AluVoiceSeizedCode_Type(Unsigned32):
    """Custom type aluVoiceSeizedCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AluVoiceSeizedCode_Type.__name__ = "Unsigned32"
_AluVoiceSeizedCode_Object = MibTableColumn
aluVoiceSeizedCode = _AluVoiceSeizedCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 8, 1, 27),
    _AluVoiceSeizedCode_Type()
)
aluVoiceSeizedCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVoiceSeizedCode.setStatus("current")
_AluVoiceChanGroupTable_Object = MibTable
aluVoiceChanGroupTable = _AluVoiceChanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 9)
)
if mibBuilder.loadTexts:
    aluVoiceChanGroupTable.setStatus("current")
_AluVoiceChanGroupEntry_Object = MibTableRow
aluVoiceChanGroupEntry = _AluVoiceChanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 9, 1)
)
aluVoiceChanGroupEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    aluVoiceChanGroupEntry.setStatus("current")
_AluVoiceChanGroupRowStatus_Type = RowStatus
_AluVoiceChanGroupRowStatus_Object = MibTableColumn
aluVoiceChanGroupRowStatus = _AluVoiceChanGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 9, 1, 1),
    _AluVoiceChanGroupRowStatus_Type()
)
aluVoiceChanGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVoiceChanGroupRowStatus.setStatus("current")
_AluVoiceChanGroupMTU_Type = Unsigned32
_AluVoiceChanGroupMTU_Object = MibTableColumn
aluVoiceChanGroupMTU = _AluVoiceChanGroupMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 9, 1, 2),
    _AluVoiceChanGroupMTU_Type()
)
aluVoiceChanGroupMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceChanGroupMTU.setStatus("current")
if mibBuilder.loadTexts:
    aluVoiceChanGroupMTU.setUnits("bytes")
_AluVoiceChanGroupOperMTU_Type = Unsigned32
_AluVoiceChanGroupOperMTU_Object = MibTableColumn
aluVoiceChanGroupOperMTU = _AluVoiceChanGroupOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 9, 1, 3),
    _AluVoiceChanGroupOperMTU_Type()
)
aluVoiceChanGroupOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVoiceChanGroupOperMTU.setStatus("current")
if mibBuilder.loadTexts:
    aluVoiceChanGroupOperMTU.setUnits("bytes")
_AluGponPortTable_Object = MibTable
aluGponPortTable = _AluGponPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 10)
)
if mibBuilder.loadTexts:
    aluGponPortTable.setStatus("current")
_AluGponPortEntry_Object = MibTableRow
aluGponPortEntry = _AluGponPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 10, 1)
)
aluGponPortEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    aluGponPortEntry.setStatus("current")


class _AluGponPortG984SerialNumber_Type(OctetString):
    """Custom type aluGponPortG984SerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AluGponPortG984SerialNumber_Type.__name__ = "OctetString"
_AluGponPortG984SerialNumber_Object = MibTableColumn
aluGponPortG984SerialNumber = _AluGponPortG984SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 10, 1, 1),
    _AluGponPortG984SerialNumber_Type()
)
aluGponPortG984SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortG984SerialNumber.setStatus("current")


class _AluGponPortSubsLocId_Type(OctetString):
    """Custom type aluGponPortSubsLocId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AluGponPortSubsLocId_Type.__name__ = "OctetString"
_AluGponPortSubsLocId_Object = MibTableColumn
aluGponPortSubsLocId = _AluGponPortSubsLocId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 10, 1, 2),
    _AluGponPortSubsLocId_Type()
)
aluGponPortSubsLocId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluGponPortSubsLocId.setStatus("current")


class _AluGponPortActiveSwVersion_Type(OctetString):
    """Custom type aluGponPortActiveSwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_AluGponPortActiveSwVersion_Type.__name__ = "OctetString"
_AluGponPortActiveSwVersion_Object = MibTableColumn
aluGponPortActiveSwVersion = _AluGponPortActiveSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 10, 1, 3),
    _AluGponPortActiveSwVersion_Type()
)
aluGponPortActiveSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortActiveSwVersion.setStatus("current")


class _AluGponPortPonStatus_Type(Integer32):
    """Custom type aluGponPortPonStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 0),
          ("active", 1),
          ("hardwareFailure", 2),
          ("softwareFailure", 3),
          ("lossOfLink", 4),
          ("softwareDownload", 5),
          ("omciNotEstablished", 6),
          ("boot", 7),
          ("ranging", 8),
          ("busy", 9))
    )


_AluGponPortPonStatus_Type.__name__ = "Integer32"
_AluGponPortPonStatus_Object = MibTableColumn
aluGponPortPonStatus = _AluGponPortPonStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 10, 1, 4),
    _AluGponPortPonStatus_Type()
)
aluGponPortPonStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPonStatus.setStatus("current")


class _AluGponPortOntEnetStatus_Type(Integer32):
    """Custom type aluGponPortOntEnetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noLink", 0),
          ("active", 1))
    )


_AluGponPortOntEnetStatus_Type.__name__ = "Integer32"
_AluGponPortOntEnetStatus_Object = MibTableColumn
aluGponPortOntEnetStatus = _AluGponPortOntEnetStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 10, 1, 5),
    _AluGponPortOntEnetStatus_Type()
)
aluGponPortOntEnetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortOntEnetStatus.setStatus("current")


class _AluGponPortOntEnetSpeed_Type(Integer32):
    """Custom type aluGponPortOntEnetSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("halfDuplex10Mbps", 1),
          ("fullDuplex10Mbps", 2),
          ("halfDuplex100Mbps", 3),
          ("fullDuplex100Mbps", 4),
          ("halfDuplex1Gbps", 5),
          ("fullDuplex1Gbps", 6))
    )


_AluGponPortOntEnetSpeed_Type.__name__ = "Integer32"
_AluGponPortOntEnetSpeed_Object = MibTableColumn
aluGponPortOntEnetSpeed = _AluGponPortOntEnetSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 10, 1, 6),
    _AluGponPortOntEnetSpeed_Type()
)
aluGponPortOntEnetSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortOntEnetSpeed.setStatus("current")
_AluDslPortTable_Object = MibTable
aluDslPortTable = _AluDslPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 11)
)
if mibBuilder.loadTexts:
    aluDslPortTable.setStatus("current")
_AluDslPortEntry_Object = MibTableRow
aluDslPortEntry = _AluDslPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 11, 1)
)
aluDslPortEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    aluDslPortEntry.setStatus("current")
_AluDslPortBondingType_Type = AluDslTpsTcType
_AluDslPortBondingType_Object = MibTableColumn
aluDslPortBondingType = _AluDslPortBondingType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 11, 1, 1),
    _AluDslPortBondingType_Type()
)
aluDslPortBondingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDslPortBondingType.setStatus("current")


class _AluDslPortBondingState_Type(Integer32):
    """Custom type aluDslPortBondingState based on Integer32"""
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


_AluDslPortBondingState_Type.__name__ = "Integer32"
_AluDslPortBondingState_Object = MibTableColumn
aluDslPortBondingState = _AluDslPortBondingState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 11, 1, 2),
    _AluDslPortBondingState_Type()
)
aluDslPortBondingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDslPortBondingState.setStatus("current")
_AluDslPortBondingBitRateUS_Type = Unsigned32
_AluDslPortBondingBitRateUS_Object = MibTableColumn
aluDslPortBondingBitRateUS = _AluDslPortBondingBitRateUS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 11, 1, 3),
    _AluDslPortBondingBitRateUS_Type()
)
aluDslPortBondingBitRateUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDslPortBondingBitRateUS.setStatus("current")
_AluDslPortBondingBitRateDS_Type = Unsigned32
_AluDslPortBondingBitRateDS_Object = MibTableColumn
aluDslPortBondingBitRateDS = _AluDslPortBondingBitRateDS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 11, 1, 4),
    _AluDslPortBondingBitRateDS_Type()
)
aluDslPortBondingBitRateDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDslPortBondingBitRateDS.setStatus("current")


class _AluDslPortAtmVpi_Type(Integer32):
    """Custom type aluDslPortAtmVpi based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AluDslPortAtmVpi_Type.__name__ = "Integer32"
_AluDslPortAtmVpi_Object = MibTableColumn
aluDslPortAtmVpi = _AluDslPortAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 11, 1, 5),
    _AluDslPortAtmVpi_Type()
)
aluDslPortAtmVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluDslPortAtmVpi.setStatus("current")


class _AluDslPortAtmVci_Type(Integer32):
    """Custom type aluDslPortAtmVci based on Integer32"""
    defaultValue = 35

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_AluDslPortAtmVci_Type.__name__ = "Integer32"
_AluDslPortAtmVci_Object = MibTableColumn
aluDslPortAtmVci = _AluDslPortAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 11, 1, 6),
    _AluDslPortAtmVci_Type()
)
aluDslPortAtmVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluDslPortAtmVci.setStatus("current")


class _AluDslPortAtmF5OamLoopback_Type(Integer32):
    """Custom type aluDslPortAtmF5OamLoopback based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("active", 1))
    )


_AluDslPortAtmF5OamLoopback_Type.__name__ = "Integer32"
_AluDslPortAtmF5OamLoopback_Object = MibTableColumn
aluDslPortAtmF5OamLoopback = _AluDslPortAtmF5OamLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 11, 1, 7),
    _AluDslPortAtmF5OamLoopback_Type()
)
aluDslPortAtmF5OamLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluDslPortAtmF5OamLoopback.setStatus("current")


class _AluDslPortAtmF5OamLoopbackStatus_Type(Integer32):
    """Custom type aluDslPortAtmF5OamLoopbackStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("fail", 1),
          ("pass", 2))
    )


_AluDslPortAtmF5OamLoopbackStatus_Type.__name__ = "Integer32"
_AluDslPortAtmF5OamLoopbackStatus_Object = MibTableColumn
aluDslPortAtmF5OamLoopbackStatus = _AluDslPortAtmF5OamLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 11, 1, 8),
    _AluDslPortAtmF5OamLoopbackStatus_Type()
)
aluDslPortAtmF5OamLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDslPortAtmF5OamLoopbackStatus.setStatus("current")


class _AluDslPortAtmF5OamLoopbackTime_Type(Unsigned32):
    """Custom type aluDslPortAtmF5OamLoopbackTime based on Unsigned32"""
    defaultValue = 0


_AluDslPortAtmF5OamLoopbackTime_Type.__name__ = "Unsigned32"
_AluDslPortAtmF5OamLoopbackTime_Object = MibTableColumn
aluDslPortAtmF5OamLoopbackTime = _AluDslPortAtmF5OamLoopbackTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 11, 1, 9),
    _AluDslPortAtmF5OamLoopbackTime_Type()
)
aluDslPortAtmF5OamLoopbackTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDslPortAtmF5OamLoopbackTime.setStatus("current")


class _AluDslPortNtrDslLineID_Type(Integer32):
    """Custom type aluDslPortNtrDslLineID based on Integer32"""
    defaultValue = 0


_AluDslPortNtrDslLineID_Type.__name__ = "Integer32"
_AluDslPortNtrDslLineID_Object = MibTableColumn
aluDslPortNtrDslLineID = _AluDslPortNtrDslLineID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 11, 1, 10),
    _AluDslPortNtrDslLineID_Type()
)
aluDslPortNtrDslLineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDslPortNtrDslLineID.setStatus("current")


class _AluDslPortNtrLockedStatus_Type(Integer32):
    """Custom type aluDslPortNtrLockedStatus based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("freeRunning", -1),
          ("acquringLock", 0),
          ("preLock", 1),
          ("lock", 2),
          ("notSelected", 3))
    )


_AluDslPortNtrLockedStatus_Type.__name__ = "Integer32"
_AluDslPortNtrLockedStatus_Object = MibTableColumn
aluDslPortNtrLockedStatus = _AluDslPortNtrLockedStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 11, 1, 11),
    _AluDslPortNtrLockedStatus_Type()
)
aluDslPortNtrLockedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDslPortNtrLockedStatus.setStatus("current")


class _AluDslPortNtrStdDev_Type(Unsigned32):
    """Custom type aluDslPortNtrStdDev based on Unsigned32"""
    defaultValue = 0


_AluDslPortNtrStdDev_Type.__name__ = "Unsigned32"
_AluDslPortNtrStdDev_Object = MibTableColumn
aluDslPortNtrStdDev = _AluDslPortNtrStdDev_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 11, 1, 12),
    _AluDslPortNtrStdDev_Type()
)
aluDslPortNtrStdDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDslPortNtrStdDev.setStatus("current")


class _AluDslPortNtrMaxError_Type(Integer32):
    """Custom type aluDslPortNtrMaxError based on Integer32"""
    defaultValue = 0


_AluDslPortNtrMaxError_Type.__name__ = "Integer32"
_AluDslPortNtrMaxError_Object = MibTableColumn
aluDslPortNtrMaxError = _AluDslPortNtrMaxError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 11, 1, 13),
    _AluDslPortNtrMaxError_Type()
)
aluDslPortNtrMaxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDslPortNtrMaxError.setStatus("current")


class _AluDslPortNtrMinError_Type(Integer32):
    """Custom type aluDslPortNtrMinError based on Integer32"""
    defaultValue = 0


_AluDslPortNtrMinError_Type.__name__ = "Integer32"
_AluDslPortNtrMinError_Object = MibTableColumn
aluDslPortNtrMinError = _AluDslPortNtrMinError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 11, 1, 14),
    _AluDslPortNtrMinError_Type()
)
aluDslPortNtrMinError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDslPortNtrMinError.setStatus("current")


class _AluDslPortAdsl2Plus_Type(Integer32):
    """Custom type aluDslPortAdsl2Plus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("g992Dot5a", 0),
          ("g992Dot5b", 1))
    )


_AluDslPortAdsl2Plus_Type.__name__ = "Integer32"
_AluDslPortAdsl2Plus_Object = MibTableColumn
aluDslPortAdsl2Plus = _AluDslPortAdsl2Plus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 11, 1, 15),
    _AluDslPortAdsl2Plus_Type()
)
aluDslPortAdsl2Plus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluDslPortAdsl2Plus.setStatus("current")


class _AluDslPortNtrSampleClockPeriod_Type(Integer32):
    """Custom type aluDslPortNtrSampleClockPeriod based on Integer32"""
    defaultValue = 0


_AluDslPortNtrSampleClockPeriod_Type.__name__ = "Integer32"
_AluDslPortNtrSampleClockPeriod_Object = MibTableColumn
aluDslPortNtrSampleClockPeriod = _AluDslPortNtrSampleClockPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 11, 1, 16),
    _AluDslPortNtrSampleClockPeriod_Type()
)
aluDslPortNtrSampleClockPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDslPortNtrSampleClockPeriod.setStatus("current")


class _AluDslPortNtrErrorHistory_Type(OctetString):
    """Custom type aluDslPortNtrErrorHistory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )
    fixed_length = 256


_AluDslPortNtrErrorHistory_Type.__name__ = "OctetString"
_AluDslPortNtrErrorHistory_Object = MibTableColumn
aluDslPortNtrErrorHistory = _AluDslPortNtrErrorHistory_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 11, 1, 17),
    _AluDslPortNtrErrorHistory_Type()
)
aluDslPortNtrErrorHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDslPortNtrErrorHistory.setStatus("current")
_AluXdslLineTable_Object = MibTable
aluXdslLineTable = _AluXdslLineTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12)
)
if mibBuilder.loadTexts:
    aluXdslLineTable.setStatus("current")
_AluXdslLineEntry_Object = MibTableRow
aluXdslLineEntry = _AluXdslLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1)
)
aluXdslLineEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "ALU-PORT-MIB", "aluXdslLineID"),
)
if mibBuilder.loadTexts:
    aluXdslLineEntry.setStatus("current")


class _AluXdslLineID_Type(Unsigned32):
    """Custom type aluXdslLineID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AluXdslLineID_Type.__name__ = "Unsigned32"
_AluXdslLineID_Object = MibTableColumn
aluXdslLineID = _AluXdslLineID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 1),
    _AluXdslLineID_Type()
)
aluXdslLineID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluXdslLineID.setStatus("current")


class _AluXdslLineOperState_Type(Integer32):
    """Custom type aluXdslLineOperState based on Integer32"""
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


_AluXdslLineOperState_Type.__name__ = "Integer32"
_AluXdslLineOperState_Object = MibTableColumn
aluXdslLineOperState = _AluXdslLineOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 2),
    _AluXdslLineOperState_Type()
)
aluXdslLineOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineOperState.setStatus("current")


class _AluXdslLineState_Type(Integer32):
    """Custom type aluXdslLineState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("idlNcon", 0),
          ("idlConf", 1),
          ("runActi", 2),
          ("runInit", 3),
          ("runShow", 4),
          ("tstMode", 5),
          ("runLdInit", 6),
          ("idlLdDone", 7),
          ("runShowL2", 8))
    )


_AluXdslLineState_Type.__name__ = "Integer32"
_AluXdslLineState_Object = MibTableColumn
aluXdslLineState = _AluXdslLineState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 3),
    _AluXdslLineState_Type()
)
aluXdslLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineState.setStatus("current")


class _AluXdslLineProtocol_Type(Integer32):
    """Custom type aluXdslLineProtocol based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("none", -1),
          ("proc9921a", 0),
          ("proc9921b", 1),
          ("proc9921c", 2),
          ("proc9922a", 3),
          ("proc9922c", 4),
          ("proc9921h", 5),
          ("proc9921i", 6),
          ("proc9932", 7),
          ("proc9912a", 8),
          ("proc9912b", 9),
          ("proc9923a", 16),
          ("proc9923b", 17),
          ("proc9923i", 18),
          ("proc9923m", 19),
          ("proc9923j", 20),
          ("proc9924i", 21),
          ("proc9923l1", 22),
          ("proc9923l2", 23),
          ("proc9925a", 24),
          ("proc9925b", 25),
          ("proc9925i", 26),
          ("proc9925m", 27),
          ("proc9925j", 28),
          ("sadsl", 29),
          ("ansi", 30),
          ("etsi", 31))
    )


_AluXdslLineProtocol_Type.__name__ = "Integer32"
_AluXdslLineProtocol_Object = MibTableColumn
aluXdslLineProtocol = _AluXdslLineProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 4),
    _AluXdslLineProtocol_Type()
)
aluXdslLineProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineProtocol.setStatus("current")


class _AluXdslLineVdslProfile_Type(Integer32):
    """Custom type aluXdslLineVdslProfile based on Integer32"""
    defaultValue = 0

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("profile8a", 1),
          ("profile8b", 2),
          ("profile8c", 3),
          ("profile8d", 4),
          ("profile12a", 5),
          ("profile12b", 6),
          ("profile17a", 7),
          ("profile30a", 8),
          ("unknown", 9))
    )


_AluXdslLineVdslProfile_Type.__name__ = "Integer32"
_AluXdslLineVdslProfile_Object = MibTableColumn
aluXdslLineVdslProfile = _AluXdslLineVdslProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 5),
    _AluXdslLineVdslProfile_Type()
)
aluXdslLineVdslProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineVdslProfile.setStatus("current")
_AluXdslLineTpsTcType_Type = AluDslTpsTcType
_AluXdslLineTpsTcType_Object = MibTableColumn
aluXdslLineTpsTcType = _AluXdslLineTpsTcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 6),
    _AluXdslLineTpsTcType_Type()
)
aluXdslLineTpsTcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineTpsTcType.setStatus("current")
_AluXdslLineInBondingGroup_Type = TruthValue
_AluXdslLineInBondingGroup_Object = MibTableColumn
aluXdslLineInBondingGroup = _AluXdslLineInBondingGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 7),
    _AluXdslLineInBondingGroup_Type()
)
aluXdslLineInBondingGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineInBondingGroup.setStatus("current")
_AluXdslLineBitRateUS_Type = Unsigned32
_AluXdslLineBitRateUS_Object = MibTableColumn
aluXdslLineBitRateUS = _AluXdslLineBitRateUS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 8),
    _AluXdslLineBitRateUS_Type()
)
aluXdslLineBitRateUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineBitRateUS.setStatus("current")


class _AluXdslLineSnrMarginUS_Type(Integer32):
    """Custom type aluXdslLineSnrMarginUS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluXdslLineSnrMarginUS_Type.__name__ = "Integer32"
_AluXdslLineSnrMarginUS_Object = MibTableColumn
aluXdslLineSnrMarginUS = _AluXdslLineSnrMarginUS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 9),
    _AluXdslLineSnrMarginUS_Type()
)
aluXdslLineSnrMarginUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineSnrMarginUS.setStatus("current")


class _AluXdslLineOutputPowerUS_Type(Integer32):
    """Custom type aluXdslLineOutputPowerUS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluXdslLineOutputPowerUS_Type.__name__ = "Integer32"
_AluXdslLineOutputPowerUS_Object = MibTableColumn
aluXdslLineOutputPowerUS = _AluXdslLineOutputPowerUS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 10),
    _AluXdslLineOutputPowerUS_Type()
)
aluXdslLineOutputPowerUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineOutputPowerUS.setStatus("current")


class _AluXdslLineRefPsdUS_Type(Integer32):
    """Custom type aluXdslLineRefPsdUS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluXdslLineRefPsdUS_Type.__name__ = "Integer32"
_AluXdslLineRefPsdUS_Object = MibTableColumn
aluXdslLineRefPsdUS = _AluXdslLineRefPsdUS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 11),
    _AluXdslLineRefPsdUS_Type()
)
aluXdslLineRefPsdUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineRefPsdUS.setStatus("current")


class _AluXdslLineLoopDelayUS_Type(Integer32):
    """Custom type aluXdslLineLoopDelayUS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluXdslLineLoopDelayUS_Type.__name__ = "Integer32"
_AluXdslLineLoopDelayUS_Object = MibTableColumn
aluXdslLineLoopDelayUS = _AluXdslLineLoopDelayUS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 12),
    _AluXdslLineLoopDelayUS_Type()
)
aluXdslLineLoopDelayUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineLoopDelayUS.setStatus("current")
_AluXdslLineFailureUS_Type = Unsigned32
_AluXdslLineFailureUS_Object = MibTableColumn
aluXdslLineFailureUS = _AluXdslLineFailureUS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 13),
    _AluXdslLineFailureUS_Type()
)
aluXdslLineFailureUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineFailureUS.setStatus("current")


class _AluXdslLineB0DelayUS_Type(Unsigned32):
    """Custom type aluXdslLineB0DelayUS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AluXdslLineB0DelayUS_Type.__name__ = "Unsigned32"
_AluXdslLineB0DelayUS_Object = MibTableColumn
aluXdslLineB0DelayUS = _AluXdslLineB0DelayUS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 14),
    _AluXdslLineB0DelayUS_Type()
)
aluXdslLineB0DelayUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineB0DelayUS.setStatus("current")


class _AluXdslLineB0InpUS_Type(Unsigned32):
    """Custom type aluXdslLineB0InpUS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AluXdslLineB0InpUS_Type.__name__ = "Unsigned32"
_AluXdslLineB0InpUS_Object = MibTableColumn
aluXdslLineB0InpUS = _AluXdslLineB0InpUS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 15),
    _AluXdslLineB0InpUS_Type()
)
aluXdslLineB0InpUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineB0InpUS.setStatus("current")
_AluXdslLineBitRateDS_Type = Unsigned32
_AluXdslLineBitRateDS_Object = MibTableColumn
aluXdslLineBitRateDS = _AluXdslLineBitRateDS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 16),
    _AluXdslLineBitRateDS_Type()
)
aluXdslLineBitRateDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineBitRateDS.setStatus("current")


class _AluXdslLineSnrMarginDS_Type(Integer32):
    """Custom type aluXdslLineSnrMarginDS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluXdslLineSnrMarginDS_Type.__name__ = "Integer32"
_AluXdslLineSnrMarginDS_Object = MibTableColumn
aluXdslLineSnrMarginDS = _AluXdslLineSnrMarginDS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 17),
    _AluXdslLineSnrMarginDS_Type()
)
aluXdslLineSnrMarginDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineSnrMarginDS.setStatus("current")


class _AluXdslLineOutputPowerDS_Type(Integer32):
    """Custom type aluXdslLineOutputPowerDS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluXdslLineOutputPowerDS_Type.__name__ = "Integer32"
_AluXdslLineOutputPowerDS_Object = MibTableColumn
aluXdslLineOutputPowerDS = _AluXdslLineOutputPowerDS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 18),
    _AluXdslLineOutputPowerDS_Type()
)
aluXdslLineOutputPowerDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineOutputPowerDS.setStatus("current")


class _AluXdslLineRefPsdDS_Type(Integer32):
    """Custom type aluXdslLineRefPsdDS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluXdslLineRefPsdDS_Type.__name__ = "Integer32"
_AluXdslLineRefPsdDS_Object = MibTableColumn
aluXdslLineRefPsdDS = _AluXdslLineRefPsdDS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 19),
    _AluXdslLineRefPsdDS_Type()
)
aluXdslLineRefPsdDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineRefPsdDS.setStatus("current")


class _AluXdslLineLoopDelayDS_Type(Integer32):
    """Custom type aluXdslLineLoopDelayDS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluXdslLineLoopDelayDS_Type.__name__ = "Integer32"
_AluXdslLineLoopDelayDS_Object = MibTableColumn
aluXdslLineLoopDelayDS = _AluXdslLineLoopDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 20),
    _AluXdslLineLoopDelayDS_Type()
)
aluXdslLineLoopDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineLoopDelayDS.setStatus("current")
_AluXdslLineFailureDS_Type = Unsigned32
_AluXdslLineFailureDS_Object = MibTableColumn
aluXdslLineFailureDS = _AluXdslLineFailureDS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 21),
    _AluXdslLineFailureDS_Type()
)
aluXdslLineFailureDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineFailureDS.setStatus("current")


class _AluXdslLineB0DelayDS_Type(Unsigned32):
    """Custom type aluXdslLineB0DelayDS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AluXdslLineB0DelayDS_Type.__name__ = "Unsigned32"
_AluXdslLineB0DelayDS_Object = MibTableColumn
aluXdslLineB0DelayDS = _AluXdslLineB0DelayDS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 22),
    _AluXdslLineB0DelayDS_Type()
)
aluXdslLineB0DelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineB0DelayDS.setStatus("current")


class _AluXdslLineB0InpDS_Type(Unsigned32):
    """Custom type aluXdslLineB0InpDS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AluXdslLineB0InpDS_Type.__name__ = "Unsigned32"
_AluXdslLineB0InpDS_Object = MibTableColumn
aluXdslLineB0InpDS = _AluXdslLineB0InpDS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 23),
    _AluXdslLineB0InpDS_Type()
)
aluXdslLineB0InpDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineB0InpDS.setStatus("current")


class _AluXdslLineAdminState_Type(AluDslAdminState):
    """Custom type aluXdslLineAdminState based on AluDslAdminState"""
    defaultValue = 1


_AluXdslLineAdminState_Type.__name__ = "AluDslAdminState"
_AluXdslLineAdminState_Object = MibTableColumn
aluXdslLineAdminState = _AluXdslLineAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 12, 1, 24),
    _AluXdslLineAdminState_Type()
)
aluXdslLineAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluXdslLineAdminState.setStatus("current")
_AluShdslLineTable_Object = MibTable
aluShdslLineTable = _AluShdslLineTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 13)
)
if mibBuilder.loadTexts:
    aluShdslLineTable.setStatus("current")
_AluShdslLineEntry_Object = MibTableRow
aluShdslLineEntry = _AluShdslLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 13, 1)
)
aluShdslLineEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "ALU-PORT-MIB", "aluShdslLineID"),
)
if mibBuilder.loadTexts:
    aluShdslLineEntry.setStatus("current")
_AluShdslLineID_Type = Unsigned32
_AluShdslLineID_Object = MibTableColumn
aluShdslLineID = _AluShdslLineID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 13, 1, 1),
    _AluShdslLineID_Type()
)
aluShdslLineID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluShdslLineID.setStatus("current")
_AluShdslLineDataRate_Type = Unsigned32
_AluShdslLineDataRate_Object = MibTableColumn
aluShdslLineDataRate = _AluShdslLineDataRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 13, 1, 2),
    _AluShdslLineDataRate_Type()
)
aluShdslLineDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluShdslLineDataRate.setStatus("current")


class _AluShdslLineState_Type(Integer32):
    """Custom type aluShdslLineState based on Integer32"""
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
        *(("downNotReady", 0),
          ("downReady", 1),
          ("stopDownReady", 2),
          ("initializing", 3),
          ("upDateMode", 4))
    )


_AluShdslLineState_Type.__name__ = "Integer32"
_AluShdslLineState_Object = MibTableColumn
aluShdslLineState = _AluShdslLineState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 13, 1, 3),
    _AluShdslLineState_Type()
)
aluShdslLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluShdslLineState.setStatus("current")


class _AluShdslLineNegotiatedConst_Type(Integer32):
    """Custom type aluShdslLineNegotiatedConst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pmd16TcPAM", 0),
          ("pmd32TcPAM", 1))
    )


_AluShdslLineNegotiatedConst_Type.__name__ = "Integer32"
_AluShdslLineNegotiatedConst_Object = MibTableColumn
aluShdslLineNegotiatedConst = _AluShdslLineNegotiatedConst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 13, 1, 4),
    _AluShdslLineNegotiatedConst_Type()
)
aluShdslLineNegotiatedConst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluShdslLineNegotiatedConst.setStatus("current")


class _AluShdslLineUsedCaplist_Type(Integer32):
    """Custom type aluShdslLineUsedCaplist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("newStyleCapList", 0),
          ("oldStyleCapList", 1))
    )


_AluShdslLineUsedCaplist_Type.__name__ = "Integer32"
_AluShdslLineUsedCaplist_Object = MibTableColumn
aluShdslLineUsedCaplist = _AluShdslLineUsedCaplist_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 13, 1, 5),
    _AluShdslLineUsedCaplist_Type()
)
aluShdslLineUsedCaplist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluShdslLineUsedCaplist.setStatus("current")


class _AluShdslLineRegion_Type(Integer32):
    """Custom type aluShdslLineRegion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("annexAF", 0),
          ("annexBG", 1))
    )


_AluShdslLineRegion_Type.__name__ = "Integer32"
_AluShdslLineRegion_Object = MibTableColumn
aluShdslLineRegion = _AluShdslLineRegion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 13, 1, 6),
    _AluShdslLineRegion_Type()
)
aluShdslLineRegion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluShdslLineRegion.setStatus("current")


class _AluShdslLineCaplistMode_Type(Integer32):
    """Custom type aluShdslLineCaplistMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("newStyleCapList", 0),
          ("oldStyleCapList", 1),
          ("autoCapList", 2),
          ("autoTcDetect", 3))
    )


_AluShdslLineCaplistMode_Type.__name__ = "Integer32"
_AluShdslLineCaplistMode_Object = MibTableColumn
aluShdslLineCaplistMode = _AluShdslLineCaplistMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 13, 1, 7),
    _AluShdslLineCaplistMode_Type()
)
aluShdslLineCaplistMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluShdslLineCaplistMode.setStatus("current")
_AluShdslLineTpsTcType_Type = AluDslTpsTcType
_AluShdslLineTpsTcType_Object = MibTableColumn
aluShdslLineTpsTcType = _AluShdslLineTpsTcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 13, 1, 8),
    _AluShdslLineTpsTcType_Type()
)
aluShdslLineTpsTcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluShdslLineTpsTcType.setStatus("current")
_AluShdslLineInBondingGroup_Type = TruthValue
_AluShdslLineInBondingGroup_Object = MibTableColumn
aluShdslLineInBondingGroup = _AluShdslLineInBondingGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 13, 1, 9),
    _AluShdslLineInBondingGroup_Type()
)
aluShdslLineInBondingGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluShdslLineInBondingGroup.setStatus("current")


class _AluShdslLineAdminState_Type(AluDslAdminState):
    """Custom type aluShdslLineAdminState based on AluDslAdminState"""
    defaultValue = 1


_AluShdslLineAdminState_Type.__name__ = "AluDslAdminState"
_AluShdslLineAdminState_Object = MibTableColumn
aluShdslLineAdminState = _AluShdslLineAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 13, 1, 10),
    _AluShdslLineAdminState_Type()
)
aluShdslLineAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluShdslLineAdminState.setStatus("current")
_AluShdslLineLineAttenuation_Type = Unsigned32
_AluShdslLineLineAttenuation_Object = MibTableColumn
aluShdslLineLineAttenuation = _AluShdslLineLineAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 13, 1, 11),
    _AluShdslLineLineAttenuation_Type()
)
aluShdslLineLineAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluShdslLineLineAttenuation.setStatus("current")
_AluShdslLineRxSNRMargin_Type = Integer32
_AluShdslLineRxSNRMargin_Object = MibTableColumn
aluShdslLineRxSNRMargin = _AluShdslLineRxSNRMargin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 13, 1, 12),
    _AluShdslLineRxSNRMargin_Type()
)
aluShdslLineRxSNRMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluShdslLineRxSNRMargin.setStatus("current")
_AluShdslLinePowerBackOffValue_Type = Unsigned32
_AluShdslLinePowerBackOffValue_Object = MibTableColumn
aluShdslLinePowerBackOffValue = _AluShdslLinePowerBackOffValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 13, 1, 13),
    _AluShdslLinePowerBackOffValue_Type()
)
aluShdslLinePowerBackOffValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluShdslLinePowerBackOffValue.setStatus("current")
_AluDataPortTable_Object = MibTable
aluDataPortTable = _AluDataPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 14)
)
if mibBuilder.loadTexts:
    aluDataPortTable.setStatus("current")
_AluDataPortEntry_Object = MibTableRow
aluDataPortEntry = _AluDataPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 14, 1)
)
aluDataPortEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    aluDataPortEntry.setStatus("current")
_AluDataPortLastChangeTime_Type = TimeStamp
_AluDataPortLastChangeTime_Object = MibTableColumn
aluDataPortLastChangeTime = _AluDataPortLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 14, 1, 1),
    _AluDataPortLastChangeTime_Type()
)
aluDataPortLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDataPortLastChangeTime.setStatus("current")


class _AluDataPortType_Type(Integer32):
    """Custom type aluDataPortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("codir", 1),
          ("tpif", 2))
    )


_AluDataPortType_Type.__name__ = "Integer32"
_AluDataPortType_Object = MibTableColumn
aluDataPortType = _AluDataPortType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 14, 1, 2),
    _AluDataPortType_Type()
)
aluDataPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluDataPortType.setStatus("current")
_AluDataTable_Object = MibTable
aluDataTable = _AluDataTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 15)
)
if mibBuilder.loadTexts:
    aluDataTable.setStatus("current")
_AluDataEntry_Object = MibTableRow
aluDataEntry = _AluDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 15, 1)
)
aluDataEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    aluDataEntry.setStatus("current")
_AluDataRowStatus_Type = RowStatus
_AluDataRowStatus_Object = MibTableColumn
aluDataRowStatus = _AluDataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 15, 1, 1),
    _AluDataRowStatus_Type()
)
aluDataRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluDataRowStatus.setStatus("current")
_AluDataLastChangeTime_Type = TimeStamp
_AluDataLastChangeTime_Object = MibTableColumn
aluDataLastChangeTime = _AluDataLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 15, 1, 2),
    _AluDataLastChangeTime_Type()
)
aluDataLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDataLastChangeTime.setStatus("current")


class _AluDataType_Type(Integer32):
    """Custom type aluDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("codir", 1),
          ("tpif", 2))
    )


_AluDataType_Type.__name__ = "Integer32"
_AluDataType_Object = MibTableColumn
aluDataType = _AluDataType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 15, 1, 3),
    _AluDataType_Type()
)
aluDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDataType.setStatus("current")
_AluDataClockSource_Type = TmnxDSXClockSource
_AluDataClockSource_Object = MibTableColumn
aluDataClockSource = _AluDataClockSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 15, 1, 4),
    _AluDataClockSource_Type()
)
aluDataClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDataClockSource.setStatus("current")


class _AluDataTiming8k_Type(TmnxEnabledDisabled):
    """Custom type aluDataTiming8k based on TmnxEnabledDisabled"""
    defaultValue = 2


_AluDataTiming8k_Type.__name__ = "TmnxEnabledDisabled"
_AluDataTiming8k_Object = MibTableColumn
aluDataTiming8k = _AluDataTiming8k_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 15, 1, 5),
    _AluDataTiming8k_Type()
)
aluDataTiming8k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluDataTiming8k.setStatus("current")
_AluDataReportAlarm_Type = AluDataReportStatus
_AluDataReportAlarm_Object = MibTableColumn
aluDataReportAlarm = _AluDataReportAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 15, 1, 6),
    _AluDataReportAlarm_Type()
)
aluDataReportAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluDataReportAlarm.setStatus("current")
_AluDataReportAlarmStatus_Type = AluDataReportStatus
_AluDataReportAlarmStatus_Object = MibTableColumn
aluDataReportAlarmStatus = _AluDataReportAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 15, 1, 7),
    _AluDataReportAlarmStatus_Type()
)
aluDataReportAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDataReportAlarmStatus.setStatus("current")


class _AluDataLoopback_Type(Integer32):
    """Custom type aluDataLoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("internal", 2),
          ("line", 3))
    )


_AluDataLoopback_Type.__name__ = "Integer32"
_AluDataLoopback_Object = MibTableColumn
aluDataLoopback = _AluDataLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 15, 1, 8),
    _AluDataLoopback_Type()
)
aluDataLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluDataLoopback.setStatus("current")
_AluDataChanGroupTable_Object = MibTable
aluDataChanGroupTable = _AluDataChanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 16)
)
if mibBuilder.loadTexts:
    aluDataChanGroupTable.setStatus("current")
_AluDataChanGroupEntry_Object = MibTableRow
aluDataChanGroupEntry = _AluDataChanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 16, 1)
)
aluDataChanGroupEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    aluDataChanGroupEntry.setStatus("current")
_AluDataChanGroupRowStatus_Type = RowStatus
_AluDataChanGroupRowStatus_Object = MibTableColumn
aluDataChanGroupRowStatus = _AluDataChanGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 16, 1, 1),
    _AluDataChanGroupRowStatus_Type()
)
aluDataChanGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluDataChanGroupRowStatus.setStatus("current")
_AluDataChanGroupLastChangeTime_Type = TimeStamp
_AluDataChanGroupLastChangeTime_Object = MibTableColumn
aluDataChanGroupLastChangeTime = _AluDataChanGroupLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 16, 1, 2),
    _AluDataChanGroupLastChangeTime_Type()
)
aluDataChanGroupLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDataChanGroupLastChangeTime.setStatus("current")
_AluDataChanGroupMTU_Type = Unsigned32
_AluDataChanGroupMTU_Object = MibTableColumn
aluDataChanGroupMTU = _AluDataChanGroupMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 16, 1, 3),
    _AluDataChanGroupMTU_Type()
)
aluDataChanGroupMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDataChanGroupMTU.setStatus("current")
if mibBuilder.loadTexts:
    aluDataChanGroupMTU.setUnits("bytes")
_AluDataChanGroupOperMTU_Type = Unsigned32
_AluDataChanGroupOperMTU_Object = MibTableColumn
aluDataChanGroupOperMTU = _AluDataChanGroupOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 16, 1, 4),
    _AluDataChanGroupOperMTU_Type()
)
aluDataChanGroupOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDataChanGroupOperMTU.setStatus("current")
if mibBuilder.loadTexts:
    aluDataChanGroupOperMTU.setUnits("bytes")


class _AluDataChanGroupPayloadFillType_Type(TmnxDSXIdleFillType):
    """Custom type aluDataChanGroupPayloadFillType based on TmnxDSXIdleFillType"""
    defaultValue = 0


_AluDataChanGroupPayloadFillType_Type.__name__ = "TmnxDSXIdleFillType"
_AluDataChanGroupPayloadFillType_Object = MibTableColumn
aluDataChanGroupPayloadFillType = _AluDataChanGroupPayloadFillType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 16, 1, 5),
    _AluDataChanGroupPayloadFillType_Type()
)
aluDataChanGroupPayloadFillType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluDataChanGroupPayloadFillType.setStatus("current")


class _AluDataChanGroupPayloadPattern_Type(Unsigned32):
    """Custom type aluDataChanGroupPayloadPattern based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AluDataChanGroupPayloadPattern_Type.__name__ = "Unsigned32"
_AluDataChanGroupPayloadPattern_Object = MibTableColumn
aluDataChanGroupPayloadPattern = _AluDataChanGroupPayloadPattern_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 16, 1, 6),
    _AluDataChanGroupPayloadPattern_Type()
)
aluDataChanGroupPayloadPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluDataChanGroupPayloadPattern.setStatus("current")
_AluDataChanGroupTimeSlots_Type = TmnxDs0ChannelList
_AluDataChanGroupTimeSlots_Object = MibTableColumn
aluDataChanGroupTimeSlots = _AluDataChanGroupTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 16, 1, 7),
    _AluDataChanGroupTimeSlots_Type()
)
aluDataChanGroupTimeSlots.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluDataChanGroupTimeSlots.setStatus("current")
_AluExtTmnxDS0ChanGroupTable_Object = MibTable
aluExtTmnxDS0ChanGroupTable = _AluExtTmnxDS0ChanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 17)
)
if mibBuilder.loadTexts:
    aluExtTmnxDS0ChanGroupTable.setStatus("current")
_AluExtTmnxDS0ChanGroupEntry_Object = MibTableRow
aluExtTmnxDS0ChanGroupEntry = _AluExtTmnxDS0ChanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 17, 1)
)
if mibBuilder.loadTexts:
    aluExtTmnxDS0ChanGroupEntry.setStatus("current")


class _AluExtDS0ChanGroupSignalMode_Type(Integer32):
    """Custom type aluExtDS0ChanGroupSignalMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("cas", 2))
    )


_AluExtDS0ChanGroupSignalMode_Type.__name__ = "Integer32"
_AluExtDS0ChanGroupSignalMode_Object = MibTableColumn
aluExtDS0ChanGroupSignalMode = _AluExtDS0ChanGroupSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 4, 17, 1, 1),
    _AluExtDS0ChanGroupSignalMode_Type()
)
aluExtDS0ChanGroupSignalMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluExtDS0ChanGroupSignalMode.setStatus("current")
_AluPortNotificationObjects_ObjectIdentity = ObjectIdentity
aluPortNotificationObjects = _AluPortNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 7)
)


class _AluPortNotifyRS232AlarmReason_Type(Integer32):
    """Custom type aluPortNotifyRS232AlarmReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 0),
          ("hcmOof", 1),
          ("hcmRai", 2))
    )


_AluPortNotifyRS232AlarmReason_Type.__name__ = "Integer32"
_AluPortNotifyRS232AlarmReason_Object = MibScalar
aluPortNotifyRS232AlarmReason = _AluPortNotifyRS232AlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 7, 2),
    _AluPortNotifyRS232AlarmReason_Type()
)
aluPortNotifyRS232AlarmReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluPortNotifyRS232AlarmReason.setStatus("current")


class _AluPortNotifyDataAlarmReason_Type(Integer32):
    """Custom type aluPortNotifyDataAlarmReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 0),
          ("ais", 1),
          ("los", 2),
          ("rai", 3))
    )


_AluPortNotifyDataAlarmReason_Type.__name__ = "Integer32"
_AluPortNotifyDataAlarmReason_Object = MibScalar
aluPortNotifyDataAlarmReason = _AluPortNotifyDataAlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 7, 3),
    _AluPortNotifyDataAlarmReason_Type()
)
aluPortNotifyDataAlarmReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluPortNotifyDataAlarmReason.setStatus("current")
_AluPortStatsObjs_ObjectIdentity = ObjectIdentity
aluPortStatsObjs = _AluPortStatsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12)
)
_AluPortDiscardStatsTable_Object = MibTable
aluPortDiscardStatsTable = _AluPortDiscardStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 1)
)
if mibBuilder.loadTexts:
    aluPortDiscardStatsTable.setStatus("current")
_AluPortDiscardsStatsEntry_Object = MibTableRow
aluPortDiscardsStatsEntry = _AluPortDiscardsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 1, 1)
)
aluPortDiscardsStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    aluPortDiscardsStatsEntry.setStatus("current")
_AluPortInL2AddrProtoDiscards_Type = Counter64
_AluPortInL2AddrProtoDiscards_Object = MibTableColumn
aluPortInL2AddrProtoDiscards = _AluPortInL2AddrProtoDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 1, 1, 1),
    _AluPortInL2AddrProtoDiscards_Type()
)
aluPortInL2AddrProtoDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortInL2AddrProtoDiscards.setStatus("current")
_AluPortInMPLSLabelDiscards_Type = Counter64
_AluPortInMPLSLabelDiscards_Object = MibTableColumn
aluPortInMPLSLabelDiscards = _AluPortInMPLSLabelDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 1, 1, 2),
    _AluPortInMPLSLabelDiscards_Type()
)
aluPortInMPLSLabelDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortInMPLSLabelDiscards.setStatus("current")
_AluPortInIPAddrProtoDiscards_Type = Counter64
_AluPortInIPAddrProtoDiscards_Object = MibTableColumn
aluPortInIPAddrProtoDiscards = _AluPortInIPAddrProtoDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 1, 1, 3),
    _AluPortInIPAddrProtoDiscards_Type()
)
aluPortInIPAddrProtoDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortInIPAddrProtoDiscards.setStatus("current")
_AluPortInVlanIdDiscards_Type = Counter64
_AluPortInVlanIdDiscards_Object = MibTableColumn
aluPortInVlanIdDiscards = _AluPortInVlanIdDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 1, 1, 4),
    _AluPortInVlanIdDiscards_Type()
)
aluPortInVlanIdDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortInVlanIdDiscards.setStatus("current")
_AluPortInHdlcCrcDiscards_Type = Counter64
_AluPortInHdlcCrcDiscards_Object = MibTableColumn
aluPortInHdlcCrcDiscards = _AluPortInHdlcCrcDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 1, 1, 5),
    _AluPortInHdlcCrcDiscards_Type()
)
aluPortInHdlcCrcDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortInHdlcCrcDiscards.setStatus("current")
_AluPortOutPortMtuDiscards_Type = Counter64
_AluPortOutPortMtuDiscards_Object = MibTableColumn
aluPortOutPortMtuDiscards = _AluPortOutPortMtuDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 1, 1, 6),
    _AluPortOutPortMtuDiscards_Type()
)
aluPortOutPortMtuDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortOutPortMtuDiscards.setStatus("current")
_AluPortInCsmQHiPriDiscards_Type = Counter64
_AluPortInCsmQHiPriDiscards_Object = MibTableColumn
aluPortInCsmQHiPriDiscards = _AluPortInCsmQHiPriDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 1, 1, 7),
    _AluPortInCsmQHiPriDiscards_Type()
)
aluPortInCsmQHiPriDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortInCsmQHiPriDiscards.setStatus("current")
_AluPortInCsmQLowPriDiscards_Type = Counter64
_AluPortInCsmQLowPriDiscards_Object = MibTableColumn
aluPortInCsmQLowPriDiscards = _AluPortInCsmQLowPriDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 1, 1, 8),
    _AluPortInCsmQLowPriDiscards_Type()
)
aluPortInCsmQLowPriDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortInCsmQLowPriDiscards.setStatus("current")
_AluPortInCsmQFtpPriDiscards_Type = Counter64
_AluPortInCsmQFtpPriDiscards_Object = MibTableColumn
aluPortInCsmQFtpPriDiscards = _AluPortInCsmQFtpPriDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 1, 1, 9),
    _AluPortInCsmQFtpPriDiscards_Type()
)
aluPortInCsmQFtpPriDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortInCsmQFtpPriDiscards.setStatus("obsolete")
_AluPortOutCsmQDiscards_Type = Counter64
_AluPortOutCsmQDiscards_Object = MibTableColumn
aluPortOutCsmQDiscards = _AluPortOutCsmQDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 1, 1, 10),
    _AluPortOutCsmQDiscards_Type()
)
aluPortOutCsmQDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortOutCsmQDiscards.setStatus("current")
_AluPortInOtherDiscards_Type = Counter64
_AluPortInOtherDiscards_Object = MibTableColumn
aluPortInOtherDiscards = _AluPortInOtherDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 1, 1, 11),
    _AluPortInOtherDiscards_Type()
)
aluPortInOtherDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortInOtherDiscards.setStatus("current")
_AluPortOutOtherDiscards_Type = Counter64
_AluPortOutOtherDiscards_Object = MibTableColumn
aluPortOutOtherDiscards = _AluPortOutOtherDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 1, 1, 12),
    _AluPortOutOtherDiscards_Type()
)
aluPortOutOtherDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortOutOtherDiscards.setStatus("current")
_AluPortInCsmQMediumPriDiscards_Type = Counter64
_AluPortInCsmQMediumPriDiscards_Object = MibTableColumn
aluPortInCsmQMediumPriDiscards = _AluPortInCsmQMediumPriDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 1, 1, 13),
    _AluPortInCsmQMediumPriDiscards_Type()
)
aluPortInCsmQMediumPriDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortInCsmQMediumPriDiscards.setStatus("current")
_AluPortAcrClkStatsTable_Object = MibTable
aluPortAcrClkStatsTable = _AluPortAcrClkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 2)
)
if mibBuilder.loadTexts:
    aluPortAcrClkStatsTable.setStatus("current")
_AluPortAcrClkStatsEntry_Object = MibTableRow
aluPortAcrClkStatsEntry = _AluPortAcrClkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 2, 1)
)
aluPortAcrClkStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    aluPortAcrClkStatsEntry.setStatus("current")
_AluLastUpdateTime_Type = TimeStamp
_AluLastUpdateTime_Object = MibTableColumn
aluLastUpdateTime = _AluLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 2, 1, 1),
    _AluLastUpdateTime_Type()
)
aluLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLastUpdateTime.setStatus("current")
_AluTotalMinutesIn24Hour_Type = Unsigned32
_AluTotalMinutesIn24Hour_Object = MibTableColumn
aluTotalMinutesIn24Hour = _AluTotalMinutesIn24Hour_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 2, 1, 2),
    _AluTotalMinutesIn24Hour_Type()
)
aluTotalMinutesIn24Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluTotalMinutesIn24Hour.setStatus("current")
_AluCurrent24HourFreqOffsetMeanPpb_Type = Integer32
_AluCurrent24HourFreqOffsetMeanPpb_Object = MibTableColumn
aluCurrent24HourFreqOffsetMeanPpb = _AluCurrent24HourFreqOffsetMeanPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 2, 1, 3),
    _AluCurrent24HourFreqOffsetMeanPpb_Type()
)
aluCurrent24HourFreqOffsetMeanPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluCurrent24HourFreqOffsetMeanPpb.setStatus("current")
_AluCurrent24HourFreqOffsetStdDevPpb_Type = Unsigned32
_AluCurrent24HourFreqOffsetStdDevPpb_Object = MibTableColumn
aluCurrent24HourFreqOffsetStdDevPpb = _AluCurrent24HourFreqOffsetStdDevPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 2, 1, 4),
    _AluCurrent24HourFreqOffsetStdDevPpb_Type()
)
aluCurrent24HourFreqOffsetStdDevPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluCurrent24HourFreqOffsetStdDevPpb.setStatus("current")
_AluMaxShortIntervalMinutes_Type = Unsigned32
_AluMaxShortIntervalMinutes_Object = MibTableColumn
aluMaxShortIntervalMinutes = _AluMaxShortIntervalMinutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 2, 1, 5),
    _AluMaxShortIntervalMinutes_Type()
)
aluMaxShortIntervalMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMaxShortIntervalMinutes.setStatus("current")
_AluTotalShortIntervalMinutes_Type = Unsigned32
_AluTotalShortIntervalMinutes_Object = MibTableColumn
aluTotalShortIntervalMinutes = _AluTotalShortIntervalMinutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 2, 1, 6),
    _AluTotalShortIntervalMinutes_Type()
)
aluTotalShortIntervalMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluTotalShortIntervalMinutes.setStatus("current")
_AluCurrent1MinValidData_Type = TruthValue
_AluCurrent1MinValidData_Object = MibTableColumn
aluCurrent1MinValidData = _AluCurrent1MinValidData_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 2, 1, 7),
    _AluCurrent1MinValidData_Type()
)
aluCurrent1MinValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluCurrent1MinValidData.setStatus("current")
_AluCurrent1MinPhaseErrorMeanPpb_Type = Integer32
_AluCurrent1MinPhaseErrorMeanPpb_Object = MibTableColumn
aluCurrent1MinPhaseErrorMeanPpb = _AluCurrent1MinPhaseErrorMeanPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 2, 1, 8),
    _AluCurrent1MinPhaseErrorMeanPpb_Type()
)
aluCurrent1MinPhaseErrorMeanPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluCurrent1MinPhaseErrorMeanPpb.setStatus("current")
_AluCurrent1MinPhaseErrorStdDevNs_Type = Unsigned32
_AluCurrent1MinPhaseErrorStdDevNs_Object = MibTableColumn
aluCurrent1MinPhaseErrorStdDevNs = _AluCurrent1MinPhaseErrorStdDevNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 2, 1, 9),
    _AluCurrent1MinPhaseErrorStdDevNs_Type()
)
aluCurrent1MinPhaseErrorStdDevNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluCurrent1MinPhaseErrorStdDevNs.setStatus("current")
_AluCurrent1MinPhaseErrorMeanNs_Type = Integer32
_AluCurrent1MinPhaseErrorMeanNs_Object = MibTableColumn
aluCurrent1MinPhaseErrorMeanNs = _AluCurrent1MinPhaseErrorMeanNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 2, 1, 10),
    _AluCurrent1MinPhaseErrorMeanNs_Type()
)
aluCurrent1MinPhaseErrorMeanNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluCurrent1MinPhaseErrorMeanNs.setStatus("current")
_AluCurrent1MinFreqOffsetMeanPpb_Type = Integer32
_AluCurrent1MinFreqOffsetMeanPpb_Object = MibTableColumn
aluCurrent1MinFreqOffsetMeanPpb = _AluCurrent1MinFreqOffsetMeanPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 2, 1, 11),
    _AluCurrent1MinFreqOffsetMeanPpb_Type()
)
aluCurrent1MinFreqOffsetMeanPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluCurrent1MinFreqOffsetMeanPpb.setStatus("current")
_AluCurrent1MinFreqOffsetStdDevPpb_Type = Unsigned32
_AluCurrent1MinFreqOffsetStdDevPpb_Object = MibTableColumn
aluCurrent1MinFreqOffsetStdDevPpb = _AluCurrent1MinFreqOffsetStdDevPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 2, 1, 12),
    _AluCurrent1MinFreqOffsetStdDevPpb_Type()
)
aluCurrent1MinFreqOffsetStdDevPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluCurrent1MinFreqOffsetStdDevPpb.setStatus("current")
_AluPortAcrClkStatsShortIntervalTable_Object = MibTable
aluPortAcrClkStatsShortIntervalTable = _AluPortAcrClkStatsShortIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 3)
)
if mibBuilder.loadTexts:
    aluPortAcrClkStatsShortIntervalTable.setStatus("current")
_AluPortAcrClkStatsShortIntervalEntry_Object = MibTableRow
aluPortAcrClkStatsShortIntervalEntry = _AluPortAcrClkStatsShortIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 3, 1)
)
aluPortAcrClkStatsShortIntervalEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "ALU-PORT-MIB", "aluIntervalNumber"),
)
if mibBuilder.loadTexts:
    aluPortAcrClkStatsShortIntervalEntry.setStatus("current")


class _AluIntervalNumber_Type(Integer32):
    """Custom type aluIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AluIntervalNumber_Type.__name__ = "Integer32"
_AluIntervalNumber_Object = MibTableColumn
aluIntervalNumber = _AluIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 3, 1, 1),
    _AluIntervalNumber_Type()
)
aluIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIntervalNumber.setStatus("current")
_AluIntervalValidData_Type = TruthValue
_AluIntervalValidData_Object = MibTableColumn
aluIntervalValidData = _AluIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 3, 1, 2),
    _AluIntervalValidData_Type()
)
aluIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIntervalValidData.setStatus("current")
_AluIntervalUpdateTime_Type = TimeStamp
_AluIntervalUpdateTime_Object = MibTableColumn
aluIntervalUpdateTime = _AluIntervalUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 3, 1, 3),
    _AluIntervalUpdateTime_Type()
)
aluIntervalUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIntervalUpdateTime.setStatus("current")
_AluIntervalPhaseErrorMeanPpb_Type = Integer32
_AluIntervalPhaseErrorMeanPpb_Object = MibTableColumn
aluIntervalPhaseErrorMeanPpb = _AluIntervalPhaseErrorMeanPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 3, 1, 4),
    _AluIntervalPhaseErrorMeanPpb_Type()
)
aluIntervalPhaseErrorMeanPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIntervalPhaseErrorMeanPpb.setStatus("current")
_AluIntervalPhaseErrorStdDevNs_Type = Unsigned32
_AluIntervalPhaseErrorStdDevNs_Object = MibTableColumn
aluIntervalPhaseErrorStdDevNs = _AluIntervalPhaseErrorStdDevNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 3, 1, 5),
    _AluIntervalPhaseErrorStdDevNs_Type()
)
aluIntervalPhaseErrorStdDevNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIntervalPhaseErrorStdDevNs.setStatus("current")
_AluIntervalPhaseErrorMeanNs_Type = Integer32
_AluIntervalPhaseErrorMeanNs_Object = MibTableColumn
aluIntervalPhaseErrorMeanNs = _AluIntervalPhaseErrorMeanNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 3, 1, 6),
    _AluIntervalPhaseErrorMeanNs_Type()
)
aluIntervalPhaseErrorMeanNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIntervalPhaseErrorMeanNs.setStatus("current")
_AluIntervalFreqOffsetMeanPpb_Type = Integer32
_AluIntervalFreqOffsetMeanPpb_Object = MibTableColumn
aluIntervalFreqOffsetMeanPpb = _AluIntervalFreqOffsetMeanPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 3, 1, 7),
    _AluIntervalFreqOffsetMeanPpb_Type()
)
aluIntervalFreqOffsetMeanPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIntervalFreqOffsetMeanPpb.setStatus("current")
_AluIntervalFreqOffsetStdDevPpb_Type = Unsigned32
_AluIntervalFreqOffsetStdDevPpb_Object = MibTableColumn
aluIntervalFreqOffsetStdDevPpb = _AluIntervalFreqOffsetStdDevPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 3, 1, 8),
    _AluIntervalFreqOffsetStdDevPpb_Type()
)
aluIntervalFreqOffsetStdDevPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIntervalFreqOffsetStdDevPpb.setStatus("current")
_AluPortNetIngressControlStatsTable_Object = MibTable
aluPortNetIngressControlStatsTable = _AluPortNetIngressControlStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 4)
)
if mibBuilder.loadTexts:
    aluPortNetIngressControlStatsTable.setStatus("current")
_AluPortNetIngressControlStatsEntry_Object = MibTableRow
aluPortNetIngressControlStatsEntry = _AluPortNetIngressControlStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 4, 1)
)
aluPortNetIngressControlStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    aluPortNetIngressControlStatsEntry.setStatus("current")
_AluPortNetIngressControlFwdPkts_Type = Counter64
_AluPortNetIngressControlFwdPkts_Object = MibTableColumn
aluPortNetIngressControlFwdPkts = _AluPortNetIngressControlFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 4, 1, 1),
    _AluPortNetIngressControlFwdPkts_Type()
)
aluPortNetIngressControlFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortNetIngressControlFwdPkts.setStatus("current")
_AluPortNetIngressControlFwdOcts_Type = Counter64
_AluPortNetIngressControlFwdOcts_Object = MibTableColumn
aluPortNetIngressControlFwdOcts = _AluPortNetIngressControlFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 4, 1, 2),
    _AluPortNetIngressControlFwdOcts_Type()
)
aluPortNetIngressControlFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortNetIngressControlFwdOcts.setStatus("current")
_AluPortNetIngressControlDroPkts_Type = Counter64
_AluPortNetIngressControlDroPkts_Object = MibTableColumn
aluPortNetIngressControlDroPkts = _AluPortNetIngressControlDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 4, 1, 3),
    _AluPortNetIngressControlDroPkts_Type()
)
aluPortNetIngressControlDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortNetIngressControlDroPkts.setStatus("current")
_AluPortNetIngressControlDroOcts_Type = Counter64
_AluPortNetIngressControlDroOcts_Object = MibTableColumn
aluPortNetIngressControlDroOcts = _AluPortNetIngressControlDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 4, 1, 4),
    _AluPortNetIngressControlDroOcts_Type()
)
aluPortNetIngressControlDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortNetIngressControlDroOcts.setStatus("current")
_AluPortNetEgressControlStatsTable_Object = MibTable
aluPortNetEgressControlStatsTable = _AluPortNetEgressControlStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 5)
)
if mibBuilder.loadTexts:
    aluPortNetEgressControlStatsTable.setStatus("current")
_AluPortNetEgressControlStatsEntry_Object = MibTableRow
aluPortNetEgressControlStatsEntry = _AluPortNetEgressControlStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 5, 1)
)
aluPortNetEgressControlStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    aluPortNetEgressControlStatsEntry.setStatus("current")
_AluPortNetEgressControlFwdPkts_Type = Counter64
_AluPortNetEgressControlFwdPkts_Object = MibTableColumn
aluPortNetEgressControlFwdPkts = _AluPortNetEgressControlFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 5, 1, 1),
    _AluPortNetEgressControlFwdPkts_Type()
)
aluPortNetEgressControlFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortNetEgressControlFwdPkts.setStatus("current")
_AluPortNetEgressControlFwdOcts_Type = Counter64
_AluPortNetEgressControlFwdOcts_Object = MibTableColumn
aluPortNetEgressControlFwdOcts = _AluPortNetEgressControlFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 5, 1, 2),
    _AluPortNetEgressControlFwdOcts_Type()
)
aluPortNetEgressControlFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortNetEgressControlFwdOcts.setStatus("current")
_AluPortNetEgressControlDroPkts_Type = Counter64
_AluPortNetEgressControlDroPkts_Object = MibTableColumn
aluPortNetEgressControlDroPkts = _AluPortNetEgressControlDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 5, 1, 3),
    _AluPortNetEgressControlDroPkts_Type()
)
aluPortNetEgressControlDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortNetEgressControlDroPkts.setStatus("current")
_AluPortNetEgressControlDroOcts_Type = Counter64
_AluPortNetEgressControlDroOcts_Object = MibTableColumn
aluPortNetEgressControlDroOcts = _AluPortNetEgressControlDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 5, 1, 4),
    _AluPortNetEgressControlDroOcts_Type()
)
aluPortNetEgressControlDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortNetEgressControlDroOcts.setStatus("current")
_AluGponPortCurrentTable_Object = MibTable
aluGponPortCurrentTable = _AluGponPortCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6)
)
if mibBuilder.loadTexts:
    aluGponPortCurrentTable.setStatus("current")
_AluGponPortCurrentEntry_Object = MibTableRow
aluGponPortCurrentEntry = _AluGponPortCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1)
)
aluGponPortCurrentEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    aluGponPortCurrentEntry.setStatus("current")
_AluGponPortCurrentLastUpdTime_Type = TimeStamp
_AluGponPortCurrentLastUpdTime_Object = MibTableColumn
aluGponPortCurrentLastUpdTime = _AluGponPortCurrentLastUpdTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 1),
    _AluGponPortCurrentLastUpdTime_Type()
)
aluGponPortCurrentLastUpdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentLastUpdTime.setStatus("current")
_AluGponPortCurrentPMEnabled_Type = TruthValue
_AluGponPortCurrentPMEnabled_Object = MibTableColumn
aluGponPortCurrentPMEnabled = _AluGponPortCurrentPMEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 2),
    _AluGponPortCurrentPMEnabled_Type()
)
aluGponPortCurrentPMEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentPMEnabled.setStatus("current")
_AluGponPortCurrentTxFrames_Type = Counter32
_AluGponPortCurrentTxFrames_Object = MibTableColumn
aluGponPortCurrentTxFrames = _AluGponPortCurrentTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 3),
    _AluGponPortCurrentTxFrames_Type()
)
aluGponPortCurrentTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentTxFrames.setStatus("current")
_AluGponPortCurrentRxFrames_Type = Counter32
_AluGponPortCurrentRxFrames_Object = MibTableColumn
aluGponPortCurrentRxFrames = _AluGponPortCurrentRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 4),
    _AluGponPortCurrentRxFrames_Type()
)
aluGponPortCurrentRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentRxFrames.setStatus("current")
_AluGponPortCurrentTxBytes_Type = Counter32
_AluGponPortCurrentTxBytes_Object = MibTableColumn
aluGponPortCurrentTxBytes = _AluGponPortCurrentTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 5),
    _AluGponPortCurrentTxBytes_Type()
)
aluGponPortCurrentTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentTxBytes.setStatus("current")
_AluGponPortCurrentRxBytes_Type = Counter32
_AluGponPortCurrentRxBytes_Object = MibTableColumn
aluGponPortCurrentRxBytes = _AluGponPortCurrentRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 6),
    _AluGponPortCurrentRxBytes_Type()
)
aluGponPortCurrentRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentRxBytes.setStatus("current")
_AluGponPortCurrentDropFrsUp_Type = Counter32
_AluGponPortCurrentDropFrsUp_Object = MibTableColumn
aluGponPortCurrentDropFrsUp = _AluGponPortCurrentDropFrsUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 7),
    _AluGponPortCurrentDropFrsUp_Type()
)
aluGponPortCurrentDropFrsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentDropFrsUp.setStatus("current")
_AluGponPortCurrentDropFrsDn_Type = Counter32
_AluGponPortCurrentDropFrsDn_Object = MibTableColumn
aluGponPortCurrentDropFrsDn = _AluGponPortCurrentDropFrsDn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 8),
    _AluGponPortCurrentDropFrsDn_Type()
)
aluGponPortCurrentDropFrsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentDropFrsDn.setStatus("current")
_AluGponPortCurrentTxFrsMcast_Type = Counter32
_AluGponPortCurrentTxFrsMcast_Object = MibTableColumn
aluGponPortCurrentTxFrsMcast = _AluGponPortCurrentTxFrsMcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 9),
    _AluGponPortCurrentTxFrsMcast_Type()
)
aluGponPortCurrentTxFrsMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentTxFrsMcast.setStatus("current")
_AluGponPortCurrentRxFrsMcast_Type = Counter32
_AluGponPortCurrentRxFrsMcast_Object = MibTableColumn
aluGponPortCurrentRxFrsMcast = _AluGponPortCurrentRxFrsMcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 10),
    _AluGponPortCurrentRxFrsMcast_Type()
)
aluGponPortCurrentRxFrsMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentRxFrsMcast.setStatus("current")
_AluGponPortCurrentFCSEs_Type = Counter32
_AluGponPortCurrentFCSEs_Object = MibTableColumn
aluGponPortCurrentFCSEs = _AluGponPortCurrentFCSEs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 11),
    _AluGponPortCurrentFCSEs_Type()
)
aluGponPortCurrentFCSEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentFCSEs.setStatus("current")
_AluGponPortCurrentECs_Type = Counter32
_AluGponPortCurrentECs_Object = MibTableColumn
aluGponPortCurrentECs = _AluGponPortCurrentECs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 12),
    _AluGponPortCurrentECs_Type()
)
aluGponPortCurrentECs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentECs.setStatus("current")
_AluGponPortCurrentLCs_Type = Counter32
_AluGponPortCurrentLCs_Object = MibTableColumn
aluGponPortCurrentLCs = _AluGponPortCurrentLCs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 13),
    _AluGponPortCurrentLCs_Type()
)
aluGponPortCurrentLCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentLCs.setStatus("current")
_AluGponPortCurrentFTLs_Type = Counter32
_AluGponPortCurrentFTLs_Object = MibTableColumn
aluGponPortCurrentFTLs = _AluGponPortCurrentFTLs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 14),
    _AluGponPortCurrentFTLs_Type()
)
aluGponPortCurrentFTLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentFTLs.setStatus("current")
_AluGponPortCurrentRBOs_Type = Counter32
_AluGponPortCurrentRBOs_Object = MibTableColumn
aluGponPortCurrentRBOs = _AluGponPortCurrentRBOs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 15),
    _AluGponPortCurrentRBOs_Type()
)
aluGponPortCurrentRBOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentRBOs.setStatus("current")
_AluGponPortCurrentTBOs_Type = Counter32
_AluGponPortCurrentTBOs_Object = MibTableColumn
aluGponPortCurrentTBOs = _AluGponPortCurrentTBOs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 16),
    _AluGponPortCurrentTBOs_Type()
)
aluGponPortCurrentTBOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentTBOs.setStatus("current")
_AluGponPortCurrentSCFs_Type = Counter32
_AluGponPortCurrentSCFs_Object = MibTableColumn
aluGponPortCurrentSCFs = _AluGponPortCurrentSCFs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 17),
    _AluGponPortCurrentSCFs_Type()
)
aluGponPortCurrentSCFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentSCFs.setStatus("current")
_AluGponPortCurrentMCFs_Type = Counter32
_AluGponPortCurrentMCFs_Object = MibTableColumn
aluGponPortCurrentMCFs = _AluGponPortCurrentMCFs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 18),
    _AluGponPortCurrentMCFs_Type()
)
aluGponPortCurrentMCFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentMCFs.setStatus("current")
_AluGponPortCurrentSQEs_Type = Counter32
_AluGponPortCurrentSQEs_Object = MibTableColumn
aluGponPortCurrentSQEs = _AluGponPortCurrentSQEs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 19),
    _AluGponPortCurrentSQEs_Type()
)
aluGponPortCurrentSQEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentSQEs.setStatus("current")
_AluGponPortCurrentDTs_Type = Counter32
_AluGponPortCurrentDTs_Object = MibTableColumn
aluGponPortCurrentDTs = _AluGponPortCurrentDTs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 20),
    _AluGponPortCurrentDTs_Type()
)
aluGponPortCurrentDTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentDTs.setStatus("current")
_AluGponPortCurrentIMTEs_Type = Counter32
_AluGponPortCurrentIMTEs_Object = MibTableColumn
aluGponPortCurrentIMTEs = _AluGponPortCurrentIMTEs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 21),
    _AluGponPortCurrentIMTEs_Type()
)
aluGponPortCurrentIMTEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentIMTEs.setStatus("current")
_AluGponPortCurrentCSEs_Type = Counter32
_AluGponPortCurrentCSEs_Object = MibTableColumn
aluGponPortCurrentCSEs = _AluGponPortCurrentCSEs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 22),
    _AluGponPortCurrentCSEs_Type()
)
aluGponPortCurrentCSEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentCSEs.setStatus("current")
_AluGponPortCurrentAEs_Type = Counter32
_AluGponPortCurrentAEs_Object = MibTableColumn
aluGponPortCurrentAEs = _AluGponPortCurrentAEs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 23),
    _AluGponPortCurrentAEs_Type()
)
aluGponPortCurrentAEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentAEs.setStatus("current")
_AluGponPortCurrentIMREs_Type = Counter32
_AluGponPortCurrentIMREs_Object = MibTableColumn
aluGponPortCurrentIMREs = _AluGponPortCurrentIMREs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 24),
    _AluGponPortCurrentIMREs_Type()
)
aluGponPortCurrentIMREs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentIMREs.setStatus("current")
_AluGponPortCurrentLostFragsDn_Type = Counter32
_AluGponPortCurrentLostFragsDn_Object = MibTableColumn
aluGponPortCurrentLostFragsDn = _AluGponPortCurrentLostFragsDn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 25),
    _AluGponPortCurrentLostFragsDn_Type()
)
aluGponPortCurrentLostFragsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentLostFragsDn.setStatus("current")
_AluGponPortCurrentLostFragsUp_Type = Counter32
_AluGponPortCurrentLostFragsUp_Object = MibTableColumn
aluGponPortCurrentLostFragsUp = _AluGponPortCurrentLostFragsUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 26),
    _AluGponPortCurrentLostFragsUp_Type()
)
aluGponPortCurrentLostFragsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentLostFragsUp.setStatus("current")
_AluGponPortCurrentRxFrags_Type = Counter32
_AluGponPortCurrentRxFrags_Object = MibTableColumn
aluGponPortCurrentRxFrags = _AluGponPortCurrentRxFrags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 27),
    _AluGponPortCurrentRxFrags_Type()
)
aluGponPortCurrentRxFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentRxFrags.setStatus("current")
_AluGponPortCurrentRxBlocks_Type = Counter32
_AluGponPortCurrentRxBlocks_Object = MibTableColumn
aluGponPortCurrentRxBlocks = _AluGponPortCurrentRxBlocks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 28),
    _AluGponPortCurrentRxBlocks_Type()
)
aluGponPortCurrentRxBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentRxBlocks.setStatus("current")
_AluGponPortCurrentTxBlocks_Type = Counter32
_AluGponPortCurrentTxBlocks_Object = MibTableColumn
aluGponPortCurrentTxBlocks = _AluGponPortCurrentTxBlocks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 29),
    _AluGponPortCurrentTxBlocks_Type()
)
aluGponPortCurrentTxBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentTxBlocks.setStatus("current")
_AluGponPortCurrentTxFrags_Type = Counter32
_AluGponPortCurrentTxFrags_Object = MibTableColumn
aluGponPortCurrentTxFrags = _AluGponPortCurrentTxFrags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 30),
    _AluGponPortCurrentTxFrags_Type()
)
aluGponPortCurrentTxFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentTxFrags.setStatus("current")
_AluGponPortCurrentBadHeaders_Type = Counter32
_AluGponPortCurrentBadHeaders_Object = MibTableColumn
aluGponPortCurrentBadHeaders = _AluGponPortCurrentBadHeaders_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 6, 1, 31),
    _AluGponPortCurrentBadHeaders_Type()
)
aluGponPortCurrentBadHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortCurrentBadHeaders.setStatus("current")
_AluGponPortPreviousTable_Object = MibTable
aluGponPortPreviousTable = _AluGponPortPreviousTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7)
)
if mibBuilder.loadTexts:
    aluGponPortPreviousTable.setStatus("current")
_AluGponPortPreviousEntry_Object = MibTableRow
aluGponPortPreviousEntry = _AluGponPortPreviousEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1)
)
aluGponPortPreviousEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    aluGponPortPreviousEntry.setStatus("current")
_AluGponPortPreviousLastUpdTime_Type = TimeStamp
_AluGponPortPreviousLastUpdTime_Object = MibTableColumn
aluGponPortPreviousLastUpdTime = _AluGponPortPreviousLastUpdTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 1),
    _AluGponPortPreviousLastUpdTime_Type()
)
aluGponPortPreviousLastUpdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousLastUpdTime.setStatus("current")
_AluGponPortPreviousPMEnabled_Type = TruthValue
_AluGponPortPreviousPMEnabled_Object = MibTableColumn
aluGponPortPreviousPMEnabled = _AluGponPortPreviousPMEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 2),
    _AluGponPortPreviousPMEnabled_Type()
)
aluGponPortPreviousPMEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousPMEnabled.setStatus("current")
_AluGponPortPreviousTxFrames_Type = Counter32
_AluGponPortPreviousTxFrames_Object = MibTableColumn
aluGponPortPreviousTxFrames = _AluGponPortPreviousTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 3),
    _AluGponPortPreviousTxFrames_Type()
)
aluGponPortPreviousTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousTxFrames.setStatus("current")
_AluGponPortPreviousRxFrames_Type = Counter32
_AluGponPortPreviousRxFrames_Object = MibTableColumn
aluGponPortPreviousRxFrames = _AluGponPortPreviousRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 4),
    _AluGponPortPreviousRxFrames_Type()
)
aluGponPortPreviousRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousRxFrames.setStatus("current")
_AluGponPortPreviousTxBytes_Type = Counter32
_AluGponPortPreviousTxBytes_Object = MibTableColumn
aluGponPortPreviousTxBytes = _AluGponPortPreviousTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 5),
    _AluGponPortPreviousTxBytes_Type()
)
aluGponPortPreviousTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousTxBytes.setStatus("current")
_AluGponPortPreviousRxBytes_Type = Counter32
_AluGponPortPreviousRxBytes_Object = MibTableColumn
aluGponPortPreviousRxBytes = _AluGponPortPreviousRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 6),
    _AluGponPortPreviousRxBytes_Type()
)
aluGponPortPreviousRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousRxBytes.setStatus("current")
_AluGponPortPreviousDropFrsUp_Type = Counter32
_AluGponPortPreviousDropFrsUp_Object = MibTableColumn
aluGponPortPreviousDropFrsUp = _AluGponPortPreviousDropFrsUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 7),
    _AluGponPortPreviousDropFrsUp_Type()
)
aluGponPortPreviousDropFrsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousDropFrsUp.setStatus("current")
_AluGponPortPreviousDropFrsDn_Type = Counter32
_AluGponPortPreviousDropFrsDn_Object = MibTableColumn
aluGponPortPreviousDropFrsDn = _AluGponPortPreviousDropFrsDn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 8),
    _AluGponPortPreviousDropFrsDn_Type()
)
aluGponPortPreviousDropFrsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousDropFrsDn.setStatus("current")
_AluGponPortPreviousTxFrsMcast_Type = Counter32
_AluGponPortPreviousTxFrsMcast_Object = MibTableColumn
aluGponPortPreviousTxFrsMcast = _AluGponPortPreviousTxFrsMcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 9),
    _AluGponPortPreviousTxFrsMcast_Type()
)
aluGponPortPreviousTxFrsMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousTxFrsMcast.setStatus("current")
_AluGponPortPreviousRxFrsMcast_Type = Counter32
_AluGponPortPreviousRxFrsMcast_Object = MibTableColumn
aluGponPortPreviousRxFrsMcast = _AluGponPortPreviousRxFrsMcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 10),
    _AluGponPortPreviousRxFrsMcast_Type()
)
aluGponPortPreviousRxFrsMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousRxFrsMcast.setStatus("current")
_AluGponPortPreviousFCSEs_Type = Counter32
_AluGponPortPreviousFCSEs_Object = MibTableColumn
aluGponPortPreviousFCSEs = _AluGponPortPreviousFCSEs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 11),
    _AluGponPortPreviousFCSEs_Type()
)
aluGponPortPreviousFCSEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousFCSEs.setStatus("current")
_AluGponPortPreviousECs_Type = Counter32
_AluGponPortPreviousECs_Object = MibTableColumn
aluGponPortPreviousECs = _AluGponPortPreviousECs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 12),
    _AluGponPortPreviousECs_Type()
)
aluGponPortPreviousECs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousECs.setStatus("current")
_AluGponPortPreviousLCs_Type = Counter32
_AluGponPortPreviousLCs_Object = MibTableColumn
aluGponPortPreviousLCs = _AluGponPortPreviousLCs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 13),
    _AluGponPortPreviousLCs_Type()
)
aluGponPortPreviousLCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousLCs.setStatus("current")
_AluGponPortPreviousFTLs_Type = Counter32
_AluGponPortPreviousFTLs_Object = MibTableColumn
aluGponPortPreviousFTLs = _AluGponPortPreviousFTLs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 14),
    _AluGponPortPreviousFTLs_Type()
)
aluGponPortPreviousFTLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousFTLs.setStatus("current")
_AluGponPortPreviousRBOs_Type = Counter32
_AluGponPortPreviousRBOs_Object = MibTableColumn
aluGponPortPreviousRBOs = _AluGponPortPreviousRBOs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 15),
    _AluGponPortPreviousRBOs_Type()
)
aluGponPortPreviousRBOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousRBOs.setStatus("current")
_AluGponPortPreviousTBOs_Type = Counter32
_AluGponPortPreviousTBOs_Object = MibTableColumn
aluGponPortPreviousTBOs = _AluGponPortPreviousTBOs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 16),
    _AluGponPortPreviousTBOs_Type()
)
aluGponPortPreviousTBOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousTBOs.setStatus("current")
_AluGponPortPreviousSCFs_Type = Counter32
_AluGponPortPreviousSCFs_Object = MibTableColumn
aluGponPortPreviousSCFs = _AluGponPortPreviousSCFs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 17),
    _AluGponPortPreviousSCFs_Type()
)
aluGponPortPreviousSCFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousSCFs.setStatus("current")
_AluGponPortPreviousMCFs_Type = Counter32
_AluGponPortPreviousMCFs_Object = MibTableColumn
aluGponPortPreviousMCFs = _AluGponPortPreviousMCFs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 18),
    _AluGponPortPreviousMCFs_Type()
)
aluGponPortPreviousMCFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousMCFs.setStatus("current")
_AluGponPortPreviousSQEs_Type = Counter32
_AluGponPortPreviousSQEs_Object = MibTableColumn
aluGponPortPreviousSQEs = _AluGponPortPreviousSQEs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 19),
    _AluGponPortPreviousSQEs_Type()
)
aluGponPortPreviousSQEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousSQEs.setStatus("current")
_AluGponPortPreviousDTs_Type = Counter32
_AluGponPortPreviousDTs_Object = MibTableColumn
aluGponPortPreviousDTs = _AluGponPortPreviousDTs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 20),
    _AluGponPortPreviousDTs_Type()
)
aluGponPortPreviousDTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousDTs.setStatus("current")
_AluGponPortPreviousIMTEs_Type = Counter32
_AluGponPortPreviousIMTEs_Object = MibTableColumn
aluGponPortPreviousIMTEs = _AluGponPortPreviousIMTEs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 21),
    _AluGponPortPreviousIMTEs_Type()
)
aluGponPortPreviousIMTEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousIMTEs.setStatus("current")
_AluGponPortPreviousCSEs_Type = Counter32
_AluGponPortPreviousCSEs_Object = MibTableColumn
aluGponPortPreviousCSEs = _AluGponPortPreviousCSEs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 22),
    _AluGponPortPreviousCSEs_Type()
)
aluGponPortPreviousCSEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousCSEs.setStatus("current")
_AluGponPortPreviousAEs_Type = Counter32
_AluGponPortPreviousAEs_Object = MibTableColumn
aluGponPortPreviousAEs = _AluGponPortPreviousAEs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 23),
    _AluGponPortPreviousAEs_Type()
)
aluGponPortPreviousAEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousAEs.setStatus("current")
_AluGponPortPreviousIMREs_Type = Counter32
_AluGponPortPreviousIMREs_Object = MibTableColumn
aluGponPortPreviousIMREs = _AluGponPortPreviousIMREs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 24),
    _AluGponPortPreviousIMREs_Type()
)
aluGponPortPreviousIMREs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousIMREs.setStatus("current")
_AluGponPortPreviousLostFragsDn_Type = Counter32
_AluGponPortPreviousLostFragsDn_Object = MibTableColumn
aluGponPortPreviousLostFragsDn = _AluGponPortPreviousLostFragsDn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 25),
    _AluGponPortPreviousLostFragsDn_Type()
)
aluGponPortPreviousLostFragsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousLostFragsDn.setStatus("current")
_AluGponPortPreviousLostFragsUp_Type = Counter32
_AluGponPortPreviousLostFragsUp_Object = MibTableColumn
aluGponPortPreviousLostFragsUp = _AluGponPortPreviousLostFragsUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 26),
    _AluGponPortPreviousLostFragsUp_Type()
)
aluGponPortPreviousLostFragsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousLostFragsUp.setStatus("current")
_AluGponPortPreviousRxFrags_Type = Counter32
_AluGponPortPreviousRxFrags_Object = MibTableColumn
aluGponPortPreviousRxFrags = _AluGponPortPreviousRxFrags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 27),
    _AluGponPortPreviousRxFrags_Type()
)
aluGponPortPreviousRxFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousRxFrags.setStatus("current")
_AluGponPortPreviousRxBlocks_Type = Counter32
_AluGponPortPreviousRxBlocks_Object = MibTableColumn
aluGponPortPreviousRxBlocks = _AluGponPortPreviousRxBlocks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 28),
    _AluGponPortPreviousRxBlocks_Type()
)
aluGponPortPreviousRxBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousRxBlocks.setStatus("current")
_AluGponPortPreviousTxBlocks_Type = Counter32
_AluGponPortPreviousTxBlocks_Object = MibTableColumn
aluGponPortPreviousTxBlocks = _AluGponPortPreviousTxBlocks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 29),
    _AluGponPortPreviousTxBlocks_Type()
)
aluGponPortPreviousTxBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousTxBlocks.setStatus("current")
_AluGponPortPreviousTxFrags_Type = Counter32
_AluGponPortPreviousTxFrags_Object = MibTableColumn
aluGponPortPreviousTxFrags = _AluGponPortPreviousTxFrags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 30),
    _AluGponPortPreviousTxFrags_Type()
)
aluGponPortPreviousTxFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousTxFrags.setStatus("current")
_AluGponPortPreviousBadHeaders_Type = Counter32
_AluGponPortPreviousBadHeaders_Object = MibTableColumn
aluGponPortPreviousBadHeaders = _AluGponPortPreviousBadHeaders_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 7, 1, 31),
    _AluGponPortPreviousBadHeaders_Type()
)
aluGponPortPreviousBadHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluGponPortPreviousBadHeaders.setStatus("current")
_AluXdslLineStatsTable_Object = MibTable
aluXdslLineStatsTable = _AluXdslLineStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8)
)
if mibBuilder.loadTexts:
    aluXdslLineStatsTable.setStatus("current")
_AluXdslLineStatsEntry_Object = MibTableRow
aluXdslLineStatsEntry = _AluXdslLineStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8, 1)
)
aluXdslLineStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "ALU-PORT-MIB", "aluXdslLineID"),
)
if mibBuilder.loadTexts:
    aluXdslLineStatsEntry.setStatus("current")
_AluXdslLineStatsNearEndFECS_Type = Counter64
_AluXdslLineStatsNearEndFECS_Object = MibTableColumn
aluXdslLineStatsNearEndFECS = _AluXdslLineStatsNearEndFECS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8, 1, 1),
    _AluXdslLineStatsNearEndFECS_Type()
)
aluXdslLineStatsNearEndFECS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineStatsNearEndFECS.setStatus("current")
_AluXdslLineStatsNearEndLOSS_Type = Counter64
_AluXdslLineStatsNearEndLOSS_Object = MibTableColumn
aluXdslLineStatsNearEndLOSS = _AluXdslLineStatsNearEndLOSS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8, 1, 2),
    _AluXdslLineStatsNearEndLOSS_Type()
)
aluXdslLineStatsNearEndLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineStatsNearEndLOSS.setStatus("current")
_AluXdslLineStatsNearEndES_Type = Counter64
_AluXdslLineStatsNearEndES_Object = MibTableColumn
aluXdslLineStatsNearEndES = _AluXdslLineStatsNearEndES_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8, 1, 3),
    _AluXdslLineStatsNearEndES_Type()
)
aluXdslLineStatsNearEndES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineStatsNearEndES.setStatus("current")
_AluXdslLineStatsNearEndSES_Type = Counter64
_AluXdslLineStatsNearEndSES_Object = MibTableColumn
aluXdslLineStatsNearEndSES = _AluXdslLineStatsNearEndSES_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8, 1, 4),
    _AluXdslLineStatsNearEndSES_Type()
)
aluXdslLineStatsNearEndSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineStatsNearEndSES.setStatus("current")
_AluXdslLineStatsNearEndUAS_Type = Counter64
_AluXdslLineStatsNearEndUAS_Object = MibTableColumn
aluXdslLineStatsNearEndUAS = _AluXdslLineStatsNearEndUAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8, 1, 5),
    _AluXdslLineStatsNearEndUAS_Type()
)
aluXdslLineStatsNearEndUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineStatsNearEndUAS.setStatus("current")
_AluXdslLineStatsNearEndAS_Type = Counter64
_AluXdslLineStatsNearEndAS_Object = MibTableColumn
aluXdslLineStatsNearEndAS = _AluXdslLineStatsNearEndAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8, 1, 6),
    _AluXdslLineStatsNearEndAS_Type()
)
aluXdslLineStatsNearEndAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineStatsNearEndAS.setStatus("current")
_AluXdslLineStatsNearEndLOFS_Type = Counter64
_AluXdslLineStatsNearEndLOFS_Object = MibTableColumn
aluXdslLineStatsNearEndLOFS = _AluXdslLineStatsNearEndLOFS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8, 1, 7),
    _AluXdslLineStatsNearEndLOFS_Type()
)
aluXdslLineStatsNearEndLOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineStatsNearEndLOFS.setStatus("current")
_AluXdslLineStatsNearEndLPRS_Type = Counter64
_AluXdslLineStatsNearEndLPRS_Object = MibTableColumn
aluXdslLineStatsNearEndLPRS = _AluXdslLineStatsNearEndLPRS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8, 1, 8),
    _AluXdslLineStatsNearEndLPRS_Type()
)
aluXdslLineStatsNearEndLPRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineStatsNearEndLPRS.setStatus("current")
_AluXdslLineStatsNearEndLEFTRS_Type = Counter64
_AluXdslLineStatsNearEndLEFTRS_Object = MibTableColumn
aluXdslLineStatsNearEndLEFTRS = _AluXdslLineStatsNearEndLEFTRS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8, 1, 9),
    _AluXdslLineStatsNearEndLEFTRS_Type()
)
aluXdslLineStatsNearEndLEFTRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineStatsNearEndLEFTRS.setStatus("current")
_AluXdslLineStatsFarEndFECS_Type = Counter64
_AluXdslLineStatsFarEndFECS_Object = MibTableColumn
aluXdslLineStatsFarEndFECS = _AluXdslLineStatsFarEndFECS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8, 1, 10),
    _AluXdslLineStatsFarEndFECS_Type()
)
aluXdslLineStatsFarEndFECS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineStatsFarEndFECS.setStatus("current")
_AluXdslLineStatsFarEndLOSS_Type = Counter64
_AluXdslLineStatsFarEndLOSS_Object = MibTableColumn
aluXdslLineStatsFarEndLOSS = _AluXdslLineStatsFarEndLOSS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8, 1, 11),
    _AluXdslLineStatsFarEndLOSS_Type()
)
aluXdslLineStatsFarEndLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineStatsFarEndLOSS.setStatus("current")
_AluXdslLineStatsFarEndES_Type = Counter64
_AluXdslLineStatsFarEndES_Object = MibTableColumn
aluXdslLineStatsFarEndES = _AluXdslLineStatsFarEndES_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8, 1, 12),
    _AluXdslLineStatsFarEndES_Type()
)
aluXdslLineStatsFarEndES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineStatsFarEndES.setStatus("current")
_AluXdslLineStatsFarEndSES_Type = Counter64
_AluXdslLineStatsFarEndSES_Object = MibTableColumn
aluXdslLineStatsFarEndSES = _AluXdslLineStatsFarEndSES_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8, 1, 13),
    _AluXdslLineStatsFarEndSES_Type()
)
aluXdslLineStatsFarEndSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineStatsFarEndSES.setStatus("current")
_AluXdslLineStatsFarEndUAS_Type = Counter64
_AluXdslLineStatsFarEndUAS_Object = MibTableColumn
aluXdslLineStatsFarEndUAS = _AluXdslLineStatsFarEndUAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8, 1, 14),
    _AluXdslLineStatsFarEndUAS_Type()
)
aluXdslLineStatsFarEndUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineStatsFarEndUAS.setStatus("current")
_AluXdslLineStatsFarEndAS_Type = Counter64
_AluXdslLineStatsFarEndAS_Object = MibTableColumn
aluXdslLineStatsFarEndAS = _AluXdslLineStatsFarEndAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8, 1, 15),
    _AluXdslLineStatsFarEndAS_Type()
)
aluXdslLineStatsFarEndAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineStatsFarEndAS.setStatus("current")
_AluXdslLineStatsFarEndLOFS_Type = Counter64
_AluXdslLineStatsFarEndLOFS_Object = MibTableColumn
aluXdslLineStatsFarEndLOFS = _AluXdslLineStatsFarEndLOFS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8, 1, 16),
    _AluXdslLineStatsFarEndLOFS_Type()
)
aluXdslLineStatsFarEndLOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineStatsFarEndLOFS.setStatus("current")
_AluXdslLineStatsFarEndLPRS_Type = Counter64
_AluXdslLineStatsFarEndLPRS_Object = MibTableColumn
aluXdslLineStatsFarEndLPRS = _AluXdslLineStatsFarEndLPRS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8, 1, 17),
    _AluXdslLineStatsFarEndLPRS_Type()
)
aluXdslLineStatsFarEndLPRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineStatsFarEndLPRS.setStatus("current")
_AluXdslLineStatsFarEndLEFTRS_Type = Counter64
_AluXdslLineStatsFarEndLEFTRS_Object = MibTableColumn
aluXdslLineStatsFarEndLEFTRS = _AluXdslLineStatsFarEndLEFTRS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8, 1, 18),
    _AluXdslLineStatsFarEndLEFTRS_Type()
)
aluXdslLineStatsFarEndLEFTRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineStatsFarEndLEFTRS.setStatus("current")
_AluXdslLineStatsUpTime_Type = Unsigned32
_AluXdslLineStatsUpTime_Object = MibTableColumn
aluXdslLineStatsUpTime = _AluXdslLineStatsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 8, 1, 19),
    _AluXdslLineStatsUpTime_Type()
)
aluXdslLineStatsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluXdslLineStatsUpTime.setStatus("current")
_AluShdslLineStatsTable_Object = MibTable
aluShdslLineStatsTable = _AluShdslLineStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 9)
)
if mibBuilder.loadTexts:
    aluShdslLineStatsTable.setStatus("current")
_AluShdslLineStatsEntry_Object = MibTableRow
aluShdslLineStatsEntry = _AluShdslLineStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 9, 1)
)
aluShdslLineStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "ALU-PORT-MIB", "aluShdslLineID"),
)
if mibBuilder.loadTexts:
    aluShdslLineStatsEntry.setStatus("current")
_AluShdslLineStatsLinkLoss_Type = Counter64
_AluShdslLineStatsLinkLoss_Object = MibTableColumn
aluShdslLineStatsLinkLoss = _AluShdslLineStatsLinkLoss_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 9, 1, 2),
    _AluShdslLineStatsLinkLoss_Type()
)
aluShdslLineStatsLinkLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluShdslLineStatsLinkLoss.setStatus("current")
_AluShdslLineStatsCVError_Type = Counter64
_AluShdslLineStatsCVError_Object = MibTableColumn
aluShdslLineStatsCVError = _AluShdslLineStatsCVError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 9, 1, 4),
    _AluShdslLineStatsCVError_Type()
)
aluShdslLineStatsCVError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluShdslLineStatsCVError.setStatus("current")
_AluShdslLineStatsES_Type = Counter64
_AluShdslLineStatsES_Object = MibTableColumn
aluShdslLineStatsES = _AluShdslLineStatsES_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 9, 1, 5),
    _AluShdslLineStatsES_Type()
)
aluShdslLineStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluShdslLineStatsES.setStatus("current")
_AluShdslLineStatsSES_Type = Counter64
_AluShdslLineStatsSES_Object = MibTableColumn
aluShdslLineStatsSES = _AluShdslLineStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 9, 1, 6),
    _AluShdslLineStatsSES_Type()
)
aluShdslLineStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluShdslLineStatsSES.setStatus("current")
_AluShdslLineStatsLOSWS_Type = Counter64
_AluShdslLineStatsLOSWS_Object = MibTableColumn
aluShdslLineStatsLOSWS = _AluShdslLineStatsLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 9, 1, 7),
    _AluShdslLineStatsLOSWS_Type()
)
aluShdslLineStatsLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluShdslLineStatsLOSWS.setStatus("current")
_AluShdslLineStatsUAS_Type = Counter64
_AluShdslLineStatsUAS_Object = MibTableColumn
aluShdslLineStatsUAS = _AluShdslLineStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 9, 1, 8),
    _AluShdslLineStatsUAS_Type()
)
aluShdslLineStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluShdslLineStatsUAS.setStatus("current")
_AluShdslLineStatsInvalidDataFlag_Type = Integer32
_AluShdslLineStatsInvalidDataFlag_Object = MibTableColumn
aluShdslLineStatsInvalidDataFlag = _AluShdslLineStatsInvalidDataFlag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 9, 1, 10),
    _AluShdslLineStatsInvalidDataFlag_Type()
)
aluShdslLineStatsInvalidDataFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluShdslLineStatsInvalidDataFlag.setStatus("current")
_AluPortCtlStatsTable_Object = MibTable
aluPortCtlStatsTable = _AluPortCtlStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 10)
)
if mibBuilder.loadTexts:
    aluPortCtlStatsTable.setStatus("current")
_AluPortCtlStatsEntry_Object = MibTableRow
aluPortCtlStatsEntry = _AluPortCtlStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 10, 1)
)
aluPortCtlStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    aluPortCtlStatsEntry.setStatus("current")
_AluPortAccessCtlInFwdPkts_Type = Counter64
_AluPortAccessCtlInFwdPkts_Object = MibTableColumn
aluPortAccessCtlInFwdPkts = _AluPortAccessCtlInFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 10, 1, 1),
    _AluPortAccessCtlInFwdPkts_Type()
)
aluPortAccessCtlInFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortAccessCtlInFwdPkts.setStatus("current")
_AluPortAccessCtlInFwdOcts_Type = Counter64
_AluPortAccessCtlInFwdOcts_Object = MibTableColumn
aluPortAccessCtlInFwdOcts = _AluPortAccessCtlInFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 10, 1, 2),
    _AluPortAccessCtlInFwdOcts_Type()
)
aluPortAccessCtlInFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortAccessCtlInFwdOcts.setStatus("current")
_AluPortAccessCtlInDroPkts_Type = Counter64
_AluPortAccessCtlInDroPkts_Object = MibTableColumn
aluPortAccessCtlInDroPkts = _AluPortAccessCtlInDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 10, 1, 3),
    _AluPortAccessCtlInDroPkts_Type()
)
aluPortAccessCtlInDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortAccessCtlInDroPkts.setStatus("current")
_AluPortAccessCtlInDroOcts_Type = Counter64
_AluPortAccessCtlInDroOcts_Object = MibTableColumn
aluPortAccessCtlInDroOcts = _AluPortAccessCtlInDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 10, 1, 4),
    _AluPortAccessCtlInDroOcts_Type()
)
aluPortAccessCtlInDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortAccessCtlInDroOcts.setStatus("current")
_AluPortAccessCtlEgrFwdPkts_Type = Counter64
_AluPortAccessCtlEgrFwdPkts_Object = MibTableColumn
aluPortAccessCtlEgrFwdPkts = _AluPortAccessCtlEgrFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 10, 1, 5),
    _AluPortAccessCtlEgrFwdPkts_Type()
)
aluPortAccessCtlEgrFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortAccessCtlEgrFwdPkts.setStatus("current")
_AluPortAccessCtlEgrFwdOcts_Type = Counter64
_AluPortAccessCtlEgrFwdOcts_Object = MibTableColumn
aluPortAccessCtlEgrFwdOcts = _AluPortAccessCtlEgrFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 10, 1, 6),
    _AluPortAccessCtlEgrFwdOcts_Type()
)
aluPortAccessCtlEgrFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortAccessCtlEgrFwdOcts.setStatus("current")
_AluPortAccessCtlEgrDroPkts_Type = Counter64
_AluPortAccessCtlEgrDroPkts_Object = MibTableColumn
aluPortAccessCtlEgrDroPkts = _AluPortAccessCtlEgrDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 10, 1, 7),
    _AluPortAccessCtlEgrDroPkts_Type()
)
aluPortAccessCtlEgrDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortAccessCtlEgrDroPkts.setStatus("current")
_AluPortAccessCtlEgrDroOcts_Type = Counter64
_AluPortAccessCtlEgrDroOcts_Object = MibTableColumn
aluPortAccessCtlEgrDroOcts = _AluPortAccessCtlEgrDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 10, 1, 8),
    _AluPortAccessCtlEgrDroOcts_Type()
)
aluPortAccessCtlEgrDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPortAccessCtlEgrDroOcts.setStatus("current")
_AluFrIfStatsTable_Object = MibTable
aluFrIfStatsTable = _AluFrIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11)
)
if mibBuilder.loadTexts:
    aluFrIfStatsTable.setStatus("current")
_AluFrIfStatsEntry_Object = MibTableRow
aluFrIfStatsEntry = _AluFrIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1)
)
if mibBuilder.loadTexts:
    aluFrIfStatsEntry.setStatus("current")
_AluFrIfRxFrames_Type = Counter64
_AluFrIfRxFrames_Object = MibTableColumn
aluFrIfRxFrames = _AluFrIfRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 1),
    _AluFrIfRxFrames_Type()
)
aluFrIfRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfRxFrames.setStatus("current")
_AluFrIfRxOctets_Type = Counter64
_AluFrIfRxOctets_Object = MibTableColumn
aluFrIfRxOctets = _AluFrIfRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 2),
    _AluFrIfRxOctets_Type()
)
aluFrIfRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfRxOctets.setStatus("current")
_AluFrIfRxDEFrames_Type = Counter64
_AluFrIfRxDEFrames_Object = MibTableColumn
aluFrIfRxDEFrames = _AluFrIfRxDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 3),
    _AluFrIfRxDEFrames_Type()
)
aluFrIfRxDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfRxDEFrames.setStatus("current")
_AluFrIfRxDEOctets_Type = Counter64
_AluFrIfRxDEOctets_Object = MibTableColumn
aluFrIfRxDEOctets = _AluFrIfRxDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 4),
    _AluFrIfRxDEOctets_Type()
)
aluFrIfRxDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfRxDEOctets.setStatus("current")
_AluFrIfRxFECNFrames_Type = Counter64
_AluFrIfRxFECNFrames_Object = MibTableColumn
aluFrIfRxFECNFrames = _AluFrIfRxFECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 5),
    _AluFrIfRxFECNFrames_Type()
)
aluFrIfRxFECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfRxFECNFrames.setStatus("current")
_AluFrIfRxBECNFrames_Type = Counter64
_AluFrIfRxBECNFrames_Object = MibTableColumn
aluFrIfRxBECNFrames = _AluFrIfRxBECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 6),
    _AluFrIfRxBECNFrames_Type()
)
aluFrIfRxBECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfRxBECNFrames.setStatus("current")
_AluFrIfTxFrames_Type = Counter64
_AluFrIfTxFrames_Object = MibTableColumn
aluFrIfTxFrames = _AluFrIfTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 7),
    _AluFrIfTxFrames_Type()
)
aluFrIfTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfTxFrames.setStatus("current")
_AluFrIfTxOctets_Type = Counter64
_AluFrIfTxOctets_Object = MibTableColumn
aluFrIfTxOctets = _AluFrIfTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 8),
    _AluFrIfTxOctets_Type()
)
aluFrIfTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfTxOctets.setStatus("current")
_AluFrIfTxDEFrames_Type = Counter64
_AluFrIfTxDEFrames_Object = MibTableColumn
aluFrIfTxDEFrames = _AluFrIfTxDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 9),
    _AluFrIfTxDEFrames_Type()
)
aluFrIfTxDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfTxDEFrames.setStatus("current")
_AluFrIfTxDEOctets_Type = Counter64
_AluFrIfTxDEOctets_Object = MibTableColumn
aluFrIfTxDEOctets = _AluFrIfTxDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 10),
    _AluFrIfTxDEOctets_Type()
)
aluFrIfTxDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfTxDEOctets.setStatus("current")
_AluFrIfTxFECNFrames_Type = Counter64
_AluFrIfTxFECNFrames_Object = MibTableColumn
aluFrIfTxFECNFrames = _AluFrIfTxFECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 11),
    _AluFrIfTxFECNFrames_Type()
)
aluFrIfTxFECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfTxFECNFrames.setStatus("current")
_AluFrIfTxBECNFrames_Type = Counter64
_AluFrIfTxBECNFrames_Object = MibTableColumn
aluFrIfTxBECNFrames = _AluFrIfTxBECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 12),
    _AluFrIfTxBECNFrames_Type()
)
aluFrIfTxBECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfTxBECNFrames.setStatus("current")
_AluFrIfRxDiscardsInvalidDlci_Type = Counter64
_AluFrIfRxDiscardsInvalidDlci_Object = MibTableColumn
aluFrIfRxDiscardsInvalidDlci = _AluFrIfRxDiscardsInvalidDlci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 13),
    _AluFrIfRxDiscardsInvalidDlci_Type()
)
aluFrIfRxDiscardsInvalidDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfRxDiscardsInvalidDlci.setStatus("current")
_AluFrIfRxLastInvalidDlci_Type = Counter64
_AluFrIfRxLastInvalidDlci_Object = MibTableColumn
aluFrIfRxLastInvalidDlci = _AluFrIfRxLastInvalidDlci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 14),
    _AluFrIfRxLastInvalidDlci_Type()
)
aluFrIfRxLastInvalidDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfRxLastInvalidDlci.setStatus("current")
_AluFrIfRxDiscardsCrcErrors_Type = Counter64
_AluFrIfRxDiscardsCrcErrors_Object = MibTableColumn
aluFrIfRxDiscardsCrcErrors = _AluFrIfRxDiscardsCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 15),
    _AluFrIfRxDiscardsCrcErrors_Type()
)
aluFrIfRxDiscardsCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfRxDiscardsCrcErrors.setStatus("current")
_AluFrIfRxDiscardsAlignmentErrors_Type = Counter64
_AluFrIfRxDiscardsAlignmentErrors_Object = MibTableColumn
aluFrIfRxDiscardsAlignmentErrors = _AluFrIfRxDiscardsAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 16),
    _AluFrIfRxDiscardsAlignmentErrors_Type()
)
aluFrIfRxDiscardsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfRxDiscardsAlignmentErrors.setStatus("current")
_AluFrIfRxDiscardsLengthViolations_Type = Counter64
_AluFrIfRxDiscardsLengthViolations_Object = MibTableColumn
aluFrIfRxDiscardsLengthViolations = _AluFrIfRxDiscardsLengthViolations_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 17),
    _AluFrIfRxDiscardsLengthViolations_Type()
)
aluFrIfRxDiscardsLengthViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfRxDiscardsLengthViolations.setStatus("current")
_AluFrIfRxDiscardsIllegalHeader_Type = Counter64
_AluFrIfRxDiscardsIllegalHeader_Object = MibTableColumn
aluFrIfRxDiscardsIllegalHeader = _AluFrIfRxDiscardsIllegalHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 18),
    _AluFrIfRxDiscardsIllegalHeader_Type()
)
aluFrIfRxDiscardsIllegalHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfRxDiscardsIllegalHeader.setStatus("current")
_AluFrIfRxDiscardsOtherErrors_Type = Counter64
_AluFrIfRxDiscardsOtherErrors_Object = MibTableColumn
aluFrIfRxDiscardsOtherErrors = _AluFrIfRxDiscardsOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 19),
    _AluFrIfRxDiscardsOtherErrors_Type()
)
aluFrIfRxDiscardsOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfRxDiscardsOtherErrors.setStatus("current")
_AluFrIfTxDiscardsUnderruns_Type = Counter64
_AluFrIfTxDiscardsUnderruns_Object = MibTableColumn
aluFrIfTxDiscardsUnderruns = _AluFrIfTxDiscardsUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 20),
    _AluFrIfTxDiscardsUnderruns_Type()
)
aluFrIfTxDiscardsUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfTxDiscardsUnderruns.setStatus("current")
_AluFrIfTxDiscardsOtherErrors_Type = Counter64
_AluFrIfTxDiscardsOtherErrors_Object = MibTableColumn
aluFrIfTxDiscardsOtherErrors = _AluFrIfTxDiscardsOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 11, 1, 21),
    _AluFrIfTxDiscardsOtherErrors_Type()
)
aluFrIfTxDiscardsOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFrIfTxDiscardsOtherErrors.setStatus("current")
_AluExtFrCircuitTable_Object = MibTable
aluExtFrCircuitTable = _AluExtFrCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 12)
)
if mibBuilder.loadTexts:
    aluExtFrCircuitTable.setStatus("current")
_AluExtFrCircuitEntry_Object = MibTableRow
aluExtFrCircuitEntry = _AluExtFrCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 12, 1)
)
if mibBuilder.loadTexts:
    aluExtFrCircuitEntry.setStatus("current")
_AluExtFrCircuitReceivedCrcDiscards_Type = Counter32
_AluExtFrCircuitReceivedCrcDiscards_Object = MibTableColumn
aluExtFrCircuitReceivedCrcDiscards = _AluExtFrCircuitReceivedCrcDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 12, 1, 1),
    _AluExtFrCircuitReceivedCrcDiscards_Type()
)
aluExtFrCircuitReceivedCrcDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtFrCircuitReceivedCrcDiscards.setStatus("current")
_AluExtFrCircuitReceivedAborts_Type = Counter32
_AluExtFrCircuitReceivedAborts_Object = MibTableColumn
aluExtFrCircuitReceivedAborts = _AluExtFrCircuitReceivedAborts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 12, 1, 2),
    _AluExtFrCircuitReceivedAborts_Type()
)
aluExtFrCircuitReceivedAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtFrCircuitReceivedAborts.setStatus("current")
_AluExtFrCircuitReceivedOtherDiscards_Type = Counter32
_AluExtFrCircuitReceivedOtherDiscards_Object = MibTableColumn
aluExtFrCircuitReceivedOtherDiscards = _AluExtFrCircuitReceivedOtherDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 12, 1, 3),
    _AluExtFrCircuitReceivedOtherDiscards_Type()
)
aluExtFrCircuitReceivedOtherDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtFrCircuitReceivedOtherDiscards.setStatus("current")
_AluExtFrCircuitSentAborts_Type = Counter32
_AluExtFrCircuitSentAborts_Object = MibTableColumn
aluExtFrCircuitSentAborts = _AluExtFrCircuitSentAborts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 12, 1, 4),
    _AluExtFrCircuitSentAborts_Type()
)
aluExtFrCircuitSentAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtFrCircuitSentAborts.setStatus("current")
_AluExtFrCircuitSentFECNs_Type = Counter32
_AluExtFrCircuitSentFECNs_Object = MibTableColumn
aluExtFrCircuitSentFECNs = _AluExtFrCircuitSentFECNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 12, 1, 5),
    _AluExtFrCircuitSentFECNs_Type()
)
aluExtFrCircuitSentFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtFrCircuitSentFECNs.setStatus("current")
_AluExtFrCircuitSentBECNs_Type = Counter32
_AluExtFrCircuitSentBECNs_Object = MibTableColumn
aluExtFrCircuitSentBECNs = _AluExtFrCircuitSentBECNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 12, 1, 6),
    _AluExtFrCircuitSentBECNs_Type()
)
aluExtFrCircuitSentBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtFrCircuitSentBECNs.setStatus("current")
_AluExtFrCircuitReceivedDEOctets_Type = Counter32
_AluExtFrCircuitReceivedDEOctets_Object = MibTableColumn
aluExtFrCircuitReceivedDEOctets = _AluExtFrCircuitReceivedDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 12, 1, 7),
    _AluExtFrCircuitReceivedDEOctets_Type()
)
aluExtFrCircuitReceivedDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtFrCircuitReceivedDEOctets.setStatus("current")
_AluExtFrCircuitSentDEOctets_Type = Counter32
_AluExtFrCircuitSentDEOctets_Object = MibTableColumn
aluExtFrCircuitSentDEOctets = _AluExtFrCircuitSentDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 12, 1, 8),
    _AluExtFrCircuitSentDEOctets_Type()
)
aluExtFrCircuitSentDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtFrCircuitSentDEOctets.setStatus("current")
_AluEthPtpTimestampStatsTable_Object = MibTable
aluEthPtpTimestampStatsTable = _AluEthPtpTimestampStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 13)
)
if mibBuilder.loadTexts:
    aluEthPtpTimestampStatsTable.setStatus("current")
_AluEthPtpTimestampStatsEntry_Object = MibTableRow
aluEthPtpTimestampStatsEntry = _AluEthPtpTimestampStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 13, 1)
)
aluEthPtpTimestampStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    aluEthPtpTimestampStatsEntry.setStatus("current")
_AluEthPtpInSyncPktTimestamped_Type = Counter64
_AluEthPtpInSyncPktTimestamped_Object = MibTableColumn
aluEthPtpInSyncPktTimestamped = _AluEthPtpInSyncPktTimestamped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 13, 1, 1),
    _AluEthPtpInSyncPktTimestamped_Type()
)
aluEthPtpInSyncPktTimestamped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluEthPtpInSyncPktTimestamped.setStatus("current")
_AluEthPtpOutSyncPktTimestamped_Type = Counter64
_AluEthPtpOutSyncPktTimestamped_Object = MibTableColumn
aluEthPtpOutSyncPktTimestamped = _AluEthPtpOutSyncPktTimestamped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 13, 1, 2),
    _AluEthPtpOutSyncPktTimestamped_Type()
)
aluEthPtpOutSyncPktTimestamped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluEthPtpOutSyncPktTimestamped.setStatus("current")
_AluEthPtpInDelReqPktTimestamped_Type = Counter64
_AluEthPtpInDelReqPktTimestamped_Object = MibTableColumn
aluEthPtpInDelReqPktTimestamped = _AluEthPtpInDelReqPktTimestamped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 13, 1, 3),
    _AluEthPtpInDelReqPktTimestamped_Type()
)
aluEthPtpInDelReqPktTimestamped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluEthPtpInDelReqPktTimestamped.setStatus("current")
_AluEthPtpOutDelReqPktTimestamped_Type = Counter64
_AluEthPtpOutDelReqPktTimestamped_Object = MibTableColumn
aluEthPtpOutDelReqPktTimestamped = _AluEthPtpOutDelReqPktTimestamped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 13, 1, 4),
    _AluEthPtpOutDelReqPktTimestamped_Type()
)
aluEthPtpOutDelReqPktTimestamped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluEthPtpOutDelReqPktTimestamped.setStatus("current")
_AluEthPtpInFcsErrorCount_Type = Counter64
_AluEthPtpInFcsErrorCount_Object = MibTableColumn
aluEthPtpInFcsErrorCount = _AluEthPtpInFcsErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 13, 1, 5),
    _AluEthPtpInFcsErrorCount_Type()
)
aluEthPtpInFcsErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluEthPtpInFcsErrorCount.setStatus("current")
_AluEthPtpOutFcsErrorCount_Type = Counter64
_AluEthPtpOutFcsErrorCount_Object = MibTableColumn
aluEthPtpOutFcsErrorCount = _AluEthPtpOutFcsErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 12, 13, 1, 6),
    _AluEthPtpOutFcsErrorCount_Type()
)
aluEthPtpOutFcsErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluEthPtpOutFcsErrorCount.setStatus("current")
_AluPortNotifyPrefix_ObjectIdentity = ObjectIdentity
aluPortNotifyPrefix = _AluPortNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 2)
)
_AluPortNotification_ObjectIdentity = ObjectIdentity
aluPortNotification = _AluPortNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 2, 0)
)
tmnxDS1PortEntry.registerAugmentions(
    ("ALU-PORT-MIB",
     "aluExtTmnxDS1PortEntry")
)
aluExtTmnxDS1PortEntry.setIndexNames(*tmnxDS1PortEntry.getIndexNames())
tmnxPortEtherEntry.registerAugmentions(
    ("ALU-PORT-MIB",
     "aluExtTmnxPortEtherEntry")
)
aluExtTmnxPortEtherEntry.setIndexNames(*tmnxPortEtherEntry.getIndexNames())
tmnxDS1Entry.registerAugmentions(
    ("ALU-PORT-MIB",
     "aluExtTmnxDS1Entry")
)
aluExtTmnxDS1Entry.setIndexNames(*tmnxDS1Entry.getIndexNames())
tmnxDS0ChanGroupEntry.registerAugmentions(
    ("ALU-PORT-MIB",
     "aluExtTmnxDS0ChanGroupEntry")
)
aluExtTmnxDS0ChanGroupEntry.setIndexNames(*tmnxDS0ChanGroupEntry.getIndexNames())
tmnxFrIntfEntry.registerAugmentions(
    ("ALU-PORT-MIB",
     "aluFrIfStatsEntry")
)
aluFrIfStatsEntry.setIndexNames(*tmnxFrIntfEntry.getIndexNames())
frCircuitEntry.registerAugmentions(
    ("ALU-PORT-MIB",
     "aluExtFrCircuitEntry")
)
aluExtFrCircuitEntry.setIndexNames(*frCircuitEntry.getIndexNames())

# Managed Objects groups

aluExtDS1PortLineImpedanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 1)
)
aluExtDS1PortLineImpedanceGroup.setObjects(
    ("ALU-PORT-MIB", "aluExtDS1PortLineImpedance")
)
if mibBuilder.loadTexts:
    aluExtDS1PortLineImpedanceGroup.setStatus("current")

aluPortDiscardStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 2)
)
aluPortDiscardStatsGroup.setObjects(
      *(("ALU-PORT-MIB", "aluPortInL2AddrProtoDiscards"),
        ("ALU-PORT-MIB", "aluPortInMPLSLabelDiscards"),
        ("ALU-PORT-MIB", "aluPortInIPAddrProtoDiscards"),
        ("ALU-PORT-MIB", "aluPortInVlanIdDiscards"),
        ("ALU-PORT-MIB", "aluPortInHdlcCrcDiscards"),
        ("ALU-PORT-MIB", "aluPortOutPortMtuDiscards"),
        ("ALU-PORT-MIB", "aluPortInCsmQHiPriDiscards"),
        ("ALU-PORT-MIB", "aluPortInCsmQLowPriDiscards"),
        ("ALU-PORT-MIB", "aluPortInCsmQFtpPriDiscards"),
        ("ALU-PORT-MIB", "aluPortOutCsmQDiscards"),
        ("ALU-PORT-MIB", "aluPortInOtherDiscards"),
        ("ALU-PORT-MIB", "aluPortOutOtherDiscards"))
)
if mibBuilder.loadTexts:
    aluPortDiscardStatsGroup.setStatus("obsolete")

aluExtPortEtherSfpSyncEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 3)
)
aluExtPortEtherSfpSyncEGroup.setObjects(
    ("ALU-PORT-MIB", "aluExtPortEtherSfpSyncEStatus")
)
if mibBuilder.loadTexts:
    aluExtPortEtherSfpSyncEGroup.setStatus("current")

aluPortAcrClkStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 5)
)
aluPortAcrClkStatsGroup.setObjects(
      *(("ALU-PORT-MIB", "aluLastUpdateTime"),
        ("ALU-PORT-MIB", "aluTotalMinutesIn24Hour"),
        ("ALU-PORT-MIB", "aluCurrent24HourFreqOffsetMeanPpb"),
        ("ALU-PORT-MIB", "aluCurrent24HourFreqOffsetStdDevPpb"),
        ("ALU-PORT-MIB", "aluMaxShortIntervalMinutes"),
        ("ALU-PORT-MIB", "aluTotalShortIntervalMinutes"),
        ("ALU-PORT-MIB", "aluCurrent1MinValidData"),
        ("ALU-PORT-MIB", "aluCurrent1MinPhaseErrorMeanPpb"),
        ("ALU-PORT-MIB", "aluCurrent1MinPhaseErrorStdDevNs"),
        ("ALU-PORT-MIB", "aluCurrent1MinPhaseErrorMeanNs"),
        ("ALU-PORT-MIB", "aluCurrent1MinFreqOffsetMeanPpb"),
        ("ALU-PORT-MIB", "aluCurrent1MinFreqOffsetStdDevPpb"),
        ("ALU-PORT-MIB", "aluIntervalNumber"),
        ("ALU-PORT-MIB", "aluIntervalValidData"),
        ("ALU-PORT-MIB", "aluIntervalUpdateTime"),
        ("ALU-PORT-MIB", "aluIntervalPhaseErrorMeanPpb"),
        ("ALU-PORT-MIB", "aluIntervalPhaseErrorStdDevNs"),
        ("ALU-PORT-MIB", "aluIntervalPhaseErrorMeanNs"),
        ("ALU-PORT-MIB", "aluIntervalFreqOffsetMeanPpb"),
        ("ALU-PORT-MIB", "aluIntervalFreqOffsetStdDevPpb"))
)
if mibBuilder.loadTexts:
    aluPortAcrClkStatsGroup.setStatus("current")

aluExtDS1HoldTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 6)
)
aluExtDS1HoldTimeGroup.setObjects(
      *(("ALU-PORT-MIB", "aluExtDS1HoldTimeUp"),
        ("ALU-PORT-MIB", "aluExtDS1HoldTimeDown"))
)
if mibBuilder.loadTexts:
    aluExtDS1HoldTimeGroup.setStatus("current")

aluRS232GroupV2v1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 7)
)
aluRS232GroupV2v1.setObjects(
      *(("ALU-PORT-MIB", "aluRS232PortLastChangeTime"),
        ("ALU-PORT-MIB", "aluRS232PortType"),
        ("ALU-PORT-MIB", "aluRS232RowStatus"),
        ("ALU-PORT-MIB", "aluRS232LastChangeTime"),
        ("ALU-PORT-MIB", "aluRS232Type"),
        ("ALU-PORT-MIB", "aluRS232DeviceMode"),
        ("ALU-PORT-MIB", "aluRS232DeviceGender"),
        ("ALU-PORT-MIB", "aluRS232Duplex"),
        ("ALU-PORT-MIB", "aluRS232Speed"),
        ("ALU-PORT-MIB", "aluRS232ClockSource"),
        ("ALU-PORT-MIB", "aluRS232Loopback"),
        ("ALU-PORT-MIB", "aluRS232CharacterLength"),
        ("ALU-PORT-MIB", "aluRS232Parity"),
        ("ALU-PORT-MIB", "aluRS232StopBits"),
        ("ALU-PORT-MIB", "aluRS232ReportAlarm"),
        ("ALU-PORT-MIB", "aluRS232ReportAlarmStatus"),
        ("ALU-PORT-MIB", "aluRS232ControlLeadDtrDsr"),
        ("ALU-PORT-MIB", "aluRS232ControlLeadRtsDcdC"),
        ("ALU-PORT-MIB", "aluRS232ControlLeadAlbCts"),
        ("ALU-PORT-MIB", "aluRS232ControlLeadRdlRi"),
        ("ALU-PORT-MIB", "aluRS232ControlLeadDsrDtr"),
        ("ALU-PORT-MIB", "aluRS232ControlLeadDcdRtsI"),
        ("ALU-PORT-MIB", "aluRS232ControlLeadCtsAlb"),
        ("ALU-PORT-MIB", "aluRS232ControlLeadRiRdl"),
        ("ALU-PORT-MIB", "aluRS232ChanGroupRowStatus"),
        ("ALU-PORT-MIB", "aluRS232ChanGroupTimeSlots"),
        ("ALU-PORT-MIB", "aluRS232ChanGroupMTU"),
        ("ALU-PORT-MIB", "aluRS232ChanGroupOperMTU"),
        ("ALU-PORT-MIB", "aluRS232ChanGroupCRC"),
        ("ALU-PORT-MIB", "aluRS232ChanGroupIdleCycleFlags"),
        ("ALU-PORT-MIB", "aluRS232ChanGroupPayloadFillType"),
        ("ALU-PORT-MIB", "aluRS232ChanGroupPayloadPattern"),
        ("ALU-PORT-MIB", "aluRS232ControlLeadsState"))
)
if mibBuilder.loadTexts:
    aluRS232GroupV2v1.setStatus("current")

aluExtPortCemGroupV2v1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 9)
)
aluExtPortCemGroupV2v1.setObjects(
    ("ALU-PORT-MIB", "aluExtDS1SignalBitsState")
)
if mibBuilder.loadTexts:
    aluExtPortCemGroupV2v1.setStatus("current")

aluVoiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 10)
)
aluVoiceGroup.setObjects(
      *(("ALU-PORT-MIB", "aluVoicePortLastChangeTime"),
        ("ALU-PORT-MIB", "aluVoicePortType"),
        ("ALU-PORT-MIB", "aluVoicePortAudioWires"),
        ("ALU-PORT-MIB", "aluVoicePortTlpRx"),
        ("ALU-PORT-MIB", "aluVoicePortTlpTx"),
        ("ALU-PORT-MIB", "aluVoiceRowStatus"),
        ("ALU-PORT-MIB", "aluVoiceLastChangeTime"),
        ("ALU-PORT-MIB", "aluVoiceType"),
        ("ALU-PORT-MIB", "aluVoiceSignalingMode"),
        ("ALU-PORT-MIB", "aluVoiceLoopback"),
        ("ALU-PORT-MIB", "aluVoiceFaultSignaling"),
        ("ALU-PORT-MIB", "aluVoiceSignalBitsState"),
        ("ALU-PORT-MIB", "aluVoiceClockSource"),
        ("ALU-PORT-MIB", "aluVoiceChanGroupRowStatus"),
        ("ALU-PORT-MIB", "aluVoiceChanGroupMTU"),
        ("ALU-PORT-MIB", "aluVoiceChanGroupOperMTU"),
        ("ALU-PORT-MIB", "aluVoiceSignalingLeadE"),
        ("ALU-PORT-MIB", "aluVoiceSignalingLeadM"),
        ("ALU-PORT-MIB", "aluVoiceSignalingLeadsState"),
        ("ALU-PORT-MIB", "aluVoiceSignalMode"),
        ("ALU-PORT-MIB", "aluVoiceCallState"),
        ("ALU-PORT-MIB", "aluVoiceIncomingCallCount"),
        ("ALU-PORT-MIB", "aluVoiceIncomingCallCountAns"),
        ("ALU-PORT-MIB", "aluVoiceIncomingCallTime"),
        ("ALU-PORT-MIB", "aluVoiceIncomingCallTimeAns"),
        ("ALU-PORT-MIB", "aluVoiceOutgoingCallCount"),
        ("ALU-PORT-MIB", "aluVoiceOutgoingCallCountAns"),
        ("ALU-PORT-MIB", "aluVoiceOutgoingCallTime"),
        ("ALU-PORT-MIB", "aluVoiceOutgoingCallTimeAns"),
        ("ALU-PORT-MIB", "aluVoiceOutOfServiceTime"),
        ("ALU-PORT-MIB", "aluVoiceIdleTime"),
        ("ALU-PORT-MIB", "aluVoiceTotalCallCount"),
        ("ALU-PORT-MIB", "aluVoiceTotalCallTime"),
        ("ALU-PORT-MIB", "aluVoiceIdleCode"),
        ("ALU-PORT-MIB", "aluVoiceSeizedCode"))
)
if mibBuilder.loadTexts:
    aluVoiceGroup.setStatus("current")

aluPortNotifyObjsGroupV2v1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 12)
)
aluPortNotifyObjsGroupV2v1.setObjects(
    ("ALU-PORT-MIB", "aluPortNotifyRS232AlarmReason")
)
if mibBuilder.loadTexts:
    aluPortNotifyObjsGroupV2v1.setStatus("current")

aluExtPortEtherLoopbackGroupV2v1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 13)
)
aluExtPortEtherLoopbackGroupV2v1.setObjects(
      *(("ALU-PORT-MIB", "aluExtPortEtherLoopback"),
        ("ALU-PORT-MIB", "aluExtPortEtherLoopbackTimer"),
        ("ALU-PORT-MIB", "aluExtPortEtherLoopbackTimeLeft"))
)
if mibBuilder.loadTexts:
    aluExtPortEtherLoopbackGroupV2v1.setStatus("obsolete")

aluExtPortEtherNwSchedulingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 14)
)
aluExtPortEtherNwSchedulingGroup.setObjects(
    ("ALU-PORT-MIB", "aluExtPortEtherNwSchedulerMode")
)
if mibBuilder.loadTexts:
    aluExtPortEtherNwSchedulingGroup.setStatus("current")

aluRS232MultiDropGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 15)
)
aluRS232MultiDropGroup.setObjects(
    ("ALU-PORT-MIB", "aluRS232MultiDrop")
)
if mibBuilder.loadTexts:
    aluRS232MultiDropGroup.setStatus("current")

aluPortDiscardStatsGroupV3v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 16)
)
aluPortDiscardStatsGroupV3v0.setObjects(
      *(("ALU-PORT-MIB", "aluPortInL2AddrProtoDiscards"),
        ("ALU-PORT-MIB", "aluPortInMPLSLabelDiscards"),
        ("ALU-PORT-MIB", "aluPortInIPAddrProtoDiscards"),
        ("ALU-PORT-MIB", "aluPortInVlanIdDiscards"),
        ("ALU-PORT-MIB", "aluPortInHdlcCrcDiscards"),
        ("ALU-PORT-MIB", "aluPortOutPortMtuDiscards"),
        ("ALU-PORT-MIB", "aluPortInCsmQHiPriDiscards"),
        ("ALU-PORT-MIB", "aluPortInCsmQMediumPriDiscards"),
        ("ALU-PORT-MIB", "aluPortInCsmQLowPriDiscards"),
        ("ALU-PORT-MIB", "aluPortOutCsmQDiscards"),
        ("ALU-PORT-MIB", "aluPortInOtherDiscards"),
        ("ALU-PORT-MIB", "aluPortOutOtherDiscards"))
)
if mibBuilder.loadTexts:
    aluPortDiscardStatsGroupV3v0.setStatus("current")

aluPortObsoletedGroupV3v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 17)
)
aluPortObsoletedGroupV3v0.setObjects(
    ("ALU-PORT-MIB", "aluPortInCsmQFtpPriDiscards")
)
if mibBuilder.loadTexts:
    aluPortObsoletedGroupV3v0.setStatus("current")

aluPortNetControlStatsGroupV3v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 18)
)
aluPortNetControlStatsGroupV3v0.setObjects(
      *(("ALU-PORT-MIB", "aluPortNetIngressControlFwdPkts"),
        ("ALU-PORT-MIB", "aluPortNetIngressControlFwdOcts"),
        ("ALU-PORT-MIB", "aluPortNetIngressControlDroPkts"),
        ("ALU-PORT-MIB", "aluPortNetIngressControlDroOcts"),
        ("ALU-PORT-MIB", "aluPortNetEgressControlFwdPkts"),
        ("ALU-PORT-MIB", "aluPortNetEgressControlFwdOcts"),
        ("ALU-PORT-MIB", "aluPortNetEgressControlDroPkts"),
        ("ALU-PORT-MIB", "aluPortNetEgressControlDroOcts"))
)
if mibBuilder.loadTexts:
    aluPortNetControlStatsGroupV3v0.setStatus("current")

aluRS232SBitSignalingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 19)
)
aluRS232SBitSignalingGroup.setObjects(
    ("ALU-PORT-MIB", "aluRS232SBitSignaling")
)
if mibBuilder.loadTexts:
    aluRS232SBitSignalingGroup.setStatus("current")

aluRS232DataPositionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 20)
)
aluRS232DataPositionGroup.setObjects(
    ("ALU-PORT-MIB", "aluRS232DataPosition")
)
if mibBuilder.loadTexts:
    aluRS232DataPositionGroup.setStatus("current")

aluExtPortEtherLoopbackGroupV4v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 21)
)
aluExtPortEtherLoopbackGroupV4v0.setObjects(
      *(("ALU-PORT-MIB", "aluExtPortEtherLoopback"),
        ("ALU-PORT-MIB", "aluExtPortEtherLoopbackTimer"),
        ("ALU-PORT-MIB", "aluExtPortEtherLoopbackTimeLeft"),
        ("ALU-PORT-MIB", "aluExtPortEtherLoopbackCfmLbMode"),
        ("ALU-PORT-MIB", "aluExtPortEtherCfmLbmRx"),
        ("ALU-PORT-MIB", "aluExtPortEtherCfmLbmDropped"),
        ("ALU-PORT-MIB", "aluExtPortEtherCfmLbrTx"),
        ("ALU-PORT-MIB", "aluExtPortEtherLoopbackSwapMacAddr"))
)
if mibBuilder.loadTexts:
    aluExtPortEtherLoopbackGroupV4v0.setStatus("current")

aluGponGroupV5v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 22)
)
aluGponGroupV5v0.setObjects(
      *(("ALU-PORT-MIB", "aluGponPortG984SerialNumber"),
        ("ALU-PORT-MIB", "aluGponPortSubsLocId"),
        ("ALU-PORT-MIB", "aluGponPortActiveSwVersion"),
        ("ALU-PORT-MIB", "aluGponPortPonStatus"),
        ("ALU-PORT-MIB", "aluGponPortOntEnetStatus"),
        ("ALU-PORT-MIB", "aluGponPortOntEnetSpeed"))
)
if mibBuilder.loadTexts:
    aluGponGroupV5v0.setStatus("current")

aluDslGroupV5v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 23)
)
aluDslGroupV5v0.setObjects(
      *(("ALU-PORT-MIB", "aluDslPortBondingType"),
        ("ALU-PORT-MIB", "aluDslPortBondingState"),
        ("ALU-PORT-MIB", "aluDslPortBondingBitRateUS"),
        ("ALU-PORT-MIB", "aluDslPortBondingBitRateDS"),
        ("ALU-PORT-MIB", "aluDslPortAtmVpi"),
        ("ALU-PORT-MIB", "aluDslPortAtmVci"),
        ("ALU-PORT-MIB", "aluDslPortAtmF5OamLoopback"),
        ("ALU-PORT-MIB", "aluDslPortAtmF5OamLoopbackStatus"),
        ("ALU-PORT-MIB", "aluDslPortAtmF5OamLoopbackTime"),
        ("ALU-PORT-MIB", "aluDslPortNtrDslLineID"),
        ("ALU-PORT-MIB", "aluDslPortNtrLockedStatus"),
        ("ALU-PORT-MIB", "aluDslPortNtrStdDev"),
        ("ALU-PORT-MIB", "aluDslPortNtrMaxError"),
        ("ALU-PORT-MIB", "aluDslPortNtrMinError"),
        ("ALU-PORT-MIB", "aluDslPortAdsl2Plus"),
        ("ALU-PORT-MIB", "aluDslPortNtrSampleClockPeriod"),
        ("ALU-PORT-MIB", "aluDslPortNtrErrorHistory"),
        ("ALU-PORT-MIB", "aluXdslLineOperState"),
        ("ALU-PORT-MIB", "aluXdslLineState"),
        ("ALU-PORT-MIB", "aluXdslLineProtocol"),
        ("ALU-PORT-MIB", "aluXdslLineVdslProfile"),
        ("ALU-PORT-MIB", "aluXdslLineTpsTcType"),
        ("ALU-PORT-MIB", "aluXdslLineInBondingGroup"),
        ("ALU-PORT-MIB", "aluXdslLineBitRateUS"),
        ("ALU-PORT-MIB", "aluXdslLineSnrMarginUS"),
        ("ALU-PORT-MIB", "aluXdslLineOutputPowerUS"),
        ("ALU-PORT-MIB", "aluXdslLineRefPsdUS"),
        ("ALU-PORT-MIB", "aluXdslLineLoopDelayUS"),
        ("ALU-PORT-MIB", "aluXdslLineFailureUS"),
        ("ALU-PORT-MIB", "aluXdslLineB0DelayUS"),
        ("ALU-PORT-MIB", "aluXdslLineB0InpUS"),
        ("ALU-PORT-MIB", "aluXdslLineBitRateDS"),
        ("ALU-PORT-MIB", "aluXdslLineSnrMarginDS"),
        ("ALU-PORT-MIB", "aluXdslLineOutputPowerDS"),
        ("ALU-PORT-MIB", "aluXdslLineRefPsdDS"),
        ("ALU-PORT-MIB", "aluXdslLineLoopDelayDS"),
        ("ALU-PORT-MIB", "aluXdslLineFailureDS"),
        ("ALU-PORT-MIB", "aluXdslLineB0DelayDS"),
        ("ALU-PORT-MIB", "aluXdslLineB0InpDS"),
        ("ALU-PORT-MIB", "aluXdslLineAdminState"),
        ("ALU-PORT-MIB", "aluShdslLineDataRate"),
        ("ALU-PORT-MIB", "aluShdslLineState"),
        ("ALU-PORT-MIB", "aluShdslLineNegotiatedConst"),
        ("ALU-PORT-MIB", "aluShdslLineUsedCaplist"),
        ("ALU-PORT-MIB", "aluShdslLineRegion"),
        ("ALU-PORT-MIB", "aluShdslLineCaplistMode"),
        ("ALU-PORT-MIB", "aluShdslLineTpsTcType"),
        ("ALU-PORT-MIB", "aluShdslLineInBondingGroup"),
        ("ALU-PORT-MIB", "aluShdslLineAdminState"),
        ("ALU-PORT-MIB", "aluShdslLineLineAttenuation"),
        ("ALU-PORT-MIB", "aluShdslLineRxSNRMargin"),
        ("ALU-PORT-MIB", "aluShdslLinePowerBackOffValue"))
)
if mibBuilder.loadTexts:
    aluDslGroupV5v0.setStatus("current")

aluGponStatsGroupV5v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 24)
)
aluGponStatsGroupV5v0.setObjects(
      *(("ALU-PORT-MIB", "aluGponPortCurrentLastUpdTime"),
        ("ALU-PORT-MIB", "aluGponPortCurrentPMEnabled"),
        ("ALU-PORT-MIB", "aluGponPortCurrentTxFrames"),
        ("ALU-PORT-MIB", "aluGponPortCurrentRxFrames"),
        ("ALU-PORT-MIB", "aluGponPortCurrentTxBytes"),
        ("ALU-PORT-MIB", "aluGponPortCurrentRxBytes"),
        ("ALU-PORT-MIB", "aluGponPortCurrentDropFrsUp"),
        ("ALU-PORT-MIB", "aluGponPortCurrentDropFrsDn"),
        ("ALU-PORT-MIB", "aluGponPortCurrentTxFrsMcast"),
        ("ALU-PORT-MIB", "aluGponPortCurrentRxFrsMcast"),
        ("ALU-PORT-MIB", "aluGponPortCurrentFCSEs"),
        ("ALU-PORT-MIB", "aluGponPortCurrentECs"),
        ("ALU-PORT-MIB", "aluGponPortCurrentLCs"),
        ("ALU-PORT-MIB", "aluGponPortCurrentFTLs"),
        ("ALU-PORT-MIB", "aluGponPortCurrentRBOs"),
        ("ALU-PORT-MIB", "aluGponPortCurrentTBOs"),
        ("ALU-PORT-MIB", "aluGponPortCurrentSCFs"),
        ("ALU-PORT-MIB", "aluGponPortCurrentMCFs"),
        ("ALU-PORT-MIB", "aluGponPortCurrentSQEs"),
        ("ALU-PORT-MIB", "aluGponPortCurrentDTs"),
        ("ALU-PORT-MIB", "aluGponPortCurrentIMTEs"),
        ("ALU-PORT-MIB", "aluGponPortCurrentCSEs"),
        ("ALU-PORT-MIB", "aluGponPortCurrentAEs"),
        ("ALU-PORT-MIB", "aluGponPortCurrentIMREs"),
        ("ALU-PORT-MIB", "aluGponPortCurrentLostFragsDn"),
        ("ALU-PORT-MIB", "aluGponPortCurrentLostFragsUp"),
        ("ALU-PORT-MIB", "aluGponPortCurrentRxFrags"),
        ("ALU-PORT-MIB", "aluGponPortCurrentRxBlocks"),
        ("ALU-PORT-MIB", "aluGponPortCurrentTxBlocks"),
        ("ALU-PORT-MIB", "aluGponPortCurrentTxFrags"),
        ("ALU-PORT-MIB", "aluGponPortCurrentBadHeaders"),
        ("ALU-PORT-MIB", "aluGponPortPreviousLastUpdTime"),
        ("ALU-PORT-MIB", "aluGponPortPreviousPMEnabled"),
        ("ALU-PORT-MIB", "aluGponPortPreviousTxFrames"),
        ("ALU-PORT-MIB", "aluGponPortPreviousRxFrames"),
        ("ALU-PORT-MIB", "aluGponPortPreviousTxBytes"),
        ("ALU-PORT-MIB", "aluGponPortPreviousRxBytes"),
        ("ALU-PORT-MIB", "aluGponPortPreviousDropFrsUp"),
        ("ALU-PORT-MIB", "aluGponPortPreviousDropFrsDn"),
        ("ALU-PORT-MIB", "aluGponPortPreviousTxFrsMcast"),
        ("ALU-PORT-MIB", "aluGponPortPreviousRxFrsMcast"),
        ("ALU-PORT-MIB", "aluGponPortPreviousFCSEs"),
        ("ALU-PORT-MIB", "aluGponPortPreviousECs"),
        ("ALU-PORT-MIB", "aluGponPortPreviousLCs"),
        ("ALU-PORT-MIB", "aluGponPortPreviousFTLs"),
        ("ALU-PORT-MIB", "aluGponPortPreviousRBOs"),
        ("ALU-PORT-MIB", "aluGponPortPreviousTBOs"),
        ("ALU-PORT-MIB", "aluGponPortPreviousSCFs"),
        ("ALU-PORT-MIB", "aluGponPortPreviousMCFs"),
        ("ALU-PORT-MIB", "aluGponPortPreviousSQEs"),
        ("ALU-PORT-MIB", "aluGponPortPreviousDTs"),
        ("ALU-PORT-MIB", "aluGponPortPreviousIMTEs"),
        ("ALU-PORT-MIB", "aluGponPortPreviousCSEs"),
        ("ALU-PORT-MIB", "aluGponPortPreviousAEs"),
        ("ALU-PORT-MIB", "aluGponPortPreviousIMREs"),
        ("ALU-PORT-MIB", "aluGponPortPreviousLostFragsDn"),
        ("ALU-PORT-MIB", "aluGponPortPreviousLostFragsUp"),
        ("ALU-PORT-MIB", "aluGponPortPreviousRxFrags"),
        ("ALU-PORT-MIB", "aluGponPortPreviousRxBlocks"),
        ("ALU-PORT-MIB", "aluGponPortPreviousTxBlocks"),
        ("ALU-PORT-MIB", "aluGponPortPreviousTxFrags"),
        ("ALU-PORT-MIB", "aluGponPortPreviousBadHeaders"))
)
if mibBuilder.loadTexts:
    aluGponStatsGroupV5v0.setStatus("current")

aluDslStatsGroupV5v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 25)
)
aluDslStatsGroupV5v0.setObjects(
      *(("ALU-PORT-MIB", "aluXdslLineStatsNearEndFECS"),
        ("ALU-PORT-MIB", "aluXdslLineStatsNearEndLOSS"),
        ("ALU-PORT-MIB", "aluXdslLineStatsNearEndES"),
        ("ALU-PORT-MIB", "aluXdslLineStatsNearEndSES"),
        ("ALU-PORT-MIB", "aluXdslLineStatsNearEndUAS"),
        ("ALU-PORT-MIB", "aluXdslLineStatsNearEndAS"),
        ("ALU-PORT-MIB", "aluXdslLineStatsNearEndLOFS"),
        ("ALU-PORT-MIB", "aluXdslLineStatsNearEndLPRS"),
        ("ALU-PORT-MIB", "aluXdslLineStatsNearEndLEFTRS"),
        ("ALU-PORT-MIB", "aluXdslLineStatsFarEndFECS"),
        ("ALU-PORT-MIB", "aluXdslLineStatsFarEndLOSS"),
        ("ALU-PORT-MIB", "aluXdslLineStatsFarEndES"),
        ("ALU-PORT-MIB", "aluXdslLineStatsFarEndSES"),
        ("ALU-PORT-MIB", "aluXdslLineStatsFarEndUAS"),
        ("ALU-PORT-MIB", "aluXdslLineStatsFarEndAS"),
        ("ALU-PORT-MIB", "aluXdslLineStatsFarEndLOFS"),
        ("ALU-PORT-MIB", "aluXdslLineStatsFarEndLPRS"),
        ("ALU-PORT-MIB", "aluXdslLineStatsFarEndLEFTRS"),
        ("ALU-PORT-MIB", "aluXdslLineStatsFarEndLEFTRS"),
        ("ALU-PORT-MIB", "aluXdslLineStatsUpTime"),
        ("ALU-PORT-MIB", "aluShdslLineStatsLinkLoss"),
        ("ALU-PORT-MIB", "aluShdslLineStatsCVError"),
        ("ALU-PORT-MIB", "aluShdslLineStatsES"),
        ("ALU-PORT-MIB", "aluShdslLineStatsSES"),
        ("ALU-PORT-MIB", "aluShdslLineStatsLOSWS"),
        ("ALU-PORT-MIB", "aluShdslLineStatsUAS"),
        ("ALU-PORT-MIB", "aluShdslLineStatsInvalidDataFlag"))
)
if mibBuilder.loadTexts:
    aluDslStatsGroupV5v0.setStatus("current")

aluVoiceTeleprotectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 27)
)
aluVoiceTeleprotectionGroup.setObjects(
      *(("ALU-PORT-MIB", "aluVoicePortLineBalance"),
        ("ALU-PORT-MIB", "aluVoicePortRingGeneration"),
        ("ALU-PORT-MIB", "aluVoicePortSignalingType"))
)
if mibBuilder.loadTexts:
    aluVoiceTeleprotectionGroup.setStatus("current")

aluDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 28)
)
aluDataGroup.setObjects(
      *(("ALU-PORT-MIB", "aluDataPortLastChangeTime"),
        ("ALU-PORT-MIB", "aluDataPortType"),
        ("ALU-PORT-MIB", "aluDataRowStatus"),
        ("ALU-PORT-MIB", "aluDataLastChangeTime"),
        ("ALU-PORT-MIB", "aluDataType"),
        ("ALU-PORT-MIB", "aluDataClockSource"),
        ("ALU-PORT-MIB", "aluDataTiming8k"),
        ("ALU-PORT-MIB", "aluDataReportAlarm"),
        ("ALU-PORT-MIB", "aluDataReportAlarmStatus"),
        ("ALU-PORT-MIB", "aluDataLoopback"),
        ("ALU-PORT-MIB", "aluDataChanGroupRowStatus"),
        ("ALU-PORT-MIB", "aluDataChanGroupLastChangeTime"),
        ("ALU-PORT-MIB", "aluDataChanGroupMTU"),
        ("ALU-PORT-MIB", "aluDataChanGroupOperMTU"),
        ("ALU-PORT-MIB", "aluDataChanGroupPayloadFillType"),
        ("ALU-PORT-MIB", "aluDataChanGroupPayloadPattern"),
        ("ALU-PORT-MIB", "aluDataChanGroupTimeSlots"))
)
if mibBuilder.loadTexts:
    aluDataGroup.setStatus("current")

aluPortCtlStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 30)
)
aluPortCtlStatsGroup.setObjects(
      *(("ALU-PORT-MIB", "aluPortAccessCtlInFwdPkts"),
        ("ALU-PORT-MIB", "aluPortAccessCtlInFwdOcts"),
        ("ALU-PORT-MIB", "aluPortAccessCtlInDroPkts"),
        ("ALU-PORT-MIB", "aluPortAccessCtlInDroOcts"),
        ("ALU-PORT-MIB", "aluPortAccessCtlEgrFwdPkts"),
        ("ALU-PORT-MIB", "aluPortAccessCtlEgrFwdOcts"),
        ("ALU-PORT-MIB", "aluPortAccessCtlEgrDroPkts"),
        ("ALU-PORT-MIB", "aluPortAccessCtlEgrDroOcts"))
)
if mibBuilder.loadTexts:
    aluPortCtlStatsGroup.setStatus("current")

aluFrStatsGroupV5v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 31)
)
aluFrStatsGroupV5v0.setObjects(
      *(("ALU-PORT-MIB", "aluFrIfRxFrames"),
        ("ALU-PORT-MIB", "aluFrIfRxOctets"),
        ("ALU-PORT-MIB", "aluFrIfRxDEFrames"),
        ("ALU-PORT-MIB", "aluFrIfRxDEOctets"),
        ("ALU-PORT-MIB", "aluFrIfRxFECNFrames"),
        ("ALU-PORT-MIB", "aluFrIfRxBECNFrames"),
        ("ALU-PORT-MIB", "aluFrIfTxFrames"),
        ("ALU-PORT-MIB", "aluFrIfTxOctets"),
        ("ALU-PORT-MIB", "aluFrIfTxDEFrames"),
        ("ALU-PORT-MIB", "aluFrIfTxDEOctets"),
        ("ALU-PORT-MIB", "aluFrIfTxFECNFrames"),
        ("ALU-PORT-MIB", "aluFrIfTxBECNFrames"),
        ("ALU-PORT-MIB", "aluFrIfRxDiscardsInvalidDlci"),
        ("ALU-PORT-MIB", "aluFrIfRxLastInvalidDlci"),
        ("ALU-PORT-MIB", "aluFrIfRxDiscardsCrcErrors"),
        ("ALU-PORT-MIB", "aluFrIfRxDiscardsAlignmentErrors"),
        ("ALU-PORT-MIB", "aluFrIfRxDiscardsLengthViolations"),
        ("ALU-PORT-MIB", "aluFrIfRxDiscardsIllegalHeader"),
        ("ALU-PORT-MIB", "aluFrIfRxDiscardsOtherErrors"),
        ("ALU-PORT-MIB", "aluFrIfTxDiscardsUnderruns"),
        ("ALU-PORT-MIB", "aluFrIfTxDiscardsOtherErrors"),
        ("ALU-PORT-MIB", "aluExtFrCircuitReceivedCrcDiscards"),
        ("ALU-PORT-MIB", "aluExtFrCircuitReceivedAborts"),
        ("ALU-PORT-MIB", "aluExtFrCircuitReceivedOtherDiscards"),
        ("ALU-PORT-MIB", "aluExtFrCircuitSentAborts"),
        ("ALU-PORT-MIB", "aluExtFrCircuitSentFECNs"),
        ("ALU-PORT-MIB", "aluExtFrCircuitSentBECNs"),
        ("ALU-PORT-MIB", "aluExtFrCircuitReceivedDEOctets"),
        ("ALU-PORT-MIB", "aluExtFrCircuitSentDEOctets"))
)
if mibBuilder.loadTexts:
    aluFrStatsGroupV5v0.setStatus("current")

aluExtPortEtherSyncGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 32)
)
aluExtPortEtherSyncGroup.setObjects(
      *(("ALU-PORT-MIB", "aluExtPortEtherAdminPhyTxClock"),
        ("ALU-PORT-MIB", "aluExtPortEtherOperPhyTxClock"))
)
if mibBuilder.loadTexts:
    aluExtPortEtherSyncGroup.setStatus("current")

aluEthPtpTimestampStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 33)
)
aluEthPtpTimestampStatsGroup.setObjects(
      *(("ALU-PORT-MIB", "aluEthPtpInSyncPktTimestamped"),
        ("ALU-PORT-MIB", "aluEthPtpOutSyncPktTimestamped"),
        ("ALU-PORT-MIB", "aluEthPtpInDelReqPktTimestamped"),
        ("ALU-PORT-MIB", "aluEthPtpOutDelReqPktTimestamped"),
        ("ALU-PORT-MIB", "aluEthPtpInFcsErrorCount"),
        ("ALU-PORT-MIB", "aluEthPtpOutFcsErrorCount"))
)
if mibBuilder.loadTexts:
    aluEthPtpTimestampStatsGroup.setStatus("current")

aluEthPtpTimestampGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 34)
)
aluEthPtpTimestampGroup.setObjects(
      *(("ALU-PORT-MIB", "aluEthPtpTimestampCapable"),
        ("ALU-PORT-MIB", "aluEthPtpTimestampEnable"),
        ("ALU-PORT-MIB", "aluEthPtpAsymmetry"))
)
if mibBuilder.loadTexts:
    aluEthPtpTimestampGroup.setStatus("current")

aluExtDS0ChanGroupSignalModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 35)
)
aluExtDS0ChanGroupSignalModeGroup.setObjects(
    ("ALU-PORT-MIB", "aluExtDS0ChanGroupSignalMode")
)
if mibBuilder.loadTexts:
    aluExtDS0ChanGroupSignalModeGroup.setStatus("current")


# Notification objects

aluPortEtherSfpESyncCompatibility = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 7, 1)
)
aluPortEtherSfpESyncCompatibility.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALU-PORT-MIB", "aluExtPortEtherSfpSyncEStatus"))
)
if mibBuilder.loadTexts:
    aluPortEtherSfpESyncCompatibility.setStatus(
        "current"
    )

aluEqPortRS232Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 2, 0, 1)
)
aluEqPortRS232Alarm.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALU-PORT-MIB", "aluPortNotifyRS232AlarmReason"))
)
if mibBuilder.loadTexts:
    aluEqPortRS232Alarm.setStatus(
        "current"
    )

aluEqPortRS232AlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 2, 0, 2)
)
aluEqPortRS232AlarmClear.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALU-PORT-MIB", "aluPortNotifyRS232AlarmReason"))
)
if mibBuilder.loadTexts:
    aluEqPortRS232AlarmClear.setStatus(
        "current"
    )

aluRS232LoopbackStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 2, 0, 3)
)
aluRS232LoopbackStarted.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALU-PORT-MIB", "aluRS232Loopback"))
)
if mibBuilder.loadTexts:
    aluRS232LoopbackStarted.setStatus(
        "current"
    )

aluRS232LoopbackStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 2, 0, 4)
)
aluRS232LoopbackStopped.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALU-PORT-MIB", "aluRS232Loopback"))
)
if mibBuilder.loadTexts:
    aluRS232LoopbackStopped.setStatus(
        "current"
    )

aluVoiceLoopbackStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 2, 0, 5)
)
aluVoiceLoopbackStarted.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALU-PORT-MIB", "aluVoiceLoopback"))
)
if mibBuilder.loadTexts:
    aluVoiceLoopbackStarted.setStatus(
        "current"
    )

aluVoiceLoopbackStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 2, 0, 6)
)
aluVoiceLoopbackStopped.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALU-PORT-MIB", "aluVoiceLoopback"))
)
if mibBuilder.loadTexts:
    aluVoiceLoopbackStopped.setStatus(
        "current"
    )

aluGponPortInbandAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 2, 0, 7)
)
aluGponPortInbandAlarm.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALU-PORT-MIB", "aluGponPortG984SerialNumber"))
)
if mibBuilder.loadTexts:
    aluGponPortInbandAlarm.setStatus(
        "current"
    )

aluGponPortInbandAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 2, 0, 8)
)
aluGponPortInbandAlarmClear.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALU-PORT-MIB", "aluGponPortG984SerialNumber"))
)
if mibBuilder.loadTexts:
    aluGponPortInbandAlarmClear.setStatus(
        "current"
    )

aluEqPortDataAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 2, 0, 9)
)
aluEqPortDataAlarm.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALU-PORT-MIB", "aluPortNotifyDataAlarmReason"))
)
if mibBuilder.loadTexts:
    aluEqPortDataAlarm.setStatus(
        "current"
    )

aluEqPortDataAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 2, 0, 10)
)
aluEqPortDataAlarmClear.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALU-PORT-MIB", "aluPortNotifyDataAlarmReason"))
)
if mibBuilder.loadTexts:
    aluEqPortDataAlarmClear.setStatus(
        "current"
    )

aluDataLoopbackStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 2, 0, 11)
)
aluDataLoopbackStarted.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALU-PORT-MIB", "aluDataLoopback"))
)
if mibBuilder.loadTexts:
    aluDataLoopbackStarted.setStatus(
        "current"
    )

aluDataLoopbackStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 2, 0, 12)
)
aluDataLoopbackStopped.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALU-PORT-MIB", "aluDataLoopback"))
)
if mibBuilder.loadTexts:
    aluDataLoopbackStopped.setStatus(
        "current"
    )


# Notifications groups

aluPortEtherSfpSyncECompatibilityGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 4)
)
aluPortEtherSfpSyncECompatibilityGroup.setObjects(
    ("ALU-PORT-MIB", "aluPortEtherSfpESyncCompatibility")
)
if mibBuilder.loadTexts:
    aluPortEtherSfpSyncECompatibilityGroup.setStatus(
        "current"
    )

aluPortNotificationGroupV2v1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 8)
)
aluPortNotificationGroupV2v1.setObjects(
      *(("ALU-PORT-MIB", "aluEqPortRS232Alarm"),
        ("ALU-PORT-MIB", "aluEqPortRS232AlarmClear"),
        ("ALU-PORT-MIB", "aluRS232LoopbackStarted"),
        ("ALU-PORT-MIB", "aluRS232LoopbackStopped"))
)
if mibBuilder.loadTexts:
    aluPortNotificationGroupV2v1.setStatus(
        "current"
    )

aluVoiceNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 11)
)
aluVoiceNotifGroup.setObjects(
      *(("ALU-PORT-MIB", "aluVoiceLoopbackStarted"),
        ("ALU-PORT-MIB", "aluVoiceLoopbackStopped"))
)
if mibBuilder.loadTexts:
    aluVoiceNotifGroup.setStatus(
        "current"
    )

aluDslGponNotificationGroupV5v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 26)
)
aluDslGponNotificationGroupV5v0.setObjects(
      *(("ALU-PORT-MIB", "aluGponPortInbandAlarm"),
        ("ALU-PORT-MIB", "aluGponPortInbandAlarmClear"))
)
if mibBuilder.loadTexts:
    aluDslGponNotificationGroupV5v0.setStatus(
        "current"
    )

aluDataNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 2, 29)
)
aluDataNotifGroup.setObjects(
      *(("ALU-PORT-MIB", "aluEqPortDataAlarm"),
        ("ALU-PORT-MIB", "aluEqPortDataAlarmClear"),
        ("ALU-PORT-MIB", "aluDataLoopbackStarted"),
        ("ALU-PORT-MIB", "aluDataLoopbackStopped"))
)
if mibBuilder.loadTexts:
    aluDataNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aluPortComp7705V1v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 1, 1, 1)
)
aluPortComp7705V1v0.setObjects(
      *(("ALU-PORT-MIB", "aluExtDS1PortLineImpedanceGroup"),
        ("ALU-PORT-MIB", "aluPortDiscardStatsGroup"))
)
if mibBuilder.loadTexts:
    aluPortComp7705V1v0.setStatus(
        "current"
    )

aluPortComp7705V1v1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 1, 1, 2)
)
aluPortComp7705V1v1.setObjects(
      *(("ALU-PORT-MIB", "aluExtPortEtherSfpSyncEGroup"),
        ("ALU-PORT-MIB", "aluPortAcrClkStatsGroup"))
)
if mibBuilder.loadTexts:
    aluPortComp7705V1v1.setStatus(
        "current"
    )

aluPortComp7705V2v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 1, 1, 3)
)
aluPortComp7705V2v0.setObjects(
    ("ALU-PORT-MIB", "aluExtDS1HoldTimeGroup")
)
if mibBuilder.loadTexts:
    aluPortComp7705V2v0.setStatus(
        "current"
    )

aluPortComp7705V2v1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 1, 1, 4)
)
aluPortComp7705V2v1.setObjects(
      *(("ALU-PORT-MIB", "aluRS232GroupV2v1"),
        ("ALU-PORT-MIB", "aluPortNotificationGroupV2v1"),
        ("ALU-PORT-MIB", "aluExtPortCemGroupV2v1"),
        ("ALU-PORT-MIB", "aluPortNotifyObjsGroupV2v1"),
        ("ALU-PORT-MIB", "aluExtPortEtherLoopbackGroupV2v1"))
)
if mibBuilder.loadTexts:
    aluPortComp7705V2v1.setStatus(
        "current"
    )

aluPortComp7705V3v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 1, 1, 5)
)
aluPortComp7705V3v0.setObjects(
      *(("ALU-PORT-MIB", "aluVoiceGroup"),
        ("ALU-PORT-MIB", "aluVoiceNotifGroup"),
        ("ALU-PORT-MIB", "aluRS232MultiDropGroup"),
        ("ALU-PORT-MIB", "aluPortDiscardStatsGroupV3v0"),
        ("ALU-PORT-MIB", "aluPortNetControlStatsGroupV3v0"),
        ("ALU-PORT-MIB", "aluRS232SBitSignalingGroup"),
        ("ALU-PORT-MIB", "aluRS232DataPositionGroup"))
)
if mibBuilder.loadTexts:
    aluPortComp7705V3v0.setStatus(
        "current"
    )

aluPortComp7705V4v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 1, 1, 6)
)
aluPortComp7705V4v0.setObjects(
      *(("ALU-PORT-MIB", "aluExtPortEtherLoopbackGroupV4v0"),
        ("ALU-PORT-MIB", "aluPortEtherSfpSyncECompatibilityGroup"))
)
if mibBuilder.loadTexts:
    aluPortComp7705V4v0.setStatus(
        "current"
    )

aluPortComp7705V5v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 4, 1, 1, 7)
)
aluPortComp7705V5v0.setObjects(
      *(("ALU-PORT-MIB", "aluGponGroupV5v0"),
        ("ALU-PORT-MIB", "aluDslGroupV5v0"),
        ("ALU-PORT-MIB", "aluGponStatsGroupV5v0"),
        ("ALU-PORT-MIB", "aluDslStatsGroupV5v0"),
        ("ALU-PORT-MIB", "aluDslGponNotificationGroupV5v0"),
        ("ALU-PORT-MIB", "aluVoiceTeleprotectionGroup"),
        ("ALU-PORT-MIB", "aluDataGroup"),
        ("ALU-PORT-MIB", "aluDataNotifGroup"),
        ("ALU-PORT-MIB", "aluExtDS0ChanGroupSignalModeGroup"),
        ("ALU-PORT-MIB", "aluPortCtlStatsGroup"))
)
if mibBuilder.loadTexts:
    aluPortComp7705V5v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-PORT-MIB",
    **{"AluRS232ReportStatus": AluRS232ReportStatus,
       "AluRS232ControlLead": AluRS232ControlLead,
       "AluVoicePortTlp": AluVoicePortTlp,
       "AluVoiceSignalingLead": AluVoiceSignalingLead,
       "AluDslTpsTcType": AluDslTpsTcType,
       "AluDslAdminState": AluDslAdminState,
       "AluDataReportStatus": AluDataReportStatus,
       "aluPortMIBModule": aluPortMIBModule,
       "aluPortConformance": aluPortConformance,
       "aluPortCompliances": aluPortCompliances,
       "aluPortComp7705": aluPortComp7705,
       "aluPortComp7705V1v0": aluPortComp7705V1v0,
       "aluPortComp7705V1v1": aluPortComp7705V1v1,
       "aluPortComp7705V2v0": aluPortComp7705V2v0,
       "aluPortComp7705V2v1": aluPortComp7705V2v1,
       "aluPortComp7705V3v0": aluPortComp7705V3v0,
       "aluPortComp7705V4v0": aluPortComp7705V4v0,
       "aluPortComp7705V5v0": aluPortComp7705V5v0,
       "aluPortGroups": aluPortGroups,
       "aluExtDS1PortLineImpedanceGroup": aluExtDS1PortLineImpedanceGroup,
       "aluPortDiscardStatsGroup": aluPortDiscardStatsGroup,
       "aluExtPortEtherSfpSyncEGroup": aluExtPortEtherSfpSyncEGroup,
       "aluPortEtherSfpSyncECompatibilityGroup": aluPortEtherSfpSyncECompatibilityGroup,
       "aluPortAcrClkStatsGroup": aluPortAcrClkStatsGroup,
       "aluExtDS1HoldTimeGroup": aluExtDS1HoldTimeGroup,
       "aluRS232GroupV2v1": aluRS232GroupV2v1,
       "aluPortNotificationGroupV2v1": aluPortNotificationGroupV2v1,
       "aluExtPortCemGroupV2v1": aluExtPortCemGroupV2v1,
       "aluVoiceGroup": aluVoiceGroup,
       "aluVoiceNotifGroup": aluVoiceNotifGroup,
       "aluPortNotifyObjsGroupV2v1": aluPortNotifyObjsGroupV2v1,
       "aluExtPortEtherLoopbackGroupV2v1": aluExtPortEtherLoopbackGroupV2v1,
       "aluExtPortEtherNwSchedulingGroup": aluExtPortEtherNwSchedulingGroup,
       "aluRS232MultiDropGroup": aluRS232MultiDropGroup,
       "aluPortDiscardStatsGroupV3v0": aluPortDiscardStatsGroupV3v0,
       "aluPortObsoletedGroupV3v0": aluPortObsoletedGroupV3v0,
       "aluPortNetControlStatsGroupV3v0": aluPortNetControlStatsGroupV3v0,
       "aluRS232SBitSignalingGroup": aluRS232SBitSignalingGroup,
       "aluRS232DataPositionGroup": aluRS232DataPositionGroup,
       "aluExtPortEtherLoopbackGroupV4v0": aluExtPortEtherLoopbackGroupV4v0,
       "aluGponGroupV5v0": aluGponGroupV5v0,
       "aluDslGroupV5v0": aluDslGroupV5v0,
       "aluGponStatsGroupV5v0": aluGponStatsGroupV5v0,
       "aluDslStatsGroupV5v0": aluDslStatsGroupV5v0,
       "aluDslGponNotificationGroupV5v0": aluDslGponNotificationGroupV5v0,
       "aluVoiceTeleprotectionGroup": aluVoiceTeleprotectionGroup,
       "aluDataGroup": aluDataGroup,
       "aluDataNotifGroup": aluDataNotifGroup,
       "aluPortCtlStatsGroup": aluPortCtlStatsGroup,
       "aluFrStatsGroupV5v0": aluFrStatsGroupV5v0,
       "aluExtPortEtherSyncGroup": aluExtPortEtherSyncGroup,
       "aluEthPtpTimestampStatsGroup": aluEthPtpTimestampStatsGroup,
       "aluEthPtpTimestampGroup": aluEthPtpTimestampGroup,
       "aluExtDS0ChanGroupSignalModeGroup": aluExtDS0ChanGroupSignalModeGroup,
       "aluPortObjs": aluPortObjs,
       "aluExtTmnxDS1PortTable": aluExtTmnxDS1PortTable,
       "aluExtTmnxDS1PortEntry": aluExtTmnxDS1PortEntry,
       "aluExtDS1PortLineImpedance": aluExtDS1PortLineImpedance,
       "aluExtTmnxPortEtherTable": aluExtTmnxPortEtherTable,
       "aluExtTmnxPortEtherEntry": aluExtTmnxPortEtherEntry,
       "aluExtPortEtherSfpSyncEStatus": aluExtPortEtherSfpSyncEStatus,
       "aluExtPortEtherLoopback": aluExtPortEtherLoopback,
       "aluExtPortEtherLoopbackTimer": aluExtPortEtherLoopbackTimer,
       "aluExtPortEtherLoopbackTimeLeft": aluExtPortEtherLoopbackTimeLeft,
       "aluExtPortEtherNwSchedulerMode": aluExtPortEtherNwSchedulerMode,
       "aluExtPortEtherLoopbackCfmLbMode": aluExtPortEtherLoopbackCfmLbMode,
       "aluExtPortEtherCfmLbmRx": aluExtPortEtherCfmLbmRx,
       "aluExtPortEtherCfmLbmDropped": aluExtPortEtherCfmLbmDropped,
       "aluExtPortEtherCfmLbrTx": aluExtPortEtherCfmLbrTx,
       "aluExtPortEtherLoopbackSwapMacAddr": aluExtPortEtherLoopbackSwapMacAddr,
       "aluExtPortEtherAdminPhyTxClock": aluExtPortEtherAdminPhyTxClock,
       "aluExtPortEtherOperPhyTxClock": aluExtPortEtherOperPhyTxClock,
       "aluEthPtpTimestampCapable": aluEthPtpTimestampCapable,
       "aluEthPtpTimestampEnable": aluEthPtpTimestampEnable,
       "aluEthPtpAsymmetry": aluEthPtpAsymmetry,
       "aluExtTmnxDS1Table": aluExtTmnxDS1Table,
       "aluExtTmnxDS1Entry": aluExtTmnxDS1Entry,
       "aluExtDS1HoldTimeUp": aluExtDS1HoldTimeUp,
       "aluExtDS1HoldTimeDown": aluExtDS1HoldTimeDown,
       "aluExtDS1SignalBitsState": aluExtDS1SignalBitsState,
       "aluRS232PortTable": aluRS232PortTable,
       "aluRS232PortEntry": aluRS232PortEntry,
       "aluRS232PortLastChangeTime": aluRS232PortLastChangeTime,
       "aluRS232PortType": aluRS232PortType,
       "aluRS232Table": aluRS232Table,
       "aluRS232Entry": aluRS232Entry,
       "aluRS232RowStatus": aluRS232RowStatus,
       "aluRS232LastChangeTime": aluRS232LastChangeTime,
       "aluRS232Type": aluRS232Type,
       "aluRS232DeviceMode": aluRS232DeviceMode,
       "aluRS232DeviceGender": aluRS232DeviceGender,
       "aluRS232Duplex": aluRS232Duplex,
       "aluRS232Speed": aluRS232Speed,
       "aluRS232ClockSource": aluRS232ClockSource,
       "aluRS232Loopback": aluRS232Loopback,
       "aluRS232CharacterLength": aluRS232CharacterLength,
       "aluRS232Parity": aluRS232Parity,
       "aluRS232StopBits": aluRS232StopBits,
       "aluRS232ReportAlarm": aluRS232ReportAlarm,
       "aluRS232ReportAlarmStatus": aluRS232ReportAlarmStatus,
       "aluRS232ControlLeadDtrDsr": aluRS232ControlLeadDtrDsr,
       "aluRS232ControlLeadRtsDcdC": aluRS232ControlLeadRtsDcdC,
       "aluRS232ControlLeadAlbCts": aluRS232ControlLeadAlbCts,
       "aluRS232ControlLeadRdlRi": aluRS232ControlLeadRdlRi,
       "aluRS232ControlLeadDsrDtr": aluRS232ControlLeadDsrDtr,
       "aluRS232ControlLeadDcdRtsI": aluRS232ControlLeadDcdRtsI,
       "aluRS232ControlLeadCtsAlb": aluRS232ControlLeadCtsAlb,
       "aluRS232ControlLeadRiRdl": aluRS232ControlLeadRiRdl,
       "aluRS232ControlLeadsState": aluRS232ControlLeadsState,
       "aluRS232MultiDrop": aluRS232MultiDrop,
       "aluRS232SBitSignaling": aluRS232SBitSignaling,
       "aluRS232DataPosition": aluRS232DataPosition,
       "aluRS232ChanGroupTable": aluRS232ChanGroupTable,
       "aluRS232ChanGroupEntry": aluRS232ChanGroupEntry,
       "aluRS232ChanGroupRowStatus": aluRS232ChanGroupRowStatus,
       "aluRS232ChanGroupTimeSlots": aluRS232ChanGroupTimeSlots,
       "aluRS232ChanGroupMTU": aluRS232ChanGroupMTU,
       "aluRS232ChanGroupOperMTU": aluRS232ChanGroupOperMTU,
       "aluRS232ChanGroupCRC": aluRS232ChanGroupCRC,
       "aluRS232ChanGroupIdleCycleFlags": aluRS232ChanGroupIdleCycleFlags,
       "aluRS232ChanGroupPayloadFillType": aluRS232ChanGroupPayloadFillType,
       "aluRS232ChanGroupPayloadPattern": aluRS232ChanGroupPayloadPattern,
       "aluVoicePortTable": aluVoicePortTable,
       "aluVoicePortEntry": aluVoicePortEntry,
       "aluVoicePortLastChangeTime": aluVoicePortLastChangeTime,
       "aluVoicePortType": aluVoicePortType,
       "aluVoicePortAudioWires": aluVoicePortAudioWires,
       "aluVoicePortTlpRx": aluVoicePortTlpRx,
       "aluVoicePortTlpTx": aluVoicePortTlpTx,
       "aluVoicePortLineBalance": aluVoicePortLineBalance,
       "aluVoicePortRingGeneration": aluVoicePortRingGeneration,
       "aluVoicePortSignalingType": aluVoicePortSignalingType,
       "aluVoiceTable": aluVoiceTable,
       "aluVoiceEntry": aluVoiceEntry,
       "aluVoiceRowStatus": aluVoiceRowStatus,
       "aluVoiceLastChangeTime": aluVoiceLastChangeTime,
       "aluVoiceType": aluVoiceType,
       "aluVoiceSignalingMode": aluVoiceSignalingMode,
       "aluVoiceLoopback": aluVoiceLoopback,
       "aluVoiceFaultSignaling": aluVoiceFaultSignaling,
       "aluVoiceSignalBitsState": aluVoiceSignalBitsState,
       "aluVoiceClockSource": aluVoiceClockSource,
       "aluVoiceSignalingLeadE": aluVoiceSignalingLeadE,
       "aluVoiceSignalingLeadM": aluVoiceSignalingLeadM,
       "aluVoiceSignalingLeadsState": aluVoiceSignalingLeadsState,
       "aluVoiceSignalMode": aluVoiceSignalMode,
       "aluVoiceCallState": aluVoiceCallState,
       "aluVoiceIncomingCallCount": aluVoiceIncomingCallCount,
       "aluVoiceIncomingCallCountAns": aluVoiceIncomingCallCountAns,
       "aluVoiceIncomingCallTime": aluVoiceIncomingCallTime,
       "aluVoiceIncomingCallTimeAns": aluVoiceIncomingCallTimeAns,
       "aluVoiceOutgoingCallCount": aluVoiceOutgoingCallCount,
       "aluVoiceOutgoingCallCountAns": aluVoiceOutgoingCallCountAns,
       "aluVoiceOutgoingCallTime": aluVoiceOutgoingCallTime,
       "aluVoiceOutgoingCallTimeAns": aluVoiceOutgoingCallTimeAns,
       "aluVoiceOutOfServiceTime": aluVoiceOutOfServiceTime,
       "aluVoiceIdleTime": aluVoiceIdleTime,
       "aluVoiceTotalCallCount": aluVoiceTotalCallCount,
       "aluVoiceTotalCallTime": aluVoiceTotalCallTime,
       "aluVoiceIdleCode": aluVoiceIdleCode,
       "aluVoiceSeizedCode": aluVoiceSeizedCode,
       "aluVoiceChanGroupTable": aluVoiceChanGroupTable,
       "aluVoiceChanGroupEntry": aluVoiceChanGroupEntry,
       "aluVoiceChanGroupRowStatus": aluVoiceChanGroupRowStatus,
       "aluVoiceChanGroupMTU": aluVoiceChanGroupMTU,
       "aluVoiceChanGroupOperMTU": aluVoiceChanGroupOperMTU,
       "aluGponPortTable": aluGponPortTable,
       "aluGponPortEntry": aluGponPortEntry,
       "aluGponPortG984SerialNumber": aluGponPortG984SerialNumber,
       "aluGponPortSubsLocId": aluGponPortSubsLocId,
       "aluGponPortActiveSwVersion": aluGponPortActiveSwVersion,
       "aluGponPortPonStatus": aluGponPortPonStatus,
       "aluGponPortOntEnetStatus": aluGponPortOntEnetStatus,
       "aluGponPortOntEnetSpeed": aluGponPortOntEnetSpeed,
       "aluDslPortTable": aluDslPortTable,
       "aluDslPortEntry": aluDslPortEntry,
       "aluDslPortBondingType": aluDslPortBondingType,
       "aluDslPortBondingState": aluDslPortBondingState,
       "aluDslPortBondingBitRateUS": aluDslPortBondingBitRateUS,
       "aluDslPortBondingBitRateDS": aluDslPortBondingBitRateDS,
       "aluDslPortAtmVpi": aluDslPortAtmVpi,
       "aluDslPortAtmVci": aluDslPortAtmVci,
       "aluDslPortAtmF5OamLoopback": aluDslPortAtmF5OamLoopback,
       "aluDslPortAtmF5OamLoopbackStatus": aluDslPortAtmF5OamLoopbackStatus,
       "aluDslPortAtmF5OamLoopbackTime": aluDslPortAtmF5OamLoopbackTime,
       "aluDslPortNtrDslLineID": aluDslPortNtrDslLineID,
       "aluDslPortNtrLockedStatus": aluDslPortNtrLockedStatus,
       "aluDslPortNtrStdDev": aluDslPortNtrStdDev,
       "aluDslPortNtrMaxError": aluDslPortNtrMaxError,
       "aluDslPortNtrMinError": aluDslPortNtrMinError,
       "aluDslPortAdsl2Plus": aluDslPortAdsl2Plus,
       "aluDslPortNtrSampleClockPeriod": aluDslPortNtrSampleClockPeriod,
       "aluDslPortNtrErrorHistory": aluDslPortNtrErrorHistory,
       "aluXdslLineTable": aluXdslLineTable,
       "aluXdslLineEntry": aluXdslLineEntry,
       "aluXdslLineID": aluXdslLineID,
       "aluXdslLineOperState": aluXdslLineOperState,
       "aluXdslLineState": aluXdslLineState,
       "aluXdslLineProtocol": aluXdslLineProtocol,
       "aluXdslLineVdslProfile": aluXdslLineVdslProfile,
       "aluXdslLineTpsTcType": aluXdslLineTpsTcType,
       "aluXdslLineInBondingGroup": aluXdslLineInBondingGroup,
       "aluXdslLineBitRateUS": aluXdslLineBitRateUS,
       "aluXdslLineSnrMarginUS": aluXdslLineSnrMarginUS,
       "aluXdslLineOutputPowerUS": aluXdslLineOutputPowerUS,
       "aluXdslLineRefPsdUS": aluXdslLineRefPsdUS,
       "aluXdslLineLoopDelayUS": aluXdslLineLoopDelayUS,
       "aluXdslLineFailureUS": aluXdslLineFailureUS,
       "aluXdslLineB0DelayUS": aluXdslLineB0DelayUS,
       "aluXdslLineB0InpUS": aluXdslLineB0InpUS,
       "aluXdslLineBitRateDS": aluXdslLineBitRateDS,
       "aluXdslLineSnrMarginDS": aluXdslLineSnrMarginDS,
       "aluXdslLineOutputPowerDS": aluXdslLineOutputPowerDS,
       "aluXdslLineRefPsdDS": aluXdslLineRefPsdDS,
       "aluXdslLineLoopDelayDS": aluXdslLineLoopDelayDS,
       "aluXdslLineFailureDS": aluXdslLineFailureDS,
       "aluXdslLineB0DelayDS": aluXdslLineB0DelayDS,
       "aluXdslLineB0InpDS": aluXdslLineB0InpDS,
       "aluXdslLineAdminState": aluXdslLineAdminState,
       "aluShdslLineTable": aluShdslLineTable,
       "aluShdslLineEntry": aluShdslLineEntry,
       "aluShdslLineID": aluShdslLineID,
       "aluShdslLineDataRate": aluShdslLineDataRate,
       "aluShdslLineState": aluShdslLineState,
       "aluShdslLineNegotiatedConst": aluShdslLineNegotiatedConst,
       "aluShdslLineUsedCaplist": aluShdslLineUsedCaplist,
       "aluShdslLineRegion": aluShdslLineRegion,
       "aluShdslLineCaplistMode": aluShdslLineCaplistMode,
       "aluShdslLineTpsTcType": aluShdslLineTpsTcType,
       "aluShdslLineInBondingGroup": aluShdslLineInBondingGroup,
       "aluShdslLineAdminState": aluShdslLineAdminState,
       "aluShdslLineLineAttenuation": aluShdslLineLineAttenuation,
       "aluShdslLineRxSNRMargin": aluShdslLineRxSNRMargin,
       "aluShdslLinePowerBackOffValue": aluShdslLinePowerBackOffValue,
       "aluDataPortTable": aluDataPortTable,
       "aluDataPortEntry": aluDataPortEntry,
       "aluDataPortLastChangeTime": aluDataPortLastChangeTime,
       "aluDataPortType": aluDataPortType,
       "aluDataTable": aluDataTable,
       "aluDataEntry": aluDataEntry,
       "aluDataRowStatus": aluDataRowStatus,
       "aluDataLastChangeTime": aluDataLastChangeTime,
       "aluDataType": aluDataType,
       "aluDataClockSource": aluDataClockSource,
       "aluDataTiming8k": aluDataTiming8k,
       "aluDataReportAlarm": aluDataReportAlarm,
       "aluDataReportAlarmStatus": aluDataReportAlarmStatus,
       "aluDataLoopback": aluDataLoopback,
       "aluDataChanGroupTable": aluDataChanGroupTable,
       "aluDataChanGroupEntry": aluDataChanGroupEntry,
       "aluDataChanGroupRowStatus": aluDataChanGroupRowStatus,
       "aluDataChanGroupLastChangeTime": aluDataChanGroupLastChangeTime,
       "aluDataChanGroupMTU": aluDataChanGroupMTU,
       "aluDataChanGroupOperMTU": aluDataChanGroupOperMTU,
       "aluDataChanGroupPayloadFillType": aluDataChanGroupPayloadFillType,
       "aluDataChanGroupPayloadPattern": aluDataChanGroupPayloadPattern,
       "aluDataChanGroupTimeSlots": aluDataChanGroupTimeSlots,
       "aluExtTmnxDS0ChanGroupTable": aluExtTmnxDS0ChanGroupTable,
       "aluExtTmnxDS0ChanGroupEntry": aluExtTmnxDS0ChanGroupEntry,
       "aluExtDS0ChanGroupSignalMode": aluExtDS0ChanGroupSignalMode,
       "aluPortNotificationObjects": aluPortNotificationObjects,
       "aluPortEtherSfpESyncCompatibility": aluPortEtherSfpESyncCompatibility,
       "aluPortNotifyRS232AlarmReason": aluPortNotifyRS232AlarmReason,
       "aluPortNotifyDataAlarmReason": aluPortNotifyDataAlarmReason,
       "aluPortStatsObjs": aluPortStatsObjs,
       "aluPortDiscardStatsTable": aluPortDiscardStatsTable,
       "aluPortDiscardsStatsEntry": aluPortDiscardsStatsEntry,
       "aluPortInL2AddrProtoDiscards": aluPortInL2AddrProtoDiscards,
       "aluPortInMPLSLabelDiscards": aluPortInMPLSLabelDiscards,
       "aluPortInIPAddrProtoDiscards": aluPortInIPAddrProtoDiscards,
       "aluPortInVlanIdDiscards": aluPortInVlanIdDiscards,
       "aluPortInHdlcCrcDiscards": aluPortInHdlcCrcDiscards,
       "aluPortOutPortMtuDiscards": aluPortOutPortMtuDiscards,
       "aluPortInCsmQHiPriDiscards": aluPortInCsmQHiPriDiscards,
       "aluPortInCsmQLowPriDiscards": aluPortInCsmQLowPriDiscards,
       "aluPortInCsmQFtpPriDiscards": aluPortInCsmQFtpPriDiscards,
       "aluPortOutCsmQDiscards": aluPortOutCsmQDiscards,
       "aluPortInOtherDiscards": aluPortInOtherDiscards,
       "aluPortOutOtherDiscards": aluPortOutOtherDiscards,
       "aluPortInCsmQMediumPriDiscards": aluPortInCsmQMediumPriDiscards,
       "aluPortAcrClkStatsTable": aluPortAcrClkStatsTable,
       "aluPortAcrClkStatsEntry": aluPortAcrClkStatsEntry,
       "aluLastUpdateTime": aluLastUpdateTime,
       "aluTotalMinutesIn24Hour": aluTotalMinutesIn24Hour,
       "aluCurrent24HourFreqOffsetMeanPpb": aluCurrent24HourFreqOffsetMeanPpb,
       "aluCurrent24HourFreqOffsetStdDevPpb": aluCurrent24HourFreqOffsetStdDevPpb,
       "aluMaxShortIntervalMinutes": aluMaxShortIntervalMinutes,
       "aluTotalShortIntervalMinutes": aluTotalShortIntervalMinutes,
       "aluCurrent1MinValidData": aluCurrent1MinValidData,
       "aluCurrent1MinPhaseErrorMeanPpb": aluCurrent1MinPhaseErrorMeanPpb,
       "aluCurrent1MinPhaseErrorStdDevNs": aluCurrent1MinPhaseErrorStdDevNs,
       "aluCurrent1MinPhaseErrorMeanNs": aluCurrent1MinPhaseErrorMeanNs,
       "aluCurrent1MinFreqOffsetMeanPpb": aluCurrent1MinFreqOffsetMeanPpb,
       "aluCurrent1MinFreqOffsetStdDevPpb": aluCurrent1MinFreqOffsetStdDevPpb,
       "aluPortAcrClkStatsShortIntervalTable": aluPortAcrClkStatsShortIntervalTable,
       "aluPortAcrClkStatsShortIntervalEntry": aluPortAcrClkStatsShortIntervalEntry,
       "aluIntervalNumber": aluIntervalNumber,
       "aluIntervalValidData": aluIntervalValidData,
       "aluIntervalUpdateTime": aluIntervalUpdateTime,
       "aluIntervalPhaseErrorMeanPpb": aluIntervalPhaseErrorMeanPpb,
       "aluIntervalPhaseErrorStdDevNs": aluIntervalPhaseErrorStdDevNs,
       "aluIntervalPhaseErrorMeanNs": aluIntervalPhaseErrorMeanNs,
       "aluIntervalFreqOffsetMeanPpb": aluIntervalFreqOffsetMeanPpb,
       "aluIntervalFreqOffsetStdDevPpb": aluIntervalFreqOffsetStdDevPpb,
       "aluPortNetIngressControlStatsTable": aluPortNetIngressControlStatsTable,
       "aluPortNetIngressControlStatsEntry": aluPortNetIngressControlStatsEntry,
       "aluPortNetIngressControlFwdPkts": aluPortNetIngressControlFwdPkts,
       "aluPortNetIngressControlFwdOcts": aluPortNetIngressControlFwdOcts,
       "aluPortNetIngressControlDroPkts": aluPortNetIngressControlDroPkts,
       "aluPortNetIngressControlDroOcts": aluPortNetIngressControlDroOcts,
       "aluPortNetEgressControlStatsTable": aluPortNetEgressControlStatsTable,
       "aluPortNetEgressControlStatsEntry": aluPortNetEgressControlStatsEntry,
       "aluPortNetEgressControlFwdPkts": aluPortNetEgressControlFwdPkts,
       "aluPortNetEgressControlFwdOcts": aluPortNetEgressControlFwdOcts,
       "aluPortNetEgressControlDroPkts": aluPortNetEgressControlDroPkts,
       "aluPortNetEgressControlDroOcts": aluPortNetEgressControlDroOcts,
       "aluGponPortCurrentTable": aluGponPortCurrentTable,
       "aluGponPortCurrentEntry": aluGponPortCurrentEntry,
       "aluGponPortCurrentLastUpdTime": aluGponPortCurrentLastUpdTime,
       "aluGponPortCurrentPMEnabled": aluGponPortCurrentPMEnabled,
       "aluGponPortCurrentTxFrames": aluGponPortCurrentTxFrames,
       "aluGponPortCurrentRxFrames": aluGponPortCurrentRxFrames,
       "aluGponPortCurrentTxBytes": aluGponPortCurrentTxBytes,
       "aluGponPortCurrentRxBytes": aluGponPortCurrentRxBytes,
       "aluGponPortCurrentDropFrsUp": aluGponPortCurrentDropFrsUp,
       "aluGponPortCurrentDropFrsDn": aluGponPortCurrentDropFrsDn,
       "aluGponPortCurrentTxFrsMcast": aluGponPortCurrentTxFrsMcast,
       "aluGponPortCurrentRxFrsMcast": aluGponPortCurrentRxFrsMcast,
       "aluGponPortCurrentFCSEs": aluGponPortCurrentFCSEs,
       "aluGponPortCurrentECs": aluGponPortCurrentECs,
       "aluGponPortCurrentLCs": aluGponPortCurrentLCs,
       "aluGponPortCurrentFTLs": aluGponPortCurrentFTLs,
       "aluGponPortCurrentRBOs": aluGponPortCurrentRBOs,
       "aluGponPortCurrentTBOs": aluGponPortCurrentTBOs,
       "aluGponPortCurrentSCFs": aluGponPortCurrentSCFs,
       "aluGponPortCurrentMCFs": aluGponPortCurrentMCFs,
       "aluGponPortCurrentSQEs": aluGponPortCurrentSQEs,
       "aluGponPortCurrentDTs": aluGponPortCurrentDTs,
       "aluGponPortCurrentIMTEs": aluGponPortCurrentIMTEs,
       "aluGponPortCurrentCSEs": aluGponPortCurrentCSEs,
       "aluGponPortCurrentAEs": aluGponPortCurrentAEs,
       "aluGponPortCurrentIMREs": aluGponPortCurrentIMREs,
       "aluGponPortCurrentLostFragsDn": aluGponPortCurrentLostFragsDn,
       "aluGponPortCurrentLostFragsUp": aluGponPortCurrentLostFragsUp,
       "aluGponPortCurrentRxFrags": aluGponPortCurrentRxFrags,
       "aluGponPortCurrentRxBlocks": aluGponPortCurrentRxBlocks,
       "aluGponPortCurrentTxBlocks": aluGponPortCurrentTxBlocks,
       "aluGponPortCurrentTxFrags": aluGponPortCurrentTxFrags,
       "aluGponPortCurrentBadHeaders": aluGponPortCurrentBadHeaders,
       "aluGponPortPreviousTable": aluGponPortPreviousTable,
       "aluGponPortPreviousEntry": aluGponPortPreviousEntry,
       "aluGponPortPreviousLastUpdTime": aluGponPortPreviousLastUpdTime,
       "aluGponPortPreviousPMEnabled": aluGponPortPreviousPMEnabled,
       "aluGponPortPreviousTxFrames": aluGponPortPreviousTxFrames,
       "aluGponPortPreviousRxFrames": aluGponPortPreviousRxFrames,
       "aluGponPortPreviousTxBytes": aluGponPortPreviousTxBytes,
       "aluGponPortPreviousRxBytes": aluGponPortPreviousRxBytes,
       "aluGponPortPreviousDropFrsUp": aluGponPortPreviousDropFrsUp,
       "aluGponPortPreviousDropFrsDn": aluGponPortPreviousDropFrsDn,
       "aluGponPortPreviousTxFrsMcast": aluGponPortPreviousTxFrsMcast,
       "aluGponPortPreviousRxFrsMcast": aluGponPortPreviousRxFrsMcast,
       "aluGponPortPreviousFCSEs": aluGponPortPreviousFCSEs,
       "aluGponPortPreviousECs": aluGponPortPreviousECs,
       "aluGponPortPreviousLCs": aluGponPortPreviousLCs,
       "aluGponPortPreviousFTLs": aluGponPortPreviousFTLs,
       "aluGponPortPreviousRBOs": aluGponPortPreviousRBOs,
       "aluGponPortPreviousTBOs": aluGponPortPreviousTBOs,
       "aluGponPortPreviousSCFs": aluGponPortPreviousSCFs,
       "aluGponPortPreviousMCFs": aluGponPortPreviousMCFs,
       "aluGponPortPreviousSQEs": aluGponPortPreviousSQEs,
       "aluGponPortPreviousDTs": aluGponPortPreviousDTs,
       "aluGponPortPreviousIMTEs": aluGponPortPreviousIMTEs,
       "aluGponPortPreviousCSEs": aluGponPortPreviousCSEs,
       "aluGponPortPreviousAEs": aluGponPortPreviousAEs,
       "aluGponPortPreviousIMREs": aluGponPortPreviousIMREs,
       "aluGponPortPreviousLostFragsDn": aluGponPortPreviousLostFragsDn,
       "aluGponPortPreviousLostFragsUp": aluGponPortPreviousLostFragsUp,
       "aluGponPortPreviousRxFrags": aluGponPortPreviousRxFrags,
       "aluGponPortPreviousRxBlocks": aluGponPortPreviousRxBlocks,
       "aluGponPortPreviousTxBlocks": aluGponPortPreviousTxBlocks,
       "aluGponPortPreviousTxFrags": aluGponPortPreviousTxFrags,
       "aluGponPortPreviousBadHeaders": aluGponPortPreviousBadHeaders,
       "aluXdslLineStatsTable": aluXdslLineStatsTable,
       "aluXdslLineStatsEntry": aluXdslLineStatsEntry,
       "aluXdslLineStatsNearEndFECS": aluXdslLineStatsNearEndFECS,
       "aluXdslLineStatsNearEndLOSS": aluXdslLineStatsNearEndLOSS,
       "aluXdslLineStatsNearEndES": aluXdslLineStatsNearEndES,
       "aluXdslLineStatsNearEndSES": aluXdslLineStatsNearEndSES,
       "aluXdslLineStatsNearEndUAS": aluXdslLineStatsNearEndUAS,
       "aluXdslLineStatsNearEndAS": aluXdslLineStatsNearEndAS,
       "aluXdslLineStatsNearEndLOFS": aluXdslLineStatsNearEndLOFS,
       "aluXdslLineStatsNearEndLPRS": aluXdslLineStatsNearEndLPRS,
       "aluXdslLineStatsNearEndLEFTRS": aluXdslLineStatsNearEndLEFTRS,
       "aluXdslLineStatsFarEndFECS": aluXdslLineStatsFarEndFECS,
       "aluXdslLineStatsFarEndLOSS": aluXdslLineStatsFarEndLOSS,
       "aluXdslLineStatsFarEndES": aluXdslLineStatsFarEndES,
       "aluXdslLineStatsFarEndSES": aluXdslLineStatsFarEndSES,
       "aluXdslLineStatsFarEndUAS": aluXdslLineStatsFarEndUAS,
       "aluXdslLineStatsFarEndAS": aluXdslLineStatsFarEndAS,
       "aluXdslLineStatsFarEndLOFS": aluXdslLineStatsFarEndLOFS,
       "aluXdslLineStatsFarEndLPRS": aluXdslLineStatsFarEndLPRS,
       "aluXdslLineStatsFarEndLEFTRS": aluXdslLineStatsFarEndLEFTRS,
       "aluXdslLineStatsUpTime": aluXdslLineStatsUpTime,
       "aluShdslLineStatsTable": aluShdslLineStatsTable,
       "aluShdslLineStatsEntry": aluShdslLineStatsEntry,
       "aluShdslLineStatsLinkLoss": aluShdslLineStatsLinkLoss,
       "aluShdslLineStatsCVError": aluShdslLineStatsCVError,
       "aluShdslLineStatsES": aluShdslLineStatsES,
       "aluShdslLineStatsSES": aluShdslLineStatsSES,
       "aluShdslLineStatsLOSWS": aluShdslLineStatsLOSWS,
       "aluShdslLineStatsUAS": aluShdslLineStatsUAS,
       "aluShdslLineStatsInvalidDataFlag": aluShdslLineStatsInvalidDataFlag,
       "aluPortCtlStatsTable": aluPortCtlStatsTable,
       "aluPortCtlStatsEntry": aluPortCtlStatsEntry,
       "aluPortAccessCtlInFwdPkts": aluPortAccessCtlInFwdPkts,
       "aluPortAccessCtlInFwdOcts": aluPortAccessCtlInFwdOcts,
       "aluPortAccessCtlInDroPkts": aluPortAccessCtlInDroPkts,
       "aluPortAccessCtlInDroOcts": aluPortAccessCtlInDroOcts,
       "aluPortAccessCtlEgrFwdPkts": aluPortAccessCtlEgrFwdPkts,
       "aluPortAccessCtlEgrFwdOcts": aluPortAccessCtlEgrFwdOcts,
       "aluPortAccessCtlEgrDroPkts": aluPortAccessCtlEgrDroPkts,
       "aluPortAccessCtlEgrDroOcts": aluPortAccessCtlEgrDroOcts,
       "aluFrIfStatsTable": aluFrIfStatsTable,
       "aluFrIfStatsEntry": aluFrIfStatsEntry,
       "aluFrIfRxFrames": aluFrIfRxFrames,
       "aluFrIfRxOctets": aluFrIfRxOctets,
       "aluFrIfRxDEFrames": aluFrIfRxDEFrames,
       "aluFrIfRxDEOctets": aluFrIfRxDEOctets,
       "aluFrIfRxFECNFrames": aluFrIfRxFECNFrames,
       "aluFrIfRxBECNFrames": aluFrIfRxBECNFrames,
       "aluFrIfTxFrames": aluFrIfTxFrames,
       "aluFrIfTxOctets": aluFrIfTxOctets,
       "aluFrIfTxDEFrames": aluFrIfTxDEFrames,
       "aluFrIfTxDEOctets": aluFrIfTxDEOctets,
       "aluFrIfTxFECNFrames": aluFrIfTxFECNFrames,
       "aluFrIfTxBECNFrames": aluFrIfTxBECNFrames,
       "aluFrIfRxDiscardsInvalidDlci": aluFrIfRxDiscardsInvalidDlci,
       "aluFrIfRxLastInvalidDlci": aluFrIfRxLastInvalidDlci,
       "aluFrIfRxDiscardsCrcErrors": aluFrIfRxDiscardsCrcErrors,
       "aluFrIfRxDiscardsAlignmentErrors": aluFrIfRxDiscardsAlignmentErrors,
       "aluFrIfRxDiscardsLengthViolations": aluFrIfRxDiscardsLengthViolations,
       "aluFrIfRxDiscardsIllegalHeader": aluFrIfRxDiscardsIllegalHeader,
       "aluFrIfRxDiscardsOtherErrors": aluFrIfRxDiscardsOtherErrors,
       "aluFrIfTxDiscardsUnderruns": aluFrIfTxDiscardsUnderruns,
       "aluFrIfTxDiscardsOtherErrors": aluFrIfTxDiscardsOtherErrors,
       "aluExtFrCircuitTable": aluExtFrCircuitTable,
       "aluExtFrCircuitEntry": aluExtFrCircuitEntry,
       "aluExtFrCircuitReceivedCrcDiscards": aluExtFrCircuitReceivedCrcDiscards,
       "aluExtFrCircuitReceivedAborts": aluExtFrCircuitReceivedAborts,
       "aluExtFrCircuitReceivedOtherDiscards": aluExtFrCircuitReceivedOtherDiscards,
       "aluExtFrCircuitSentAborts": aluExtFrCircuitSentAborts,
       "aluExtFrCircuitSentFECNs": aluExtFrCircuitSentFECNs,
       "aluExtFrCircuitSentBECNs": aluExtFrCircuitSentBECNs,
       "aluExtFrCircuitReceivedDEOctets": aluExtFrCircuitReceivedDEOctets,
       "aluExtFrCircuitSentDEOctets": aluExtFrCircuitSentDEOctets,
       "aluEthPtpTimestampStatsTable": aluEthPtpTimestampStatsTable,
       "aluEthPtpTimestampStatsEntry": aluEthPtpTimestampStatsEntry,
       "aluEthPtpInSyncPktTimestamped": aluEthPtpInSyncPktTimestamped,
       "aluEthPtpOutSyncPktTimestamped": aluEthPtpOutSyncPktTimestamped,
       "aluEthPtpInDelReqPktTimestamped": aluEthPtpInDelReqPktTimestamped,
       "aluEthPtpOutDelReqPktTimestamped": aluEthPtpOutDelReqPktTimestamped,
       "aluEthPtpInFcsErrorCount": aluEthPtpInFcsErrorCount,
       "aluEthPtpOutFcsErrorCount": aluEthPtpOutFcsErrorCount,
       "aluPortNotifyPrefix": aluPortNotifyPrefix,
       "aluPortNotification": aluPortNotification,
       "aluEqPortRS232Alarm": aluEqPortRS232Alarm,
       "aluEqPortRS232AlarmClear": aluEqPortRS232AlarmClear,
       "aluRS232LoopbackStarted": aluRS232LoopbackStarted,
       "aluRS232LoopbackStopped": aluRS232LoopbackStopped,
       "aluVoiceLoopbackStarted": aluVoiceLoopbackStarted,
       "aluVoiceLoopbackStopped": aluVoiceLoopbackStopped,
       "aluGponPortInbandAlarm": aluGponPortInbandAlarm,
       "aluGponPortInbandAlarmClear": aluGponPortInbandAlarmClear,
       "aluEqPortDataAlarm": aluEqPortDataAlarm,
       "aluEqPortDataAlarmClear": aluEqPortDataAlarmClear,
       "aluDataLoopbackStarted": aluDataLoopbackStarted,
       "aluDataLoopbackStopped": aluDataLoopbackStopped}
)

# SNMP MIB module (ALU-PTPV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/ALU-PTPV2-MIB.mib
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

(Alu1588PtpClockId,
 Alu1588PtpClockIndex,
 Alu1588PtpPortState) = mibBuilder.importSymbols(
    "ALU-IEEE1588-PTP-MIB",
    "Alu1588PtpClockId",
    "Alu1588PtpClockIndex",
    "Alu1588PtpPortState")

(aluSARConfs,
 aluSARMIBModules,
 aluSARNotifyPrefix,
 aluSARObjs) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARConfs",
    "aluSARMIBModules",
    "aluSARNotifyPrefix",
    "aluSARObjs")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(TmnxChassisIndex,
 TmnxHwIndexOrZero,
 TmnxPortAdminStatus,
 TmnxSETSRefSource,
 tmnxChassisIndex) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxChassisIndex",
    "TmnxHwIndexOrZero",
    "TmnxPortAdminStatus",
    "TmnxSETSRefSource",
    "tmnxChassisIndex")

(TItemDescription,
 TNamedItemOrEmpty,
 TmnxAdminState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItemOrEmpty",
    "TmnxAdminState")


# MODULE-IDENTITY

aluPtpV2Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 12)
)
if mibBuilder.loadTexts:
    aluPtpV2Module.setRevisions(
        ("1911-08-18 00:00",
         "1910-08-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Alu1588PtpPortIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )



class Alu1588PtpMasterIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )



class Alu1588PtpProfile(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("ituTelecomFreq", 1),
          ("ieee1588-2008", 2))
    )



class Alu1588PtpClockStepType(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("oneStep", 1),
          ("twoStep", 2))
    )



class Alu1588PtpClockType(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 0),
          ("boundary", 1),
          ("ordinary", 2),
          ("endToEndTransparent", 3),
          ("peerToPeerTransparent", 4),
          ("managementNode", 5))
    )



class Alu1588PtpLogInterval(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7, 4),
    )



class Alu1588PtpClockRecoveryState(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 0),
          ("freeRun", 1),
          ("acquiring", 2),
          ("phase-tracking", 3),
          ("holdover", 4),
          ("locked", 5))
    )



class AluPtpTimeSource(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              48,
              64,
              80,
              96,
              144,
              160,
              255)
        )
    )
    namedValues = NamedValues(
        *(("atomic-clock", 16),
          ("gps", 32),
          ("terrestrial-radio", 48),
          ("ptp", 64),
          ("ntp", 80),
          ("hand-set", 96),
          ("other", 144),
          ("internal-osc", 160),
          ("reserved", 255))
    )



class Alu1588PtpFreqSource(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("ptp", 1),
          ("ssu", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AluPtpMIBConformance_ObjectIdentity = ObjectIdentity
aluPtpMIBConformance = _AluPtpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 12)
)
_AluPtpConformance_ObjectIdentity = ObjectIdentity
aluPtpConformance = _AluPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 12, 1)
)
_AluPtpCompliances_ObjectIdentity = ObjectIdentity
aluPtpCompliances = _AluPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 12, 1, 1)
)
_AluPtpComp7705_ObjectIdentity = ObjectIdentity
aluPtpComp7705 = _AluPtpComp7705_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 12, 1, 1, 1)
)
_AluPtpGroups_ObjectIdentity = ObjectIdentity
aluPtpGroups = _AluPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 12, 1, 2)
)
_AluPtpObjs_ObjectIdentity = ObjectIdentity
aluPtpObjs = _AluPtpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12)
)
_AluPtpClock_ObjectIdentity = ObjectIdentity
aluPtpClock = _AluPtpClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1)
)


class _AluPtpClockMaxNumber_Type(Integer32):
    """Custom type aluPtpClockMaxNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AluPtpClockMaxNumber_Type.__name__ = "Integer32"
_AluPtpClockMaxNumber_Object = MibScalar
aluPtpClockMaxNumber = _AluPtpClockMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 1),
    _AluPtpClockMaxNumber_Type()
)
aluPtpClockMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockMaxNumber.setStatus("current")
_AluPtpClockTable_Object = MibTable
aluPtpClockTable = _AluPtpClockTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 2)
)
if mibBuilder.loadTexts:
    aluPtpClockTable.setStatus("current")
_AluPtpClockEntry_Object = MibTableRow
aluPtpClockEntry = _AluPtpClockEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 2, 1)
)
aluPtpClockEntry.setIndexNames(
    (0, "ALU-PTPV2-MIB", "aluPtpClockIndex"),
)
if mibBuilder.loadTexts:
    aluPtpClockEntry.setStatus("current")
_AluPtpClockIndex_Type = Alu1588PtpClockIndex
_AluPtpClockIndex_Object = MibTableColumn
aluPtpClockIndex = _AluPtpClockIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 2, 1, 1),
    _AluPtpClockIndex_Type()
)
aluPtpClockIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluPtpClockIndex.setStatus("current")
_AluPtpClockRowStatus_Type = RowStatus
_AluPtpClockRowStatus_Object = MibTableColumn
aluPtpClockRowStatus = _AluPtpClockRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 2, 1, 2),
    _AluPtpClockRowStatus_Type()
)
aluPtpClockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluPtpClockRowStatus.setStatus("current")


class _AluPtpClockIpInterface_Type(TNamedItemOrEmpty):
    """Custom type aluPtpClockIpInterface based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluPtpClockIpInterface_Type.__name__ = "TNamedItemOrEmpty"
_AluPtpClockIpInterface_Object = MibTableColumn
aluPtpClockIpInterface = _AluPtpClockIpInterface_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 2, 1, 3),
    _AluPtpClockIpInterface_Type()
)
aluPtpClockIpInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluPtpClockIpInterface.setStatus("current")


class _AluPtpClockHw_Type(TmnxHwIndexOrZero):
    """Custom type aluPtpClockHw based on TmnxHwIndexOrZero"""
    defaultValue = 0


_AluPtpClockHw_Type.__name__ = "TmnxHwIndexOrZero"
_AluPtpClockHw_Object = MibTableColumn
aluPtpClockHw = _AluPtpClockHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 2, 1, 4),
    _AluPtpClockHw_Type()
)
aluPtpClockHw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluPtpClockHw.setStatus("current")


class _AluPtpClockProfile_Type(Alu1588PtpProfile):
    """Custom type aluPtpClockProfile based on Alu1588PtpProfile"""
    defaultValue = 2


_AluPtpClockProfile_Type.__name__ = "Alu1588PtpProfile"
_AluPtpClockProfile_Object = MibTableColumn
aluPtpClockProfile = _AluPtpClockProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 2, 1, 5),
    _AluPtpClockProfile_Type()
)
aluPtpClockProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluPtpClockProfile.setStatus("current")


class _AluPtpClockAdminState_Type(TmnxAdminState):
    """Custom type aluPtpClockAdminState based on TmnxAdminState"""
    defaultValue = 3


_AluPtpClockAdminState_Type.__name__ = "TmnxAdminState"
_AluPtpClockAdminState_Object = MibTableColumn
aluPtpClockAdminState = _AluPtpClockAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 2, 1, 6),
    _AluPtpClockAdminState_Type()
)
aluPtpClockAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluPtpClockAdminState.setStatus("current")


class _AluPtpClockDynamicPeers_Type(TruthValue):
    """Custom type aluPtpClockDynamicPeers based on TruthValue"""
    defaultValue = 2


_AluPtpClockDynamicPeers_Type.__name__ = "TruthValue"
_AluPtpClockDynamicPeers_Object = MibTableColumn
aluPtpClockDynamicPeers = _AluPtpClockDynamicPeers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 2, 1, 7),
    _AluPtpClockDynamicPeers_Type()
)
aluPtpClockDynamicPeers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluPtpClockDynamicPeers.setStatus("current")


class _AluPtpClockForwardWeight_Type(Integer32):
    """Custom type aluPtpClockForwardWeight based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_AluPtpClockForwardWeight_Type.__name__ = "Integer32"
_AluPtpClockForwardWeight_Object = MibTableColumn
aluPtpClockForwardWeight = _AluPtpClockForwardWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 2, 1, 8),
    _AluPtpClockForwardWeight_Type()
)
aluPtpClockForwardWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockForwardWeight.setStatus("current")


class _AluPtpClockRecoveryState_Type(Alu1588PtpClockRecoveryState):
    """Custom type aluPtpClockRecoveryState based on Alu1588PtpClockRecoveryState"""
    defaultValue = 0


_AluPtpClockRecoveryState_Type.__name__ = "Alu1588PtpClockRecoveryState"
_AluPtpClockRecoveryState_Object = MibTableColumn
aluPtpClockRecoveryState = _AluPtpClockRecoveryState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 2, 1, 9),
    _AluPtpClockRecoveryState_Type()
)
aluPtpClockRecoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockRecoveryState.setStatus("current")


class _AluPtpClockTimeRefPriority_Type(Integer32):
    """Custom type aluPtpClockTimeRefPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AluPtpClockTimeRefPriority_Type.__name__ = "Integer32"
_AluPtpClockTimeRefPriority_Object = MibTableColumn
aluPtpClockTimeRefPriority = _AluPtpClockTimeRefPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 2, 1, 10),
    _AluPtpClockTimeRefPriority_Type()
)
aluPtpClockTimeRefPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluPtpClockTimeRefPriority.setStatus("current")


class _AluPtpClockAdminFreqSource_Type(Alu1588PtpFreqSource):
    """Custom type aluPtpClockAdminFreqSource based on Alu1588PtpFreqSource"""
    defaultValue = 1


_AluPtpClockAdminFreqSource_Type.__name__ = "Alu1588PtpFreqSource"
_AluPtpClockAdminFreqSource_Object = MibTableColumn
aluPtpClockAdminFreqSource = _AluPtpClockAdminFreqSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 2, 1, 11),
    _AluPtpClockAdminFreqSource_Type()
)
aluPtpClockAdminFreqSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluPtpClockAdminFreqSource.setStatus("current")
_AluPtpClockOperFreqSource_Type = Alu1588PtpFreqSource
_AluPtpClockOperFreqSource_Object = MibTableColumn
aluPtpClockOperFreqSource = _AluPtpClockOperFreqSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 2, 1, 12),
    _AluPtpClockOperFreqSource_Type()
)
aluPtpClockOperFreqSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockOperFreqSource.setStatus("current")
_AluPtpClockDefaultDSTable_Object = MibTable
aluPtpClockDefaultDSTable = _AluPtpClockDefaultDSTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 3)
)
if mibBuilder.loadTexts:
    aluPtpClockDefaultDSTable.setStatus("current")
_AluPtpClockDefaultDSEntry_Object = MibTableRow
aluPtpClockDefaultDSEntry = _AluPtpClockDefaultDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aluPtpClockDefaultDSEntry.setStatus("current")
_AluPtpClockId_Type = Alu1588PtpClockId
_AluPtpClockId_Object = MibTableColumn
aluPtpClockId = _AluPtpClockId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 3, 1, 1),
    _AluPtpClockId_Type()
)
aluPtpClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockId.setStatus("current")


class _AluPtpClockType_Type(Alu1588PtpClockType):
    """Custom type aluPtpClockType based on Alu1588PtpClockType"""
    defaultValue = 2


_AluPtpClockType_Type.__name__ = "Alu1588PtpClockType"
_AluPtpClockType_Object = MibTableColumn
aluPtpClockType = _AluPtpClockType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 3, 1, 2),
    _AluPtpClockType_Type()
)
aluPtpClockType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluPtpClockType.setStatus("current")


class _AluPtpClockSlaveOnly_Type(TruthValue):
    """Custom type aluPtpClockSlaveOnly based on TruthValue"""
    defaultValue = 1


_AluPtpClockSlaveOnly_Type.__name__ = "TruthValue"
_AluPtpClockSlaveOnly_Object = MibTableColumn
aluPtpClockSlaveOnly = _AluPtpClockSlaveOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 3, 1, 3),
    _AluPtpClockSlaveOnly_Type()
)
aluPtpClockSlaveOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluPtpClockSlaveOnly.setStatus("current")


class _AluPtpClockDomain_Type(Unsigned32):
    """Custom type aluPtpClockDomain based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AluPtpClockDomain_Type.__name__ = "Unsigned32"
_AluPtpClockDomain_Object = MibTableColumn
aluPtpClockDomain = _AluPtpClockDomain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 3, 1, 4),
    _AluPtpClockDomain_Type()
)
aluPtpClockDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluPtpClockDomain.setStatus("current")


class _AluPtpClockNumberPorts_Type(Unsigned32):
    """Custom type aluPtpClockNumberPorts based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AluPtpClockNumberPorts_Type.__name__ = "Unsigned32"
_AluPtpClockNumberPorts_Object = MibTableColumn
aluPtpClockNumberPorts = _AluPtpClockNumberPorts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 3, 1, 5),
    _AluPtpClockNumberPorts_Type()
)
aluPtpClockNumberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockNumberPorts.setStatus("current")


class _AluPtpClockClass_Type(Unsigned32):
    """Custom type aluPtpClockClass based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AluPtpClockClass_Type.__name__ = "Unsigned32"
_AluPtpClockClass_Object = MibTableColumn
aluPtpClockClass = _AluPtpClockClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 3, 1, 6),
    _AluPtpClockClass_Type()
)
aluPtpClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockClass.setStatus("current")


class _AluPtpClockAccuracy_Type(Unsigned32):
    """Custom type aluPtpClockAccuracy based on Unsigned32"""
    defaultValue = 254

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AluPtpClockAccuracy_Type.__name__ = "Unsigned32"
_AluPtpClockAccuracy_Object = MibTableColumn
aluPtpClockAccuracy = _AluPtpClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 3, 1, 7),
    _AluPtpClockAccuracy_Type()
)
aluPtpClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockAccuracy.setStatus("current")


class _AluPtpClockVariance_Type(Integer32):
    """Custom type aluPtpClockVariance based on Integer32"""
    defaultValue = 65535


_AluPtpClockVariance_Type.__name__ = "Integer32"
_AluPtpClockVariance_Object = MibTableColumn
aluPtpClockVariance = _AluPtpClockVariance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 3, 1, 8),
    _AluPtpClockVariance_Type()
)
aluPtpClockVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockVariance.setStatus("current")


class _AluPtpClockPriority1_Type(Unsigned32):
    """Custom type aluPtpClockPriority1 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AluPtpClockPriority1_Type.__name__ = "Unsigned32"
_AluPtpClockPriority1_Object = MibTableColumn
aluPtpClockPriority1 = _AluPtpClockPriority1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 3, 1, 9),
    _AluPtpClockPriority1_Type()
)
aluPtpClockPriority1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluPtpClockPriority1.setStatus("current")


class _AluPtpClockPriority2_Type(Unsigned32):
    """Custom type aluPtpClockPriority2 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AluPtpClockPriority2_Type.__name__ = "Unsigned32"
_AluPtpClockPriority2_Object = MibTableColumn
aluPtpClockPriority2 = _AluPtpClockPriority2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 3, 1, 10),
    _AluPtpClockPriority2_Type()
)
aluPtpClockPriority2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluPtpClockPriority2.setStatus("current")
_AluPtpClockTwoStepFlag_Type = Alu1588PtpClockStepType
_AluPtpClockTwoStepFlag_Object = MibTableColumn
aluPtpClockTwoStepFlag = _AluPtpClockTwoStepFlag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 3, 1, 11),
    _AluPtpClockTwoStepFlag_Type()
)
aluPtpClockTwoStepFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockTwoStepFlag.setStatus("current")
_AluPtpClockCurrentDSTable_Object = MibTable
aluPtpClockCurrentDSTable = _AluPtpClockCurrentDSTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 4)
)
if mibBuilder.loadTexts:
    aluPtpClockCurrentDSTable.setStatus("current")
_AluPtpClockCurrentDSEntry_Object = MibTableRow
aluPtpClockCurrentDSEntry = _AluPtpClockCurrentDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 4, 1)
)
if mibBuilder.loadTexts:
    aluPtpClockCurrentDSEntry.setStatus("current")


class _AluPtpClockStepsRemoved_Type(Unsigned32):
    """Custom type aluPtpClockStepsRemoved based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AluPtpClockStepsRemoved_Type.__name__ = "Unsigned32"
_AluPtpClockStepsRemoved_Object = MibTableColumn
aluPtpClockStepsRemoved = _AluPtpClockStepsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 4, 1, 2),
    _AluPtpClockStepsRemoved_Type()
)
aluPtpClockStepsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockStepsRemoved.setStatus("current")
_AluPtpClockParentDSTable_Object = MibTable
aluPtpClockParentDSTable = _AluPtpClockParentDSTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 5)
)
if mibBuilder.loadTexts:
    aluPtpClockParentDSTable.setStatus("current")
_AluPtpClockParentDSEntry_Object = MibTableRow
aluPtpClockParentDSEntry = _AluPtpClockParentDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 5, 1)
)
if mibBuilder.loadTexts:
    aluPtpClockParentDSEntry.setStatus("current")
_AluPtpClockParentId_Type = Alu1588PtpClockId
_AluPtpClockParentId_Object = MibTableColumn
aluPtpClockParentId = _AluPtpClockParentId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 5, 1, 1),
    _AluPtpClockParentId_Type()
)
aluPtpClockParentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockParentId.setStatus("current")


class _AluPtpClockParentPortNum_Type(Unsigned32):
    """Custom type aluPtpClockParentPortNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AluPtpClockParentPortNum_Type.__name__ = "Unsigned32"
_AluPtpClockParentPortNum_Object = MibTableColumn
aluPtpClockParentPortNum = _AluPtpClockParentPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 5, 1, 2),
    _AluPtpClockParentPortNum_Type()
)
aluPtpClockParentPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockParentPortNum.setStatus("current")
_AluPtpClockParentStats_Type = TruthValue
_AluPtpClockParentStats_Object = MibTableColumn
aluPtpClockParentStats = _AluPtpClockParentStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 5, 1, 3),
    _AluPtpClockParentStats_Type()
)
aluPtpClockParentStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockParentStats.setStatus("current")
_AluPtpClockParentVariance_Type = Integer32
_AluPtpClockParentVariance_Object = MibTableColumn
aluPtpClockParentVariance = _AluPtpClockParentVariance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 5, 1, 4),
    _AluPtpClockParentVariance_Type()
)
aluPtpClockParentVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockParentVariance.setStatus("current")
_AluPtpClockGMClockId_Type = Alu1588PtpClockId
_AluPtpClockGMClockId_Object = MibTableColumn
aluPtpClockGMClockId = _AluPtpClockGMClockId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 5, 1, 6),
    _AluPtpClockGMClockId_Type()
)
aluPtpClockGMClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockGMClockId.setStatus("current")


class _AluPtpClockGMClass_Type(Unsigned32):
    """Custom type aluPtpClockGMClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AluPtpClockGMClass_Type.__name__ = "Unsigned32"
_AluPtpClockGMClass_Object = MibTableColumn
aluPtpClockGMClass = _AluPtpClockGMClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 5, 1, 7),
    _AluPtpClockGMClass_Type()
)
aluPtpClockGMClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockGMClass.setStatus("current")


class _AluPtpClockGMAccuracy_Type(Unsigned32):
    """Custom type aluPtpClockGMAccuracy based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AluPtpClockGMAccuracy_Type.__name__ = "Unsigned32"
_AluPtpClockGMAccuracy_Object = MibTableColumn
aluPtpClockGMAccuracy = _AluPtpClockGMAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 5, 1, 8),
    _AluPtpClockGMAccuracy_Type()
)
aluPtpClockGMAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockGMAccuracy.setStatus("current")
_AluPtpClockGMVariance_Type = Unsigned32
_AluPtpClockGMVariance_Object = MibTableColumn
aluPtpClockGMVariance = _AluPtpClockGMVariance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 5, 1, 9),
    _AluPtpClockGMVariance_Type()
)
aluPtpClockGMVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockGMVariance.setStatus("current")


class _AluPtpClockGMPriority1_Type(Unsigned32):
    """Custom type aluPtpClockGMPriority1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AluPtpClockGMPriority1_Type.__name__ = "Unsigned32"
_AluPtpClockGMPriority1_Object = MibTableColumn
aluPtpClockGMPriority1 = _AluPtpClockGMPriority1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 5, 1, 10),
    _AluPtpClockGMPriority1_Type()
)
aluPtpClockGMPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockGMPriority1.setStatus("current")


class _AluPtpClockGMPriority2_Type(Unsigned32):
    """Custom type aluPtpClockGMPriority2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AluPtpClockGMPriority2_Type.__name__ = "Unsigned32"
_AluPtpClockGMPriority2_Object = MibTableColumn
aluPtpClockGMPriority2 = _AluPtpClockGMPriority2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 5, 1, 11),
    _AluPtpClockGMPriority2_Type()
)
aluPtpClockGMPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockGMPriority2.setStatus("current")
_AluPtpClockTimePropertyDSTable_Object = MibTable
aluPtpClockTimePropertyDSTable = _AluPtpClockTimePropertyDSTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 6)
)
if mibBuilder.loadTexts:
    aluPtpClockTimePropertyDSTable.setStatus("current")
_AluPtpClockTimePropertyDSEntry_Object = MibTableRow
aluPtpClockTimePropertyDSEntry = _AluPtpClockTimePropertyDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 6, 1)
)
if mibBuilder.loadTexts:
    aluPtpClockTimePropertyDSEntry.setStatus("current")


class _AluPtpClockCurUtcOffset_Type(Integer32):
    """Custom type aluPtpClockCurUtcOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65536, 65535),
    )


_AluPtpClockCurUtcOffset_Type.__name__ = "Integer32"
_AluPtpClockCurUtcOffset_Object = MibTableColumn
aluPtpClockCurUtcOffset = _AluPtpClockCurUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 6, 1, 1),
    _AluPtpClockCurUtcOffset_Type()
)
aluPtpClockCurUtcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockCurUtcOffset.setStatus("current")
_AluPtpClockCurUtcOffsetValid_Type = TruthValue
_AluPtpClockCurUtcOffsetValid_Object = MibTableColumn
aluPtpClockCurUtcOffsetValid = _AluPtpClockCurUtcOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 6, 1, 2),
    _AluPtpClockCurUtcOffsetValid_Type()
)
aluPtpClockCurUtcOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockCurUtcOffsetValid.setStatus("current")
_AluPtpClockLeap59_Type = TruthValue
_AluPtpClockLeap59_Object = MibTableColumn
aluPtpClockLeap59 = _AluPtpClockLeap59_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 6, 1, 3),
    _AluPtpClockLeap59_Type()
)
aluPtpClockLeap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockLeap59.setStatus("current")
_AluPtpClockLeap61_Type = TruthValue
_AluPtpClockLeap61_Object = MibTableColumn
aluPtpClockLeap61 = _AluPtpClockLeap61_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 6, 1, 4),
    _AluPtpClockLeap61_Type()
)
aluPtpClockLeap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockLeap61.setStatus("current")
_AluPtpClockTimeTraceable_Type = TruthValue
_AluPtpClockTimeTraceable_Object = MibTableColumn
aluPtpClockTimeTraceable = _AluPtpClockTimeTraceable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 6, 1, 6),
    _AluPtpClockTimeTraceable_Type()
)
aluPtpClockTimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockTimeTraceable.setStatus("current")
_AluPtpClockFreqTraceable_Type = TruthValue
_AluPtpClockFreqTraceable_Object = MibTableColumn
aluPtpClockFreqTraceable = _AluPtpClockFreqTraceable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 6, 1, 7),
    _AluPtpClockFreqTraceable_Type()
)
aluPtpClockFreqTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockFreqTraceable.setStatus("current")
_AluPtpClockPtpTimescale_Type = TruthValue
_AluPtpClockPtpTimescale_Object = MibTableColumn
aluPtpClockPtpTimescale = _AluPtpClockPtpTimescale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 6, 1, 8),
    _AluPtpClockPtpTimescale_Type()
)
aluPtpClockPtpTimescale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockPtpTimescale.setStatus("current")
_AluPtpClockTimeSource_Type = AluPtpTimeSource
_AluPtpClockTimeSource_Object = MibTableColumn
aluPtpClockTimeSource = _AluPtpClockTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 1, 6, 1, 9),
    _AluPtpClockTimeSource_Type()
)
aluPtpClockTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpClockTimeSource.setStatus("current")
_AluPtpPort_ObjectIdentity = ObjectIdentity
aluPtpPort = _AluPtpPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 2)
)
_AluPtpPortTable_Object = MibTable
aluPtpPortTable = _AluPtpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 2, 1)
)
if mibBuilder.loadTexts:
    aluPtpPortTable.setStatus("current")
_AluPtpPortEntry_Object = MibTableRow
aluPtpPortEntry = _AluPtpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 2, 1, 1)
)
aluPtpPortEntry.setIndexNames(
    (0, "ALU-PTPV2-MIB", "aluPtpPortClockIndex"),
    (0, "ALU-PTPV2-MIB", "aluPtpPortIndex"),
)
if mibBuilder.loadTexts:
    aluPtpPortEntry.setStatus("current")
_AluPtpPortClockIndex_Type = Alu1588PtpClockIndex
_AluPtpPortClockIndex_Object = MibTableColumn
aluPtpPortClockIndex = _AluPtpPortClockIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 2, 1, 1, 1),
    _AluPtpPortClockIndex_Type()
)
aluPtpPortClockIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluPtpPortClockIndex.setStatus("current")
_AluPtpPortIndex_Type = Alu1588PtpPortIndex
_AluPtpPortIndex_Object = MibTableColumn
aluPtpPortIndex = _AluPtpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 2, 1, 1, 2),
    _AluPtpPortIndex_Type()
)
aluPtpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluPtpPortIndex.setStatus("current")


class _AluPtpPortAdminState_Type(TmnxAdminState):
    """Custom type aluPtpPortAdminState based on TmnxAdminState"""
    defaultValue = 3


_AluPtpPortAdminState_Type.__name__ = "TmnxAdminState"
_AluPtpPortAdminState_Object = MibTableColumn
aluPtpPortAdminState = _AluPtpPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 2, 1, 1, 3),
    _AluPtpPortAdminState_Type()
)
aluPtpPortAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluPtpPortAdminState.setStatus("current")


class _AluPtpPortUcNegotiate_Type(TruthValue):
    """Custom type aluPtpPortUcNegotiate based on TruthValue"""
    defaultValue = 1


_AluPtpPortUcNegotiate_Type.__name__ = "TruthValue"
_AluPtpPortUcNegotiate_Object = MibTableColumn
aluPtpPortUcNegotiate = _AluPtpPortUcNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 2, 1, 1, 4),
    _AluPtpPortUcNegotiate_Type()
)
aluPtpPortUcNegotiate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluPtpPortUcNegotiate.setStatus("current")


class _AluPtpPortNumPeers_Type(Unsigned32):
    """Custom type aluPtpPortNumPeers based on Unsigned32"""
    defaultValue = 2


_AluPtpPortNumPeers_Type.__name__ = "Unsigned32"
_AluPtpPortNumPeers_Object = MibTableColumn
aluPtpPortNumPeers = _AluPtpPortNumPeers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 2, 1, 1, 5),
    _AluPtpPortNumPeers_Type()
)
aluPtpPortNumPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPortNumPeers.setStatus("current")
_AluPtpPortDSTable_Object = MibTable
aluPtpPortDSTable = _AluPtpPortDSTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 2, 2)
)
if mibBuilder.loadTexts:
    aluPtpPortDSTable.setStatus("current")
_AluPtpPortDSEntry_Object = MibTableRow
aluPtpPortDSEntry = _AluPtpPortDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 2, 2, 1)
)
if mibBuilder.loadTexts:
    aluPtpPortDSEntry.setStatus("current")


class _AluPtpPortDSPortNum_Type(Unsigned32):
    """Custom type aluPtpPortDSPortNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AluPtpPortDSPortNum_Type.__name__ = "Unsigned32"
_AluPtpPortDSPortNum_Object = MibTableColumn
aluPtpPortDSPortNum = _AluPtpPortDSPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 2, 2, 1, 1),
    _AluPtpPortDSPortNum_Type()
)
aluPtpPortDSPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPortDSPortNum.setStatus("current")


class _AluPtpPortDSAnnoRxTimeout_Type(Unsigned32):
    """Custom type aluPtpPortDSAnnoRxTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_AluPtpPortDSAnnoRxTimeout_Type.__name__ = "Unsigned32"
_AluPtpPortDSAnnoRxTimeout_Object = MibTableColumn
aluPtpPortDSAnnoRxTimeout = _AluPtpPortDSAnnoRxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 2, 2, 1, 2),
    _AluPtpPortDSAnnoRxTimeout_Type()
)
aluPtpPortDSAnnoRxTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluPtpPortDSAnnoRxTimeout.setStatus("current")


class _AluPtpPortDSLogAnnoInterval_Type(Integer32):
    """Custom type aluPtpPortDSLogAnnoInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AluPtpPortDSLogAnnoInterval_Type.__name__ = "Integer32"
_AluPtpPortDSLogAnnoInterval_Object = MibTableColumn
aluPtpPortDSLogAnnoInterval = _AluPtpPortDSLogAnnoInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 2, 2, 1, 3),
    _AluPtpPortDSLogAnnoInterval_Type()
)
aluPtpPortDSLogAnnoInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluPtpPortDSLogAnnoInterval.setStatus("current")


class _AluPtpPortDSLogSyncInterval_Type(Integer32):
    """Custom type aluPtpPortDSLogSyncInterval based on Integer32"""
    defaultValue = -6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7, -6),
    )


_AluPtpPortDSLogSyncInterval_Type.__name__ = "Integer32"
_AluPtpPortDSLogSyncInterval_Object = MibTableColumn
aluPtpPortDSLogSyncInterval = _AluPtpPortDSLogSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 2, 2, 1, 4),
    _AluPtpPortDSLogSyncInterval_Type()
)
aluPtpPortDSLogSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluPtpPortDSLogSyncInterval.setStatus("current")


class _AluPtpPortDSPortState_Type(Alu1588PtpPortState):
    """Custom type aluPtpPortDSPortState based on Alu1588PtpPortState"""
    defaultValue = 1


_AluPtpPortDSPortState_Type.__name__ = "Alu1588PtpPortState"
_AluPtpPortDSPortState_Object = MibTableColumn
aluPtpPortDSPortState = _AluPtpPortDSPortState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 2, 2, 1, 5),
    _AluPtpPortDSPortState_Type()
)
aluPtpPortDSPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPortDSPortState.setStatus("current")


class _AluPtpPortDSDelayMechanism_Type(Integer32):
    """Custom type aluPtpPortDSDelayMechanism based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254)
        )
    )
    namedValues = NamedValues(
        *(("e2e", 1),
          ("p2p", 2),
          ("disabled", 254))
    )


_AluPtpPortDSDelayMechanism_Type.__name__ = "Integer32"
_AluPtpPortDSDelayMechanism_Object = MibTableColumn
aluPtpPortDSDelayMechanism = _AluPtpPortDSDelayMechanism_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 2, 2, 1, 6),
    _AluPtpPortDSDelayMechanism_Type()
)
aluPtpPortDSDelayMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPortDSDelayMechanism.setStatus("current")


class _AluPtpPortDSVersionNumber_Type(Integer32):
    """Custom type aluPtpPortDSVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("v2", 2)
    )


_AluPtpPortDSVersionNumber_Type.__name__ = "Integer32"
_AluPtpPortDSVersionNumber_Object = MibTableColumn
aluPtpPortDSVersionNumber = _AluPtpPortDSVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 2, 2, 1, 7),
    _AluPtpPortDSVersionNumber_Type()
)
aluPtpPortDSVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPortDSVersionNumber.setStatus("current")
_AluPtpPeer_ObjectIdentity = ObjectIdentity
aluPtpPeer = _AluPtpPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3)
)
_AluPtpUcMasterTable_Object = MibTable
aluPtpUcMasterTable = _AluPtpUcMasterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 1)
)
if mibBuilder.loadTexts:
    aluPtpUcMasterTable.setStatus("current")
_AluPtpUcMasterEntry_Object = MibTableRow
aluPtpUcMasterEntry = _AluPtpUcMasterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 1, 1)
)
aluPtpUcMasterEntry.setIndexNames(
    (0, "ALU-PTPV2-MIB", "aluPtpPeerClockIndex"),
    (0, "ALU-PTPV2-MIB", "aluPtpPeerPortIndex"),
    (0, "ALU-PTPV2-MIB", "aluPtpPeerIndex"),
)
if mibBuilder.loadTexts:
    aluPtpUcMasterEntry.setStatus("current")
_AluPtpPeerClockIndex_Type = Alu1588PtpClockIndex
_AluPtpPeerClockIndex_Object = MibTableColumn
aluPtpPeerClockIndex = _AluPtpPeerClockIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 1, 1, 1),
    _AluPtpPeerClockIndex_Type()
)
aluPtpPeerClockIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluPtpPeerClockIndex.setStatus("current")
_AluPtpPeerPortIndex_Type = Alu1588PtpPortIndex
_AluPtpPeerPortIndex_Object = MibTableColumn
aluPtpPeerPortIndex = _AluPtpPeerPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 1, 1, 2),
    _AluPtpPeerPortIndex_Type()
)
aluPtpPeerPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluPtpPeerPortIndex.setStatus("current")
_AluPtpPeerIndex_Type = Alu1588PtpMasterIndex
_AluPtpPeerIndex_Object = MibTableColumn
aluPtpPeerIndex = _AluPtpPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 1, 1, 3),
    _AluPtpPeerIndex_Type()
)
aluPtpPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluPtpPeerIndex.setStatus("current")


class _AluPtpPeerIpAddrType_Type(InetAddressType):
    """Custom type aluPtpPeerIpAddrType based on InetAddressType"""
    defaultValue = 0


_AluPtpPeerIpAddrType_Type.__name__ = "InetAddressType"
_AluPtpPeerIpAddrType_Object = MibTableColumn
aluPtpPeerIpAddrType = _AluPtpPeerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 1, 1, 4),
    _AluPtpPeerIpAddrType_Type()
)
aluPtpPeerIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluPtpPeerIpAddrType.setStatus("current")


class _AluPtpPeerIpAddr_Type(InetAddress):
    """Custom type aluPtpPeerIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AluPtpPeerIpAddr_Type.__name__ = "InetAddress"
_AluPtpPeerIpAddr_Object = MibTableColumn
aluPtpPeerIpAddr = _AluPtpPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 1, 1, 5),
    _AluPtpPeerIpAddr_Type()
)
aluPtpPeerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluPtpPeerIpAddr.setStatus("current")
_AluPtpPeerLastChanged_Type = TimeStamp
_AluPtpPeerLastChanged_Object = MibTableColumn
aluPtpPeerLastChanged = _AluPtpPeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 1, 1, 6),
    _AluPtpPeerLastChanged_Type()
)
aluPtpPeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerLastChanged.setStatus("current")


class _AluPtpPeerDescription_Type(TItemDescription):
    """Custom type aluPtpPeerDescription based on TItemDescription"""
    defaultHexValue = ""


_AluPtpPeerDescription_Type.__name__ = "TItemDescription"
_AluPtpPeerDescription_Object = MibTableColumn
aluPtpPeerDescription = _AluPtpPeerDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 1, 1, 7),
    _AluPtpPeerDescription_Type()
)
aluPtpPeerDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluPtpPeerDescription.setStatus("current")


class _AluPtpPeerDiscovered_Type(TruthValue):
    """Custom type aluPtpPeerDiscovered based on TruthValue"""
    defaultValue = 2


_AluPtpPeerDiscovered_Type.__name__ = "TruthValue"
_AluPtpPeerDiscovered_Object = MibTableColumn
aluPtpPeerDiscovered = _AluPtpPeerDiscovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 1, 1, 8),
    _AluPtpPeerDiscovered_Type()
)
aluPtpPeerDiscovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerDiscovered.setStatus("current")
_AluPtpPeerPacketStatsTable_Object = MibTable
aluPtpPeerPacketStatsTable = _AluPtpPeerPacketStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2)
)
if mibBuilder.loadTexts:
    aluPtpPeerPacketStatsTable.setStatus("current")
_AluPtpPeerPacketStatsEntry_Object = MibTableRow
aluPtpPeerPacketStatsEntry = _AluPtpPeerPacketStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1)
)
if mibBuilder.loadTexts:
    aluPtpPeerPacketStatsEntry.setStatus("current")
_AluPtpPeerPacketLastUpdateTime_Type = TimeStamp
_AluPtpPeerPacketLastUpdateTime_Object = MibTableColumn
aluPtpPeerPacketLastUpdateTime = _AluPtpPeerPacketLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 1),
    _AluPtpPeerPacketLastUpdateTime_Type()
)
aluPtpPeerPacketLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerPacketLastUpdateTime.setStatus("current")
_AluPtpPeerBadVersionDisc_Type = Counter64
_AluPtpPeerBadVersionDisc_Object = MibTableColumn
aluPtpPeerBadVersionDisc = _AluPtpPeerBadVersionDisc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 2),
    _AluPtpPeerBadVersionDisc_Type()
)
aluPtpPeerBadVersionDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerBadVersionDisc.setStatus("current")
_AluPtpPeerBadDomainDisc_Type = Counter64
_AluPtpPeerBadDomainDisc_Object = MibTableColumn
aluPtpPeerBadDomainDisc = _AluPtpPeerBadDomainDisc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 3),
    _AluPtpPeerBadDomainDisc_Type()
)
aluPtpPeerBadDomainDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerBadDomainDisc.setStatus("current")
_AluPtpPeerAlternateMasterDisc_Type = Counter64
_AluPtpPeerAlternateMasterDisc_Object = MibTableColumn
aluPtpPeerAlternateMasterDisc = _AluPtpPeerAlternateMasterDisc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 4),
    _AluPtpPeerAlternateMasterDisc_Type()
)
aluPtpPeerAlternateMasterDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerAlternateMasterDisc.setStatus("current")
_AluPtpPeerStepRemovedGreaterThan255Disc_Type = Counter64
_AluPtpPeerStepRemovedGreaterThan255Disc_Object = MibTableColumn
aluPtpPeerStepRemovedGreaterThan255Disc = _AluPtpPeerStepRemovedGreaterThan255Disc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 5),
    _AluPtpPeerStepRemovedGreaterThan255Disc_Type()
)
aluPtpPeerStepRemovedGreaterThan255Disc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerStepRemovedGreaterThan255Disc.setStatus("current")
_AluPtpPeerAnnounceMsgTx_Type = Counter64
_AluPtpPeerAnnounceMsgTx_Object = MibTableColumn
aluPtpPeerAnnounceMsgTx = _AluPtpPeerAnnounceMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 6),
    _AluPtpPeerAnnounceMsgTx_Type()
)
aluPtpPeerAnnounceMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerAnnounceMsgTx.setStatus("current")
_AluPtpPeerAnnounceMsgRx_Type = Counter64
_AluPtpPeerAnnounceMsgRx_Object = MibTableColumn
aluPtpPeerAnnounceMsgRx = _AluPtpPeerAnnounceMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 7),
    _AluPtpPeerAnnounceMsgRx_Type()
)
aluPtpPeerAnnounceMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerAnnounceMsgRx.setStatus("current")
_AluPtpPeerSyncMsgTx_Type = Counter64
_AluPtpPeerSyncMsgTx_Object = MibTableColumn
aluPtpPeerSyncMsgTx = _AluPtpPeerSyncMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 8),
    _AluPtpPeerSyncMsgTx_Type()
)
aluPtpPeerSyncMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerSyncMsgTx.setStatus("current")
_AluPtpPeerSyncMsgRx_Type = Counter64
_AluPtpPeerSyncMsgRx_Object = MibTableColumn
aluPtpPeerSyncMsgRx = _AluPtpPeerSyncMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 9),
    _AluPtpPeerSyncMsgRx_Type()
)
aluPtpPeerSyncMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerSyncMsgRx.setStatus("current")
_AluPtpPeerSignalingMsgTx_Type = Counter64
_AluPtpPeerSignalingMsgTx_Object = MibTableColumn
aluPtpPeerSignalingMsgTx = _AluPtpPeerSignalingMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 10),
    _AluPtpPeerSignalingMsgTx_Type()
)
aluPtpPeerSignalingMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerSignalingMsgTx.setStatus("current")
_AluPtpPeerSignalingMsgRx_Type = Counter64
_AluPtpPeerSignalingMsgRx_Object = MibTableColumn
aluPtpPeerSignalingMsgRx = _AluPtpPeerSignalingMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 11),
    _AluPtpPeerSignalingMsgRx_Type()
)
aluPtpPeerSignalingMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerSignalingMsgRx.setStatus("current")
_AluPtpPeerTotalUdpGeneralMsgTx_Type = Counter64
_AluPtpPeerTotalUdpGeneralMsgTx_Object = MibTableColumn
aluPtpPeerTotalUdpGeneralMsgTx = _AluPtpPeerTotalUdpGeneralMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 12),
    _AluPtpPeerTotalUdpGeneralMsgTx_Type()
)
aluPtpPeerTotalUdpGeneralMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerTotalUdpGeneralMsgTx.setStatus("current")
_AluPtpPeerTotalUdpGeneralMsgRx_Type = Counter64
_AluPtpPeerTotalUdpGeneralMsgRx_Object = MibTableColumn
aluPtpPeerTotalUdpGeneralMsgRx = _AluPtpPeerTotalUdpGeneralMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 13),
    _AluPtpPeerTotalUdpGeneralMsgRx_Type()
)
aluPtpPeerTotalUdpGeneralMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerTotalUdpGeneralMsgRx.setStatus("current")
_AluPtpPeerTotalUdpEventMsgTx_Type = Counter64
_AluPtpPeerTotalUdpEventMsgTx_Object = MibTableColumn
aluPtpPeerTotalUdpEventMsgTx = _AluPtpPeerTotalUdpEventMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 14),
    _AluPtpPeerTotalUdpEventMsgTx_Type()
)
aluPtpPeerTotalUdpEventMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerTotalUdpEventMsgTx.setStatus("current")
_AluPtpPeerTotalUdpEventMsgRx_Type = Counter64
_AluPtpPeerTotalUdpEventMsgRx_Object = MibTableColumn
aluPtpPeerTotalUdpEventMsgRx = _AluPtpPeerTotalUdpEventMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 15),
    _AluPtpPeerTotalUdpEventMsgRx_Type()
)
aluPtpPeerTotalUdpEventMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerTotalUdpEventMsgRx.setStatus("current")
_AluPtpPeerUcReqAnnoTx_Type = Counter64
_AluPtpPeerUcReqAnnoTx_Object = MibTableColumn
aluPtpPeerUcReqAnnoTx = _AluPtpPeerUcReqAnnoTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 16),
    _AluPtpPeerUcReqAnnoTx_Type()
)
aluPtpPeerUcReqAnnoTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcReqAnnoTx.setStatus("current")
_AluPtpPeerUcReqAnnoRx_Type = Counter64
_AluPtpPeerUcReqAnnoRx_Object = MibTableColumn
aluPtpPeerUcReqAnnoRx = _AluPtpPeerUcReqAnnoRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 17),
    _AluPtpPeerUcReqAnnoRx_Type()
)
aluPtpPeerUcReqAnnoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcReqAnnoRx.setStatus("current")
_AluPtpPeerUcGrantAnnoTx_Type = Counter64
_AluPtpPeerUcGrantAnnoTx_Object = MibTableColumn
aluPtpPeerUcGrantAnnoTx = _AluPtpPeerUcGrantAnnoTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 18),
    _AluPtpPeerUcGrantAnnoTx_Type()
)
aluPtpPeerUcGrantAnnoTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcGrantAnnoTx.setStatus("current")
_AluPtpPeerUcGrantAnnoRx_Type = Counter64
_AluPtpPeerUcGrantAnnoRx_Object = MibTableColumn
aluPtpPeerUcGrantAnnoRx = _AluPtpPeerUcGrantAnnoRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 19),
    _AluPtpPeerUcGrantAnnoRx_Type()
)
aluPtpPeerUcGrantAnnoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcGrantAnnoRx.setStatus("current")
_AluPtpPeerUcReqSyncTx_Type = Counter64
_AluPtpPeerUcReqSyncTx_Object = MibTableColumn
aluPtpPeerUcReqSyncTx = _AluPtpPeerUcReqSyncTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 20),
    _AluPtpPeerUcReqSyncTx_Type()
)
aluPtpPeerUcReqSyncTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcReqSyncTx.setStatus("current")
_AluPtpPeerUcReqSyncRx_Type = Counter64
_AluPtpPeerUcReqSyncRx_Object = MibTableColumn
aluPtpPeerUcReqSyncRx = _AluPtpPeerUcReqSyncRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 21),
    _AluPtpPeerUcReqSyncRx_Type()
)
aluPtpPeerUcReqSyncRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcReqSyncRx.setStatus("current")
_AluPtpPeerUcGrantSyncTx_Type = Counter64
_AluPtpPeerUcGrantSyncTx_Object = MibTableColumn
aluPtpPeerUcGrantSyncTx = _AluPtpPeerUcGrantSyncTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 22),
    _AluPtpPeerUcGrantSyncTx_Type()
)
aluPtpPeerUcGrantSyncTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcGrantSyncTx.setStatus("current")
_AluPtpPeerUcGrantSyncRx_Type = Counter64
_AluPtpPeerUcGrantSyncRx_Object = MibTableColumn
aluPtpPeerUcGrantSyncRx = _AluPtpPeerUcGrantSyncRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 23),
    _AluPtpPeerUcGrantSyncRx_Type()
)
aluPtpPeerUcGrantSyncRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcGrantSyncRx.setStatus("current")
_AluPtpPeerUcCancelAnnoTx_Type = Counter64
_AluPtpPeerUcCancelAnnoTx_Object = MibTableColumn
aluPtpPeerUcCancelAnnoTx = _AluPtpPeerUcCancelAnnoTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 24),
    _AluPtpPeerUcCancelAnnoTx_Type()
)
aluPtpPeerUcCancelAnnoTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcCancelAnnoTx.setStatus("current")
_AluPtpPeerUcCancelAnnoRx_Type = Counter64
_AluPtpPeerUcCancelAnnoRx_Object = MibTableColumn
aluPtpPeerUcCancelAnnoRx = _AluPtpPeerUcCancelAnnoRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 25),
    _AluPtpPeerUcCancelAnnoRx_Type()
)
aluPtpPeerUcCancelAnnoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcCancelAnnoRx.setStatus("current")
_AluPtpPeerUcCancelSyncTx_Type = Counter64
_AluPtpPeerUcCancelSyncTx_Object = MibTableColumn
aluPtpPeerUcCancelSyncTx = _AluPtpPeerUcCancelSyncTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 26),
    _AluPtpPeerUcCancelSyncTx_Type()
)
aluPtpPeerUcCancelSyncTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcCancelSyncTx.setStatus("current")
_AluPtpPeerUcCancelSyncRx_Type = Counter64
_AluPtpPeerUcCancelSyncRx_Object = MibTableColumn
aluPtpPeerUcCancelSyncRx = _AluPtpPeerUcCancelSyncRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 27),
    _AluPtpPeerUcCancelSyncRx_Type()
)
aluPtpPeerUcCancelSyncRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcCancelSyncRx.setStatus("current")
_AluPtpPeerUcCancelAckAnnoTx_Type = Counter64
_AluPtpPeerUcCancelAckAnnoTx_Object = MibTableColumn
aluPtpPeerUcCancelAckAnnoTx = _AluPtpPeerUcCancelAckAnnoTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 28),
    _AluPtpPeerUcCancelAckAnnoTx_Type()
)
aluPtpPeerUcCancelAckAnnoTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcCancelAckAnnoTx.setStatus("current")
_AluPtpPeerUcCancelAckAnnoRx_Type = Counter64
_AluPtpPeerUcCancelAckAnnoRx_Object = MibTableColumn
aluPtpPeerUcCancelAckAnnoRx = _AluPtpPeerUcCancelAckAnnoRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 29),
    _AluPtpPeerUcCancelAckAnnoRx_Type()
)
aluPtpPeerUcCancelAckAnnoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcCancelAckAnnoRx.setStatus("current")
_AluPtpPeerUcCancelAckSyncTx_Type = Counter64
_AluPtpPeerUcCancelAckSyncTx_Object = MibTableColumn
aluPtpPeerUcCancelAckSyncTx = _AluPtpPeerUcCancelAckSyncTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 30),
    _AluPtpPeerUcCancelAckSyncTx_Type()
)
aluPtpPeerUcCancelAckSyncTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcCancelAckSyncTx.setStatus("current")
_AluPtpPeerUcCancelAckSyncRx_Type = Counter64
_AluPtpPeerUcCancelAckSyncRx_Object = MibTableColumn
aluPtpPeerUcCancelAckSyncRx = _AluPtpPeerUcCancelAckSyncRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 31),
    _AluPtpPeerUcCancelAckSyncRx_Type()
)
aluPtpPeerUcCancelAckSyncRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcCancelAckSyncRx.setStatus("current")
_AluPtpPeerUcNegRejectsAnno_Type = Counter64
_AluPtpPeerUcNegRejectsAnno_Object = MibTableColumn
aluPtpPeerUcNegRejectsAnno = _AluPtpPeerUcNegRejectsAnno_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 32),
    _AluPtpPeerUcNegRejectsAnno_Type()
)
aluPtpPeerUcNegRejectsAnno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcNegRejectsAnno.setStatus("current")
_AluPtpPeerUcNegRejectsSync_Type = Counter64
_AluPtpPeerUcNegRejectsSync_Object = MibTableColumn
aluPtpPeerUcNegRejectsSync = _AluPtpPeerUcNegRejectsSync_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 33),
    _AluPtpPeerUcNegRejectsSync_Type()
)
aluPtpPeerUcNegRejectsSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcNegRejectsSync.setStatus("current")
_AluPtpPeerOutOfOrderSyncPktRx_Type = Counter64
_AluPtpPeerOutOfOrderSyncPktRx_Object = MibTableColumn
aluPtpPeerOutOfOrderSyncPktRx = _AluPtpPeerOutOfOrderSyncPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 34),
    _AluPtpPeerOutOfOrderSyncPktRx_Type()
)
aluPtpPeerOutOfOrderSyncPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerOutOfOrderSyncPktRx.setStatus("current")
_AluPtpPeerDuplicateMsgDisc_Type = Counter64
_AluPtpPeerDuplicateMsgDisc_Object = MibTableColumn
aluPtpPeerDuplicateMsgDisc = _AluPtpPeerDuplicateMsgDisc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 35),
    _AluPtpPeerDuplicateMsgDisc_Type()
)
aluPtpPeerDuplicateMsgDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerDuplicateMsgDisc.setStatus("current")
_AluPtpPeerUcReqAnnoTxTimeout_Type = Counter64
_AluPtpPeerUcReqAnnoTxTimeout_Object = MibTableColumn
aluPtpPeerUcReqAnnoTxTimeout = _AluPtpPeerUcReqAnnoTxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 36),
    _AluPtpPeerUcReqAnnoTxTimeout_Type()
)
aluPtpPeerUcReqAnnoTxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcReqAnnoTxTimeout.setStatus("current")
_AluPtpPeerUcReqSyncTxTimeout_Type = Counter64
_AluPtpPeerUcReqSyncTxTimeout_Object = MibTableColumn
aluPtpPeerUcReqSyncTxTimeout = _AluPtpPeerUcReqSyncTxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 37),
    _AluPtpPeerUcReqSyncTxTimeout_Type()
)
aluPtpPeerUcReqSyncTxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcReqSyncTxTimeout.setStatus("current")
_AluPtpPeerUcGrantAnnoRejected_Type = Counter64
_AluPtpPeerUcGrantAnnoRejected_Object = MibTableColumn
aluPtpPeerUcGrantAnnoRejected = _AluPtpPeerUcGrantAnnoRejected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 38),
    _AluPtpPeerUcGrantAnnoRejected_Type()
)
aluPtpPeerUcGrantAnnoRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcGrantAnnoRejected.setStatus("current")
_AluPtpPeerUcGrantSyncRejected_Type = Counter64
_AluPtpPeerUcGrantSyncRejected_Object = MibTableColumn
aluPtpPeerUcGrantSyncRejected = _AluPtpPeerUcGrantSyncRejected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 39),
    _AluPtpPeerUcGrantSyncRejected_Type()
)
aluPtpPeerUcGrantSyncRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcGrantSyncRejected.setStatus("current")
_AluPtpPeerDelayRespMsgTx_Type = Counter64
_AluPtpPeerDelayRespMsgTx_Object = MibTableColumn
aluPtpPeerDelayRespMsgTx = _AluPtpPeerDelayRespMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 40),
    _AluPtpPeerDelayRespMsgTx_Type()
)
aluPtpPeerDelayRespMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerDelayRespMsgTx.setStatus("current")
_AluPtpPeerDelayRespMsgRx_Type = Counter64
_AluPtpPeerDelayRespMsgRx_Object = MibTableColumn
aluPtpPeerDelayRespMsgRx = _AluPtpPeerDelayRespMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 41),
    _AluPtpPeerDelayRespMsgRx_Type()
)
aluPtpPeerDelayRespMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerDelayRespMsgRx.setStatus("current")
_AluPtpPeerUcReqDelayRespTx_Type = Counter64
_AluPtpPeerUcReqDelayRespTx_Object = MibTableColumn
aluPtpPeerUcReqDelayRespTx = _AluPtpPeerUcReqDelayRespTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 42),
    _AluPtpPeerUcReqDelayRespTx_Type()
)
aluPtpPeerUcReqDelayRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcReqDelayRespTx.setStatus("current")
_AluPtpPeerUcReqDelayRespRx_Type = Counter64
_AluPtpPeerUcReqDelayRespRx_Object = MibTableColumn
aluPtpPeerUcReqDelayRespRx = _AluPtpPeerUcReqDelayRespRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 43),
    _AluPtpPeerUcReqDelayRespRx_Type()
)
aluPtpPeerUcReqDelayRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcReqDelayRespRx.setStatus("current")
_AluPtpPeerUcGrantDelayRespTx_Type = Counter64
_AluPtpPeerUcGrantDelayRespTx_Object = MibTableColumn
aluPtpPeerUcGrantDelayRespTx = _AluPtpPeerUcGrantDelayRespTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 44),
    _AluPtpPeerUcGrantDelayRespTx_Type()
)
aluPtpPeerUcGrantDelayRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcGrantDelayRespTx.setStatus("current")
_AluPtpPeerUcGrantDelayRespRx_Type = Counter64
_AluPtpPeerUcGrantDelayRespRx_Object = MibTableColumn
aluPtpPeerUcGrantDelayRespRx = _AluPtpPeerUcGrantDelayRespRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 45),
    _AluPtpPeerUcGrantDelayRespRx_Type()
)
aluPtpPeerUcGrantDelayRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcGrantDelayRespRx.setStatus("current")
_AluPtpPeerUcCancelDelayRespTx_Type = Counter64
_AluPtpPeerUcCancelDelayRespTx_Object = MibTableColumn
aluPtpPeerUcCancelDelayRespTx = _AluPtpPeerUcCancelDelayRespTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 46),
    _AluPtpPeerUcCancelDelayRespTx_Type()
)
aluPtpPeerUcCancelDelayRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcCancelDelayRespTx.setStatus("current")
_AluPtpPeerUcCancelDelayRespRx_Type = Counter64
_AluPtpPeerUcCancelDelayRespRx_Object = MibTableColumn
aluPtpPeerUcCancelDelayRespRx = _AluPtpPeerUcCancelDelayRespRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 47),
    _AluPtpPeerUcCancelDelayRespRx_Type()
)
aluPtpPeerUcCancelDelayRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcCancelDelayRespRx.setStatus("current")
_AluPtpPeerUcCancelAckDelayRespTx_Type = Counter64
_AluPtpPeerUcCancelAckDelayRespTx_Object = MibTableColumn
aluPtpPeerUcCancelAckDelayRespTx = _AluPtpPeerUcCancelAckDelayRespTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 48),
    _AluPtpPeerUcCancelAckDelayRespTx_Type()
)
aluPtpPeerUcCancelAckDelayRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcCancelAckDelayRespTx.setStatus("current")
_AluPtpPeerUcCancelAckDelayRespRx_Type = Counter64
_AluPtpPeerUcCancelAckDelayRespRx_Object = MibTableColumn
aluPtpPeerUcCancelAckDelayRespRx = _AluPtpPeerUcCancelAckDelayRespRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 49),
    _AluPtpPeerUcCancelAckDelayRespRx_Type()
)
aluPtpPeerUcCancelAckDelayRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcCancelAckDelayRespRx.setStatus("current")
_AluPtpPeerUcReqDelayRespTxTimeout_Type = Counter64
_AluPtpPeerUcReqDelayRespTxTimeout_Object = MibTableColumn
aluPtpPeerUcReqDelayRespTxTimeout = _AluPtpPeerUcReqDelayRespTxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 50),
    _AluPtpPeerUcReqDelayRespTxTimeout_Type()
)
aluPtpPeerUcReqDelayRespTxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcReqDelayRespTxTimeout.setStatus("current")
_AluPtpPeerUcNegRejectsDelayResp_Type = Counter64
_AluPtpPeerUcNegRejectsDelayResp_Object = MibTableColumn
aluPtpPeerUcNegRejectsDelayResp = _AluPtpPeerUcNegRejectsDelayResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 51),
    _AluPtpPeerUcNegRejectsDelayResp_Type()
)
aluPtpPeerUcNegRejectsDelayResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcNegRejectsDelayResp.setStatus("current")
_AluPtpPeerUcGrantDelayRespRejected_Type = Counter64
_AluPtpPeerUcGrantDelayRespRejected_Object = MibTableColumn
aluPtpPeerUcGrantDelayRespRejected = _AluPtpPeerUcGrantDelayRespRejected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 52),
    _AluPtpPeerUcGrantDelayRespRejected_Type()
)
aluPtpPeerUcGrantDelayRespRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcGrantDelayRespRejected.setStatus("current")
_AluPtpPeerDelayReqMsgTx_Type = Counter64
_AluPtpPeerDelayReqMsgTx_Object = MibTableColumn
aluPtpPeerDelayReqMsgTx = _AluPtpPeerDelayReqMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 53),
    _AluPtpPeerDelayReqMsgTx_Type()
)
aluPtpPeerDelayReqMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerDelayReqMsgTx.setStatus("current")
_AluPtpPeerDelayReqMsgRx_Type = Counter64
_AluPtpPeerDelayReqMsgRx_Object = MibTableColumn
aluPtpPeerDelayReqMsgRx = _AluPtpPeerDelayReqMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 54),
    _AluPtpPeerDelayReqMsgRx_Type()
)
aluPtpPeerDelayReqMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerDelayReqMsgRx.setStatus("current")
_AluPtpPeerUcGrantDenyAnnoTx_Type = Counter64
_AluPtpPeerUcGrantDenyAnnoTx_Object = MibTableColumn
aluPtpPeerUcGrantDenyAnnoTx = _AluPtpPeerUcGrantDenyAnnoTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 55),
    _AluPtpPeerUcGrantDenyAnnoTx_Type()
)
aluPtpPeerUcGrantDenyAnnoTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcGrantDenyAnnoTx.setStatus("current")
_AluPtpPeerUcGrantDenySyncTx_Type = Counter64
_AluPtpPeerUcGrantDenySyncTx_Object = MibTableColumn
aluPtpPeerUcGrantDenySyncTx = _AluPtpPeerUcGrantDenySyncTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 56),
    _AluPtpPeerUcGrantDenySyncTx_Type()
)
aluPtpPeerUcGrantDenySyncTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcGrantDenySyncTx.setStatus("current")
_AluPtpPeerUcGrantDenyDelayRespTx_Type = Counter64
_AluPtpPeerUcGrantDenyDelayRespTx_Object = MibTableColumn
aluPtpPeerUcGrantDenyDelayRespTx = _AluPtpPeerUcGrantDenyDelayRespTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 58),
    _AluPtpPeerUcGrantDenyDelayRespTx_Type()
)
aluPtpPeerUcGrantDenyDelayRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcGrantDenyDelayRespTx.setStatus("current")
_AluPtpPeerUcReqAnnoRxTimeout_Type = Counter64
_AluPtpPeerUcReqAnnoRxTimeout_Object = MibTableColumn
aluPtpPeerUcReqAnnoRxTimeout = _AluPtpPeerUcReqAnnoRxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 59),
    _AluPtpPeerUcReqAnnoRxTimeout_Type()
)
aluPtpPeerUcReqAnnoRxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcReqAnnoRxTimeout.setStatus("current")
_AluPtpPeerUcReqSyncRxTimeout_Type = Counter64
_AluPtpPeerUcReqSyncRxTimeout_Object = MibTableColumn
aluPtpPeerUcReqSyncRxTimeout = _AluPtpPeerUcReqSyncRxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 60),
    _AluPtpPeerUcReqSyncRxTimeout_Type()
)
aluPtpPeerUcReqSyncRxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcReqSyncRxTimeout.setStatus("current")
_AluPtpPeerUcReqDelayRespRxTimeout_Type = Counter64
_AluPtpPeerUcReqDelayRespRxTimeout_Object = MibTableColumn
aluPtpPeerUcReqDelayRespRxTimeout = _AluPtpPeerUcReqDelayRespRxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 2, 1, 61),
    _AluPtpPeerUcReqDelayRespRxTimeout_Type()
)
aluPtpPeerUcReqDelayRespRxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerUcReqDelayRespRxTimeout.setStatus("current")
_AluPtpPeerRecClkStatsTable_Object = MibTable
aluPtpPeerRecClkStatsTable = _AluPtpPeerRecClkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 3)
)
if mibBuilder.loadTexts:
    aluPtpPeerRecClkStatsTable.setStatus("current")
_AluPtpPeerRecClkStatsEntry_Object = MibTableRow
aluPtpPeerRecClkStatsEntry = _AluPtpPeerRecClkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 3, 1)
)
if mibBuilder.loadTexts:
    aluPtpPeerRecClkStatsEntry.setStatus("current")
_AluPtpPeerRecLastUpdateTime_Type = TimeStamp
_AluPtpPeerRecLastUpdateTime_Object = MibTableColumn
aluPtpPeerRecLastUpdateTime = _AluPtpPeerRecLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 3, 1, 1),
    _AluPtpPeerRecLastUpdateTime_Type()
)
aluPtpPeerRecLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerRecLastUpdateTime.setStatus("current")
_AluPtpPeerTotalMinutesIn24Hour_Type = Unsigned32
_AluPtpPeerTotalMinutesIn24Hour_Object = MibTableColumn
aluPtpPeerTotalMinutesIn24Hour = _AluPtpPeerTotalMinutesIn24Hour_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 3, 1, 2),
    _AluPtpPeerTotalMinutesIn24Hour_Type()
)
aluPtpPeerTotalMinutesIn24Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerTotalMinutesIn24Hour.setStatus("current")
_AluPtpPeerCurrent24HourFreqOffsetMeanPpb_Type = Integer32
_AluPtpPeerCurrent24HourFreqOffsetMeanPpb_Object = MibTableColumn
aluPtpPeerCurrent24HourFreqOffsetMeanPpb = _AluPtpPeerCurrent24HourFreqOffsetMeanPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 3, 1, 3),
    _AluPtpPeerCurrent24HourFreqOffsetMeanPpb_Type()
)
aluPtpPeerCurrent24HourFreqOffsetMeanPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerCurrent24HourFreqOffsetMeanPpb.setStatus("current")
_AluPtpPeerCurrent24HourFreqOffsetStdDevPpb_Type = Unsigned32
_AluPtpPeerCurrent24HourFreqOffsetStdDevPpb_Object = MibTableColumn
aluPtpPeerCurrent24HourFreqOffsetStdDevPpb = _AluPtpPeerCurrent24HourFreqOffsetStdDevPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 3, 1, 4),
    _AluPtpPeerCurrent24HourFreqOffsetStdDevPpb_Type()
)
aluPtpPeerCurrent24HourFreqOffsetStdDevPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerCurrent24HourFreqOffsetStdDevPpb.setStatus("current")
_AluPtpPeerMaxShortIntvlMinutes_Type = Unsigned32
_AluPtpPeerMaxShortIntvlMinutes_Object = MibTableColumn
aluPtpPeerMaxShortIntvlMinutes = _AluPtpPeerMaxShortIntvlMinutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 3, 1, 5),
    _AluPtpPeerMaxShortIntvlMinutes_Type()
)
aluPtpPeerMaxShortIntvlMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerMaxShortIntvlMinutes.setStatus("current")
_AluPtpPeerTotalShortIntvlMinutes_Type = Unsigned32
_AluPtpPeerTotalShortIntvlMinutes_Object = MibTableColumn
aluPtpPeerTotalShortIntvlMinutes = _AluPtpPeerTotalShortIntvlMinutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 3, 1, 6),
    _AluPtpPeerTotalShortIntvlMinutes_Type()
)
aluPtpPeerTotalShortIntvlMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerTotalShortIntvlMinutes.setStatus("current")
_AluPtpPeerCurrent1MinValidData_Type = TruthValue
_AluPtpPeerCurrent1MinValidData_Object = MibTableColumn
aluPtpPeerCurrent1MinValidData = _AluPtpPeerCurrent1MinValidData_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 3, 1, 7),
    _AluPtpPeerCurrent1MinValidData_Type()
)
aluPtpPeerCurrent1MinValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerCurrent1MinValidData.setStatus("current")
_AluPtpPeerCurrent1MinPhaseErrorMeanPpb_Type = Integer32
_AluPtpPeerCurrent1MinPhaseErrorMeanPpb_Object = MibTableColumn
aluPtpPeerCurrent1MinPhaseErrorMeanPpb = _AluPtpPeerCurrent1MinPhaseErrorMeanPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 3, 1, 8),
    _AluPtpPeerCurrent1MinPhaseErrorMeanPpb_Type()
)
aluPtpPeerCurrent1MinPhaseErrorMeanPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerCurrent1MinPhaseErrorMeanPpb.setStatus("current")
_AluPtpPeerCurrent1MinPhaseErrorStdDevNs_Type = Unsigned32
_AluPtpPeerCurrent1MinPhaseErrorStdDevNs_Object = MibTableColumn
aluPtpPeerCurrent1MinPhaseErrorStdDevNs = _AluPtpPeerCurrent1MinPhaseErrorStdDevNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 3, 1, 9),
    _AluPtpPeerCurrent1MinPhaseErrorStdDevNs_Type()
)
aluPtpPeerCurrent1MinPhaseErrorStdDevNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerCurrent1MinPhaseErrorStdDevNs.setStatus("current")
_AluPtpPeerCurrent1MinPhaseErrorMeanNs_Type = Integer32
_AluPtpPeerCurrent1MinPhaseErrorMeanNs_Object = MibTableColumn
aluPtpPeerCurrent1MinPhaseErrorMeanNs = _AluPtpPeerCurrent1MinPhaseErrorMeanNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 3, 1, 10),
    _AluPtpPeerCurrent1MinPhaseErrorMeanNs_Type()
)
aluPtpPeerCurrent1MinPhaseErrorMeanNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerCurrent1MinPhaseErrorMeanNs.setStatus("current")
_AluPtpPeerCurrent1MinFreqOffsetMeanPpb_Type = Integer32
_AluPtpPeerCurrent1MinFreqOffsetMeanPpb_Object = MibTableColumn
aluPtpPeerCurrent1MinFreqOffsetMeanPpb = _AluPtpPeerCurrent1MinFreqOffsetMeanPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 3, 1, 11),
    _AluPtpPeerCurrent1MinFreqOffsetMeanPpb_Type()
)
aluPtpPeerCurrent1MinFreqOffsetMeanPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerCurrent1MinFreqOffsetMeanPpb.setStatus("current")
_AluPtpPeerCurrent1MinFreqOffsetStdDevPpb_Type = Unsigned32
_AluPtpPeerCurrent1MinFreqOffsetStdDevPpb_Object = MibTableColumn
aluPtpPeerCurrent1MinFreqOffsetStdDevPpb = _AluPtpPeerCurrent1MinFreqOffsetStdDevPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 3, 1, 12),
    _AluPtpPeerCurrent1MinFreqOffsetStdDevPpb_Type()
)
aluPtpPeerCurrent1MinFreqOffsetStdDevPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerCurrent1MinFreqOffsetStdDevPpb.setStatus("current")
_AluPtpPeerRecClkStatsShortIntvlTable_Object = MibTable
aluPtpPeerRecClkStatsShortIntvlTable = _AluPtpPeerRecClkStatsShortIntvlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 4)
)
if mibBuilder.loadTexts:
    aluPtpPeerRecClkStatsShortIntvlTable.setStatus("current")
_AluPtpPeerRecClkStatsShortIntvlEntry_Object = MibTableRow
aluPtpPeerRecClkStatsShortIntvlEntry = _AluPtpPeerRecClkStatsShortIntvlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 4, 1)
)
aluPtpPeerRecClkStatsShortIntvlEntry.setIndexNames(
    (0, "ALU-PTPV2-MIB", "aluPtpPeerIntvlClockIndex"),
    (0, "ALU-PTPV2-MIB", "aluPtpPeerIntvlPortIndex"),
    (0, "ALU-PTPV2-MIB", "aluPtpPeerIntvlIndex"),
    (0, "ALU-PTPV2-MIB", "aluPtpPeerIntvlNumber"),
)
if mibBuilder.loadTexts:
    aluPtpPeerRecClkStatsShortIntvlEntry.setStatus("current")
_AluPtpPeerIntvlClockIndex_Type = Alu1588PtpClockIndex
_AluPtpPeerIntvlClockIndex_Object = MibTableColumn
aluPtpPeerIntvlClockIndex = _AluPtpPeerIntvlClockIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 4, 1, 1),
    _AluPtpPeerIntvlClockIndex_Type()
)
aluPtpPeerIntvlClockIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluPtpPeerIntvlClockIndex.setStatus("current")
_AluPtpPeerIntvlPortIndex_Type = Alu1588PtpPortIndex
_AluPtpPeerIntvlPortIndex_Object = MibTableColumn
aluPtpPeerIntvlPortIndex = _AluPtpPeerIntvlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 4, 1, 2),
    _AluPtpPeerIntvlPortIndex_Type()
)
aluPtpPeerIntvlPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluPtpPeerIntvlPortIndex.setStatus("current")
_AluPtpPeerIntvlIndex_Type = Alu1588PtpMasterIndex
_AluPtpPeerIntvlIndex_Object = MibTableColumn
aluPtpPeerIntvlIndex = _AluPtpPeerIntvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 4, 1, 3),
    _AluPtpPeerIntvlIndex_Type()
)
aluPtpPeerIntvlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluPtpPeerIntvlIndex.setStatus("current")


class _AluPtpPeerIntvlNumber_Type(Integer32):
    """Custom type aluPtpPeerIntvlNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AluPtpPeerIntvlNumber_Type.__name__ = "Integer32"
_AluPtpPeerIntvlNumber_Object = MibTableColumn
aluPtpPeerIntvlNumber = _AluPtpPeerIntvlNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 4, 1, 4),
    _AluPtpPeerIntvlNumber_Type()
)
aluPtpPeerIntvlNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluPtpPeerIntvlNumber.setStatus("current")
_AluPtpPeerIntvlValidData_Type = TruthValue
_AluPtpPeerIntvlValidData_Object = MibTableColumn
aluPtpPeerIntvlValidData = _AluPtpPeerIntvlValidData_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 4, 1, 5),
    _AluPtpPeerIntvlValidData_Type()
)
aluPtpPeerIntvlValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerIntvlValidData.setStatus("current")
_AluPtpPeerIntvlUpdateTime_Type = TimeStamp
_AluPtpPeerIntvlUpdateTime_Object = MibTableColumn
aluPtpPeerIntvlUpdateTime = _AluPtpPeerIntvlUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 4, 1, 6),
    _AluPtpPeerIntvlUpdateTime_Type()
)
aluPtpPeerIntvlUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerIntvlUpdateTime.setStatus("current")
_AluPtpPeerIntvlPhaseErrorMeanPpb_Type = Integer32
_AluPtpPeerIntvlPhaseErrorMeanPpb_Object = MibTableColumn
aluPtpPeerIntvlPhaseErrorMeanPpb = _AluPtpPeerIntvlPhaseErrorMeanPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 4, 1, 7),
    _AluPtpPeerIntvlPhaseErrorMeanPpb_Type()
)
aluPtpPeerIntvlPhaseErrorMeanPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerIntvlPhaseErrorMeanPpb.setStatus("current")
_AluPtpPeerIntvlPhaseErrorStdDevNs_Type = Unsigned32
_AluPtpPeerIntvlPhaseErrorStdDevNs_Object = MibTableColumn
aluPtpPeerIntvlPhaseErrorStdDevNs = _AluPtpPeerIntvlPhaseErrorStdDevNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 4, 1, 8),
    _AluPtpPeerIntvlPhaseErrorStdDevNs_Type()
)
aluPtpPeerIntvlPhaseErrorStdDevNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerIntvlPhaseErrorStdDevNs.setStatus("current")
_AluPtpPeerIntvlPhaseErrorMeanNs_Type = Integer32
_AluPtpPeerIntvlPhaseErrorMeanNs_Object = MibTableColumn
aluPtpPeerIntvlPhaseErrorMeanNs = _AluPtpPeerIntvlPhaseErrorMeanNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 3, 4, 1, 9),
    _AluPtpPeerIntvlPhaseErrorMeanNs_Type()
)
aluPtpPeerIntvlPhaseErrorMeanNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPtpPeerIntvlPhaseErrorMeanNs.setStatus("current")
_AluPtpNotificationObjects_ObjectIdentity = ObjectIdentity
aluPtpNotificationObjects = _AluPtpNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 12, 4)
)
_AluPtpNotifyPrefix_ObjectIdentity = ObjectIdentity
aluPtpNotifyPrefix = _AluPtpNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 8)
)
_AluPtpNotification_ObjectIdentity = ObjectIdentity
aluPtpNotification = _AluPtpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 8, 0)
)
_AluPtpClockNotifyIndex_Type = Alu1588PtpClockIndex
_AluPtpClockNotifyIndex_Object = MibScalar
aluPtpClockNotifyIndex = _AluPtpClockNotifyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 8, 0, 1),
    _AluPtpClockNotifyIndex_Type()
)
aluPtpClockNotifyIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluPtpClockNotifyIndex.setStatus("current")
_AluPtpPortNotifyIndex_Type = Alu1588PtpClockIndex
_AluPtpPortNotifyIndex_Object = MibScalar
aluPtpPortNotifyIndex = _AluPtpPortNotifyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 8, 0, 2),
    _AluPtpPortNotifyIndex_Type()
)
aluPtpPortNotifyIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluPtpPortNotifyIndex.setStatus("current")
_AluPtpPeerNotifyIndex_Type = Alu1588PtpClockIndex
_AluPtpPeerNotifyIndex_Object = MibScalar
aluPtpPeerNotifyIndex = _AluPtpPeerNotifyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 8, 0, 3),
    _AluPtpPeerNotifyIndex_Type()
)
aluPtpPeerNotifyIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluPtpPeerNotifyIndex.setStatus("current")
aluPtpClockEntry.registerAugmentions(
    ("ALU-PTPV2-MIB",
     "aluPtpClockDefaultDSEntry")
)
aluPtpClockDefaultDSEntry.setIndexNames(*aluPtpClockEntry.getIndexNames())
aluPtpClockEntry.registerAugmentions(
    ("ALU-PTPV2-MIB",
     "aluPtpClockCurrentDSEntry")
)
aluPtpClockCurrentDSEntry.setIndexNames(*aluPtpClockEntry.getIndexNames())
aluPtpClockEntry.registerAugmentions(
    ("ALU-PTPV2-MIB",
     "aluPtpClockParentDSEntry")
)
aluPtpClockParentDSEntry.setIndexNames(*aluPtpClockEntry.getIndexNames())
aluPtpClockEntry.registerAugmentions(
    ("ALU-PTPV2-MIB",
     "aluPtpClockTimePropertyDSEntry")
)
aluPtpClockTimePropertyDSEntry.setIndexNames(*aluPtpClockEntry.getIndexNames())
aluPtpPortEntry.registerAugmentions(
    ("ALU-PTPV2-MIB",
     "aluPtpPortDSEntry")
)
aluPtpPortDSEntry.setIndexNames(*aluPtpPortEntry.getIndexNames())
aluPtpUcMasterEntry.registerAugmentions(
    ("ALU-PTPV2-MIB",
     "aluPtpPeerPacketStatsEntry")
)
aluPtpPeerPacketStatsEntry.setIndexNames(*aluPtpUcMasterEntry.getIndexNames())
aluPtpUcMasterEntry.registerAugmentions(
    ("ALU-PTPV2-MIB",
     "aluPtpPeerRecClkStatsEntry")
)
aluPtpPeerRecClkStatsEntry.setIndexNames(*aluPtpUcMasterEntry.getIndexNames())

# Managed Objects groups

aluPtpClockV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 12, 1, 2, 1)
)
aluPtpClockV4v0Group.setObjects(
      *(("ALU-PTPV2-MIB", "aluPtpClockMaxNumber"),
        ("ALU-PTPV2-MIB", "aluPtpClockRowStatus"),
        ("ALU-PTPV2-MIB", "aluPtpClockIpInterface"),
        ("ALU-PTPV2-MIB", "aluPtpClockHw"),
        ("ALU-PTPV2-MIB", "aluPtpClockProfile"),
        ("ALU-PTPV2-MIB", "aluPtpClockAdminState"),
        ("ALU-PTPV2-MIB", "aluPtpClockDynamicPeers"),
        ("ALU-PTPV2-MIB", "aluPtpClockId"),
        ("ALU-PTPV2-MIB", "aluPtpClockDomain"),
        ("ALU-PTPV2-MIB", "aluPtpClockTwoStepFlag"),
        ("ALU-PTPV2-MIB", "aluPtpClockType"),
        ("ALU-PTPV2-MIB", "aluPtpClockNumberPorts"),
        ("ALU-PTPV2-MIB", "aluPtpClockClass"),
        ("ALU-PTPV2-MIB", "aluPtpClockAccuracy"),
        ("ALU-PTPV2-MIB", "aluPtpClockVariance"),
        ("ALU-PTPV2-MIB", "aluPtpClockPriority1"),
        ("ALU-PTPV2-MIB", "aluPtpClockPriority2"),
        ("ALU-PTPV2-MIB", "aluPtpClockSlaveOnly"),
        ("ALU-PTPV2-MIB", "aluPtpClockStepsRemoved"),
        ("ALU-PTPV2-MIB", "aluPtpClockParentId"),
        ("ALU-PTPV2-MIB", "aluPtpClockParentPortNum"),
        ("ALU-PTPV2-MIB", "aluPtpClockParentStats"),
        ("ALU-PTPV2-MIB", "aluPtpClockParentVariance"),
        ("ALU-PTPV2-MIB", "aluPtpClockGMClockId"),
        ("ALU-PTPV2-MIB", "aluPtpClockGMClass"),
        ("ALU-PTPV2-MIB", "aluPtpClockGMAccuracy"),
        ("ALU-PTPV2-MIB", "aluPtpClockGMVariance"),
        ("ALU-PTPV2-MIB", "aluPtpClockGMPriority1"),
        ("ALU-PTPV2-MIB", "aluPtpClockGMPriority2"),
        ("ALU-PTPV2-MIB", "aluPtpClockForwardWeight"),
        ("ALU-PTPV2-MIB", "aluPtpClockRecoveryState"))
)
if mibBuilder.loadTexts:
    aluPtpClockV4v0Group.setStatus("current")

aluPtpPortV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 12, 1, 2, 2)
)
aluPtpPortV4v0Group.setObjects(
      *(("ALU-PTPV2-MIB", "aluPtpPortAdminState"),
        ("ALU-PTPV2-MIB", "aluPtpPortUcNegotiate"),
        ("ALU-PTPV2-MIB", "aluPtpPortNumPeers"),
        ("ALU-PTPV2-MIB", "aluPtpPortDSPortNum"),
        ("ALU-PTPV2-MIB", "aluPtpPortDSAnnoRxTimeout"),
        ("ALU-PTPV2-MIB", "aluPtpPortDSLogAnnoInterval"),
        ("ALU-PTPV2-MIB", "aluPtpPortDSLogSyncInterval"),
        ("ALU-PTPV2-MIB", "aluPtpPortDSPortState"),
        ("ALU-PTPV2-MIB", "aluPtpPortDSDelayMechanism"),
        ("ALU-PTPV2-MIB", "aluPtpPortDSVersionNumber"))
)
if mibBuilder.loadTexts:
    aluPtpPortV4v0Group.setStatus("current")

aluPtpPeerV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 12, 1, 2, 3)
)
aluPtpPeerV4v0Group.setObjects(
      *(("ALU-PTPV2-MIB", "aluPtpPeerIpAddrType"),
        ("ALU-PTPV2-MIB", "aluPtpPeerIpAddr"),
        ("ALU-PTPV2-MIB", "aluPtpPeerLastChanged"),
        ("ALU-PTPV2-MIB", "aluPtpPeerDescription"),
        ("ALU-PTPV2-MIB", "aluPtpPeerDiscovered"))
)
if mibBuilder.loadTexts:
    aluPtpPeerV4v0Group.setStatus("current")

aluPtpPeerStatsV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 12, 1, 2, 4)
)
aluPtpPeerStatsV4v0Group.setObjects(
      *(("ALU-PTPV2-MIB", "aluPtpPeerBadVersionDisc"),
        ("ALU-PTPV2-MIB", "aluPtpPeerBadDomainDisc"),
        ("ALU-PTPV2-MIB", "aluPtpPeerAlternateMasterDisc"),
        ("ALU-PTPV2-MIB", "aluPtpPeerDuplicateMsgDisc"),
        ("ALU-PTPV2-MIB", "aluPtpPeerStepRemovedGreaterThan255Disc"),
        ("ALU-PTPV2-MIB", "aluPtpPeerAnnounceMsgTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerAnnounceMsgRx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerSyncMsgTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerSyncMsgRx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerSignalingMsgTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerSignalingMsgRx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerTotalUdpGeneralMsgTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerTotalUdpGeneralMsgRx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerTotalUdpEventMsgTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerTotalUdpEventMsgRx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcReqAnnoTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcReqAnnoRx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcGrantAnnoTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcGrantAnnoRx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcReqSyncTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcReqSyncRx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcGrantSyncTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcGrantSyncRx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcCancelAnnoTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcCancelAnnoRx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcCancelSyncTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcCancelSyncRx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcCancelAckAnnoTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcCancelAckAnnoRx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcCancelAckSyncTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcCancelAckSyncRx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcNegRejectsAnno"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcNegRejectsSync"),
        ("ALU-PTPV2-MIB", "aluPtpPeerOutOfOrderSyncPktRx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerRecLastUpdateTime"),
        ("ALU-PTPV2-MIB", "aluPtpPeerTotalMinutesIn24Hour"),
        ("ALU-PTPV2-MIB", "aluPtpPeerCurrent24HourFreqOffsetMeanPpb"),
        ("ALU-PTPV2-MIB", "aluPtpPeerCurrent24HourFreqOffsetStdDevPpb"),
        ("ALU-PTPV2-MIB", "aluPtpPeerMaxShortIntvlMinutes"),
        ("ALU-PTPV2-MIB", "aluPtpPeerTotalShortIntvlMinutes"),
        ("ALU-PTPV2-MIB", "aluPtpPeerCurrent1MinValidData"),
        ("ALU-PTPV2-MIB", "aluPtpPeerCurrent1MinPhaseErrorMeanPpb"),
        ("ALU-PTPV2-MIB", "aluPtpPeerCurrent1MinPhaseErrorStdDevNs"),
        ("ALU-PTPV2-MIB", "aluPtpPeerCurrent1MinPhaseErrorMeanNs"),
        ("ALU-PTPV2-MIB", "aluPtpPeerCurrent1MinFreqOffsetMeanPpb"),
        ("ALU-PTPV2-MIB", "aluPtpPeerCurrent1MinFreqOffsetStdDevPpb"),
        ("ALU-PTPV2-MIB", "aluPtpPeerIntvlValidData"),
        ("ALU-PTPV2-MIB", "aluPtpPeerIntvlUpdateTime"),
        ("ALU-PTPV2-MIB", "aluPtpPeerIntvlPhaseErrorMeanPpb"),
        ("ALU-PTPV2-MIB", "aluPtpPeerIntvlPhaseErrorStdDevNs"),
        ("ALU-PTPV2-MIB", "aluPtpPeerIntvlPhaseErrorMeanNs"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcReqAnnoTxTimeout"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcReqSyncTxTimeout"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcGrantAnnoRejected"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcGrantSyncRejected"),
        ("ALU-PTPV2-MIB", "aluPtpPeerDelayRespMsgTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerDelayRespMsgRx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcReqDelayRespTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcReqDelayRespRx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcGrantDelayRespTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcGrantDelayRespRx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcCancelDelayRespTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcCancelDelayRespRx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcCancelAckDelayRespTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcCancelAckDelayRespRx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcReqDelayRespTxTimeout"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcNegRejectsDelayResp"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcGrantDelayRespRejected"),
        ("ALU-PTPV2-MIB", "aluPtpPeerDelayReqMsgTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerDelayReqMsgRx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerPacketLastUpdateTime"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcGrantDenyAnnoTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcGrantDenySyncTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcGrantDenyDelayRespTx"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcReqAnnoRxTimeout"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcReqSyncRxTimeout"),
        ("ALU-PTPV2-MIB", "aluPtpPeerUcReqDelayRespRxTimeout"))
)
if mibBuilder.loadTexts:
    aluPtpPeerStatsV4v0Group.setStatus("current")

aluPtpNotifyObjsV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 12, 1, 2, 5)
)
aluPtpNotifyObjsV4v0Group.setObjects(
      *(("ALU-PTPV2-MIB", "aluPtpClockNotifyIndex"),
        ("ALU-PTPV2-MIB", "aluPtpPortNotifyIndex"),
        ("ALU-PTPV2-MIB", "aluPtpPeerNotifyIndex"))
)
if mibBuilder.loadTexts:
    aluPtpNotifyObjsV4v0Group.setStatus("current")

aluPtpClockV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 12, 1, 2, 7)
)
aluPtpClockV5v0Group.setObjects(
      *(("ALU-PTPV2-MIB", "aluPtpClockTimeRefPriority"),
        ("ALU-PTPV2-MIB", "aluPtpClockCurUtcOffset"),
        ("ALU-PTPV2-MIB", "aluPtpClockCurUtcOffsetValid"),
        ("ALU-PTPV2-MIB", "aluPtpClockLeap59"),
        ("ALU-PTPV2-MIB", "aluPtpClockLeap61"),
        ("ALU-PTPV2-MIB", "aluPtpClockTimeTraceable"),
        ("ALU-PTPV2-MIB", "aluPtpClockFreqTraceable"),
        ("ALU-PTPV2-MIB", "aluPtpClockTimeSource"),
        ("ALU-PTPV2-MIB", "aluPtpClockAdminFreqSource"),
        ("ALU-PTPV2-MIB", "aluPtpClockOperFreqSource"))
)
if mibBuilder.loadTexts:
    aluPtpClockV5v0Group.setStatus("current")


# Notification objects

aluPtpMasterChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 8, 0, 4)
)
aluPtpMasterChange.setObjects(
      *(("ALU-PTPV2-MIB", "aluPtpPeerIpAddrType"),
        ("ALU-PTPV2-MIB", "aluPtpPeerIpAddr"),
        ("ALU-PTPV2-MIB", "aluPtpClockNotifyIndex"),
        ("ALU-PTPV2-MIB", "aluPtpPortNotifyIndex"),
        ("ALU-PTPV2-MIB", "aluPtpPeerNotifyIndex"))
)
if mibBuilder.loadTexts:
    aluPtpMasterChange.setStatus(
        "current"
    )

aluPtpClockNoMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 8, 0, 5)
)
aluPtpClockNoMaster.setObjects(
    ("ALU-PTPV2-MIB", "aluPtpClockNotifyIndex")
)
if mibBuilder.loadTexts:
    aluPtpClockNoMaster.setStatus(
        "current"
    )

aluPtpPortStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 8, 0, 6)
)
aluPtpPortStateChange.setObjects(
      *(("ALU-PTPV2-MIB", "aluPtpPortDSPortState"),
        ("ALU-PTPV2-MIB", "aluPtpClockNotifyIndex"),
        ("ALU-PTPV2-MIB", "aluPtpPortNotifyIndex"))
)
if mibBuilder.loadTexts:
    aluPtpPortStateChange.setStatus(
        "current"
    )

aluPtpClockRecovClkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 8, 0, 7)
)
aluPtpClockRecovClkChange.setObjects(
      *(("ALU-PTPV2-MIB", "aluPtpClockRecoveryState"),
        ("ALU-PTPV2-MIB", "aluPtpClockNotifyIndex"))
)
if mibBuilder.loadTexts:
    aluPtpClockRecovClkChange.setStatus(
        "current"
    )

aluPtpPeerDiscoveryChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 8, 0, 8)
)
aluPtpPeerDiscoveryChange.setObjects(
      *(("ALU-PTPV2-MIB", "aluPtpPeerDiscovered"),
        ("ALU-PTPV2-MIB", "aluPtpClockNotifyIndex"),
        ("ALU-PTPV2-MIB", "aluPtpPortNotifyIndex"),
        ("ALU-PTPV2-MIB", "aluPtpPeerNotifyIndex"))
)
if mibBuilder.loadTexts:
    aluPtpPeerDiscoveryChange.setStatus(
        "current"
    )


# Notifications groups

aluPtpNotificationV4v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 12, 1, 2, 6)
)
aluPtpNotificationV4v0Group.setObjects(
      *(("ALU-PTPV2-MIB", "aluPtpMasterChange"),
        ("ALU-PTPV2-MIB", "aluPtpClockNoMaster"),
        ("ALU-PTPV2-MIB", "aluPtpPortStateChange"),
        ("ALU-PTPV2-MIB", "aluPtpClockRecovClkChange"),
        ("ALU-PTPV2-MIB", "aluPtpPeerDiscoveryChange"))
)
if mibBuilder.loadTexts:
    aluPtpNotificationV4v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aluPtpComp7705V4v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 12, 1, 1, 1, 1)
)
aluPtpComp7705V4v0.setObjects(
      *(("ALU-PTPV2-MIB", "aluPtpClockV4v0Group"),
        ("ALU-PTPV2-MIB", "aluPtpPortV4v0Group"),
        ("ALU-PTPV2-MIB", "aluPtpPeerV4v0Group"),
        ("ALU-PTPV2-MIB", "aluPtpNotificationV4v0Group"))
)
if mibBuilder.loadTexts:
    aluPtpComp7705V4v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-PTPV2-MIB",
    **{"Alu1588PtpPortIndex": Alu1588PtpPortIndex,
       "Alu1588PtpMasterIndex": Alu1588PtpMasterIndex,
       "Alu1588PtpProfile": Alu1588PtpProfile,
       "Alu1588PtpClockStepType": Alu1588PtpClockStepType,
       "Alu1588PtpClockType": Alu1588PtpClockType,
       "Alu1588PtpLogInterval": Alu1588PtpLogInterval,
       "Alu1588PtpClockRecoveryState": Alu1588PtpClockRecoveryState,
       "AluPtpTimeSource": AluPtpTimeSource,
       "Alu1588PtpFreqSource": Alu1588PtpFreqSource,
       "aluPtpV2Module": aluPtpV2Module,
       "aluPtpMIBConformance": aluPtpMIBConformance,
       "aluPtpConformance": aluPtpConformance,
       "aluPtpCompliances": aluPtpCompliances,
       "aluPtpComp7705": aluPtpComp7705,
       "aluPtpComp7705V4v0": aluPtpComp7705V4v0,
       "aluPtpGroups": aluPtpGroups,
       "aluPtpClockV4v0Group": aluPtpClockV4v0Group,
       "aluPtpPortV4v0Group": aluPtpPortV4v0Group,
       "aluPtpPeerV4v0Group": aluPtpPeerV4v0Group,
       "aluPtpPeerStatsV4v0Group": aluPtpPeerStatsV4v0Group,
       "aluPtpNotifyObjsV4v0Group": aluPtpNotifyObjsV4v0Group,
       "aluPtpNotificationV4v0Group": aluPtpNotificationV4v0Group,
       "aluPtpClockV5v0Group": aluPtpClockV5v0Group,
       "aluPtpObjs": aluPtpObjs,
       "aluPtpClock": aluPtpClock,
       "aluPtpClockMaxNumber": aluPtpClockMaxNumber,
       "aluPtpClockTable": aluPtpClockTable,
       "aluPtpClockEntry": aluPtpClockEntry,
       "aluPtpClockIndex": aluPtpClockIndex,
       "aluPtpClockRowStatus": aluPtpClockRowStatus,
       "aluPtpClockIpInterface": aluPtpClockIpInterface,
       "aluPtpClockHw": aluPtpClockHw,
       "aluPtpClockProfile": aluPtpClockProfile,
       "aluPtpClockAdminState": aluPtpClockAdminState,
       "aluPtpClockDynamicPeers": aluPtpClockDynamicPeers,
       "aluPtpClockForwardWeight": aluPtpClockForwardWeight,
       "aluPtpClockRecoveryState": aluPtpClockRecoveryState,
       "aluPtpClockTimeRefPriority": aluPtpClockTimeRefPriority,
       "aluPtpClockAdminFreqSource": aluPtpClockAdminFreqSource,
       "aluPtpClockOperFreqSource": aluPtpClockOperFreqSource,
       "aluPtpClockDefaultDSTable": aluPtpClockDefaultDSTable,
       "aluPtpClockDefaultDSEntry": aluPtpClockDefaultDSEntry,
       "aluPtpClockId": aluPtpClockId,
       "aluPtpClockType": aluPtpClockType,
       "aluPtpClockSlaveOnly": aluPtpClockSlaveOnly,
       "aluPtpClockDomain": aluPtpClockDomain,
       "aluPtpClockNumberPorts": aluPtpClockNumberPorts,
       "aluPtpClockClass": aluPtpClockClass,
       "aluPtpClockAccuracy": aluPtpClockAccuracy,
       "aluPtpClockVariance": aluPtpClockVariance,
       "aluPtpClockPriority1": aluPtpClockPriority1,
       "aluPtpClockPriority2": aluPtpClockPriority2,
       "aluPtpClockTwoStepFlag": aluPtpClockTwoStepFlag,
       "aluPtpClockCurrentDSTable": aluPtpClockCurrentDSTable,
       "aluPtpClockCurrentDSEntry": aluPtpClockCurrentDSEntry,
       "aluPtpClockStepsRemoved": aluPtpClockStepsRemoved,
       "aluPtpClockParentDSTable": aluPtpClockParentDSTable,
       "aluPtpClockParentDSEntry": aluPtpClockParentDSEntry,
       "aluPtpClockParentId": aluPtpClockParentId,
       "aluPtpClockParentPortNum": aluPtpClockParentPortNum,
       "aluPtpClockParentStats": aluPtpClockParentStats,
       "aluPtpClockParentVariance": aluPtpClockParentVariance,
       "aluPtpClockGMClockId": aluPtpClockGMClockId,
       "aluPtpClockGMClass": aluPtpClockGMClass,
       "aluPtpClockGMAccuracy": aluPtpClockGMAccuracy,
       "aluPtpClockGMVariance": aluPtpClockGMVariance,
       "aluPtpClockGMPriority1": aluPtpClockGMPriority1,
       "aluPtpClockGMPriority2": aluPtpClockGMPriority2,
       "aluPtpClockTimePropertyDSTable": aluPtpClockTimePropertyDSTable,
       "aluPtpClockTimePropertyDSEntry": aluPtpClockTimePropertyDSEntry,
       "aluPtpClockCurUtcOffset": aluPtpClockCurUtcOffset,
       "aluPtpClockCurUtcOffsetValid": aluPtpClockCurUtcOffsetValid,
       "aluPtpClockLeap59": aluPtpClockLeap59,
       "aluPtpClockLeap61": aluPtpClockLeap61,
       "aluPtpClockTimeTraceable": aluPtpClockTimeTraceable,
       "aluPtpClockFreqTraceable": aluPtpClockFreqTraceable,
       "aluPtpClockPtpTimescale": aluPtpClockPtpTimescale,
       "aluPtpClockTimeSource": aluPtpClockTimeSource,
       "aluPtpPort": aluPtpPort,
       "aluPtpPortTable": aluPtpPortTable,
       "aluPtpPortEntry": aluPtpPortEntry,
       "aluPtpPortClockIndex": aluPtpPortClockIndex,
       "aluPtpPortIndex": aluPtpPortIndex,
       "aluPtpPortAdminState": aluPtpPortAdminState,
       "aluPtpPortUcNegotiate": aluPtpPortUcNegotiate,
       "aluPtpPortNumPeers": aluPtpPortNumPeers,
       "aluPtpPortDSTable": aluPtpPortDSTable,
       "aluPtpPortDSEntry": aluPtpPortDSEntry,
       "aluPtpPortDSPortNum": aluPtpPortDSPortNum,
       "aluPtpPortDSAnnoRxTimeout": aluPtpPortDSAnnoRxTimeout,
       "aluPtpPortDSLogAnnoInterval": aluPtpPortDSLogAnnoInterval,
       "aluPtpPortDSLogSyncInterval": aluPtpPortDSLogSyncInterval,
       "aluPtpPortDSPortState": aluPtpPortDSPortState,
       "aluPtpPortDSDelayMechanism": aluPtpPortDSDelayMechanism,
       "aluPtpPortDSVersionNumber": aluPtpPortDSVersionNumber,
       "aluPtpPeer": aluPtpPeer,
       "aluPtpUcMasterTable": aluPtpUcMasterTable,
       "aluPtpUcMasterEntry": aluPtpUcMasterEntry,
       "aluPtpPeerClockIndex": aluPtpPeerClockIndex,
       "aluPtpPeerPortIndex": aluPtpPeerPortIndex,
       "aluPtpPeerIndex": aluPtpPeerIndex,
       "aluPtpPeerIpAddrType": aluPtpPeerIpAddrType,
       "aluPtpPeerIpAddr": aluPtpPeerIpAddr,
       "aluPtpPeerLastChanged": aluPtpPeerLastChanged,
       "aluPtpPeerDescription": aluPtpPeerDescription,
       "aluPtpPeerDiscovered": aluPtpPeerDiscovered,
       "aluPtpPeerPacketStatsTable": aluPtpPeerPacketStatsTable,
       "aluPtpPeerPacketStatsEntry": aluPtpPeerPacketStatsEntry,
       "aluPtpPeerPacketLastUpdateTime": aluPtpPeerPacketLastUpdateTime,
       "aluPtpPeerBadVersionDisc": aluPtpPeerBadVersionDisc,
       "aluPtpPeerBadDomainDisc": aluPtpPeerBadDomainDisc,
       "aluPtpPeerAlternateMasterDisc": aluPtpPeerAlternateMasterDisc,
       "aluPtpPeerStepRemovedGreaterThan255Disc": aluPtpPeerStepRemovedGreaterThan255Disc,
       "aluPtpPeerAnnounceMsgTx": aluPtpPeerAnnounceMsgTx,
       "aluPtpPeerAnnounceMsgRx": aluPtpPeerAnnounceMsgRx,
       "aluPtpPeerSyncMsgTx": aluPtpPeerSyncMsgTx,
       "aluPtpPeerSyncMsgRx": aluPtpPeerSyncMsgRx,
       "aluPtpPeerSignalingMsgTx": aluPtpPeerSignalingMsgTx,
       "aluPtpPeerSignalingMsgRx": aluPtpPeerSignalingMsgRx,
       "aluPtpPeerTotalUdpGeneralMsgTx": aluPtpPeerTotalUdpGeneralMsgTx,
       "aluPtpPeerTotalUdpGeneralMsgRx": aluPtpPeerTotalUdpGeneralMsgRx,
       "aluPtpPeerTotalUdpEventMsgTx": aluPtpPeerTotalUdpEventMsgTx,
       "aluPtpPeerTotalUdpEventMsgRx": aluPtpPeerTotalUdpEventMsgRx,
       "aluPtpPeerUcReqAnnoTx": aluPtpPeerUcReqAnnoTx,
       "aluPtpPeerUcReqAnnoRx": aluPtpPeerUcReqAnnoRx,
       "aluPtpPeerUcGrantAnnoTx": aluPtpPeerUcGrantAnnoTx,
       "aluPtpPeerUcGrantAnnoRx": aluPtpPeerUcGrantAnnoRx,
       "aluPtpPeerUcReqSyncTx": aluPtpPeerUcReqSyncTx,
       "aluPtpPeerUcReqSyncRx": aluPtpPeerUcReqSyncRx,
       "aluPtpPeerUcGrantSyncTx": aluPtpPeerUcGrantSyncTx,
       "aluPtpPeerUcGrantSyncRx": aluPtpPeerUcGrantSyncRx,
       "aluPtpPeerUcCancelAnnoTx": aluPtpPeerUcCancelAnnoTx,
       "aluPtpPeerUcCancelAnnoRx": aluPtpPeerUcCancelAnnoRx,
       "aluPtpPeerUcCancelSyncTx": aluPtpPeerUcCancelSyncTx,
       "aluPtpPeerUcCancelSyncRx": aluPtpPeerUcCancelSyncRx,
       "aluPtpPeerUcCancelAckAnnoTx": aluPtpPeerUcCancelAckAnnoTx,
       "aluPtpPeerUcCancelAckAnnoRx": aluPtpPeerUcCancelAckAnnoRx,
       "aluPtpPeerUcCancelAckSyncTx": aluPtpPeerUcCancelAckSyncTx,
       "aluPtpPeerUcCancelAckSyncRx": aluPtpPeerUcCancelAckSyncRx,
       "aluPtpPeerUcNegRejectsAnno": aluPtpPeerUcNegRejectsAnno,
       "aluPtpPeerUcNegRejectsSync": aluPtpPeerUcNegRejectsSync,
       "aluPtpPeerOutOfOrderSyncPktRx": aluPtpPeerOutOfOrderSyncPktRx,
       "aluPtpPeerDuplicateMsgDisc": aluPtpPeerDuplicateMsgDisc,
       "aluPtpPeerUcReqAnnoTxTimeout": aluPtpPeerUcReqAnnoTxTimeout,
       "aluPtpPeerUcReqSyncTxTimeout": aluPtpPeerUcReqSyncTxTimeout,
       "aluPtpPeerUcGrantAnnoRejected": aluPtpPeerUcGrantAnnoRejected,
       "aluPtpPeerUcGrantSyncRejected": aluPtpPeerUcGrantSyncRejected,
       "aluPtpPeerDelayRespMsgTx": aluPtpPeerDelayRespMsgTx,
       "aluPtpPeerDelayRespMsgRx": aluPtpPeerDelayRespMsgRx,
       "aluPtpPeerUcReqDelayRespTx": aluPtpPeerUcReqDelayRespTx,
       "aluPtpPeerUcReqDelayRespRx": aluPtpPeerUcReqDelayRespRx,
       "aluPtpPeerUcGrantDelayRespTx": aluPtpPeerUcGrantDelayRespTx,
       "aluPtpPeerUcGrantDelayRespRx": aluPtpPeerUcGrantDelayRespRx,
       "aluPtpPeerUcCancelDelayRespTx": aluPtpPeerUcCancelDelayRespTx,
       "aluPtpPeerUcCancelDelayRespRx": aluPtpPeerUcCancelDelayRespRx,
       "aluPtpPeerUcCancelAckDelayRespTx": aluPtpPeerUcCancelAckDelayRespTx,
       "aluPtpPeerUcCancelAckDelayRespRx": aluPtpPeerUcCancelAckDelayRespRx,
       "aluPtpPeerUcReqDelayRespTxTimeout": aluPtpPeerUcReqDelayRespTxTimeout,
       "aluPtpPeerUcNegRejectsDelayResp": aluPtpPeerUcNegRejectsDelayResp,
       "aluPtpPeerUcGrantDelayRespRejected": aluPtpPeerUcGrantDelayRespRejected,
       "aluPtpPeerDelayReqMsgTx": aluPtpPeerDelayReqMsgTx,
       "aluPtpPeerDelayReqMsgRx": aluPtpPeerDelayReqMsgRx,
       "aluPtpPeerUcGrantDenyAnnoTx": aluPtpPeerUcGrantDenyAnnoTx,
       "aluPtpPeerUcGrantDenySyncTx": aluPtpPeerUcGrantDenySyncTx,
       "aluPtpPeerUcGrantDenyDelayRespTx": aluPtpPeerUcGrantDenyDelayRespTx,
       "aluPtpPeerUcReqAnnoRxTimeout": aluPtpPeerUcReqAnnoRxTimeout,
       "aluPtpPeerUcReqSyncRxTimeout": aluPtpPeerUcReqSyncRxTimeout,
       "aluPtpPeerUcReqDelayRespRxTimeout": aluPtpPeerUcReqDelayRespRxTimeout,
       "aluPtpPeerRecClkStatsTable": aluPtpPeerRecClkStatsTable,
       "aluPtpPeerRecClkStatsEntry": aluPtpPeerRecClkStatsEntry,
       "aluPtpPeerRecLastUpdateTime": aluPtpPeerRecLastUpdateTime,
       "aluPtpPeerTotalMinutesIn24Hour": aluPtpPeerTotalMinutesIn24Hour,
       "aluPtpPeerCurrent24HourFreqOffsetMeanPpb": aluPtpPeerCurrent24HourFreqOffsetMeanPpb,
       "aluPtpPeerCurrent24HourFreqOffsetStdDevPpb": aluPtpPeerCurrent24HourFreqOffsetStdDevPpb,
       "aluPtpPeerMaxShortIntvlMinutes": aluPtpPeerMaxShortIntvlMinutes,
       "aluPtpPeerTotalShortIntvlMinutes": aluPtpPeerTotalShortIntvlMinutes,
       "aluPtpPeerCurrent1MinValidData": aluPtpPeerCurrent1MinValidData,
       "aluPtpPeerCurrent1MinPhaseErrorMeanPpb": aluPtpPeerCurrent1MinPhaseErrorMeanPpb,
       "aluPtpPeerCurrent1MinPhaseErrorStdDevNs": aluPtpPeerCurrent1MinPhaseErrorStdDevNs,
       "aluPtpPeerCurrent1MinPhaseErrorMeanNs": aluPtpPeerCurrent1MinPhaseErrorMeanNs,
       "aluPtpPeerCurrent1MinFreqOffsetMeanPpb": aluPtpPeerCurrent1MinFreqOffsetMeanPpb,
       "aluPtpPeerCurrent1MinFreqOffsetStdDevPpb": aluPtpPeerCurrent1MinFreqOffsetStdDevPpb,
       "aluPtpPeerRecClkStatsShortIntvlTable": aluPtpPeerRecClkStatsShortIntvlTable,
       "aluPtpPeerRecClkStatsShortIntvlEntry": aluPtpPeerRecClkStatsShortIntvlEntry,
       "aluPtpPeerIntvlClockIndex": aluPtpPeerIntvlClockIndex,
       "aluPtpPeerIntvlPortIndex": aluPtpPeerIntvlPortIndex,
       "aluPtpPeerIntvlIndex": aluPtpPeerIntvlIndex,
       "aluPtpPeerIntvlNumber": aluPtpPeerIntvlNumber,
       "aluPtpPeerIntvlValidData": aluPtpPeerIntvlValidData,
       "aluPtpPeerIntvlUpdateTime": aluPtpPeerIntvlUpdateTime,
       "aluPtpPeerIntvlPhaseErrorMeanPpb": aluPtpPeerIntvlPhaseErrorMeanPpb,
       "aluPtpPeerIntvlPhaseErrorStdDevNs": aluPtpPeerIntvlPhaseErrorStdDevNs,
       "aluPtpPeerIntvlPhaseErrorMeanNs": aluPtpPeerIntvlPhaseErrorMeanNs,
       "aluPtpNotificationObjects": aluPtpNotificationObjects,
       "aluPtpNotifyPrefix": aluPtpNotifyPrefix,
       "aluPtpNotification": aluPtpNotification,
       "aluPtpClockNotifyIndex": aluPtpClockNotifyIndex,
       "aluPtpPortNotifyIndex": aluPtpPortNotifyIndex,
       "aluPtpPeerNotifyIndex": aluPtpPeerNotifyIndex,
       "aluPtpMasterChange": aluPtpMasterChange,
       "aluPtpClockNoMaster": aluPtpClockNoMaster,
       "aluPtpPortStateChange": aluPtpPortStateChange,
       "aluPtpClockRecovClkChange": aluPtpClockRecovClkChange,
       "aluPtpPeerDiscoveryChange": aluPtpPeerDiscoveryChange}
)

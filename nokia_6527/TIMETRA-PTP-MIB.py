# SNMP MIB module (TIMETRA-PTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-PTP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:32 2025
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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tmnxChassisIndex,
 tmnxChassisNotifyChassisId,
 tmnxChassisNotifyHwIndex,
 tmnxCpmCardEntry,
 tmnxCpmCardOscillatorType) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxChassisIndex",
    "tmnxChassisNotifyChassisId",
    "tmnxChassisNotifyHwIndex",
    "tmnxCpmCardEntry",
    "tmnxCpmCardOscillatorType")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TmnxPortEncapType,
 tmnxPortPortID) = mibBuilder.importSymbols(
    "TIMETRA-PORT-MIB",
    "TmnxPortEncapType",
    "tmnxPortPortID")

(TItemDescription,
 TmnxAdminState,
 TmnxEncapVal,
 TmnxOperState,
 TmnxPortID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TmnxAdminState",
    "TmnxEncapVal",
    "TmnxOperState",
    "TmnxPortID")

(vRtrID,
 vRtrIfEntry) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfEntry")


# MODULE-IDENTITY

timetraPtpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 74)
)
if mibBuilder.loadTexts:
    timetraPtpMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2011-02-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxPtpClockType(TextualConvention, Integer32):
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
        *(("ordinarySlave", 1),
          ("ordinaryMaster", 2),
          ("boundary", 3))
    )



class TmnxPtpClockIdentity(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class TmnxPtpClockClass(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxPtpDomain(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxPtpPriority(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxPtpProfile(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("g8265dot1-2010", 1),
          ("ieee1588-2008", 2))
    )



class TmnxPtpDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2))
    )



class TmnxPtpLogInterval(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7, 4),
    )



class TmnxPtpClockStepType(TextualConvention, Integer32):
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



class TmnxPtpClockAccuracy(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxPtpClockVariance(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TmnxPtpPortState(TextualConvention, Integer32):
    status = "current"
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
        *(("notApplicable", 0),
          ("initializing", 1),
          ("faulty", 2),
          ("disabled", 3),
          ("listening", 4),
          ("preMaster", 5),
          ("master", 6),
          ("passive", 7),
          ("uncalibrated", 8),
          ("slave", 9))
    )



class TmnxPtpPortNumber(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )



class TmnxPtpTimeStampReferencePoint(TextualConvention, Integer32):
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
          ("port", 1),
          ("cpm", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxPtp1588Conformance_ObjectIdentity = ObjectIdentity
tmnxPtp1588Conformance = _TmnxPtp1588Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74)
)
_TmnxPtp1588Compliances_ObjectIdentity = ObjectIdentity
tmnxPtp1588Compliances = _TmnxPtp1588Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 1)
)
_TmnxPtp1588Groups_ObjectIdentity = ObjectIdentity
tmnxPtp1588Groups = _TmnxPtp1588Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2)
)
_TmnxPtpV9v0Groups_ObjectIdentity = ObjectIdentity
tmnxPtpV9v0Groups = _TmnxPtpV9v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 1)
)
_TmnxPtpV10v0Groups_ObjectIdentity = ObjectIdentity
tmnxPtpV10v0Groups = _TmnxPtpV10v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 2)
)
_TmnxPtpV11v0Groups_ObjectIdentity = ObjectIdentity
tmnxPtpV11v0Groups = _TmnxPtpV11v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 3)
)
_TmnxPtpV12v0Groups_ObjectIdentity = ObjectIdentity
tmnxPtpV12v0Groups = _TmnxPtpV12v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 4)
)
_TmnxPtp1588Objs_ObjectIdentity = ObjectIdentity
tmnxPtp1588Objs = _TmnxPtp1588Objs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74)
)
_TmnxPtp1588ConfigTimeStamps_ObjectIdentity = ObjectIdentity
tmnxPtp1588ConfigTimeStamps = _TmnxPtp1588ConfigTimeStamps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 1)
)
_TmnxPtpPeerConfigTblLastChanged_Type = TimeStamp
_TmnxPtpPeerConfigTblLastChanged_Object = MibScalar
tmnxPtpPeerConfigTblLastChanged = _TmnxPtpPeerConfigTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 1, 1),
    _TmnxPtpPeerConfigTblLastChanged_Type()
)
tmnxPtpPeerConfigTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerConfigTblLastChanged.setStatus("current")
_TmnxPtpVRtrIfTableLastChanged_Type = TimeStamp
_TmnxPtpVRtrIfTableLastChanged_Object = MibScalar
tmnxPtpVRtrIfTableLastChanged = _TmnxPtpVRtrIfTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 1, 2),
    _TmnxPtpVRtrIfTableLastChanged_Type()
)
tmnxPtpVRtrIfTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpVRtrIfTableLastChanged.setStatus("current")
_TmnxPtpVRtrTableLastChanged_Type = TimeStamp
_TmnxPtpVRtrTableLastChanged_Object = MibScalar
tmnxPtpVRtrTableLastChanged = _TmnxPtpVRtrTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 1, 3),
    _TmnxPtpVRtrTableLastChanged_Type()
)
tmnxPtpVRtrTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpVRtrTableLastChanged.setStatus("current")
_TmnxPtp1588Configurations_ObjectIdentity = ObjectIdentity
tmnxPtp1588Configurations = _TmnxPtp1588Configurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2)
)
_TmnxPtpClockConfig_ObjectIdentity = ObjectIdentity
tmnxPtpClockConfig = _TmnxPtpClockConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 1)
)


class _TmnxPtpClockAdminState_Type(TmnxAdminState):
    """Custom type tmnxPtpClockAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxPtpClockAdminState_Type.__name__ = "TmnxAdminState"
_TmnxPtpClockAdminState_Object = MibScalar
tmnxPtpClockAdminState = _TmnxPtpClockAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 1, 1),
    _TmnxPtpClockAdminState_Type()
)
tmnxPtpClockAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPtpClockAdminState.setStatus("current")


class _TmnxPtpClockClockType_Type(TmnxPtpClockType):
    """Custom type tmnxPtpClockClockType based on TmnxPtpClockType"""
    defaultValue = 1


_TmnxPtpClockClockType_Type.__name__ = "TmnxPtpClockType"
_TmnxPtpClockClockType_Object = MibScalar
tmnxPtpClockClockType = _TmnxPtpClockClockType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 1, 2),
    _TmnxPtpClockClockType_Type()
)
tmnxPtpClockClockType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPtpClockClockType.setStatus("current")


class _TmnxPtpClockProfile_Type(TmnxPtpProfile):
    """Custom type tmnxPtpClockProfile based on TmnxPtpProfile"""
    defaultValue = 1


_TmnxPtpClockProfile_Type.__name__ = "TmnxPtpProfile"
_TmnxPtpClockProfile_Object = MibScalar
tmnxPtpClockProfile = _TmnxPtpClockProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 1, 3),
    _TmnxPtpClockProfile_Type()
)
tmnxPtpClockProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPtpClockProfile.setStatus("current")


class _TmnxPtpClockDomain_Type(TmnxPtpDomain):
    """Custom type tmnxPtpClockDomain based on TmnxPtpDomain"""
    defaultValue = 4


_TmnxPtpClockDomain_Type.__name__ = "TmnxPtpDomain"
_TmnxPtpClockDomain_Object = MibScalar
tmnxPtpClockDomain = _TmnxPtpClockDomain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 1, 4),
    _TmnxPtpClockDomain_Type()
)
tmnxPtpClockDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPtpClockDomain.setStatus("current")


class _TmnxPtpClockAnnounceInterval_Type(TmnxPtpLogInterval):
    """Custom type tmnxPtpClockAnnounceInterval based on TmnxPtpLogInterval"""
    defaultValue = 1

    subtypeSpec = TmnxPtpLogInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3, 4),
    )


_TmnxPtpClockAnnounceInterval_Type.__name__ = "TmnxPtpLogInterval"
_TmnxPtpClockAnnounceInterval_Object = MibScalar
tmnxPtpClockAnnounceInterval = _TmnxPtpClockAnnounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 1, 5),
    _TmnxPtpClockAnnounceInterval_Type()
)
tmnxPtpClockAnnounceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPtpClockAnnounceInterval.setStatus("current")


class _TmnxPtpClockPriority1_Type(TmnxPtpPriority):
    """Custom type tmnxPtpClockPriority1 based on TmnxPtpPriority"""
    defaultValue = 128


_TmnxPtpClockPriority1_Type.__name__ = "TmnxPtpPriority"
_TmnxPtpClockPriority1_Object = MibScalar
tmnxPtpClockPriority1 = _TmnxPtpClockPriority1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 1, 6),
    _TmnxPtpClockPriority1_Type()
)
tmnxPtpClockPriority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPtpClockPriority1.setStatus("current")


class _TmnxPtpClockPriority2_Type(TmnxPtpPriority):
    """Custom type tmnxPtpClockPriority2 based on TmnxPtpPriority"""
    defaultValue = 128


_TmnxPtpClockPriority2_Type.__name__ = "TmnxPtpPriority"
_TmnxPtpClockPriority2_Object = MibScalar
tmnxPtpClockPriority2 = _TmnxPtpClockPriority2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 1, 7),
    _TmnxPtpClockPriority2_Type()
)
tmnxPtpClockPriority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPtpClockPriority2.setStatus("current")


class _TmnxPtpClockNetworkType_Type(Integer32):
    """Custom type tmnxPtpClockNetworkType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sonet", 1),
          ("sdh", 2))
    )


_TmnxPtpClockNetworkType_Type.__name__ = "Integer32"
_TmnxPtpClockNetworkType_Object = MibScalar
tmnxPtpClockNetworkType = _TmnxPtpClockNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 1, 9),
    _TmnxPtpClockNetworkType_Type()
)
tmnxPtpClockNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPtpClockNetworkType.setStatus("current")


class _TmnxPtpClockAnnoRxTimeout_Type(Unsigned32):
    """Custom type tmnxPtpClockAnnoRxTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_TmnxPtpClockAnnoRxTimeout_Type.__name__ = "Unsigned32"
_TmnxPtpClockAnnoRxTimeout_Object = MibScalar
tmnxPtpClockAnnoRxTimeout = _TmnxPtpClockAnnoRxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 1, 10),
    _TmnxPtpClockAnnoRxTimeout_Type()
)
tmnxPtpClockAnnoRxTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPtpClockAnnoRxTimeout.setStatus("current")
_TmnxPtpPeerConfigTable_Object = MibTable
tmnxPtpPeerConfigTable = _TmnxPtpPeerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxPtpPeerConfigTable.setStatus("current")
_TmnxPtpPeerConfigEntry_Object = MibTableRow
tmnxPtpPeerConfigEntry = _TmnxPtpPeerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1)
)
tmnxPtpPeerConfigEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PTP-MIB", "tmnxPtpPeerIpAddrType"),
    (0, "TIMETRA-PTP-MIB", "tmnxPtpPeerIpAddress"),
)
if mibBuilder.loadTexts:
    tmnxPtpPeerConfigEntry.setStatus("current")
_TmnxPtpPeerIpAddrType_Type = InetAddressType
_TmnxPtpPeerIpAddrType_Object = MibTableColumn
tmnxPtpPeerIpAddrType = _TmnxPtpPeerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 1),
    _TmnxPtpPeerIpAddrType_Type()
)
tmnxPtpPeerIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPtpPeerIpAddrType.setStatus("current")


class _TmnxPtpPeerIpAddress_Type(InetAddress):
    """Custom type tmnxPtpPeerIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxPtpPeerIpAddress_Type.__name__ = "InetAddress"
_TmnxPtpPeerIpAddress_Object = MibTableColumn
tmnxPtpPeerIpAddress = _TmnxPtpPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 2),
    _TmnxPtpPeerIpAddress_Type()
)
tmnxPtpPeerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPtpPeerIpAddress.setStatus("current")
_TmnxPtpPeerRowStatus_Type = RowStatus
_TmnxPtpPeerRowStatus_Object = MibTableColumn
tmnxPtpPeerRowStatus = _TmnxPtpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 3),
    _TmnxPtpPeerRowStatus_Type()
)
tmnxPtpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPtpPeerRowStatus.setStatus("current")
_TmnxPtpPeerLastChanged_Type = TimeStamp
_TmnxPtpPeerLastChanged_Object = MibTableColumn
tmnxPtpPeerLastChanged = _TmnxPtpPeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 4),
    _TmnxPtpPeerLastChanged_Type()
)
tmnxPtpPeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerLastChanged.setStatus("current")


class _TmnxPtpPeerAdminState_Type(TmnxAdminState):
    """Custom type tmnxPtpPeerAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxPtpPeerAdminState_Type.__name__ = "TmnxAdminState"
_TmnxPtpPeerAdminState_Object = MibTableColumn
tmnxPtpPeerAdminState = _TmnxPtpPeerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 5),
    _TmnxPtpPeerAdminState_Type()
)
tmnxPtpPeerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPtpPeerAdminState.setStatus("current")
_TmnxPtpPeerPortState_Type = TmnxPtpPortState
_TmnxPtpPeerPortState_Object = MibTableColumn
tmnxPtpPeerPortState = _TmnxPtpPeerPortState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 6),
    _TmnxPtpPeerPortState_Type()
)
tmnxPtpPeerPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPortState.setStatus("current")


class _TmnxPtpPeerLocalPriority_Type(TmnxPtpPriority):
    """Custom type tmnxPtpPeerLocalPriority based on TmnxPtpPriority"""
    defaultValue = 128


_TmnxPtpPeerLocalPriority_Type.__name__ = "TmnxPtpPriority"
_TmnxPtpPeerLocalPriority_Object = MibTableColumn
tmnxPtpPeerLocalPriority = _TmnxPtpPeerLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 7),
    _TmnxPtpPeerLocalPriority_Type()
)
tmnxPtpPeerLocalPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPtpPeerLocalPriority.setStatus("current")
_TmnxPtpPeerRemoteMaster_Type = TruthValue
_TmnxPtpPeerRemoteMaster_Object = MibTableColumn
tmnxPtpPeerRemoteMaster = _TmnxPtpPeerRemoteMaster_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 8),
    _TmnxPtpPeerRemoteMaster_Type()
)
tmnxPtpPeerRemoteMaster.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPtpPeerRemoteMaster.setStatus("current")
_TmnxPtpPeerRemoteSlave_Type = TruthValue
_TmnxPtpPeerRemoteSlave_Object = MibTableColumn
tmnxPtpPeerRemoteSlave = _TmnxPtpPeerRemoteSlave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 9),
    _TmnxPtpPeerRemoteSlave_Type()
)
tmnxPtpPeerRemoteSlave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerRemoteSlave.setStatus("current")
_TmnxPtpPeerClockId_Type = TmnxPtpClockIdentity
_TmnxPtpPeerClockId_Object = MibTableColumn
tmnxPtpPeerClockId = _TmnxPtpPeerClockId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 10),
    _TmnxPtpPeerClockId_Type()
)
tmnxPtpPeerClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerClockId.setStatus("current")
_TmnxPtpPeerLocalPortNumber_Type = TmnxPtpPortNumber
_TmnxPtpPeerLocalPortNumber_Object = MibTableColumn
tmnxPtpPeerLocalPortNumber = _TmnxPtpPeerLocalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 11),
    _TmnxPtpPeerLocalPortNumber_Type()
)
tmnxPtpPeerLocalPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerLocalPortNumber.setStatus("current")
_TmnxPtpPeerRemotePortNumber_Type = TmnxPtpPortNumber
_TmnxPtpPeerRemotePortNumber_Object = MibTableColumn
tmnxPtpPeerRemotePortNumber = _TmnxPtpPeerRemotePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 12),
    _TmnxPtpPeerRemotePortNumber_Type()
)
tmnxPtpPeerRemotePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerRemotePortNumber.setStatus("current")
_TmnxPtpPeerTxTimeStampPoint_Type = TmnxPtpTimeStampReferencePoint
_TmnxPtpPeerTxTimeStampPoint_Object = MibTableColumn
tmnxPtpPeerTxTimeStampPoint = _TmnxPtpPeerTxTimeStampPoint_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 13),
    _TmnxPtpPeerTxTimeStampPoint_Type()
)
tmnxPtpPeerTxTimeStampPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerTxTimeStampPoint.setStatus("current")
_TmnxPtpPeerLastTxPortId_Type = TmnxPortID
_TmnxPtpPeerLastTxPortId_Object = MibTableColumn
tmnxPtpPeerLastTxPortId = _TmnxPtpPeerLastTxPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 14),
    _TmnxPtpPeerLastTxPortId_Type()
)
tmnxPtpPeerLastTxPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerLastTxPortId.setStatus("current")
_TmnxPtpPeerLastTxPortEncapType_Type = TmnxPortEncapType
_TmnxPtpPeerLastTxPortEncapType_Object = MibTableColumn
tmnxPtpPeerLastTxPortEncapType = _TmnxPtpPeerLastTxPortEncapType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 15),
    _TmnxPtpPeerLastTxPortEncapType_Type()
)
tmnxPtpPeerLastTxPortEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerLastTxPortEncapType.setStatus("current")
_TmnxPtpPeerLastTxPortEncapValue_Type = TmnxEncapVal
_TmnxPtpPeerLastTxPortEncapValue_Object = MibTableColumn
tmnxPtpPeerLastTxPortEncapValue = _TmnxPtpPeerLastTxPortEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 16),
    _TmnxPtpPeerLastTxPortEncapValue_Type()
)
tmnxPtpPeerLastTxPortEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerLastTxPortEncapValue.setStatus("current")
_TmnxPtpPeerRxTimeStampPoint_Type = TmnxPtpTimeStampReferencePoint
_TmnxPtpPeerRxTimeStampPoint_Object = MibTableColumn
tmnxPtpPeerRxTimeStampPoint = _TmnxPtpPeerRxTimeStampPoint_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 17),
    _TmnxPtpPeerRxTimeStampPoint_Type()
)
tmnxPtpPeerRxTimeStampPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerRxTimeStampPoint.setStatus("current")
_TmnxPtpPeerLastRxPortId_Type = TmnxPortID
_TmnxPtpPeerLastRxPortId_Object = MibTableColumn
tmnxPtpPeerLastRxPortId = _TmnxPtpPeerLastRxPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 18),
    _TmnxPtpPeerLastRxPortId_Type()
)
tmnxPtpPeerLastRxPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerLastRxPortId.setStatus("current")
_TmnxPtpPeerLastRxPortEncapType_Type = TmnxPortEncapType
_TmnxPtpPeerLastRxPortEncapType_Object = MibTableColumn
tmnxPtpPeerLastRxPortEncapType = _TmnxPtpPeerLastRxPortEncapType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 19),
    _TmnxPtpPeerLastRxPortEncapType_Type()
)
tmnxPtpPeerLastRxPortEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerLastRxPortEncapType.setStatus("current")
_TmnxPtpPeerLastRxPortEncapValue_Type = TmnxEncapVal
_TmnxPtpPeerLastRxPortEncapValue_Object = MibTableColumn
tmnxPtpPeerLastRxPortEncapValue = _TmnxPtpPeerLastRxPortEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 20),
    _TmnxPtpPeerLastRxPortEncapValue_Type()
)
tmnxPtpPeerLastRxPortEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerLastRxPortEncapValue.setStatus("current")


class _TmnxPtpPeerSyncInterval_Type(TmnxPtpLogInterval):
    """Custom type tmnxPtpPeerSyncInterval based on TmnxPtpLogInterval"""
    defaultValue = -6

    subtypeSpec = TmnxPtpLogInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-6, 0),
    )


_TmnxPtpPeerSyncInterval_Type.__name__ = "TmnxPtpLogInterval"
_TmnxPtpPeerSyncInterval_Object = MibTableColumn
tmnxPtpPeerSyncInterval = _TmnxPtpPeerSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 3, 1, 21),
    _TmnxPtpPeerSyncInterval_Type()
)
tmnxPtpPeerSyncInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPtpPeerSyncInterval.setStatus("current")
_TmnxPtpVRtrIfTable_Object = MibTable
tmnxPtpVRtrIfTable = _TmnxPtpVRtrIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxPtpVRtrIfTable.setStatus("current")
_TmnxPtpVRtrIfEntry_Object = MibTableRow
tmnxPtpVRtrIfEntry = _TmnxPtpVRtrIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxPtpVRtrIfEntry.setStatus("current")
_TmnxPtpVRtrIfAdminState_Type = TmnxAdminState
_TmnxPtpVRtrIfAdminState_Object = MibTableColumn
tmnxPtpVRtrIfAdminState = _TmnxPtpVRtrIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 4, 1, 1),
    _TmnxPtpVRtrIfAdminState_Type()
)
tmnxPtpVRtrIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPtpVRtrIfAdminState.setStatus("current")
_TmnxPtpVRtrTable_Object = MibTable
tmnxPtpVRtrTable = _TmnxPtpVRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 5)
)
if mibBuilder.loadTexts:
    tmnxPtpVRtrTable.setStatus("current")
_TmnxPtpVRtrEntry_Object = MibTableRow
tmnxPtpVRtrEntry = _TmnxPtpVRtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 5, 1)
)
tmnxPtpVRtrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    tmnxPtpVRtrEntry.setStatus("current")
_TmnxPtpVRtrRowStatus_Type = RowStatus
_TmnxPtpVRtrRowStatus_Object = MibTableColumn
tmnxPtpVRtrRowStatus = _TmnxPtpVRtrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 5, 1, 1),
    _TmnxPtpVRtrRowStatus_Type()
)
tmnxPtpVRtrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPtpVRtrRowStatus.setStatus("current")
_TmnxPtpVRtrLastChanged_Type = TimeStamp
_TmnxPtpVRtrLastChanged_Object = MibTableColumn
tmnxPtpVRtrLastChanged = _TmnxPtpVRtrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 5, 1, 2),
    _TmnxPtpVRtrLastChanged_Type()
)
tmnxPtpVRtrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpVRtrLastChanged.setStatus("current")


class _TmnxPtpVRtrAdminState_Type(TmnxAdminState):
    """Custom type tmnxPtpVRtrAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxPtpVRtrAdminState_Type.__name__ = "TmnxAdminState"
_TmnxPtpVRtrAdminState_Object = MibTableColumn
tmnxPtpVRtrAdminState = _TmnxPtpVRtrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 5, 1, 3),
    _TmnxPtpVRtrAdminState_Type()
)
tmnxPtpVRtrAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPtpVRtrAdminState.setStatus("current")
_TmnxPtpVRtrOperState_Type = TmnxOperState
_TmnxPtpVRtrOperState_Object = MibTableColumn
tmnxPtpVRtrOperState = _TmnxPtpVRtrOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 5, 1, 4),
    _TmnxPtpVRtrOperState_Type()
)
tmnxPtpVRtrOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpVRtrOperState.setStatus("current")


class _TmnxPtpVRtrPeerLimit_Type(Integer32):
    """Custom type tmnxPtpVRtrPeerLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 512),
    )


_TmnxPtpVRtrPeerLimit_Type.__name__ = "Integer32"
_TmnxPtpVRtrPeerLimit_Object = MibTableColumn
tmnxPtpVRtrPeerLimit = _TmnxPtpVRtrPeerLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 2, 5, 1, 5),
    _TmnxPtpVRtrPeerLimit_Type()
)
tmnxPtpVRtrPeerLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPtpVRtrPeerLimit.setStatus("current")
_TmnxPtp1588Status_ObjectIdentity = ObjectIdentity
tmnxPtp1588Status = _TmnxPtp1588Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3)
)
_TmnxPtpClockOperTable_Object = MibTable
tmnxPtpClockOperTable = _TmnxPtpClockOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxPtpClockOperTable.setStatus("current")
_TmnxPtpClockOperEntry_Object = MibTableRow
tmnxPtpClockOperEntry = _TmnxPtpClockOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxPtpClockOperEntry.setStatus("current")
_TmnxPtpClockIdentity_Type = TmnxPtpClockIdentity
_TmnxPtpClockIdentity_Object = MibTableColumn
tmnxPtpClockIdentity = _TmnxPtpClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 1, 1, 1),
    _TmnxPtpClockIdentity_Type()
)
tmnxPtpClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockIdentity.setStatus("current")
_TmnxPtpClockOperState_Type = TmnxOperState
_TmnxPtpClockOperState_Object = MibTableColumn
tmnxPtpClockOperState = _TmnxPtpClockOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 1, 1, 2),
    _TmnxPtpClockOperState_Type()
)
tmnxPtpClockOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockOperState.setStatus("current")
_TmnxPtpClockStepType_Type = TmnxPtpClockStepType
_TmnxPtpClockStepType_Object = MibTableColumn
tmnxPtpClockStepType = _TmnxPtpClockStepType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 1, 1, 3),
    _TmnxPtpClockStepType_Type()
)
tmnxPtpClockStepType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockStepType.setStatus("current")
_TmnxPtpClockClass_Type = TmnxPtpClockClass
_TmnxPtpClockClass_Object = MibTableColumn
tmnxPtpClockClass = _TmnxPtpClockClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 1, 1, 4),
    _TmnxPtpClockClass_Type()
)
tmnxPtpClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockClass.setStatus("current")
_TmnxPtpClockAccuracy_Type = TmnxPtpClockAccuracy
_TmnxPtpClockAccuracy_Object = MibTableColumn
tmnxPtpClockAccuracy = _TmnxPtpClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 1, 1, 5),
    _TmnxPtpClockAccuracy_Type()
)
tmnxPtpClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockAccuracy.setStatus("current")
_TmnxPtpClockVariance_Type = TmnxPtpClockVariance
_TmnxPtpClockVariance_Object = MibTableColumn
tmnxPtpClockVariance = _TmnxPtpClockVariance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 1, 1, 6),
    _TmnxPtpClockVariance_Type()
)
tmnxPtpClockVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockVariance.setStatus("current")
_TmnxPtpClockPortState_Type = TmnxPtpPortState
_TmnxPtpClockPortState_Object = MibTableColumn
tmnxPtpClockPortState = _TmnxPtpClockPortState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 1, 1, 7),
    _TmnxPtpClockPortState_Type()
)
tmnxPtpClockPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockPortState.setStatus("current")
_TmnxPtpClockPortStateLastChanged_Type = TimeStamp
_TmnxPtpClockPortStateLastChanged_Object = MibTableColumn
tmnxPtpClockPortStateLastChanged = _TmnxPtpClockPortStateLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 1, 1, 8),
    _TmnxPtpClockPortStateLastChanged_Type()
)
tmnxPtpClockPortStateLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockPortStateLastChanged.setStatus("current")


class _TmnxPtpClockRecoveryState_Type(Integer32):
    """Custom type tmnxPtpClockRecoveryState based on Integer32"""
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
        *(("notApplicable", 0),
          ("initial", 1),
          ("acquiring", 2),
          ("phaseTracking", 3),
          ("holdover", 4),
          ("locked", 5))
    )


_TmnxPtpClockRecoveryState_Type.__name__ = "Integer32"
_TmnxPtpClockRecoveryState_Object = MibTableColumn
tmnxPtpClockRecoveryState = _TmnxPtpClockRecoveryState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 1, 1, 9),
    _TmnxPtpClockRecoveryState_Type()
)
tmnxPtpClockRecoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockRecoveryState.setStatus("current")
_TmnxPtpClockRecoveryStateLastChg_Type = TimeStamp
_TmnxPtpClockRecoveryStateLastChg_Object = MibTableColumn
tmnxPtpClockRecoveryStateLastChg = _TmnxPtpClockRecoveryStateLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 1, 1, 10),
    _TmnxPtpClockRecoveryStateLastChg_Type()
)
tmnxPtpClockRecoveryStateLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockRecoveryStateLastChg.setStatus("current")
_TmnxPtpClockFrequencyOffset_Type = Integer32
_TmnxPtpClockFrequencyOffset_Object = MibTableColumn
tmnxPtpClockFrequencyOffset = _TmnxPtpClockFrequencyOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 1, 1, 11),
    _TmnxPtpClockFrequencyOffset_Type()
)
tmnxPtpClockFrequencyOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockFrequencyOffset.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPtpClockFrequencyOffset.setUnits("parts per trillion")
_TmnxPtpMasterClockOper_ObjectIdentity = ObjectIdentity
tmnxPtpMasterClockOper = _TmnxPtpMasterClockOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 2)
)
_TmnxPtpMasterClockAddressType_Type = InetAddressType
_TmnxPtpMasterClockAddressType_Object = MibScalar
tmnxPtpMasterClockAddressType = _TmnxPtpMasterClockAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 2, 1),
    _TmnxPtpMasterClockAddressType_Type()
)
tmnxPtpMasterClockAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpMasterClockAddressType.setStatus("current")


class _TmnxPtpMasterClockAddress_Type(InetAddress):
    """Custom type tmnxPtpMasterClockAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxPtpMasterClockAddress_Type.__name__ = "InetAddress"
_TmnxPtpMasterClockAddress_Object = MibScalar
tmnxPtpMasterClockAddress = _TmnxPtpMasterClockAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 2, 2),
    _TmnxPtpMasterClockAddress_Type()
)
tmnxPtpMasterClockAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpMasterClockAddress.setStatus("current")
_TmnxPtpMasterClockGMClockId_Type = TmnxPtpClockIdentity
_TmnxPtpMasterClockGMClockId_Object = MibScalar
tmnxPtpMasterClockGMClockId = _TmnxPtpMasterClockGMClockId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 2, 3),
    _TmnxPtpMasterClockGMClockId_Type()
)
tmnxPtpMasterClockGMClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpMasterClockGMClockId.setStatus("current")
_TmnxPtpMasterClockGMClockPrio1_Type = TmnxPtpPriority
_TmnxPtpMasterClockGMClockPrio1_Object = MibScalar
tmnxPtpMasterClockGMClockPrio1 = _TmnxPtpMasterClockGMClockPrio1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 2, 4),
    _TmnxPtpMasterClockGMClockPrio1_Type()
)
tmnxPtpMasterClockGMClockPrio1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpMasterClockGMClockPrio1.setStatus("current")
_TmnxPtpMasterClockGMClockPrio2_Type = TmnxPtpPriority
_TmnxPtpMasterClockGMClockPrio2_Object = MibScalar
tmnxPtpMasterClockGMClockPrio2 = _TmnxPtpMasterClockGMClockPrio2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 2, 5),
    _TmnxPtpMasterClockGMClockPrio2_Type()
)
tmnxPtpMasterClockGMClockPrio2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpMasterClockGMClockPrio2.setStatus("current")
_TmnxPtpMasterClockGMClockClass_Type = TmnxPtpClockClass
_TmnxPtpMasterClockGMClockClass_Object = MibScalar
tmnxPtpMasterClockGMClockClass = _TmnxPtpMasterClockGMClockClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 2, 6),
    _TmnxPtpMasterClockGMClockClass_Type()
)
tmnxPtpMasterClockGMClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpMasterClockGMClockClass.setStatus("current")
_TmnxPtpMasterClockGMAccuracy_Type = TmnxPtpClockAccuracy
_TmnxPtpMasterClockGMAccuracy_Object = MibScalar
tmnxPtpMasterClockGMAccuracy = _TmnxPtpMasterClockGMAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 2, 7),
    _TmnxPtpMasterClockGMAccuracy_Type()
)
tmnxPtpMasterClockGMAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpMasterClockGMAccuracy.setStatus("current")
_TmnxPtpMasterClockGMVariance_Type = TmnxPtpClockVariance
_TmnxPtpMasterClockGMVariance_Object = MibScalar
tmnxPtpMasterClockGMVariance = _TmnxPtpMasterClockGMVariance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 2, 8),
    _TmnxPtpMasterClockGMVariance_Type()
)
tmnxPtpMasterClockGMVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpMasterClockGMVariance.setStatus("current")
_TmnxPtpMasterClockParentClockId_Type = TmnxPtpClockIdentity
_TmnxPtpMasterClockParentClockId_Object = MibScalar
tmnxPtpMasterClockParentClockId = _TmnxPtpMasterClockParentClockId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 2, 9),
    _TmnxPtpMasterClockParentClockId_Type()
)
tmnxPtpMasterClockParentClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpMasterClockParentClockId.setStatus("current")
_TmnxPtpMasterClockParentPortNum_Type = TmnxPtpPortNumber
_TmnxPtpMasterClockParentPortNum_Object = MibScalar
tmnxPtpMasterClockParentPortNum = _TmnxPtpMasterClockParentPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 2, 10),
    _TmnxPtpMasterClockParentPortNum_Type()
)
tmnxPtpMasterClockParentPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpMasterClockParentPortNum.setStatus("current")
_TmnxPtpPeerMasterStatusTable_Object = MibTable
tmnxPtpPeerMasterStatusTable = _TmnxPtpPeerMasterStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxPtpPeerMasterStatusTable.setStatus("current")
_TmnxPtpPeerMasterStatusEntry_Object = MibTableRow
tmnxPtpPeerMasterStatusEntry = _TmnxPtpPeerMasterStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 3, 1)
)
tmnxPtpPeerMasterStatusEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PTP-MIB", "tmnxPtpPeerIpAddrType"),
    (0, "TIMETRA-PTP-MIB", "tmnxPtpPeerIpAddress"),
)
if mibBuilder.loadTexts:
    tmnxPtpPeerMasterStatusEntry.setStatus("current")
_TmnxPtpPeerMasterCurrentMaster_Type = TruthValue
_TmnxPtpPeerMasterCurrentMaster_Object = MibTableColumn
tmnxPtpPeerMasterCurrentMaster = _TmnxPtpPeerMasterCurrentMaster_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 3, 1, 1),
    _TmnxPtpPeerMasterCurrentMaster_Type()
)
tmnxPtpPeerMasterCurrentMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerMasterCurrentMaster.setStatus("current")
_TmnxPtpPeerMasterClockStepType_Type = TmnxPtpClockStepType
_TmnxPtpPeerMasterClockStepType_Object = MibTableColumn
tmnxPtpPeerMasterClockStepType = _TmnxPtpPeerMasterClockStepType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 3, 1, 2),
    _TmnxPtpPeerMasterClockStepType_Type()
)
tmnxPtpPeerMasterClockStepType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerMasterClockStepType.setStatus("current")
_TmnxPtpPeerMasterClockStepsRemvd_Type = Unsigned32
_TmnxPtpPeerMasterClockStepsRemvd_Object = MibTableColumn
tmnxPtpPeerMasterClockStepsRemvd = _TmnxPtpPeerMasterClockStepsRemvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 3, 1, 3),
    _TmnxPtpPeerMasterClockStepsRemvd_Type()
)
tmnxPtpPeerMasterClockStepsRemvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerMasterClockStepsRemvd.setStatus("current")
_TmnxPtpPeerMasterGMClockId_Type = TmnxPtpClockIdentity
_TmnxPtpPeerMasterGMClockId_Object = MibTableColumn
tmnxPtpPeerMasterGMClockId = _TmnxPtpPeerMasterGMClockId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 3, 1, 4),
    _TmnxPtpPeerMasterGMClockId_Type()
)
tmnxPtpPeerMasterGMClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerMasterGMClockId.setStatus("current")
_TmnxPtpPeerMasterGMClockPrio1_Type = TmnxPtpPriority
_TmnxPtpPeerMasterGMClockPrio1_Object = MibTableColumn
tmnxPtpPeerMasterGMClockPrio1 = _TmnxPtpPeerMasterGMClockPrio1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 3, 1, 5),
    _TmnxPtpPeerMasterGMClockPrio1_Type()
)
tmnxPtpPeerMasterGMClockPrio1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerMasterGMClockPrio1.setStatus("current")
_TmnxPtpPeerMasterGMClockPrio2_Type = TmnxPtpPriority
_TmnxPtpPeerMasterGMClockPrio2_Object = MibTableColumn
tmnxPtpPeerMasterGMClockPrio2 = _TmnxPtpPeerMasterGMClockPrio2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 3, 1, 6),
    _TmnxPtpPeerMasterGMClockPrio2_Type()
)
tmnxPtpPeerMasterGMClockPrio2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerMasterGMClockPrio2.setStatus("current")
_TmnxPtpPeerMasterGMClockClass_Type = TmnxPtpClockClass
_TmnxPtpPeerMasterGMClockClass_Object = MibTableColumn
tmnxPtpPeerMasterGMClockClass = _TmnxPtpPeerMasterGMClockClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 3, 1, 7),
    _TmnxPtpPeerMasterGMClockClass_Type()
)
tmnxPtpPeerMasterGMClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerMasterGMClockClass.setStatus("current")
_TmnxPtpPeerMasterGMClockAccuracy_Type = TmnxPtpClockAccuracy
_TmnxPtpPeerMasterGMClockAccuracy_Object = MibTableColumn
tmnxPtpPeerMasterGMClockAccuracy = _TmnxPtpPeerMasterGMClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 3, 1, 8),
    _TmnxPtpPeerMasterGMClockAccuracy_Type()
)
tmnxPtpPeerMasterGMClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerMasterGMClockAccuracy.setStatus("current")
_TmnxPtpPeerMasterGMClockVariance_Type = TmnxPtpClockVariance
_TmnxPtpPeerMasterGMClockVariance_Object = MibTableColumn
tmnxPtpPeerMasterGMClockVariance = _TmnxPtpPeerMasterGMClockVariance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 3, 1, 9),
    _TmnxPtpPeerMasterGMClockVariance_Type()
)
tmnxPtpPeerMasterGMClockVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerMasterGMClockVariance.setStatus("current")


class _TmnxPtpPeerMasterAlarm_Type(Bits):
    """Custom type tmnxPtpPeerMasterAlarm based on Bits"""
    namedValues = NamedValues(
        *(("ptsfLossAnnounce", 0),
          ("ptsfLossSync", 1))
    )

_TmnxPtpPeerMasterAlarm_Type.__name__ = "Bits"
_TmnxPtpPeerMasterAlarm_Object = MibTableColumn
tmnxPtpPeerMasterAlarm = _TmnxPtpPeerMasterAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 3, 1, 11),
    _TmnxPtpPeerMasterAlarm_Type()
)
tmnxPtpPeerMasterAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerMasterAlarm.setStatus("current")
_TmnxPtpPeerUnicastTable_Object = MibTable
tmnxPtpPeerUnicastTable = _TmnxPtpPeerUnicastTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxPtpPeerUnicastTable.setStatus("current")
_TmnxPtpPeerUnicastEntry_Object = MibTableRow
tmnxPtpPeerUnicastEntry = _TmnxPtpPeerUnicastEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 4, 1)
)
tmnxPtpPeerUnicastEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PTP-MIB", "tmnxPtpPeerIpAddrType"),
    (0, "TIMETRA-PTP-MIB", "tmnxPtpPeerIpAddress"),
    (0, "TIMETRA-PTP-MIB", "tmnxPtpPeerUnicastDirection"),
    (0, "TIMETRA-PTP-MIB", "tmnxPtpPeerUnicastPktType"),
)
if mibBuilder.loadTexts:
    tmnxPtpPeerUnicastEntry.setStatus("current")
_TmnxPtpPeerUnicastDirection_Type = TmnxPtpDirection
_TmnxPtpPeerUnicastDirection_Object = MibTableColumn
tmnxPtpPeerUnicastDirection = _TmnxPtpPeerUnicastDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 4, 1, 1),
    _TmnxPtpPeerUnicastDirection_Type()
)
tmnxPtpPeerUnicastDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPtpPeerUnicastDirection.setStatus("current")


class _TmnxPtpPeerUnicastPktType_Type(Integer32):
    """Custom type tmnxPtpPeerUnicastPktType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("announce", 1),
          ("sync", 2),
          ("delayResponse", 3))
    )


_TmnxPtpPeerUnicastPktType_Type.__name__ = "Integer32"
_TmnxPtpPeerUnicastPktType_Object = MibTableColumn
tmnxPtpPeerUnicastPktType = _TmnxPtpPeerUnicastPktType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 4, 1, 2),
    _TmnxPtpPeerUnicastPktType_Type()
)
tmnxPtpPeerUnicastPktType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPtpPeerUnicastPktType.setStatus("current")


class _TmnxPtpPeerUnicastStatus_Type(Integer32):
    """Custom type tmnxPtpPeerUnicastStatus based on Integer32"""
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
        *(("pending", 1),
          ("granted", 2),
          ("denied", 3),
          ("expired", 4),
          ("canceled", 5))
    )


_TmnxPtpPeerUnicastStatus_Type.__name__ = "Integer32"
_TmnxPtpPeerUnicastStatus_Object = MibTableColumn
tmnxPtpPeerUnicastStatus = _TmnxPtpPeerUnicastStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 4, 1, 3),
    _TmnxPtpPeerUnicastStatus_Type()
)
tmnxPtpPeerUnicastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerUnicastStatus.setStatus("current")
_TmnxPtpPeerUnicastRate_Type = TmnxPtpLogInterval
_TmnxPtpPeerUnicastRate_Object = MibTableColumn
tmnxPtpPeerUnicastRate = _TmnxPtpPeerUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 4, 1, 4),
    _TmnxPtpPeerUnicastRate_Type()
)
tmnxPtpPeerUnicastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerUnicastRate.setStatus("current")
_TmnxPtpPeerUnicastDuration_Type = Unsigned32
_TmnxPtpPeerUnicastDuration_Object = MibTableColumn
tmnxPtpPeerUnicastDuration = _TmnxPtpPeerUnicastDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 4, 1, 5),
    _TmnxPtpPeerUnicastDuration_Type()
)
tmnxPtpPeerUnicastDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerUnicastDuration.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPtpPeerUnicastDuration.setUnits("seconds")
_TmnxPtpPeerUnicastEventTime_Type = TimeStamp
_TmnxPtpPeerUnicastEventTime_Object = MibTableColumn
tmnxPtpPeerUnicastEventTime = _TmnxPtpPeerUnicastEventTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 4, 1, 6),
    _TmnxPtpPeerUnicastEventTime_Type()
)
tmnxPtpPeerUnicastEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerUnicastEventTime.setStatus("current")
_TmnxPtpTimeInformation_ObjectIdentity = ObjectIdentity
tmnxPtpTimeInformation = _TmnxPtpTimeInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 5)
)


class _TmnxPtpTimeInfoTimescale_Type(Integer32):
    """Custom type tmnxPtpTimeInfoTimescale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ptp", 1),
          ("arbitrary", 2))
    )


_TmnxPtpTimeInfoTimescale_Type.__name__ = "Integer32"
_TmnxPtpTimeInfoTimescale_Object = MibScalar
tmnxPtpTimeInfoTimescale = _TmnxPtpTimeInfoTimescale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 5, 1),
    _TmnxPtpTimeInfoTimescale_Type()
)
tmnxPtpTimeInfoTimescale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpTimeInfoTimescale.setStatus("current")


class _TmnxPtpTimeInfoCurrentTime_Type(DateAndTime):
    """Custom type tmnxPtpTimeInfoCurrentTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxPtpTimeInfoCurrentTime_Type.__name__ = "DateAndTime"
_TmnxPtpTimeInfoCurrentTime_Object = MibScalar
tmnxPtpTimeInfoCurrentTime = _TmnxPtpTimeInfoCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 5, 2),
    _TmnxPtpTimeInfoCurrentTime_Type()
)
tmnxPtpTimeInfoCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpTimeInfoCurrentTime.setStatus("current")
_TmnxPtpTimeInfoFreqTraceable_Type = TruthValue
_TmnxPtpTimeInfoFreqTraceable_Object = MibScalar
tmnxPtpTimeInfoFreqTraceable = _TmnxPtpTimeInfoFreqTraceable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 5, 3),
    _TmnxPtpTimeInfoFreqTraceable_Type()
)
tmnxPtpTimeInfoFreqTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpTimeInfoFreqTraceable.setStatus("current")
_TmnxPtpTimeInfoTimeTraceable_Type = TruthValue
_TmnxPtpTimeInfoTimeTraceable_Object = MibScalar
tmnxPtpTimeInfoTimeTraceable = _TmnxPtpTimeInfoTimeTraceable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 5, 4),
    _TmnxPtpTimeInfoTimeTraceable_Type()
)
tmnxPtpTimeInfoTimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpTimeInfoTimeTraceable.setStatus("current")


class _TmnxPtpTimeInfoTimeSource_Type(Integer32):
    """Custom type tmnxPtpTimeInfoTimeSource based on Integer32"""
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
        *(("atomicClock", 16),
          ("gps", 32),
          ("terrestrialRadio", 48),
          ("ptp", 64),
          ("ntp", 80),
          ("handSet", 96),
          ("other", 144),
          ("internalOscillator", 160),
          ("reserved", 255))
    )


_TmnxPtpTimeInfoTimeSource_Type.__name__ = "Integer32"
_TmnxPtpTimeInfoTimeSource_Object = MibScalar
tmnxPtpTimeInfoTimeSource = _TmnxPtpTimeInfoTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 3, 5, 5),
    _TmnxPtpTimeInfoTimeSource_Type()
)
tmnxPtpTimeInfoTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpTimeInfoTimeSource.setStatus("current")
_TmnxPtp1588Statistics_ObjectIdentity = ObjectIdentity
tmnxPtp1588Statistics = _TmnxPtp1588Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5)
)
_TmnxPtpClockPacketStatsTable_Object = MibTable
tmnxPtpClockPacketStatsTable = _TmnxPtpClockPacketStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxPtpClockPacketStatsTable.setStatus("current")
_TmnxPtpClockPacketStatsEntry_Object = MibTableRow
tmnxPtpClockPacketStatsEntry = _TmnxPtpClockPacketStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1)
)
tmnxPtpClockPacketStatsEntry.setIndexNames(
    (0, "TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsDirection"),
)
if mibBuilder.loadTexts:
    tmnxPtpClockPacketStatsEntry.setStatus("current")
_TmnxPtpClkPktStatsDirection_Type = TmnxPtpDirection
_TmnxPtpClkPktStatsDirection_Object = MibTableColumn
tmnxPtpClkPktStatsDirection = _TmnxPtpClkPktStatsDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 1),
    _TmnxPtpClkPktStatsDirection_Type()
)
tmnxPtpClkPktStatsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsDirection.setStatus("current")
_TmnxPtpClkPktStatsAnnounce_Type = Counter32
_TmnxPtpClkPktStatsAnnounce_Object = MibTableColumn
tmnxPtpClkPktStatsAnnounce = _TmnxPtpClkPktStatsAnnounce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 2),
    _TmnxPtpClkPktStatsAnnounce_Type()
)
tmnxPtpClkPktStatsAnnounce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsAnnounce.setStatus("current")
_TmnxPtpClkPktStatsSync_Type = Counter32
_TmnxPtpClkPktStatsSync_Object = MibTableColumn
tmnxPtpClkPktStatsSync = _TmnxPtpClkPktStatsSync_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 3),
    _TmnxPtpClkPktStatsSync_Type()
)
tmnxPtpClkPktStatsSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsSync.setStatus("current")
_TmnxPtpClkPktStatsFollowUp_Type = Counter32
_TmnxPtpClkPktStatsFollowUp_Object = MibTableColumn
tmnxPtpClkPktStatsFollowUp = _TmnxPtpClkPktStatsFollowUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 4),
    _TmnxPtpClkPktStatsFollowUp_Type()
)
tmnxPtpClkPktStatsFollowUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsFollowUp.setStatus("current")
_TmnxPtpClkPktStatsDelayRequest_Type = Counter32
_TmnxPtpClkPktStatsDelayRequest_Object = MibTableColumn
tmnxPtpClkPktStatsDelayRequest = _TmnxPtpClkPktStatsDelayRequest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 5),
    _TmnxPtpClkPktStatsDelayRequest_Type()
)
tmnxPtpClkPktStatsDelayRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsDelayRequest.setStatus("current")
_TmnxPtpClkPktStatsDelayResp_Type = Counter32
_TmnxPtpClkPktStatsDelayResp_Object = MibTableColumn
tmnxPtpClkPktStatsDelayResp = _TmnxPtpClkPktStatsDelayResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 6),
    _TmnxPtpClkPktStatsDelayResp_Type()
)
tmnxPtpClkPktStatsDelayResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsDelayResp.setStatus("current")
_TmnxPtpClkPktStatsSignaling_Type = Counter32
_TmnxPtpClkPktStatsSignaling_Object = MibTableColumn
tmnxPtpClkPktStatsSignaling = _TmnxPtpClkPktStatsSignaling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 7),
    _TmnxPtpClkPktStatsSignaling_Type()
)
tmnxPtpClkPktStatsSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsSignaling.setStatus("current")
_TmnxPtpClkPktStatsOther_Type = Counter32
_TmnxPtpClkPktStatsOther_Object = MibTableColumn
tmnxPtpClkPktStatsOther = _TmnxPtpClkPktStatsOther_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 8),
    _TmnxPtpClkPktStatsOther_Type()
)
tmnxPtpClkPktStatsOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsOther.setStatus("current")
_TmnxPtpClkPktStatsUniReqAnno_Type = Counter32
_TmnxPtpClkPktStatsUniReqAnno_Object = MibTableColumn
tmnxPtpClkPktStatsUniReqAnno = _TmnxPtpClkPktStatsUniReqAnno_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 9),
    _TmnxPtpClkPktStatsUniReqAnno_Type()
)
tmnxPtpClkPktStatsUniReqAnno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsUniReqAnno.setStatus("current")
_TmnxPtpClkPktStatsUniReqSync_Type = Counter32
_TmnxPtpClkPktStatsUniReqSync_Object = MibTableColumn
tmnxPtpClkPktStatsUniReqSync = _TmnxPtpClkPktStatsUniReqSync_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 10),
    _TmnxPtpClkPktStatsUniReqSync_Type()
)
tmnxPtpClkPktStatsUniReqSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsUniReqSync.setStatus("current")
_TmnxPtpClkPktStatsUniReqDelayRsp_Type = Counter32
_TmnxPtpClkPktStatsUniReqDelayRsp_Object = MibTableColumn
tmnxPtpClkPktStatsUniReqDelayRsp = _TmnxPtpClkPktStatsUniReqDelayRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 11),
    _TmnxPtpClkPktStatsUniReqDelayRsp_Type()
)
tmnxPtpClkPktStatsUniReqDelayRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsUniReqDelayRsp.setStatus("current")
_TmnxPtpClkPktStatsUniGrantAnno_Type = Counter32
_TmnxPtpClkPktStatsUniGrantAnno_Object = MibTableColumn
tmnxPtpClkPktStatsUniGrantAnno = _TmnxPtpClkPktStatsUniGrantAnno_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 12),
    _TmnxPtpClkPktStatsUniGrantAnno_Type()
)
tmnxPtpClkPktStatsUniGrantAnno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsUniGrantAnno.setStatus("current")
_TmnxPtpClkPktStatsUniGrantSync_Type = Counter32
_TmnxPtpClkPktStatsUniGrantSync_Object = MibTableColumn
tmnxPtpClkPktStatsUniGrantSync = _TmnxPtpClkPktStatsUniGrantSync_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 13),
    _TmnxPtpClkPktStatsUniGrantSync_Type()
)
tmnxPtpClkPktStatsUniGrantSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsUniGrantSync.setStatus("current")
_TmnxPtpClkPktStatsUniGrantDelRsp_Type = Counter32
_TmnxPtpClkPktStatsUniGrantDelRsp_Object = MibTableColumn
tmnxPtpClkPktStatsUniGrantDelRsp = _TmnxPtpClkPktStatsUniGrantDelRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 14),
    _TmnxPtpClkPktStatsUniGrantDelRsp_Type()
)
tmnxPtpClkPktStatsUniGrantDelRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsUniGrantDelRsp.setStatus("current")
_TmnxPtpClkPktStatsUniDenyAnno_Type = Counter32
_TmnxPtpClkPktStatsUniDenyAnno_Object = MibTableColumn
tmnxPtpClkPktStatsUniDenyAnno = _TmnxPtpClkPktStatsUniDenyAnno_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 15),
    _TmnxPtpClkPktStatsUniDenyAnno_Type()
)
tmnxPtpClkPktStatsUniDenyAnno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsUniDenyAnno.setStatus("current")
_TmnxPtpClkPktStatsUniDenySync_Type = Counter32
_TmnxPtpClkPktStatsUniDenySync_Object = MibTableColumn
tmnxPtpClkPktStatsUniDenySync = _TmnxPtpClkPktStatsUniDenySync_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 16),
    _TmnxPtpClkPktStatsUniDenySync_Type()
)
tmnxPtpClkPktStatsUniDenySync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsUniDenySync.setStatus("current")
_TmnxPtpClkPktStatsUniDenyDelRsp_Type = Counter32
_TmnxPtpClkPktStatsUniDenyDelRsp_Object = MibTableColumn
tmnxPtpClkPktStatsUniDenyDelRsp = _TmnxPtpClkPktStatsUniDenyDelRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 17),
    _TmnxPtpClkPktStatsUniDenyDelRsp_Type()
)
tmnxPtpClkPktStatsUniDenyDelRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsUniDenyDelRsp.setStatus("current")
_TmnxPtpClkPktStatsUniCancelAnno_Type = Counter32
_TmnxPtpClkPktStatsUniCancelAnno_Object = MibTableColumn
tmnxPtpClkPktStatsUniCancelAnno = _TmnxPtpClkPktStatsUniCancelAnno_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 18),
    _TmnxPtpClkPktStatsUniCancelAnno_Type()
)
tmnxPtpClkPktStatsUniCancelAnno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsUniCancelAnno.setStatus("current")
_TmnxPtpClkPktStatsUniCancelSync_Type = Counter32
_TmnxPtpClkPktStatsUniCancelSync_Object = MibTableColumn
tmnxPtpClkPktStatsUniCancelSync = _TmnxPtpClkPktStatsUniCancelSync_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 19),
    _TmnxPtpClkPktStatsUniCancelSync_Type()
)
tmnxPtpClkPktStatsUniCancelSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsUniCancelSync.setStatus("current")
_TmnxPtpClkPktStatsUniCancelDelay_Type = Counter32
_TmnxPtpClkPktStatsUniCancelDelay_Object = MibTableColumn
tmnxPtpClkPktStatsUniCancelDelay = _TmnxPtpClkPktStatsUniCancelDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 20),
    _TmnxPtpClkPktStatsUniCancelDelay_Type()
)
tmnxPtpClkPktStatsUniCancelDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsUniCancelDelay.setStatus("current")
_TmnxPtpClkPktStatsUniAckCnclAnno_Type = Counter32
_TmnxPtpClkPktStatsUniAckCnclAnno_Object = MibTableColumn
tmnxPtpClkPktStatsUniAckCnclAnno = _TmnxPtpClkPktStatsUniAckCnclAnno_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 21),
    _TmnxPtpClkPktStatsUniAckCnclAnno_Type()
)
tmnxPtpClkPktStatsUniAckCnclAnno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsUniAckCnclAnno.setStatus("current")
_TmnxPtpClkPktStatsUniAckCnclSync_Type = Counter32
_TmnxPtpClkPktStatsUniAckCnclSync_Object = MibTableColumn
tmnxPtpClkPktStatsUniAckCnclSync = _TmnxPtpClkPktStatsUniAckCnclSync_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 22),
    _TmnxPtpClkPktStatsUniAckCnclSync_Type()
)
tmnxPtpClkPktStatsUniAckCnclSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsUniAckCnclSync.setStatus("current")
_TmnxPtpClkPktStatsUniAckCnclDly_Type = Counter32
_TmnxPtpClkPktStatsUniAckCnclDly_Object = MibTableColumn
tmnxPtpClkPktStatsUniAckCnclDly = _TmnxPtpClkPktStatsUniAckCnclDly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 23),
    _TmnxPtpClkPktStatsUniAckCnclDly_Type()
)
tmnxPtpClkPktStatsUniAckCnclDly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsUniAckCnclDly.setStatus("current")
_TmnxPtpClkPktStatsOtherTLVs_Type = Counter32
_TmnxPtpClkPktStatsOtherTLVs_Object = MibTableColumn
tmnxPtpClkPktStatsOtherTLVs = _TmnxPtpClkPktStatsOtherTLVs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 24),
    _TmnxPtpClkPktStatsOtherTLVs_Type()
)
tmnxPtpClkPktStatsOtherTLVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsOtherTLVs.setStatus("current")
_TmnxPtpClkPktStatsDropBadDomain_Type = Counter32
_TmnxPtpClkPktStatsDropBadDomain_Object = MibTableColumn
tmnxPtpClkPktStatsDropBadDomain = _TmnxPtpClkPktStatsDropBadDomain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 25),
    _TmnxPtpClkPktStatsDropBadDomain_Type()
)
tmnxPtpClkPktStatsDropBadDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsDropBadDomain.setStatus("current")
_TmnxPtpClkPktStatsDropAltMaster_Type = Counter32
_TmnxPtpClkPktStatsDropAltMaster_Object = MibTableColumn
tmnxPtpClkPktStatsDropAltMaster = _TmnxPtpClkPktStatsDropAltMaster_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 26),
    _TmnxPtpClkPktStatsDropAltMaster_Type()
)
tmnxPtpClkPktStatsDropAltMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsDropAltMaster.setStatus("current")
_TmnxPtpClkPktStatsDropOther_Type = Counter32
_TmnxPtpClkPktStatsDropOther_Object = MibTableColumn
tmnxPtpClkPktStatsDropOther = _TmnxPtpClkPktStatsDropOther_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 27),
    _TmnxPtpClkPktStatsDropOther_Type()
)
tmnxPtpClkPktStatsDropOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsDropOther.setStatus("current")
_TmnxPtpClkPktStatsTimeStampPort_Type = Counter32
_TmnxPtpClkPktStatsTimeStampPort_Object = MibTableColumn
tmnxPtpClkPktStatsTimeStampPort = _TmnxPtpClkPktStatsTimeStampPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 28),
    _TmnxPtpClkPktStatsTimeStampPort_Type()
)
tmnxPtpClkPktStatsTimeStampPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsTimeStampPort.setStatus("current")
_TmnxPtpClkPktStatsTimeStampCpm_Type = Counter32
_TmnxPtpClkPktStatsTimeStampCpm_Object = MibTableColumn
tmnxPtpClkPktStatsTimeStampCpm = _TmnxPtpClkPktStatsTimeStampCpm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 29),
    _TmnxPtpClkPktStatsTimeStampCpm_Type()
)
tmnxPtpClkPktStatsTimeStampCpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsTimeStampCpm.setStatus("current")
_TmnxPtpClkPktStatsDropOutOfSeq_Type = Counter32
_TmnxPtpClkPktStatsDropOutOfSeq_Object = MibTableColumn
tmnxPtpClkPktStatsDropOutOfSeq = _TmnxPtpClkPktStatsDropOutOfSeq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 30),
    _TmnxPtpClkPktStatsDropOutOfSeq_Type()
)
tmnxPtpClkPktStatsDropOutOfSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsDropOutOfSeq.setStatus("current")
_TmnxPtpClkPktStatsDropPeerShut_Type = Counter32
_TmnxPtpClkPktStatsDropPeerShut_Object = MibTableColumn
tmnxPtpClkPktStatsDropPeerShut = _TmnxPtpClkPktStatsDropPeerShut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 1, 1, 31),
    _TmnxPtpClkPktStatsDropPeerShut_Type()
)
tmnxPtpClkPktStatsDropPeerShut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClkPktStatsDropPeerShut.setStatus("current")
_TmnxPtpPeerPacketStatsTable_Object = MibTable
tmnxPtpPeerPacketStatsTable = _TmnxPtpPeerPacketStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2)
)
if mibBuilder.loadTexts:
    tmnxPtpPeerPacketStatsTable.setStatus("current")
_TmnxPtpPeerPacketStatsEntry_Object = MibTableRow
tmnxPtpPeerPacketStatsEntry = _TmnxPtpPeerPacketStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1)
)
tmnxPtpPeerPacketStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PTP-MIB", "tmnxPtpPeerIpAddrType"),
    (0, "TIMETRA-PTP-MIB", "tmnxPtpPeerIpAddress"),
    (0, "TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatDirection"),
)
if mibBuilder.loadTexts:
    tmnxPtpPeerPacketStatsEntry.setStatus("current")
_TmnxPtpPeerPktStatDirection_Type = TmnxPtpDirection
_TmnxPtpPeerPktStatDirection_Object = MibTableColumn
tmnxPtpPeerPktStatDirection = _TmnxPtpPeerPktStatDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 1),
    _TmnxPtpPeerPktStatDirection_Type()
)
tmnxPtpPeerPktStatDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatDirection.setStatus("current")
_TmnxPtpPeerPktStatAnnounce_Type = Counter32
_TmnxPtpPeerPktStatAnnounce_Object = MibTableColumn
tmnxPtpPeerPktStatAnnounce = _TmnxPtpPeerPktStatAnnounce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 2),
    _TmnxPtpPeerPktStatAnnounce_Type()
)
tmnxPtpPeerPktStatAnnounce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatAnnounce.setStatus("current")
_TmnxPtpPeerPktStatSync_Type = Counter32
_TmnxPtpPeerPktStatSync_Object = MibTableColumn
tmnxPtpPeerPktStatSync = _TmnxPtpPeerPktStatSync_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 3),
    _TmnxPtpPeerPktStatSync_Type()
)
tmnxPtpPeerPktStatSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatSync.setStatus("current")
_TmnxPtpPeerPktStatFollowUp_Type = Counter32
_TmnxPtpPeerPktStatFollowUp_Object = MibTableColumn
tmnxPtpPeerPktStatFollowUp = _TmnxPtpPeerPktStatFollowUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 4),
    _TmnxPtpPeerPktStatFollowUp_Type()
)
tmnxPtpPeerPktStatFollowUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatFollowUp.setStatus("current")
_TmnxPtpPeerPktStatDelayRequest_Type = Counter32
_TmnxPtpPeerPktStatDelayRequest_Object = MibTableColumn
tmnxPtpPeerPktStatDelayRequest = _TmnxPtpPeerPktStatDelayRequest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 5),
    _TmnxPtpPeerPktStatDelayRequest_Type()
)
tmnxPtpPeerPktStatDelayRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatDelayRequest.setStatus("current")
_TmnxPtpPeerPktStatDelayResp_Type = Counter32
_TmnxPtpPeerPktStatDelayResp_Object = MibTableColumn
tmnxPtpPeerPktStatDelayResp = _TmnxPtpPeerPktStatDelayResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 6),
    _TmnxPtpPeerPktStatDelayResp_Type()
)
tmnxPtpPeerPktStatDelayResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatDelayResp.setStatus("current")
_TmnxPtpPeerPktStatSignaling_Type = Counter32
_TmnxPtpPeerPktStatSignaling_Object = MibTableColumn
tmnxPtpPeerPktStatSignaling = _TmnxPtpPeerPktStatSignaling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 7),
    _TmnxPtpPeerPktStatSignaling_Type()
)
tmnxPtpPeerPktStatSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatSignaling.setStatus("current")
_TmnxPtpPeerPktStatOther_Type = Counter32
_TmnxPtpPeerPktStatOther_Object = MibTableColumn
tmnxPtpPeerPktStatOther = _TmnxPtpPeerPktStatOther_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 8),
    _TmnxPtpPeerPktStatOther_Type()
)
tmnxPtpPeerPktStatOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatOther.setStatus("current")
_TmnxPtpPeerPktStatUniReqAnno_Type = Counter32
_TmnxPtpPeerPktStatUniReqAnno_Object = MibTableColumn
tmnxPtpPeerPktStatUniReqAnno = _TmnxPtpPeerPktStatUniReqAnno_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 9),
    _TmnxPtpPeerPktStatUniReqAnno_Type()
)
tmnxPtpPeerPktStatUniReqAnno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatUniReqAnno.setStatus("current")
_TmnxPtpPeerPktStatUniReqSync_Type = Counter32
_TmnxPtpPeerPktStatUniReqSync_Object = MibTableColumn
tmnxPtpPeerPktStatUniReqSync = _TmnxPtpPeerPktStatUniReqSync_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 10),
    _TmnxPtpPeerPktStatUniReqSync_Type()
)
tmnxPtpPeerPktStatUniReqSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatUniReqSync.setStatus("current")
_TmnxPtpPeerPktStatUniReqDelayRsp_Type = Counter32
_TmnxPtpPeerPktStatUniReqDelayRsp_Object = MibTableColumn
tmnxPtpPeerPktStatUniReqDelayRsp = _TmnxPtpPeerPktStatUniReqDelayRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 11),
    _TmnxPtpPeerPktStatUniReqDelayRsp_Type()
)
tmnxPtpPeerPktStatUniReqDelayRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatUniReqDelayRsp.setStatus("current")
_TmnxPtpPeerPktStatUniGrantAnno_Type = Counter32
_TmnxPtpPeerPktStatUniGrantAnno_Object = MibTableColumn
tmnxPtpPeerPktStatUniGrantAnno = _TmnxPtpPeerPktStatUniGrantAnno_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 12),
    _TmnxPtpPeerPktStatUniGrantAnno_Type()
)
tmnxPtpPeerPktStatUniGrantAnno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatUniGrantAnno.setStatus("current")
_TmnxPtpPeerPktStatUniGrantSync_Type = Counter32
_TmnxPtpPeerPktStatUniGrantSync_Object = MibTableColumn
tmnxPtpPeerPktStatUniGrantSync = _TmnxPtpPeerPktStatUniGrantSync_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 13),
    _TmnxPtpPeerPktStatUniGrantSync_Type()
)
tmnxPtpPeerPktStatUniGrantSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatUniGrantSync.setStatus("current")
_TmnxPtpPeerPktStatUniGrantDelRsp_Type = Counter32
_TmnxPtpPeerPktStatUniGrantDelRsp_Object = MibTableColumn
tmnxPtpPeerPktStatUniGrantDelRsp = _TmnxPtpPeerPktStatUniGrantDelRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 14),
    _TmnxPtpPeerPktStatUniGrantDelRsp_Type()
)
tmnxPtpPeerPktStatUniGrantDelRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatUniGrantDelRsp.setStatus("current")
_TmnxPtpPeerPktStatUniDenyAnno_Type = Counter32
_TmnxPtpPeerPktStatUniDenyAnno_Object = MibTableColumn
tmnxPtpPeerPktStatUniDenyAnno = _TmnxPtpPeerPktStatUniDenyAnno_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 15),
    _TmnxPtpPeerPktStatUniDenyAnno_Type()
)
tmnxPtpPeerPktStatUniDenyAnno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatUniDenyAnno.setStatus("current")
_TmnxPtpPeerPktStatUniDenySync_Type = Counter32
_TmnxPtpPeerPktStatUniDenySync_Object = MibTableColumn
tmnxPtpPeerPktStatUniDenySync = _TmnxPtpPeerPktStatUniDenySync_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 16),
    _TmnxPtpPeerPktStatUniDenySync_Type()
)
tmnxPtpPeerPktStatUniDenySync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatUniDenySync.setStatus("current")
_TmnxPtpPeerPktStatUniDenyDelRsp_Type = Counter32
_TmnxPtpPeerPktStatUniDenyDelRsp_Object = MibTableColumn
tmnxPtpPeerPktStatUniDenyDelRsp = _TmnxPtpPeerPktStatUniDenyDelRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 17),
    _TmnxPtpPeerPktStatUniDenyDelRsp_Type()
)
tmnxPtpPeerPktStatUniDenyDelRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatUniDenyDelRsp.setStatus("current")
_TmnxPtpPeerPktStatUniCancelAnno_Type = Counter32
_TmnxPtpPeerPktStatUniCancelAnno_Object = MibTableColumn
tmnxPtpPeerPktStatUniCancelAnno = _TmnxPtpPeerPktStatUniCancelAnno_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 18),
    _TmnxPtpPeerPktStatUniCancelAnno_Type()
)
tmnxPtpPeerPktStatUniCancelAnno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatUniCancelAnno.setStatus("current")
_TmnxPtpPeerPktStatUniCancelSync_Type = Counter32
_TmnxPtpPeerPktStatUniCancelSync_Object = MibTableColumn
tmnxPtpPeerPktStatUniCancelSync = _TmnxPtpPeerPktStatUniCancelSync_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 19),
    _TmnxPtpPeerPktStatUniCancelSync_Type()
)
tmnxPtpPeerPktStatUniCancelSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatUniCancelSync.setStatus("current")
_TmnxPtpPeerPktStatUniCancelDelay_Type = Counter32
_TmnxPtpPeerPktStatUniCancelDelay_Object = MibTableColumn
tmnxPtpPeerPktStatUniCancelDelay = _TmnxPtpPeerPktStatUniCancelDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 20),
    _TmnxPtpPeerPktStatUniCancelDelay_Type()
)
tmnxPtpPeerPktStatUniCancelDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatUniCancelDelay.setStatus("current")
_TmnxPtpPeerPktStatUniAckCnclAnno_Type = Counter32
_TmnxPtpPeerPktStatUniAckCnclAnno_Object = MibTableColumn
tmnxPtpPeerPktStatUniAckCnclAnno = _TmnxPtpPeerPktStatUniAckCnclAnno_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 21),
    _TmnxPtpPeerPktStatUniAckCnclAnno_Type()
)
tmnxPtpPeerPktStatUniAckCnclAnno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatUniAckCnclAnno.setStatus("current")
_TmnxPtpPeerPktStatUniAckCnclSync_Type = Counter32
_TmnxPtpPeerPktStatUniAckCnclSync_Object = MibTableColumn
tmnxPtpPeerPktStatUniAckCnclSync = _TmnxPtpPeerPktStatUniAckCnclSync_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 22),
    _TmnxPtpPeerPktStatUniAckCnclSync_Type()
)
tmnxPtpPeerPktStatUniAckCnclSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatUniAckCnclSync.setStatus("current")
_TmnxPtpPeerPktStatUniAckCnclDly_Type = Counter32
_TmnxPtpPeerPktStatUniAckCnclDly_Object = MibTableColumn
tmnxPtpPeerPktStatUniAckCnclDly = _TmnxPtpPeerPktStatUniAckCnclDly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 23),
    _TmnxPtpPeerPktStatUniAckCnclDly_Type()
)
tmnxPtpPeerPktStatUniAckCnclDly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatUniAckCnclDly.setStatus("current")
_TmnxPtpPeerPktStatOtherTLVs_Type = Counter32
_TmnxPtpPeerPktStatOtherTLVs_Object = MibTableColumn
tmnxPtpPeerPktStatOtherTLVs = _TmnxPtpPeerPktStatOtherTLVs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 24),
    _TmnxPtpPeerPktStatOtherTLVs_Type()
)
tmnxPtpPeerPktStatOtherTLVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatOtherTLVs.setStatus("current")
_TmnxPtpPeerPktStatDropBadDomain_Type = Counter32
_TmnxPtpPeerPktStatDropBadDomain_Object = MibTableColumn
tmnxPtpPeerPktStatDropBadDomain = _TmnxPtpPeerPktStatDropBadDomain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 25),
    _TmnxPtpPeerPktStatDropBadDomain_Type()
)
tmnxPtpPeerPktStatDropBadDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatDropBadDomain.setStatus("current")
_TmnxPtpPeerPktStatDropAltMaster_Type = Counter32
_TmnxPtpPeerPktStatDropAltMaster_Object = MibTableColumn
tmnxPtpPeerPktStatDropAltMaster = _TmnxPtpPeerPktStatDropAltMaster_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 26),
    _TmnxPtpPeerPktStatDropAltMaster_Type()
)
tmnxPtpPeerPktStatDropAltMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatDropAltMaster.setStatus("current")
_TmnxPtpPeerPktStatDropOther_Type = Counter32
_TmnxPtpPeerPktStatDropOther_Object = MibTableColumn
tmnxPtpPeerPktStatDropOther = _TmnxPtpPeerPktStatDropOther_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 27),
    _TmnxPtpPeerPktStatDropOther_Type()
)
tmnxPtpPeerPktStatDropOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatDropOther.setStatus("current")
_TmnxPtpPeerPktStatTimeStampPort_Type = Counter32
_TmnxPtpPeerPktStatTimeStampPort_Object = MibTableColumn
tmnxPtpPeerPktStatTimeStampPort = _TmnxPtpPeerPktStatTimeStampPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 28),
    _TmnxPtpPeerPktStatTimeStampPort_Type()
)
tmnxPtpPeerPktStatTimeStampPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatTimeStampPort.setStatus("current")
_TmnxPtpPeerPktStatTimeStampCpm_Type = Counter32
_TmnxPtpPeerPktStatTimeStampCpm_Object = MibTableColumn
tmnxPtpPeerPktStatTimeStampCpm = _TmnxPtpPeerPktStatTimeStampCpm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 29),
    _TmnxPtpPeerPktStatTimeStampCpm_Type()
)
tmnxPtpPeerPktStatTimeStampCpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatTimeStampCpm.setStatus("current")
_TmnxPtpPeerPktStatDropOutOfSeq_Type = Counter32
_TmnxPtpPeerPktStatDropOutOfSeq_Object = MibTableColumn
tmnxPtpPeerPktStatDropOutOfSeq = _TmnxPtpPeerPktStatDropOutOfSeq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 30),
    _TmnxPtpPeerPktStatDropOutOfSeq_Type()
)
tmnxPtpPeerPktStatDropOutOfSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatDropOutOfSeq.setStatus("current")
_TmnxPtpPeerPktStatDropPeerShut_Type = Counter32
_TmnxPtpPeerPktStatDropPeerShut_Object = MibTableColumn
tmnxPtpPeerPktStatDropPeerShut = _TmnxPtpPeerPktStatDropPeerShut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 2, 1, 31),
    _TmnxPtpPeerPktStatDropPeerShut_Type()
)
tmnxPtpPeerPktStatDropPeerShut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpPeerPktStatDropPeerShut.setStatus("current")
_TmnxPtpClockRecoveryStatistics_ObjectIdentity = ObjectIdentity
tmnxPtpClockRecoveryStatistics = _TmnxPtpClockRecoveryStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 3)
)
_TmnxPtpClockRecStatsInitial_Type = Unsigned32
_TmnxPtpClockRecStatsInitial_Object = MibScalar
tmnxPtpClockRecStatsInitial = _TmnxPtpClockRecStatsInitial_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 3, 1),
    _TmnxPtpClockRecStatsInitial_Type()
)
tmnxPtpClockRecStatsInitial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockRecStatsInitial.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPtpClockRecStatsInitial.setUnits("seconds")
_TmnxPtpClockRecStatsAcquiring_Type = Unsigned32
_TmnxPtpClockRecStatsAcquiring_Object = MibScalar
tmnxPtpClockRecStatsAcquiring = _TmnxPtpClockRecStatsAcquiring_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 3, 2),
    _TmnxPtpClockRecStatsAcquiring_Type()
)
tmnxPtpClockRecStatsAcquiring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockRecStatsAcquiring.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPtpClockRecStatsAcquiring.setUnits("seconds")
_TmnxPtpClockRecStatsPhaseTrack_Type = Unsigned32
_TmnxPtpClockRecStatsPhaseTrack_Object = MibScalar
tmnxPtpClockRecStatsPhaseTrack = _TmnxPtpClockRecStatsPhaseTrack_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 3, 3),
    _TmnxPtpClockRecStatsPhaseTrack_Type()
)
tmnxPtpClockRecStatsPhaseTrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockRecStatsPhaseTrack.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPtpClockRecStatsPhaseTrack.setUnits("seconds")
_TmnxPtpClockRecStatsLocked_Type = Unsigned32
_TmnxPtpClockRecStatsLocked_Object = MibScalar
tmnxPtpClockRecStatsLocked = _TmnxPtpClockRecStatsLocked_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 3, 4),
    _TmnxPtpClockRecStatsLocked_Type()
)
tmnxPtpClockRecStatsLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockRecStatsLocked.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPtpClockRecStatsLocked.setUnits("seconds")
_TmnxPtpClockRecStatsHoldover_Type = Unsigned32
_TmnxPtpClockRecStatsHoldover_Object = MibScalar
tmnxPtpClockRecStatsHoldover = _TmnxPtpClockRecStatsHoldover_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 3, 5),
    _TmnxPtpClockRecStatsHoldover_Type()
)
tmnxPtpClockRecStatsHoldover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockRecStatsHoldover.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPtpClockRecStatsHoldover.setUnits("seconds")
_TmnxPtpClockRecStatsSyncPktLoss_Type = Counter32
_TmnxPtpClockRecStatsSyncPktLoss_Object = MibScalar
tmnxPtpClockRecStatsSyncPktLoss = _TmnxPtpClockRecStatsSyncPktLoss_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 3, 6),
    _TmnxPtpClockRecStatsSyncPktLoss_Type()
)
tmnxPtpClockRecStatsSyncPktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockRecStatsSyncPktLoss.setStatus("current")
_TmnxPtpClockRecStatsSyncHiPktLss_Type = Counter32
_TmnxPtpClockRecStatsSyncHiPktLss_Object = MibScalar
tmnxPtpClockRecStatsSyncHiPktLss = _TmnxPtpClockRecStatsSyncHiPktLss_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 3, 7),
    _TmnxPtpClockRecStatsSyncHiPktLss_Type()
)
tmnxPtpClockRecStatsSyncHiPktLss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockRecStatsSyncHiPktLss.setStatus("current")
_TmnxPtpClockRecStatsSyncStep_Type = Counter32
_TmnxPtpClockRecStatsSyncStep_Object = MibScalar
tmnxPtpClockRecStatsSyncStep = _TmnxPtpClockRecStatsSyncStep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 3, 8),
    _TmnxPtpClockRecStatsSyncStep_Type()
)
tmnxPtpClockRecStatsSyncStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockRecStatsSyncStep.setStatus("current")
_TmnxPtpClockRecStatsSyncHighPDV_Type = Counter32
_TmnxPtpClockRecStatsSyncHighPDV_Object = MibScalar
tmnxPtpClockRecStatsSyncHighPDV = _TmnxPtpClockRecStatsSyncHighPDV_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 3, 9),
    _TmnxPtpClockRecStatsSyncHighPDV_Type()
)
tmnxPtpClockRecStatsSyncHighPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockRecStatsSyncHighPDV.setStatus("current")
_TmnxPtpClockRecStatsDlyPktLoss_Type = Counter32
_TmnxPtpClockRecStatsDlyPktLoss_Object = MibScalar
tmnxPtpClockRecStatsDlyPktLoss = _TmnxPtpClockRecStatsDlyPktLoss_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 3, 10),
    _TmnxPtpClockRecStatsDlyPktLoss_Type()
)
tmnxPtpClockRecStatsDlyPktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockRecStatsDlyPktLoss.setStatus("current")
_TmnxPtpClockRecStatsDlyHiPktLss_Type = Counter32
_TmnxPtpClockRecStatsDlyHiPktLss_Object = MibScalar
tmnxPtpClockRecStatsDlyHiPktLss = _TmnxPtpClockRecStatsDlyHiPktLss_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 3, 11),
    _TmnxPtpClockRecStatsDlyHiPktLss_Type()
)
tmnxPtpClockRecStatsDlyHiPktLss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockRecStatsDlyHiPktLss.setStatus("current")
_TmnxPtpClockRecStatsDlyStep_Type = Counter32
_TmnxPtpClockRecStatsDlyStep_Object = MibScalar
tmnxPtpClockRecStatsDlyStep = _TmnxPtpClockRecStatsDlyStep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 3, 12),
    _TmnxPtpClockRecStatsDlyStep_Type()
)
tmnxPtpClockRecStatsDlyStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockRecStatsDlyStep.setStatus("current")
_TmnxPtpClockRecStatsDlyHighPDV_Type = Counter32
_TmnxPtpClockRecStatsDlyHighPDV_Object = MibScalar
tmnxPtpClockRecStatsDlyHighPDV = _TmnxPtpClockRecStatsDlyHighPDV_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 5, 3, 13),
    _TmnxPtpClockRecStatsDlyHighPDV_Type()
)
tmnxPtpClockRecStatsDlyHighPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPtpClockRecStatsDlyHighPDV.setStatus("current")
_TmnxPtp1588NotifyObjects_ObjectIdentity = ObjectIdentity
tmnxPtp1588NotifyObjects = _TmnxPtp1588NotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 10)
)
_TmnxPtpMasterClockLastIpAddrType_Type = InetAddressType
_TmnxPtpMasterClockLastIpAddrType_Object = MibScalar
tmnxPtpMasterClockLastIpAddrType = _TmnxPtpMasterClockLastIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 10, 1),
    _TmnxPtpMasterClockLastIpAddrType_Type()
)
tmnxPtpMasterClockLastIpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPtpMasterClockLastIpAddrType.setStatus("current")


class _TmnxPtpMasterClockLastIpAddress_Type(InetAddress):
    """Custom type tmnxPtpMasterClockLastIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxPtpMasterClockLastIpAddress_Type.__name__ = "InetAddress"
_TmnxPtpMasterClockLastIpAddress_Object = MibScalar
tmnxPtpMasterClockLastIpAddress = _TmnxPtpMasterClockLastIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 10, 2),
    _TmnxPtpMasterClockLastIpAddress_Type()
)
tmnxPtpMasterClockLastIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPtpMasterClockLastIpAddress.setStatus("current")
_TmnxPtpNotifyRowPointer_Type = RowPointer
_TmnxPtpNotifyRowPointer_Object = MibScalar
tmnxPtpNotifyRowPointer = _TmnxPtpNotifyRowPointer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 10, 3),
    _TmnxPtpNotifyRowPointer_Type()
)
tmnxPtpNotifyRowPointer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPtpNotifyRowPointer.setStatus("current")
_TmnxPtpNotifyRowDescription_Type = TItemDescription
_TmnxPtpNotifyRowDescription_Object = MibScalar
tmnxPtpNotifyRowDescription = _TmnxPtpNotifyRowDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 74, 10, 4),
    _TmnxPtpNotifyRowDescription_Type()
)
tmnxPtpNotifyRowDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPtpNotifyRowDescription.setStatus("current")
_TmnxPtp1588NotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxPtp1588NotifyPrefix = _TmnxPtp1588NotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 74)
)
_TmnxPtp1588Notifications_ObjectIdentity = ObjectIdentity
tmnxPtp1588Notifications = _TmnxPtp1588Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 74, 0)
)
vRtrIfEntry.registerAugmentions(
    ("TIMETRA-PTP-MIB",
     "tmnxPtpVRtrIfEntry")
)
tmnxPtpVRtrIfEntry.setIndexNames(*vRtrIfEntry.getIndexNames())
tmnxCpmCardEntry.registerAugmentions(
    ("TIMETRA-PTP-MIB",
     "tmnxPtpClockOperEntry")
)
tmnxPtpClockOperEntry.setIndexNames(*tmnxCpmCardEntry.getIndexNames())

# Managed Objects groups

tmnxPtpTimeStampGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 1, 1)
)
tmnxPtpTimeStampGroup.setObjects(
    ("TIMETRA-PTP-MIB", "tmnxPtpPeerConfigTblLastChanged")
)
if mibBuilder.loadTexts:
    tmnxPtpTimeStampGroup.setStatus("current")

tmnxPtpLocalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 1, 2)
)
tmnxPtpLocalConfigGroup.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpClockAdminState"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockClockType"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockProfile"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockDomain"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockPriority1"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockPriority2"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockNetworkType"))
)
if mibBuilder.loadTexts:
    tmnxPtpLocalConfigGroup.setStatus("current")

tmnxPtpLocalOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 1, 3)
)
tmnxPtpLocalOperGroup.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpClockIdentity"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockOperState"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockStepType"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockClass"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockAccuracy"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockVariance"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockPortState"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockPortStateLastChanged"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockRecoveryState"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockRecoveryStateLastChg"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockFrequencyOffset"))
)
if mibBuilder.loadTexts:
    tmnxPtpLocalOperGroup.setStatus("current")

tmnxPtpMasterClockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 1, 4)
)
tmnxPtpMasterClockGroup.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpMasterClockAddressType"),
        ("TIMETRA-PTP-MIB", "tmnxPtpMasterClockAddress"),
        ("TIMETRA-PTP-MIB", "tmnxPtpMasterClockGMClockId"),
        ("TIMETRA-PTP-MIB", "tmnxPtpMasterClockGMClockPrio1"),
        ("TIMETRA-PTP-MIB", "tmnxPtpMasterClockGMClockPrio2"),
        ("TIMETRA-PTP-MIB", "tmnxPtpMasterClockGMClockClass"),
        ("TIMETRA-PTP-MIB", "tmnxPtpMasterClockGMAccuracy"),
        ("TIMETRA-PTP-MIB", "tmnxPtpMasterClockGMVariance"),
        ("TIMETRA-PTP-MIB", "tmnxPtpMasterClockParentClockId"),
        ("TIMETRA-PTP-MIB", "tmnxPtpMasterClockParentPortNum"))
)
if mibBuilder.loadTexts:
    tmnxPtpMasterClockGroup.setStatus("current")

tmnxPtpPeerBaseConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 1, 5)
)
tmnxPtpPeerBaseConfigGroup.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpPeerRowStatus"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerLastChanged"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerAdminState"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPortState"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerLocalPriority"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerRemoteMaster"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerRemoteSlave"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerClockId"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerLocalPortNumber"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerRemotePortNumber"))
)
if mibBuilder.loadTexts:
    tmnxPtpPeerBaseConfigGroup.setStatus("current")

tmnxPtpPeerMasterStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 1, 6)
)
tmnxPtpPeerMasterStatusGroup.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpPeerMasterCurrentMaster"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerMasterClockStepType"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerMasterClockStepsRemvd"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerMasterGMClockId"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerMasterGMClockPrio1"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerMasterGMClockPrio2"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerMasterGMClockClass"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerMasterGMClockAccuracy"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerMasterGMClockVariance"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerMasterAlarm"))
)
if mibBuilder.loadTexts:
    tmnxPtpPeerMasterStatusGroup.setStatus("current")

tmnxPtpPacketStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 1, 7)
)
tmnxPtpPacketStatsGroup.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsAnnounce"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsSync"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsFollowUp"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsDelayRequest"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsDelayResp"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsSignaling"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsOther"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsUniReqAnno"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsUniReqSync"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsUniReqDelayRsp"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsUniGrantAnno"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsUniGrantSync"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsUniGrantDelRsp"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsUniDenyAnno"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsUniDenySync"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsUniDenyDelRsp"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsUniCancelAnno"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsUniCancelSync"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsUniCancelDelay"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsUniAckCnclAnno"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsUniAckCnclSync"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsUniAckCnclDly"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsOtherTLVs"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsDropBadDomain"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsDropAltMaster"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsDropOther"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsDropOutOfSeq"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsDropPeerShut"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatAnnounce"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatSync"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatFollowUp"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatDelayRequest"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatDelayResp"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatSignaling"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatOther"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatUniReqAnno"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatUniReqSync"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatUniReqDelayRsp"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatUniGrantAnno"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatUniGrantSync"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatUniGrantDelRsp"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatUniDenyAnno"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatUniDenySync"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatUniDenyDelRsp"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatUniCancelAnno"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatUniCancelSync"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatUniCancelDelay"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatUniAckCnclAnno"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatUniAckCnclSync"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatUniAckCnclDly"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatOtherTLVs"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatDropBadDomain"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatDropAltMaster"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatDropOther"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatDropOutOfSeq"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatDropPeerShut"))
)
if mibBuilder.loadTexts:
    tmnxPtpPacketStatsGroup.setStatus("current")

tmnxPtpClockRecoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 1, 8)
)
tmnxPtpClockRecoveryGroup.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpClockRecStatsInitial"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockRecStatsAcquiring"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockRecStatsPhaseTrack"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockRecStatsLocked"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockRecStatsHoldover"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockRecStatsSyncPktLoss"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockRecStatsSyncHiPktLss"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockRecStatsSyncStep"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockRecStatsSyncHighPDV"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockRecStatsDlyPktLoss"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockRecStatsDlyHiPktLss"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockRecStatsDlyStep"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockRecStatsDlyHighPDV"))
)
if mibBuilder.loadTexts:
    tmnxPtpClockRecoveryGroup.setStatus("current")

tmnxPtpPeerUnicastStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 1, 9)
)
tmnxPtpPeerUnicastStatusGroup.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpPeerUnicastStatus"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerUnicastRate"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerUnicastDuration"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerUnicastEventTime"))
)
if mibBuilder.loadTexts:
    tmnxPtpPeerUnicastStatusGroup.setStatus("current")

tmnxPtpNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 1, 10)
)
tmnxPtpNotifyObjsGroup.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpMasterClockLastIpAddrType"),
        ("TIMETRA-PTP-MIB", "tmnxPtpMasterClockLastIpAddress"),
        ("TIMETRA-PTP-MIB", "tmnxPtpNotifyRowPointer"),
        ("TIMETRA-PTP-MIB", "tmnxPtpNotifyRowDescription"))
)
if mibBuilder.loadTexts:
    tmnxPtpNotifyObjsGroup.setStatus("current")

tmnxPtpVRtrIfTimeStampGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 2, 1)
)
tmnxPtpVRtrIfTimeStampGroup.setObjects(
    ("TIMETRA-PTP-MIB", "tmnxPtpVRtrIfTableLastChanged")
)
if mibBuilder.loadTexts:
    tmnxPtpVRtrIfTimeStampGroup.setStatus("current")

tmnxPtpVRtrIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 2, 2)
)
tmnxPtpVRtrIfConfigGroup.setObjects(
    ("TIMETRA-PTP-MIB", "tmnxPtpVRtrIfAdminState")
)
if mibBuilder.loadTexts:
    tmnxPtpVRtrIfConfigGroup.setStatus("current")

tmnxPtpTimeInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 2, 3)
)
tmnxPtpTimeInfoGroup.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpTimeInfoTimescale"),
        ("TIMETRA-PTP-MIB", "tmnxPtpTimeInfoCurrentTime"),
        ("TIMETRA-PTP-MIB", "tmnxPtpTimeInfoFreqTraceable"),
        ("TIMETRA-PTP-MIB", "tmnxPtpTimeInfoTimeTraceable"),
        ("TIMETRA-PTP-MIB", "tmnxPtpTimeInfoTimeSource"))
)
if mibBuilder.loadTexts:
    tmnxPtpTimeInfoGroup.setStatus("current")

tmnxPtpPeerOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 2, 5)
)
tmnxPtpPeerOperGroup.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpPeerTxTimeStampPoint"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerLastTxPortId"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerLastTxPortEncapType"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerLastTxPortEncapValue"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerRxTimeStampPoint"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerLastRxPortId"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerLastRxPortEncapType"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerLastRxPortEncapValue"))
)
if mibBuilder.loadTexts:
    tmnxPtpPeerOperGroup.setStatus("current")

tmnxPtpPacketStatsV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 2, 6)
)
tmnxPtpPacketStatsV10v0Group.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsTimeStampPort"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClkPktStatsTimeStampCpm"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatTimeStampPort"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerPktStatTimeStampCpm"))
)
if mibBuilder.loadTexts:
    tmnxPtpPacketStatsV10v0Group.setStatus("current")

tmnxPtpVRtrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 3, 1)
)
tmnxPtpVRtrGroup.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpVRtrTableLastChanged"),
        ("TIMETRA-PTP-MIB", "tmnxPtpVRtrRowStatus"),
        ("TIMETRA-PTP-MIB", "tmnxPtpVRtrLastChanged"),
        ("TIMETRA-PTP-MIB", "tmnxPtpVRtrAdminState"),
        ("TIMETRA-PTP-MIB", "tmnxPtpVRtrOperState"),
        ("TIMETRA-PTP-MIB", "tmnxPtpVRtrPeerLimit"))
)
if mibBuilder.loadTexts:
    tmnxPtpVRtrGroup.setStatus("current")

tmnxPtpLocalConfigV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 4, 1)
)
tmnxPtpLocalConfigV12v0Group.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpClockAnnounceInterval"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockAnnoRxTimeout"))
)
if mibBuilder.loadTexts:
    tmnxPtpLocalConfigV12v0Group.setStatus("current")

tmnxPtpPeerBaseConfigV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 4, 2)
)
tmnxPtpPeerBaseConfigV12v0Group.setObjects(
    ("TIMETRA-PTP-MIB", "tmnxPtpPeerSyncInterval")
)
if mibBuilder.loadTexts:
    tmnxPtpPeerBaseConfigV12v0Group.setStatus("current")


# Notification objects

tmnxPtpCardNotSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 74, 0, 1)
)
tmnxPtpCardNotSupported.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxCpmCardOscillatorType"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockClockType"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockAdminState"))
)
if mibBuilder.loadTexts:
    tmnxPtpCardNotSupported.setStatus(
        "current"
    )

tmnxPtpCardNotSupportedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 74, 0, 2)
)
tmnxPtpCardNotSupportedClear.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxCpmCardOscillatorType"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockClockType"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockAdminState"))
)
if mibBuilder.loadTexts:
    tmnxPtpCardNotSupportedClear.setStatus(
        "current"
    )

tmnxPtpMasterClockChangedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 74, 0, 3)
)
tmnxPtpMasterClockChangedEvent.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpMasterClockAddressType"),
        ("TIMETRA-PTP-MIB", "tmnxPtpMasterClockAddress"),
        ("TIMETRA-PTP-MIB", "tmnxPtpMasterClockLastIpAddrType"),
        ("TIMETRA-PTP-MIB", "tmnxPtpMasterClockLastIpAddress"))
)
if mibBuilder.loadTexts:
    tmnxPtpMasterClockChangedEvent.setStatus(
        "current"
    )

tmnxPtpClockRecoveryStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 74, 0, 4)
)
tmnxPtpClockRecoveryStateChange.setObjects(
    ("TIMETRA-PTP-MIB", "tmnxPtpClockRecoveryState")
)
if mibBuilder.loadTexts:
    tmnxPtpClockRecoveryStateChange.setStatus(
        "current"
    )

tmnxPtpOutOfResources = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 74, 0, 5)
)
tmnxPtpOutOfResources.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyChassisId"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"))
)
if mibBuilder.loadTexts:
    tmnxPtpOutOfResources.setStatus(
        "current"
    )

tmnxPtpOutOfResourcesClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 74, 0, 6)
)
tmnxPtpOutOfResourcesClear.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyChassisId"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"))
)
if mibBuilder.loadTexts:
    tmnxPtpOutOfResourcesClear.setStatus(
        "current"
    )

tmnxPtpDynamicChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 74, 0, 7)
)
tmnxPtpDynamicChange.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpNotifyRowPointer"),
        ("TIMETRA-PTP-MIB", "tmnxPtpNotifyRowDescription"))
)
if mibBuilder.loadTexts:
    tmnxPtpDynamicChange.setStatus(
        "current"
    )


# Notifications groups

tmnxPtpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 2, 1, 11)
)
tmnxPtpNotificationsGroup.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpCardNotSupported"),
        ("TIMETRA-PTP-MIB", "tmnxPtpCardNotSupportedClear"),
        ("TIMETRA-PTP-MIB", "tmnxPtpMasterClockChangedEvent"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockRecoveryStateChange"),
        ("TIMETRA-PTP-MIB", "tmnxPtpOutOfResources"),
        ("TIMETRA-PTP-MIB", "tmnxPtpOutOfResourcesClear"),
        ("TIMETRA-PTP-MIB", "tmnxPtpDynamicChange"))
)
if mibBuilder.loadTexts:
    tmnxPtpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 1, 1)
)
tmnxPtpCompliance.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpTimeStampGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpLocalConfigGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpLocalOperGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpMasterClockGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerBaseConfigGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerMasterStatusGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPacketStatsGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockRecoveryGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerUnicastStatusGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpNotificationsGroup"))
)
if mibBuilder.loadTexts:
    tmnxPtpCompliance.setStatus(
        "obsolete"
    )

tmnxPtpComplianceV10v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 1, 2)
)
tmnxPtpComplianceV10v0.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpTimeStampGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpLocalConfigGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpLocalOperGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpMasterClockGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerBaseConfigGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerMasterStatusGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPacketStatsGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockRecoveryGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerUnicastStatusGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpNotificationsGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpVRtrIfTimeStampGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpVRtrIfConfigGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpTimeInfoGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerOperGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPacketStatsV10v0Group"))
)
if mibBuilder.loadTexts:
    tmnxPtpComplianceV10v0.setStatus(
        "obsolete"
    )

tmnxPtpComplianceV11v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 1, 3)
)
tmnxPtpComplianceV11v0.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpTimeStampGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpLocalConfigGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpLocalOperGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpMasterClockGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerBaseConfigGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerMasterStatusGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPacketStatsGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpClockRecoveryGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerUnicastStatusGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpNotificationsGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpVRtrIfTimeStampGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpVRtrIfConfigGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpTimeInfoGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerOperGroup"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPacketStatsV10v0Group"),
        ("TIMETRA-PTP-MIB", "tmnxPtpVRtrGroup"))
)
if mibBuilder.loadTexts:
    tmnxPtpComplianceV11v0.setStatus(
        "current"
    )

tmnxPtpComplianceV12v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 74, 1, 4)
)
tmnxPtpComplianceV12v0.setObjects(
      *(("TIMETRA-PTP-MIB", "tmnxPtpLocalConfigV12v0Group"),
        ("TIMETRA-PTP-MIB", "tmnxPtpPeerBaseConfigV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxPtpComplianceV12v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-PTP-MIB",
    **{"TmnxPtpClockType": TmnxPtpClockType,
       "TmnxPtpClockIdentity": TmnxPtpClockIdentity,
       "TmnxPtpClockClass": TmnxPtpClockClass,
       "TmnxPtpDomain": TmnxPtpDomain,
       "TmnxPtpPriority": TmnxPtpPriority,
       "TmnxPtpProfile": TmnxPtpProfile,
       "TmnxPtpDirection": TmnxPtpDirection,
       "TmnxPtpLogInterval": TmnxPtpLogInterval,
       "TmnxPtpClockStepType": TmnxPtpClockStepType,
       "TmnxPtpClockAccuracy": TmnxPtpClockAccuracy,
       "TmnxPtpClockVariance": TmnxPtpClockVariance,
       "TmnxPtpPortState": TmnxPtpPortState,
       "TmnxPtpPortNumber": TmnxPtpPortNumber,
       "TmnxPtpTimeStampReferencePoint": TmnxPtpTimeStampReferencePoint,
       "timetraPtpMIBModule": timetraPtpMIBModule,
       "tmnxPtp1588Conformance": tmnxPtp1588Conformance,
       "tmnxPtp1588Compliances": tmnxPtp1588Compliances,
       "tmnxPtpCompliance": tmnxPtpCompliance,
       "tmnxPtpComplianceV10v0": tmnxPtpComplianceV10v0,
       "tmnxPtpComplianceV11v0": tmnxPtpComplianceV11v0,
       "tmnxPtpComplianceV12v0": tmnxPtpComplianceV12v0,
       "tmnxPtp1588Groups": tmnxPtp1588Groups,
       "tmnxPtpV9v0Groups": tmnxPtpV9v0Groups,
       "tmnxPtpTimeStampGroup": tmnxPtpTimeStampGroup,
       "tmnxPtpLocalConfigGroup": tmnxPtpLocalConfigGroup,
       "tmnxPtpLocalOperGroup": tmnxPtpLocalOperGroup,
       "tmnxPtpMasterClockGroup": tmnxPtpMasterClockGroup,
       "tmnxPtpPeerBaseConfigGroup": tmnxPtpPeerBaseConfigGroup,
       "tmnxPtpPeerMasterStatusGroup": tmnxPtpPeerMasterStatusGroup,
       "tmnxPtpPacketStatsGroup": tmnxPtpPacketStatsGroup,
       "tmnxPtpClockRecoveryGroup": tmnxPtpClockRecoveryGroup,
       "tmnxPtpPeerUnicastStatusGroup": tmnxPtpPeerUnicastStatusGroup,
       "tmnxPtpNotifyObjsGroup": tmnxPtpNotifyObjsGroup,
       "tmnxPtpNotificationsGroup": tmnxPtpNotificationsGroup,
       "tmnxPtpV10v0Groups": tmnxPtpV10v0Groups,
       "tmnxPtpVRtrIfTimeStampGroup": tmnxPtpVRtrIfTimeStampGroup,
       "tmnxPtpVRtrIfConfigGroup": tmnxPtpVRtrIfConfigGroup,
       "tmnxPtpTimeInfoGroup": tmnxPtpTimeInfoGroup,
       "tmnxPtpPeerOperGroup": tmnxPtpPeerOperGroup,
       "tmnxPtpPacketStatsV10v0Group": tmnxPtpPacketStatsV10v0Group,
       "tmnxPtpV11v0Groups": tmnxPtpV11v0Groups,
       "tmnxPtpVRtrGroup": tmnxPtpVRtrGroup,
       "tmnxPtpV12v0Groups": tmnxPtpV12v0Groups,
       "tmnxPtpLocalConfigV12v0Group": tmnxPtpLocalConfigV12v0Group,
       "tmnxPtpPeerBaseConfigV12v0Group": tmnxPtpPeerBaseConfigV12v0Group,
       "tmnxPtp1588Objs": tmnxPtp1588Objs,
       "tmnxPtp1588ConfigTimeStamps": tmnxPtp1588ConfigTimeStamps,
       "tmnxPtpPeerConfigTblLastChanged": tmnxPtpPeerConfigTblLastChanged,
       "tmnxPtpVRtrIfTableLastChanged": tmnxPtpVRtrIfTableLastChanged,
       "tmnxPtpVRtrTableLastChanged": tmnxPtpVRtrTableLastChanged,
       "tmnxPtp1588Configurations": tmnxPtp1588Configurations,
       "tmnxPtpClockConfig": tmnxPtpClockConfig,
       "tmnxPtpClockAdminState": tmnxPtpClockAdminState,
       "tmnxPtpClockClockType": tmnxPtpClockClockType,
       "tmnxPtpClockProfile": tmnxPtpClockProfile,
       "tmnxPtpClockDomain": tmnxPtpClockDomain,
       "tmnxPtpClockAnnounceInterval": tmnxPtpClockAnnounceInterval,
       "tmnxPtpClockPriority1": tmnxPtpClockPriority1,
       "tmnxPtpClockPriority2": tmnxPtpClockPriority2,
       "tmnxPtpClockNetworkType": tmnxPtpClockNetworkType,
       "tmnxPtpClockAnnoRxTimeout": tmnxPtpClockAnnoRxTimeout,
       "tmnxPtpPeerConfigTable": tmnxPtpPeerConfigTable,
       "tmnxPtpPeerConfigEntry": tmnxPtpPeerConfigEntry,
       "tmnxPtpPeerIpAddrType": tmnxPtpPeerIpAddrType,
       "tmnxPtpPeerIpAddress": tmnxPtpPeerIpAddress,
       "tmnxPtpPeerRowStatus": tmnxPtpPeerRowStatus,
       "tmnxPtpPeerLastChanged": tmnxPtpPeerLastChanged,
       "tmnxPtpPeerAdminState": tmnxPtpPeerAdminState,
       "tmnxPtpPeerPortState": tmnxPtpPeerPortState,
       "tmnxPtpPeerLocalPriority": tmnxPtpPeerLocalPriority,
       "tmnxPtpPeerRemoteMaster": tmnxPtpPeerRemoteMaster,
       "tmnxPtpPeerRemoteSlave": tmnxPtpPeerRemoteSlave,
       "tmnxPtpPeerClockId": tmnxPtpPeerClockId,
       "tmnxPtpPeerLocalPortNumber": tmnxPtpPeerLocalPortNumber,
       "tmnxPtpPeerRemotePortNumber": tmnxPtpPeerRemotePortNumber,
       "tmnxPtpPeerTxTimeStampPoint": tmnxPtpPeerTxTimeStampPoint,
       "tmnxPtpPeerLastTxPortId": tmnxPtpPeerLastTxPortId,
       "tmnxPtpPeerLastTxPortEncapType": tmnxPtpPeerLastTxPortEncapType,
       "tmnxPtpPeerLastTxPortEncapValue": tmnxPtpPeerLastTxPortEncapValue,
       "tmnxPtpPeerRxTimeStampPoint": tmnxPtpPeerRxTimeStampPoint,
       "tmnxPtpPeerLastRxPortId": tmnxPtpPeerLastRxPortId,
       "tmnxPtpPeerLastRxPortEncapType": tmnxPtpPeerLastRxPortEncapType,
       "tmnxPtpPeerLastRxPortEncapValue": tmnxPtpPeerLastRxPortEncapValue,
       "tmnxPtpPeerSyncInterval": tmnxPtpPeerSyncInterval,
       "tmnxPtpVRtrIfTable": tmnxPtpVRtrIfTable,
       "tmnxPtpVRtrIfEntry": tmnxPtpVRtrIfEntry,
       "tmnxPtpVRtrIfAdminState": tmnxPtpVRtrIfAdminState,
       "tmnxPtpVRtrTable": tmnxPtpVRtrTable,
       "tmnxPtpVRtrEntry": tmnxPtpVRtrEntry,
       "tmnxPtpVRtrRowStatus": tmnxPtpVRtrRowStatus,
       "tmnxPtpVRtrLastChanged": tmnxPtpVRtrLastChanged,
       "tmnxPtpVRtrAdminState": tmnxPtpVRtrAdminState,
       "tmnxPtpVRtrOperState": tmnxPtpVRtrOperState,
       "tmnxPtpVRtrPeerLimit": tmnxPtpVRtrPeerLimit,
       "tmnxPtp1588Status": tmnxPtp1588Status,
       "tmnxPtpClockOperTable": tmnxPtpClockOperTable,
       "tmnxPtpClockOperEntry": tmnxPtpClockOperEntry,
       "tmnxPtpClockIdentity": tmnxPtpClockIdentity,
       "tmnxPtpClockOperState": tmnxPtpClockOperState,
       "tmnxPtpClockStepType": tmnxPtpClockStepType,
       "tmnxPtpClockClass": tmnxPtpClockClass,
       "tmnxPtpClockAccuracy": tmnxPtpClockAccuracy,
       "tmnxPtpClockVariance": tmnxPtpClockVariance,
       "tmnxPtpClockPortState": tmnxPtpClockPortState,
       "tmnxPtpClockPortStateLastChanged": tmnxPtpClockPortStateLastChanged,
       "tmnxPtpClockRecoveryState": tmnxPtpClockRecoveryState,
       "tmnxPtpClockRecoveryStateLastChg": tmnxPtpClockRecoveryStateLastChg,
       "tmnxPtpClockFrequencyOffset": tmnxPtpClockFrequencyOffset,
       "tmnxPtpMasterClockOper": tmnxPtpMasterClockOper,
       "tmnxPtpMasterClockAddressType": tmnxPtpMasterClockAddressType,
       "tmnxPtpMasterClockAddress": tmnxPtpMasterClockAddress,
       "tmnxPtpMasterClockGMClockId": tmnxPtpMasterClockGMClockId,
       "tmnxPtpMasterClockGMClockPrio1": tmnxPtpMasterClockGMClockPrio1,
       "tmnxPtpMasterClockGMClockPrio2": tmnxPtpMasterClockGMClockPrio2,
       "tmnxPtpMasterClockGMClockClass": tmnxPtpMasterClockGMClockClass,
       "tmnxPtpMasterClockGMAccuracy": tmnxPtpMasterClockGMAccuracy,
       "tmnxPtpMasterClockGMVariance": tmnxPtpMasterClockGMVariance,
       "tmnxPtpMasterClockParentClockId": tmnxPtpMasterClockParentClockId,
       "tmnxPtpMasterClockParentPortNum": tmnxPtpMasterClockParentPortNum,
       "tmnxPtpPeerMasterStatusTable": tmnxPtpPeerMasterStatusTable,
       "tmnxPtpPeerMasterStatusEntry": tmnxPtpPeerMasterStatusEntry,
       "tmnxPtpPeerMasterCurrentMaster": tmnxPtpPeerMasterCurrentMaster,
       "tmnxPtpPeerMasterClockStepType": tmnxPtpPeerMasterClockStepType,
       "tmnxPtpPeerMasterClockStepsRemvd": tmnxPtpPeerMasterClockStepsRemvd,
       "tmnxPtpPeerMasterGMClockId": tmnxPtpPeerMasterGMClockId,
       "tmnxPtpPeerMasterGMClockPrio1": tmnxPtpPeerMasterGMClockPrio1,
       "tmnxPtpPeerMasterGMClockPrio2": tmnxPtpPeerMasterGMClockPrio2,
       "tmnxPtpPeerMasterGMClockClass": tmnxPtpPeerMasterGMClockClass,
       "tmnxPtpPeerMasterGMClockAccuracy": tmnxPtpPeerMasterGMClockAccuracy,
       "tmnxPtpPeerMasterGMClockVariance": tmnxPtpPeerMasterGMClockVariance,
       "tmnxPtpPeerMasterAlarm": tmnxPtpPeerMasterAlarm,
       "tmnxPtpPeerUnicastTable": tmnxPtpPeerUnicastTable,
       "tmnxPtpPeerUnicastEntry": tmnxPtpPeerUnicastEntry,
       "tmnxPtpPeerUnicastDirection": tmnxPtpPeerUnicastDirection,
       "tmnxPtpPeerUnicastPktType": tmnxPtpPeerUnicastPktType,
       "tmnxPtpPeerUnicastStatus": tmnxPtpPeerUnicastStatus,
       "tmnxPtpPeerUnicastRate": tmnxPtpPeerUnicastRate,
       "tmnxPtpPeerUnicastDuration": tmnxPtpPeerUnicastDuration,
       "tmnxPtpPeerUnicastEventTime": tmnxPtpPeerUnicastEventTime,
       "tmnxPtpTimeInformation": tmnxPtpTimeInformation,
       "tmnxPtpTimeInfoTimescale": tmnxPtpTimeInfoTimescale,
       "tmnxPtpTimeInfoCurrentTime": tmnxPtpTimeInfoCurrentTime,
       "tmnxPtpTimeInfoFreqTraceable": tmnxPtpTimeInfoFreqTraceable,
       "tmnxPtpTimeInfoTimeTraceable": tmnxPtpTimeInfoTimeTraceable,
       "tmnxPtpTimeInfoTimeSource": tmnxPtpTimeInfoTimeSource,
       "tmnxPtp1588Statistics": tmnxPtp1588Statistics,
       "tmnxPtpClockPacketStatsTable": tmnxPtpClockPacketStatsTable,
       "tmnxPtpClockPacketStatsEntry": tmnxPtpClockPacketStatsEntry,
       "tmnxPtpClkPktStatsDirection": tmnxPtpClkPktStatsDirection,
       "tmnxPtpClkPktStatsAnnounce": tmnxPtpClkPktStatsAnnounce,
       "tmnxPtpClkPktStatsSync": tmnxPtpClkPktStatsSync,
       "tmnxPtpClkPktStatsFollowUp": tmnxPtpClkPktStatsFollowUp,
       "tmnxPtpClkPktStatsDelayRequest": tmnxPtpClkPktStatsDelayRequest,
       "tmnxPtpClkPktStatsDelayResp": tmnxPtpClkPktStatsDelayResp,
       "tmnxPtpClkPktStatsSignaling": tmnxPtpClkPktStatsSignaling,
       "tmnxPtpClkPktStatsOther": tmnxPtpClkPktStatsOther,
       "tmnxPtpClkPktStatsUniReqAnno": tmnxPtpClkPktStatsUniReqAnno,
       "tmnxPtpClkPktStatsUniReqSync": tmnxPtpClkPktStatsUniReqSync,
       "tmnxPtpClkPktStatsUniReqDelayRsp": tmnxPtpClkPktStatsUniReqDelayRsp,
       "tmnxPtpClkPktStatsUniGrantAnno": tmnxPtpClkPktStatsUniGrantAnno,
       "tmnxPtpClkPktStatsUniGrantSync": tmnxPtpClkPktStatsUniGrantSync,
       "tmnxPtpClkPktStatsUniGrantDelRsp": tmnxPtpClkPktStatsUniGrantDelRsp,
       "tmnxPtpClkPktStatsUniDenyAnno": tmnxPtpClkPktStatsUniDenyAnno,
       "tmnxPtpClkPktStatsUniDenySync": tmnxPtpClkPktStatsUniDenySync,
       "tmnxPtpClkPktStatsUniDenyDelRsp": tmnxPtpClkPktStatsUniDenyDelRsp,
       "tmnxPtpClkPktStatsUniCancelAnno": tmnxPtpClkPktStatsUniCancelAnno,
       "tmnxPtpClkPktStatsUniCancelSync": tmnxPtpClkPktStatsUniCancelSync,
       "tmnxPtpClkPktStatsUniCancelDelay": tmnxPtpClkPktStatsUniCancelDelay,
       "tmnxPtpClkPktStatsUniAckCnclAnno": tmnxPtpClkPktStatsUniAckCnclAnno,
       "tmnxPtpClkPktStatsUniAckCnclSync": tmnxPtpClkPktStatsUniAckCnclSync,
       "tmnxPtpClkPktStatsUniAckCnclDly": tmnxPtpClkPktStatsUniAckCnclDly,
       "tmnxPtpClkPktStatsOtherTLVs": tmnxPtpClkPktStatsOtherTLVs,
       "tmnxPtpClkPktStatsDropBadDomain": tmnxPtpClkPktStatsDropBadDomain,
       "tmnxPtpClkPktStatsDropAltMaster": tmnxPtpClkPktStatsDropAltMaster,
       "tmnxPtpClkPktStatsDropOther": tmnxPtpClkPktStatsDropOther,
       "tmnxPtpClkPktStatsTimeStampPort": tmnxPtpClkPktStatsTimeStampPort,
       "tmnxPtpClkPktStatsTimeStampCpm": tmnxPtpClkPktStatsTimeStampCpm,
       "tmnxPtpClkPktStatsDropOutOfSeq": tmnxPtpClkPktStatsDropOutOfSeq,
       "tmnxPtpClkPktStatsDropPeerShut": tmnxPtpClkPktStatsDropPeerShut,
       "tmnxPtpPeerPacketStatsTable": tmnxPtpPeerPacketStatsTable,
       "tmnxPtpPeerPacketStatsEntry": tmnxPtpPeerPacketStatsEntry,
       "tmnxPtpPeerPktStatDirection": tmnxPtpPeerPktStatDirection,
       "tmnxPtpPeerPktStatAnnounce": tmnxPtpPeerPktStatAnnounce,
       "tmnxPtpPeerPktStatSync": tmnxPtpPeerPktStatSync,
       "tmnxPtpPeerPktStatFollowUp": tmnxPtpPeerPktStatFollowUp,
       "tmnxPtpPeerPktStatDelayRequest": tmnxPtpPeerPktStatDelayRequest,
       "tmnxPtpPeerPktStatDelayResp": tmnxPtpPeerPktStatDelayResp,
       "tmnxPtpPeerPktStatSignaling": tmnxPtpPeerPktStatSignaling,
       "tmnxPtpPeerPktStatOther": tmnxPtpPeerPktStatOther,
       "tmnxPtpPeerPktStatUniReqAnno": tmnxPtpPeerPktStatUniReqAnno,
       "tmnxPtpPeerPktStatUniReqSync": tmnxPtpPeerPktStatUniReqSync,
       "tmnxPtpPeerPktStatUniReqDelayRsp": tmnxPtpPeerPktStatUniReqDelayRsp,
       "tmnxPtpPeerPktStatUniGrantAnno": tmnxPtpPeerPktStatUniGrantAnno,
       "tmnxPtpPeerPktStatUniGrantSync": tmnxPtpPeerPktStatUniGrantSync,
       "tmnxPtpPeerPktStatUniGrantDelRsp": tmnxPtpPeerPktStatUniGrantDelRsp,
       "tmnxPtpPeerPktStatUniDenyAnno": tmnxPtpPeerPktStatUniDenyAnno,
       "tmnxPtpPeerPktStatUniDenySync": tmnxPtpPeerPktStatUniDenySync,
       "tmnxPtpPeerPktStatUniDenyDelRsp": tmnxPtpPeerPktStatUniDenyDelRsp,
       "tmnxPtpPeerPktStatUniCancelAnno": tmnxPtpPeerPktStatUniCancelAnno,
       "tmnxPtpPeerPktStatUniCancelSync": tmnxPtpPeerPktStatUniCancelSync,
       "tmnxPtpPeerPktStatUniCancelDelay": tmnxPtpPeerPktStatUniCancelDelay,
       "tmnxPtpPeerPktStatUniAckCnclAnno": tmnxPtpPeerPktStatUniAckCnclAnno,
       "tmnxPtpPeerPktStatUniAckCnclSync": tmnxPtpPeerPktStatUniAckCnclSync,
       "tmnxPtpPeerPktStatUniAckCnclDly": tmnxPtpPeerPktStatUniAckCnclDly,
       "tmnxPtpPeerPktStatOtherTLVs": tmnxPtpPeerPktStatOtherTLVs,
       "tmnxPtpPeerPktStatDropBadDomain": tmnxPtpPeerPktStatDropBadDomain,
       "tmnxPtpPeerPktStatDropAltMaster": tmnxPtpPeerPktStatDropAltMaster,
       "tmnxPtpPeerPktStatDropOther": tmnxPtpPeerPktStatDropOther,
       "tmnxPtpPeerPktStatTimeStampPort": tmnxPtpPeerPktStatTimeStampPort,
       "tmnxPtpPeerPktStatTimeStampCpm": tmnxPtpPeerPktStatTimeStampCpm,
       "tmnxPtpPeerPktStatDropOutOfSeq": tmnxPtpPeerPktStatDropOutOfSeq,
       "tmnxPtpPeerPktStatDropPeerShut": tmnxPtpPeerPktStatDropPeerShut,
       "tmnxPtpClockRecoveryStatistics": tmnxPtpClockRecoveryStatistics,
       "tmnxPtpClockRecStatsInitial": tmnxPtpClockRecStatsInitial,
       "tmnxPtpClockRecStatsAcquiring": tmnxPtpClockRecStatsAcquiring,
       "tmnxPtpClockRecStatsPhaseTrack": tmnxPtpClockRecStatsPhaseTrack,
       "tmnxPtpClockRecStatsLocked": tmnxPtpClockRecStatsLocked,
       "tmnxPtpClockRecStatsHoldover": tmnxPtpClockRecStatsHoldover,
       "tmnxPtpClockRecStatsSyncPktLoss": tmnxPtpClockRecStatsSyncPktLoss,
       "tmnxPtpClockRecStatsSyncHiPktLss": tmnxPtpClockRecStatsSyncHiPktLss,
       "tmnxPtpClockRecStatsSyncStep": tmnxPtpClockRecStatsSyncStep,
       "tmnxPtpClockRecStatsSyncHighPDV": tmnxPtpClockRecStatsSyncHighPDV,
       "tmnxPtpClockRecStatsDlyPktLoss": tmnxPtpClockRecStatsDlyPktLoss,
       "tmnxPtpClockRecStatsDlyHiPktLss": tmnxPtpClockRecStatsDlyHiPktLss,
       "tmnxPtpClockRecStatsDlyStep": tmnxPtpClockRecStatsDlyStep,
       "tmnxPtpClockRecStatsDlyHighPDV": tmnxPtpClockRecStatsDlyHighPDV,
       "tmnxPtp1588NotifyObjects": tmnxPtp1588NotifyObjects,
       "tmnxPtpMasterClockLastIpAddrType": tmnxPtpMasterClockLastIpAddrType,
       "tmnxPtpMasterClockLastIpAddress": tmnxPtpMasterClockLastIpAddress,
       "tmnxPtpNotifyRowPointer": tmnxPtpNotifyRowPointer,
       "tmnxPtpNotifyRowDescription": tmnxPtpNotifyRowDescription,
       "tmnxPtp1588NotifyPrefix": tmnxPtp1588NotifyPrefix,
       "tmnxPtp1588Notifications": tmnxPtp1588Notifications,
       "tmnxPtpCardNotSupported": tmnxPtpCardNotSupported,
       "tmnxPtpCardNotSupportedClear": tmnxPtpCardNotSupportedClear,
       "tmnxPtpMasterClockChangedEvent": tmnxPtpMasterClockChangedEvent,
       "tmnxPtpClockRecoveryStateChange": tmnxPtpClockRecoveryStateChange,
       "tmnxPtpOutOfResources": tmnxPtpOutOfResources,
       "tmnxPtpOutOfResourcesClear": tmnxPtpOutOfResourcesClear,
       "tmnxPtpDynamicChange": tmnxPtpDynamicChange}
)

# SNMP MIB module (TIMETRA-RPKI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-RPKI-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:23 2025
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
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber",
    "InetPortNumber")

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

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(BgpConnectRetryTime,
 BgpHoldTime,
 TLNamedItemOrEmpty,
 TNamedItem,
 TmnxAdminState,
 TmnxOperState,
 TmnxPortID,
 TmnxVRtrID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "BgpConnectRetryTime",
    "BgpHoldTime",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TmnxAdminState",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxVRtrID")

(vRtrID,) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID")


# MODULE-IDENTITY

timetraRpkiOriginValidMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 96)
)
if mibBuilder.loadTexts:
    timetraRpkiOriginValidMIBModule.setRevisions(
        ("2014-03-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxRpkiConformance_ObjectIdentity = ObjectIdentity
tmnxRpkiConformance = _TmnxRpkiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 96)
)
_TmnxRpkiCompliances_ObjectIdentity = ObjectIdentity
tmnxRpkiCompliances = _TmnxRpkiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 96, 1)
)
_TmnxRpkiGroups_ObjectIdentity = ObjectIdentity
tmnxRpkiGroups = _TmnxRpkiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 96, 2)
)
_TmnxRpkiObjs_ObjectIdentity = ObjectIdentity
tmnxRpkiObjs = _TmnxRpkiObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96)
)
_VRtrRpkiSessInstanceTable_Object = MibTable
vRtrRpkiSessInstanceTable = _VRtrRpkiSessInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1)
)
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceTable.setStatus("current")
_VRtrRpkiSessInstanceEntry_Object = MibTableRow
vRtrRpkiSessInstanceEntry = _VRtrRpkiSessInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1)
)
vRtrRpkiSessInstanceEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RPKI-MIB", "vRtrRpkiSessInstanceAddressType"),
    (0, "TIMETRA-RPKI-MIB", "vRtrRpkiSessInstanceAddress"),
)
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceEntry.setStatus("current")
_VRtrRpkiSessInstanceAddressType_Type = InetAddressType
_VRtrRpkiSessInstanceAddressType_Object = MibTableColumn
vRtrRpkiSessInstanceAddressType = _VRtrRpkiSessInstanceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1, 1),
    _VRtrRpkiSessInstanceAddressType_Type()
)
vRtrRpkiSessInstanceAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceAddressType.setStatus("current")


class _VRtrRpkiSessInstanceAddress_Type(InetAddress):
    """Custom type vRtrRpkiSessInstanceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_VRtrRpkiSessInstanceAddress_Type.__name__ = "InetAddress"
_VRtrRpkiSessInstanceAddress_Object = MibTableColumn
vRtrRpkiSessInstanceAddress = _VRtrRpkiSessInstanceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1, 2),
    _VRtrRpkiSessInstanceAddress_Type()
)
vRtrRpkiSessInstanceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceAddress.setStatus("current")
_VRtrRpkiSessInstanceRowStatus_Type = RowStatus
_VRtrRpkiSessInstanceRowStatus_Object = MibTableColumn
vRtrRpkiSessInstanceRowStatus = _VRtrRpkiSessInstanceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1, 3),
    _VRtrRpkiSessInstanceRowStatus_Type()
)
vRtrRpkiSessInstanceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceRowStatus.setStatus("current")


class _VRtrRpkiSessInstanceConnectRetry_Type(BgpConnectRetryTime):
    """Custom type vRtrRpkiSessInstanceConnectRetry based on BgpConnectRetryTime"""
    defaultValue = 120


_VRtrRpkiSessInstanceConnectRetry_Type.__name__ = "BgpConnectRetryTime"
_VRtrRpkiSessInstanceConnectRetry_Object = MibTableColumn
vRtrRpkiSessInstanceConnectRetry = _VRtrRpkiSessInstanceConnectRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1, 4),
    _VRtrRpkiSessInstanceConnectRetry_Type()
)
vRtrRpkiSessInstanceConnectRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceConnectRetry.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceConnectRetry.setUnits("seconds")


class _VRtrRpkiSessInstanceDescription_Type(DisplayString):
    """Custom type vRtrRpkiSessInstanceDescription based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_VRtrRpkiSessInstanceDescription_Type.__name__ = "DisplayString"
_VRtrRpkiSessInstanceDescription_Object = MibTableColumn
vRtrRpkiSessInstanceDescription = _VRtrRpkiSessInstanceDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1, 5),
    _VRtrRpkiSessInstanceDescription_Type()
)
vRtrRpkiSessInstanceDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceDescription.setStatus("current")


class _VRtrRpkiSessInstanceHoldTime_Type(BgpHoldTime):
    """Custom type vRtrRpkiSessInstanceHoldTime based on BgpHoldTime"""
    defaultValue = 600


_VRtrRpkiSessInstanceHoldTime_Type.__name__ = "BgpHoldTime"
_VRtrRpkiSessInstanceHoldTime_Object = MibTableColumn
vRtrRpkiSessInstanceHoldTime = _VRtrRpkiSessInstanceHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1, 6),
    _VRtrRpkiSessInstanceHoldTime_Type()
)
vRtrRpkiSessInstanceHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceHoldTime.setUnits("seconds")


class _VRtrRpkiSessLocalAddressType_Type(InetAddressType):
    """Custom type vRtrRpkiSessLocalAddressType based on InetAddressType"""
    defaultValue = 0


_VRtrRpkiSessLocalAddressType_Type.__name__ = "InetAddressType"
_VRtrRpkiSessLocalAddressType_Object = MibTableColumn
vRtrRpkiSessLocalAddressType = _VRtrRpkiSessLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1, 7),
    _VRtrRpkiSessLocalAddressType_Type()
)
vRtrRpkiSessLocalAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRpkiSessLocalAddressType.setStatus("current")


class _VRtrRpkiSessLocalAddress_Type(InetAddress):
    """Custom type vRtrRpkiSessLocalAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrRpkiSessLocalAddress_Type.__name__ = "InetAddress"
_VRtrRpkiSessLocalAddress_Object = MibTableColumn
vRtrRpkiSessLocalAddress = _VRtrRpkiSessLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1, 8),
    _VRtrRpkiSessLocalAddress_Type()
)
vRtrRpkiSessLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRpkiSessLocalAddress.setStatus("current")


class _VRtrRpkiSessInstancePort_Type(Unsigned32):
    """Custom type vRtrRpkiSessInstancePort based on Unsigned32"""
    defaultValue = 323

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrRpkiSessInstancePort_Type.__name__ = "Unsigned32"
_VRtrRpkiSessInstancePort_Object = MibTableColumn
vRtrRpkiSessInstancePort = _VRtrRpkiSessInstancePort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1, 9),
    _VRtrRpkiSessInstancePort_Type()
)
vRtrRpkiSessInstancePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstancePort.setStatus("current")


class _VRtrRpkiSessInstanceRefreshTime_Type(Unsigned32):
    """Custom type vRtrRpkiSessInstanceRefreshTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32767),
    )


_VRtrRpkiSessInstanceRefreshTime_Type.__name__ = "Unsigned32"
_VRtrRpkiSessInstanceRefreshTime_Object = MibTableColumn
vRtrRpkiSessInstanceRefreshTime = _VRtrRpkiSessInstanceRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1, 10),
    _VRtrRpkiSessInstanceRefreshTime_Type()
)
vRtrRpkiSessInstanceRefreshTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceRefreshTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceRefreshTime.setUnits("seconds")


class _VRtrRpkiSessInstanceAdminState_Type(TmnxAdminState):
    """Custom type vRtrRpkiSessInstanceAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrRpkiSessInstanceAdminState_Type.__name__ = "TmnxAdminState"
_VRtrRpkiSessInstanceAdminState_Object = MibTableColumn
vRtrRpkiSessInstanceAdminState = _VRtrRpkiSessInstanceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1, 11),
    _VRtrRpkiSessInstanceAdminState_Type()
)
vRtrRpkiSessInstanceAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceAdminState.setStatus("current")


class _VRtrRpkiSessInstanceStaleRoutTim_Type(Unsigned32):
    """Custom type vRtrRpkiSessInstanceStaleRoutTim based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_VRtrRpkiSessInstanceStaleRoutTim_Type.__name__ = "Unsigned32"
_VRtrRpkiSessInstanceStaleRoutTim_Object = MibTableColumn
vRtrRpkiSessInstanceStaleRoutTim = _VRtrRpkiSessInstanceStaleRoutTim_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1, 12),
    _VRtrRpkiSessInstanceStaleRoutTim_Type()
)
vRtrRpkiSessInstanceStaleRoutTim.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceStaleRoutTim.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceStaleRoutTim.setUnits("seconds")


class _VRtrRpkiSessInstanceSessionState_Type(Integer32):
    """Custom type vRtrRpkiSessInstanceSessionState based on Integer32"""
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
        *(("idle", 0),
          ("connect", 1),
          ("established", 2),
          ("cleanup", 3))
    )


_VRtrRpkiSessInstanceSessionState_Type.__name__ = "Integer32"
_VRtrRpkiSessInstanceSessionState_Object = MibTableColumn
vRtrRpkiSessInstanceSessionState = _VRtrRpkiSessInstanceSessionState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1, 13),
    _VRtrRpkiSessInstanceSessionState_Type()
)
vRtrRpkiSessInstanceSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceSessionState.setStatus("current")
_VRtrRpkiSessInstanceSessionFlaps_Type = Unsigned32
_VRtrRpkiSessInstanceSessionFlaps_Object = MibTableColumn
vRtrRpkiSessInstanceSessionFlaps = _VRtrRpkiSessInstanceSessionFlaps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1, 14),
    _VRtrRpkiSessInstanceSessionFlaps_Type()
)
vRtrRpkiSessInstanceSessionFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceSessionFlaps.setStatus("current")
_VRtrRpkiSessInstanceUptime_Type = TimeStamp
_VRtrRpkiSessInstanceUptime_Object = MibTableColumn
vRtrRpkiSessInstanceUptime = _VRtrRpkiSessInstanceUptime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1, 15),
    _VRtrRpkiSessInstanceUptime_Type()
)
vRtrRpkiSessInstanceUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceUptime.setStatus("current")
_VRtrRpkiSessInstanceActIpv4Rec_Type = Unsigned32
_VRtrRpkiSessInstanceActIpv4Rec_Object = MibTableColumn
vRtrRpkiSessInstanceActIpv4Rec = _VRtrRpkiSessInstanceActIpv4Rec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1, 16),
    _VRtrRpkiSessInstanceActIpv4Rec_Type()
)
vRtrRpkiSessInstanceActIpv4Rec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceActIpv4Rec.setStatus("current")
_VRtrRpkiSessInstanceActIpv6Rec_Type = Unsigned32
_VRtrRpkiSessInstanceActIpv6Rec_Object = MibTableColumn
vRtrRpkiSessInstanceActIpv6Rec = _VRtrRpkiSessInstanceActIpv6Rec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1, 17),
    _VRtrRpkiSessInstanceActIpv6Rec_Type()
)
vRtrRpkiSessInstanceActIpv6Rec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceActIpv6Rec.setStatus("current")
_VRtrRpkiSessInstanceSerialId_Type = Unsigned32
_VRtrRpkiSessInstanceSerialId_Object = MibTableColumn
vRtrRpkiSessInstanceSerialId = _VRtrRpkiSessInstanceSerialId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1, 18),
    _VRtrRpkiSessInstanceSerialId_Type()
)
vRtrRpkiSessInstanceSerialId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceSerialId.setStatus("current")
_VRtrRpkiSessInstanceSessionId_Type = Unsigned32
_VRtrRpkiSessInstanceSessionId_Object = MibTableColumn
vRtrRpkiSessInstanceSessionId = _VRtrRpkiSessInstanceSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1, 19),
    _VRtrRpkiSessInstanceSessionId_Type()
)
vRtrRpkiSessInstanceSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceSessionId.setStatus("current")
_VRtrRpkiSessInstanceLastChange_Type = TimeStamp
_VRtrRpkiSessInstanceLastChange_Object = MibTableColumn
vRtrRpkiSessInstanceLastChange = _VRtrRpkiSessInstanceLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 1, 1, 20),
    _VRtrRpkiSessInstanceLastChange_Type()
)
vRtrRpkiSessInstanceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRpkiSessInstanceLastChange.setStatus("current")
_VRtrOriginValStaticTable_Object = MibTable
vRtrOriginValStaticTable = _VRtrOriginValStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 2)
)
if mibBuilder.loadTexts:
    vRtrOriginValStaticTable.setStatus("current")
_VRtrOriginValStaticEntry_Object = MibTableRow
vRtrOriginValStaticEntry = _VRtrOriginValStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 2, 1)
)
vRtrOriginValStaticEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RPKI-MIB", "vRtrOrigValStaticIpPrefixType"),
    (0, "TIMETRA-RPKI-MIB", "vRtrOrigValStaticIpPrefix"),
    (0, "TIMETRA-RPKI-MIB", "vRtrOrigValStaticMinPrefixLen"),
    (0, "TIMETRA-RPKI-MIB", "vRtrOrigValStaticMaxPrefixLen"),
    (0, "TIMETRA-RPKI-MIB", "vRtrOrigValStaticAS4Byte"),
)
if mibBuilder.loadTexts:
    vRtrOriginValStaticEntry.setStatus("current")
_VRtrOrigValStaticIpPrefixType_Type = InetAddressType
_VRtrOrigValStaticIpPrefixType_Object = MibTableColumn
vRtrOrigValStaticIpPrefixType = _VRtrOrigValStaticIpPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 2, 1, 1),
    _VRtrOrigValStaticIpPrefixType_Type()
)
vRtrOrigValStaticIpPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrOrigValStaticIpPrefixType.setStatus("current")


class _VRtrOrigValStaticIpPrefix_Type(InetAddress):
    """Custom type vRtrOrigValStaticIpPrefix based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrOrigValStaticIpPrefix_Type.__name__ = "InetAddress"
_VRtrOrigValStaticIpPrefix_Object = MibTableColumn
vRtrOrigValStaticIpPrefix = _VRtrOrigValStaticIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 2, 1, 2),
    _VRtrOrigValStaticIpPrefix_Type()
)
vRtrOrigValStaticIpPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrOrigValStaticIpPrefix.setStatus("current")


class _VRtrOrigValStaticMinPrefixLen_Type(InetAddressPrefixLength):
    """Custom type vRtrOrigValStaticMinPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_VRtrOrigValStaticMinPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_VRtrOrigValStaticMinPrefixLen_Object = MibTableColumn
vRtrOrigValStaticMinPrefixLen = _VRtrOrigValStaticMinPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 2, 1, 3),
    _VRtrOrigValStaticMinPrefixLen_Type()
)
vRtrOrigValStaticMinPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrOrigValStaticMinPrefixLen.setStatus("current")


class _VRtrOrigValStaticMaxPrefixLen_Type(InetAddressPrefixLength):
    """Custom type vRtrOrigValStaticMaxPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_VRtrOrigValStaticMaxPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_VRtrOrigValStaticMaxPrefixLen_Object = MibTableColumn
vRtrOrigValStaticMaxPrefixLen = _VRtrOrigValStaticMaxPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 2, 1, 4),
    _VRtrOrigValStaticMaxPrefixLen_Type()
)
vRtrOrigValStaticMaxPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrOrigValStaticMaxPrefixLen.setStatus("current")


class _VRtrOrigValStaticAS4Byte_Type(InetAutonomousSystemNumber):
    """Custom type vRtrOrigValStaticAS4Byte based on InetAutonomousSystemNumber"""
    defaultValue = 0


_VRtrOrigValStaticAS4Byte_Type.__name__ = "InetAutonomousSystemNumber"
_VRtrOrigValStaticAS4Byte_Object = MibTableColumn
vRtrOrigValStaticAS4Byte = _VRtrOrigValStaticAS4Byte_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 2, 1, 5),
    _VRtrOrigValStaticAS4Byte_Type()
)
vRtrOrigValStaticAS4Byte.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrOrigValStaticAS4Byte.setStatus("current")
_VRtrOrigValStaticRowStatus_Type = RowStatus
_VRtrOrigValStaticRowStatus_Object = MibTableColumn
vRtrOrigValStaticRowStatus = _VRtrOrigValStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 2, 1, 6),
    _VRtrOrigValStaticRowStatus_Type()
)
vRtrOrigValStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOrigValStaticRowStatus.setStatus("current")


class _VRtrOrigValStaticASValidity_Type(TruthValue):
    """Custom type vRtrOrigValStaticASValidity based on TruthValue"""
    defaultValue = 1


_VRtrOrigValStaticASValidity_Type.__name__ = "TruthValue"
_VRtrOrigValStaticASValidity_Object = MibTableColumn
vRtrOrigValStaticASValidity = _VRtrOrigValStaticASValidity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 2, 1, 7),
    _VRtrOrigValStaticASValidity_Type()
)
vRtrOrigValStaticASValidity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOrigValStaticASValidity.setStatus("current")
_VRtrOriginValRouteTable_Object = MibTable
vRtrOriginValRouteTable = _VRtrOriginValRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 3)
)
if mibBuilder.loadTexts:
    vRtrOriginValRouteTable.setStatus("current")
_VRtrOriginValRouteEntry_Object = MibTableRow
vRtrOriginValRouteEntry = _VRtrOriginValRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 3, 1)
)
vRtrOriginValRouteEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RPKI-MIB", "vRtrOrigValRouteIpPrefixType"),
    (0, "TIMETRA-RPKI-MIB", "vRtrOrigValRouteIpPrefix"),
    (0, "TIMETRA-RPKI-MIB", "vRtrOrigValRouteMinPrefixLen"),
    (0, "TIMETRA-RPKI-MIB", "vRtrOrigValRouteMaxPrefixLen"),
    (0, "TIMETRA-RPKI-MIB", "vRtrOrigValRouteAS4Byte"),
    (0, "TIMETRA-RPKI-MIB", "vRtrOrigValRouteType"),
    (0, "TIMETRA-RPKI-MIB", "vRtrOrigValRouteRpkiVrId"),
    (0, "TIMETRA-RPKI-MIB", "vRtrOrigValRouteRpkiAddrType"),
    (0, "TIMETRA-RPKI-MIB", "vRtrOrigValRouteRpkiAddress"),
)
if mibBuilder.loadTexts:
    vRtrOriginValRouteEntry.setStatus("current")
_VRtrOrigValRouteIpPrefixType_Type = InetAddressType
_VRtrOrigValRouteIpPrefixType_Object = MibTableColumn
vRtrOrigValRouteIpPrefixType = _VRtrOrigValRouteIpPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 3, 1, 1),
    _VRtrOrigValRouteIpPrefixType_Type()
)
vRtrOrigValRouteIpPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrOrigValRouteIpPrefixType.setStatus("current")


class _VRtrOrigValRouteIpPrefix_Type(InetAddress):
    """Custom type vRtrOrigValRouteIpPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrOrigValRouteIpPrefix_Type.__name__ = "InetAddress"
_VRtrOrigValRouteIpPrefix_Object = MibTableColumn
vRtrOrigValRouteIpPrefix = _VRtrOrigValRouteIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 3, 1, 2),
    _VRtrOrigValRouteIpPrefix_Type()
)
vRtrOrigValRouteIpPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrOrigValRouteIpPrefix.setStatus("current")


class _VRtrOrigValRouteMinPrefixLen_Type(InetAddressPrefixLength):
    """Custom type vRtrOrigValRouteMinPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_VRtrOrigValRouteMinPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_VRtrOrigValRouteMinPrefixLen_Object = MibTableColumn
vRtrOrigValRouteMinPrefixLen = _VRtrOrigValRouteMinPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 3, 1, 3),
    _VRtrOrigValRouteMinPrefixLen_Type()
)
vRtrOrigValRouteMinPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrOrigValRouteMinPrefixLen.setStatus("current")


class _VRtrOrigValRouteMaxPrefixLen_Type(InetAddressPrefixLength):
    """Custom type vRtrOrigValRouteMaxPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_VRtrOrigValRouteMaxPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_VRtrOrigValRouteMaxPrefixLen_Object = MibTableColumn
vRtrOrigValRouteMaxPrefixLen = _VRtrOrigValRouteMaxPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 3, 1, 4),
    _VRtrOrigValRouteMaxPrefixLen_Type()
)
vRtrOrigValRouteMaxPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrOrigValRouteMaxPrefixLen.setStatus("current")
_VRtrOrigValRouteAS4Byte_Type = InetAutonomousSystemNumber
_VRtrOrigValRouteAS4Byte_Object = MibTableColumn
vRtrOrigValRouteAS4Byte = _VRtrOrigValRouteAS4Byte_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 3, 1, 5),
    _VRtrOrigValRouteAS4Byte_Type()
)
vRtrOrigValRouteAS4Byte.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrOrigValRouteAS4Byte.setStatus("current")


class _VRtrOrigValRouteType_Type(Integer32):
    """Custom type vRtrOrigValRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_VRtrOrigValRouteType_Type.__name__ = "Integer32"
_VRtrOrigValRouteType_Object = MibTableColumn
vRtrOrigValRouteType = _VRtrOrigValRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 3, 1, 6),
    _VRtrOrigValRouteType_Type()
)
vRtrOrigValRouteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrOrigValRouteType.setStatus("current")
_VRtrOrigValRouteRpkiVrId_Type = TmnxVRtrID
_VRtrOrigValRouteRpkiVrId_Object = MibTableColumn
vRtrOrigValRouteRpkiVrId = _VRtrOrigValRouteRpkiVrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 3, 1, 7),
    _VRtrOrigValRouteRpkiVrId_Type()
)
vRtrOrigValRouteRpkiVrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrOrigValRouteRpkiVrId.setStatus("current")
_VRtrOrigValRouteRpkiAddrType_Type = InetAddressType
_VRtrOrigValRouteRpkiAddrType_Object = MibTableColumn
vRtrOrigValRouteRpkiAddrType = _VRtrOrigValRouteRpkiAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 3, 1, 8),
    _VRtrOrigValRouteRpkiAddrType_Type()
)
vRtrOrigValRouteRpkiAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrOrigValRouteRpkiAddrType.setStatus("current")


class _VRtrOrigValRouteRpkiAddress_Type(InetAddress):
    """Custom type vRtrOrigValRouteRpkiAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_VRtrOrigValRouteRpkiAddress_Type.__name__ = "InetAddress"
_VRtrOrigValRouteRpkiAddress_Object = MibTableColumn
vRtrOrigValRouteRpkiAddress = _VRtrOrigValRouteRpkiAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 3, 1, 9),
    _VRtrOrigValRouteRpkiAddress_Type()
)
vRtrOrigValRouteRpkiAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrOrigValRouteRpkiAddress.setStatus("current")
_VRtrOrigValASRouteValidity_Type = TruthValue
_VRtrOrigValASRouteValidity_Object = MibTableColumn
vRtrOrigValASRouteValidity = _VRtrOrigValASRouteValidity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 3, 1, 10),
    _VRtrOrigValASRouteValidity_Type()
)
vRtrOrigValASRouteValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOrigValASRouteValidity.setStatus("current")
_TmnxRpkiNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxRpkiNotificationObjs = _TmnxRpkiNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 4)
)
_TmnxRpkiPeerAddrType_Type = InetAddressType
_TmnxRpkiPeerAddrType_Object = MibScalar
tmnxRpkiPeerAddrType = _TmnxRpkiPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 4, 1),
    _TmnxRpkiPeerAddrType_Type()
)
tmnxRpkiPeerAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxRpkiPeerAddrType.setStatus("current")
_TmnxRpkiPeerAddr_Type = InetAddress
_TmnxRpkiPeerAddr_Object = MibScalar
tmnxRpkiPeerAddr = _TmnxRpkiPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 4, 2),
    _TmnxRpkiPeerAddr_Type()
)
tmnxRpkiPeerAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxRpkiPeerAddr.setStatus("current")


class _TmnxRpkiErrorType_Type(Integer32):
    """Custom type tmnxRpkiErrorType based on Integer32"""
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
        *(("holdTimerExpired", 1),
          ("tcpConnectionFailure", 2),
          ("sessionIdMismatch", 3),
          ("fatalErrorCode", 4),
          ("sessionEstablished", 5))
    )


_TmnxRpkiErrorType_Type.__name__ = "Integer32"
_TmnxRpkiErrorType_Object = MibScalar
tmnxRpkiErrorType = _TmnxRpkiErrorType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 4, 3),
    _TmnxRpkiErrorType_Type()
)
tmnxRpkiErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxRpkiErrorType.setStatus("current")


class _TmnxRpkiTrapStatus_Type(Integer32):
    """Custom type tmnxRpkiTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TmnxRpkiTrapStatus_Type.__name__ = "Integer32"
_TmnxRpkiTrapStatus_Object = MibScalar
tmnxRpkiTrapStatus = _TmnxRpkiTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 96, 4, 4),
    _TmnxRpkiTrapStatus_Type()
)
tmnxRpkiTrapStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxRpkiTrapStatus.setStatus("current")
_TmnxRpkiNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxRpkiNotifyPrefix = _TmnxRpkiNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 96)
)
_TmnxRpkiNotifications_ObjectIdentity = ObjectIdentity
tmnxRpkiNotifications = _TmnxRpkiNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 96, 0)
)

# Managed Objects groups

tmnxRpkiOriginValidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 96, 2, 1)
)
tmnxRpkiOriginValidGroup.setObjects(
      *(("TIMETRA-RPKI-MIB", "vRtrRpkiSessInstanceRowStatus"),
        ("TIMETRA-RPKI-MIB", "vRtrRpkiSessInstanceConnectRetry"),
        ("TIMETRA-RPKI-MIB", "vRtrRpkiSessInstanceDescription"),
        ("TIMETRA-RPKI-MIB", "vRtrRpkiSessInstanceHoldTime"),
        ("TIMETRA-RPKI-MIB", "vRtrRpkiSessLocalAddressType"),
        ("TIMETRA-RPKI-MIB", "vRtrRpkiSessLocalAddress"),
        ("TIMETRA-RPKI-MIB", "vRtrRpkiSessInstancePort"),
        ("TIMETRA-RPKI-MIB", "vRtrRpkiSessInstanceRefreshTime"),
        ("TIMETRA-RPKI-MIB", "vRtrRpkiSessInstanceAdminState"),
        ("TIMETRA-RPKI-MIB", "vRtrRpkiSessInstanceStaleRoutTim"),
        ("TIMETRA-RPKI-MIB", "vRtrRpkiSessInstanceSessionState"),
        ("TIMETRA-RPKI-MIB", "vRtrRpkiSessInstanceSessionFlaps"),
        ("TIMETRA-RPKI-MIB", "vRtrRpkiSessInstanceUptime"),
        ("TIMETRA-RPKI-MIB", "vRtrRpkiSessInstanceActIpv4Rec"),
        ("TIMETRA-RPKI-MIB", "vRtrRpkiSessInstanceActIpv6Rec"),
        ("TIMETRA-RPKI-MIB", "vRtrOrigValStaticRowStatus"),
        ("TIMETRA-RPKI-MIB", "vRtrOrigValStaticASValidity"),
        ("TIMETRA-RPKI-MIB", "vRtrOrigValASRouteValidity"),
        ("TIMETRA-RPKI-MIB", "vRtrRpkiSessInstanceSerialId"),
        ("TIMETRA-RPKI-MIB", "vRtrRpkiSessInstanceSessionId"),
        ("TIMETRA-RPKI-MIB", "vRtrRpkiSessInstanceLastChange"))
)
if mibBuilder.loadTexts:
    tmnxRpkiOriginValidGroup.setStatus("current")

tmnxRpkiNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 96, 2, 2)
)
tmnxRpkiNotifyObjsGroup.setObjects(
      *(("TIMETRA-RPKI-MIB", "tmnxRpkiErrorType"),
        ("TIMETRA-RPKI-MIB", "tmnxRpkiPeerAddr"),
        ("TIMETRA-RPKI-MIB", "tmnxRpkiPeerAddrType"),
        ("TIMETRA-RPKI-MIB", "tmnxRpkiTrapStatus"))
)
if mibBuilder.loadTexts:
    tmnxRpkiNotifyObjsGroup.setStatus("current")


# Notification objects

tmnxRpkiNotifySession = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 96, 0, 1)
)
tmnxRpkiNotifySession.setObjects(
      *(("TIMETRA-RPKI-MIB", "tmnxRpkiPeerAddrType"),
        ("TIMETRA-RPKI-MIB", "tmnxRpkiPeerAddr"),
        ("TIMETRA-RPKI-MIB", "tmnxRpkiErrorType"),
        ("TIMETRA-RPKI-MIB", "tmnxRpkiTrapStatus"))
)
if mibBuilder.loadTexts:
    tmnxRpkiNotifySession.setStatus(
        "current"
    )

tmnxRpkiStaleTimerExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 96, 0, 2)
)
tmnxRpkiStaleTimerExpiry.setObjects(
      *(("TIMETRA-RPKI-MIB", "tmnxRpkiPeerAddrType"),
        ("TIMETRA-RPKI-MIB", "tmnxRpkiPeerAddr"))
)
if mibBuilder.loadTexts:
    tmnxRpkiStaleTimerExpiry.setStatus(
        "current"
    )


# Notifications groups

tmnxRpkiNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 96, 2, 3)
)
tmnxRpkiNotificationGroup.setObjects(
      *(("TIMETRA-RPKI-MIB", "tmnxRpkiNotifySession"),
        ("TIMETRA-RPKI-MIB", "tmnxRpkiStaleTimerExpiry"))
)
if mibBuilder.loadTexts:
    tmnxRpkiNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxOriginValidV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 96, 1, 1)
)
tmnxOriginValidV12v0Compliance.setObjects(
      *(("TIMETRA-RPKI-MIB", "tmnxRpkiOriginValidGroup"),
        ("TIMETRA-RPKI-MIB", "tmnxRpkiNotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxOriginValidV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-RPKI-MIB",
    **{"timetraRpkiOriginValidMIBModule": timetraRpkiOriginValidMIBModule,
       "tmnxRpkiConformance": tmnxRpkiConformance,
       "tmnxRpkiCompliances": tmnxRpkiCompliances,
       "tmnxOriginValidV12v0Compliance": tmnxOriginValidV12v0Compliance,
       "tmnxRpkiGroups": tmnxRpkiGroups,
       "tmnxRpkiOriginValidGroup": tmnxRpkiOriginValidGroup,
       "tmnxRpkiNotifyObjsGroup": tmnxRpkiNotifyObjsGroup,
       "tmnxRpkiNotificationGroup": tmnxRpkiNotificationGroup,
       "tmnxRpkiObjs": tmnxRpkiObjs,
       "vRtrRpkiSessInstanceTable": vRtrRpkiSessInstanceTable,
       "vRtrRpkiSessInstanceEntry": vRtrRpkiSessInstanceEntry,
       "vRtrRpkiSessInstanceAddressType": vRtrRpkiSessInstanceAddressType,
       "vRtrRpkiSessInstanceAddress": vRtrRpkiSessInstanceAddress,
       "vRtrRpkiSessInstanceRowStatus": vRtrRpkiSessInstanceRowStatus,
       "vRtrRpkiSessInstanceConnectRetry": vRtrRpkiSessInstanceConnectRetry,
       "vRtrRpkiSessInstanceDescription": vRtrRpkiSessInstanceDescription,
       "vRtrRpkiSessInstanceHoldTime": vRtrRpkiSessInstanceHoldTime,
       "vRtrRpkiSessLocalAddressType": vRtrRpkiSessLocalAddressType,
       "vRtrRpkiSessLocalAddress": vRtrRpkiSessLocalAddress,
       "vRtrRpkiSessInstancePort": vRtrRpkiSessInstancePort,
       "vRtrRpkiSessInstanceRefreshTime": vRtrRpkiSessInstanceRefreshTime,
       "vRtrRpkiSessInstanceAdminState": vRtrRpkiSessInstanceAdminState,
       "vRtrRpkiSessInstanceStaleRoutTim": vRtrRpkiSessInstanceStaleRoutTim,
       "vRtrRpkiSessInstanceSessionState": vRtrRpkiSessInstanceSessionState,
       "vRtrRpkiSessInstanceSessionFlaps": vRtrRpkiSessInstanceSessionFlaps,
       "vRtrRpkiSessInstanceUptime": vRtrRpkiSessInstanceUptime,
       "vRtrRpkiSessInstanceActIpv4Rec": vRtrRpkiSessInstanceActIpv4Rec,
       "vRtrRpkiSessInstanceActIpv6Rec": vRtrRpkiSessInstanceActIpv6Rec,
       "vRtrRpkiSessInstanceSerialId": vRtrRpkiSessInstanceSerialId,
       "vRtrRpkiSessInstanceSessionId": vRtrRpkiSessInstanceSessionId,
       "vRtrRpkiSessInstanceLastChange": vRtrRpkiSessInstanceLastChange,
       "vRtrOriginValStaticTable": vRtrOriginValStaticTable,
       "vRtrOriginValStaticEntry": vRtrOriginValStaticEntry,
       "vRtrOrigValStaticIpPrefixType": vRtrOrigValStaticIpPrefixType,
       "vRtrOrigValStaticIpPrefix": vRtrOrigValStaticIpPrefix,
       "vRtrOrigValStaticMinPrefixLen": vRtrOrigValStaticMinPrefixLen,
       "vRtrOrigValStaticMaxPrefixLen": vRtrOrigValStaticMaxPrefixLen,
       "vRtrOrigValStaticAS4Byte": vRtrOrigValStaticAS4Byte,
       "vRtrOrigValStaticRowStatus": vRtrOrigValStaticRowStatus,
       "vRtrOrigValStaticASValidity": vRtrOrigValStaticASValidity,
       "vRtrOriginValRouteTable": vRtrOriginValRouteTable,
       "vRtrOriginValRouteEntry": vRtrOriginValRouteEntry,
       "vRtrOrigValRouteIpPrefixType": vRtrOrigValRouteIpPrefixType,
       "vRtrOrigValRouteIpPrefix": vRtrOrigValRouteIpPrefix,
       "vRtrOrigValRouteMinPrefixLen": vRtrOrigValRouteMinPrefixLen,
       "vRtrOrigValRouteMaxPrefixLen": vRtrOrigValRouteMaxPrefixLen,
       "vRtrOrigValRouteAS4Byte": vRtrOrigValRouteAS4Byte,
       "vRtrOrigValRouteType": vRtrOrigValRouteType,
       "vRtrOrigValRouteRpkiVrId": vRtrOrigValRouteRpkiVrId,
       "vRtrOrigValRouteRpkiAddrType": vRtrOrigValRouteRpkiAddrType,
       "vRtrOrigValRouteRpkiAddress": vRtrOrigValRouteRpkiAddress,
       "vRtrOrigValASRouteValidity": vRtrOrigValASRouteValidity,
       "tmnxRpkiNotificationObjs": tmnxRpkiNotificationObjs,
       "tmnxRpkiPeerAddrType": tmnxRpkiPeerAddrType,
       "tmnxRpkiPeerAddr": tmnxRpkiPeerAddr,
       "tmnxRpkiErrorType": tmnxRpkiErrorType,
       "tmnxRpkiTrapStatus": tmnxRpkiTrapStatus,
       "tmnxRpkiNotifyPrefix": tmnxRpkiNotifyPrefix,
       "tmnxRpkiNotifications": tmnxRpkiNotifications,
       "tmnxRpkiNotifySession": tmnxRpkiNotifySession,
       "tmnxRpkiStaleTimerExpiry": tmnxRpkiStaleTimerExpiry}
)

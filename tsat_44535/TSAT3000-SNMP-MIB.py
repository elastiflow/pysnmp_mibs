# SNMP MIB module (TSAT3000-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/tsat_44535/TSAT3000-SNMP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:05:18 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

tsat = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 44535)
)
if mibBuilder.loadTexts:
    tsat.setRevisions(
        ("2016-09-19 07:11",
         "2014-10-09 09:43")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tsat3000_ObjectIdentity = ObjectIdentity
tsat3000 = _Tsat3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44535, 1)
)
_Tsat3000Nms_ObjectIdentity = ObjectIdentity
tsat3000Nms = _Tsat3000Nms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44535, 1, 1)
)
_Tsat3000NmsNotifications_ObjectIdentity = ObjectIdentity
tsat3000NmsNotifications = _Tsat3000NmsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44535, 1, 1, 0)
)
_Tsat3000NmsName_Type = OctetString
_Tsat3000NmsName_Object = MibScalar
tsat3000NmsName = _Tsat3000NmsName_Object(
    (1, 3, 6, 1, 4, 1, 44535, 1, 1, 1),
    _Tsat3000NmsName_Type()
)
tsat3000NmsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsat3000NmsName.setStatus("current")
if mibBuilder.loadTexts:
    tsat3000NmsName.setUnits("The OCTET STRING type represents arbitrary binary or textual data of maximum 255 octets.")


class _Tsat3000NmsStatus_Type(Integer32):
    """Custom type tsat3000NmsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Tsat3000NmsStatus_Type.__name__ = "Integer32"
_Tsat3000NmsStatus_Object = MibScalar
tsat3000NmsStatus = _Tsat3000NmsStatus_Object(
    (1, 3, 6, 1, 4, 1, 44535, 1, 1, 2),
    _Tsat3000NmsStatus_Type()
)
tsat3000NmsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsat3000NmsStatus.setStatus("current")
if mibBuilder.loadTexts:
    tsat3000NmsStatus.setUnits("0 = link down (most likely means that the NMS is down) 1 = link up")
_Tsat3000NmsUptime_Type = TimeTicks
_Tsat3000NmsUptime_Object = MibScalar
tsat3000NmsUptime = _Tsat3000NmsUptime_Object(
    (1, 3, 6, 1, 4, 1, 44535, 1, 1, 3),
    _Tsat3000NmsUptime_Type()
)
tsat3000NmsUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsat3000NmsUptime.setStatus("current")
if mibBuilder.loadTexts:
    tsat3000NmsUptime.setUnits("TimeTicks represents a non-negative integer which represents the time, modulo 2^32 (4294967296 decimal), in hundredths of a second between two epochs.")


class _Tsat3000NmsPort_Type(Integer32):
    """Custom type tsat3000NmsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Tsat3000NmsPort_Type.__name__ = "Integer32"
_Tsat3000NmsPort_Object = MibScalar
tsat3000NmsPort = _Tsat3000NmsPort_Object(
    (1, 3, 6, 1, 4, 1, 44535, 1, 1, 4),
    _Tsat3000NmsPort_Type()
)
tsat3000NmsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsat3000NmsPort.setStatus("current")
if mibBuilder.loadTexts:
    tsat3000NmsPort.setUnits("Range: 1-1068")


class _Tsat3000NmsAppIdleStatus_Type(Integer32):
    """Custom type tsat3000NmsAppIdleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Tsat3000NmsAppIdleStatus_Type.__name__ = "Integer32"
_Tsat3000NmsAppIdleStatus_Object = MibScalar
tsat3000NmsAppIdleStatus = _Tsat3000NmsAppIdleStatus_Object(
    (1, 3, 6, 1, 4, 1, 44535, 1, 1, 5),
    _Tsat3000NmsAppIdleStatus_Type()
)
tsat3000NmsAppIdleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsat3000NmsAppIdleStatus.setStatus("current")
if mibBuilder.loadTexts:
    tsat3000NmsAppIdleStatus.setUnits("0 = not ok 1 = ok")


class _Tsat3000NmsPortStatus_Type(Integer32):
    """Custom type tsat3000NmsPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Tsat3000NmsPortStatus_Type.__name__ = "Integer32"
_Tsat3000NmsPortStatus_Object = MibScalar
tsat3000NmsPortStatus = _Tsat3000NmsPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 44535, 1, 1, 6),
    _Tsat3000NmsPortStatus_Type()
)
tsat3000NmsPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsat3000NmsPortStatus.setStatus("current")
if mibBuilder.loadTexts:
    tsat3000NmsPortStatus.setUnits("0 = not ok 1 = ok")
_Tsat3000Hub_ObjectIdentity = ObjectIdentity
tsat3000Hub = _Tsat3000Hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44535, 1, 2)
)
_Tsat3000HubNotifications_ObjectIdentity = ObjectIdentity
tsat3000HubNotifications = _Tsat3000HubNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44535, 1, 2, 0)
)


class _Tsat3000HubId_Type(Integer32):
    """Custom type tsat3000HubId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Tsat3000HubId_Type.__name__ = "Integer32"
_Tsat3000HubId_Object = MibScalar
tsat3000HubId = _Tsat3000HubId_Object(
    (1, 3, 6, 1, 4, 1, 44535, 1, 2, 1),
    _Tsat3000HubId_Type()
)
tsat3000HubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsat3000HubId.setStatus("current")
_Tsat3000HubName_Type = OctetString
_Tsat3000HubName_Object = MibScalar
tsat3000HubName = _Tsat3000HubName_Object(
    (1, 3, 6, 1, 4, 1, 44535, 1, 2, 2),
    _Tsat3000HubName_Type()
)
tsat3000HubName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsat3000HubName.setStatus("current")
if mibBuilder.loadTexts:
    tsat3000HubName.setUnits("The OCTET STRING type represents arbitrary binary or textual data of maximum 255 octets.")


class _Tsat3000HubStatus_Type(Integer32):
    """Custom type tsat3000HubStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Tsat3000HubStatus_Type.__name__ = "Integer32"
_Tsat3000HubStatus_Object = MibScalar
tsat3000HubStatus = _Tsat3000HubStatus_Object(
    (1, 3, 6, 1, 4, 1, 44535, 1, 2, 3),
    _Tsat3000HubStatus_Type()
)
tsat3000HubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsat3000HubStatus.setStatus("current")
if mibBuilder.loadTexts:
    tsat3000HubStatus.setUnits("0 = NMS to HUB link down 1 = NMS to HUB link up, HUB searching for HUB 2 = NMS to HUB link up, HUB searching for RTs 3 = NMS to HUB link up, emergency polling 4 = NMS to HUB link up, all ok")
_Tsat3000HubUptime_Type = TimeTicks
_Tsat3000HubUptime_Object = MibScalar
tsat3000HubUptime = _Tsat3000HubUptime_Object(
    (1, 3, 6, 1, 4, 1, 44535, 1, 2, 4),
    _Tsat3000HubUptime_Type()
)
tsat3000HubUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsat3000HubUptime.setStatus("current")
if mibBuilder.loadTexts:
    tsat3000HubUptime.setUnits("TimeTicks represents a non-negative integer which represents the time, modulo 2^32 (4294967296 decimal), in hundredths of a second between two epochs.")


class _Tsat3000HubLoad_Type(Integer32):
    """Custom type tsat3000HubLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Tsat3000HubLoad_Type.__name__ = "Integer32"
_Tsat3000HubLoad_Object = MibScalar
tsat3000HubLoad = _Tsat3000HubLoad_Object(
    (1, 3, 6, 1, 4, 1, 44535, 1, 2, 5),
    _Tsat3000HubLoad_Type()
)
tsat3000HubLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsat3000HubLoad.setStatus("current")
if mibBuilder.loadTexts:
    tsat3000HubLoad.setUnits("0 = not ok 1 = ok")


class _Tsat3000HubToNmsLinkStatus_Type(Integer32):
    """Custom type tsat3000HubToNmsLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Tsat3000HubToNmsLinkStatus_Type.__name__ = "Integer32"
_Tsat3000HubToNmsLinkStatus_Object = MibScalar
tsat3000HubToNmsLinkStatus = _Tsat3000HubToNmsLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 44535, 1, 2, 6),
    _Tsat3000HubToNmsLinkStatus_Type()
)
tsat3000HubToNmsLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsat3000HubToNmsLinkStatus.setStatus("current")
if mibBuilder.loadTexts:
    tsat3000HubToNmsLinkStatus.setUnits("0 = not ok 1 = ok")
_Tsat3000Rt_ObjectIdentity = ObjectIdentity
tsat3000Rt = _Tsat3000Rt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44535, 1, 3)
)
_Tsat3000RtNotifications_ObjectIdentity = ObjectIdentity
tsat3000RtNotifications = _Tsat3000RtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44535, 1, 3, 0)
)


class _Tsat3000RtId_Type(Integer32):
    """Custom type tsat3000RtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Tsat3000RtId_Type.__name__ = "Integer32"
_Tsat3000RtId_Object = MibScalar
tsat3000RtId = _Tsat3000RtId_Object(
    (1, 3, 6, 1, 4, 1, 44535, 1, 3, 1),
    _Tsat3000RtId_Type()
)
tsat3000RtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsat3000RtId.setStatus("current")


class _Tsat3000RtStatus_Type(Integer32):
    """Custom type tsat3000RtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Tsat3000RtStatus_Type.__name__ = "Integer32"
_Tsat3000RtStatus_Object = MibScalar
tsat3000RtStatus = _Tsat3000RtStatus_Object(
    (1, 3, 6, 1, 4, 1, 44535, 1, 3, 2),
    _Tsat3000RtStatus_Type()
)
tsat3000RtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsat3000RtStatus.setStatus("current")
if mibBuilder.loadTexts:
    tsat3000RtStatus.setUnits("0 = link down 1 = link up")
_Tsat3000RtUptime_Type = TimeTicks
_Tsat3000RtUptime_Object = MibScalar
tsat3000RtUptime = _Tsat3000RtUptime_Object(
    (1, 3, 6, 1, 4, 1, 44535, 1, 3, 3),
    _Tsat3000RtUptime_Type()
)
tsat3000RtUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsat3000RtUptime.setStatus("current")
if mibBuilder.loadTexts:
    tsat3000RtUptime.setUnits("TimeTicks represents a non-negative integer which represents the time, modulo 2^32 (4294967296 decimal), in hundredths of a second between two epochs.")


class _Tsat3000RtEbNoStatus_Type(Integer32):
    """Custom type tsat3000RtEbNoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Tsat3000RtEbNoStatus_Type.__name__ = "Integer32"
_Tsat3000RtEbNoStatus_Object = MibScalar
tsat3000RtEbNoStatus = _Tsat3000RtEbNoStatus_Object(
    (1, 3, 6, 1, 4, 1, 44535, 1, 3, 4),
    _Tsat3000RtEbNoStatus_Type()
)
tsat3000RtEbNoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsat3000RtEbNoStatus.setStatus("current")
if mibBuilder.loadTexts:
    tsat3000RtEbNoStatus.setUnits("0 = not ok 1 = ok")


class _Tsat3000RtCrcStatus_Type(Integer32):
    """Custom type tsat3000RtCrcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Tsat3000RtCrcStatus_Type.__name__ = "Integer32"
_Tsat3000RtCrcStatus_Object = MibScalar
tsat3000RtCrcStatus = _Tsat3000RtCrcStatus_Object(
    (1, 3, 6, 1, 4, 1, 44535, 1, 3, 5),
    _Tsat3000RtCrcStatus_Type()
)
tsat3000RtCrcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsat3000RtCrcStatus.setStatus("current")
if mibBuilder.loadTexts:
    tsat3000RtCrcStatus.setUnits("0 = not ok 1 = ok")


class _Tsat3000RtName_Type(Integer32):
    """Custom type tsat3000RtName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Tsat3000RtName_Type.__name__ = "Integer32"
_Tsat3000RtName_Object = MibScalar
tsat3000RtName = _Tsat3000RtName_Object(
    (1, 3, 6, 1, 4, 1, 44535, 1, 3, 6),
    _Tsat3000RtName_Type()
)
tsat3000RtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsat3000RtName.setStatus("current")
_Tsat3000Conformance_ObjectIdentity = ObjectIdentity
tsat3000Conformance = _Tsat3000Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44535, 1, 10)
)
_Tsat3000ConformanceNms_ObjectIdentity = ObjectIdentity
tsat3000ConformanceNms = _Tsat3000ConformanceNms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44535, 1, 10, 1)
)
_Tsat3000ConformanceHub_ObjectIdentity = ObjectIdentity
tsat3000ConformanceHub = _Tsat3000ConformanceHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44535, 1, 10, 2)
)
_Tsat3000ConformanceRt_ObjectIdentity = ObjectIdentity
tsat3000ConformanceRt = _Tsat3000ConformanceRt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44535, 1, 10, 3)
)
_Tsat3000NotificationGenerics_ObjectIdentity = ObjectIdentity
tsat3000NotificationGenerics = _Tsat3000NotificationGenerics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44535, 1, 10, 4)
)
_Tsat3000NotificationDescription_Type = OctetString
_Tsat3000NotificationDescription_Object = MibScalar
tsat3000NotificationDescription = _Tsat3000NotificationDescription_Object(
    (1, 3, 6, 1, 4, 1, 44535, 1, 10, 4, 1),
    _Tsat3000NotificationDescription_Type()
)
tsat3000NotificationDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsat3000NotificationDescription.setStatus("current")


class _Tsat3000NotificationSeverity_Type(Integer32):
    """Custom type tsat3000NotificationSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Tsat3000NotificationSeverity_Type.__name__ = "Integer32"
_Tsat3000NotificationSeverity_Object = MibScalar
tsat3000NotificationSeverity = _Tsat3000NotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 44535, 1, 10, 4, 2),
    _Tsat3000NotificationSeverity_Type()
)
tsat3000NotificationSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsat3000NotificationSeverity.setStatus("current")
if mibBuilder.loadTexts:
    tsat3000NotificationSeverity.setUnits("0: undefined 1: informational 2: minor 3: major 4: critical")

# Managed Objects groups

tsat3000NmsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44535, 1, 10, 1, 2)
)
tsat3000NmsObjectGroup.setObjects(
      *(("TSAT3000-SNMP-MIB", "tsat3000NmsName"),
        ("TSAT3000-SNMP-MIB", "tsat3000NmsStatus"),
        ("TSAT3000-SNMP-MIB", "tsat3000NmsUptime"),
        ("TSAT3000-SNMP-MIB", "tsat3000NmsPort"),
        ("TSAT3000-SNMP-MIB", "tsat3000NmsAppIdleStatus"),
        ("TSAT3000-SNMP-MIB", "tsat3000NmsPortStatus"))
)
if mibBuilder.loadTexts:
    tsat3000NmsObjectGroup.setStatus("current")

tsat3000HubObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44535, 1, 10, 2, 2)
)
tsat3000HubObjectGroup.setObjects(
      *(("TSAT3000-SNMP-MIB", "tsat3000HubId"),
        ("TSAT3000-SNMP-MIB", "tsat3000HubName"),
        ("TSAT3000-SNMP-MIB", "tsat3000HubStatus"),
        ("TSAT3000-SNMP-MIB", "tsat3000HubUptime"),
        ("TSAT3000-SNMP-MIB", "tsat3000HubLoad"),
        ("TSAT3000-SNMP-MIB", "tsat3000HubToNmsLinkStatus"))
)
if mibBuilder.loadTexts:
    tsat3000HubObjectGroup.setStatus("current")

tsat3000RtObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44535, 1, 10, 3, 2)
)
tsat3000RtObjectGroup.setObjects(
      *(("TSAT3000-SNMP-MIB", "tsat3000RtId"),
        ("TSAT3000-SNMP-MIB", "tsat3000RtStatus"),
        ("TSAT3000-SNMP-MIB", "tsat3000RtUptime"),
        ("TSAT3000-SNMP-MIB", "tsat3000RtEbNoStatus"),
        ("TSAT3000-SNMP-MIB", "tsat3000RtCrcStatus"),
        ("TSAT3000-SNMP-MIB", "tsat3000RtName"))
)
if mibBuilder.loadTexts:
    tsat3000RtObjectGroup.setStatus("current")

tsat3000NotificationGenericsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44535, 1, 10, 4, 3)
)
tsat3000NotificationGenericsGroup.setObjects(
      *(("TSAT3000-SNMP-MIB", "tsat3000NotificationDescription"),
        ("TSAT3000-SNMP-MIB", "tsat3000NotificationSeverity"))
)
if mibBuilder.loadTexts:
    tsat3000NotificationGenericsGroup.setStatus("current")


# Notification objects

tsat3000NmsStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44535, 1, 1, 0, 1)
)
tsat3000NmsStatusNotification.setObjects(
      *(("TSAT3000-SNMP-MIB", "tsat3000NmsName"),
        ("TSAT3000-SNMP-MIB", "tsat3000NmsStatus"),
        ("TSAT3000-SNMP-MIB", "tsat3000NmsUptime"),
        ("TSAT3000-SNMP-MIB", "tsat3000NotificationDescription"),
        ("TSAT3000-SNMP-MIB", "tsat3000NotificationSeverity"))
)
if mibBuilder.loadTexts:
    tsat3000NmsStatusNotification.setStatus(
        "current"
    )

tsat3000NmsPortNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44535, 1, 1, 0, 2)
)
tsat3000NmsPortNotification.setObjects(
      *(("TSAT3000-SNMP-MIB", "tsat3000NmsName"),
        ("TSAT3000-SNMP-MIB", "tsat3000NmsPort"),
        ("TSAT3000-SNMP-MIB", "tsat3000NmsPortStatus"),
        ("TSAT3000-SNMP-MIB", "tsat3000NotificationDescription"),
        ("TSAT3000-SNMP-MIB", "tsat3000NotificationSeverity"))
)
if mibBuilder.loadTexts:
    tsat3000NmsPortNotification.setStatus(
        "current"
    )

tsat3000NmsAppIdleNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44535, 1, 1, 0, 3)
)
tsat3000NmsAppIdleNotification.setObjects(
      *(("TSAT3000-SNMP-MIB", "tsat3000NmsName"),
        ("TSAT3000-SNMP-MIB", "tsat3000NmsPort"),
        ("TSAT3000-SNMP-MIB", "tsat3000NmsAppIdleStatus"),
        ("TSAT3000-SNMP-MIB", "tsat3000NotificationDescription"),
        ("TSAT3000-SNMP-MIB", "tsat3000NotificationSeverity"))
)
if mibBuilder.loadTexts:
    tsat3000NmsAppIdleNotification.setStatus(
        "current"
    )

tsat3000HubStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44535, 1, 2, 0, 1)
)
tsat3000HubStatusNotification.setObjects(
      *(("TSAT3000-SNMP-MIB", "tsat3000HubId"),
        ("TSAT3000-SNMP-MIB", "tsat3000HubName"),
        ("TSAT3000-SNMP-MIB", "tsat3000HubStatus"),
        ("TSAT3000-SNMP-MIB", "tsat3000HubUptime"),
        ("TSAT3000-SNMP-MIB", "tsat3000NotificationDescription"),
        ("TSAT3000-SNMP-MIB", "tsat3000NotificationSeverity"))
)
if mibBuilder.loadTexts:
    tsat3000HubStatusNotification.setStatus(
        "current"
    )

tsat3000HubLoadNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44535, 1, 2, 0, 2)
)
tsat3000HubLoadNotification.setObjects(
      *(("TSAT3000-SNMP-MIB", "tsat3000HubId"),
        ("TSAT3000-SNMP-MIB", "tsat3000HubName"),
        ("TSAT3000-SNMP-MIB", "tsat3000HubLoad"),
        ("TSAT3000-SNMP-MIB", "tsat3000NotificationDescription"),
        ("TSAT3000-SNMP-MIB", "tsat3000NotificationSeverity"))
)
if mibBuilder.loadTexts:
    tsat3000HubLoadNotification.setStatus(
        "current"
    )

tsat3000HubToNmsLinkNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44535, 1, 2, 0, 3)
)
tsat3000HubToNmsLinkNotification.setObjects(
      *(("TSAT3000-SNMP-MIB", "tsat3000HubId"),
        ("TSAT3000-SNMP-MIB", "tsat3000HubName"),
        ("TSAT3000-SNMP-MIB", "tsat3000HubToNmsLinkStatus"),
        ("TSAT3000-SNMP-MIB", "tsat3000NotificationDescription"),
        ("TSAT3000-SNMP-MIB", "tsat3000NotificationSeverity"))
)
if mibBuilder.loadTexts:
    tsat3000HubToNmsLinkNotification.setStatus(
        "current"
    )

tsat3000RtStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44535, 1, 3, 0, 1)
)
tsat3000RtStatusNotification.setObjects(
      *(("TSAT3000-SNMP-MIB", "tsat3000RtId"),
        ("TSAT3000-SNMP-MIB", "tsat3000RtName"),
        ("TSAT3000-SNMP-MIB", "tsat3000RtStatus"),
        ("TSAT3000-SNMP-MIB", "tsat3000RtUptime"),
        ("TSAT3000-SNMP-MIB", "tsat3000NotificationDescription"),
        ("TSAT3000-SNMP-MIB", "tsat3000NotificationSeverity"))
)
if mibBuilder.loadTexts:
    tsat3000RtStatusNotification.setStatus(
        "current"
    )

tsat3000RtCrcNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44535, 1, 3, 0, 2)
)
tsat3000RtCrcNotification.setObjects(
      *(("TSAT3000-SNMP-MIB", "tsat3000RtId"),
        ("TSAT3000-SNMP-MIB", "tsat3000RtName"),
        ("TSAT3000-SNMP-MIB", "tsat3000RtCrcStatus"),
        ("TSAT3000-SNMP-MIB", "tsat3000NotificationDescription"),
        ("TSAT3000-SNMP-MIB", "tsat3000NotificationSeverity"))
)
if mibBuilder.loadTexts:
    tsat3000RtCrcNotification.setStatus(
        "current"
    )

tsat3000RtEbNoNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44535, 1, 3, 0, 3)
)
tsat3000RtEbNoNotification.setObjects(
      *(("TSAT3000-SNMP-MIB", "tsat3000RtId"),
        ("TSAT3000-SNMP-MIB", "tsat3000RtName"),
        ("TSAT3000-SNMP-MIB", "tsat3000RtEbNoStatus"),
        ("TSAT3000-SNMP-MIB", "tsat3000NotificationDescription"),
        ("TSAT3000-SNMP-MIB", "tsat3000NotificationSeverity"))
)
if mibBuilder.loadTexts:
    tsat3000RtEbNoNotification.setStatus(
        "current"
    )


# Notifications groups

tsat3000NmsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 44535, 1, 10, 1, 1)
)
tsat3000NmsNotificationGroup.setObjects(
      *(("TSAT3000-SNMP-MIB", "tsat3000NmsStatusNotification"),
        ("TSAT3000-SNMP-MIB", "tsat3000NmsPortNotification"),
        ("TSAT3000-SNMP-MIB", "tsat3000NmsAppIdleNotification"),
        ("TSAT3000-SNMP-MIB", "tsat3000HubToNmsLinkNotification"))
)
if mibBuilder.loadTexts:
    tsat3000NmsNotificationGroup.setStatus(
        "current"
    )

tsat3000HubNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 44535, 1, 10, 2, 1)
)
tsat3000HubNotificationGroup.setObjects(
      *(("TSAT3000-SNMP-MIB", "tsat3000HubStatusNotification"),
        ("TSAT3000-SNMP-MIB", "tsat3000HubLoadNotification"))
)
if mibBuilder.loadTexts:
    tsat3000HubNotificationGroup.setStatus(
        "current"
    )

tsat3000RtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 44535, 1, 10, 3, 1)
)
tsat3000RtNotificationGroup.setObjects(
      *(("TSAT3000-SNMP-MIB", "tsat3000RtStatusNotification"),
        ("TSAT3000-SNMP-MIB", "tsat3000RtCrcNotification"),
        ("TSAT3000-SNMP-MIB", "tsat3000RtEbNoNotification"))
)
if mibBuilder.loadTexts:
    tsat3000RtNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TSAT3000-SNMP-MIB",
    **{"tsat": tsat,
       "tsat3000": tsat3000,
       "tsat3000Nms": tsat3000Nms,
       "tsat3000NmsNotifications": tsat3000NmsNotifications,
       "tsat3000NmsStatusNotification": tsat3000NmsStatusNotification,
       "tsat3000NmsPortNotification": tsat3000NmsPortNotification,
       "tsat3000NmsAppIdleNotification": tsat3000NmsAppIdleNotification,
       "tsat3000NmsName": tsat3000NmsName,
       "tsat3000NmsStatus": tsat3000NmsStatus,
       "tsat3000NmsUptime": tsat3000NmsUptime,
       "tsat3000NmsPort": tsat3000NmsPort,
       "tsat3000NmsAppIdleStatus": tsat3000NmsAppIdleStatus,
       "tsat3000NmsPortStatus": tsat3000NmsPortStatus,
       "tsat3000Hub": tsat3000Hub,
       "tsat3000HubNotifications": tsat3000HubNotifications,
       "tsat3000HubStatusNotification": tsat3000HubStatusNotification,
       "tsat3000HubLoadNotification": tsat3000HubLoadNotification,
       "tsat3000HubToNmsLinkNotification": tsat3000HubToNmsLinkNotification,
       "tsat3000HubId": tsat3000HubId,
       "tsat3000HubName": tsat3000HubName,
       "tsat3000HubStatus": tsat3000HubStatus,
       "tsat3000HubUptime": tsat3000HubUptime,
       "tsat3000HubLoad": tsat3000HubLoad,
       "tsat3000HubToNmsLinkStatus": tsat3000HubToNmsLinkStatus,
       "tsat3000Rt": tsat3000Rt,
       "tsat3000RtNotifications": tsat3000RtNotifications,
       "tsat3000RtStatusNotification": tsat3000RtStatusNotification,
       "tsat3000RtCrcNotification": tsat3000RtCrcNotification,
       "tsat3000RtEbNoNotification": tsat3000RtEbNoNotification,
       "tsat3000RtId": tsat3000RtId,
       "tsat3000RtStatus": tsat3000RtStatus,
       "tsat3000RtUptime": tsat3000RtUptime,
       "tsat3000RtEbNoStatus": tsat3000RtEbNoStatus,
       "tsat3000RtCrcStatus": tsat3000RtCrcStatus,
       "tsat3000RtName": tsat3000RtName,
       "tsat3000Conformance": tsat3000Conformance,
       "tsat3000ConformanceNms": tsat3000ConformanceNms,
       "tsat3000NmsNotificationGroup": tsat3000NmsNotificationGroup,
       "tsat3000NmsObjectGroup": tsat3000NmsObjectGroup,
       "tsat3000ConformanceHub": tsat3000ConformanceHub,
       "tsat3000HubNotificationGroup": tsat3000HubNotificationGroup,
       "tsat3000HubObjectGroup": tsat3000HubObjectGroup,
       "tsat3000ConformanceRt": tsat3000ConformanceRt,
       "tsat3000RtNotificationGroup": tsat3000RtNotificationGroup,
       "tsat3000RtObjectGroup": tsat3000RtObjectGroup,
       "tsat3000NotificationGenerics": tsat3000NotificationGenerics,
       "tsat3000NotificationDescription": tsat3000NotificationDescription,
       "tsat3000NotificationSeverity": tsat3000NotificationSeverity,
       "tsat3000NotificationGenericsGroup": tsat3000NotificationGenericsGroup}
)

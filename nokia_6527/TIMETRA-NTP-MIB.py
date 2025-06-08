# SNMP MIB module (TIMETRA-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-NTP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:39 2025
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

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TmnxAdminState,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TmnxAdminState",
    "TmnxOperState")

(vRtrID,) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID")


# MODULE-IDENTITY

timetraNtpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 38)
)
if mibBuilder.loadTexts:
    timetraNtpMIBModule.setRevisions(
        ("1908-01-01 00:00",
         "1906-03-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NTPTimeStamp(TextualConvention, OctetString):
    status = "current"
    displayHint = "4d.4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class NTPLeapIndicator(TextualConvention, Integer32):
    status = "current"
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
        *(("noWarning", 0),
          ("addSecond", 1),
          ("subtractSecond", 2),
          ("alarm", 3))
    )



class NTPSignedTimeValue(TextualConvention, OctetString):
    status = "current"
    displayHint = "4d.4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class NTPUnsignedTimeValue(TextualConvention, OctetString):
    status = "current"
    displayHint = "4d.4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class NTPStratum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class NTPRefId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



class NTPPollInterval(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )



class NTPAssocIdentifier(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class NTPVersion(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )



class TmnxNtpDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transmit", 1),
          ("receive", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxNtpConformance_ObjectIdentity = ObjectIdentity
tmnxNtpConformance = _TmnxNtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38)
)
_TmnxNtpCompliances_ObjectIdentity = ObjectIdentity
tmnxNtpCompliances = _TmnxNtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 1)
)
_TmnxNtpGroups_ObjectIdentity = ObjectIdentity
tmnxNtpGroups = _TmnxNtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 2)
)
_TmnxNtpObjs_ObjectIdentity = ObjectIdentity
tmnxNtpObjs = _TmnxNtpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38)
)
_TmnxNtpSysObjs_ObjectIdentity = ObjectIdentity
tmnxNtpSysObjs = _TmnxNtpSysObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1)
)
_TmnxNtpSystem_ObjectIdentity = ObjectIdentity
tmnxNtpSystem = _TmnxNtpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 1)
)
_TmnxNtpSysLeap_Type = NTPLeapIndicator
_TmnxNtpSysLeap_Object = MibScalar
tmnxNtpSysLeap = _TmnxNtpSysLeap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 1, 1),
    _TmnxNtpSysLeap_Type()
)
tmnxNtpSysLeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpSysLeap.setStatus("current")
_TmnxNtpSysStratum_Type = NTPStratum
_TmnxNtpSysStratum_Object = MibScalar
tmnxNtpSysStratum = _TmnxNtpSysStratum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 1, 2),
    _TmnxNtpSysStratum_Type()
)
tmnxNtpSysStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpSysStratum.setStatus("current")
_TmnxNtpSysRefId_Type = NTPRefId
_TmnxNtpSysRefId_Object = MibScalar
tmnxNtpSysRefId = _TmnxNtpSysRefId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 1, 3),
    _TmnxNtpSysRefId_Type()
)
tmnxNtpSysRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpSysRefId.setStatus("current")
_TmnxNtpSysRefTime_Type = NTPTimeStamp
_TmnxNtpSysRefTime_Object = MibScalar
tmnxNtpSysRefTime = _TmnxNtpSysRefTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 1, 4),
    _TmnxNtpSysRefTime_Type()
)
tmnxNtpSysRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpSysRefTime.setStatus("current")
_TmnxNtpSysPoll_Type = NTPPollInterval
_TmnxNtpSysPoll_Object = MibScalar
tmnxNtpSysPoll = _TmnxNtpSysPoll_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 1, 5),
    _TmnxNtpSysPoll_Type()
)
tmnxNtpSysPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpSysPoll.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNtpSysPoll.setUnits("seconds as a power of two")
_TmnxNtpSysPeer_Type = NTPAssocIdentifier
_TmnxNtpSysPeer_Object = MibScalar
tmnxNtpSysPeer = _TmnxNtpSysPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 1, 6),
    _TmnxNtpSysPeer_Type()
)
tmnxNtpSysPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpSysPeer.setStatus("current")
_TmnxNtpSysClock_Type = NTPTimeStamp
_TmnxNtpSysClock_Object = MibScalar
tmnxNtpSysClock = _TmnxNtpSysClock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 1, 7),
    _TmnxNtpSysClock_Type()
)
tmnxNtpSysClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpSysClock.setStatus("current")


class _TmnxNtp_Type(Integer32):
    """Custom type tmnxNtp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TmnxNtp_Type.__name__ = "Integer32"
_TmnxNtp_Object = MibScalar
tmnxNtp = _TmnxNtp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 1, 8),
    _TmnxNtp_Type()
)
tmnxNtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNtp.setStatus("obsolete")


class _TmnxNtpAdminState_Type(Integer32):
    """Custom type tmnxNtpAdminState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("inService", 2),
          ("outOfService", 3))
    )


_TmnxNtpAdminState_Type.__name__ = "Integer32"
_TmnxNtpAdminState_Object = MibScalar
tmnxNtpAdminState = _TmnxNtpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 1, 9),
    _TmnxNtpAdminState_Type()
)
tmnxNtpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNtpAdminState.setStatus("obsolete")


class _TmnxNtpOperState_Type(Integer32):
    """Custom type tmnxNtpOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("inService", 2),
          ("outOfService", 3))
    )


_TmnxNtpOperState_Type.__name__ = "Integer32"
_TmnxNtpOperState_Object = MibScalar
tmnxNtpOperState = _TmnxNtpOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 1, 10),
    _TmnxNtpOperState_Type()
)
tmnxNtpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpOperState.setStatus("current")


class _TmnxNtpServer_Type(TruthValue):
    """Custom type tmnxNtpServer based on TruthValue"""
    defaultValue = 2


_TmnxNtpServer_Type.__name__ = "TruthValue"
_TmnxNtpServer_Object = MibScalar
tmnxNtpServer = _TmnxNtpServer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 1, 11),
    _TmnxNtpServer_Type()
)
tmnxNtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNtpServer.setStatus("obsolete")


class _TmnxNtpServerKeyId_Type(Unsigned32):
    """Custom type tmnxNtpServerKeyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_TmnxNtpServerKeyId_Type.__name__ = "Unsigned32"
_TmnxNtpServerKeyId_Object = MibScalar
tmnxNtpServerKeyId = _TmnxNtpServerKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 1, 12),
    _TmnxNtpServerKeyId_Type()
)
tmnxNtpServerKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNtpServerKeyId.setStatus("obsolete")


class _TmnxNtpAuthCheck_Type(TruthValue):
    """Custom type tmnxNtpAuthCheck based on TruthValue"""
    defaultValue = 1


_TmnxNtpAuthCheck_Type.__name__ = "TruthValue"
_TmnxNtpAuthCheck_Object = MibScalar
tmnxNtpAuthCheck = _TmnxNtpAuthCheck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 1, 13),
    _TmnxNtpAuthCheck_Type()
)
tmnxNtpAuthCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNtpAuthCheck.setStatus("obsolete")
_TmnxNtpBroadcastTable_Object = MibTable
tmnxNtpBroadcastTable = _TmnxNtpBroadcastTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxNtpBroadcastTable.setStatus("current")
_TmnxNtpBroadcastEntry_Object = MibTableRow
tmnxNtpBroadcastEntry = _TmnxNtpBroadcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 2, 1)
)
tmnxNtpBroadcastEntry.setIndexNames(
    (0, "TIMETRA-NTP-MIB", "tmnxNtpBroadcastDirection"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NTP-MIB", "tmnxNtpBroadcastIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxNtpBroadcastEntry.setStatus("current")
_TmnxNtpBroadcastDirection_Type = TmnxNtpDirection
_TmnxNtpBroadcastDirection_Object = MibTableColumn
tmnxNtpBroadcastDirection = _TmnxNtpBroadcastDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 2, 1, 1),
    _TmnxNtpBroadcastDirection_Type()
)
tmnxNtpBroadcastDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNtpBroadcastDirection.setStatus("current")
_TmnxNtpBroadcastIfIndex_Type = InterfaceIndex
_TmnxNtpBroadcastIfIndex_Object = MibTableColumn
tmnxNtpBroadcastIfIndex = _TmnxNtpBroadcastIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 2, 1, 2),
    _TmnxNtpBroadcastIfIndex_Type()
)
tmnxNtpBroadcastIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNtpBroadcastIfIndex.setStatus("current")
_TmnxNtpBroadcastEntryStatus_Type = RowStatus
_TmnxNtpBroadcastEntryStatus_Object = MibTableColumn
tmnxNtpBroadcastEntryStatus = _TmnxNtpBroadcastEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 2, 1, 3),
    _TmnxNtpBroadcastEntryStatus_Type()
)
tmnxNtpBroadcastEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpBroadcastEntryStatus.setStatus("current")
_TmnxNtpBroadcastLastChanged_Type = TimeStamp
_TmnxNtpBroadcastLastChanged_Object = MibTableColumn
tmnxNtpBroadcastLastChanged = _TmnxNtpBroadcastLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 2, 1, 4),
    _TmnxNtpBroadcastLastChanged_Type()
)
tmnxNtpBroadcastLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpBroadcastLastChanged.setStatus("current")


class _TmnxNtpBroadcastAuthKeyId_Type(Unsigned32):
    """Custom type tmnxNtpBroadcastAuthKeyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_TmnxNtpBroadcastAuthKeyId_Type.__name__ = "Unsigned32"
_TmnxNtpBroadcastAuthKeyId_Object = MibTableColumn
tmnxNtpBroadcastAuthKeyId = _TmnxNtpBroadcastAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 2, 1, 5),
    _TmnxNtpBroadcastAuthKeyId_Type()
)
tmnxNtpBroadcastAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpBroadcastAuthKeyId.setStatus("current")


class _TmnxNtpBroadcastVersion_Type(NTPVersion):
    """Custom type tmnxNtpBroadcastVersion based on NTPVersion"""
    defaultValue = 4


_TmnxNtpBroadcastVersion_Type.__name__ = "NTPVersion"
_TmnxNtpBroadcastVersion_Object = MibTableColumn
tmnxNtpBroadcastVersion = _TmnxNtpBroadcastVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 2, 1, 6),
    _TmnxNtpBroadcastVersion_Type()
)
tmnxNtpBroadcastVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpBroadcastVersion.setStatus("current")


class _TmnxNtpBroadcastTtl_Type(Unsigned32):
    """Custom type tmnxNtpBroadcastTtl based on Unsigned32"""
    defaultValue = 127

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxNtpBroadcastTtl_Type.__name__ = "Unsigned32"
_TmnxNtpBroadcastTtl_Object = MibTableColumn
tmnxNtpBroadcastTtl = _TmnxNtpBroadcastTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 2, 1, 7),
    _TmnxNtpBroadcastTtl_Type()
)
tmnxNtpBroadcastTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpBroadcastTtl.setStatus("current")
_TmnxNtpBroadcastAuthErrs_Type = Counter32
_TmnxNtpBroadcastAuthErrs_Object = MibTableColumn
tmnxNtpBroadcastAuthErrs = _TmnxNtpBroadcastAuthErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 2, 1, 8),
    _TmnxNtpBroadcastAuthErrs_Type()
)
tmnxNtpBroadcastAuthErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpBroadcastAuthErrs.setStatus("current")


class _TmnxNtpBroadcastAuthenticate_Type(TruthValue):
    """Custom type tmnxNtpBroadcastAuthenticate based on TruthValue"""
    defaultValue = 2


_TmnxNtpBroadcastAuthenticate_Type.__name__ = "TruthValue"
_TmnxNtpBroadcastAuthenticate_Object = MibTableColumn
tmnxNtpBroadcastAuthenticate = _TmnxNtpBroadcastAuthenticate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 2, 1, 9),
    _TmnxNtpBroadcastAuthenticate_Type()
)
tmnxNtpBroadcastAuthenticate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpBroadcastAuthenticate.setStatus("current")
_TmnxNtpBroadcastAssocId_Type = NTPAssocIdentifier
_TmnxNtpBroadcastAssocId_Object = MibTableColumn
tmnxNtpBroadcastAssocId = _TmnxNtpBroadcastAssocId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 2, 1, 10),
    _TmnxNtpBroadcastAssocId_Type()
)
tmnxNtpBroadcastAssocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpBroadcastAssocId.setStatus("current")
_TmnxNtpMulticastTable_Object = MibTable
tmnxNtpMulticastTable = _TmnxNtpMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxNtpMulticastTable.setStatus("current")
_TmnxNtpMulticastEntry_Object = MibTableRow
tmnxNtpMulticastEntry = _TmnxNtpMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 3, 1)
)
tmnxNtpMulticastEntry.setIndexNames(
    (0, "TIMETRA-NTP-MIB", "tmnxNtpMulticastDirection"),
    (0, "TIMETRA-NTP-MIB", "tmnxNtpMulticastIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxNtpMulticastEntry.setStatus("current")
_TmnxNtpMulticastDirection_Type = TmnxNtpDirection
_TmnxNtpMulticastDirection_Object = MibTableColumn
tmnxNtpMulticastDirection = _TmnxNtpMulticastDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 3, 1, 1),
    _TmnxNtpMulticastDirection_Type()
)
tmnxNtpMulticastDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNtpMulticastDirection.setStatus("current")
_TmnxNtpMulticastIfIndex_Type = InterfaceIndex
_TmnxNtpMulticastIfIndex_Object = MibTableColumn
tmnxNtpMulticastIfIndex = _TmnxNtpMulticastIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 3, 1, 2),
    _TmnxNtpMulticastIfIndex_Type()
)
tmnxNtpMulticastIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNtpMulticastIfIndex.setStatus("current")
_TmnxNtpMulticastAddressType_Type = InetAddressType
_TmnxNtpMulticastAddressType_Object = MibTableColumn
tmnxNtpMulticastAddressType = _TmnxNtpMulticastAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 3, 1, 3),
    _TmnxNtpMulticastAddressType_Type()
)
tmnxNtpMulticastAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpMulticastAddressType.setStatus("current")


class _TmnxNtpMulticastAddress_Type(InetAddress):
    """Custom type tmnxNtpMulticastAddress based on InetAddress"""
    defaultHexValue = "E0000101"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNtpMulticastAddress_Type.__name__ = "InetAddress"
_TmnxNtpMulticastAddress_Object = MibTableColumn
tmnxNtpMulticastAddress = _TmnxNtpMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 3, 1, 4),
    _TmnxNtpMulticastAddress_Type()
)
tmnxNtpMulticastAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpMulticastAddress.setStatus("current")
_TmnxNtpMulticastEntryStatus_Type = RowStatus
_TmnxNtpMulticastEntryStatus_Object = MibTableColumn
tmnxNtpMulticastEntryStatus = _TmnxNtpMulticastEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 3, 1, 5),
    _TmnxNtpMulticastEntryStatus_Type()
)
tmnxNtpMulticastEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpMulticastEntryStatus.setStatus("current")
_TmnxNtpMulticastLastChanged_Type = TimeStamp
_TmnxNtpMulticastLastChanged_Object = MibTableColumn
tmnxNtpMulticastLastChanged = _TmnxNtpMulticastLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 3, 1, 6),
    _TmnxNtpMulticastLastChanged_Type()
)
tmnxNtpMulticastLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpMulticastLastChanged.setStatus("current")


class _TmnxNtpMulticastAuthKeyId_Type(Unsigned32):
    """Custom type tmnxNtpMulticastAuthKeyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_TmnxNtpMulticastAuthKeyId_Type.__name__ = "Unsigned32"
_TmnxNtpMulticastAuthKeyId_Object = MibTableColumn
tmnxNtpMulticastAuthKeyId = _TmnxNtpMulticastAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 3, 1, 7),
    _TmnxNtpMulticastAuthKeyId_Type()
)
tmnxNtpMulticastAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpMulticastAuthKeyId.setStatus("current")


class _TmnxNtpMulticastVersion_Type(NTPVersion):
    """Custom type tmnxNtpMulticastVersion based on NTPVersion"""
    defaultValue = 4


_TmnxNtpMulticastVersion_Type.__name__ = "NTPVersion"
_TmnxNtpMulticastVersion_Object = MibTableColumn
tmnxNtpMulticastVersion = _TmnxNtpMulticastVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 3, 1, 8),
    _TmnxNtpMulticastVersion_Type()
)
tmnxNtpMulticastVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpMulticastVersion.setStatus("current")


class _TmnxNtpMulticastTtl_Type(Unsigned32):
    """Custom type tmnxNtpMulticastTtl based on Unsigned32"""
    defaultValue = 127

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxNtpMulticastTtl_Type.__name__ = "Unsigned32"
_TmnxNtpMulticastTtl_Object = MibTableColumn
tmnxNtpMulticastTtl = _TmnxNtpMulticastTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 3, 1, 9),
    _TmnxNtpMulticastTtl_Type()
)
tmnxNtpMulticastTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpMulticastTtl.setStatus("current")
_TmnxNtpMulticastAuthErrs_Type = Counter32
_TmnxNtpMulticastAuthErrs_Object = MibTableColumn
tmnxNtpMulticastAuthErrs = _TmnxNtpMulticastAuthErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 3, 1, 10),
    _TmnxNtpMulticastAuthErrs_Type()
)
tmnxNtpMulticastAuthErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpMulticastAuthErrs.setStatus("current")


class _TmnxNtpMulticastAuthenticate_Type(TruthValue):
    """Custom type tmnxNtpMulticastAuthenticate based on TruthValue"""
    defaultValue = 2


_TmnxNtpMulticastAuthenticate_Type.__name__ = "TruthValue"
_TmnxNtpMulticastAuthenticate_Object = MibTableColumn
tmnxNtpMulticastAuthenticate = _TmnxNtpMulticastAuthenticate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 3, 1, 11),
    _TmnxNtpMulticastAuthenticate_Type()
)
tmnxNtpMulticastAuthenticate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpMulticastAuthenticate.setStatus("current")
_TmnxNtpMulticastAssocId_Type = NTPAssocIdentifier
_TmnxNtpMulticastAssocId_Object = MibTableColumn
tmnxNtpMulticastAssocId = _TmnxNtpMulticastAssocId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 1, 3, 1, 12),
    _TmnxNtpMulticastAssocId_Type()
)
tmnxNtpMulticastAssocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpMulticastAssocId.setStatus("current")
_TmnxNtpServers_ObjectIdentity = ObjectIdentity
tmnxNtpServers = _TmnxNtpServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 2)
)
_TmnxNtpServersTable_Object = MibTable
tmnxNtpServersTable = _TmnxNtpServersTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxNtpServersTable.setStatus("current")
_TmnxNtpServersEntry_Object = MibTableRow
tmnxNtpServersEntry = _TmnxNtpServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 2, 1, 1)
)
tmnxNtpServersEntry.setIndexNames(
    (0, "TIMETRA-NTP-MIB", "tmnxNtpServersAddrType"),
    (0, "TIMETRA-NTP-MIB", "tmnxNtpServersAddress"),
)
if mibBuilder.loadTexts:
    tmnxNtpServersEntry.setStatus("current")
_TmnxNtpServersAddrType_Type = InetAddressType
_TmnxNtpServersAddrType_Object = MibTableColumn
tmnxNtpServersAddrType = _TmnxNtpServersAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 2, 1, 1, 1),
    _TmnxNtpServersAddrType_Type()
)
tmnxNtpServersAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNtpServersAddrType.setStatus("current")


class _TmnxNtpServersAddress_Type(InetAddress):
    """Custom type tmnxNtpServersAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNtpServersAddress_Type.__name__ = "InetAddress"
_TmnxNtpServersAddress_Object = MibTableColumn
tmnxNtpServersAddress = _TmnxNtpServersAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 2, 1, 1, 2),
    _TmnxNtpServersAddress_Type()
)
tmnxNtpServersAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNtpServersAddress.setStatus("current")
_TmnxNtpServersEntryStatus_Type = RowStatus
_TmnxNtpServersEntryStatus_Object = MibTableColumn
tmnxNtpServersEntryStatus = _TmnxNtpServersEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 2, 1, 1, 3),
    _TmnxNtpServersEntryStatus_Type()
)
tmnxNtpServersEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpServersEntryStatus.setStatus("current")
_TmnxNtpServersLastChanged_Type = TimeStamp
_TmnxNtpServersLastChanged_Object = MibTableColumn
tmnxNtpServersLastChanged = _TmnxNtpServersLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 2, 1, 1, 4),
    _TmnxNtpServersLastChanged_Type()
)
tmnxNtpServersLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpServersLastChanged.setStatus("current")


class _TmnxNtpServersAuthKeyId_Type(Unsigned32):
    """Custom type tmnxNtpServersAuthKeyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_TmnxNtpServersAuthKeyId_Type.__name__ = "Unsigned32"
_TmnxNtpServersAuthKeyId_Object = MibTableColumn
tmnxNtpServersAuthKeyId = _TmnxNtpServersAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 2, 1, 1, 5),
    _TmnxNtpServersAuthKeyId_Type()
)
tmnxNtpServersAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpServersAuthKeyId.setStatus("current")


class _TmnxNtpServersVersion_Type(NTPVersion):
    """Custom type tmnxNtpServersVersion based on NTPVersion"""
    defaultValue = 4


_TmnxNtpServersVersion_Type.__name__ = "NTPVersion"
_TmnxNtpServersVersion_Object = MibTableColumn
tmnxNtpServersVersion = _TmnxNtpServersVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 2, 1, 1, 6),
    _TmnxNtpServersVersion_Type()
)
tmnxNtpServersVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpServersVersion.setStatus("current")


class _TmnxNtpServersPrefer_Type(TruthValue):
    """Custom type tmnxNtpServersPrefer based on TruthValue"""
    defaultValue = 2


_TmnxNtpServersPrefer_Type.__name__ = "TruthValue"
_TmnxNtpServersPrefer_Object = MibTableColumn
tmnxNtpServersPrefer = _TmnxNtpServersPrefer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 2, 1, 1, 7),
    _TmnxNtpServersPrefer_Type()
)
tmnxNtpServersPrefer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpServersPrefer.setStatus("current")
_TmnxNtpServersAssocId_Type = NTPAssocIdentifier
_TmnxNtpServersAssocId_Object = MibTableColumn
tmnxNtpServersAssocId = _TmnxNtpServersAssocId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 2, 1, 1, 8),
    _TmnxNtpServersAssocId_Type()
)
tmnxNtpServersAssocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpServersAssocId.setStatus("current")
_TmnxNtpServersAuthErrs_Type = Counter32
_TmnxNtpServersAuthErrs_Object = MibTableColumn
tmnxNtpServersAuthErrs = _TmnxNtpServersAuthErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 2, 1, 1, 9),
    _TmnxNtpServersAuthErrs_Type()
)
tmnxNtpServersAuthErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpServersAuthErrs.setStatus("current")
_TmnxNtpPeers_ObjectIdentity = ObjectIdentity
tmnxNtpPeers = _TmnxNtpPeers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3)
)
_TmnxNtpPeersTable_Object = MibTable
tmnxNtpPeersTable = _TmnxNtpPeersTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxNtpPeersTable.setStatus("current")
_TmnxNtpPeersEntry_Object = MibTableRow
tmnxNtpPeersEntry = _TmnxNtpPeersEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 1, 1)
)
tmnxNtpPeersEntry.setIndexNames(
    (0, "TIMETRA-NTP-MIB", "tmnxNtpPeersAddrType"),
    (0, "TIMETRA-NTP-MIB", "tmnxNtpPeersAddress"),
)
if mibBuilder.loadTexts:
    tmnxNtpPeersEntry.setStatus("current")
_TmnxNtpPeersAddrType_Type = InetAddressType
_TmnxNtpPeersAddrType_Object = MibTableColumn
tmnxNtpPeersAddrType = _TmnxNtpPeersAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 1, 1, 1),
    _TmnxNtpPeersAddrType_Type()
)
tmnxNtpPeersAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNtpPeersAddrType.setStatus("current")


class _TmnxNtpPeersAddress_Type(InetAddress):
    """Custom type tmnxNtpPeersAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNtpPeersAddress_Type.__name__ = "InetAddress"
_TmnxNtpPeersAddress_Object = MibTableColumn
tmnxNtpPeersAddress = _TmnxNtpPeersAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 1, 1, 2),
    _TmnxNtpPeersAddress_Type()
)
tmnxNtpPeersAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNtpPeersAddress.setStatus("current")
_TmnxNtpPeersEntryStatus_Type = RowStatus
_TmnxNtpPeersEntryStatus_Object = MibTableColumn
tmnxNtpPeersEntryStatus = _TmnxNtpPeersEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 1, 1, 3),
    _TmnxNtpPeersEntryStatus_Type()
)
tmnxNtpPeersEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpPeersEntryStatus.setStatus("current")
_TmnxNtpPeersLastChanged_Type = TimeStamp
_TmnxNtpPeersLastChanged_Object = MibTableColumn
tmnxNtpPeersLastChanged = _TmnxNtpPeersLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 1, 1, 4),
    _TmnxNtpPeersLastChanged_Type()
)
tmnxNtpPeersLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersLastChanged.setStatus("current")


class _TmnxNtpPeersAuthKeyId_Type(Unsigned32):
    """Custom type tmnxNtpPeersAuthKeyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_TmnxNtpPeersAuthKeyId_Type.__name__ = "Unsigned32"
_TmnxNtpPeersAuthKeyId_Object = MibTableColumn
tmnxNtpPeersAuthKeyId = _TmnxNtpPeersAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 1, 1, 5),
    _TmnxNtpPeersAuthKeyId_Type()
)
tmnxNtpPeersAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpPeersAuthKeyId.setStatus("current")


class _TmnxNtpPeersVersion_Type(NTPVersion):
    """Custom type tmnxNtpPeersVersion based on NTPVersion"""
    defaultValue = 4


_TmnxNtpPeersVersion_Type.__name__ = "NTPVersion"
_TmnxNtpPeersVersion_Object = MibTableColumn
tmnxNtpPeersVersion = _TmnxNtpPeersVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 1, 1, 6),
    _TmnxNtpPeersVersion_Type()
)
tmnxNtpPeersVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpPeersVersion.setStatus("current")


class _TmnxNtpPeersPrefer_Type(TruthValue):
    """Custom type tmnxNtpPeersPrefer based on TruthValue"""
    defaultValue = 2


_TmnxNtpPeersPrefer_Type.__name__ = "TruthValue"
_TmnxNtpPeersPrefer_Object = MibTableColumn
tmnxNtpPeersPrefer = _TmnxNtpPeersPrefer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 1, 1, 7),
    _TmnxNtpPeersPrefer_Type()
)
tmnxNtpPeersPrefer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpPeersPrefer.setStatus("current")
_TmnxNtpPeersAssocId_Type = NTPAssocIdentifier
_TmnxNtpPeersAssocId_Object = MibTableColumn
tmnxNtpPeersAssocId = _TmnxNtpPeersAssocId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 1, 1, 8),
    _TmnxNtpPeersAssocId_Type()
)
tmnxNtpPeersAssocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersAssocId.setStatus("current")
_TmnxNtpPeersAuthErrs_Type = Counter32
_TmnxNtpPeersAuthErrs_Object = MibTableColumn
tmnxNtpPeersAuthErrs = _TmnxNtpPeersAuthErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 1, 1, 9),
    _TmnxNtpPeersAuthErrs_Type()
)
tmnxNtpPeersAuthErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersAuthErrs.setStatus("current")
_TmnxNtpPeersVarTable_Object = MibTable
tmnxNtpPeersVarTable = _TmnxNtpPeersVarTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxNtpPeersVarTable.setStatus("current")
_TmnxNtpPeersVarEntry_Object = MibTableRow
tmnxNtpPeersVarEntry = _TmnxNtpPeersVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2, 1)
)
tmnxNtpPeersVarEntry.setIndexNames(
    (0, "TIMETRA-NTP-MIB", "tmnxNtpPeersVarAssocId"),
)
if mibBuilder.loadTexts:
    tmnxNtpPeersVarEntry.setStatus("current")
_TmnxNtpPeersVarAssocId_Type = NTPAssocIdentifier
_TmnxNtpPeersVarAssocId_Object = MibTableColumn
tmnxNtpPeersVarAssocId = _TmnxNtpPeersVarAssocId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2, 1, 1),
    _TmnxNtpPeersVarAssocId_Type()
)
tmnxNtpPeersVarAssocId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNtpPeersVarAssocId.setStatus("current")
_TmnxNtpPeersConfigured_Type = TruthValue
_TmnxNtpPeersConfigured_Object = MibTableColumn
tmnxNtpPeersConfigured = _TmnxNtpPeersConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2, 1, 2),
    _TmnxNtpPeersConfigured_Type()
)
tmnxNtpPeersConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersConfigured.setStatus("current")
_TmnxNtpPeersPeerAddrType_Type = InetAddressType
_TmnxNtpPeersPeerAddrType_Object = MibTableColumn
tmnxNtpPeersPeerAddrType = _TmnxNtpPeersPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2, 1, 3),
    _TmnxNtpPeersPeerAddrType_Type()
)
tmnxNtpPeersPeerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersPeerAddrType.setStatus("current")


class _TmnxNtpPeersPeerAddress_Type(InetAddress):
    """Custom type tmnxNtpPeersPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNtpPeersPeerAddress_Type.__name__ = "InetAddress"
_TmnxNtpPeersPeerAddress_Object = MibTableColumn
tmnxNtpPeersPeerAddress = _TmnxNtpPeersPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2, 1, 4),
    _TmnxNtpPeersPeerAddress_Type()
)
tmnxNtpPeersPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersPeerAddress.setStatus("current")
_TmnxNtpPeersPeerPort_Type = Unsigned32
_TmnxNtpPeersPeerPort_Object = MibTableColumn
tmnxNtpPeersPeerPort = _TmnxNtpPeersPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2, 1, 5),
    _TmnxNtpPeersPeerPort_Type()
)
tmnxNtpPeersPeerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersPeerPort.setStatus("current")
_TmnxNtpPeersHostAddrType_Type = InetAddressType
_TmnxNtpPeersHostAddrType_Object = MibTableColumn
tmnxNtpPeersHostAddrType = _TmnxNtpPeersHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2, 1, 6),
    _TmnxNtpPeersHostAddrType_Type()
)
tmnxNtpPeersHostAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersHostAddrType.setStatus("current")


class _TmnxNtpPeersHostAddress_Type(InetAddress):
    """Custom type tmnxNtpPeersHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNtpPeersHostAddress_Type.__name__ = "InetAddress"
_TmnxNtpPeersHostAddress_Object = MibTableColumn
tmnxNtpPeersHostAddress = _TmnxNtpPeersHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2, 1, 7),
    _TmnxNtpPeersHostAddress_Type()
)
tmnxNtpPeersHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersHostAddress.setStatus("current")
_TmnxNtpPeersHostPort_Type = Unsigned32
_TmnxNtpPeersHostPort_Object = MibTableColumn
tmnxNtpPeersHostPort = _TmnxNtpPeersHostPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2, 1, 8),
    _TmnxNtpPeersHostPort_Type()
)
tmnxNtpPeersHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersHostPort.setStatus("current")


class _TmnxNtpPeersMode_Type(Integer32):
    """Custom type tmnxNtpPeersMode based on Integer32"""
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
        *(("unspecified", 0),
          ("symmetricActive", 1),
          ("symmetricPassive", 2),
          ("client", 3),
          ("server", 4),
          ("broadcast", 5),
          ("reservedControl", 6),
          ("reservedPrivate", 7),
          ("broadcastclient", 8))
    )


_TmnxNtpPeersMode_Type.__name__ = "Integer32"
_TmnxNtpPeersMode_Object = MibTableColumn
tmnxNtpPeersMode = _TmnxNtpPeersMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2, 1, 9),
    _TmnxNtpPeersMode_Type()
)
tmnxNtpPeersMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersMode.setStatus("current")
_TmnxNtpPeersStratum_Type = NTPStratum
_TmnxNtpPeersStratum_Object = MibTableColumn
tmnxNtpPeersStratum = _TmnxNtpPeersStratum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2, 1, 10),
    _TmnxNtpPeersStratum_Type()
)
tmnxNtpPeersStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersStratum.setStatus("current")
_TmnxNtpPeersPeerPoll_Type = NTPPollInterval
_TmnxNtpPeersPeerPoll_Object = MibTableColumn
tmnxNtpPeersPeerPoll = _TmnxNtpPeersPeerPoll_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2, 1, 11),
    _TmnxNtpPeersPeerPoll_Type()
)
tmnxNtpPeersPeerPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersPeerPoll.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNtpPeersPeerPoll.setUnits("seconds as a power of two")
_TmnxNtpPeersHostPoll_Type = NTPPollInterval
_TmnxNtpPeersHostPoll_Object = MibTableColumn
tmnxNtpPeersHostPoll = _TmnxNtpPeersHostPoll_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2, 1, 12),
    _TmnxNtpPeersHostPoll_Type()
)
tmnxNtpPeersHostPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersHostPoll.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNtpPeersHostPoll.setUnits("seconds as a power of two")
_TmnxNtpPeersRefId_Type = NTPRefId
_TmnxNtpPeersRefId_Object = MibTableColumn
tmnxNtpPeersRefId = _TmnxNtpPeersRefId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2, 1, 13),
    _TmnxNtpPeersRefId_Type()
)
tmnxNtpPeersRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersRefId.setStatus("current")
_TmnxNtpPeersReceiveTime_Type = NTPTimeStamp
_TmnxNtpPeersReceiveTime_Object = MibTableColumn
tmnxNtpPeersReceiveTime = _TmnxNtpPeersReceiveTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2, 1, 14),
    _TmnxNtpPeersReceiveTime_Type()
)
tmnxNtpPeersReceiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersReceiveTime.setStatus("current")
_TmnxNtpPeersReach_Type = Unsigned32
_TmnxNtpPeersReach_Object = MibTableColumn
tmnxNtpPeersReach = _TmnxNtpPeersReach_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2, 1, 15),
    _TmnxNtpPeersReach_Type()
)
tmnxNtpPeersReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersReach.setStatus("current")
_TmnxNtpPeersOffset_Type = NTPSignedTimeValue
_TmnxNtpPeersOffset_Object = MibTableColumn
tmnxNtpPeersOffset = _TmnxNtpPeersOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2, 1, 16),
    _TmnxNtpPeersOffset_Type()
)
tmnxNtpPeersOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersOffset.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNtpPeersOffset.setUnits("seconds")
_TmnxNtpPeersPrefPeer_Type = TruthValue
_TmnxNtpPeersPrefPeer_Object = MibTableColumn
tmnxNtpPeersPrefPeer = _TmnxNtpPeersPrefPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2, 1, 17),
    _TmnxNtpPeersPrefPeer_Type()
)
tmnxNtpPeersPrefPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersPrefPeer.setStatus("current")


class _TmnxNtpPeersStatus_Type(Integer32):
    """Custom type tmnxNtpPeersStatus based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("reject", 0),
          ("inaccurate", 1),
          ("excess", 2),
          ("outlyer", 3),
          ("candidate", 4),
          ("selected", 5),
          ("syspeer", 6),
          ("ppspeer", 7))
    )


_TmnxNtpPeersStatus_Type.__name__ = "Integer32"
_TmnxNtpPeersStatus_Object = MibTableColumn
tmnxNtpPeersStatus = _TmnxNtpPeersStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2, 1, 18),
    _TmnxNtpPeersStatus_Type()
)
tmnxNtpPeersStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersStatus.setStatus("current")


class _TmnxNtpPeersStatusFlags_Type(Bits):
    """Custom type tmnxNtpPeersStatusFlags based on Bits"""
    namedValues = NamedValues(
        *(("config", 0),
          ("authenable", 1),
          ("authentic", 2),
          ("reachable", 3),
          ("broadcastclient", 4),
          ("multicastclient", 5),
          ("broadcast", 6),
          ("multicast", 7))
    )

_TmnxNtpPeersStatusFlags_Type.__name__ = "Bits"
_TmnxNtpPeersStatusFlags_Object = MibTableColumn
tmnxNtpPeersStatusFlags = _TmnxNtpPeersStatusFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 3, 2, 1, 19),
    _TmnxNtpPeersStatusFlags_Type()
)
tmnxNtpPeersStatusFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpPeersStatusFlags.setStatus("current")
_TmnxNtpFilter_ObjectIdentity = ObjectIdentity
tmnxNtpFilter = _TmnxNtpFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 4)
)
_TmnxNtpAuthKeys_ObjectIdentity = ObjectIdentity
tmnxNtpAuthKeys = _TmnxNtpAuthKeys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 5)
)
_TmnxNtpAuthKeyTable_Object = MibTable
tmnxNtpAuthKeyTable = _TmnxNtpAuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxNtpAuthKeyTable.setStatus("current")
_TmnxNtpAuthKeyEntry_Object = MibTableRow
tmnxNtpAuthKeyEntry = _TmnxNtpAuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 5, 1, 1)
)
tmnxNtpAuthKeyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NTP-MIB", "tmnxNtpAuthKeyId"),
)
if mibBuilder.loadTexts:
    tmnxNtpAuthKeyEntry.setStatus("current")


class _TmnxNtpAuthKeyId_Type(Unsigned32):
    """Custom type tmnxNtpAuthKeyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxNtpAuthKeyId_Type.__name__ = "Unsigned32"
_TmnxNtpAuthKeyId_Object = MibTableColumn
tmnxNtpAuthKeyId = _TmnxNtpAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 5, 1, 1, 1),
    _TmnxNtpAuthKeyId_Type()
)
tmnxNtpAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNtpAuthKeyId.setStatus("current")
_TmnxNtpAuthKeyEntryStatus_Type = RowStatus
_TmnxNtpAuthKeyEntryStatus_Object = MibTableColumn
tmnxNtpAuthKeyEntryStatus = _TmnxNtpAuthKeyEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 5, 1, 1, 2),
    _TmnxNtpAuthKeyEntryStatus_Type()
)
tmnxNtpAuthKeyEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpAuthKeyEntryStatus.setStatus("current")
_TmnxNtpAuthKeyLastChanged_Type = TimeStamp
_TmnxNtpAuthKeyLastChanged_Object = MibTableColumn
tmnxNtpAuthKeyLastChanged = _TmnxNtpAuthKeyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 5, 1, 1, 3),
    _TmnxNtpAuthKeyLastChanged_Type()
)
tmnxNtpAuthKeyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpAuthKeyLastChanged.setStatus("current")


class _TmnxNtpAuthKey_Type(OctetString):
    """Custom type tmnxNtpAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxNtpAuthKey_Type.__name__ = "OctetString"
_TmnxNtpAuthKey_Object = MibTableColumn
tmnxNtpAuthKey = _TmnxNtpAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 5, 1, 1, 4),
    _TmnxNtpAuthKey_Type()
)
tmnxNtpAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpAuthKey.setStatus("current")


class _TmnxNtpAuthKeyType_Type(Integer32):
    """Custom type tmnxNtpAuthKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("des", 1),
          ("messageDigest", 2))
    )


_TmnxNtpAuthKeyType_Type.__name__ = "Integer32"
_TmnxNtpAuthKeyType_Object = MibTableColumn
tmnxNtpAuthKeyType = _TmnxNtpAuthKeyType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 5, 1, 1, 5),
    _TmnxNtpAuthKeyType_Type()
)
tmnxNtpAuthKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpAuthKeyType.setStatus("current")
_TmnxNtpNotifyObjs_ObjectIdentity = ObjectIdentity
tmnxNtpNotifyObjs = _TmnxNtpNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 6)
)
_TmnxNtpUTCOffset_Type = NTPSignedTimeValue
_TmnxNtpUTCOffset_Object = MibScalar
tmnxNtpUTCOffset = _TmnxNtpUTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 6, 1),
    _TmnxNtpUTCOffset_Type()
)
tmnxNtpUTCOffset.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNtpUTCOffset.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNtpUTCOffset.setUnits("seconds")
_TmnxNtpUTCOffsetThreshold_Type = NTPSignedTimeValue
_TmnxNtpUTCOffsetThreshold_Object = MibScalar
tmnxNtpUTCOffsetThreshold = _TmnxNtpUTCOffsetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 6, 2),
    _TmnxNtpUTCOffsetThreshold_Type()
)
tmnxNtpUTCOffsetThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNtpUTCOffsetThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNtpUTCOffsetThreshold.setUnits("seconds")


class _TmnxNtpAuthKeyFailType_Type(Integer32):
    """Custom type tmnxNtpAuthKeyFailType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalidAuthKeyType", 1),
          ("invalidAuthKey", 2),
          ("invalidAuthKeyId", 3))
    )


_TmnxNtpAuthKeyFailType_Type.__name__ = "Integer32"
_TmnxNtpAuthKeyFailType_Object = MibScalar
tmnxNtpAuthKeyFailType = _TmnxNtpAuthKeyFailType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 6, 3),
    _TmnxNtpAuthKeyFailType_Type()
)
tmnxNtpAuthKeyFailType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNtpAuthKeyFailType.setStatus("current")
_TmnxNtpConfigs_ObjectIdentity = ObjectIdentity
tmnxNtpConfigs = _TmnxNtpConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 7)
)
_TmnxNtpConfigTable_Object = MibTable
tmnxNtpConfigTable = _TmnxNtpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 7, 1)
)
if mibBuilder.loadTexts:
    tmnxNtpConfigTable.setStatus("current")
_TmnxNtpConfigEntry_Object = MibTableRow
tmnxNtpConfigEntry = _TmnxNtpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 7, 1, 1)
)
tmnxNtpConfigEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    tmnxNtpConfigEntry.setStatus("current")
_TmnxNtpConfigRowStatus_Type = RowStatus
_TmnxNtpConfigRowStatus_Object = MibTableColumn
tmnxNtpConfigRowStatus = _TmnxNtpConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 7, 1, 1, 1),
    _TmnxNtpConfigRowStatus_Type()
)
tmnxNtpConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpConfigRowStatus.setStatus("current")


class _TmnxNtpConfigAdminState_Type(TmnxAdminState):
    """Custom type tmnxNtpConfigAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNtpConfigAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNtpConfigAdminState_Object = MibTableColumn
tmnxNtpConfigAdminState = _TmnxNtpConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 7, 1, 1, 2),
    _TmnxNtpConfigAdminState_Type()
)
tmnxNtpConfigAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpConfigAdminState.setStatus("current")


class _TmnxNtpConfigServer_Type(TruthValue):
    """Custom type tmnxNtpConfigServer based on TruthValue"""
    defaultValue = 1


_TmnxNtpConfigServer_Type.__name__ = "TruthValue"
_TmnxNtpConfigServer_Object = MibTableColumn
tmnxNtpConfigServer = _TmnxNtpConfigServer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 7, 1, 1, 3),
    _TmnxNtpConfigServer_Type()
)
tmnxNtpConfigServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpConfigServer.setStatus("current")


class _TmnxNtpConfigServerAuthenticate_Type(TruthValue):
    """Custom type tmnxNtpConfigServerAuthenticate based on TruthValue"""
    defaultValue = 2


_TmnxNtpConfigServerAuthenticate_Type.__name__ = "TruthValue"
_TmnxNtpConfigServerAuthenticate_Object = MibTableColumn
tmnxNtpConfigServerAuthenticate = _TmnxNtpConfigServerAuthenticate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 7, 1, 1, 4),
    _TmnxNtpConfigServerAuthenticate_Type()
)
tmnxNtpConfigServerAuthenticate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpConfigServerAuthenticate.setStatus("current")


class _TmnxNtpConfigAuthCheck_Type(TruthValue):
    """Custom type tmnxNtpConfigAuthCheck based on TruthValue"""
    defaultValue = 1


_TmnxNtpConfigAuthCheck_Type.__name__ = "TruthValue"
_TmnxNtpConfigAuthCheck_Object = MibTableColumn
tmnxNtpConfigAuthCheck = _TmnxNtpConfigAuthCheck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 7, 1, 1, 5),
    _TmnxNtpConfigAuthCheck_Type()
)
tmnxNtpConfigAuthCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNtpConfigAuthCheck.setStatus("current")
_TmnxNtpClientInfoTable_Object = MibTable
tmnxNtpClientInfoTable = _TmnxNtpClientInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 7, 2)
)
if mibBuilder.loadTexts:
    tmnxNtpClientInfoTable.setStatus("current")
_TmnxNtpClientInfoEntry_Object = MibTableRow
tmnxNtpClientInfoEntry = _TmnxNtpClientInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 7, 2, 1)
)
tmnxNtpClientInfoEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NTP-MIB", "tmnxNtpClientAddressType"),
    (0, "TIMETRA-NTP-MIB", "tmnxNtpClientAddress"),
)
if mibBuilder.loadTexts:
    tmnxNtpClientInfoEntry.setStatus("current")
_TmnxNtpClientAddressType_Type = InetAddressType
_TmnxNtpClientAddressType_Object = MibTableColumn
tmnxNtpClientAddressType = _TmnxNtpClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 7, 2, 1, 1),
    _TmnxNtpClientAddressType_Type()
)
tmnxNtpClientAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNtpClientAddressType.setStatus("current")


class _TmnxNtpClientAddress_Type(InetAddress):
    """Custom type tmnxNtpClientAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNtpClientAddress_Type.__name__ = "InetAddress"
_TmnxNtpClientAddress_Object = MibTableColumn
tmnxNtpClientAddress = _TmnxNtpClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 7, 2, 1, 2),
    _TmnxNtpClientAddress_Type()
)
tmnxNtpClientAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNtpClientAddress.setStatus("current")
_TmnxNtpClientInfoLastRequestTime_Type = TimeStamp
_TmnxNtpClientInfoLastRequestTime_Object = MibTableColumn
tmnxNtpClientInfoLastRequestTime = _TmnxNtpClientInfoLastRequestTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 38, 7, 2, 1, 3),
    _TmnxNtpClientInfoLastRequestTime_Type()
)
tmnxNtpClientInfoLastRequestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNtpClientInfoLastRequestTime.setStatus("current")
_TmnxNtpNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxNtpNotifyPrefix = _TmnxNtpNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 38)
)
_TmnxNtpNotifications_ObjectIdentity = ObjectIdentity
tmnxNtpNotifications = _TmnxNtpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 38, 0)
)

# Managed Objects groups

tmnxNtpGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 2, 1)
)
tmnxNtpGlobalGroup.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpSysLeap"),
        ("TIMETRA-NTP-MIB", "tmnxNtpSysStratum"),
        ("TIMETRA-NTP-MIB", "tmnxNtpSysRefId"),
        ("TIMETRA-NTP-MIB", "tmnxNtpSysRefTime"),
        ("TIMETRA-NTP-MIB", "tmnxNtpSysPoll"),
        ("TIMETRA-NTP-MIB", "tmnxNtpSysPeer"),
        ("TIMETRA-NTP-MIB", "tmnxNtpSysClock"),
        ("TIMETRA-NTP-MIB", "tmnxNtp"),
        ("TIMETRA-NTP-MIB", "tmnxNtpAdminState"),
        ("TIMETRA-NTP-MIB", "tmnxNtpOperState"),
        ("TIMETRA-NTP-MIB", "tmnxNtpServer"),
        ("TIMETRA-NTP-MIB", "tmnxNtpServerKeyId"),
        ("TIMETRA-NTP-MIB", "tmnxNtpAuthCheck"))
)
if mibBuilder.loadTexts:
    tmnxNtpGlobalGroup.setStatus("obsolete")

tmnxNtpBroadcastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 2, 2)
)
tmnxNtpBroadcastGroup.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpBroadcastEntryStatus"),
        ("TIMETRA-NTP-MIB", "tmnxNtpBroadcastLastChanged"),
        ("TIMETRA-NTP-MIB", "tmnxNtpBroadcastAuthKeyId"),
        ("TIMETRA-NTP-MIB", "tmnxNtpBroadcastVersion"),
        ("TIMETRA-NTP-MIB", "tmnxNtpBroadcastTtl"),
        ("TIMETRA-NTP-MIB", "tmnxNtpBroadcastAuthErrs"),
        ("TIMETRA-NTP-MIB", "tmnxNtpBroadcastAuthenticate"),
        ("TIMETRA-NTP-MIB", "tmnxNtpBroadcastAssocId"))
)
if mibBuilder.loadTexts:
    tmnxNtpBroadcastGroup.setStatus("current")

tmnxNtpMulticastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 2, 3)
)
tmnxNtpMulticastGroup.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpMulticastAddressType"),
        ("TIMETRA-NTP-MIB", "tmnxNtpMulticastAddress"),
        ("TIMETRA-NTP-MIB", "tmnxNtpMulticastEntryStatus"),
        ("TIMETRA-NTP-MIB", "tmnxNtpMulticastLastChanged"),
        ("TIMETRA-NTP-MIB", "tmnxNtpMulticastAuthKeyId"),
        ("TIMETRA-NTP-MIB", "tmnxNtpMulticastVersion"),
        ("TIMETRA-NTP-MIB", "tmnxNtpMulticastTtl"),
        ("TIMETRA-NTP-MIB", "tmnxNtpMulticastAuthErrs"),
        ("TIMETRA-NTP-MIB", "tmnxNtpMulticastAuthenticate"),
        ("TIMETRA-NTP-MIB", "tmnxNtpMulticastAssocId"))
)
if mibBuilder.loadTexts:
    tmnxNtpMulticastGroup.setStatus("current")

tmnxNtpServersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 2, 4)
)
tmnxNtpServersGroup.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpServersEntryStatus"),
        ("TIMETRA-NTP-MIB", "tmnxNtpServersLastChanged"),
        ("TIMETRA-NTP-MIB", "tmnxNtpServersAuthKeyId"),
        ("TIMETRA-NTP-MIB", "tmnxNtpServersVersion"),
        ("TIMETRA-NTP-MIB", "tmnxNtpServersPrefer"),
        ("TIMETRA-NTP-MIB", "tmnxNtpServersAssocId"),
        ("TIMETRA-NTP-MIB", "tmnxNtpServersAuthErrs"))
)
if mibBuilder.loadTexts:
    tmnxNtpServersGroup.setStatus("current")

tmnxNtpPeersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 2, 5)
)
tmnxNtpPeersGroup.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpPeersEntryStatus"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersLastChanged"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersAuthKeyId"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersVersion"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersPrefer"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersAssocId"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersAuthErrs"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersConfigured"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersPeerAddrType"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersPeerAddress"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersPeerPort"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersHostAddrType"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersHostAddress"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersHostPort"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersMode"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersStratum"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersPeerPoll"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersHostPoll"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersRefId"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersReceiveTime"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersReach"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersOffset"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersPrefPeer"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersStatus"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersStatusFlags"))
)
if mibBuilder.loadTexts:
    tmnxNtpPeersGroup.setStatus("current")

tmnxNtpAuthKeyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 2, 6)
)
tmnxNtpAuthKeyGroup.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpAuthKeyEntryStatus"),
        ("TIMETRA-NTP-MIB", "tmnxNtpAuthKeyLastChanged"),
        ("TIMETRA-NTP-MIB", "tmnxNtpAuthKey"),
        ("TIMETRA-NTP-MIB", "tmnxNtpAuthKeyType"))
)
if mibBuilder.loadTexts:
    tmnxNtpAuthKeyGroup.setStatus("current")

tmnxNtpNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 2, 8)
)
tmnxNtpNotifyObjsGroup.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpUTCOffset"),
        ("TIMETRA-NTP-MIB", "tmnxNtpUTCOffsetThreshold"),
        ("TIMETRA-NTP-MIB", "tmnxNtpAuthKeyFailType"))
)
if mibBuilder.loadTexts:
    tmnxNtpNotifyObjsGroup.setStatus("current")

tmnxNtpObsoleteV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 2, 13)
)
tmnxNtpObsoleteV8v0Group.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtp"),
        ("TIMETRA-NTP-MIB", "tmnxNtpAdminState"),
        ("TIMETRA-NTP-MIB", "tmnxNtpServer"),
        ("TIMETRA-NTP-MIB", "tmnxNtpServerKeyId"),
        ("TIMETRA-NTP-MIB", "tmnxNtpAuthCheck"))
)
if mibBuilder.loadTexts:
    tmnxNtpObsoleteV8v0Group.setStatus("current")

tmnxNtpGlobalV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 2, 14)
)
tmnxNtpGlobalV8v0Group.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpSysLeap"),
        ("TIMETRA-NTP-MIB", "tmnxNtpSysStratum"),
        ("TIMETRA-NTP-MIB", "tmnxNtpSysRefId"),
        ("TIMETRA-NTP-MIB", "tmnxNtpSysRefTime"),
        ("TIMETRA-NTP-MIB", "tmnxNtpSysPoll"),
        ("TIMETRA-NTP-MIB", "tmnxNtpSysPeer"),
        ("TIMETRA-NTP-MIB", "tmnxNtpSysClock"),
        ("TIMETRA-NTP-MIB", "tmnxNtpOperState"))
)
if mibBuilder.loadTexts:
    tmnxNtpGlobalV8v0Group.setStatus("current")

tmnxNtpV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 2, 15)
)
tmnxNtpV8v0Group.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpConfigRowStatus"),
        ("TIMETRA-NTP-MIB", "tmnxNtpConfigAdminState"),
        ("TIMETRA-NTP-MIB", "tmnxNtpConfigServer"),
        ("TIMETRA-NTP-MIB", "tmnxNtpConfigServerAuthenticate"),
        ("TIMETRA-NTP-MIB", "tmnxNtpConfigAuthCheck"),
        ("TIMETRA-NTP-MIB", "tmnxNtpClientInfoLastRequestTime"))
)
if mibBuilder.loadTexts:
    tmnxNtpV8v0Group.setStatus("current")


# Notification objects

tmnxNtpAuthMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 38, 0, 1)
)
tmnxNtpAuthMismatch.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpPeersPeerAddrType"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersPeerAddress"),
        ("TIMETRA-NTP-MIB", "tmnxNtpAuthKeyFailType"))
)
if mibBuilder.loadTexts:
    tmnxNtpAuthMismatch.setStatus(
        "current"
    )

tmnxNtpNoServersAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 38, 0, 2)
)
if mibBuilder.loadTexts:
    tmnxNtpNoServersAvail.setStatus(
        "current"
    )

tmnxNtpServersAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 38, 0, 3)
)
if mibBuilder.loadTexts:
    tmnxNtpServersAvail.setStatus(
        "current"
    )

tmnxNtpMaxFreqDftExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 38, 0, 4)
)
if mibBuilder.loadTexts:
    tmnxNtpMaxFreqDftExceed.setStatus(
        "obsolete"
    )

tmnxNtpUtcOffsetExThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 38, 0, 5)
)
tmnxNtpUtcOffsetExThreshold.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpUTCOffset"),
        ("TIMETRA-NTP-MIB", "tmnxNtpUTCOffsetThreshold"))
)
if mibBuilder.loadTexts:
    tmnxNtpUtcOffsetExThreshold.setStatus(
        "obsolete"
    )

tmnxNtpUtcOffsetInThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 38, 0, 6)
)
tmnxNtpUtcOffsetInThreshold.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpUTCOffset"),
        ("TIMETRA-NTP-MIB", "tmnxNtpUTCOffsetThreshold"))
)
if mibBuilder.loadTexts:
    tmnxNtpUtcOffsetInThreshold.setStatus(
        "obsolete"
    )

tmnxNtpOperChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 38, 0, 7)
)
tmnxNtpOperChange.setObjects(
    ("TIMETRA-NTP-MIB", "tmnxNtpOperState")
)
if mibBuilder.loadTexts:
    tmnxNtpOperChange.setStatus(
        "current"
    )

tmnxNtpServerChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 38, 0, 8)
)
tmnxNtpServerChange.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpPeersPeerAddrType"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersPeerAddress"))
)
if mibBuilder.loadTexts:
    tmnxNtpServerChange.setStatus(
        "current"
    )


# Notifications groups

tmnxNtpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 2, 7)
)
tmnxNtpNotificationGroup.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpAuthMismatch"),
        ("TIMETRA-NTP-MIB", "tmnxNtpNoServersAvail"),
        ("TIMETRA-NTP-MIB", "tmnxNtpServersAvail"),
        ("TIMETRA-NTP-MIB", "tmnxNtpMaxFreqDftExceed"),
        ("TIMETRA-NTP-MIB", "tmnxNtpUtcOffsetExThreshold"),
        ("TIMETRA-NTP-MIB", "tmnxNtpUtcOffsetInThreshold"),
        ("TIMETRA-NTP-MIB", "tmnxNtpOperChange"))
)
if mibBuilder.loadTexts:
    tmnxNtpNotificationGroup.setStatus(
        "obsolete"
    )

tmnxNtpObsoleteNotificationV4v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 2, 9)
)
tmnxNtpObsoleteNotificationV4v0Group.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpUtcOffsetExThreshold"),
        ("TIMETRA-NTP-MIB", "tmnxNtpUtcOffsetInThreshold"))
)
if mibBuilder.loadTexts:
    tmnxNtpObsoleteNotificationV4v0Group.setStatus(
        "current"
    )

tmnxNtpNotificationV4v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 2, 10)
)
tmnxNtpNotificationV4v0Group.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpAuthMismatch"),
        ("TIMETRA-NTP-MIB", "tmnxNtpNoServersAvail"),
        ("TIMETRA-NTP-MIB", "tmnxNtpServersAvail"),
        ("TIMETRA-NTP-MIB", "tmnxNtpMaxFreqDftExceed"),
        ("TIMETRA-NTP-MIB", "tmnxNtpOperChange"))
)
if mibBuilder.loadTexts:
    tmnxNtpNotificationV4v0Group.setStatus(
        "obsolete"
    )

tmnxNtpNotificationV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 2, 11)
)
tmnxNtpNotificationV6v0Group.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpAuthMismatch"),
        ("TIMETRA-NTP-MIB", "tmnxNtpNoServersAvail"),
        ("TIMETRA-NTP-MIB", "tmnxNtpServersAvail"),
        ("TIMETRA-NTP-MIB", "tmnxNtpOperChange"),
        ("TIMETRA-NTP-MIB", "tmnxNtpServerChange"))
)
if mibBuilder.loadTexts:
    tmnxNtpNotificationV6v0Group.setStatus(
        "current"
    )

tmnxNtpObsoleteNotficatnV6v0Grp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 2, 12)
)
tmnxNtpObsoleteNotficatnV6v0Grp.setObjects(
    ("TIMETRA-NTP-MIB", "tmnxNtpMaxFreqDftExceed")
)
if mibBuilder.loadTexts:
    tmnxNtpObsoleteNotficatnV6v0Grp.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxNtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 1, 1)
)
tmnxNtpCompliance.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpGlobalGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpBroadcastGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpMulticastGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpServersGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpAuthKeyGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpNotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxNtpCompliance.setStatus(
        "obsolete"
    )

tmnxNtpV4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 1, 2)
)
tmnxNtpV4v0Compliance.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpGlobalGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpBroadcastGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpMulticastGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpServersGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpAuthKeyGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpNotificationV4v0Group"))
)
if mibBuilder.loadTexts:
    tmnxNtpV4v0Compliance.setStatus(
        "obsolete"
    )

tmnxNtpV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 1, 3)
)
tmnxNtpV6v0Compliance.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpGlobalGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpBroadcastGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpMulticastGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpServersGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpAuthKeyGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpNotificationV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxNtpV6v0Compliance.setStatus(
        "obsolete"
    )

tmnxNtpV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 38, 1, 4)
)
tmnxNtpV8v0Compliance.setObjects(
      *(("TIMETRA-NTP-MIB", "tmnxNtpGlobalV8v0Group"),
        ("TIMETRA-NTP-MIB", "tmnxNtpV8v0Group"),
        ("TIMETRA-NTP-MIB", "tmnxNtpBroadcastGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpMulticastGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpServersGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpPeersGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpAuthKeyGroup"),
        ("TIMETRA-NTP-MIB", "tmnxNtpNotificationV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxNtpV8v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-NTP-MIB",
    **{"NTPTimeStamp": NTPTimeStamp,
       "NTPLeapIndicator": NTPLeapIndicator,
       "NTPSignedTimeValue": NTPSignedTimeValue,
       "NTPUnsignedTimeValue": NTPUnsignedTimeValue,
       "NTPStratum": NTPStratum,
       "NTPRefId": NTPRefId,
       "NTPPollInterval": NTPPollInterval,
       "NTPAssocIdentifier": NTPAssocIdentifier,
       "NTPVersion": NTPVersion,
       "TmnxNtpDirection": TmnxNtpDirection,
       "timetraNtpMIBModule": timetraNtpMIBModule,
       "tmnxNtpConformance": tmnxNtpConformance,
       "tmnxNtpCompliances": tmnxNtpCompliances,
       "tmnxNtpCompliance": tmnxNtpCompliance,
       "tmnxNtpV4v0Compliance": tmnxNtpV4v0Compliance,
       "tmnxNtpV6v0Compliance": tmnxNtpV6v0Compliance,
       "tmnxNtpV8v0Compliance": tmnxNtpV8v0Compliance,
       "tmnxNtpGroups": tmnxNtpGroups,
       "tmnxNtpGlobalGroup": tmnxNtpGlobalGroup,
       "tmnxNtpBroadcastGroup": tmnxNtpBroadcastGroup,
       "tmnxNtpMulticastGroup": tmnxNtpMulticastGroup,
       "tmnxNtpServersGroup": tmnxNtpServersGroup,
       "tmnxNtpPeersGroup": tmnxNtpPeersGroup,
       "tmnxNtpAuthKeyGroup": tmnxNtpAuthKeyGroup,
       "tmnxNtpNotificationGroup": tmnxNtpNotificationGroup,
       "tmnxNtpNotifyObjsGroup": tmnxNtpNotifyObjsGroup,
       "tmnxNtpObsoleteNotificationV4v0Group": tmnxNtpObsoleteNotificationV4v0Group,
       "tmnxNtpNotificationV4v0Group": tmnxNtpNotificationV4v0Group,
       "tmnxNtpNotificationV6v0Group": tmnxNtpNotificationV6v0Group,
       "tmnxNtpObsoleteNotficatnV6v0Grp": tmnxNtpObsoleteNotficatnV6v0Grp,
       "tmnxNtpObsoleteV8v0Group": tmnxNtpObsoleteV8v0Group,
       "tmnxNtpGlobalV8v0Group": tmnxNtpGlobalV8v0Group,
       "tmnxNtpV8v0Group": tmnxNtpV8v0Group,
       "tmnxNtpObjs": tmnxNtpObjs,
       "tmnxNtpSysObjs": tmnxNtpSysObjs,
       "tmnxNtpSystem": tmnxNtpSystem,
       "tmnxNtpSysLeap": tmnxNtpSysLeap,
       "tmnxNtpSysStratum": tmnxNtpSysStratum,
       "tmnxNtpSysRefId": tmnxNtpSysRefId,
       "tmnxNtpSysRefTime": tmnxNtpSysRefTime,
       "tmnxNtpSysPoll": tmnxNtpSysPoll,
       "tmnxNtpSysPeer": tmnxNtpSysPeer,
       "tmnxNtpSysClock": tmnxNtpSysClock,
       "tmnxNtp": tmnxNtp,
       "tmnxNtpAdminState": tmnxNtpAdminState,
       "tmnxNtpOperState": tmnxNtpOperState,
       "tmnxNtpServer": tmnxNtpServer,
       "tmnxNtpServerKeyId": tmnxNtpServerKeyId,
       "tmnxNtpAuthCheck": tmnxNtpAuthCheck,
       "tmnxNtpBroadcastTable": tmnxNtpBroadcastTable,
       "tmnxNtpBroadcastEntry": tmnxNtpBroadcastEntry,
       "tmnxNtpBroadcastDirection": tmnxNtpBroadcastDirection,
       "tmnxNtpBroadcastIfIndex": tmnxNtpBroadcastIfIndex,
       "tmnxNtpBroadcastEntryStatus": tmnxNtpBroadcastEntryStatus,
       "tmnxNtpBroadcastLastChanged": tmnxNtpBroadcastLastChanged,
       "tmnxNtpBroadcastAuthKeyId": tmnxNtpBroadcastAuthKeyId,
       "tmnxNtpBroadcastVersion": tmnxNtpBroadcastVersion,
       "tmnxNtpBroadcastTtl": tmnxNtpBroadcastTtl,
       "tmnxNtpBroadcastAuthErrs": tmnxNtpBroadcastAuthErrs,
       "tmnxNtpBroadcastAuthenticate": tmnxNtpBroadcastAuthenticate,
       "tmnxNtpBroadcastAssocId": tmnxNtpBroadcastAssocId,
       "tmnxNtpMulticastTable": tmnxNtpMulticastTable,
       "tmnxNtpMulticastEntry": tmnxNtpMulticastEntry,
       "tmnxNtpMulticastDirection": tmnxNtpMulticastDirection,
       "tmnxNtpMulticastIfIndex": tmnxNtpMulticastIfIndex,
       "tmnxNtpMulticastAddressType": tmnxNtpMulticastAddressType,
       "tmnxNtpMulticastAddress": tmnxNtpMulticastAddress,
       "tmnxNtpMulticastEntryStatus": tmnxNtpMulticastEntryStatus,
       "tmnxNtpMulticastLastChanged": tmnxNtpMulticastLastChanged,
       "tmnxNtpMulticastAuthKeyId": tmnxNtpMulticastAuthKeyId,
       "tmnxNtpMulticastVersion": tmnxNtpMulticastVersion,
       "tmnxNtpMulticastTtl": tmnxNtpMulticastTtl,
       "tmnxNtpMulticastAuthErrs": tmnxNtpMulticastAuthErrs,
       "tmnxNtpMulticastAuthenticate": tmnxNtpMulticastAuthenticate,
       "tmnxNtpMulticastAssocId": tmnxNtpMulticastAssocId,
       "tmnxNtpServers": tmnxNtpServers,
       "tmnxNtpServersTable": tmnxNtpServersTable,
       "tmnxNtpServersEntry": tmnxNtpServersEntry,
       "tmnxNtpServersAddrType": tmnxNtpServersAddrType,
       "tmnxNtpServersAddress": tmnxNtpServersAddress,
       "tmnxNtpServersEntryStatus": tmnxNtpServersEntryStatus,
       "tmnxNtpServersLastChanged": tmnxNtpServersLastChanged,
       "tmnxNtpServersAuthKeyId": tmnxNtpServersAuthKeyId,
       "tmnxNtpServersVersion": tmnxNtpServersVersion,
       "tmnxNtpServersPrefer": tmnxNtpServersPrefer,
       "tmnxNtpServersAssocId": tmnxNtpServersAssocId,
       "tmnxNtpServersAuthErrs": tmnxNtpServersAuthErrs,
       "tmnxNtpPeers": tmnxNtpPeers,
       "tmnxNtpPeersTable": tmnxNtpPeersTable,
       "tmnxNtpPeersEntry": tmnxNtpPeersEntry,
       "tmnxNtpPeersAddrType": tmnxNtpPeersAddrType,
       "tmnxNtpPeersAddress": tmnxNtpPeersAddress,
       "tmnxNtpPeersEntryStatus": tmnxNtpPeersEntryStatus,
       "tmnxNtpPeersLastChanged": tmnxNtpPeersLastChanged,
       "tmnxNtpPeersAuthKeyId": tmnxNtpPeersAuthKeyId,
       "tmnxNtpPeersVersion": tmnxNtpPeersVersion,
       "tmnxNtpPeersPrefer": tmnxNtpPeersPrefer,
       "tmnxNtpPeersAssocId": tmnxNtpPeersAssocId,
       "tmnxNtpPeersAuthErrs": tmnxNtpPeersAuthErrs,
       "tmnxNtpPeersVarTable": tmnxNtpPeersVarTable,
       "tmnxNtpPeersVarEntry": tmnxNtpPeersVarEntry,
       "tmnxNtpPeersVarAssocId": tmnxNtpPeersVarAssocId,
       "tmnxNtpPeersConfigured": tmnxNtpPeersConfigured,
       "tmnxNtpPeersPeerAddrType": tmnxNtpPeersPeerAddrType,
       "tmnxNtpPeersPeerAddress": tmnxNtpPeersPeerAddress,
       "tmnxNtpPeersPeerPort": tmnxNtpPeersPeerPort,
       "tmnxNtpPeersHostAddrType": tmnxNtpPeersHostAddrType,
       "tmnxNtpPeersHostAddress": tmnxNtpPeersHostAddress,
       "tmnxNtpPeersHostPort": tmnxNtpPeersHostPort,
       "tmnxNtpPeersMode": tmnxNtpPeersMode,
       "tmnxNtpPeersStratum": tmnxNtpPeersStratum,
       "tmnxNtpPeersPeerPoll": tmnxNtpPeersPeerPoll,
       "tmnxNtpPeersHostPoll": tmnxNtpPeersHostPoll,
       "tmnxNtpPeersRefId": tmnxNtpPeersRefId,
       "tmnxNtpPeersReceiveTime": tmnxNtpPeersReceiveTime,
       "tmnxNtpPeersReach": tmnxNtpPeersReach,
       "tmnxNtpPeersOffset": tmnxNtpPeersOffset,
       "tmnxNtpPeersPrefPeer": tmnxNtpPeersPrefPeer,
       "tmnxNtpPeersStatus": tmnxNtpPeersStatus,
       "tmnxNtpPeersStatusFlags": tmnxNtpPeersStatusFlags,
       "tmnxNtpFilter": tmnxNtpFilter,
       "tmnxNtpAuthKeys": tmnxNtpAuthKeys,
       "tmnxNtpAuthKeyTable": tmnxNtpAuthKeyTable,
       "tmnxNtpAuthKeyEntry": tmnxNtpAuthKeyEntry,
       "tmnxNtpAuthKeyId": tmnxNtpAuthKeyId,
       "tmnxNtpAuthKeyEntryStatus": tmnxNtpAuthKeyEntryStatus,
       "tmnxNtpAuthKeyLastChanged": tmnxNtpAuthKeyLastChanged,
       "tmnxNtpAuthKey": tmnxNtpAuthKey,
       "tmnxNtpAuthKeyType": tmnxNtpAuthKeyType,
       "tmnxNtpNotifyObjs": tmnxNtpNotifyObjs,
       "tmnxNtpUTCOffset": tmnxNtpUTCOffset,
       "tmnxNtpUTCOffsetThreshold": tmnxNtpUTCOffsetThreshold,
       "tmnxNtpAuthKeyFailType": tmnxNtpAuthKeyFailType,
       "tmnxNtpConfigs": tmnxNtpConfigs,
       "tmnxNtpConfigTable": tmnxNtpConfigTable,
       "tmnxNtpConfigEntry": tmnxNtpConfigEntry,
       "tmnxNtpConfigRowStatus": tmnxNtpConfigRowStatus,
       "tmnxNtpConfigAdminState": tmnxNtpConfigAdminState,
       "tmnxNtpConfigServer": tmnxNtpConfigServer,
       "tmnxNtpConfigServerAuthenticate": tmnxNtpConfigServerAuthenticate,
       "tmnxNtpConfigAuthCheck": tmnxNtpConfigAuthCheck,
       "tmnxNtpClientInfoTable": tmnxNtpClientInfoTable,
       "tmnxNtpClientInfoEntry": tmnxNtpClientInfoEntry,
       "tmnxNtpClientAddressType": tmnxNtpClientAddressType,
       "tmnxNtpClientAddress": tmnxNtpClientAddress,
       "tmnxNtpClientInfoLastRequestTime": tmnxNtpClientInfoLastRequestTime,
       "tmnxNtpNotifyPrefix": tmnxNtpNotifyPrefix,
       "tmnxNtpNotifications": tmnxNtpNotifications,
       "tmnxNtpAuthMismatch": tmnxNtpAuthMismatch,
       "tmnxNtpNoServersAvail": tmnxNtpNoServersAvail,
       "tmnxNtpServersAvail": tmnxNtpServersAvail,
       "tmnxNtpMaxFreqDftExceed": tmnxNtpMaxFreqDftExceed,
       "tmnxNtpUtcOffsetExThreshold": tmnxNtpUtcOffsetExThreshold,
       "tmnxNtpUtcOffsetInThreshold": tmnxNtpUtcOffsetInThreshold,
       "tmnxNtpOperChange": tmnxNtpOperChange,
       "tmnxNtpServerChange": tmnxNtpServerChange}
)

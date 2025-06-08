# SNMP MIB module (RUIJIE-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-NTP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:07 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijieNtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49)
)
if mibBuilder.loadTexts:
    ruijieNtpMIB.setRevisions(
        ("2009-05-14 00:00",)
    )


# Types definitions



class NTPTimeStamp(OctetString):
    """Custom type NTPTimeStamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8





class NTPLeapIndicator(Integer32):
    """Custom type NTPLeapIndicator based on Integer32"""
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





class NTPSignedTimeValue(OctetString):
    """Custom type NTPSignedTimeValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4





class NTPUnsignedTimeValue(OctetString):
    """Custom type NTPUnsignedTimeValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4





class NTPStratum(Integer32):
    """Custom type NTPStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class NTPRefId(OctetString):
    """Custom type NTPRefId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieNtpMIBObjects_ObjectIdentity = ObjectIdentity
ruijieNtpMIBObjects = _RuijieNtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1)
)
_RuijientpSystem_ObjectIdentity = ObjectIdentity
ruijientpSystem = _RuijientpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 1)
)
_RuijientpSysLeap_Type = NTPLeapIndicator
_RuijientpSysLeap_Object = MibScalar
ruijientpSysLeap = _RuijientpSysLeap_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 1, 1),
    _RuijientpSysLeap_Type()
)
ruijientpSysLeap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijientpSysLeap.setStatus("current")
_RuijientpSysStratum_Type = NTPStratum
_RuijientpSysStratum_Object = MibScalar
ruijientpSysStratum = _RuijientpSysStratum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 1, 2),
    _RuijientpSysStratum_Type()
)
ruijientpSysStratum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijientpSysStratum.setStatus("current")


class _RuijientpSysPrecision_Type(Integer32):
    """Custom type ruijientpSysPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-24, 24),
    )


_RuijientpSysPrecision_Type.__name__ = "Integer32"
_RuijientpSysPrecision_Object = MibScalar
ruijientpSysPrecision = _RuijientpSysPrecision_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 1, 3),
    _RuijientpSysPrecision_Type()
)
ruijientpSysPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijientpSysPrecision.setStatus("current")
_RuijientpSysRootDelay_Type = NTPSignedTimeValue
_RuijientpSysRootDelay_Object = MibScalar
ruijientpSysRootDelay = _RuijientpSysRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 1, 4),
    _RuijientpSysRootDelay_Type()
)
ruijientpSysRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijientpSysRootDelay.setStatus("current")
_RuijientpSysRootDispersion_Type = NTPUnsignedTimeValue
_RuijientpSysRootDispersion_Object = MibScalar
ruijientpSysRootDispersion = _RuijientpSysRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 1, 5),
    _RuijientpSysRootDispersion_Type()
)
ruijientpSysRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijientpSysRootDispersion.setStatus("current")
_RuijientpSysRefId_Type = NTPRefId
_RuijientpSysRefId_Object = MibScalar
ruijientpSysRefId = _RuijientpSysRefId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 1, 6),
    _RuijientpSysRefId_Type()
)
ruijientpSysRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijientpSysRefId.setStatus("current")
_RuijientpSysRefTime_Type = NTPTimeStamp
_RuijientpSysRefTime_Object = MibScalar
ruijientpSysRefTime = _RuijientpSysRefTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 1, 7),
    _RuijientpSysRefTime_Type()
)
ruijientpSysRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijientpSysRefTime.setStatus("current")
_RuijieNTPServerIPAdd_Type = IpAddress
_RuijieNTPServerIPAdd_Object = MibScalar
ruijieNTPServerIPAdd = _RuijieNTPServerIPAdd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 1, 8),
    _RuijieNTPServerIPAdd_Type()
)
ruijieNTPServerIPAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNTPServerIPAdd.setStatus("current")


class _RuijieTimeAfterNTPCal_Type(OctetString):
    """Custom type ruijieTimeAfterNTPCal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_RuijieTimeAfterNTPCal_Type.__name__ = "OctetString"
_RuijieTimeAfterNTPCal_Object = MibScalar
ruijieTimeAfterNTPCal = _RuijieTimeAfterNTPCal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 1, 9),
    _RuijieTimeAfterNTPCal_Type()
)
ruijieTimeAfterNTPCal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTimeAfterNTPCal.setStatus("current")


class _RuijieTimeSyncPeriod_Type(Integer32):
    """Custom type ruijieTimeSyncPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8640000),
    )


_RuijieTimeSyncPeriod_Type.__name__ = "Integer32"
_RuijieTimeSyncPeriod_Object = MibScalar
ruijieTimeSyncPeriod = _RuijieTimeSyncPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 1, 10),
    _RuijieTimeSyncPeriod_Type()
)
ruijieTimeSyncPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieTimeSyncPeriod.setStatus("current")
_RuijieNtpServerTable_Object = MibTable
ruijieNtpServerTable = _RuijieNtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 1, 11)
)
if mibBuilder.loadTexts:
    ruijieNtpServerTable.setStatus("current")
_RuijieNtpServerEntry_Object = MibTableRow
ruijieNtpServerEntry = _RuijieNtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 1, 11, 1)
)
ruijieNtpServerEntry.setIndexNames(
    (0, "RUIJIE-NTP-MIB", "ruijieNtpServerNetType"),
    (0, "RUIJIE-NTP-MIB", "ruijieNtpServerNetAddr"),
)
if mibBuilder.loadTexts:
    ruijieNtpServerEntry.setStatus("current")
_RuijieNtpServerNetType_Type = InetAddressType
_RuijieNtpServerNetType_Object = MibTableColumn
ruijieNtpServerNetType = _RuijieNtpServerNetType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 1, 11, 1, 1),
    _RuijieNtpServerNetType_Type()
)
ruijieNtpServerNetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNtpServerNetType.setStatus("current")
_RuijieNtpServerNetAddr_Type = InetAddress
_RuijieNtpServerNetAddr_Object = MibTableColumn
ruijieNtpServerNetAddr = _RuijieNtpServerNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 1, 11, 1, 2),
    _RuijieNtpServerNetAddr_Type()
)
ruijieNtpServerNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNtpServerNetAddr.setStatus("current")


class _RuijieNtpServerVersion_Type(Integer32):
    """Custom type ruijieNtpServerVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2),
          ("version3", 3))
    )


_RuijieNtpServerVersion_Type.__name__ = "Integer32"
_RuijieNtpServerVersion_Object = MibTableColumn
ruijieNtpServerVersion = _RuijieNtpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 1, 11, 1, 3),
    _RuijieNtpServerVersion_Type()
)
ruijieNtpServerVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieNtpServerVersion.setStatus("current")
_RuijieNtpServerStatus_Type = RowStatus
_RuijieNtpServerStatus_Object = MibTableColumn
ruijieNtpServerStatus = _RuijieNtpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 1, 11, 1, 4),
    _RuijieNtpServerStatus_Type()
)
ruijieNtpServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieNtpServerStatus.setStatus("current")


class _RuijientpSysState_Type(Integer32):
    """Custom type ruijientpSysState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unsynchronized", 0),
          ("synchronized", 1))
    )


_RuijientpSysState_Type.__name__ = "Integer32"
_RuijientpSysState_Object = MibScalar
ruijientpSysState = _RuijientpSysState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 1, 12),
    _RuijientpSysState_Type()
)
ruijientpSysState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijientpSysState.setStatus("current")
_RuijieNtpMIBTrap_ObjectIdentity = ObjectIdentity
ruijieNtpMIBTrap = _RuijieNtpMIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 2)
)


class _RuijientpSysServerIPAdd_Type(DisplayString):
    """Custom type ruijientpSysServerIPAdd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RuijientpSysServerIPAdd_Type.__name__ = "DisplayString"
_RuijientpSysServerIPAdd_Object = MibScalar
ruijientpSysServerIPAdd = _RuijientpSysServerIPAdd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 2, 2),
    _RuijientpSysServerIPAdd_Type()
)
ruijientpSysServerIPAdd.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijientpSysServerIPAdd.setStatus("current")


class _RuijientpSourceVpnName_Type(DisplayString):
    """Custom type ruijientpSourceVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijientpSourceVpnName_Type.__name__ = "DisplayString"
_RuijientpSourceVpnName_Object = MibScalar
ruijientpSourceVpnName = _RuijientpSourceVpnName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 2, 3),
    _RuijientpSourceVpnName_Type()
)
ruijientpSourceVpnName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijientpSourceVpnName.setStatus("current")


class _RuijientpOldSysServerIPAdd_Type(DisplayString):
    """Custom type ruijientpOldSysServerIPAdd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RuijientpOldSysServerIPAdd_Type.__name__ = "DisplayString"
_RuijientpOldSysServerIPAdd_Object = MibScalar
ruijientpOldSysServerIPAdd = _RuijientpOldSysServerIPAdd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 2, 4),
    _RuijientpOldSysServerIPAdd_Type()
)
ruijientpOldSysServerIPAdd.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijientpOldSysServerIPAdd.setStatus("current")


class _RuijientpOldSourceVpnName_Type(DisplayString):
    """Custom type ruijientpOldSourceVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijientpOldSourceVpnName_Type.__name__ = "DisplayString"
_RuijientpOldSourceVpnName_Object = MibScalar
ruijientpOldSourceVpnName = _RuijientpOldSourceVpnName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 2, 5),
    _RuijientpOldSourceVpnName_Type()
)
ruijientpOldSourceVpnName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijientpOldSourceVpnName.setStatus("current")
_RuijieNtpMIBConformance_ObjectIdentity = ObjectIdentity
ruijieNtpMIBConformance = _RuijieNtpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 2)
)
_RuijieNtpMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieNtpMIBCompliances = _RuijieNtpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 2, 1)
)
_RuijieNtpMIBGroups_ObjectIdentity = ObjectIdentity
ruijieNtpMIBGroups = _RuijieNtpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 2, 2)
)

# Managed Objects groups

ruijieNtpSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 2, 2, 1)
)
ruijieNtpSysGroup.setObjects(
      *(("RUIJIE-NTP-MIB", "ruijientpSysLeap"),
        ("RUIJIE-NTP-MIB", "ruijientpSysStratum"),
        ("RUIJIE-NTP-MIB", "ruijientpSysPrecision"),
        ("RUIJIE-NTP-MIB", "ruijientpSysRootDelay"),
        ("RUIJIE-NTP-MIB", "ruijientpSysRootDispersion"),
        ("RUIJIE-NTP-MIB", "ruijientpSysRefId"),
        ("RUIJIE-NTP-MIB", "ruijientpSysRefTime"),
        ("RUIJIE-NTP-MIB", "ruijieNTPServerIPAdd"),
        ("RUIJIE-NTP-MIB", "ruijieTimeAfterNTPCal"),
        ("RUIJIE-NTP-MIB", "ruijieTimeSyncPeriod"),
        ("RUIJIE-NTP-MIB", "ruijieNtpServerNetType"),
        ("RUIJIE-NTP-MIB", "ruijieNtpServerNetAddr"),
        ("RUIJIE-NTP-MIB", "ruijieNtpServerVersion"),
        ("RUIJIE-NTP-MIB", "ruijieNtpServerStatus"),
        ("RUIJIE-NTP-MIB", "ruijientpSysState"))
)
if mibBuilder.loadTexts:
    ruijieNtpSysGroup.setStatus("current")


# Notification objects

ruijieNtpStatussyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 2, 1)
)
ruijieNtpStatussyncTrap.setObjects(
      *(("RUIJIE-NTP-MIB", "ruijientpSysState"),
        ("RUIJIE-NTP-MIB", "ruijientpSysServerIPAdd"),
        ("RUIJIE-NTP-MIB", "ruijientpSourceVpnName"))
)
if mibBuilder.loadTexts:
    ruijieNtpStatussyncTrap.setStatus(
        "current"
    )

ruijieNtpSysPeerChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 1, 2, 6)
)
ruijieNtpSysPeerChangeTrap.setObjects(
      *(("RUIJIE-NTP-MIB", "ruijientpSysServerIPAdd"),
        ("RUIJIE-NTP-MIB", "ruijientpSourceVpnName"),
        ("RUIJIE-NTP-MIB", "ruijientpOldSysServerIPAdd"),
        ("RUIJIE-NTP-MIB", "ruijientpOldSourceVpnName"))
)
if mibBuilder.loadTexts:
    ruijieNtpSysPeerChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijieNtpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 49, 2, 1, 1)
)
ruijieNtpMIBCompliance.setObjects(
    ("RUIJIE-NTP-MIB", "ruijieNtpMIBGroups")
)
if mibBuilder.loadTexts:
    ruijieNtpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-NTP-MIB",
    **{"NTPTimeStamp": NTPTimeStamp,
       "NTPLeapIndicator": NTPLeapIndicator,
       "NTPSignedTimeValue": NTPSignedTimeValue,
       "NTPUnsignedTimeValue": NTPUnsignedTimeValue,
       "NTPStratum": NTPStratum,
       "NTPRefId": NTPRefId,
       "ruijieNtpMIB": ruijieNtpMIB,
       "ruijieNtpMIBObjects": ruijieNtpMIBObjects,
       "ruijientpSystem": ruijientpSystem,
       "ruijientpSysLeap": ruijientpSysLeap,
       "ruijientpSysStratum": ruijientpSysStratum,
       "ruijientpSysPrecision": ruijientpSysPrecision,
       "ruijientpSysRootDelay": ruijientpSysRootDelay,
       "ruijientpSysRootDispersion": ruijientpSysRootDispersion,
       "ruijientpSysRefId": ruijientpSysRefId,
       "ruijientpSysRefTime": ruijientpSysRefTime,
       "ruijieNTPServerIPAdd": ruijieNTPServerIPAdd,
       "ruijieTimeAfterNTPCal": ruijieTimeAfterNTPCal,
       "ruijieTimeSyncPeriod": ruijieTimeSyncPeriod,
       "ruijieNtpServerTable": ruijieNtpServerTable,
       "ruijieNtpServerEntry": ruijieNtpServerEntry,
       "ruijieNtpServerNetType": ruijieNtpServerNetType,
       "ruijieNtpServerNetAddr": ruijieNtpServerNetAddr,
       "ruijieNtpServerVersion": ruijieNtpServerVersion,
       "ruijieNtpServerStatus": ruijieNtpServerStatus,
       "ruijientpSysState": ruijientpSysState,
       "ruijieNtpMIBTrap": ruijieNtpMIBTrap,
       "ruijieNtpStatussyncTrap": ruijieNtpStatussyncTrap,
       "ruijientpSysServerIPAdd": ruijientpSysServerIPAdd,
       "ruijientpSourceVpnName": ruijientpSourceVpnName,
       "ruijientpOldSysServerIPAdd": ruijientpOldSysServerIPAdd,
       "ruijientpOldSourceVpnName": ruijientpOldSourceVpnName,
       "ruijieNtpSysPeerChangeTrap": ruijieNtpSysPeerChangeTrap,
       "ruijieNtpMIBConformance": ruijieNtpMIBConformance,
       "ruijieNtpMIBCompliances": ruijieNtpMIBCompliances,
       "ruijieNtpMIBCompliance": ruijieNtpMIBCompliance,
       "ruijieNtpMIBGroups": ruijieNtpMIBGroups,
       "ruijieNtpSysGroup": ruijieNtpSysGroup}
)

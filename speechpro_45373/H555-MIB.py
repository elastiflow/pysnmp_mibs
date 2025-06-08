# SNMP MIB module (H555-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/speechpro_45373/H555-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:02:11 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(speechpro,) = mibBuilder.importSymbols(
    "SPEECHPRO-MIB",
    "speechpro")


# MODULE-IDENTITY

h555 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45373, 1)
)
if mibBuilder.loadTexts:
    h555.setRevisions(
        ("2016-05-06 00:00",
         "2015-11-09 00:00",
         "2014-09-18 00:00",
         "2014-09-15 00:00",
         "2014-09-12 00:00",
         "2014-09-12 00:00",
         "2014-09-04 00:00",
         "2014-08-15 00:00",
         "2014-08-04 00:00",
         "2014-07-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class H555IpAddrEntry(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d.1d.1d.1d/1d.1d.1d.1d/1d.1d.1d.1d"


# MIB Managed Objects in the order of their OIDs

_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1)
)
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 1),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_TimeSettings_ObjectIdentity = ObjectIdentity
timeSettings = _TimeSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 2)
)
_Date_Type = DisplayString
_Date_Object = MibScalar
date = _Date_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 2, 1),
    _Date_Type()
)
date.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    date.setStatus("current")
_Time_Type = DisplayString
_Time_Object = MibScalar
time = _Time_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 2, 2),
    _Time_Type()
)
time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time.setStatus("current")
_UnixTime_Type = Unsigned32
_UnixTime_Object = MibScalar
unixTime = _UnixTime_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 2, 3),
    _UnixTime_Type()
)
unixTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unixTime.setStatus("current")
_UnixTimeExt_Type = Unsigned32
_UnixTimeExt_Object = MibScalar
unixTimeExt = _UnixTimeExt_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 2, 4),
    _UnixTimeExt_Type()
)
unixTimeExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unixTimeExt.setStatus("current")
_Timezone_Type = DisplayString
_Timezone_Object = MibScalar
timezone = _Timezone_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 2, 5),
    _Timezone_Type()
)
timezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timezone.setStatus("current")


class _NtpEnabled_Type(Integer32):
    """Custom type ntpEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NtpEnabled_Type.__name__ = "Integer32"
_NtpEnabled_Object = MibScalar
ntpEnabled = _NtpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 2, 6),
    _NtpEnabled_Type()
)
ntpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpEnabled.setStatus("current")
_NtpServer_Type = DisplayString
_NtpServer_Object = MibScalar
ntpServer = _NtpServer_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 2, 7),
    _NtpServer_Type()
)
ntpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServer.setStatus("current")


class _NtpServerRestart_Type(Integer32):
    """Custom type ntpServerRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NtpServerRestart_Type.__name__ = "Integer32"
_NtpServerRestart_Object = MibScalar
ntpServerRestart = _NtpServerRestart_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 2, 8),
    _NtpServerRestart_Type()
)
ntpServerRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServerRestart.setStatus("current")
_MediaStreamSettings_ObjectIdentity = ObjectIdentity
mediaStreamSettings = _MediaStreamSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 3)
)


class _Maxport_Type(Integer32):
    """Custom type maxport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_Maxport_Type.__name__ = "Integer32"
_Maxport_Object = MibScalar
maxport = _Maxport_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 3, 1),
    _Maxport_Type()
)
maxport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxport.setStatus("current")


class _Minport_Type(Integer32):
    """Custom type minport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_Minport_Type.__name__ = "Integer32"
_Minport_Object = MibScalar
minport = _Minport_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 3, 2),
    _Minport_Type()
)
minport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minport.setStatus("current")
_FilenameTemplate_Type = DisplayString
_FilenameTemplate_Object = MibScalar
filenameTemplate = _FilenameTemplate_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 3, 3),
    _FilenameTemplate_Type()
)
filenameTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filenameTemplate.setStatus("current")
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 4)
)
_FreeSpace_Type = DisplayString
_FreeSpace_Object = MibScalar
freeSpace = _FreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 4, 1),
    _FreeSpace_Type()
)
freeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeSpace.setStatus("current")
_TotalSpace_Type = DisplayString
_TotalSpace_Object = MibScalar
totalSpace = _TotalSpace_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 4, 2),
    _TotalSpace_Type()
)
totalSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalSpace.setStatus("current")
_UsedSpace_Type = DisplayString
_UsedSpace_Object = MibScalar
usedSpace = _UsedSpace_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 4, 3),
    _UsedSpace_Type()
)
usedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usedSpace.setStatus("current")
_Sensors_ObjectIdentity = ObjectIdentity
sensors = _Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 5)
)
_Cputemp_Type = Integer32
_Cputemp_Object = MibScalar
cputemp = _Cputemp_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 5, 1),
    _Cputemp_Type()
)
cputemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cputemp.setStatus("current")
_Hddtemp_Type = Integer32
_Hddtemp_Object = MibScalar
hddtemp = _Hddtemp_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 5, 2),
    _Hddtemp_Type()
)
hddtemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddtemp.setStatus("current")
_Netconfig_ObjectIdentity = ObjectIdentity
netconfig = _Netconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 6)
)
_MacAddress_Type = DisplayString
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 6, 1),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")


class _DhcpClient_Type(Integer32):
    """Custom type dhcpClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DhcpClient_Type.__name__ = "Integer32"
_DhcpClient_Object = MibScalar
dhcpClient = _DhcpClient_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 6, 2),
    _DhcpClient_Type()
)
dhcpClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClient.setStatus("current")
_IpConfig_Type = H555IpAddrEntry
_IpConfig_Object = MibScalar
ipConfig = _IpConfig_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 6, 3),
    _IpConfig_Type()
)
ipConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfig.setStatus("current")
_RouteTable_Object = MibTable
routeTable = _RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 6, 7)
)
if mibBuilder.loadTexts:
    routeTable.setStatus("current")
_RouteEntry_Object = MibTableRow
routeEntry = _RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 6, 7, 1)
)
routeEntry.setIndexNames(
    (0, "H555-MIB", "routeIndex"),
)
if mibBuilder.loadTexts:
    routeEntry.setStatus("current")


class _RouteIndex_Type(Integer32):
    """Custom type routeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_RouteIndex_Type.__name__ = "Integer32"
_RouteIndex_Object = MibTableColumn
routeIndex = _RouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 6, 7, 1, 1),
    _RouteIndex_Type()
)
routeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeIndex.setStatus("current")
_RouteDestIp_Type = IpAddress
_RouteDestIp_Object = MibTableColumn
routeDestIp = _RouteDestIp_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 6, 7, 1, 2),
    _RouteDestIp_Type()
)
routeDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeDestIp.setStatus("current")
_RouteDestNetMask_Type = IpAddress
_RouteDestNetMask_Object = MibTableColumn
routeDestNetMask = _RouteDestNetMask_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 6, 7, 1, 3),
    _RouteDestNetMask_Type()
)
routeDestNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeDestNetMask.setStatus("current")
_RouteGateway_Type = IpAddress
_RouteGateway_Object = MibTableColumn
routeGateway = _RouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 6, 7, 1, 4),
    _RouteGateway_Type()
)
routeGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeGateway.setStatus("current")
_LogTable_Object = MibTable
logTable = _LogTable_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 7)
)
if mibBuilder.loadTexts:
    logTable.setStatus("current")
_LogEntry_Object = MibTableRow
logEntry = _LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 7, 1)
)
logEntry.setIndexNames(
    (0, "H555-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    logEntry.setStatus("current")


class _LogIndex_Type(Integer32):
    """Custom type logIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_LogIndex_Type.__name__ = "Integer32"
_LogIndex_Object = MibTableColumn
logIndex = _LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 7, 1, 1),
    _LogIndex_Type()
)
logIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logIndex.setStatus("current")
_LogTime_Type = DisplayString
_LogTime_Object = MibTableColumn
logTime = _LogTime_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 7, 1, 2),
    _LogTime_Type()
)
logTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTime.setStatus("current")
_LogUser_Type = DisplayString
_LogUser_Object = MibTableColumn
logUser = _LogUser_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 7, 1, 3),
    _LogUser_Type()
)
logUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logUser.setStatus("current")
_LogHost_Type = DisplayString
_LogHost_Object = MibTableColumn
logHost = _LogHost_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 7, 1, 4),
    _LogHost_Type()
)
logHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logHost.setStatus("current")
_LogAction_Type = DisplayString
_LogAction_Object = MibTableColumn
logAction = _LogAction_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 7, 1, 5),
    _LogAction_Type()
)
logAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logAction.setStatus("current")


class _LogResult_Type(Integer32):
    """Custom type logResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LogResult_Type.__name__ = "Integer32"
_LogResult_Object = MibTableColumn
logResult = _LogResult_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 7, 1, 6),
    _LogResult_Type()
)
logResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logResult.setStatus("current")
_LogResultReason_Type = DisplayString
_LogResultReason_Object = MibTableColumn
logResultReason = _LogResultReason_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 7, 1, 7),
    _LogResultReason_Type()
)
logResultReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logResultReason.setStatus("current")
_LogDetails_Type = OctetString
_LogDetails_Object = MibTableColumn
logDetails = _LogDetails_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 1, 7, 1, 8),
    _LogDetails_Type()
)
logDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logDetails.setStatus("current")
_SnmpConf_ObjectIdentity = ObjectIdentity
snmpConf = _SnmpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45373, 1, 2)
)
_TrapReceicer_Type = IpAddress
_TrapReceicer_Object = MibScalar
trapReceicer = _TrapReceicer_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 2, 1),
    _TrapReceicer_Type()
)
trapReceicer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReceicer.setStatus("current")
_H555Url_Type = OctetString
_H555Url_Object = MibScalar
h555Url = _H555Url_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 2, 2),
    _H555Url_Type()
)
h555Url.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h555Url.setStatus("current")
_H555Login_Type = OctetString
_H555Login_Object = MibScalar
h555Login = _H555Login_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 2, 3),
    _H555Login_Type()
)
h555Login.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h555Login.setStatus("current")
_H555Pass_Type = OctetString
_H555Pass_Object = MibScalar
h555Pass = _H555Pass_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 2, 4),
    _H555Pass_Type()
)
h555Pass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h555Pass.setStatus("current")


class _LogLimit_Type(Integer32):
    """Custom type logLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_LogLimit_Type.__name__ = "Integer32"
_LogLimit_Object = MibScalar
logLimit = _LogLimit_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 2, 5),
    _LogLimit_Type()
)
logLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logLimit.setStatus("current")
_SnmpDebug_Type = Integer32
_SnmpDebug_Object = MibScalar
snmpDebug = _SnmpDebug_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 2, 10),
    _SnmpDebug_Type()
)
snmpDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpDebug.setStatus("current")
_SaveSnmpConf_Type = Integer32
_SaveSnmpConf_Object = MibScalar
saveSnmpConf = _SaveSnmpConf_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 2, 11),
    _SaveSnmpConf_Type()
)
saveSnmpConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveSnmpConf.setStatus("current")
_CamTable_Object = MibTable
camTable = _CamTable_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3)
)
if mibBuilder.loadTexts:
    camTable.setStatus("current")
_CamEntry_Object = MibTableRow
camEntry = _CamEntry_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1)
)
camEntry.setIndexNames(
    (0, "H555-MIB", "camIndex"),
)
if mibBuilder.loadTexts:
    camEntry.setStatus("current")


class _CamIndex_Type(Integer32):
    """Custom type camIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CamIndex_Type.__name__ = "Integer32"
_CamIndex_Object = MibTableColumn
camIndex = _CamIndex_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 1),
    _CamIndex_Type()
)
camIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    camIndex.setStatus("current")
_CamName_Type = DisplayString
_CamName_Object = MibTableColumn
camName = _CamName_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 2),
    _CamName_Type()
)
camName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camName.setStatus("current")


class _CamEnabled_Type(Integer32):
    """Custom type camEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CamEnabled_Type.__name__ = "Integer32"
_CamEnabled_Object = MibTableColumn
camEnabled = _CamEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 3),
    _CamEnabled_Type()
)
camEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camEnabled.setStatus("current")


class _CamRecord_Type(Integer32):
    """Custom type camRecord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CamRecord_Type.__name__ = "Integer32"
_CamRecord_Object = MibTableColumn
camRecord = _CamRecord_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 4),
    _CamRecord_Type()
)
camRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camRecord.setStatus("current")
_CamState_Type = DisplayString
_CamState_Object = MibTableColumn
camState = _CamState_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 5),
    _CamState_Type()
)
camState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camState.setStatus("current")
_CamStoreDuration_Type = Integer32
_CamStoreDuration_Object = MibTableColumn
camStoreDuration = _CamStoreDuration_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 6),
    _CamStoreDuration_Type()
)
camStoreDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camStoreDuration.setStatus("current")


class _CamImportancy_Type(Integer32):
    """Custom type camImportancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_CamImportancy_Type.__name__ = "Integer32"
_CamImportancy_Object = MibTableColumn
camImportancy = _CamImportancy_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 7),
    _CamImportancy_Type()
)
camImportancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camImportancy.setStatus("current")
_CamSize_Type = Integer32
_CamSize_Object = MibTableColumn
camSize = _CamSize_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 8),
    _CamSize_Type()
)
camSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camSize.setStatus("current")


class _CamDuration_Type(Integer32):
    """Custom type camDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1800),
    )


_CamDuration_Type.__name__ = "Integer32"
_CamDuration_Object = MibTableColumn
camDuration = _CamDuration_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 9),
    _CamDuration_Type()
)
camDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camDuration.setStatus("current")


class _CamHasSchedule_Type(Integer32):
    """Custom type camHasSchedule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CamHasSchedule_Type.__name__ = "Integer32"
_CamHasSchedule_Object = MibTableColumn
camHasSchedule = _CamHasSchedule_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 10),
    _CamHasSchedule_Type()
)
camHasSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camHasSchedule.setStatus("current")
_CamComment_Type = SnmpAdminString
_CamComment_Object = MibTableColumn
camComment = _CamComment_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 11),
    _CamComment_Type()
)
camComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camComment.setStatus("current")


class _CamAudio_Type(Integer32):
    """Custom type camAudio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CamAudio_Type.__name__ = "Integer32"
_CamAudio_Object = MibTableColumn
camAudio = _CamAudio_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 12),
    _CamAudio_Type()
)
camAudio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camAudio.setStatus("current")
_CamCompanding_Type = DisplayString
_CamCompanding_Object = MibTableColumn
camCompanding = _CamCompanding_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 13),
    _CamCompanding_Type()
)
camCompanding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camCompanding.setStatus("current")


class _CamAudiorate_Type(Integer32):
    """Custom type camAudiorate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 44100),
    )


_CamAudiorate_Type.__name__ = "Integer32"
_CamAudiorate_Object = MibTableColumn
camAudiorate = _CamAudiorate_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 14),
    _CamAudiorate_Type()
)
camAudiorate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camAudiorate.setStatus("current")


class _CamGain_Type(Integer32):
    """Custom type camGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CamGain_Type.__name__ = "Integer32"
_CamGain_Object = MibTableColumn
camGain = _CamGain_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 15),
    _CamGain_Type()
)
camGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camGain.setStatus("current")


class _CamMicVoltage_Type(Integer32):
    """Custom type camMicVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CamMicVoltage_Type.__name__ = "Integer32"
_CamMicVoltage_Object = MibTableColumn
camMicVoltage = _CamMicVoltage_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 16),
    _CamMicVoltage_Type()
)
camMicVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camMicVoltage.setStatus("current")


class _CamAcStartThreshold_Type(Unsigned32):
    """Custom type camAcStartThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CamAcStartThreshold_Type.__name__ = "Unsigned32"
_CamAcStartThreshold_Object = MibTableColumn
camAcStartThreshold = _CamAcStartThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 17),
    _CamAcStartThreshold_Type()
)
camAcStartThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camAcStartThreshold.setStatus("current")


class _CamVideo_Type(Integer32):
    """Custom type camVideo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CamVideo_Type.__name__ = "Integer32"
_CamVideo_Object = MibTableColumn
camVideo = _CamVideo_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 18),
    _CamVideo_Type()
)
camVideo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camVideo.setStatus("current")
_CamCodec_Type = DisplayString
_CamCodec_Object = MibTableColumn
camCodec = _CamCodec_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 19),
    _CamCodec_Type()
)
camCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camCodec.setStatus("current")
_CamFormat_Type = DisplayString
_CamFormat_Object = MibTableColumn
camFormat = _CamFormat_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 20),
    _CamFormat_Type()
)
camFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camFormat.setStatus("current")


class _CamVideorate_Type(Integer32):
    """Custom type camVideorate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CamVideorate_Type.__name__ = "Integer32"
_CamVideorate_Object = MibTableColumn
camVideorate = _CamVideorate_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 21),
    _CamVideorate_Type()
)
camVideorate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camVideorate.setStatus("current")


class _CamQuality_Type(Integer32):
    """Custom type camQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CamQuality_Type.__name__ = "Integer32"
_CamQuality_Object = MibTableColumn
camQuality = _CamQuality_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 22),
    _CamQuality_Type()
)
camQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camQuality.setStatus("current")


class _CamBitrate_Type(Integer32):
    """Custom type camBitrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_CamBitrate_Type.__name__ = "Integer32"
_CamBitrate_Object = MibTableColumn
camBitrate = _CamBitrate_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 23),
    _CamBitrate_Type()
)
camBitrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camBitrate.setStatus("current")


class _CamVcStartThreshold_Type(Integer32):
    """Custom type camVcStartThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CamVcStartThreshold_Type.__name__ = "Integer32"
_CamVcStartThreshold_Object = MibTableColumn
camVcStartThreshold = _CamVcStartThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 24),
    _CamVcStartThreshold_Type()
)
camVcStartThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camVcStartThreshold.setStatus("current")


class _CamLowRes_Type(Integer32):
    """Custom type camLowRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CamLowRes_Type.__name__ = "Integer32"
_CamLowRes_Object = MibTableColumn
camLowRes = _CamLowRes_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 25),
    _CamLowRes_Type()
)
camLowRes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camLowRes.setStatus("current")


class _CamBrightness_Type(Integer32):
    """Custom type camBrightness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CamBrightness_Type.__name__ = "Integer32"
_CamBrightness_Object = MibTableColumn
camBrightness = _CamBrightness_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 26),
    _CamBrightness_Type()
)
camBrightness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camBrightness.setStatus("current")


class _CamContrast_Type(Integer32):
    """Custom type camContrast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CamContrast_Type.__name__ = "Integer32"
_CamContrast_Object = MibTableColumn
camContrast = _CamContrast_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 27),
    _CamContrast_Type()
)
camContrast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camContrast.setStatus("current")


class _CamGrayscale_Type(Integer32):
    """Custom type camGrayscale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CamGrayscale_Type.__name__ = "Integer32"
_CamGrayscale_Object = MibTableColumn
camGrayscale = _CamGrayscale_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 28),
    _CamGrayscale_Type()
)
camGrayscale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camGrayscale.setStatus("current")


class _CamDeinterlace_Type(Integer32):
    """Custom type camDeinterlace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CamDeinterlace_Type.__name__ = "Integer32"
_CamDeinterlace_Object = MibTableColumn
camDeinterlace = _CamDeinterlace_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 29),
    _CamDeinterlace_Type()
)
camDeinterlace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camDeinterlace.setStatus("current")


class _CamAreaX_Type(Integer32):
    """Custom type camAreaX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 719),
    )


_CamAreaX_Type.__name__ = "Integer32"
_CamAreaX_Object = MibTableColumn
camAreaX = _CamAreaX_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 30),
    _CamAreaX_Type()
)
camAreaX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camAreaX.setStatus("current")


class _CamAreaY_Type(Integer32):
    """Custom type camAreaY based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 575),
    )


_CamAreaY_Type.__name__ = "Integer32"
_CamAreaY_Object = MibTableColumn
camAreaY = _CamAreaY_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 31),
    _CamAreaY_Type()
)
camAreaY.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camAreaY.setStatus("current")


class _CamAreaW_Type(Integer32):
    """Custom type camAreaW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 720),
    )


_CamAreaW_Type.__name__ = "Integer32"
_CamAreaW_Object = MibTableColumn
camAreaW = _CamAreaW_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 32),
    _CamAreaW_Type()
)
camAreaW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camAreaW.setStatus("current")


class _CamAreaH_Type(Integer32):
    """Custom type camAreaH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 576),
    )


_CamAreaH_Type.__name__ = "Integer32"
_CamAreaH_Object = MibTableColumn
camAreaH = _CamAreaH_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 33),
    _CamAreaH_Type()
)
camAreaH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camAreaH.setStatus("current")
_CamVadEventCounter_Type = Integer32
_CamVadEventCounter_Object = MibTableColumn
camVadEventCounter = _CamVadEventCounter_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 34),
    _CamVadEventCounter_Type()
)
camVadEventCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camVadEventCounter.setStatus("current")
_CamMadEventCounter_Type = Integer32
_CamMadEventCounter_Object = MibTableColumn
camMadEventCounter = _CamMadEventCounter_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 35),
    _CamMadEventCounter_Type()
)
camMadEventCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camMadEventCounter.setStatus("current")


class _CamBuffer_Type(Integer32):
    """Custom type camBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CamBuffer_Type.__name__ = "Integer32"
_CamBuffer_Object = MibScalar
camBuffer = _CamBuffer_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 36),
    _CamBuffer_Type()
)
camBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camBuffer.setStatus("current")


class _CamApplyToAll_Type(Integer32):
    """Custom type camApplyToAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noChange", 0),
          ("applyToAll", 1))
    )


_CamApplyToAll_Type.__name__ = "Integer32"
_CamApplyToAll_Object = MibTableColumn
camApplyToAll = _CamApplyToAll_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 3, 1, 50),
    _CamApplyToAll_Type()
)
camApplyToAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camApplyToAll.setStatus("current")
_CamScheduleTable_Object = MibTable
camScheduleTable = _CamScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 4)
)
if mibBuilder.loadTexts:
    camScheduleTable.setStatus("current")
_CamScheduleEntry_Object = MibTableRow
camScheduleEntry = _CamScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 4, 1)
)
camScheduleEntry.setIndexNames(
    (0, "H555-MIB", "camIndex"),
    (0, "H555-MIB", "camScheduleIndex"),
)
if mibBuilder.loadTexts:
    camScheduleEntry.setStatus("current")
_CamScheduleCameraName_Type = SnmpAdminString
_CamScheduleCameraName_Object = MibTableColumn
camScheduleCameraName = _CamScheduleCameraName_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 4, 1, 1),
    _CamScheduleCameraName_Type()
)
camScheduleCameraName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camScheduleCameraName.setStatus("current")


class _CamScheduleIndex_Type(Integer32):
    """Custom type camScheduleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CamScheduleIndex_Type.__name__ = "Integer32"
_CamScheduleIndex_Object = MibTableColumn
camScheduleIndex = _CamScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 4, 1, 2),
    _CamScheduleIndex_Type()
)
camScheduleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    camScheduleIndex.setStatus("current")


class _CamScheduleTimerType_Type(Integer32):
    """Custom type camScheduleTimerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oneTimeEvent", 0),
          ("weeklyEvent", 1))
    )


_CamScheduleTimerType_Type.__name__ = "Integer32"
_CamScheduleTimerType_Object = MibTableColumn
camScheduleTimerType = _CamScheduleTimerType_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 4, 1, 3),
    _CamScheduleTimerType_Type()
)
camScheduleTimerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camScheduleTimerType.setStatus("current")
_CamScheduleTime_Type = DisplayString
_CamScheduleTime_Object = MibTableColumn
camScheduleTime = _CamScheduleTime_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 4, 1, 4),
    _CamScheduleTime_Type()
)
camScheduleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camScheduleTime.setStatus("current")
_CamScheduleDate_Type = DisplayString
_CamScheduleDate_Object = MibTableColumn
camScheduleDate = _CamScheduleDate_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 4, 1, 5),
    _CamScheduleDate_Type()
)
camScheduleDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camScheduleDate.setStatus("current")
_CamScheduleDays_Type = DisplayString
_CamScheduleDays_Object = MibTableColumn
camScheduleDays = _CamScheduleDays_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 4, 1, 6),
    _CamScheduleDays_Type()
)
camScheduleDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camScheduleDays.setStatus("current")
_CamScheduleDuration_Type = Integer32
_CamScheduleDuration_Object = MibTableColumn
camScheduleDuration = _CamScheduleDuration_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 4, 1, 7),
    _CamScheduleDuration_Type()
)
camScheduleDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camScheduleDuration.setStatus("current")


class _CamScheduleVad_Type(Integer32):
    """Custom type camScheduleVad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vadDisabled", 0),
          ("vadEnabled", 1))
    )


_CamScheduleVad_Type.__name__ = "Integer32"
_CamScheduleVad_Object = MibTableColumn
camScheduleVad = _CamScheduleVad_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 4, 1, 8),
    _CamScheduleVad_Type()
)
camScheduleVad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camScheduleVad.setStatus("current")


class _CamScheduleVadDuration_Type(Integer32):
    """Custom type camScheduleVadDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CamScheduleVadDuration_Type.__name__ = "Integer32"
_CamScheduleVadDuration_Object = MibTableColumn
camScheduleVadDuration = _CamScheduleVadDuration_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 4, 1, 9),
    _CamScheduleVadDuration_Type()
)
camScheduleVadDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camScheduleVadDuration.setStatus("current")


class _CamScheduleMad_Type(Integer32):
    """Custom type camScheduleMad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("madDisabled", 0),
          ("madEnabled", 1))
    )


_CamScheduleMad_Type.__name__ = "Integer32"
_CamScheduleMad_Object = MibTableColumn
camScheduleMad = _CamScheduleMad_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 4, 1, 10),
    _CamScheduleMad_Type()
)
camScheduleMad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camScheduleMad.setStatus("current")


class _CamScheduleMadDuration_Type(Integer32):
    """Custom type camScheduleMadDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CamScheduleMadDuration_Type.__name__ = "Integer32"
_CamScheduleMadDuration_Object = MibTableColumn
camScheduleMadDuration = _CamScheduleMadDuration_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 4, 1, 11),
    _CamScheduleMadDuration_Type()
)
camScheduleMadDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camScheduleMadDuration.setStatus("current")


class _CamScheduleId_Type(Integer32):
    """Custom type camScheduleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CamScheduleId_Type.__name__ = "Integer32"
_CamScheduleId_Object = MibTableColumn
camScheduleId = _CamScheduleId_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 4, 1, 12),
    _CamScheduleId_Type()
)
camScheduleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camScheduleId.setStatus("current")


class _CamScheduleSave_Type(Integer32):
    """Custom type camScheduleSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CamScheduleSave_Type.__name__ = "Integer32"
_CamScheduleSave_Object = MibTableColumn
camScheduleSave = _CamScheduleSave_Object(
    (1, 3, 6, 1, 4, 1, 45373, 1, 4, 1, 13),
    _CamScheduleSave_Type()
)
camScheduleSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    camScheduleSave.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H555-MIB",
    **{"H555IpAddrEntry": H555IpAddrEntry,
       "h555": h555,
       "device": device,
       "version": version,
       "timeSettings": timeSettings,
       "date": date,
       "time": time,
       "unixTime": unixTime,
       "unixTimeExt": unixTimeExt,
       "timezone": timezone,
       "ntpEnabled": ntpEnabled,
       "ntpServer": ntpServer,
       "ntpServerRestart": ntpServerRestart,
       "mediaStreamSettings": mediaStreamSettings,
       "maxport": maxport,
       "minport": minport,
       "filenameTemplate": filenameTemplate,
       "storage": storage,
       "freeSpace": freeSpace,
       "totalSpace": totalSpace,
       "usedSpace": usedSpace,
       "sensors": sensors,
       "cputemp": cputemp,
       "hddtemp": hddtemp,
       "netconfig": netconfig,
       "macAddress": macAddress,
       "dhcpClient": dhcpClient,
       "ipConfig": ipConfig,
       "routeTable": routeTable,
       "routeEntry": routeEntry,
       "routeIndex": routeIndex,
       "routeDestIp": routeDestIp,
       "routeDestNetMask": routeDestNetMask,
       "routeGateway": routeGateway,
       "logTable": logTable,
       "logEntry": logEntry,
       "logIndex": logIndex,
       "logTime": logTime,
       "logUser": logUser,
       "logHost": logHost,
       "logAction": logAction,
       "logResult": logResult,
       "logResultReason": logResultReason,
       "logDetails": logDetails,
       "snmpConf": snmpConf,
       "trapReceicer": trapReceicer,
       "h555Url": h555Url,
       "h555Login": h555Login,
       "h555Pass": h555Pass,
       "logLimit": logLimit,
       "snmpDebug": snmpDebug,
       "saveSnmpConf": saveSnmpConf,
       "camTable": camTable,
       "camEntry": camEntry,
       "camIndex": camIndex,
       "camName": camName,
       "camEnabled": camEnabled,
       "camRecord": camRecord,
       "camState": camState,
       "camStoreDuration": camStoreDuration,
       "camImportancy": camImportancy,
       "camSize": camSize,
       "camDuration": camDuration,
       "camHasSchedule": camHasSchedule,
       "camComment": camComment,
       "camAudio": camAudio,
       "camCompanding": camCompanding,
       "camAudiorate": camAudiorate,
       "camGain": camGain,
       "camMicVoltage": camMicVoltage,
       "camAcStartThreshold": camAcStartThreshold,
       "camVideo": camVideo,
       "camCodec": camCodec,
       "camFormat": camFormat,
       "camVideorate": camVideorate,
       "camQuality": camQuality,
       "camBitrate": camBitrate,
       "camVcStartThreshold": camVcStartThreshold,
       "camLowRes": camLowRes,
       "camBrightness": camBrightness,
       "camContrast": camContrast,
       "camGrayscale": camGrayscale,
       "camDeinterlace": camDeinterlace,
       "camAreaX": camAreaX,
       "camAreaY": camAreaY,
       "camAreaW": camAreaW,
       "camAreaH": camAreaH,
       "camVadEventCounter": camVadEventCounter,
       "camMadEventCounter": camMadEventCounter,
       "camBuffer": camBuffer,
       "camApplyToAll": camApplyToAll,
       "camScheduleTable": camScheduleTable,
       "camScheduleEntry": camScheduleEntry,
       "camScheduleCameraName": camScheduleCameraName,
       "camScheduleIndex": camScheduleIndex,
       "camScheduleTimerType": camScheduleTimerType,
       "camScheduleTime": camScheduleTime,
       "camScheduleDate": camScheduleDate,
       "camScheduleDays": camScheduleDays,
       "camScheduleDuration": camScheduleDuration,
       "camScheduleVad": camScheduleVad,
       "camScheduleVadDuration": camScheduleVadDuration,
       "camScheduleMad": camScheduleMad,
       "camScheduleMadDuration": camScheduleMadDuration,
       "camScheduleId": camScheduleId,
       "camScheduleSave": camScheduleSave}
)

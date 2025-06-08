# SNMP MIB module (CM-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/CM-SYSTEM-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:57 2025
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

(FileTransferProtocol,
 TrapCounter,
 fsp150cm) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "FileTransferProtocol",
    "TrapCounter",
    "fsp150cm")

(IpVersion,
 RestartType) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "IpVersion",
    "RestartType")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(lldpV2RemEntry,) = mibBuilder.importSymbols(
    "LLDP-V2-MIB",
    "lldpV2RemEntry")

(LldpV2DestAddressTableIndex,) = mibBuilder.importSymbols(
    "LLDP-V2-TC-MIB",
    "LldpV2DestAddressTableIndex")

(SnmpEngineID,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpEngineID")

(snmpTargetAddrName,) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "snmpTargetAddrName")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

cmSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2)
)
if mibBuilder.loadTexts:
    cmSystemMIB.setRevisions(
        ("2016-01-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CmAclFilterAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )



class CmAutoProvMode(TextualConvention, Integer32):
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
        *(("off", 1),
          ("confirm", 2),
          ("auto", 3))
    )



class CmNtpType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unicast", 1)
    )



class CmNtpMode(TextualConvention, Integer32):
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
        *(("client", 1),
          ("server", 2),
          ("both", 3))
    )



class CmNtpServerType(TextualConvention, Integer32):
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
        *(("not-applicable", 0),
          ("primary", 1),
          ("secondary", 2))
    )



class CmFileTransferMethod(TextualConvention, Integer32):
    status = "current"
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
        *(("ftp", 1),
          ("scp", 2),
          ("sftp", 3),
          ("web", 4))
    )



class CmVersionType(TextualConvention, Integer32):
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
        *(("active", 1),
          ("standby", 2),
          ("staging", 3))
    )



class CmFileServicesStatus(TextualConvention, Integer32):
    status = "current"
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("in-progress", 1),
          ("success", 2),
          ("login-failed", 3),
          ("file-not-found", 4),
          ("permission-denied", 5),
          ("server-unreachable", 6),
          ("no-space-left", 7),
          ("invalid-file-type", 8),
          ("nobackup-database", 9),
          ("no-sw-toinstall", 10),
          ("sw-not-installed", 11),
          ("validation-timer-notactive", 12),
          ("cannot-revert", 13),
          ("install-failed", 14),
          ("upgrade-failed", 15),
          ("revert-failed", 16),
          ("failure", 17),
          ("badarchive", 18),
          ("incompatarchive", 19),
          ("swVersionNotApproved", 20))
    )



class CmFileServicesMode(TextualConvention, Integer32):
    status = "current"
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
        *(("idle", 1),
          ("dbupload", 2),
          ("dbdownload", 3),
          ("dbbackup", 4),
          ("dbrestore", 5),
          ("swdownload", 6),
          ("swinstall", 7),
          ("swupgrade", 8),
          ("swvalidate", 9),
          ("swcancelupgrade", 10),
          ("swrevert", 11),
          ("rebooting", 12),
          ("debugfileupload", 13),
          ("securitylogfileupload", 14),
          ("alarmlogfileupload", 15),
          ("auditlogfileupload", 16),
          ("dbpropagate", 17),
          ("swpropagate", 18),
          ("sysdiagfileupload", 19),
          ("sysdiagfilesave", 20),
          ("configfileupload", 21),
          ("configfiledownload", 22),
          ("defaultvalsfiledownload", 23),
          ("satresultupload", 24))
    )



class CmRestartCauseType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("poweronreset", 1),
          ("userinitiated", 2),
          ("unreoverableappevent", 3),
          ("unrecoverablesysevent", 4),
          ("hwwatchdogexpired", 5),
          ("bustxntimeout", 6),
          ("hardware", 7))
    )



class F3ConfigFileAction(TextualConvention, Integer32):
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
        *(("none", 0),
          ("restart-with-file", 1),
          ("save-delta", 2),
          ("remove", 3),
          ("save-full", 4),
          ("load-config", 5))
    )



class F3ConfigFileStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("not-applicable", 0),
          ("initial", 1),
          ("in-progress", 2),
          ("completed", 3),
          ("failed", 4))
    )



class TimeOfDayType(TextualConvention, Integer32):
    status = "current"
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
        *(("local", 1),
          ("ntp", 2),
          ("ptp", 3),
          ("timeclock", 4))
    )



class LldpV2ConfigurationADVAExtMaxNeighborsAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete-entry", 1),
          ("discard-lldppdu", 2))
    )



class FileTransferServerType(TextualConvention, Integer32):
    status = "current"
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
        *(("ipaddr", 1),
          ("ipv6addr", 2),
          ("hostname", 3),
          ("url", 4))
    )



class ServerConfigType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("userdefined", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CmSystemObjects_ObjectIdentity = ObjectIdentity
cmSystemObjects = _CmSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1)
)
_CmErrorInfoObjects_ObjectIdentity = ObjectIdentity
cmErrorInfoObjects = _CmErrorInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 1)
)


class _LastSetErrorInformation_Type(DisplayString):
    """Custom type lastSetErrorInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LastSetErrorInformation_Type.__name__ = "DisplayString"
_LastSetErrorInformation_Object = MibScalar
lastSetErrorInformation = _LastSetErrorInformation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 1, 1),
    _LastSetErrorInformation_Type()
)
lastSetErrorInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastSetErrorInformation.setStatus("current")
_CmCliObjects_ObjectIdentity = ObjectIdentity
cmCliObjects = _CmCliObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 2)
)


class _CliCmdPromptPrefix_Type(DisplayString):
    """Custom type cliCmdPromptPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CliCmdPromptPrefix_Type.__name__ = "DisplayString"
_CliCmdPromptPrefix_Object = MibScalar
cliCmdPromptPrefix = _CliCmdPromptPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 2, 1),
    _CliCmdPromptPrefix_Type()
)
cliCmdPromptPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cliCmdPromptPrefix.setStatus("current")
_CmAccessProtocols_ObjectIdentity = ObjectIdentity
cmAccessProtocols = _CmAccessProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 3)
)
_TelnetEnabled_Type = TruthValue
_TelnetEnabled_Object = MibScalar
telnetEnabled = _TelnetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 3, 1),
    _TelnetEnabled_Type()
)
telnetEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetEnabled.setStatus("current")
_SshEnabled_Type = TruthValue
_SshEnabled_Object = MibScalar
sshEnabled = _SshEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 3, 2),
    _SshEnabled_Type()
)
sshEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshEnabled.setStatus("current")
_FtpEnabled_Type = TruthValue
_FtpEnabled_Object = MibScalar
ftpEnabled = _FtpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 3, 3),
    _FtpEnabled_Type()
)
ftpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpEnabled.setStatus("current")
_ScpEnabled_Type = TruthValue
_ScpEnabled_Object = MibScalar
scpEnabled = _ScpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 3, 4),
    _ScpEnabled_Type()
)
scpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scpEnabled.setStatus("current")
_SerialPortEnabled_Type = TruthValue
_SerialPortEnabled_Object = MibScalar
serialPortEnabled = _SerialPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 3, 5),
    _SerialPortEnabled_Type()
)
serialPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialPortEnabled.setStatus("current")
_HttpEnabled_Type = TruthValue
_HttpEnabled_Object = MibScalar
httpEnabled = _HttpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 3, 6),
    _HttpEnabled_Type()
)
httpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpEnabled.setStatus("current")
_HttpsEnabled_Type = TruthValue
_HttpsEnabled_Object = MibScalar
httpsEnabled = _HttpsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 3, 7),
    _HttpsEnabled_Type()
)
httpsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpsEnabled.setStatus("current")
_SftpEnabled_Type = TruthValue
_SftpEnabled_Object = MibScalar
sftpEnabled = _SftpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 3, 8),
    _SftpEnabled_Type()
)
sftpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sftpEnabled.setStatus("current")
_TftpEnabled_Type = TruthValue
_TftpEnabled_Object = MibScalar
tftpEnabled = _TftpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 3, 9),
    _TftpEnabled_Type()
)
tftpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpEnabled.setStatus("current")
_CmSysSecObjects_ObjectIdentity = ObjectIdentity
cmSysSecObjects = _CmSysSecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 4)
)


class _SecurityBanner_Type(DisplayString):
    """Custom type securityBanner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2000),
    )


_SecurityBanner_Type.__name__ = "DisplayString"
_SecurityBanner_Object = MibScalar
securityBanner = _SecurityBanner_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 4, 1),
    _SecurityBanner_Type()
)
securityBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityBanner.setStatus("current")
_AclTable_Object = MibTable
aclTable = _AclTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    aclTable.setStatus("current")
_AclEntry_Object = MibTableRow
aclEntry = _AclEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 4, 2, 1)
)
aclEntry.setIndexNames(
    (0, "CM-SYSTEM-MIB", "aclEntryIndex"),
)
if mibBuilder.loadTexts:
    aclEntry.setStatus("current")


class _AclEntryIndex_Type(Integer32):
    """Custom type aclEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AclEntryIndex_Type.__name__ = "Integer32"
_AclEntryIndex_Object = MibTableColumn
aclEntryIndex = _AclEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 4, 2, 1, 1),
    _AclEntryIndex_Type()
)
aclEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclEntryIndex.setStatus("current")
_AclEntryFilterAction_Type = CmAclFilterAction
_AclEntryFilterAction_Object = MibTableColumn
aclEntryFilterAction = _AclEntryFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 4, 2, 1, 2),
    _AclEntryFilterAction_Type()
)
aclEntryFilterAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclEntryFilterAction.setStatus("current")
_AclEntryNetworkAddress_Type = IpAddress
_AclEntryNetworkAddress_Object = MibTableColumn
aclEntryNetworkAddress = _AclEntryNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 4, 2, 1, 3),
    _AclEntryNetworkAddress_Type()
)
aclEntryNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclEntryNetworkAddress.setStatus("current")
_AclEntryNetworkMask_Type = IpAddress
_AclEntryNetworkMask_Object = MibTableColumn
aclEntryNetworkMask = _AclEntryNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 4, 2, 1, 4),
    _AclEntryNetworkMask_Type()
)
aclEntryNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclEntryNetworkMask.setStatus("current")
_AclEntryEnabled_Type = TruthValue
_AclEntryEnabled_Object = MibTableColumn
aclEntryEnabled = _AclEntryEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 4, 2, 1, 5),
    _AclEntryEnabled_Type()
)
aclEntryEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclEntryEnabled.setStatus("current")
_AclEntryIpVersion_Type = IpVersion
_AclEntryIpVersion_Object = MibTableColumn
aclEntryIpVersion = _AclEntryIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 4, 2, 1, 6),
    _AclEntryIpVersion_Type()
)
aclEntryIpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclEntryIpVersion.setStatus("current")
_AclEntryNetworkIpv6Addr_Type = Ipv6Address
_AclEntryNetworkIpv6Addr_Object = MibTableColumn
aclEntryNetworkIpv6Addr = _AclEntryNetworkIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 4, 2, 1, 7),
    _AclEntryNetworkIpv6Addr_Type()
)
aclEntryNetworkIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclEntryNetworkIpv6Addr.setStatus("current")


class _AclEntryPrefixLength_Type(Integer32):
    """Custom type aclEntryPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AclEntryPrefixLength_Type.__name__ = "Integer32"
_AclEntryPrefixLength_Object = MibTableColumn
aclEntryPrefixLength = _AclEntryPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 4, 2, 1, 8),
    _AclEntryPrefixLength_Type()
)
aclEntryPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclEntryPrefixLength.setStatus("current")
_SerialPortDisconnectAutoLogOff_Type = TruthValue
_SerialPortDisconnectAutoLogOff_Object = MibScalar
serialPortDisconnectAutoLogOff = _SerialPortDisconnectAutoLogOff_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 4, 3),
    _SerialPortDisconnectAutoLogOff_Type()
)
serialPortDisconnectAutoLogOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialPortDisconnectAutoLogOff.setStatus("current")
_SecurityPromptEnabled_Type = TruthValue
_SecurityPromptEnabled_Object = MibScalar
securityPromptEnabled = _SecurityPromptEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 4, 4),
    _SecurityPromptEnabled_Type()
)
securityPromptEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityPromptEnabled.setStatus("current")
_CmSysModeObjects_ObjectIdentity = ObjectIdentity
cmSysModeObjects = _CmSysModeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 5)
)
_NtpMode_Type = CmNtpMode
_NtpMode_Object = MibScalar
ntpMode = _NtpMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 5, 1),
    _NtpMode_Type()
)
ntpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpMode.setStatus("current")


class _AutoProvMode_Type(Integer32):
    """Custom type autoProvMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("confirm", 2),
          ("auto", 3))
    )


_AutoProvMode_Type.__name__ = "Integer32"
_AutoProvMode_Object = MibScalar
autoProvMode = _AutoProvMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 5, 2),
    _AutoProvMode_Type()
)
autoProvMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoProvMode.setStatus("current")
_SysTimeOfDayType_Type = TimeOfDayType
_SysTimeOfDayType_Object = MibScalar
sysTimeOfDayType = _SysTimeOfDayType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 5, 3),
    _SysTimeOfDayType_Type()
)
sysTimeOfDayType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeOfDayType.setStatus("current")
_NtpServerConfigType_Type = ServerConfigType
_NtpServerConfigType_Object = MibScalar
ntpServerConfigType = _NtpServerConfigType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 5, 4),
    _NtpServerConfigType_Type()
)
ntpServerConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServerConfigType.setStatus("current")
_SysLogServerConfigType_Type = ServerConfigType
_SysLogServerConfigType_Object = MibScalar
sysLogServerConfigType = _SysLogServerConfigType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 5, 5),
    _SysLogServerConfigType_Type()
)
sysLogServerConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogServerConfigType.setStatus("current")
_SysUseUtcLeapOffsetEnable_Type = TruthValue
_SysUseUtcLeapOffsetEnable_Object = MibScalar
sysUseUtcLeapOffsetEnable = _SysUseUtcLeapOffsetEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 5, 6),
    _SysUseUtcLeapOffsetEnable_Type()
)
sysUseUtcLeapOffsetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysUseUtcLeapOffsetEnable.setStatus("current")
_CmDatabaseObjects_ObjectIdentity = ObjectIdentity
cmDatabaseObjects = _CmDatabaseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 6)
)


class _DatabaseAction_Type(Integer32):
    """Custom type databaseAction based on Integer32"""
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
        *(("not-applicable", 0),
          ("backup", 1),
          ("restore", 2),
          ("activate", 3),
          ("save-sysdefaults", 4),
          ("new-sysdefaults", 5),
          ("restore-sysdefaults", 6),
          ("restore-factorydefaults", 7),
          ("propagate-to-standby-nemi", 8),
          ("force-normal", 9))
    )


_DatabaseAction_Type.__name__ = "Integer32"
_DatabaseAction_Object = MibScalar
databaseAction = _DatabaseAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 6, 1),
    _DatabaseAction_Type()
)
databaseAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseAction.setStatus("current")
_DatabaseLastSaveTime_Type = DateAndTime
_DatabaseLastSaveTime_Object = MibScalar
databaseLastSaveTime = _DatabaseLastSaveTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 6, 2),
    _DatabaseLastSaveTime_Type()
)
databaseLastSaveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseLastSaveTime.setStatus("current")
_DatabaseTable_Object = MibTable
databaseTable = _DatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 6, 3)
)
if mibBuilder.loadTexts:
    databaseTable.setStatus("current")
_DatabaseEntry_Object = MibTableRow
databaseEntry = _DatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 6, 3, 1)
)
databaseEntry.setIndexNames(
    (0, "CM-SYSTEM-MIB", "databaseIndex"),
)
if mibBuilder.loadTexts:
    databaseEntry.setStatus("current")


class _DatabaseIndex_Type(Integer32):
    """Custom type databaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DatabaseIndex_Type.__name__ = "Integer32"
_DatabaseIndex_Object = MibTableColumn
databaseIndex = _DatabaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 6, 3, 1, 1),
    _DatabaseIndex_Type()
)
databaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseIndex.setStatus("current")
_DatabaseType_Type = CmVersionType
_DatabaseType_Object = MibTableColumn
databaseType = _DatabaseType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 6, 3, 1, 2),
    _DatabaseType_Type()
)
databaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseType.setStatus("current")


class _DatabaseVersion_Type(DisplayString):
    """Custom type databaseVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DatabaseVersion_Type.__name__ = "DisplayString"
_DatabaseVersion_Object = MibTableColumn
databaseVersion = _DatabaseVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 6, 3, 1, 3),
    _DatabaseVersion_Type()
)
databaseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseVersion.setStatus("current")
_CmSoftwareObjects_ObjectIdentity = ObjectIdentity
cmSoftwareObjects = _CmSoftwareObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 7)
)


class _SoftwareAction_Type(Integer32):
    """Custom type softwareAction based on Integer32"""
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
        *(("not-applicable", 0),
          ("install", 1),
          ("schedule-upgrade", 2),
          ("cancel-upgrade", 3),
          ("validate-upgrade", 4),
          ("revert-upgrade", 5),
          ("propagate-to-standby-nemi", 6))
    )


_SoftwareAction_Type.__name__ = "Integer32"
_SoftwareAction_Object = MibScalar
softwareAction = _SoftwareAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 7, 1),
    _SoftwareAction_Type()
)
softwareAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareAction.setStatus("current")
_SoftwareUpgradeTime_Type = DateAndTime
_SoftwareUpgradeTime_Object = MibScalar
softwareUpgradeTime = _SoftwareUpgradeTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 7, 2),
    _SoftwareUpgradeTime_Type()
)
softwareUpgradeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareUpgradeTime.setStatus("current")


class _SoftwareValidationTimer_Type(Integer32):
    """Custom type softwareValidationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 720),
    )


_SoftwareValidationTimer_Type.__name__ = "Integer32"
_SoftwareValidationTimer_Object = MibScalar
softwareValidationTimer = _SoftwareValidationTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 7, 3),
    _SoftwareValidationTimer_Type()
)
softwareValidationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareValidationTimer.setStatus("current")
_SoftwareTable_Object = MibTable
softwareTable = _SoftwareTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 7, 4)
)
if mibBuilder.loadTexts:
    softwareTable.setStatus("current")
_SoftwareEntry_Object = MibTableRow
softwareEntry = _SoftwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 7, 4, 1)
)
softwareEntry.setIndexNames(
    (0, "CM-SYSTEM-MIB", "softwareIndex"),
)
if mibBuilder.loadTexts:
    softwareEntry.setStatus("current")


class _SoftwareIndex_Type(Integer32):
    """Custom type softwareIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SoftwareIndex_Type.__name__ = "Integer32"
_SoftwareIndex_Object = MibTableColumn
softwareIndex = _SoftwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 7, 4, 1, 1),
    _SoftwareIndex_Type()
)
softwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareIndex.setStatus("current")
_SoftwareType_Type = CmVersionType
_SoftwareType_Object = MibTableColumn
softwareType = _SoftwareType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 7, 4, 1, 2),
    _SoftwareType_Type()
)
softwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareType.setStatus("current")


class _SoftwareVersion_Type(DisplayString):
    """Custom type softwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SoftwareVersion_Type.__name__ = "DisplayString"
_SoftwareVersion_Object = MibTableColumn
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 7, 4, 1, 3),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("current")
_CmFileServicesObjects_ObjectIdentity = ObjectIdentity
cmFileServicesObjects = _CmFileServicesObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 8)
)


class _FileServicesAction_Type(Integer32):
    """Custom type fileServicesAction based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("get-database", 1),
          ("put-database", 2),
          ("software-copy", 3),
          ("get-sys-database", 4),
          ("put-sys-database", 5),
          ("get-defaultsvalue-file", 6),
          ("put-sysresetdebuginfo-file", 7),
          ("put-securitylog-file", 8),
          ("put-alarmlog-file", 9),
          ("put-auditlog-file", 10),
          ("get-config-file", 11),
          ("put-config-file", 12),
          ("put-sat-result", 13))
    )


_FileServicesAction_Type.__name__ = "Integer32"
_FileServicesAction_Object = MibScalar
fileServicesAction = _FileServicesAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 8, 1),
    _FileServicesAction_Type()
)
fileServicesAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileServicesAction.setStatus("current")
_FileServicesMethod_Type = CmFileTransferMethod
_FileServicesMethod_Object = MibScalar
fileServicesMethod = _FileServicesMethod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 8, 2),
    _FileServicesMethod_Type()
)
fileServicesMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileServicesMethod.setStatus("current")
_FileServicesServerIp_Type = IpAddress
_FileServicesServerIp_Object = MibScalar
fileServicesServerIp = _FileServicesServerIp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 8, 3),
    _FileServicesServerIp_Type()
)
fileServicesServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileServicesServerIp.setStatus("current")


class _FileServicesUserId_Type(DisplayString):
    """Custom type fileServicesUserId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FileServicesUserId_Type.__name__ = "DisplayString"
_FileServicesUserId_Object = MibScalar
fileServicesUserId = _FileServicesUserId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 8, 4),
    _FileServicesUserId_Type()
)
fileServicesUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileServicesUserId.setStatus("current")


class _FileServicesPassword_Type(DisplayString):
    """Custom type fileServicesPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FileServicesPassword_Type.__name__ = "DisplayString"
_FileServicesPassword_Object = MibScalar
fileServicesPassword = _FileServicesPassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 8, 5),
    _FileServicesPassword_Type()
)
fileServicesPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileServicesPassword.setStatus("current")


class _FileServicesRemoteFile_Type(DisplayString):
    """Custom type fileServicesRemoteFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FileServicesRemoteFile_Type.__name__ = "DisplayString"
_FileServicesRemoteFile_Object = MibScalar
fileServicesRemoteFile = _FileServicesRemoteFile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 8, 6),
    _FileServicesRemoteFile_Type()
)
fileServicesRemoteFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileServicesRemoteFile.setStatus("current")
_FileServicesStatus_Type = CmFileServicesStatus
_FileServicesStatus_Object = MibScalar
fileServicesStatus = _FileServicesStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 8, 7),
    _FileServicesStatus_Type()
)
fileServicesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileServicesStatus.setStatus("current")


class _FileServicesPercentComplete_Type(Integer32):
    """Custom type fileServicesPercentComplete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FileServicesPercentComplete_Type.__name__ = "Integer32"
_FileServicesPercentComplete_Object = MibScalar
fileServicesPercentComplete = _FileServicesPercentComplete_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 8, 8),
    _FileServicesPercentComplete_Type()
)
fileServicesPercentComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileServicesPercentComplete.setStatus("current")
_FileServicesMode_Type = CmFileServicesMode
_FileServicesMode_Object = MibScalar
fileServicesMode = _FileServicesMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 8, 9),
    _FileServicesMode_Type()
)
fileServicesMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileServicesMode.setStatus("current")
_FileServicesServerType_Type = FileTransferServerType
_FileServicesServerType_Object = MibScalar
fileServicesServerType = _FileServicesServerType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 8, 10),
    _FileServicesServerType_Type()
)
fileServicesServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileServicesServerType.setStatus("current")
_FileServicesServerIpv6Addr_Type = Ipv6Address
_FileServicesServerIpv6Addr_Object = MibScalar
fileServicesServerIpv6Addr = _FileServicesServerIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 8, 11),
    _FileServicesServerIpv6Addr_Type()
)
fileServicesServerIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileServicesServerIpv6Addr.setStatus("current")
_CmLogObjects_ObjectIdentity = ObjectIdentity
cmLogObjects = _CmLogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 9)
)
_CmSysLogObjects_ObjectIdentity = ObjectIdentity
cmSysLogObjects = _CmSysLogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 9, 1)
)
_SysLogServerTable_Object = MibTable
sysLogServerTable = _SysLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    sysLogServerTable.setStatus("current")
_SysLogServerEntry_Object = MibTableRow
sysLogServerEntry = _SysLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 9, 1, 1, 1)
)
sysLogServerEntry.setIndexNames(
    (0, "CM-SYSTEM-MIB", "sysLogServerIndex"),
)
if mibBuilder.loadTexts:
    sysLogServerEntry.setStatus("current")


class _SysLogServerIndex_Type(Integer32):
    """Custom type sysLogServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SysLogServerIndex_Type.__name__ = "Integer32"
_SysLogServerIndex_Object = MibTableColumn
sysLogServerIndex = _SysLogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 9, 1, 1, 1, 1),
    _SysLogServerIndex_Type()
)
sysLogServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLogServerIndex.setStatus("current")
_SysLogIpAddress_Type = IpAddress
_SysLogIpAddress_Object = MibTableColumn
sysLogIpAddress = _SysLogIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 9, 1, 1, 1, 2),
    _SysLogIpAddress_Type()
)
sysLogIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogIpAddress.setStatus("current")


class _SysLogPort_Type(Integer32):
    """Custom type sysLogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysLogPort_Type.__name__ = "Integer32"
_SysLogPort_Object = MibTableColumn
sysLogPort = _SysLogPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 9, 1, 1, 1, 3),
    _SysLogPort_Type()
)
sysLogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogPort.setStatus("current")
_SysLogIpVersion_Type = IpVersion
_SysLogIpVersion_Object = MibTableColumn
sysLogIpVersion = _SysLogIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 9, 1, 1, 1, 4),
    _SysLogIpVersion_Type()
)
sysLogIpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogIpVersion.setStatus("current")
_SysLogIpv6Addr_Type = Ipv6Address
_SysLogIpv6Addr_Object = MibTableColumn
sysLogIpv6Addr = _SysLogIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 9, 1, 1, 1, 5),
    _SysLogIpv6Addr_Type()
)
sysLogIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogIpv6Addr.setStatus("current")
_CmSecLogObjects_ObjectIdentity = ObjectIdentity
cmSecLogObjects = _CmSecLogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 9, 2)
)
_SecLog2sysLogEnabled_Type = TruthValue
_SecLog2sysLogEnabled_Object = MibScalar
secLog2sysLogEnabled = _SecLog2sysLogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 9, 2, 1),
    _SecLog2sysLogEnabled_Type()
)
secLog2sysLogEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secLog2sysLogEnabled.setStatus("current")
_CmAuditLogObjects_ObjectIdentity = ObjectIdentity
cmAuditLogObjects = _CmAuditLogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 9, 3)
)
_AuditLog2sysLogEnabled_Type = TruthValue
_AuditLog2sysLogEnabled_Object = MibScalar
auditLog2sysLogEnabled = _AuditLog2sysLogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 9, 3, 1),
    _AuditLog2sysLogEnabled_Type()
)
auditLog2sysLogEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLog2sysLogEnabled.setStatus("current")
_AuditLog2fileEnabled_Type = TruthValue
_AuditLog2fileEnabled_Object = MibScalar
auditLog2fileEnabled = _AuditLog2fileEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 9, 3, 2),
    _AuditLog2fileEnabled_Type()
)
auditLog2fileEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLog2fileEnabled.setStatus("current")
_CmAlarmLogObjects_ObjectIdentity = ObjectIdentity
cmAlarmLogObjects = _CmAlarmLogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 9, 4)
)
_AlarmLog2sysLogEnabled_Type = TruthValue
_AlarmLog2sysLogEnabled_Object = MibScalar
alarmLog2sysLogEnabled = _AlarmLog2sysLogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 9, 4, 1),
    _AlarmLog2sysLogEnabled_Type()
)
alarmLog2sysLogEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLog2sysLogEnabled.setStatus("current")
_AlarmLog2fileEnabled_Type = TruthValue
_AlarmLog2fileEnabled_Object = MibScalar
alarmLog2fileEnabled = _AlarmLog2fileEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 9, 4, 2),
    _AlarmLog2fileEnabled_Type()
)
alarmLog2fileEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLog2fileEnabled.setStatus("current")
_CmTimeObjects_ObjectIdentity = ObjectIdentity
cmTimeObjects = _CmTimeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 10)
)
_NtpClientEnabled_Type = TruthValue
_NtpClientEnabled_Object = MibScalar
ntpClientEnabled = _NtpClientEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 10, 1),
    _NtpClientEnabled_Type()
)
ntpClientEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpClientEnabled.setStatus("current")
_NtpPrimaryServer_Type = IpAddress
_NtpPrimaryServer_Object = MibScalar
ntpPrimaryServer = _NtpPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 10, 2),
    _NtpPrimaryServer_Type()
)
ntpPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpPrimaryServer.setStatus("current")
_NtpBackupServer_Type = IpAddress
_NtpBackupServer_Object = MibScalar
ntpBackupServer = _NtpBackupServer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 10, 3),
    _NtpBackupServer_Type()
)
ntpBackupServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpBackupServer.setStatus("current")
_NtpType_Type = CmNtpType
_NtpType_Object = MibScalar
ntpType = _NtpType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 10, 4),
    _NtpType_Type()
)
ntpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpType.setStatus("current")
_NtpActiveServer_Type = CmNtpServerType
_NtpActiveServer_Object = MibScalar
ntpActiveServer = _NtpActiveServer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 10, 5),
    _NtpActiveServer_Type()
)
ntpActiveServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpActiveServer.setStatus("current")
_NtpSwitchServer_Type = CmNtpServerType
_NtpSwitchServer_Object = MibScalar
ntpSwitchServer = _NtpSwitchServer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 10, 6),
    _NtpSwitchServer_Type()
)
ntpSwitchServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpSwitchServer.setStatus("current")
_NtpServerRoundTripDelay_Type = Integer32
_NtpServerRoundTripDelay_Object = MibScalar
ntpServerRoundTripDelay = _NtpServerRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 10, 7),
    _NtpServerRoundTripDelay_Type()
)
ntpServerRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpServerRoundTripDelay.setStatus("current")
_NtpServerPrecision_Type = Integer32
_NtpServerPrecision_Object = MibScalar
ntpServerPrecision = _NtpServerPrecision_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 10, 8),
    _NtpServerPrecision_Type()
)
ntpServerPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpServerPrecision.setStatus("current")
_NtpPollingInterval_Type = Integer32
_NtpPollingInterval_Object = MibScalar
ntpPollingInterval = _NtpPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 10, 9),
    _NtpPollingInterval_Type()
)
ntpPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpPollingInterval.setStatus("current")
_NtpPrimaryServerIpVersion_Type = IpVersion
_NtpPrimaryServerIpVersion_Object = MibScalar
ntpPrimaryServerIpVersion = _NtpPrimaryServerIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 10, 10),
    _NtpPrimaryServerIpVersion_Type()
)
ntpPrimaryServerIpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpPrimaryServerIpVersion.setStatus("current")
_NtpPrimaryServerIpv6Addr_Type = Ipv6Address
_NtpPrimaryServerIpv6Addr_Object = MibScalar
ntpPrimaryServerIpv6Addr = _NtpPrimaryServerIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 10, 11),
    _NtpPrimaryServerIpv6Addr_Type()
)
ntpPrimaryServerIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpPrimaryServerIpv6Addr.setStatus("current")
_NtpBackupServerIpVersion_Type = IpVersion
_NtpBackupServerIpVersion_Object = MibScalar
ntpBackupServerIpVersion = _NtpBackupServerIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 10, 12),
    _NtpBackupServerIpVersion_Type()
)
ntpBackupServerIpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpBackupServerIpVersion.setStatus("current")
_NtpBackupServerIpv6Addr_Type = Ipv6Address
_NtpBackupServerIpv6Addr_Object = MibScalar
ntpBackupServerIpv6Addr = _NtpBackupServerIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 10, 13),
    _NtpBackupServerIpv6Addr_Type()
)
ntpBackupServerIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpBackupServerIpv6Addr.setStatus("current")
_CmSnmpObjects_ObjectIdentity = ObjectIdentity
cmSnmpObjects = _CmSnmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 11)
)
_F3SnmpTargetAddrExtTable_Object = MibTable
f3SnmpTargetAddrExtTable = _F3SnmpTargetAddrExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    f3SnmpTargetAddrExtTable.setStatus("current")
_F3SnmpTargetAddrExtEntry_Object = MibTableRow
f3SnmpTargetAddrExtEntry = _F3SnmpTargetAddrExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 11, 1, 1)
)
f3SnmpTargetAddrExtEntry.setIndexNames(
    (1, "SNMP-TARGET-MIB", "snmpTargetAddrName"),
)
if mibBuilder.loadTexts:
    f3SnmpTargetAddrExtEntry.setStatus("current")
_F3SnmpTargetAddrExtDyingGaspPort_Type = VariablePointer
_F3SnmpTargetAddrExtDyingGaspPort_Object = MibTableColumn
f3SnmpTargetAddrExtDyingGaspPort = _F3SnmpTargetAddrExtDyingGaspPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 11, 1, 1, 1),
    _F3SnmpTargetAddrExtDyingGaspPort_Type()
)
f3SnmpTargetAddrExtDyingGaspPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SnmpTargetAddrExtDyingGaspPort.setStatus("current")
_F3SnmpTargetAddrExtDyingGaspEnabled_Type = TruthValue
_F3SnmpTargetAddrExtDyingGaspEnabled_Object = MibTableColumn
f3SnmpTargetAddrExtDyingGaspEnabled = _F3SnmpTargetAddrExtDyingGaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 11, 1, 1, 2),
    _F3SnmpTargetAddrExtDyingGaspEnabled_Type()
)
f3SnmpTargetAddrExtDyingGaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SnmpTargetAddrExtDyingGaspEnabled.setStatus("current")
_F3SnmpTargetAddrExtDyingGaspActive_Type = TruthValue
_F3SnmpTargetAddrExtDyingGaspActive_Object = MibTableColumn
f3SnmpTargetAddrExtDyingGaspActive = _F3SnmpTargetAddrExtDyingGaspActive_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 11, 1, 1, 3),
    _F3SnmpTargetAddrExtDyingGaspActive_Type()
)
f3SnmpTargetAddrExtDyingGaspActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SnmpTargetAddrExtDyingGaspActive.setStatus("current")
_F3SnmpTargetAddrExtBulkTrapsEnabled_Type = TruthValue
_F3SnmpTargetAddrExtBulkTrapsEnabled_Object = MibTableColumn
f3SnmpTargetAddrExtBulkTrapsEnabled = _F3SnmpTargetAddrExtBulkTrapsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 11, 1, 1, 4),
    _F3SnmpTargetAddrExtBulkTrapsEnabled_Type()
)
f3SnmpTargetAddrExtBulkTrapsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SnmpTargetAddrExtBulkTrapsEnabled.setStatus("current")
_F3SnmpEngineID_Type = SnmpEngineID
_F3SnmpEngineID_Object = MibScalar
f3SnmpEngineID = _F3SnmpEngineID_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 11, 2),
    _F3SnmpEngineID_Type()
)
f3SnmpEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SnmpEngineID.setStatus("current")
_F3SnmpLongIfAlias_Type = TruthValue
_F3SnmpLongIfAlias_Object = MibScalar
f3SnmpLongIfAlias = _F3SnmpLongIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 11, 3),
    _F3SnmpLongIfAlias_Type()
)
f3SnmpLongIfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SnmpLongIfAlias.setStatus("current")
_CmResetCauseObjects_ObjectIdentity = ObjectIdentity
cmResetCauseObjects = _CmResetCauseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 12)
)
_F3SysLastResetType_Type = RestartType
_F3SysLastResetType_Object = MibScalar
f3SysLastResetType = _F3SysLastResetType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 12, 1),
    _F3SysLastResetType_Type()
)
f3SysLastResetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SysLastResetType.setStatus("current")
_F3SysLastResetCauseType_Type = CmRestartCauseType
_F3SysLastResetCauseType_Object = MibScalar
f3SysLastResetCauseType = _F3SysLastResetCauseType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 12, 2),
    _F3SysLastResetCauseType_Type()
)
f3SysLastResetCauseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SysLastResetCauseType.setStatus("current")
_F3SysLastAbnormalResetTimestamp1_Type = DateAndTime
_F3SysLastAbnormalResetTimestamp1_Object = MibScalar
f3SysLastAbnormalResetTimestamp1 = _F3SysLastAbnormalResetTimestamp1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 12, 3),
    _F3SysLastAbnormalResetTimestamp1_Type()
)
f3SysLastAbnormalResetTimestamp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SysLastAbnormalResetTimestamp1.setStatus("current")
_F3SysLastAbnormalResetTimestamp2_Type = DateAndTime
_F3SysLastAbnormalResetTimestamp2_Object = MibScalar
f3SysLastAbnormalResetTimestamp2 = _F3SysLastAbnormalResetTimestamp2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 12, 4),
    _F3SysLastAbnormalResetTimestamp2_Type()
)
f3SysLastAbnormalResetTimestamp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SysLastAbnormalResetTimestamp2.setStatus("current")
_F3SysLastAbnormalResetTimestamp3_Type = DateAndTime
_F3SysLastAbnormalResetTimestamp3_Object = MibScalar
f3SysLastAbnormalResetTimestamp3 = _F3SysLastAbnormalResetTimestamp3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 12, 5),
    _F3SysLastAbnormalResetTimestamp3_Type()
)
f3SysLastAbnormalResetTimestamp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SysLastAbnormalResetTimestamp3.setStatus("current")
_F3NotifObjects_ObjectIdentity = ObjectIdentity
f3NotifObjects = _F3NotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 13)
)
_F3DatabaseSyncTrapObject_Type = VariablePointer
_F3DatabaseSyncTrapObject_Object = MibScalar
f3DatabaseSyncTrapObject = _F3DatabaseSyncTrapObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 13, 1),
    _F3DatabaseSyncTrapObject_Type()
)
f3DatabaseSyncTrapObject.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3DatabaseSyncTrapObject.setStatus("current")
_F3ConfigFileObjects_ObjectIdentity = ObjectIdentity
f3ConfigFileObjects = _F3ConfigFileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 14)
)


class _F3ConfigFileActionFileName_Type(DisplayString):
    """Custom type f3ConfigFileActionFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3ConfigFileActionFileName_Type.__name__ = "DisplayString"
_F3ConfigFileActionFileName_Object = MibScalar
f3ConfigFileActionFileName = _F3ConfigFileActionFileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 14, 1),
    _F3ConfigFileActionFileName_Type()
)
f3ConfigFileActionFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConfigFileActionFileName.setStatus("current")
_F3ConfigFileAction_Type = F3ConfigFileAction
_F3ConfigFileAction_Object = MibScalar
f3ConfigFileAction = _F3ConfigFileAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 14, 2),
    _F3ConfigFileAction_Type()
)
f3ConfigFileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConfigFileAction.setStatus("current")
_F3ConfigFileStatus_Type = F3ConfigFileStatus
_F3ConfigFileStatus_Object = MibScalar
f3ConfigFileStatus = _F3ConfigFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 14, 3),
    _F3ConfigFileStatus_Type()
)
f3ConfigFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConfigFileStatus.setStatus("current")


class _F3ConfigFileErrorInformation_Type(DisplayString):
    """Custom type f3ConfigFileErrorInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_F3ConfigFileErrorInformation_Type.__name__ = "DisplayString"
_F3ConfigFileErrorInformation_Object = MibScalar
f3ConfigFileErrorInformation = _F3ConfigFileErrorInformation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 14, 4),
    _F3ConfigFileErrorInformation_Type()
)
f3ConfigFileErrorInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConfigFileErrorInformation.setStatus("current")
_F3ConfigFileTable_Object = MibTable
f3ConfigFileTable = _F3ConfigFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 14, 5)
)
if mibBuilder.loadTexts:
    f3ConfigFileTable.setStatus("current")
_F3ConfigFileEntry_Object = MibTableRow
f3ConfigFileEntry = _F3ConfigFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 14, 5, 1)
)
f3ConfigFileEntry.setIndexNames(
    (0, "CM-SYSTEM-MIB", "f3ConfigFileIndex"),
)
if mibBuilder.loadTexts:
    f3ConfigFileEntry.setStatus("current")
_F3ConfigFileIndex_Type = Integer32
_F3ConfigFileIndex_Object = MibTableColumn
f3ConfigFileIndex = _F3ConfigFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 14, 5, 1, 1),
    _F3ConfigFileIndex_Type()
)
f3ConfigFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3ConfigFileIndex.setStatus("current")


class _F3ConfigFileName_Type(DisplayString):
    """Custom type f3ConfigFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_F3ConfigFileName_Type.__name__ = "DisplayString"
_F3ConfigFileName_Object = MibTableColumn
f3ConfigFileName = _F3ConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 14, 5, 1, 2),
    _F3ConfigFileName_Type()
)
f3ConfigFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConfigFileName.setStatus("current")


class _F3ConfigFileDescription_Type(DisplayString):
    """Custom type f3ConfigFileDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3ConfigFileDescription_Type.__name__ = "DisplayString"
_F3ConfigFileDescription_Object = MibTableColumn
f3ConfigFileDescription = _F3ConfigFileDescription_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 14, 5, 1, 3),
    _F3ConfigFileDescription_Type()
)
f3ConfigFileDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConfigFileDescription.setStatus("current")


class _F3ConfigFilePercentComplete_Type(Integer32):
    """Custom type f3ConfigFilePercentComplete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_F3ConfigFilePercentComplete_Type.__name__ = "Integer32"
_F3ConfigFilePercentComplete_Object = MibScalar
f3ConfigFilePercentComplete = _F3ConfigFilePercentComplete_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 14, 6),
    _F3ConfigFilePercentComplete_Type()
)
f3ConfigFilePercentComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConfigFilePercentComplete.setStatus("current")
_CmFeatureManagementObjects_ObjectIdentity = ObjectIdentity
cmFeatureManagementObjects = _CmFeatureManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 15)
)
_F3SystemFeatureTable_Object = MibTable
f3SystemFeatureTable = _F3SystemFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 15, 1)
)
if mibBuilder.loadTexts:
    f3SystemFeatureTable.setStatus("current")
_F3SystemFeatureEntry_Object = MibTableRow
f3SystemFeatureEntry = _F3SystemFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 15, 1, 1)
)
f3SystemFeatureEntry.setIndexNames(
    (0, "CM-SYSTEM-MIB", "f3SystemFeatureIndex"),
)
if mibBuilder.loadTexts:
    f3SystemFeatureEntry.setStatus("current")
_F3SystemFeatureIndex_Type = Integer32
_F3SystemFeatureIndex_Object = MibTableColumn
f3SystemFeatureIndex = _F3SystemFeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 15, 1, 1, 1),
    _F3SystemFeatureIndex_Type()
)
f3SystemFeatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SystemFeatureIndex.setStatus("current")


class _F3SystemFeatureName_Type(DisplayString):
    """Custom type f3SystemFeatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_F3SystemFeatureName_Type.__name__ = "DisplayString"
_F3SystemFeatureName_Object = MibTableColumn
f3SystemFeatureName = _F3SystemFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 15, 1, 1, 2),
    _F3SystemFeatureName_Type()
)
f3SystemFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SystemFeatureName.setStatus("current")
_F3SystemFeatureEnabled_Type = TruthValue
_F3SystemFeatureEnabled_Object = MibTableColumn
f3SystemFeatureEnabled = _F3SystemFeatureEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 15, 1, 1, 3),
    _F3SystemFeatureEnabled_Type()
)
f3SystemFeatureEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SystemFeatureEnabled.setStatus("current")
_CmLldpV2DestAdressADVAExtObjects_ObjectIdentity = ObjectIdentity
cmLldpV2DestAdressADVAExtObjects = _CmLldpV2DestAdressADVAExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16)
)
_F3SystemLldpV2DestAddressADVAExtTable_Object = MibTable
f3SystemLldpV2DestAddressADVAExtTable = _F3SystemLldpV2DestAddressADVAExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16, 1)
)
if mibBuilder.loadTexts:
    f3SystemLldpV2DestAddressADVAExtTable.setStatus("current")
_F3SystemLldpV2DestAddressADVAExtEntry_Object = MibTableRow
f3SystemLldpV2DestAddressADVAExtEntry = _F3SystemLldpV2DestAddressADVAExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16, 1, 1)
)
f3SystemLldpV2DestAddressADVAExtEntry.setIndexNames(
    (0, "CM-SYSTEM-MIB", "f3SystemLldpV2DestAddressADVAExtIndex"),
)
if mibBuilder.loadTexts:
    f3SystemLldpV2DestAddressADVAExtEntry.setStatus("current")
_F3SystemLldpV2DestAddressADVAExtIndex_Type = Integer32
_F3SystemLldpV2DestAddressADVAExtIndex_Object = MibTableColumn
f3SystemLldpV2DestAddressADVAExtIndex = _F3SystemLldpV2DestAddressADVAExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16, 1, 1, 1),
    _F3SystemLldpV2DestAddressADVAExtIndex_Type()
)
f3SystemLldpV2DestAddressADVAExtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SystemLldpV2DestAddressADVAExtIndex.setStatus("current")
_F3SystemLldpV2ADVAExtDestMacAddress_Type = MacAddress
_F3SystemLldpV2ADVAExtDestMacAddress_Object = MibTableColumn
f3SystemLldpV2ADVAExtDestMacAddress = _F3SystemLldpV2ADVAExtDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16, 1, 1, 2),
    _F3SystemLldpV2ADVAExtDestMacAddress_Type()
)
f3SystemLldpV2ADVAExtDestMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SystemLldpV2ADVAExtDestMacAddress.setStatus("current")
_F3SystemLldpV2DestAddressADVAExtRowStatus_Type = RowStatus
_F3SystemLldpV2DestAddressADVAExtRowStatus_Object = MibTableColumn
f3SystemLldpV2DestAddressADVAExtRowStatus = _F3SystemLldpV2DestAddressADVAExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16, 1, 1, 3),
    _F3SystemLldpV2DestAddressADVAExtRowStatus_Type()
)
f3SystemLldpV2DestAddressADVAExtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SystemLldpV2DestAddressADVAExtRowStatus.setStatus("current")
_F3SystemLldpV2PortConfigADVAExtTable_Object = MibTable
f3SystemLldpV2PortConfigADVAExtTable = _F3SystemLldpV2PortConfigADVAExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16, 2)
)
if mibBuilder.loadTexts:
    f3SystemLldpV2PortConfigADVAExtTable.setStatus("current")
_F3SystemLldpV2PortConfigADVAExtEntry_Object = MibTableRow
f3SystemLldpV2PortConfigADVAExtEntry = _F3SystemLldpV2PortConfigADVAExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16, 2, 1)
)
f3SystemLldpV2PortConfigADVAExtEntry.setIndexNames(
    (0, "CM-SYSTEM-MIB", "f3SystemLldpV2PortConfigADVAExtIfIndex"),
    (0, "CM-SYSTEM-MIB", "f3SystemLldpV2PortConfigADVAExtDestAddressIndex"),
)
if mibBuilder.loadTexts:
    f3SystemLldpV2PortConfigADVAExtEntry.setStatus("current")
_F3SystemLldpV2PortConfigADVAExtIfIndex_Type = InterfaceIndex
_F3SystemLldpV2PortConfigADVAExtIfIndex_Object = MibTableColumn
f3SystemLldpV2PortConfigADVAExtIfIndex = _F3SystemLldpV2PortConfigADVAExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16, 2, 1, 1),
    _F3SystemLldpV2PortConfigADVAExtIfIndex_Type()
)
f3SystemLldpV2PortConfigADVAExtIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SystemLldpV2PortConfigADVAExtIfIndex.setStatus("current")
_F3SystemLldpV2PortConfigADVAExtDestAddressIndex_Type = LldpV2DestAddressTableIndex
_F3SystemLldpV2PortConfigADVAExtDestAddressIndex_Object = MibTableColumn
f3SystemLldpV2PortConfigADVAExtDestAddressIndex = _F3SystemLldpV2PortConfigADVAExtDestAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16, 2, 1, 2),
    _F3SystemLldpV2PortConfigADVAExtDestAddressIndex_Type()
)
f3SystemLldpV2PortConfigADVAExtDestAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SystemLldpV2PortConfigADVAExtDestAddressIndex.setStatus("current")


class _F3SystemLldpV2PortConfigADVAExtAdminStatus_Type(Integer32):
    """Custom type f3SystemLldpV2PortConfigADVAExtAdminStatus based on Integer32"""
    defaultValue = 3

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
        *(("txOnly", 1),
          ("rxOnly", 2),
          ("txAndRx", 3),
          ("disabled", 4))
    )


_F3SystemLldpV2PortConfigADVAExtAdminStatus_Type.__name__ = "Integer32"
_F3SystemLldpV2PortConfigADVAExtAdminStatus_Object = MibTableColumn
f3SystemLldpV2PortConfigADVAExtAdminStatus = _F3SystemLldpV2PortConfigADVAExtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16, 2, 1, 3),
    _F3SystemLldpV2PortConfigADVAExtAdminStatus_Type()
)
f3SystemLldpV2PortConfigADVAExtAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SystemLldpV2PortConfigADVAExtAdminStatus.setStatus("current")


class _F3SystemLldpV2PortConfigADVAExtNotificationEnable_Type(TruthValue):
    """Custom type f3SystemLldpV2PortConfigADVAExtNotificationEnable based on TruthValue"""
    defaultValue = 2


_F3SystemLldpV2PortConfigADVAExtNotificationEnable_Type.__name__ = "TruthValue"
_F3SystemLldpV2PortConfigADVAExtNotificationEnable_Object = MibTableColumn
f3SystemLldpV2PortConfigADVAExtNotificationEnable = _F3SystemLldpV2PortConfigADVAExtNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16, 2, 1, 4),
    _F3SystemLldpV2PortConfigADVAExtNotificationEnable_Type()
)
f3SystemLldpV2PortConfigADVAExtNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SystemLldpV2PortConfigADVAExtNotificationEnable.setStatus("current")


class _F3SystemLldpV2PortConfigADVAExtTLVsTxEnable_Type(Bits):
    """Custom type f3SystemLldpV2PortConfigADVAExtTLVsTxEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("portDesc", 0),
          ("sysName", 1),
          ("sysDesc", 2),
          ("sysCap", 3))
    )

_F3SystemLldpV2PortConfigADVAExtTLVsTxEnable_Type.__name__ = "Bits"
_F3SystemLldpV2PortConfigADVAExtTLVsTxEnable_Object = MibTableColumn
f3SystemLldpV2PortConfigADVAExtTLVsTxEnable = _F3SystemLldpV2PortConfigADVAExtTLVsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16, 2, 1, 5),
    _F3SystemLldpV2PortConfigADVAExtTLVsTxEnable_Type()
)
f3SystemLldpV2PortConfigADVAExtTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SystemLldpV2PortConfigADVAExtTLVsTxEnable.setStatus("current")
_F3SystemLldpV2PortConfigADVAExtStorageType_Type = StorageType
_F3SystemLldpV2PortConfigADVAExtStorageType_Object = MibTableColumn
f3SystemLldpV2PortConfigADVAExtStorageType = _F3SystemLldpV2PortConfigADVAExtStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16, 2, 1, 6),
    _F3SystemLldpV2PortConfigADVAExtStorageType_Type()
)
f3SystemLldpV2PortConfigADVAExtStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SystemLldpV2PortConfigADVAExtStorageType.setStatus("current")
_F3SystemLldpV2PortConfigADVAExtRowStatus_Type = RowStatus
_F3SystemLldpV2PortConfigADVAExtRowStatus_Object = MibTableColumn
f3SystemLldpV2PortConfigADVAExtRowStatus = _F3SystemLldpV2PortConfigADVAExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16, 2, 1, 7),
    _F3SystemLldpV2PortConfigADVAExtRowStatus_Type()
)
f3SystemLldpV2PortConfigADVAExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SystemLldpV2PortConfigADVAExtRowStatus.setStatus("current")
_F3SystemLldpV2ManAddrConfigTxPortsADVAExtTable_Object = MibTable
f3SystemLldpV2ManAddrConfigTxPortsADVAExtTable = _F3SystemLldpV2ManAddrConfigTxPortsADVAExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16, 3)
)
if mibBuilder.loadTexts:
    f3SystemLldpV2ManAddrConfigTxPortsADVAExtTable.setStatus("current")
_F3SystemLldpV2ManAddrConfigTxPortsADVAExtEntry_Object = MibTableRow
f3SystemLldpV2ManAddrConfigTxPortsADVAExtEntry = _F3SystemLldpV2ManAddrConfigTxPortsADVAExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16, 3, 1)
)
f3SystemLldpV2ManAddrConfigTxPortsADVAExtEntry.setIndexNames(
    (0, "CM-SYSTEM-MIB", "f3SystemLldpV2PortConfigADVAExtIfIndex"),
    (0, "CM-SYSTEM-MIB", "f3SystemLldpV2PortConfigADVAExtDestAddressIndex"),
    (0, "CM-SYSTEM-MIB", "f3SystemLldpV2ManAddrConfigTxPortsADVAExtRefInterface"),
)
if mibBuilder.loadTexts:
    f3SystemLldpV2ManAddrConfigTxPortsADVAExtEntry.setStatus("current")
_F3SystemLldpV2ManAddrConfigTxPortsADVAExtRefInterface_Type = VariablePointer
_F3SystemLldpV2ManAddrConfigTxPortsADVAExtRefInterface_Object = MibTableColumn
f3SystemLldpV2ManAddrConfigTxPortsADVAExtRefInterface = _F3SystemLldpV2ManAddrConfigTxPortsADVAExtRefInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16, 3, 1, 1),
    _F3SystemLldpV2ManAddrConfigTxPortsADVAExtRefInterface_Type()
)
f3SystemLldpV2ManAddrConfigTxPortsADVAExtRefInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SystemLldpV2ManAddrConfigTxPortsADVAExtRefInterface.setStatus("current")
_F3SystemLldpV2ManAddrConfigTxPortsADVAExtEnable_Type = TruthValue
_F3SystemLldpV2ManAddrConfigTxPortsADVAExtEnable_Object = MibTableColumn
f3SystemLldpV2ManAddrConfigTxPortsADVAExtEnable = _F3SystemLldpV2ManAddrConfigTxPortsADVAExtEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16, 3, 1, 2),
    _F3SystemLldpV2ManAddrConfigTxPortsADVAExtEnable_Type()
)
f3SystemLldpV2ManAddrConfigTxPortsADVAExtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SystemLldpV2ManAddrConfigTxPortsADVAExtEnable.setStatus("current")
_F3SystemLldpV2ManAddrConfigTxPortsADVAExtStorageType_Type = StorageType
_F3SystemLldpV2ManAddrConfigTxPortsADVAExtStorageType_Object = MibTableColumn
f3SystemLldpV2ManAddrConfigTxPortsADVAExtStorageType = _F3SystemLldpV2ManAddrConfigTxPortsADVAExtStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16, 3, 1, 3),
    _F3SystemLldpV2ManAddrConfigTxPortsADVAExtStorageType_Type()
)
f3SystemLldpV2ManAddrConfigTxPortsADVAExtStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SystemLldpV2ManAddrConfigTxPortsADVAExtStorageType.setStatus("current")
_F3SystemLldpV2ManAddrConfigTxPortsADVAExtRowStatus_Type = RowStatus
_F3SystemLldpV2ManAddrConfigTxPortsADVAExtRowStatus_Object = MibTableColumn
f3SystemLldpV2ManAddrConfigTxPortsADVAExtRowStatus = _F3SystemLldpV2ManAddrConfigTxPortsADVAExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 16, 3, 1, 4),
    _F3SystemLldpV2ManAddrConfigTxPortsADVAExtRowStatus_Type()
)
f3SystemLldpV2ManAddrConfigTxPortsADVAExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SystemLldpV2ManAddrConfigTxPortsADVAExtRowStatus.setStatus("current")
_F3LldpV2ConfigurationADVAExtObjects_ObjectIdentity = ObjectIdentity
f3LldpV2ConfigurationADVAExtObjects = _F3LldpV2ConfigurationADVAExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 17)
)
_F3LldpMaxNeighborsAction_Type = LldpV2ConfigurationADVAExtMaxNeighborsAction
_F3LldpMaxNeighborsAction_Object = MibScalar
f3LldpMaxNeighborsAction = _F3LldpMaxNeighborsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 17, 1),
    _F3LldpMaxNeighborsAction_Type()
)
f3LldpMaxNeighborsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3LldpMaxNeighborsAction.setStatus("current")
_SnmpIPv6UDPDomain_ObjectIdentity = ObjectIdentity
snmpIPv6UDPDomain = _SnmpIPv6UDPDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 18)
)
_F3RawDataObjects_ObjectIdentity = ObjectIdentity
f3RawDataObjects = _F3RawDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 19)
)
_F3RawDataServerFtProtocol_Type = CmFileTransferMethod
_F3RawDataServerFtProtocol_Object = MibScalar
f3RawDataServerFtProtocol = _F3RawDataServerFtProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 19, 1),
    _F3RawDataServerFtProtocol_Type()
)
f3RawDataServerFtProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3RawDataServerFtProtocol.setStatus("current")
_F3RawDataServerFtServerName_Type = IpAddress
_F3RawDataServerFtServerName_Object = MibScalar
f3RawDataServerFtServerName = _F3RawDataServerFtServerName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 19, 2),
    _F3RawDataServerFtServerName_Type()
)
f3RawDataServerFtServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3RawDataServerFtServerName.setStatus("current")


class _F3RawDataServerFtUserId_Type(DisplayString):
    """Custom type f3RawDataServerFtUserId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_F3RawDataServerFtUserId_Type.__name__ = "DisplayString"
_F3RawDataServerFtUserId_Object = MibScalar
f3RawDataServerFtUserId = _F3RawDataServerFtUserId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 19, 3),
    _F3RawDataServerFtUserId_Type()
)
f3RawDataServerFtUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3RawDataServerFtUserId.setStatus("current")


class _F3RawDataServerFtPasswd_Type(DisplayString):
    """Custom type f3RawDataServerFtPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_F3RawDataServerFtPasswd_Type.__name__ = "DisplayString"
_F3RawDataServerFtPasswd_Object = MibScalar
f3RawDataServerFtPasswd = _F3RawDataServerFtPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 19, 4),
    _F3RawDataServerFtPasswd_Type()
)
f3RawDataServerFtPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3RawDataServerFtPasswd.setStatus("current")
_F3LldpV2RemoteSystemsData_ObjectIdentity = ObjectIdentity
f3LldpV2RemoteSystemsData = _F3LldpV2RemoteSystemsData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 20)
)
_F3LldpV2RemExtTable_Object = MibTable
f3LldpV2RemExtTable = _F3LldpV2RemExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 20, 1)
)
if mibBuilder.loadTexts:
    f3LldpV2RemExtTable.setStatus("current")
_F3LldpV2RemExtEntry_Object = MibTableRow
f3LldpV2RemExtEntry = _F3LldpV2RemExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 20, 1, 1)
)
if mibBuilder.loadTexts:
    f3LldpV2RemExtEntry.setStatus("current")


class _F3LldpV2RemTTL_Type(Unsigned32):
    """Custom type f3LldpV2RemTTL based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3LldpV2RemTTL_Type.__name__ = "Unsigned32"
_F3LldpV2RemTTL_Object = MibTableColumn
f3LldpV2RemTTL = _F3LldpV2RemTTL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 1, 20, 1, 1, 1),
    _F3LldpV2RemTTL_Type()
)
f3LldpV2RemTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3LldpV2RemTTL.setStatus("current")
_CmSystemNotifications_ObjectIdentity = ObjectIdentity
cmSystemNotifications = _CmSystemNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 2)
)
_CmSystemConformance_ObjectIdentity = ObjectIdentity
cmSystemConformance = _CmSystemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 3)
)
_CmSystemCompliances_ObjectIdentity = ObjectIdentity
cmSystemCompliances = _CmSystemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 3, 1)
)
_CmSystemGroups_ObjectIdentity = ObjectIdentity
cmSystemGroups = _CmSystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 3, 2)
)
_F3SystemBulkGroups_ObjectIdentity = ObjectIdentity
f3SystemBulkGroups = _F3SystemBulkGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 3, 3)
)
_F3BulkNotifObjects_ObjectIdentity = ObjectIdentity
f3BulkNotifObjects = _F3BulkNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 4)
)
_F3StartNeEventLogIndex_Type = TrapCounter
_F3StartNeEventLogIndex_Object = MibScalar
f3StartNeEventLogIndex = _F3StartNeEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 4, 1),
    _F3StartNeEventLogIndex_Type()
)
f3StartNeEventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3StartNeEventLogIndex.setStatus("current")
_F3EndNeEventLogIndex_Type = TrapCounter
_F3EndNeEventLogIndex_Object = MibScalar
f3EndNeEventLogIndex = _F3EndNeEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 4, 2),
    _F3EndNeEventLogIndex_Type()
)
f3EndNeEventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EndNeEventLogIndex.setStatus("current")
_F3SystemBulkNotifications_ObjectIdentity = ObjectIdentity
f3SystemBulkNotifications = _F3SystemBulkNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 5)
)
lldpV2RemEntry.registerAugmentions(
    ("CM-SYSTEM-MIB",
     "f3LldpV2RemExtEntry")
)
f3LldpV2RemExtEntry.setIndexNames(*lldpV2RemEntry.getIndexNames())

# Managed Objects groups

cmSystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 3, 2, 1)
)
cmSystemObjectGroup.setObjects(
      *(("CM-SYSTEM-MIB", "lastSetErrorInformation"),
        ("CM-SYSTEM-MIB", "cliCmdPromptPrefix"),
        ("CM-SYSTEM-MIB", "securityPromptEnabled"),
        ("CM-SYSTEM-MIB", "securityBanner"),
        ("CM-SYSTEM-MIB", "aclEntryFilterAction"),
        ("CM-SYSTEM-MIB", "aclEntryNetworkAddress"),
        ("CM-SYSTEM-MIB", "aclEntryNetworkMask"),
        ("CM-SYSTEM-MIB", "aclEntryEnabled"),
        ("CM-SYSTEM-MIB", "aclEntryIpVersion"),
        ("CM-SYSTEM-MIB", "aclEntryNetworkIpv6Addr"),
        ("CM-SYSTEM-MIB", "aclEntryPrefixLength"),
        ("CM-SYSTEM-MIB", "serialPortDisconnectAutoLogOff"),
        ("CM-SYSTEM-MIB", "telnetEnabled"),
        ("CM-SYSTEM-MIB", "sshEnabled"),
        ("CM-SYSTEM-MIB", "ftpEnabled"),
        ("CM-SYSTEM-MIB", "scpEnabled"),
        ("CM-SYSTEM-MIB", "serialPortEnabled"),
        ("CM-SYSTEM-MIB", "httpEnabled"),
        ("CM-SYSTEM-MIB", "httpsEnabled"),
        ("CM-SYSTEM-MIB", "sftpEnabled"),
        ("CM-SYSTEM-MIB", "tftpEnabled"),
        ("CM-SYSTEM-MIB", "ntpMode"),
        ("CM-SYSTEM-MIB", "autoProvMode"),
        ("CM-SYSTEM-MIB", "sysTimeOfDayType"),
        ("CM-SYSTEM-MIB", "ntpServerConfigType"),
        ("CM-SYSTEM-MIB", "sysLogServerConfigType"),
        ("CM-SYSTEM-MIB", "fileServicesAction"),
        ("CM-SYSTEM-MIB", "fileServicesMethod"),
        ("CM-SYSTEM-MIB", "fileServicesServerIp"),
        ("CM-SYSTEM-MIB", "fileServicesUserId"),
        ("CM-SYSTEM-MIB", "fileServicesPassword"),
        ("CM-SYSTEM-MIB", "fileServicesRemoteFile"),
        ("CM-SYSTEM-MIB", "fileServicesStatus"),
        ("CM-SYSTEM-MIB", "fileServicesPercentComplete"),
        ("CM-SYSTEM-MIB", "fileServicesMode"),
        ("CM-SYSTEM-MIB", "databaseAction"),
        ("CM-SYSTEM-MIB", "databaseLastSaveTime"),
        ("CM-SYSTEM-MIB", "databaseIndex"),
        ("CM-SYSTEM-MIB", "databaseType"),
        ("CM-SYSTEM-MIB", "databaseVersion"),
        ("CM-SYSTEM-MIB", "softwareAction"),
        ("CM-SYSTEM-MIB", "softwareUpgradeTime"),
        ("CM-SYSTEM-MIB", "softwareValidationTimer"),
        ("CM-SYSTEM-MIB", "softwareIndex"),
        ("CM-SYSTEM-MIB", "softwareType"),
        ("CM-SYSTEM-MIB", "softwareVersion"),
        ("CM-SYSTEM-MIB", "sysLogServerIndex"),
        ("CM-SYSTEM-MIB", "sysLogIpAddress"),
        ("CM-SYSTEM-MIB", "sysLogPort"),
        ("CM-SYSTEM-MIB", "secLog2sysLogEnabled"),
        ("CM-SYSTEM-MIB", "auditLog2sysLogEnabled"),
        ("CM-SYSTEM-MIB", "auditLog2fileEnabled"),
        ("CM-SYSTEM-MIB", "alarmLog2sysLogEnabled"),
        ("CM-SYSTEM-MIB", "alarmLog2fileEnabled"),
        ("CM-SYSTEM-MIB", "ntpClientEnabled"),
        ("CM-SYSTEM-MIB", "ntpPrimaryServer"),
        ("CM-SYSTEM-MIB", "ntpBackupServer"),
        ("CM-SYSTEM-MIB", "ntpType"),
        ("CM-SYSTEM-MIB", "ntpActiveServer"),
        ("CM-SYSTEM-MIB", "ntpSwitchServer"),
        ("CM-SYSTEM-MIB", "ntpServerRoundTripDelay"),
        ("CM-SYSTEM-MIB", "ntpServerPrecision"),
        ("CM-SYSTEM-MIB", "ntpPollingInterval"),
        ("CM-SYSTEM-MIB", "f3SnmpTargetAddrExtDyingGaspPort"),
        ("CM-SYSTEM-MIB", "f3SnmpTargetAddrExtDyingGaspEnabled"),
        ("CM-SYSTEM-MIB", "f3SnmpTargetAddrExtDyingGaspActive"),
        ("CM-SYSTEM-MIB", "f3SnmpTargetAddrExtBulkTrapsEnabled"),
        ("CM-SYSTEM-MIB", "f3SysLastResetType"),
        ("CM-SYSTEM-MIB", "f3SysLastResetCauseType"),
        ("CM-SYSTEM-MIB", "f3SysLastAbnormalResetTimestamp1"),
        ("CM-SYSTEM-MIB", "f3SysLastAbnormalResetTimestamp2"),
        ("CM-SYSTEM-MIB", "f3SysLastAbnormalResetTimestamp3"),
        ("CM-SYSTEM-MIB", "f3DatabaseSyncTrapObject"),
        ("CM-SYSTEM-MIB", "f3ConfigFileActionFileName"),
        ("CM-SYSTEM-MIB", "f3ConfigFileAction"),
        ("CM-SYSTEM-MIB", "f3ConfigFileStatus"),
        ("CM-SYSTEM-MIB", "f3ConfigFileErrorInformation"),
        ("CM-SYSTEM-MIB", "f3ConfigFileIndex"),
        ("CM-SYSTEM-MIB", "f3ConfigFileName"),
        ("CM-SYSTEM-MIB", "f3ConfigFileDescription"),
        ("CM-SYSTEM-MIB", "f3ConfigFilePercentComplete"),
        ("CM-SYSTEM-MIB", "f3SystemFeatureIndex"),
        ("CM-SYSTEM-MIB", "f3SystemFeatureName"),
        ("CM-SYSTEM-MIB", "f3SystemFeatureEnabled"),
        ("CM-SYSTEM-MIB", "f3SystemLldpV2DestAddressADVAExtIndex"),
        ("CM-SYSTEM-MIB", "f3SystemLldpV2ADVAExtDestMacAddress"),
        ("CM-SYSTEM-MIB", "f3SystemLldpV2DestAddressADVAExtRowStatus"),
        ("CM-SYSTEM-MIB", "f3LldpMaxNeighborsAction"),
        ("CM-SYSTEM-MIB", "f3SystemLldpV2PortConfigADVAExtIfIndex"),
        ("CM-SYSTEM-MIB", "f3SystemLldpV2PortConfigADVAExtDestAddressIndex"),
        ("CM-SYSTEM-MIB", "f3SystemLldpV2PortConfigADVAExtAdminStatus"),
        ("CM-SYSTEM-MIB", "f3SystemLldpV2PortConfigADVAExtNotificationEnable"),
        ("CM-SYSTEM-MIB", "f3SystemLldpV2PortConfigADVAExtTLVsTxEnable"),
        ("CM-SYSTEM-MIB", "f3SystemLldpV2PortConfigADVAExtStorageType"),
        ("CM-SYSTEM-MIB", "f3SystemLldpV2PortConfigADVAExtRowStatus"),
        ("CM-SYSTEM-MIB", "f3SystemLldpV2ManAddrConfigTxPortsADVAExtRefInterface"),
        ("CM-SYSTEM-MIB", "f3SystemLldpV2ManAddrConfigTxPortsADVAExtEnable"),
        ("CM-SYSTEM-MIB", "f3SystemLldpV2ManAddrConfigTxPortsADVAExtStorageType"),
        ("CM-SYSTEM-MIB", "f3SystemLldpV2ManAddrConfigTxPortsADVAExtRowStatus"),
        ("CM-SYSTEM-MIB", "f3RawDataServerFtProtocol"),
        ("CM-SYSTEM-MIB", "f3RawDataServerFtServerName"),
        ("CM-SYSTEM-MIB", "f3RawDataServerFtUserId"),
        ("CM-SYSTEM-MIB", "f3RawDataServerFtPasswd"),
        ("CM-SYSTEM-MIB", "f3LldpV2RemTTL"))
)
if mibBuilder.loadTexts:
    cmSystemObjectGroup.setStatus("current")

cmSystemObjectGroupCmHub = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 3, 2, 3)
)
cmSystemObjectGroupCmHub.setObjects(
      *(("CM-SYSTEM-MIB", "lastSetErrorInformation"),
        ("CM-SYSTEM-MIB", "cliCmdPromptPrefix"),
        ("CM-SYSTEM-MIB", "securityPromptEnabled"),
        ("CM-SYSTEM-MIB", "securityBanner"),
        ("CM-SYSTEM-MIB", "aclEntryFilterAction"),
        ("CM-SYSTEM-MIB", "aclEntryNetworkAddress"),
        ("CM-SYSTEM-MIB", "aclEntryNetworkMask"),
        ("CM-SYSTEM-MIB", "aclEntryEnabled"),
        ("CM-SYSTEM-MIB", "serialPortDisconnectAutoLogOff"),
        ("CM-SYSTEM-MIB", "telnetEnabled"),
        ("CM-SYSTEM-MIB", "sshEnabled"),
        ("CM-SYSTEM-MIB", "ftpEnabled"),
        ("CM-SYSTEM-MIB", "scpEnabled"),
        ("CM-SYSTEM-MIB", "serialPortEnabled"),
        ("CM-SYSTEM-MIB", "httpEnabled"),
        ("CM-SYSTEM-MIB", "httpsEnabled"),
        ("CM-SYSTEM-MIB", "sftpEnabled"),
        ("CM-SYSTEM-MIB", "ntpMode"),
        ("CM-SYSTEM-MIB", "autoProvMode"),
        ("CM-SYSTEM-MIB", "fileServicesAction"),
        ("CM-SYSTEM-MIB", "fileServicesMethod"),
        ("CM-SYSTEM-MIB", "fileServicesServerIp"),
        ("CM-SYSTEM-MIB", "fileServicesUserId"),
        ("CM-SYSTEM-MIB", "fileServicesPassword"),
        ("CM-SYSTEM-MIB", "fileServicesRemoteFile"),
        ("CM-SYSTEM-MIB", "fileServicesStatus"),
        ("CM-SYSTEM-MIB", "fileServicesPercentComplete"),
        ("CM-SYSTEM-MIB", "fileServicesMode"),
        ("CM-SYSTEM-MIB", "fileServicesServerType"),
        ("CM-SYSTEM-MIB", "fileServicesServerIpv6Addr"),
        ("CM-SYSTEM-MIB", "sysLogIpVersion"),
        ("CM-SYSTEM-MIB", "sysLogIpv6Addr"),
        ("CM-SYSTEM-MIB", "ntpPrimaryServerIpVersion"),
        ("CM-SYSTEM-MIB", "ntpPrimaryServerIpv6Addr"),
        ("CM-SYSTEM-MIB", "ntpBackupServerIpVersion"),
        ("CM-SYSTEM-MIB", "ntpBackupServerIpv6Addr"),
        ("CM-SYSTEM-MIB", "databaseAction"),
        ("CM-SYSTEM-MIB", "databaseLastSaveTime"),
        ("CM-SYSTEM-MIB", "databaseIndex"),
        ("CM-SYSTEM-MIB", "databaseType"),
        ("CM-SYSTEM-MIB", "databaseVersion"),
        ("CM-SYSTEM-MIB", "softwareAction"),
        ("CM-SYSTEM-MIB", "softwareUpgradeTime"),
        ("CM-SYSTEM-MIB", "softwareValidationTimer"),
        ("CM-SYSTEM-MIB", "softwareIndex"),
        ("CM-SYSTEM-MIB", "softwareType"),
        ("CM-SYSTEM-MIB", "softwareVersion"),
        ("CM-SYSTEM-MIB", "sysLogServerIndex"),
        ("CM-SYSTEM-MIB", "sysLogIpAddress"),
        ("CM-SYSTEM-MIB", "sysLogPort"),
        ("CM-SYSTEM-MIB", "secLog2sysLogEnabled"),
        ("CM-SYSTEM-MIB", "auditLog2sysLogEnabled"),
        ("CM-SYSTEM-MIB", "auditLog2fileEnabled"),
        ("CM-SYSTEM-MIB", "alarmLog2sysLogEnabled"),
        ("CM-SYSTEM-MIB", "alarmLog2fileEnabled"),
        ("CM-SYSTEM-MIB", "ntpClientEnabled"),
        ("CM-SYSTEM-MIB", "ntpPrimaryServer"),
        ("CM-SYSTEM-MIB", "ntpBackupServer"),
        ("CM-SYSTEM-MIB", "ntpType"),
        ("CM-SYSTEM-MIB", "ntpActiveServer"),
        ("CM-SYSTEM-MIB", "ntpSwitchServer"),
        ("CM-SYSTEM-MIB", "ntpServerRoundTripDelay"),
        ("CM-SYSTEM-MIB", "ntpServerPrecision"),
        ("CM-SYSTEM-MIB", "ntpPollingInterval"),
        ("CM-SYSTEM-MIB", "f3SnmpTargetAddrExtDyingGaspPort"),
        ("CM-SYSTEM-MIB", "f3SnmpTargetAddrExtDyingGaspEnabled"),
        ("CM-SYSTEM-MIB", "f3SnmpTargetAddrExtDyingGaspActive"),
        ("CM-SYSTEM-MIB", "f3SysLastResetType"),
        ("CM-SYSTEM-MIB", "f3SysLastResetCauseType"),
        ("CM-SYSTEM-MIB", "f3SysLastAbnormalResetTimestamp1"),
        ("CM-SYSTEM-MIB", "f3SysLastAbnormalResetTimestamp2"),
        ("CM-SYSTEM-MIB", "f3SysLastAbnormalResetTimestamp3"),
        ("CM-SYSTEM-MIB", "f3DatabaseSyncTrapObject"))
)
if mibBuilder.loadTexts:
    cmSystemObjectGroupCmHub.setStatus("current")

f3SystemObjectBulkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 3, 3, 1)
)
f3SystemObjectBulkGroup.setObjects(
      *(("CM-SYSTEM-MIB", "f3StartNeEventLogIndex"),
        ("CM-SYSTEM-MIB", "f3EndNeEventLogIndex"))
)
if mibBuilder.loadTexts:
    f3SystemObjectBulkGroup.setStatus("current")


# Notification objects

cmStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cmStateChangeTrap.setStatus(
        "current"
    )

cmAttributeValueChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cmAttributeValueChangeTrap.setStatus(
        "current"
    )

cmObjectCreationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 2, 3)
)
if mibBuilder.loadTexts:
    cmObjectCreationTrap.setStatus(
        "current"
    )

cmObjectDeletionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 2, 4)
)
if mibBuilder.loadTexts:
    cmObjectDeletionTrap.setStatus(
        "current"
    )

cmSnmpDyingGaspTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 2, 5)
)
if mibBuilder.loadTexts:
    cmSnmpDyingGaspTrap.setStatus(
        "current"
    )

f3DatabaseSyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 2, 6)
)
if mibBuilder.loadTexts:
    f3DatabaseSyncTrap.setStatus(
        "current"
    )

f3BulkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 5, 1)
)
if mibBuilder.loadTexts:
    f3BulkTrap.setStatus(
        "current"
    )


# Notifications groups

cmSystemNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 3, 2, 2)
)
cmSystemNotifGroup.setObjects(
      *(("CM-SYSTEM-MIB", "cmStateChangeTrap"),
        ("CM-SYSTEM-MIB", "cmAttributeValueChangeTrap"),
        ("CM-SYSTEM-MIB", "cmObjectCreationTrap"),
        ("CM-SYSTEM-MIB", "cmObjectDeletionTrap"),
        ("CM-SYSTEM-MIB", "cmSnmpDyingGaspTrap"),
        ("CM-SYSTEM-MIB", "f3DatabaseSyncTrap"))
)
if mibBuilder.loadTexts:
    cmSystemNotifGroup.setStatus(
        "current"
    )

f3SystemNotifBulkGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 3, 3, 2)
)
f3SystemNotifBulkGroup.setObjects(
    ("CM-SYSTEM-MIB", "f3BulkTrap")
)
if mibBuilder.loadTexts:
    f3SystemNotifBulkGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cmSystemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 2, 3, 1, 1)
)
cmSystemCompliance.setObjects(
      *(("CM-SYSTEM-MIB", "cmSystemObjectGroup"),
        ("CM-SYSTEM-MIB", "cmSystemNotifGroup"),
        ("CM-SYSTEM-MIB", "f3SystemObjectBulkGroup"),
        ("CM-SYSTEM-MIB", "f3SystemNotifBulkGroup"))
)
if mibBuilder.loadTexts:
    cmSystemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CM-SYSTEM-MIB",
    **{"CmAclFilterAction": CmAclFilterAction,
       "CmAutoProvMode": CmAutoProvMode,
       "CmNtpType": CmNtpType,
       "CmNtpMode": CmNtpMode,
       "CmNtpServerType": CmNtpServerType,
       "CmFileTransferMethod": CmFileTransferMethod,
       "CmVersionType": CmVersionType,
       "CmFileServicesStatus": CmFileServicesStatus,
       "CmFileServicesMode": CmFileServicesMode,
       "CmRestartCauseType": CmRestartCauseType,
       "F3ConfigFileAction": F3ConfigFileAction,
       "F3ConfigFileStatus": F3ConfigFileStatus,
       "TimeOfDayType": TimeOfDayType,
       "LldpV2ConfigurationADVAExtMaxNeighborsAction": LldpV2ConfigurationADVAExtMaxNeighborsAction,
       "FileTransferServerType": FileTransferServerType,
       "ServerConfigType": ServerConfigType,
       "cmSystemMIB": cmSystemMIB,
       "cmSystemObjects": cmSystemObjects,
       "cmErrorInfoObjects": cmErrorInfoObjects,
       "lastSetErrorInformation": lastSetErrorInformation,
       "cmCliObjects": cmCliObjects,
       "cliCmdPromptPrefix": cliCmdPromptPrefix,
       "cmAccessProtocols": cmAccessProtocols,
       "telnetEnabled": telnetEnabled,
       "sshEnabled": sshEnabled,
       "ftpEnabled": ftpEnabled,
       "scpEnabled": scpEnabled,
       "serialPortEnabled": serialPortEnabled,
       "httpEnabled": httpEnabled,
       "httpsEnabled": httpsEnabled,
       "sftpEnabled": sftpEnabled,
       "tftpEnabled": tftpEnabled,
       "cmSysSecObjects": cmSysSecObjects,
       "securityBanner": securityBanner,
       "aclTable": aclTable,
       "aclEntry": aclEntry,
       "aclEntryIndex": aclEntryIndex,
       "aclEntryFilterAction": aclEntryFilterAction,
       "aclEntryNetworkAddress": aclEntryNetworkAddress,
       "aclEntryNetworkMask": aclEntryNetworkMask,
       "aclEntryEnabled": aclEntryEnabled,
       "aclEntryIpVersion": aclEntryIpVersion,
       "aclEntryNetworkIpv6Addr": aclEntryNetworkIpv6Addr,
       "aclEntryPrefixLength": aclEntryPrefixLength,
       "serialPortDisconnectAutoLogOff": serialPortDisconnectAutoLogOff,
       "securityPromptEnabled": securityPromptEnabled,
       "cmSysModeObjects": cmSysModeObjects,
       "ntpMode": ntpMode,
       "autoProvMode": autoProvMode,
       "sysTimeOfDayType": sysTimeOfDayType,
       "ntpServerConfigType": ntpServerConfigType,
       "sysLogServerConfigType": sysLogServerConfigType,
       "sysUseUtcLeapOffsetEnable": sysUseUtcLeapOffsetEnable,
       "cmDatabaseObjects": cmDatabaseObjects,
       "databaseAction": databaseAction,
       "databaseLastSaveTime": databaseLastSaveTime,
       "databaseTable": databaseTable,
       "databaseEntry": databaseEntry,
       "databaseIndex": databaseIndex,
       "databaseType": databaseType,
       "databaseVersion": databaseVersion,
       "cmSoftwareObjects": cmSoftwareObjects,
       "softwareAction": softwareAction,
       "softwareUpgradeTime": softwareUpgradeTime,
       "softwareValidationTimer": softwareValidationTimer,
       "softwareTable": softwareTable,
       "softwareEntry": softwareEntry,
       "softwareIndex": softwareIndex,
       "softwareType": softwareType,
       "softwareVersion": softwareVersion,
       "cmFileServicesObjects": cmFileServicesObjects,
       "fileServicesAction": fileServicesAction,
       "fileServicesMethod": fileServicesMethod,
       "fileServicesServerIp": fileServicesServerIp,
       "fileServicesUserId": fileServicesUserId,
       "fileServicesPassword": fileServicesPassword,
       "fileServicesRemoteFile": fileServicesRemoteFile,
       "fileServicesStatus": fileServicesStatus,
       "fileServicesPercentComplete": fileServicesPercentComplete,
       "fileServicesMode": fileServicesMode,
       "fileServicesServerType": fileServicesServerType,
       "fileServicesServerIpv6Addr": fileServicesServerIpv6Addr,
       "cmLogObjects": cmLogObjects,
       "cmSysLogObjects": cmSysLogObjects,
       "sysLogServerTable": sysLogServerTable,
       "sysLogServerEntry": sysLogServerEntry,
       "sysLogServerIndex": sysLogServerIndex,
       "sysLogIpAddress": sysLogIpAddress,
       "sysLogPort": sysLogPort,
       "sysLogIpVersion": sysLogIpVersion,
       "sysLogIpv6Addr": sysLogIpv6Addr,
       "cmSecLogObjects": cmSecLogObjects,
       "secLog2sysLogEnabled": secLog2sysLogEnabled,
       "cmAuditLogObjects": cmAuditLogObjects,
       "auditLog2sysLogEnabled": auditLog2sysLogEnabled,
       "auditLog2fileEnabled": auditLog2fileEnabled,
       "cmAlarmLogObjects": cmAlarmLogObjects,
       "alarmLog2sysLogEnabled": alarmLog2sysLogEnabled,
       "alarmLog2fileEnabled": alarmLog2fileEnabled,
       "cmTimeObjects": cmTimeObjects,
       "ntpClientEnabled": ntpClientEnabled,
       "ntpPrimaryServer": ntpPrimaryServer,
       "ntpBackupServer": ntpBackupServer,
       "ntpType": ntpType,
       "ntpActiveServer": ntpActiveServer,
       "ntpSwitchServer": ntpSwitchServer,
       "ntpServerRoundTripDelay": ntpServerRoundTripDelay,
       "ntpServerPrecision": ntpServerPrecision,
       "ntpPollingInterval": ntpPollingInterval,
       "ntpPrimaryServerIpVersion": ntpPrimaryServerIpVersion,
       "ntpPrimaryServerIpv6Addr": ntpPrimaryServerIpv6Addr,
       "ntpBackupServerIpVersion": ntpBackupServerIpVersion,
       "ntpBackupServerIpv6Addr": ntpBackupServerIpv6Addr,
       "cmSnmpObjects": cmSnmpObjects,
       "f3SnmpTargetAddrExtTable": f3SnmpTargetAddrExtTable,
       "f3SnmpTargetAddrExtEntry": f3SnmpTargetAddrExtEntry,
       "f3SnmpTargetAddrExtDyingGaspPort": f3SnmpTargetAddrExtDyingGaspPort,
       "f3SnmpTargetAddrExtDyingGaspEnabled": f3SnmpTargetAddrExtDyingGaspEnabled,
       "f3SnmpTargetAddrExtDyingGaspActive": f3SnmpTargetAddrExtDyingGaspActive,
       "f3SnmpTargetAddrExtBulkTrapsEnabled": f3SnmpTargetAddrExtBulkTrapsEnabled,
       "f3SnmpEngineID": f3SnmpEngineID,
       "f3SnmpLongIfAlias": f3SnmpLongIfAlias,
       "cmResetCauseObjects": cmResetCauseObjects,
       "f3SysLastResetType": f3SysLastResetType,
       "f3SysLastResetCauseType": f3SysLastResetCauseType,
       "f3SysLastAbnormalResetTimestamp1": f3SysLastAbnormalResetTimestamp1,
       "f3SysLastAbnormalResetTimestamp2": f3SysLastAbnormalResetTimestamp2,
       "f3SysLastAbnormalResetTimestamp3": f3SysLastAbnormalResetTimestamp3,
       "f3NotifObjects": f3NotifObjects,
       "f3DatabaseSyncTrapObject": f3DatabaseSyncTrapObject,
       "f3ConfigFileObjects": f3ConfigFileObjects,
       "f3ConfigFileActionFileName": f3ConfigFileActionFileName,
       "f3ConfigFileAction": f3ConfigFileAction,
       "f3ConfigFileStatus": f3ConfigFileStatus,
       "f3ConfigFileErrorInformation": f3ConfigFileErrorInformation,
       "f3ConfigFileTable": f3ConfigFileTable,
       "f3ConfigFileEntry": f3ConfigFileEntry,
       "f3ConfigFileIndex": f3ConfigFileIndex,
       "f3ConfigFileName": f3ConfigFileName,
       "f3ConfigFileDescription": f3ConfigFileDescription,
       "f3ConfigFilePercentComplete": f3ConfigFilePercentComplete,
       "cmFeatureManagementObjects": cmFeatureManagementObjects,
       "f3SystemFeatureTable": f3SystemFeatureTable,
       "f3SystemFeatureEntry": f3SystemFeatureEntry,
       "f3SystemFeatureIndex": f3SystemFeatureIndex,
       "f3SystemFeatureName": f3SystemFeatureName,
       "f3SystemFeatureEnabled": f3SystemFeatureEnabled,
       "cmLldpV2DestAdressADVAExtObjects": cmLldpV2DestAdressADVAExtObjects,
       "f3SystemLldpV2DestAddressADVAExtTable": f3SystemLldpV2DestAddressADVAExtTable,
       "f3SystemLldpV2DestAddressADVAExtEntry": f3SystemLldpV2DestAddressADVAExtEntry,
       "f3SystemLldpV2DestAddressADVAExtIndex": f3SystemLldpV2DestAddressADVAExtIndex,
       "f3SystemLldpV2ADVAExtDestMacAddress": f3SystemLldpV2ADVAExtDestMacAddress,
       "f3SystemLldpV2DestAddressADVAExtRowStatus": f3SystemLldpV2DestAddressADVAExtRowStatus,
       "f3SystemLldpV2PortConfigADVAExtTable": f3SystemLldpV2PortConfigADVAExtTable,
       "f3SystemLldpV2PortConfigADVAExtEntry": f3SystemLldpV2PortConfigADVAExtEntry,
       "f3SystemLldpV2PortConfigADVAExtIfIndex": f3SystemLldpV2PortConfigADVAExtIfIndex,
       "f3SystemLldpV2PortConfigADVAExtDestAddressIndex": f3SystemLldpV2PortConfigADVAExtDestAddressIndex,
       "f3SystemLldpV2PortConfigADVAExtAdminStatus": f3SystemLldpV2PortConfigADVAExtAdminStatus,
       "f3SystemLldpV2PortConfigADVAExtNotificationEnable": f3SystemLldpV2PortConfigADVAExtNotificationEnable,
       "f3SystemLldpV2PortConfigADVAExtTLVsTxEnable": f3SystemLldpV2PortConfigADVAExtTLVsTxEnable,
       "f3SystemLldpV2PortConfigADVAExtStorageType": f3SystemLldpV2PortConfigADVAExtStorageType,
       "f3SystemLldpV2PortConfigADVAExtRowStatus": f3SystemLldpV2PortConfigADVAExtRowStatus,
       "f3SystemLldpV2ManAddrConfigTxPortsADVAExtTable": f3SystemLldpV2ManAddrConfigTxPortsADVAExtTable,
       "f3SystemLldpV2ManAddrConfigTxPortsADVAExtEntry": f3SystemLldpV2ManAddrConfigTxPortsADVAExtEntry,
       "f3SystemLldpV2ManAddrConfigTxPortsADVAExtRefInterface": f3SystemLldpV2ManAddrConfigTxPortsADVAExtRefInterface,
       "f3SystemLldpV2ManAddrConfigTxPortsADVAExtEnable": f3SystemLldpV2ManAddrConfigTxPortsADVAExtEnable,
       "f3SystemLldpV2ManAddrConfigTxPortsADVAExtStorageType": f3SystemLldpV2ManAddrConfigTxPortsADVAExtStorageType,
       "f3SystemLldpV2ManAddrConfigTxPortsADVAExtRowStatus": f3SystemLldpV2ManAddrConfigTxPortsADVAExtRowStatus,
       "f3LldpV2ConfigurationADVAExtObjects": f3LldpV2ConfigurationADVAExtObjects,
       "f3LldpMaxNeighborsAction": f3LldpMaxNeighborsAction,
       "snmpIPv6UDPDomain": snmpIPv6UDPDomain,
       "f3RawDataObjects": f3RawDataObjects,
       "f3RawDataServerFtProtocol": f3RawDataServerFtProtocol,
       "f3RawDataServerFtServerName": f3RawDataServerFtServerName,
       "f3RawDataServerFtUserId": f3RawDataServerFtUserId,
       "f3RawDataServerFtPasswd": f3RawDataServerFtPasswd,
       "f3LldpV2RemoteSystemsData": f3LldpV2RemoteSystemsData,
       "f3LldpV2RemExtTable": f3LldpV2RemExtTable,
       "f3LldpV2RemExtEntry": f3LldpV2RemExtEntry,
       "f3LldpV2RemTTL": f3LldpV2RemTTL,
       "cmSystemNotifications": cmSystemNotifications,
       "cmStateChangeTrap": cmStateChangeTrap,
       "cmAttributeValueChangeTrap": cmAttributeValueChangeTrap,
       "cmObjectCreationTrap": cmObjectCreationTrap,
       "cmObjectDeletionTrap": cmObjectDeletionTrap,
       "cmSnmpDyingGaspTrap": cmSnmpDyingGaspTrap,
       "f3DatabaseSyncTrap": f3DatabaseSyncTrap,
       "cmSystemConformance": cmSystemConformance,
       "cmSystemCompliances": cmSystemCompliances,
       "cmSystemCompliance": cmSystemCompliance,
       "cmSystemGroups": cmSystemGroups,
       "cmSystemObjectGroup": cmSystemObjectGroup,
       "cmSystemNotifGroup": cmSystemNotifGroup,
       "cmSystemObjectGroupCmHub": cmSystemObjectGroupCmHub,
       "f3SystemBulkGroups": f3SystemBulkGroups,
       "f3SystemObjectBulkGroup": f3SystemObjectBulkGroup,
       "f3SystemNotifBulkGroup": f3SystemNotifBulkGroup,
       "f3BulkNotifObjects": f3BulkNotifObjects,
       "f3StartNeEventLogIndex": f3StartNeEventLogIndex,
       "f3EndNeEventLogIndex": f3EndNeEventLogIndex,
       "f3SystemBulkNotifications": f3SystemBulkNotifications,
       "f3BulkTrap": f3BulkTrap}
)

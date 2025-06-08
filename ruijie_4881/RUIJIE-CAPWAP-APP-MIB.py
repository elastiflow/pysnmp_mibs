# SNMP MIB module (RUIJIE-CAPWAP-APP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-CAPWAP-APP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:05:44 2025
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

(ruijieDeviceMacAddress,) = mibBuilder.importSymbols(
    "RUIJIE-ENTITY-MIB",
    "ruijieDeviceMacAddress")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ruijieSystemSerialno,) = mibBuilder.importSymbols(
    "RUIJIE-SYSTEM-MIB",
    "ruijieSystemSerialno")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysObjectID,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysObjectID")

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
 TAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieCapwapAppMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87)
)
if mibBuilder.loadTexts:
    ruijieCapwapAppMIB.setRevisions(
        ("2010-06-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieCapwapAppMIBObjects_ObjectIdentity = ObjectIdentity
ruijieCapwapAppMIBObjects = _RuijieCapwapAppMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1)
)
_RuijieAppHeartbeatMIBObjects_ObjectIdentity = ObjectIdentity
ruijieAppHeartbeatMIBObjects = _RuijieAppHeartbeatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 1)
)
_RuijieAppHeartbeatMIBTraps_ObjectIdentity = ObjectIdentity
ruijieAppHeartbeatMIBTraps = _RuijieAppHeartbeatMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 1, 0)
)


class _RuijieAppHeartbeatOnOff_Type(Integer32):
    """Custom type ruijieAppHeartbeatOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_RuijieAppHeartbeatOnOff_Type.__name__ = "Integer32"
_RuijieAppHeartbeatOnOff_Object = MibScalar
ruijieAppHeartbeatOnOff = _RuijieAppHeartbeatOnOff_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 1, 1),
    _RuijieAppHeartbeatOnOff_Type()
)
ruijieAppHeartbeatOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAppHeartbeatOnOff.setStatus("current")


class _RuijieAppHeartbeatPeriod_Type(Integer32):
    """Custom type ruijieAppHeartbeatPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_RuijieAppHeartbeatPeriod_Type.__name__ = "Integer32"
_RuijieAppHeartbeatPeriod_Object = MibScalar
ruijieAppHeartbeatPeriod = _RuijieAppHeartbeatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 1, 2),
    _RuijieAppHeartbeatPeriod_Type()
)
ruijieAppHeartbeatPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAppHeartbeatPeriod.setStatus("current")
_RuijieAppHeartbeatIpAddr_Type = IpAddress
_RuijieAppHeartbeatIpAddr_Object = MibScalar
ruijieAppHeartbeatIpAddr = _RuijieAppHeartbeatIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 1, 3),
    _RuijieAppHeartbeatIpAddr_Type()
)
ruijieAppHeartbeatIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAppHeartbeatIpAddr.setStatus("current")
_RuijieAppHeartbeatTimeStamp_Type = TimeTicks
_RuijieAppHeartbeatTimeStamp_Object = MibScalar
ruijieAppHeartbeatTimeStamp = _RuijieAppHeartbeatTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 1, 4),
    _RuijieAppHeartbeatTimeStamp_Type()
)
ruijieAppHeartbeatTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAppHeartbeatTimeStamp.setStatus("current")
_RuijieAppAdminInfoMIBObjects_ObjectIdentity = ObjectIdentity
ruijieAppAdminInfoMIBObjects = _RuijieAppAdminInfoMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2)
)
_RuijieAppAdminMIBTraps_ObjectIdentity = ObjectIdentity
ruijieAppAdminMIBTraps = _RuijieAppAdminMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2, 0)
)
_RuijieAppAdminInfoTable_Object = MibTable
ruijieAppAdminInfoTable = _RuijieAppAdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieAppAdminInfoTable.setStatus("current")
_RuijieAppAdminInfoEntry_Object = MibTableRow
ruijieAppAdminInfoEntry = _RuijieAppAdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2, 1, 1)
)
ruijieAppAdminInfoEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminName"),
)
if mibBuilder.loadTexts:
    ruijieAppAdminInfoEntry.setStatus("current")


class _RuijieAppAdminName_Type(DisplayString):
    """Custom type ruijieAppAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieAppAdminName_Type.__name__ = "DisplayString"
_RuijieAppAdminName_Object = MibTableColumn
ruijieAppAdminName = _RuijieAppAdminName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2, 1, 1, 1),
    _RuijieAppAdminName_Type()
)
ruijieAppAdminName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAppAdminName.setStatus("current")


class _RuijieAppAdminPwd_Type(DisplayString):
    """Custom type ruijieAppAdminPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieAppAdminPwd_Type.__name__ = "DisplayString"
_RuijieAppAdminPwd_Object = MibTableColumn
ruijieAppAdminPwd = _RuijieAppAdminPwd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2, 1, 1, 2),
    _RuijieAppAdminPwd_Type()
)
ruijieAppAdminPwd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAppAdminPwd.setStatus("current")
_RuijieAppAdminPriLevel_Type = Integer32
_RuijieAppAdminPriLevel_Object = MibTableColumn
ruijieAppAdminPriLevel = _RuijieAppAdminPriLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2, 1, 1, 3),
    _RuijieAppAdminPriLevel_Type()
)
ruijieAppAdminPriLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAppAdminPriLevel.setStatus("current")
_RuijieAppAdminStatus_Type = RowStatus
_RuijieAppAdminStatus_Object = MibTableColumn
ruijieAppAdminStatus = _RuijieAppAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2, 1, 1, 4),
    _RuijieAppAdminStatus_Type()
)
ruijieAppAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAppAdminStatus.setStatus("current")


class _RuijieAppAdminInfoName_Type(DisplayString):
    """Custom type ruijieAppAdminInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieAppAdminInfoName_Type.__name__ = "DisplayString"
_RuijieAppAdminInfoName_Object = MibScalar
ruijieAppAdminInfoName = _RuijieAppAdminInfoName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2, 2),
    _RuijieAppAdminInfoName_Type()
)
ruijieAppAdminInfoName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAppAdminInfoName.setStatus("current")
_RuijieAppAdminInfoIpAddr_Type = IpAddress
_RuijieAppAdminInfoIpAddr_Object = MibScalar
ruijieAppAdminInfoIpAddr = _RuijieAppAdminInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2, 3),
    _RuijieAppAdminInfoIpAddr_Type()
)
ruijieAppAdminInfoIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAppAdminInfoIpAddr.setStatus("current")


class _RuijieAppAdminInfoConfigContext_Type(OctetString):
    """Custom type ruijieAppAdminInfoConfigContext based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_RuijieAppAdminInfoConfigContext_Type.__name__ = "OctetString"
_RuijieAppAdminInfoConfigContext_Object = MibScalar
ruijieAppAdminInfoConfigContext = _RuijieAppAdminInfoConfigContext_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2, 4),
    _RuijieAppAdminInfoConfigContext_Type()
)
ruijieAppAdminInfoConfigContext.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAppAdminInfoConfigContext.setStatus("current")


class _RuijieAppAdminInfoLoginType_Type(DisplayString):
    """Custom type ruijieAppAdminInfoLoginType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieAppAdminInfoLoginType_Type.__name__ = "DisplayString"
_RuijieAppAdminInfoLoginType_Object = MibScalar
ruijieAppAdminInfoLoginType = _RuijieAppAdminInfoLoginType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2, 5),
    _RuijieAppAdminInfoLoginType_Type()
)
ruijieAppAdminInfoLoginType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAppAdminInfoLoginType.setStatus("current")


class _RuijieAppAdminTerminalInfo_Type(DisplayString):
    """Custom type ruijieAppAdminTerminalInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieAppAdminTerminalInfo_Type.__name__ = "DisplayString"
_RuijieAppAdminTerminalInfo_Object = MibScalar
ruijieAppAdminTerminalInfo = _RuijieAppAdminTerminalInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2, 6),
    _RuijieAppAdminTerminalInfo_Type()
)
ruijieAppAdminTerminalInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAppAdminTerminalInfo.setStatus("current")
_RuijieAppAdminLoginFailReason_Type = Integer32
_RuijieAppAdminLoginFailReason_Object = MibScalar
ruijieAppAdminLoginFailReason = _RuijieAppAdminLoginFailReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2, 7),
    _RuijieAppAdminLoginFailReason_Type()
)
ruijieAppAdminLoginFailReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAppAdminLoginFailReason.setStatus("current")


class _RuijieAppAdminTargetLevel_Type(Integer32):
    """Custom type ruijieAppAdminTargetLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RuijieAppAdminTargetLevel_Type.__name__ = "Integer32"
_RuijieAppAdminTargetLevel_Object = MibScalar
ruijieAppAdminTargetLevel = _RuijieAppAdminTargetLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2, 8),
    _RuijieAppAdminTargetLevel_Type()
)
ruijieAppAdminTargetLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAppAdminTargetLevel.setStatus("current")


class _RuijieAppAdminInfoLoginProtocol_Type(DisplayString):
    """Custom type ruijieAppAdminInfoLoginProtocol based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieAppAdminInfoLoginProtocol_Type.__name__ = "DisplayString"
_RuijieAppAdminInfoLoginProtocol_Object = MibScalar
ruijieAppAdminInfoLoginProtocol = _RuijieAppAdminInfoLoginProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2, 9),
    _RuijieAppAdminInfoLoginProtocol_Type()
)
ruijieAppAdminInfoLoginProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAppAdminInfoLoginProtocol.setStatus("current")


class _RuijieAppAdminInfoLoginIPv6_Type(DisplayString):
    """Custom type ruijieAppAdminInfoLoginIPv6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieAppAdminInfoLoginIPv6_Type.__name__ = "DisplayString"
_RuijieAppAdminInfoLoginIPv6_Object = MibScalar
ruijieAppAdminInfoLoginIPv6 = _RuijieAppAdminInfoLoginIPv6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2, 10),
    _RuijieAppAdminInfoLoginIPv6_Type()
)
ruijieAppAdminInfoLoginIPv6.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAppAdminInfoLoginIPv6.setStatus("current")
_RuijieAppPollTimeMIBObjects_ObjectIdentity = ObjectIdentity
ruijieAppPollTimeMIBObjects = _RuijieAppPollTimeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 3)
)
_RuijieAppPollTimeOfLast_Type = TimeTicks
_RuijieAppPollTimeOfLast_Object = MibScalar
ruijieAppPollTimeOfLast = _RuijieAppPollTimeOfLast_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 3, 1),
    _RuijieAppPollTimeOfLast_Type()
)
ruijieAppPollTimeOfLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAppPollTimeOfLast.setStatus("current")
_RuijieAppConfigMIBObjects_ObjectIdentity = ObjectIdentity
ruijieAppConfigMIBObjects = _RuijieAppConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 4)
)
_RuijieAppConfigMIBTraps_ObjectIdentity = ObjectIdentity
ruijieAppConfigMIBTraps = _RuijieAppConfigMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 4, 0)
)


class _RuijieAppRcvToDefConfig_Type(Integer32):
    """Custom type ruijieAppRcvToDefConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reset", 1))
    )


_RuijieAppRcvToDefConfig_Type.__name__ = "Integer32"
_RuijieAppRcvToDefConfig_Object = MibScalar
ruijieAppRcvToDefConfig = _RuijieAppRcvToDefConfig_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 4, 1),
    _RuijieAppRcvToDefConfig_Type()
)
ruijieAppRcvToDefConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAppRcvToDefConfig.setStatus("current")


class _RuijieAppConfigFileName_Type(DisplayString):
    """Custom type ruijieAppConfigFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieAppConfigFileName_Type.__name__ = "DisplayString"
_RuijieAppConfigFileName_Object = MibScalar
ruijieAppConfigFileName = _RuijieAppConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 4, 2),
    _RuijieAppConfigFileName_Type()
)
ruijieAppConfigFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAppConfigFileName.setStatus("current")


class _RuijieAppConfigParseErrReason_Type(DisplayString):
    """Custom type ruijieAppConfigParseErrReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieAppConfigParseErrReason_Type.__name__ = "DisplayString"
_RuijieAppConfigParseErrReason_Object = MibScalar
ruijieAppConfigParseErrReason = _RuijieAppConfigParseErrReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 4, 3),
    _RuijieAppConfigParseErrReason_Type()
)
ruijieAppConfigParseErrReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAppConfigParseErrReason.setStatus("current")
_RuijieAppSyslogMIBObjects_ObjectIdentity = ObjectIdentity
ruijieAppSyslogMIBObjects = _RuijieAppSyslogMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 5)
)
_RuijieAppSyslogSvcEnable_Type = TruthValue
_RuijieAppSyslogSvcEnable_Object = MibScalar
ruijieAppSyslogSvcEnable = _RuijieAppSyslogSvcEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 5, 1),
    _RuijieAppSyslogSvcEnable_Type()
)
ruijieAppSyslogSvcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAppSyslogSvcEnable.setStatus("current")
_RuijieAppSyslogReportEventLevel_Type = Integer32
_RuijieAppSyslogReportEventLevel_Object = MibScalar
ruijieAppSyslogReportEventLevel = _RuijieAppSyslogReportEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 5, 2),
    _RuijieAppSyslogReportEventLevel_Type()
)
ruijieAppSyslogReportEventLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAppSyslogReportEventLevel.setStatus("current")
_RuijieAppSyslogSvrCfgTable_Object = MibTable
ruijieAppSyslogSvrCfgTable = _RuijieAppSyslogSvrCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 5, 3)
)
if mibBuilder.loadTexts:
    ruijieAppSyslogSvrCfgTable.setStatus("current")
_RuijieAppSyslogSvrCfgEntry_Object = MibTableRow
ruijieAppSyslogSvrCfgEntry = _RuijieAppSyslogSvrCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 5, 3, 1)
)
ruijieAppSyslogSvrCfgEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-APP-MIB", "ruijieAppSyslogSvrNetType"),
    (0, "RUIJIE-CAPWAP-APP-MIB", "ruijieAppSyslogSvrNetAddr"),
)
if mibBuilder.loadTexts:
    ruijieAppSyslogSvrCfgEntry.setStatus("current")
_RuijieAppSyslogSvrNetType_Type = InetAddressType
_RuijieAppSyslogSvrNetType_Object = MibTableColumn
ruijieAppSyslogSvrNetType = _RuijieAppSyslogSvrNetType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 5, 3, 1, 1),
    _RuijieAppSyslogSvrNetType_Type()
)
ruijieAppSyslogSvrNetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAppSyslogSvrNetType.setStatus("current")
_RuijieAppSyslogSvrNetAddr_Type = InetAddress
_RuijieAppSyslogSvrNetAddr_Object = MibTableColumn
ruijieAppSyslogSvrNetAddr = _RuijieAppSyslogSvrNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 5, 3, 1, 2),
    _RuijieAppSyslogSvrNetAddr_Type()
)
ruijieAppSyslogSvrNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAppSyslogSvrNetAddr.setStatus("current")
_RuijieAppSyslogSvrNetPort_Type = Unsigned32
_RuijieAppSyslogSvrNetPort_Object = MibTableColumn
ruijieAppSyslogSvrNetPort = _RuijieAppSyslogSvrNetPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 5, 3, 1, 3),
    _RuijieAppSyslogSvrNetPort_Type()
)
ruijieAppSyslogSvrNetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAppSyslogSvrNetPort.setStatus("current")
_RuijieAppSyslogVrfName_Type = DisplayString
_RuijieAppSyslogVrfName_Object = MibTableColumn
ruijieAppSyslogVrfName = _RuijieAppSyslogVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 5, 3, 1, 4),
    _RuijieAppSyslogVrfName_Type()
)
ruijieAppSyslogVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAppSyslogVrfName.setStatus("current")
_RuijieAppSyslogStatus_Type = RowStatus
_RuijieAppSyslogStatus_Object = MibTableColumn
ruijieAppSyslogStatus = _RuijieAppSyslogStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 5, 3, 1, 5),
    _RuijieAppSyslogStatus_Type()
)
ruijieAppSyslogStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAppSyslogStatus.setStatus("current")
_RuijieSyslogServerAddrInfoTable_Object = MibTable
ruijieSyslogServerAddrInfoTable = _RuijieSyslogServerAddrInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 5, 4)
)
if mibBuilder.loadTexts:
    ruijieSyslogServerAddrInfoTable.setStatus("current")
_RuijieSyslogServerAddrInfoEntry_Object = MibTableRow
ruijieSyslogServerAddrInfoEntry = _RuijieSyslogServerAddrInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 5, 4, 1)
)
ruijieSyslogServerAddrInfoEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-APP-MIB", "ruijieSyslogServerIndex"),
)
if mibBuilder.loadTexts:
    ruijieSyslogServerAddrInfoEntry.setStatus("current")
_RuijieSyslogServerIndex_Type = Integer32
_RuijieSyslogServerIndex_Object = MibTableColumn
ruijieSyslogServerIndex = _RuijieSyslogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 5, 4, 1, 1),
    _RuijieSyslogServerIndex_Type()
)
ruijieSyslogServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyslogServerIndex.setStatus("current")
_RuijieSyslogServerAddr_Type = TAddress
_RuijieSyslogServerAddr_Object = MibTableColumn
ruijieSyslogServerAddr = _RuijieSyslogServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 5, 4, 1, 2),
    _RuijieSyslogServerAddr_Type()
)
ruijieSyslogServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSyslogServerAddr.setStatus("current")
_RuijieSyslogServerVrfName_Type = DisplayString
_RuijieSyslogServerVrfName_Object = MibTableColumn
ruijieSyslogServerVrfName = _RuijieSyslogServerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 5, 4, 1, 3),
    _RuijieSyslogServerVrfName_Type()
)
ruijieSyslogServerVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSyslogServerVrfName.setStatus("current")
_RuijieSyslogServerStatus_Type = RowStatus
_RuijieSyslogServerStatus_Object = MibTableColumn
ruijieSyslogServerStatus = _RuijieSyslogServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 5, 4, 1, 4),
    _RuijieSyslogServerStatus_Type()
)
ruijieSyslogServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSyslogServerStatus.setStatus("current")
_RuijieAppTrapActionMIBObjects_ObjectIdentity = ObjectIdentity
ruijieAppTrapActionMIBObjects = _RuijieAppTrapActionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 6)
)


class _RuijieAppTrapActionEnable_Type(Integer32):
    """Custom type ruijieAppTrapActionEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disableSendTrap", 0),
          ("enableSendTrap", 1))
    )


_RuijieAppTrapActionEnable_Type.__name__ = "Integer32"
_RuijieAppTrapActionEnable_Object = MibScalar
ruijieAppTrapActionEnable = _RuijieAppTrapActionEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 6, 1),
    _RuijieAppTrapActionEnable_Type()
)
ruijieAppTrapActionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAppTrapActionEnable.setStatus("current")
_RuijieAppTrapActionTable_Object = MibTable
ruijieAppTrapActionTable = _RuijieAppTrapActionTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 6, 2)
)
if mibBuilder.loadTexts:
    ruijieAppTrapActionTable.setStatus("current")
_RuijieAppTrapActionEntry_Object = MibTableRow
ruijieAppTrapActionEntry = _RuijieAppTrapActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 6, 2, 1)
)
ruijieAppTrapActionEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-APP-MIB", "ruijieAppTrapType"),
)
if mibBuilder.loadTexts:
    ruijieAppTrapActionEntry.setStatus("current")


class _RuijieAppTrapType_Type(Integer32):
    """Custom type ruijieAppTrapType based on Integer32"""
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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202)
        )
    )
    namedValues = NamedValues(
        *(("gencoldstart", 1),
          ("genwarmstart", 2),
          ("genlinkdown", 3),
          ("genlinkup", 4),
          ("genauthenfail", 5),
          ("genegpnbloss", 6),
          ("spenewroot", 7),
          ("spetopchange", 8),
          ("spehardchange", 9),
          ("speportsecuviolation", 10),
          ("spestormviolation", 11),
          ("spemacnotification", 12),
          ("spevrrpnewmaster", 13),
          ("spevrrpauthfailure", 14),
          ("spepowerstatetrans", 15),
          ("spefanstatetrans", 16),
          ("speospf", 17),
          ("speospfvifstatechange", 18),
          ("speospfnbrstatechange", 19),
          ("speospfvifnbrstatechange", 20),
          ("speospfifconfigerror", 21),
          ("speospfvifconfigerror", 22),
          ("speospfifauthfailure", 23),
          ("speospfvifauthfailure", 24),
          ("speospfifrxbadpacket", 25),
          ("speospfvifrxbadpacket", 26),
          ("speospftxretransmit", 27),
          ("speospfviftxretransmit", 28),
          ("speospforiginatelsa", 29),
          ("speospfmaxagelsa", 30),
          ("speospflsdboverflow", 31),
          ("speospflsdbapproachingoverflow", 32),
          ("speospfifstatechange", 33),
          ("spebgpestablished", 34),
          ("spebgpbackwardtransition", 35),
          ("speisisdatabaseoverload", 36),
          ("speisismanualaddressdrop", 37),
          ("speisiscorruptedlspdetected", 38),
          ("speisisattempttoexceedmaxseq", 39),
          ("speisisidlenmismatch", 40),
          ("speisismaxareaaddrmismatch", 41),
          ("speisisownlsppurge", 42),
          ("speisisseqnumberskip", 43),
          ("speisisauthtypefailure", 44),
          ("speisisauthfailure", 45),
          ("speisisversionskew", 46),
          ("speisisareamismatch", 47),
          ("speisisrejectedadj", 48),
          ("speisislsptoolargetopropagate", 49),
          ("speisisoriglspbufsizemismatch", 50),
          ("speisisprotocolsupportedmismatch", 51),
          ("speisisadjchange", 52),
          ("spepim", 53),
          ("speigmp", 54),
          ("spedvmrp", 55),
          ("speentitychange", 56),
          ("specluster", 57),
          ("spedetectipviolation", 58),
          ("spelinestate", 59),
          ("spesysguard", 60),
          ("spernfpmsgtrap", 61),
          ("sperrmclientsfailedtrap", 62),
          ("sperrmloadfailedtrap", 63),
          ("sperrmnoisefailedtrap", 64),
          ("sperrminterferencefailedtrap", 65),
          ("sperrmperformancefailedtrap", 66),
          ("sperrmclientspasstrap", 67),
          ("sperrmloadpasstrap", 68),
          ("sperrmnoisepasstrap", 69),
          ("sperrminterferencepasstrap", 70),
          ("sperrmperformancepasstrap", 71),
          ("sperrmchannelchangetrap", 72),
          ("sperrmtxpowerchangetrap", 73),
          ("sperrmleaderachangetrap", 74),
          ("sperrmleaderbchangetrap", 75),
          ("sperrmdfsfreecountatrap", 76),
          ("sperrmdfsfreecountbtrap", 77),
          ("sperrmneighborapintertrap", 78),
          ("sperrmstationintertrap", 79),
          ("sperrmotherdiveceintertrap", 80),
          ("rmonalarmfallingtrap", 81),
          ("rmonalarmrisingtrap", 82),
          ("smpframerelaytrap", 83),
          ("priventitytrans", 84),
          ("privtemperaturetrans", 85),
          ("speipv6ifstatechange", 86),
          ("psmachashconflicttrap", 87),
          ("privwebauthuserleave", 88),
          ("radiusauthserverdowntrap", 89),
          ("radiusacctserverdowntrap", 90),
          ("configurationerrortrap", 91),
          ("cpuusagetoohightrap", 92),
          ("cpuusagetoohighrecovtrap", 93),
          ("memusagetoohightrap", 94),
          ("memusagetoohighrecovtrap", 95),
          ("systmcoldstarttrap", 96),
          ("ipaddrchangetrap", 97),
          ("apmtworkmodechgtrap", 98),
          ("apswupdatefailtrap", 99),
          ("ssidkeyconflicttrap", 100),
          ("fatapheartbeattrap", 101),
          ("acconfigurationerrortrap", 102),
          ("accpuusagetoohightrap", 103),
          ("accpuusagetoohighrecovtrap", 104),
          ("acmemusagetoohightrap", 105),
          ("acmemusagetoohighrecovtrap", 106),
          ("acofflinetrap", 107),
          ("aconlinetrap", 108),
          ("acapmtworkmodechgtrap", 109),
          ("acapswupdatefailtrap", 110),
          ("acssidkeyconflicttrap", 111),
          ("acfatapheartbeattrap", 112),
          ("staauthfailtrap", 113),
          ("staassofailtrap", 114),
          ("acstaauthfailtrap", 115),
          ("acstaassofailtrap", 116),
          ("invalidcertinvadetrap", 117),
          ("repaccacktrap", 118),
          ("tamperattacktrap", 119),
          ("lowersafeattacktrap", 120),
          ("addrredirectiontrap", 121),
          ("acinvalidcertinvadetrap", 122),
          ("acrepaccacktrap", 123),
          ("actamperattacktrap", 124),
          ("aclowersafeattacktrap", 125),
          ("acaddrredirectiontrap", 126),
          ("widsieee80211connect", 127),
          ("widsieee80211disconnect", 128),
          ("widsieee80211reauthentication", 129),
          ("widsieee80211authenticationfailure", 130),
          ("widsieee80211connectfailure", 131),
          ("apcointerfdetectedtrap", 132),
          ("apcointerfcleartrap", 133),
          ("apnerborinterfdetectedtrap", 134),
          ("apneiborinterfcleartrap", 135),
          ("stainterfdetectedtrap", 136),
          ("stainterfcleartrap", 137),
          ("otherdeviceinterfdetectedtrap", 138),
          ("otherdevinterfcleartrap", 139),
          ("radiodowntrap", 140),
          ("radiodownrecovtrap", 141),
          ("apstafulltrap", 142),
          ("apstafullrecovertrap", 143),
          ("apmtrdochanlchgtrap", 144),
          ("acapcointerfdetectedtrap", 145),
          ("acapcointerfcleartrap", 146),
          ("acapnerborinterfdetectedtrap", 147),
          ("acapneiborinterfcleartrap", 148),
          ("acstainterfdetectedtrap", 149),
          ("acstainterfcleartrap", 150),
          ("acotherdeviceinterfdetectedtrap", 151),
          ("acotherdevinterfcleartrap", 152),
          ("acradiodowntrap", 153),
          ("acradiodownrecovtrap", 154),
          ("acapstafulltrap", 155),
          ("acapstafullrecovertrap", 156),
          ("acapmtrdochanlchgtrap", 157),
          ("acspeciousdevicedetecttrap", 158),
          ("acrxpackage", 159),
          ("accpuusage", 160),
          ("capwapbasechanup", 161),
          ("capwapbasechandown", 162),
          ("capwapbasedecrypterrorreport", 163),
          ("capwapbasejoinfail", 164),
          ("capwapbaseimageupgradefail", 165),
          ("capwapbaseconifgmsgerror", 166),
          ("capwapbaseradiooperstatu", 167),
          ("capwapbaseauthenfail", 168),
          ("apmgmtaptimestamp", 169),
          ("apmgmtstaoper", 170),
          ("apmgmtmbchange", 171),
          ("apmgmtapswupdtfail", 172),
          ("widswarninginfo", 173),
          ("privcmccportalunavailable", 174),
          ("privipaddrchange", 175),
          ("dhcppoolexhaust", 176),
          ("dhcppoolnoexhaust", 177),
          ("speheartbeatperiodtrap", 178),
          ("tftpupgradefailed", 179),
          ("syscpuhigh", 180),
          ("syscpuhighrecov", 181),
          ("systemperaturehigh", 182),
          ("systemperaturehighrecov", 183),
          ("sysmemoryhigh", 184),
          ("sysmemoryhighrecov", 185),
          ("speconfigmodifytrap", 186),
          ("speconfigparseerrtrap", 187),
          ("apmgmtstaactoverthrehold", 188),
          ("apmgmtstadisactoverthredhold", 189),
          ("apmgmtstaroamtotaloverthredhlod", 190),
          ("apmgmtstaroamoerminoverthredhold", 191),
          ("apmgmtapwritebuffero", 192),
          ("apmgmtacheartbeat", 193),
          ("apmgmtacpowerstatus", 194),
          ("radiusauthserverrecovertrap", 195),
          ("radiusacctserverrecovertrap", 196),
          ("privcmccportalavailable", 197),
          ("sysapcpuhigh", 198),
          ("sysapcpuhighrecov", 199),
          ("sysapmemoryhigh", 200),
          ("sysapmemoryhighrecov", 201),
          ("syssystemreset", 202))
    )


_RuijieAppTrapType_Type.__name__ = "Integer32"
_RuijieAppTrapType_Object = MibTableColumn
ruijieAppTrapType = _RuijieAppTrapType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 6, 2, 1, 1),
    _RuijieAppTrapType_Type()
)
ruijieAppTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAppTrapType.setStatus("current")


class _RuijieAppTrapAction_Type(Integer32):
    """Custom type ruijieAppTrapAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_RuijieAppTrapAction_Type.__name__ = "Integer32"
_RuijieAppTrapAction_Object = MibTableColumn
ruijieAppTrapAction = _RuijieAppTrapAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 6, 2, 1, 2),
    _RuijieAppTrapAction_Type()
)
ruijieAppTrapAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAppTrapAction.setStatus("current")
_RuijieAppTrapDescr_Type = DisplayString
_RuijieAppTrapDescr_Object = MibTableColumn
ruijieAppTrapDescr = _RuijieAppTrapDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 6, 2, 1, 3),
    _RuijieAppTrapDescr_Type()
)
ruijieAppTrapDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAppTrapDescr.setStatus("current")
_RuijieZCMMIBObjects_ObjectIdentity = ObjectIdentity
ruijieZCMMIBObjects = _RuijieZCMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 7)
)
_RuijieZCMMIBTraps_ObjectIdentity = ObjectIdentity
ruijieZCMMIBTraps = _RuijieZCMMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 7, 0)
)
_RuijieAssignedIPAddress_Type = IpAddress
_RuijieAssignedIPAddress_Object = MibScalar
ruijieAssignedIPAddress = _RuijieAssignedIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 7, 1),
    _RuijieAssignedIPAddress_Type()
)
ruijieAssignedIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAssignedIPAddress.setStatus("current")


class _RuijieNeedConfiguration_Type(Integer32):
    """Custom type ruijieNeedConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RuijieNeedConfiguration_Type.__name__ = "Integer32"
_RuijieNeedConfiguration_Object = MibScalar
ruijieNeedConfiguration = _RuijieNeedConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 7, 2),
    _RuijieNeedConfiguration_Type()
)
ruijieNeedConfiguration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieNeedConfiguration.setStatus("current")
_RuijieCapwapAppMIBConformance_ObjectIdentity = ObjectIdentity
ruijieCapwapAppMIBConformance = _RuijieCapwapAppMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 2)
)
_RuijieCapwapAppMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieCapwapAppMIBCompliances = _RuijieCapwapAppMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 2, 1)
)
_RuijieCapwapAppMIBGroups_ObjectIdentity = ObjectIdentity
ruijieCapwapAppMIBGroups = _RuijieCapwapAppMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 2, 2)
)

# Managed Objects groups

ruijieCapwapAppMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 2, 2, 1)
)
ruijieCapwapAppMIBGroup.setObjects(
      *(("RUIJIE-CAPWAP-APP-MIB", "ruijieAppHeartbeatOnOff"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppHeartbeatPeriod"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppHeartbeatIpAddr"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppHeartbeatTimeStamp"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminName"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminPwd"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminPriLevel"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminStatus"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppPollTimeOfLast"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppRcvToDefConfig"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppConfigFileName"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppConfigParseErrReason"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppSyslogSvcEnable"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppSyslogReportEventLevel"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppSyslogSvrNetType"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppSyslogSvrNetAddr"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppSyslogSvrNetPort"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppSyslogVrfName"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppSyslogStatus"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieSyslogServerAddr"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieSyslogServerVrfName"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieSyslogServerStatus"))
)
if mibBuilder.loadTexts:
    ruijieCapwapAppMIBGroup.setStatus("current")


# Notification objects

ruijieAppHeartbeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 1, 0, 1)
)
ruijieAppHeartbeatTrap.setObjects(
      *(("RUIJIE-CAPWAP-APP-MIB", "ruijieAppHeartbeatIpAddr"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppHeartbeatTimeStamp"))
)
if mibBuilder.loadTexts:
    ruijieAppHeartbeatTrap.setStatus(
        "current"
    )

ruijieAppAdminLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2, 0, 1)
)
ruijieAppAdminLoginTrap.setObjects(
      *(("RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminInfoName"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminInfoIpAddr"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminInfoLoginType"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminInfoLoginProtocol"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminInfoLoginIPv6"))
)
if mibBuilder.loadTexts:
    ruijieAppAdminLoginTrap.setStatus(
        "current"
    )

ruijieAppAdminModifyConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2, 0, 2)
)
ruijieAppAdminModifyConfigTrap.setObjects(
      *(("RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminInfoName"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminInfoIpAddr"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminInfoConfigContext"))
)
if mibBuilder.loadTexts:
    ruijieAppAdminModifyConfigTrap.setStatus(
        "current"
    )

ruijieAppAdminLoginFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2, 0, 3)
)
ruijieAppAdminLoginFailTrap.setObjects(
      *(("RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminInfoName"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminInfoIpAddr"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminTerminalInfo"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminLoginFailReason"))
)
if mibBuilder.loadTexts:
    ruijieAppAdminLoginFailTrap.setStatus(
        "current"
    )

ruijieAppAdminEnableFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 2, 0, 4)
)
ruijieAppAdminEnableFailTrap.setObjects(
      *(("RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminInfoName"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminInfoIpAddr"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminTerminalInfo"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppAdminTargetLevel"))
)
if mibBuilder.loadTexts:
    ruijieAppAdminEnableFailTrap.setStatus(
        "current"
    )

ruijieAppConfigModifyFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 4, 0, 1)
)
if mibBuilder.loadTexts:
    ruijieAppConfigModifyFileTrap.setStatus(
        "current"
    )

ruijieAppConfigParseErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 4, 0, 2)
)
ruijieAppConfigParseErrTrap.setObjects(
      *(("RUIJIE-CAPWAP-APP-MIB", "ruijieAppConfigFileName"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAppConfigParseErrReason"))
)
if mibBuilder.loadTexts:
    ruijieAppConfigParseErrTrap.setStatus(
        "current"
    )

ruijieZCMNotifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 1, 7, 0, 1)
)
ruijieZCMNotifyTrap.setObjects(
      *(("RUIJIE-SYSTEM-MIB", "ruijieSystemSerialno"),
        ("RUIJIE-ENTITY-MIB", "ruijieDeviceMacAddress"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieAssignedIPAddress"),
        ("RUIJIE-CAPWAP-APP-MIB", "ruijieNeedConfiguration"),
        ("SNMPv2-MIB", "sysObjectID"))
)
if mibBuilder.loadTexts:
    ruijieZCMNotifyTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijieCapwapAppMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 87, 2, 1, 1)
)
ruijieCapwapAppMIBCompliance.setObjects(
    ("RUIJIE-CAPWAP-APP-MIB", "ruijieCapwapAppMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieCapwapAppMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-CAPWAP-APP-MIB",
    **{"ruijieCapwapAppMIB": ruijieCapwapAppMIB,
       "ruijieCapwapAppMIBObjects": ruijieCapwapAppMIBObjects,
       "ruijieAppHeartbeatMIBObjects": ruijieAppHeartbeatMIBObjects,
       "ruijieAppHeartbeatMIBTraps": ruijieAppHeartbeatMIBTraps,
       "ruijieAppHeartbeatTrap": ruijieAppHeartbeatTrap,
       "ruijieAppHeartbeatOnOff": ruijieAppHeartbeatOnOff,
       "ruijieAppHeartbeatPeriod": ruijieAppHeartbeatPeriod,
       "ruijieAppHeartbeatIpAddr": ruijieAppHeartbeatIpAddr,
       "ruijieAppHeartbeatTimeStamp": ruijieAppHeartbeatTimeStamp,
       "ruijieAppAdminInfoMIBObjects": ruijieAppAdminInfoMIBObjects,
       "ruijieAppAdminMIBTraps": ruijieAppAdminMIBTraps,
       "ruijieAppAdminLoginTrap": ruijieAppAdminLoginTrap,
       "ruijieAppAdminModifyConfigTrap": ruijieAppAdminModifyConfigTrap,
       "ruijieAppAdminLoginFailTrap": ruijieAppAdminLoginFailTrap,
       "ruijieAppAdminEnableFailTrap": ruijieAppAdminEnableFailTrap,
       "ruijieAppAdminInfoTable": ruijieAppAdminInfoTable,
       "ruijieAppAdminInfoEntry": ruijieAppAdminInfoEntry,
       "ruijieAppAdminName": ruijieAppAdminName,
       "ruijieAppAdminPwd": ruijieAppAdminPwd,
       "ruijieAppAdminPriLevel": ruijieAppAdminPriLevel,
       "ruijieAppAdminStatus": ruijieAppAdminStatus,
       "ruijieAppAdminInfoName": ruijieAppAdminInfoName,
       "ruijieAppAdminInfoIpAddr": ruijieAppAdminInfoIpAddr,
       "ruijieAppAdminInfoConfigContext": ruijieAppAdminInfoConfigContext,
       "ruijieAppAdminInfoLoginType": ruijieAppAdminInfoLoginType,
       "ruijieAppAdminTerminalInfo": ruijieAppAdminTerminalInfo,
       "ruijieAppAdminLoginFailReason": ruijieAppAdminLoginFailReason,
       "ruijieAppAdminTargetLevel": ruijieAppAdminTargetLevel,
       "ruijieAppAdminInfoLoginProtocol": ruijieAppAdminInfoLoginProtocol,
       "ruijieAppAdminInfoLoginIPv6": ruijieAppAdminInfoLoginIPv6,
       "ruijieAppPollTimeMIBObjects": ruijieAppPollTimeMIBObjects,
       "ruijieAppPollTimeOfLast": ruijieAppPollTimeOfLast,
       "ruijieAppConfigMIBObjects": ruijieAppConfigMIBObjects,
       "ruijieAppConfigMIBTraps": ruijieAppConfigMIBTraps,
       "ruijieAppConfigModifyFileTrap": ruijieAppConfigModifyFileTrap,
       "ruijieAppConfigParseErrTrap": ruijieAppConfigParseErrTrap,
       "ruijieAppRcvToDefConfig": ruijieAppRcvToDefConfig,
       "ruijieAppConfigFileName": ruijieAppConfigFileName,
       "ruijieAppConfigParseErrReason": ruijieAppConfigParseErrReason,
       "ruijieAppSyslogMIBObjects": ruijieAppSyslogMIBObjects,
       "ruijieAppSyslogSvcEnable": ruijieAppSyslogSvcEnable,
       "ruijieAppSyslogReportEventLevel": ruijieAppSyslogReportEventLevel,
       "ruijieAppSyslogSvrCfgTable": ruijieAppSyslogSvrCfgTable,
       "ruijieAppSyslogSvrCfgEntry": ruijieAppSyslogSvrCfgEntry,
       "ruijieAppSyslogSvrNetType": ruijieAppSyslogSvrNetType,
       "ruijieAppSyslogSvrNetAddr": ruijieAppSyslogSvrNetAddr,
       "ruijieAppSyslogSvrNetPort": ruijieAppSyslogSvrNetPort,
       "ruijieAppSyslogVrfName": ruijieAppSyslogVrfName,
       "ruijieAppSyslogStatus": ruijieAppSyslogStatus,
       "ruijieSyslogServerAddrInfoTable": ruijieSyslogServerAddrInfoTable,
       "ruijieSyslogServerAddrInfoEntry": ruijieSyslogServerAddrInfoEntry,
       "ruijieSyslogServerIndex": ruijieSyslogServerIndex,
       "ruijieSyslogServerAddr": ruijieSyslogServerAddr,
       "ruijieSyslogServerVrfName": ruijieSyslogServerVrfName,
       "ruijieSyslogServerStatus": ruijieSyslogServerStatus,
       "ruijieAppTrapActionMIBObjects": ruijieAppTrapActionMIBObjects,
       "ruijieAppTrapActionEnable": ruijieAppTrapActionEnable,
       "ruijieAppTrapActionTable": ruijieAppTrapActionTable,
       "ruijieAppTrapActionEntry": ruijieAppTrapActionEntry,
       "ruijieAppTrapType": ruijieAppTrapType,
       "ruijieAppTrapAction": ruijieAppTrapAction,
       "ruijieAppTrapDescr": ruijieAppTrapDescr,
       "ruijieZCMMIBObjects": ruijieZCMMIBObjects,
       "ruijieZCMMIBTraps": ruijieZCMMIBTraps,
       "ruijieZCMNotifyTrap": ruijieZCMNotifyTrap,
       "ruijieAssignedIPAddress": ruijieAssignedIPAddress,
       "ruijieNeedConfiguration": ruijieNeedConfiguration,
       "ruijieCapwapAppMIBConformance": ruijieCapwapAppMIBConformance,
       "ruijieCapwapAppMIBCompliances": ruijieCapwapAppMIBCompliances,
       "ruijieCapwapAppMIBCompliance": ruijieCapwapAppMIBCompliance,
       "ruijieCapwapAppMIBGroups": ruijieCapwapAppMIBGroups,
       "ruijieCapwapAppMIBGroup": ruijieCapwapAppMIBGroup}
)

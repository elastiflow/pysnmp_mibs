# SNMP MIB module (CISCO-LWAPP-AP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-AP-EXT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:47:34 2025
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

(bsnDot11EssSecurityAuthType,) = mibBuilder.importSymbols(
    "AIRESPACE-WIRELESS-MIB",
    "bsnDot11EssSecurityAuthType")

(cLApDataEncryptionStatus,
 cLApDot11IfSlotId,
 cLApDot11RadioChannelNumber,
 cLApDot11RadioCurrentChannel,
 cLApDot11RadioMACAddress,
 cLApEthernetIfSlotId,
 cLApIfSmtDot11Bssid,
 cLApLastRebootReason,
 cLApName,
 cLApRSSI,
 cLApSysMacAddress) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApDataEncryptionStatus",
    "cLApDot11IfSlotId",
    "cLApDot11RadioChannelNumber",
    "cLApDot11RadioCurrentChannel",
    "cLApDot11RadioMACAddress",
    "cLApEthernetIfSlotId",
    "cLApIfSmtDot11Bssid",
    "cLApLastRebootReason",
    "cLApName",
    "cLApRSSI",
    "cLApSysMacAddress")

(cldcApMacAddress,
 cldcClientMacAddress,
 cldcClientSSID) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-MIB",
    "cldcApMacAddress",
    "cldcClientMacAddress",
    "cldcClientSSID")

(cldHtDot11nBand,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-MIB",
    "cldHtDot11nBand")

(cLRFProfileName,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-RF-MIB",
    "cLRFProfileName")

(clsPortDot1dBasePort,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-SYS-MIB",
    "clsPortDot1dBasePort")

(CLDot11Channel,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLDot11Channel")

(cLWlanIndex,
 cLWlanSsid) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanIndex",
    "cLWlanSsid")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappApExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998)
)
if mibBuilder.loadTexts:
    ciscoLwappApExtMIB.setRevisions(
        ("2017-04-20 00:00",
         "2013-05-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CLSwitch(TextualConvention, Integer32):
    status = "current"
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



class CLExtApDisassocReason(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 1),
          ("missedEchoFromAp", 2),
          ("wtpReset", 3),
          ("msgTimerExpiry", 4),
          ("heartBeatExpiry", 5))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoLwappApExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappApExtMIBNotifs = _CiscoLwappApExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 0)
)
_CiscoLwappApExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappApExtMIBObjects = _CiscoLwappApExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1)
)
_CiscoLwappApExtConfig_ObjectIdentity = ObjectIdentity
ciscoLwappApExtConfig = _CiscoLwappApExtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1)
)
_ClExtSys_ObjectIdentity = ObjectIdentity
clExtSys = _ClExtSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 1)
)


class _ClExtNMHeartBeatEnable_Type(CLSwitch):
    """Custom type clExtNMHeartBeatEnable based on CLSwitch"""
    defaultValue = 0


_ClExtNMHeartBeatEnable_Type.__name__ = "CLSwitch"
_ClExtNMHeartBeatEnable_Object = MibScalar
clExtNMHeartBeatEnable = _ClExtNMHeartBeatEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 1, 1),
    _ClExtNMHeartBeatEnable_Type()
)
clExtNMHeartBeatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clExtNMHeartBeatEnable.setStatus("current")


class _ClExtAgentResetSystem_Type(Integer32):
    """Custom type clExtAgentResetSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ClExtAgentResetSystem_Type.__name__ = "Integer32"
_ClExtAgentResetSystem_Object = MibScalar
clExtAgentResetSystem = _ClExtAgentResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 1, 2),
    _ClExtAgentResetSystem_Type()
)
clExtAgentResetSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clExtAgentResetSystem.setStatus("current")
_ClExtAgentClearConfig_Type = TruthValue
_ClExtAgentClearConfig_Object = MibScalar
clExtAgentClearConfig = _ClExtAgentClearConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 1, 3),
    _ClExtAgentClearConfig_Type()
)
clExtAgentClearConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clExtAgentClearConfig.setStatus("current")


class _ClExtSystemCurrentTime_Type(DisplayString):
    """Custom type clExtSystemCurrentTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClExtSystemCurrentTime_Type.__name__ = "DisplayString"
_ClExtSystemCurrentTime_Object = MibScalar
clExtSystemCurrentTime = _ClExtSystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 1, 4),
    _ClExtSystemCurrentTime_Type()
)
clExtSystemCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clExtSystemCurrentTime.setStatus("current")
_ClExtPortModeConfigTable_Object = MibTable
clExtPortModeConfigTable = _ClExtPortModeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    clExtPortModeConfigTable.setStatus("current")
_ClExtPortModeConfigEntry_Object = MibTableRow
clExtPortModeConfigEntry = _ClExtPortModeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 1, 5, 1)
)
clExtPortModeConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-SYS-MIB", "clsPortDot1dBasePort"),
)
if mibBuilder.loadTexts:
    clExtPortModeConfigEntry.setStatus("current")


class _ClExtPortOperStatus_Type(Integer32):
    """Custom type clExtPortOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("admindown", 4))
    )


_ClExtPortOperStatus_Type.__name__ = "Integer32"
_ClExtPortOperStatus_Object = MibTableColumn
clExtPortOperStatus = _ClExtPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 1, 5, 1, 1),
    _ClExtPortOperStatus_Type()
)
clExtPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtPortOperStatus.setStatus("current")
_ClExtSysMaxNewConnectionPerSecond_Type = Integer32
_ClExtSysMaxNewConnectionPerSecond_Object = MibScalar
clExtSysMaxNewConnectionPerSecond = _ClExtSysMaxNewConnectionPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 1, 6),
    _ClExtSysMaxNewConnectionPerSecond_Type()
)
clExtSysMaxNewConnectionPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtSysMaxNewConnectionPerSecond.setStatus("current")
_ClExtIf_ObjectIdentity = ObjectIdentity
clExtIf = _ClExtIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 2)
)
_ClExtIfTable_Object = MibTable
clExtIfTable = _ClExtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    clExtIfTable.setStatus("current")
_ClExtIfEntry_Object = MibTableRow
clExtIfEntry = _ClExtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 2, 1, 1)
)
clExtIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    clExtIfEntry.setStatus("current")
_ClExtIfSpeed_Type = Gauge32
_ClExtIfSpeed_Object = MibTableColumn
clExtIfSpeed = _ClExtIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 2, 1, 1, 1),
    _ClExtIfSpeed_Type()
)
clExtIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtIfSpeed.setStatus("current")
_ClExtIfSinceLastChange_Type = TimeTicks
_ClExtIfSinceLastChange_Object = MibTableColumn
clExtIfSinceLastChange = _ClExtIfSinceLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 2, 1, 1, 2),
    _ClExtIfSinceLastChange_Type()
)
clExtIfSinceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtIfSinceLastChange.setStatus("current")
_ClExtAp_ObjectIdentity = ObjectIdentity
clExtAp = _ClExtAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3)
)
_ClExtApTable_Object = MibTable
clExtApTable = _ClExtApTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    clExtApTable.setStatus("current")
_ClExtApEntry_Object = MibTableRow
clExtApEntry = _ClExtApEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 1, 1)
)
clExtApEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    clExtApEntry.setStatus("current")


class _ClExtApRealTimeStatsModeEnabled_Type(CLSwitch):
    """Custom type clExtApRealTimeStatsModeEnabled based on CLSwitch"""
    defaultValue = 0


_ClExtApRealTimeStatsModeEnabled_Type.__name__ = "CLSwitch"
_ClExtApRealTimeStatsModeEnabled_Object = MibTableColumn
clExtApRealTimeStatsModeEnabled = _ClExtApRealTimeStatsModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 1, 1, 1),
    _ClExtApRealTimeStatsModeEnabled_Type()
)
clExtApRealTimeStatsModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clExtApRealTimeStatsModeEnabled.setStatus("current")


class _ClExtApMonitorMode_Type(Integer32):
    """Custom type clExtApMonitorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("monitor", 1),
          ("semimonitor", 2))
    )


_ClExtApMonitorMode_Type.__name__ = "Integer32"
_ClExtApMonitorMode_Object = MibTableColumn
clExtApMonitorMode = _ClExtApMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 1, 1, 2),
    _ClExtApMonitorMode_Type()
)
clExtApMonitorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clExtApMonitorMode.setStatus("current")
_ClExtApSysManufacturer_Type = SnmpAdminString
_ClExtApSysManufacturer_Object = MibTableColumn
clExtApSysManufacturer = _ClExtApSysManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 1, 1, 3),
    _ClExtApSysManufacturer_Type()
)
clExtApSysManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtApSysManufacturer.setStatus("current")
_ClExtApSysSoftwareName_Type = SnmpAdminString
_ClExtApSysSoftwareName_Object = MibTableColumn
clExtApSysSoftwareName = _ClExtApSysSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 1, 1, 4),
    _ClExtApSysSoftwareName_Type()
)
clExtApSysSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtApSysSoftwareName.setStatus("current")
_ClExtApSysSoftwareVersion_Type = SnmpAdminString
_ClExtApSysSoftwareVersion_Object = MibTableColumn
clExtApSysSoftwareVersion = _ClExtApSysSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 1, 1, 5),
    _ClExtApSysSoftwareVersion_Type()
)
clExtApSysSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtApSysSoftwareVersion.setStatus("current")
_ClExtApSysSoftwareVendor_Type = SnmpAdminString
_ClExtApSysSoftwareVendor_Object = MibTableColumn
clExtApSysSoftwareVendor = _ClExtApSysSoftwareVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 1, 1, 6),
    _ClExtApSysSoftwareVendor_Type()
)
clExtApSysSoftwareVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtApSysSoftwareVendor.setStatus("current")


class _ClExtApQosMinBandwidth_Type(Integer32):
    """Custom type clExtApQosMinBandwidth based on Integer32"""
    defaultValue = 80


_ClExtApQosMinBandwidth_Type.__name__ = "Integer32"
_ClExtApQosMinBandwidth_Object = MibTableColumn
clExtApQosMinBandwidth = _ClExtApQosMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 1, 1, 7),
    _ClExtApQosMinBandwidth_Type()
)
clExtApQosMinBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clExtApQosMinBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    clExtApQosMinBandwidth.setUnits("Mbps")
_ClExtApTotalPhyInterfaceCount_Type = Unsigned32
_ClExtApTotalPhyInterfaceCount_Object = MibTableColumn
clExtApTotalPhyInterfaceCount = _ClExtApTotalPhyInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 1, 1, 8),
    _ClExtApTotalPhyInterfaceCount_Type()
)
clExtApTotalPhyInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtApTotalPhyInterfaceCount.setStatus("current")
_ClExtApName_Type = SnmpAdminString
_ClExtApName_Object = MibTableColumn
clExtApName = _ClExtApName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 1, 1, 9),
    _ClExtApName_Type()
)
clExtApName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clExtApName.setStatus("current")
_ClExtApDot11IfTable_Object = MibTable
clExtApDot11IfTable = _ClExtApDot11IfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    clExtApDot11IfTable.setStatus("current")
_ClExtApDot11IfEntry_Object = MibTableRow
clExtApDot11IfEntry = _ClExtApDot11IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 2, 1)
)
clExtApDot11IfEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    clExtApDot11IfEntry.setStatus("current")


class _ClExtAp11nChannelBandwidth_Type(Integer32):
    """Custom type clExtAp11nChannelBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forty", 1),
          ("twenty", 2))
    )


_ClExtAp11nChannelBandwidth_Type.__name__ = "Integer32"
_ClExtAp11nChannelBandwidth_Object = MibTableColumn
clExtAp11nChannelBandwidth = _ClExtAp11nChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 2, 1, 1),
    _ClExtAp11nChannelBandwidth_Type()
)
clExtAp11nChannelBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clExtAp11nChannelBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    clExtAp11nChannelBandwidth.setUnits("mhz")
_ClExtApDot11IfIANAType_Type = IANAifType
_ClExtApDot11IfIANAType_Object = MibTableColumn
clExtApDot11IfIANAType = _ClExtApDot11IfIANAType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 2, 1, 2),
    _ClExtApDot11IfIANAType_Type()
)
clExtApDot11IfIANAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtApDot11IfIANAType.setStatus("current")
_ClExtApIfPhyChannelAssignment_Type = CLSwitch
_ClExtApIfPhyChannelAssignment_Object = MibTableColumn
clExtApIfPhyChannelAssignment = _ClExtApIfPhyChannelAssignment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 2, 1, 3),
    _ClExtApIfPhyChannelAssignment_Type()
)
clExtApIfPhyChannelAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clExtApIfPhyChannelAssignment.setStatus("current")
_ClExtApDot11RadioStatsRxByteCount_Type = Counter64
_ClExtApDot11RadioStatsRxByteCount_Object = MibTableColumn
clExtApDot11RadioStatsRxByteCount = _ClExtApDot11RadioStatsRxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 2, 1, 4),
    _ClExtApDot11RadioStatsRxByteCount_Type()
)
clExtApDot11RadioStatsRxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtApDot11RadioStatsRxByteCount.setStatus("current")
if mibBuilder.loadTexts:
    clExtApDot11RadioStatsRxByteCount.setUnits("bytes")
_ClExtApDot11RadioStatsTxByteCount_Type = Counter64
_ClExtApDot11RadioStatsTxByteCount_Object = MibTableColumn
clExtApDot11RadioStatsTxByteCount = _ClExtApDot11RadioStatsTxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 2, 1, 5),
    _ClExtApDot11RadioStatsTxByteCount_Type()
)
clExtApDot11RadioStatsTxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtApDot11RadioStatsTxByteCount.setStatus("current")
if mibBuilder.loadTexts:
    clExtApDot11RadioStatsTxByteCount.setUnits("bytes")


class _ClExtApDot11WirelessModeSupported_Type(Integer32):
    """Custom type clExtApDot11WirelessModeSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ClExtApDot11WirelessModeSupported_Type.__name__ = "Integer32"
_ClExtApDot11WirelessModeSupported_Object = MibTableColumn
clExtApDot11WirelessModeSupported = _ClExtApDot11WirelessModeSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 2, 1, 6),
    _ClExtApDot11WirelessModeSupported_Type()
)
clExtApDot11WirelessModeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtApDot11WirelessModeSupported.setStatus("current")


class _ClExtApDot11IfAdminStatus_Type(Integer32):
    """Custom type clExtApDot11IfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_ClExtApDot11IfAdminStatus_Type.__name__ = "Integer32"
_ClExtApDot11IfAdminStatus_Object = MibTableColumn
clExtApDot11IfAdminStatus = _ClExtApDot11IfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 2, 1, 7),
    _ClExtApDot11IfAdminStatus_Type()
)
clExtApDot11IfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clExtApDot11IfAdminStatus.setStatus("current")


class _ClExtApDot11IfOperStatus_Type(Integer32):
    """Custom type clExtApDot11IfOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("admindown", 4))
    )


_ClExtApDot11IfOperStatus_Type.__name__ = "Integer32"
_ClExtApDot11IfOperStatus_Object = MibTableColumn
clExtApDot11IfOperStatus = _ClExtApDot11IfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 2, 1, 8),
    _ClExtApDot11IfOperStatus_Type()
)
clExtApDot11IfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtApDot11IfOperStatus.setStatus("current")
_CLExtAPDot11IfRTSThreshold_Type = Integer32
_CLExtAPDot11IfRTSThreshold_Object = MibTableColumn
cLExtAPDot11IfRTSThreshold = _CLExtAPDot11IfRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 2, 1, 9),
    _CLExtAPDot11IfRTSThreshold_Type()
)
cLExtAPDot11IfRTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLExtAPDot11IfRTSThreshold.setStatus("current")
_ClExtApDot11RadioStatsTable_Object = MibTable
clExtApDot11RadioStatsTable = _ClExtApDot11RadioStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    clExtApDot11RadioStatsTable.setStatus("current")
_ClExtApDot11RadioStatsEntry_Object = MibTableRow
clExtApDot11RadioStatsEntry = _ClExtApDot11RadioStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 3, 1)
)
clExtApDot11RadioStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    clExtApDot11RadioStatsEntry.setStatus("current")
_ClExtApDot11RadioStatsRetryFrameCount_Type = Counter64
_ClExtApDot11RadioStatsRetryFrameCount_Object = MibTableColumn
clExtApDot11RadioStatsRetryFrameCount = _ClExtApDot11RadioStatsRetryFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 3, 1, 1),
    _ClExtApDot11RadioStatsRetryFrameCount_Type()
)
clExtApDot11RadioStatsRetryFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtApDot11RadioStatsRetryFrameCount.setStatus("current")
if mibBuilder.loadTexts:
    clExtApDot11RadioStatsRetryFrameCount.setUnits("frames")
_ClExtApDot11RadioStatsRetryPacketCount_Type = Counter64
_ClExtApDot11RadioStatsRetryPacketCount_Object = MibTableColumn
clExtApDot11RadioStatsRetryPacketCount = _ClExtApDot11RadioStatsRetryPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 3, 1, 2),
    _ClExtApDot11RadioStatsRetryPacketCount_Type()
)
clExtApDot11RadioStatsRetryPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtApDot11RadioStatsRetryPacketCount.setStatus("current")
if mibBuilder.loadTexts:
    clExtApDot11RadioStatsRetryPacketCount.setUnits("packets")
_ClExtApDot11RadioStatsRxErrorPacketCount_Type = Counter32
_ClExtApDot11RadioStatsRxErrorPacketCount_Object = MibTableColumn
clExtApDot11RadioStatsRxErrorPacketCount = _ClExtApDot11RadioStatsRxErrorPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 3, 1, 3),
    _ClExtApDot11RadioStatsRxErrorPacketCount_Type()
)
clExtApDot11RadioStatsRxErrorPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtApDot11RadioStatsRxErrorPacketCount.setStatus("current")
if mibBuilder.loadTexts:
    clExtApDot11RadioStatsRxErrorPacketCount.setUnits("packets")
_ClExtApEthernetIfTable_Object = MibTable
clExtApEthernetIfTable = _ClExtApEthernetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    clExtApEthernetIfTable.setStatus("current")
_ClExtApEthernetIfEntry_Object = MibTableRow
clExtApEthernetIfEntry = _ClExtApEthernetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 4, 1)
)
clExtApEthernetIfEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApEthernetIfSlotId"),
)
if mibBuilder.loadTexts:
    clExtApEthernetIfEntry.setStatus("current")


class _ClExtApEthernetIfOperStatus_Type(Integer32):
    """Custom type clExtApEthernetIfOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("admindown", 4))
    )


_ClExtApEthernetIfOperStatus_Type.__name__ = "Integer32"
_ClExtApEthernetIfOperStatus_Object = MibTableColumn
clExtApEthernetIfOperStatus = _ClExtApEthernetIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 4, 1, 1),
    _ClExtApEthernetIfOperStatus_Type()
)
clExtApEthernetIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtApEthernetIfOperStatus.setStatus("current")
_ClExtApEthernetIfRxBcastPkts_Type = Counter32
_ClExtApEthernetIfRxBcastPkts_Object = MibTableColumn
clExtApEthernetIfRxBcastPkts = _ClExtApEthernetIfRxBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 4, 1, 2),
    _ClExtApEthernetIfRxBcastPkts_Type()
)
clExtApEthernetIfRxBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtApEthernetIfRxBcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    clExtApEthernetIfRxBcastPkts.setUnits("packets")
_ClExtApEthernetIfRxMcastPkts_Type = Counter32
_ClExtApEthernetIfRxMcastPkts_Object = MibTableColumn
clExtApEthernetIfRxMcastPkts = _ClExtApEthernetIfRxMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 4, 1, 3),
    _ClExtApEthernetIfRxMcastPkts_Type()
)
clExtApEthernetIfRxMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtApEthernetIfRxMcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    clExtApEthernetIfRxMcastPkts.setUnits("packets")
_ClExtApEthernetIfTxBcastPkts_Type = Counter32
_ClExtApEthernetIfTxBcastPkts_Object = MibTableColumn
clExtApEthernetIfTxBcastPkts = _ClExtApEthernetIfTxBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 4, 1, 4),
    _ClExtApEthernetIfTxBcastPkts_Type()
)
clExtApEthernetIfTxBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtApEthernetIfTxBcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    clExtApEthernetIfTxBcastPkts.setUnits("packets")
_ClExtApEthernetIfTxMcastPkts_Type = Counter32
_ClExtApEthernetIfTxMcastPkts_Object = MibTableColumn
clExtApEthernetIfTxMcastPkts = _ClExtApEthernetIfTxMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 4, 1, 5),
    _ClExtApEthernetIfTxMcastPkts_Type()
)
clExtApEthernetIfTxMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtApEthernetIfTxMcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    clExtApEthernetIfTxMcastPkts.setUnits("packets")
_CLApOperationInfoTable_Object = MibTable
cLApOperationInfoTable = _CLApOperationInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cLApOperationInfoTable.setStatus("current")
_CLApOperationInfoEntry_Object = MibTableRow
cLApOperationInfoEntry = _CLApOperationInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 5, 1)
)
cLApOperationInfoEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-EXT-MIB", "cLApOperationSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLApOperationInfoEntry.setStatus("current")
_CLApOperationSysMacAddress_Type = MacAddress
_CLApOperationSysMacAddress_Object = MibTableColumn
cLApOperationSysMacAddress = _CLApOperationSysMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 5, 1, 1),
    _CLApOperationSysMacAddress_Type()
)
cLApOperationSysMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApOperationSysMacAddress.setStatus("current")


class _CLApOperationStatus_Type(Integer32):
    """Custom type cLApOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disassociated", 0),
          ("associated", 1))
    )


_CLApOperationStatus_Type.__name__ = "Integer32"
_CLApOperationStatus_Object = MibTableColumn
cLApOperationStatus = _CLApOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 3, 5, 1, 2),
    _CLApOperationStatus_Type()
)
cLApOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApOperationStatus.setStatus("current")
_ClExtWlan_ObjectIdentity = ObjectIdentity
clExtWlan = _ClExtWlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 4)
)
_ClExtWlanConfigTable_Object = MibTable
clExtWlanConfigTable = _ClExtWlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    clExtWlanConfigTable.setStatus("current")
_ClExtWlanConfigEntry_Object = MibTableRow
clExtWlanConfigEntry = _ClExtWlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 4, 1, 1)
)
clExtWlanConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    clExtWlanConfigEntry.setStatus("current")


class _ClExtWlanAdminStatus_Type(TruthValue):
    """Custom type clExtWlanAdminStatus based on TruthValue"""
    defaultValue = 2


_ClExtWlanAdminStatus_Type.__name__ = "TruthValue"
_ClExtWlanAdminStatus_Object = MibTableColumn
clExtWlanAdminStatus = _ClExtWlanAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 4, 1, 1, 1),
    _ClExtWlanAdminStatus_Type()
)
clExtWlanAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clExtWlanAdminStatus.setStatus("current")


class _ClExtWlanBroadcastSsidEnable_Type(TruthValue):
    """Custom type clExtWlanBroadcastSsidEnable based on TruthValue"""
    defaultValue = 1


_ClExtWlanBroadcastSsidEnable_Type.__name__ = "TruthValue"
_ClExtWlanBroadcastSsidEnable_Object = MibTableColumn
clExtWlanBroadcastSsidEnable = _ClExtWlanBroadcastSsidEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 4, 1, 1, 2),
    _ClExtWlanBroadcastSsidEnable_Type()
)
clExtWlanBroadcastSsidEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clExtWlanBroadcastSsidEnable.setStatus("current")


class _ClExtWlanLoadBalancingMode_Type(Integer32):
    """Custom type clExtWlanLoadBalancingMode based on Integer32"""
    defaultValue = 2

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
          ("uplinkUsage", 1),
          ("clientCount", 2))
    )


_ClExtWlanLoadBalancingMode_Type.__name__ = "Integer32"
_ClExtWlanLoadBalancingMode_Object = MibTableColumn
clExtWlanLoadBalancingMode = _ClExtWlanLoadBalancingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 4, 1, 1, 3),
    _ClExtWlanLoadBalancingMode_Type()
)
clExtWlanLoadBalancingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clExtWlanLoadBalancingMode.setStatus("current")


class _ClExtWlanP2PBlocking_Type(TruthValue):
    """Custom type clExtWlanP2PBlocking based on TruthValue"""
    defaultValue = 2


_ClExtWlanP2PBlocking_Type.__name__ = "TruthValue"
_ClExtWlanP2PBlocking_Object = MibTableColumn
clExtWlanP2PBlocking = _ClExtWlanP2PBlocking_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 4, 1, 1, 4),
    _ClExtWlanP2PBlocking_Type()
)
clExtWlanP2PBlocking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clExtWlanP2PBlocking.setStatus("current")


class _ClExtWlanSecurityAuthType_Type(Integer32):
    """Custom type clExtWlanSecurityAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              128)
        )
    )
    namedValues = NamedValues(
        *(("authOpen", 0),
          ("authSharedKey", 1),
          ("authCiscoLeap", 128))
    )


_ClExtWlanSecurityAuthType_Type.__name__ = "Integer32"
_ClExtWlanSecurityAuthType_Object = MibTableColumn
clExtWlanSecurityAuthType = _ClExtWlanSecurityAuthType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 4, 1, 1, 5),
    _ClExtWlanSecurityAuthType_Type()
)
clExtWlanSecurityAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clExtWlanSecurityAuthType.setStatus("current")


class _ClExtWlanDot11Auth_Type(Integer32):
    """Custom type clExtWlanDot11Auth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("opensystem", 0),
          ("sharekey", 1))
    )


_ClExtWlanDot11Auth_Type.__name__ = "Integer32"
_ClExtWlanDot11Auth_Object = MibTableColumn
clExtWlanDot11Auth = _ClExtWlanDot11Auth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 4, 1, 1, 6),
    _ClExtWlanDot11Auth_Type()
)
clExtWlanDot11Auth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clExtWlanDot11Auth.setStatus("current")


class _ClExtWlanSecurity_Type(Integer32):
    """Custom type clExtWlanSecurity based on Integer32"""
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
        *(("none", 0),
          ("wpa", 1),
          ("wpa2", 2),
          ("wapi", 3))
    )


_ClExtWlanSecurity_Type.__name__ = "Integer32"
_ClExtWlanSecurity_Object = MibTableColumn
clExtWlanSecurity = _ClExtWlanSecurity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 4, 1, 1, 7),
    _ClExtWlanSecurity_Type()
)
clExtWlanSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clExtWlanSecurity.setStatus("current")


class _ClExtWlanAuthenMode_Type(Integer32):
    """Custom type clExtWlanAuthenMode based on Integer32"""
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
        *(("none", 0),
          ("psk", 1),
          ("radius", 2),
          ("wapi-cer", 3))
    )


_ClExtWlanAuthenMode_Type.__name__ = "Integer32"
_ClExtWlanAuthenMode_Object = MibTableColumn
clExtWlanAuthenMode = _ClExtWlanAuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 4, 1, 1, 8),
    _ClExtWlanAuthenMode_Type()
)
clExtWlanAuthenMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clExtWlanAuthenMode.setStatus("current")


class _ClExtWlanSecurityCiphers_Type(Integer32):
    """Custom type clExtWlanSecurityCiphers based on Integer32"""
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
          ("wep40", 1),
          ("wep104", 2),
          ("tkip", 3),
          ("aesccmp", 4),
          ("wpi-sms4", 5))
    )


_ClExtWlanSecurityCiphers_Type.__name__ = "Integer32"
_ClExtWlanSecurityCiphers_Object = MibTableColumn
clExtWlanSecurityCiphers = _ClExtWlanSecurityCiphers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 4, 1, 1, 9),
    _ClExtWlanSecurityCiphers_Type()
)
clExtWlanSecurityCiphers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clExtWlanSecurityCiphers.setStatus("current")


class _ClExtWepCipherKeyIndex_Type(Integer32):
    """Custom type clExtWepCipherKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ClExtWepCipherKeyIndex_Type.__name__ = "Integer32"
_ClExtWepCipherKeyIndex_Object = MibTableColumn
clExtWepCipherKeyIndex = _ClExtWepCipherKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 4, 1, 1, 10),
    _ClExtWepCipherKeyIndex_Type()
)
clExtWepCipherKeyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clExtWepCipherKeyIndex.setStatus("current")


class _ClExtWepCipherKeyValue_Type(OctetString):
    """Custom type clExtWepCipherKeyValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 26),
    )


_ClExtWepCipherKeyValue_Type.__name__ = "OctetString"
_ClExtWepCipherKeyValue_Object = MibTableColumn
clExtWepCipherKeyValue = _ClExtWepCipherKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 4, 1, 1, 11),
    _ClExtWepCipherKeyValue_Type()
)
clExtWepCipherKeyValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clExtWepCipherKeyValue.setStatus("current")


class _ClExtWepCipherKeyCharType_Type(Integer32):
    """Custom type clExtWepCipherKeyCharType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("hex", 2),
          ("ascii", 3))
    )


_ClExtWepCipherKeyCharType_Type.__name__ = "Integer32"
_ClExtWepCipherKeyCharType_Object = MibTableColumn
clExtWepCipherKeyCharType = _ClExtWepCipherKeyCharType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 4, 1, 1, 12),
    _ClExtWepCipherKeyCharType_Type()
)
clExtWepCipherKeyCharType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clExtWepCipherKeyCharType.setStatus("current")
_ClExtDot11Client_ObjectIdentity = ObjectIdentity
clExtDot11Client = _ClExtDot11Client_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 5)
)
_ClExtClientTable_Object = MibTable
clExtClientTable = _ClExtClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    clExtClientTable.setStatus("current")
_ClExtClientEntry_Object = MibTableRow
clExtClientEntry = _ClExtClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 5, 1, 1)
)
clExtClientEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    clExtClientEntry.setStatus("current")


class _ClExtClientProtocol_Type(Integer32):
    """Custom type clExtClientProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11b", 2),
          ("dot11g", 4),
          ("dot11n5", 8),
          ("dot11n24", 16))
    )


_ClExtClientProtocol_Type.__name__ = "Integer32"
_ClExtClientProtocol_Object = MibTableColumn
clExtClientProtocol = _ClExtClientProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 5, 1, 1, 1),
    _ClExtClientProtocol_Type()
)
clExtClientProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtClientProtocol.setStatus("current")


class _ClExtClientPowerSaveMode_Type(Integer32):
    """Custom type clExtClientPowerSaveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("powersave", 1))
    )


_ClExtClientPowerSaveMode_Type.__name__ = "Integer32"
_ClExtClientPowerSaveMode_Object = MibTableColumn
clExtClientPowerSaveMode = _ClExtClientPowerSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 5, 1, 1, 2),
    _ClExtClientPowerSaveMode_Type()
)
clExtClientPowerSaveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtClientPowerSaveMode.setStatus("current")
_ClExtClientUpTime_Type = TimeTicks
_ClExtClientUpTime_Object = MibTableColumn
clExtClientUpTime = _ClExtClientUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 5, 1, 1, 3),
    _ClExtClientUpTime_Type()
)
clExtClientUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtClientUpTime.setStatus("current")
_ClExtClientAuthFailReason_Type = SnmpAdminString
_ClExtClientAuthFailReason_Object = MibTableColumn
clExtClientAuthFailReason = _ClExtClientAuthFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 5, 1, 1, 4),
    _ClExtClientAuthFailReason_Type()
)
clExtClientAuthFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtClientAuthFailReason.setStatus("current")
_ClExtClientRxThroughput_Type = Unsigned32
_ClExtClientRxThroughput_Object = MibTableColumn
clExtClientRxThroughput = _ClExtClientRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 5, 1, 1, 5),
    _ClExtClientRxThroughput_Type()
)
clExtClientRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtClientRxThroughput.setStatus("current")
if mibBuilder.loadTexts:
    clExtClientRxThroughput.setUnits("bit/s")
_ClExtClientTxThroughput_Type = Unsigned32
_ClExtClientTxThroughput_Object = MibTableColumn
clExtClientTxThroughput = _ClExtClientTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 5, 1, 1, 6),
    _ClExtClientTxThroughput_Type()
)
clExtClientTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtClientTxThroughput.setStatus("current")
if mibBuilder.loadTexts:
    clExtClientTxThroughput.setUnits("bit/s")
_ClExtDot11_ObjectIdentity = ObjectIdentity
clExtDot11 = _ClExtDot11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 6)
)
_ClExtHtMacOperationsTable_Object = MibTable
clExtHtMacOperationsTable = _ClExtHtMacOperationsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    clExtHtMacOperationsTable.setStatus("current")
_ClExtHtMacOperationsEntry_Object = MibTableRow
clExtHtMacOperationsEntry = _ClExtHtMacOperationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 6, 1, 1)
)
clExtHtMacOperationsEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-MIB", "cldHtDot11nBand"),
)
if mibBuilder.loadTexts:
    clExtHtMacOperationsEntry.setStatus("current")


class _ClExtHtDot11nAmpduEnable_Type(CLSwitch):
    """Custom type clExtHtDot11nAmpduEnable based on CLSwitch"""
    defaultValue = 1


_ClExtHtDot11nAmpduEnable_Type.__name__ = "CLSwitch"
_ClExtHtDot11nAmpduEnable_Object = MibTableColumn
clExtHtDot11nAmpduEnable = _ClExtHtDot11nAmpduEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 6, 1, 1, 1),
    _ClExtHtDot11nAmpduEnable_Type()
)
clExtHtDot11nAmpduEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clExtHtDot11nAmpduEnable.setStatus("current")


class _ClExtHtDot11nGuardIntervalEnable_Type(CLSwitch):
    """Custom type clExtHtDot11nGuardIntervalEnable based on CLSwitch"""
    defaultValue = 1


_ClExtHtDot11nGuardIntervalEnable_Type.__name__ = "CLSwitch"
_ClExtHtDot11nGuardIntervalEnable_Object = MibTableColumn
clExtHtDot11nGuardIntervalEnable = _ClExtHtDot11nGuardIntervalEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 6, 1, 1, 2),
    _ClExtHtDot11nGuardIntervalEnable_Type()
)
clExtHtDot11nGuardIntervalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clExtHtDot11nGuardIntervalEnable.setStatus("current")
_ClExtRF_ObjectIdentity = ObjectIdentity
clExtRF = _ClExtRF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 7)
)
_ClExtRFProfileTable_Object = MibTable
clExtRFProfileTable = _ClExtRFProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    clExtRFProfileTable.setStatus("current")
_ClExtRFProfileEntry_Object = MibTableRow
clExtRFProfileEntry = _ClExtRFProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 7, 1, 1)
)
clExtRFProfileEntry.setIndexNames(
    (0, "CISCO-LWAPP-RF-MIB", "cLRFProfileName"),
)
if mibBuilder.loadTexts:
    clExtRFProfileEntry.setStatus("current")


class _ClExtRFProfileWirelessMode_Type(Unsigned32):
    """Custom type clExtRFProfileWirelessMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ClExtRFProfileWirelessMode_Type.__name__ = "Unsigned32"
_ClExtRFProfileWirelessMode_Object = MibTableColumn
clExtRFProfileWirelessMode = _ClExtRFProfileWirelessMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 7, 1, 1, 1),
    _ClExtRFProfileWirelessMode_Type()
)
clExtRFProfileWirelessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clExtRFProfileWirelessMode.setStatus("current")
_ClExtSecurity_ObjectIdentity = ObjectIdentity
clExtSecurity = _ClExtSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 8)
)
_ClExtAbnormalClientSecurityTable_Object = MibTable
clExtAbnormalClientSecurityTable = _ClExtAbnormalClientSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    clExtAbnormalClientSecurityTable.setStatus("current")
_ClExtAbnormalClientSecurityEntry_Object = MibTableRow
clExtAbnormalClientSecurityEntry = _ClExtAbnormalClientSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 8, 1, 1)
)
clExtAbnormalClientSecurityEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-EXT-MIB", "clExtSecurityType"),
)
if mibBuilder.loadTexts:
    clExtAbnormalClientSecurityEntry.setStatus("current")


class _ClExtSecurityType_Type(Integer32):
    """Custom type clExtSecurityType based on Integer32"""
    defaultValue = 1

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
        *(("open", 1),
          ("wepPsk", 2),
          ("peapSim", 3),
          ("webAuth", 4))
    )


_ClExtSecurityType_Type.__name__ = "Integer32"
_ClExtSecurityType_Object = MibTableColumn
clExtSecurityType = _ClExtSecurityType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 8, 1, 1, 1),
    _ClExtSecurityType_Type()
)
clExtSecurityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clExtSecurityType.setStatus("current")
_ClExtAbnormalOfflineClientCount_Type = Counter32
_ClExtAbnormalOfflineClientCount_Object = MibTableColumn
clExtAbnormalOfflineClientCount = _ClExtAbnormalOfflineClientCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 1, 8, 1, 1, 2),
    _ClExtAbnormalOfflineClientCount_Type()
)
clExtAbnormalOfflineClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clExtAbnormalOfflineClientCount.setStatus("current")
_CiscoLwappApExtStats_ObjectIdentity = ObjectIdentity
ciscoLwappApExtStats = _CiscoLwappApExtStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 1, 2)
)
_CiscoLwappApExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappApExtMIBConform = _CiscoLwappApExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 2)
)
_CiscoLwappApExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappApExtMIBCompliances = _CiscoLwappApExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 2, 1)
)
_CiscoLwappApExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappApExtMIBGroups = _CiscoLwappApExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 2, 2)
)
_CiscoLwappApExtMIBNotifObjects_ObjectIdentity = ObjectIdentity
ciscoLwappApExtMIBNotifObjects = _CiscoLwappApExtMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 3)
)
_CLExtApDisassocReason_Type = CLExtApDisassocReason
_CLExtApDisassocReason_Object = MibScalar
cLExtApDisassocReason = _CLExtApDisassocReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 3, 1),
    _CLExtApDisassocReason_Type()
)
cLExtApDisassocReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLExtApDisassocReason.setStatus("current")
_CLExtDot11ClientAssocFailReason_Type = DisplayString
_CLExtDot11ClientAssocFailReason_Object = MibScalar
cLExtDot11ClientAssocFailReason = _CLExtDot11ClientAssocFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 3, 2),
    _CLExtDot11ClientAssocFailReason_Type()
)
cLExtDot11ClientAssocFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLExtDot11ClientAssocFailReason.setStatus("current")
_CLExtApDetectedMacAddress_Type = MacAddress
_CLExtApDetectedMacAddress_Object = MibScalar
cLExtApDetectedMacAddress = _CLExtApDetectedMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 3, 3),
    _CLExtApDetectedMacAddress_Type()
)
cLExtApDetectedMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLExtApDetectedMacAddress.setStatus("current")
_CLExtApDetectedChannel_Type = CLDot11Channel
_CLExtApDetectedChannel_Object = MibScalar
cLExtApDetectedChannel = _CLExtApDetectedChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 3, 4),
    _CLExtApDetectedChannel_Type()
)
cLExtApDetectedChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLExtApDetectedChannel.setStatus("current")
_CLExtApDectedSsid_Type = SnmpAdminString
_CLExtApDectedSsid_Object = MibScalar
cLExtApDectedSsid = _CLExtApDectedSsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 3, 5),
    _CLExtApDectedSsid_Type()
)
cLExtApDectedSsid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLExtApDectedSsid.setStatus("current")

# Managed Objects groups

ciscoLwappApExtMIBConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 2, 2, 1)
)
ciscoLwappApExtMIBConfigGroup.setObjects(
      *(("CISCO-LWAPP-AP-EXT-MIB", "clExtApMonitorMode"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApRealTimeStatsModeEnabled"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApQosMinBandwidth"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApName"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtAp11nChannelBandwidth"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApIfPhyChannelAssignment"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApDot11IfAdminStatus"),
        ("CISCO-LWAPP-AP-EXT-MIB", "cLExtAPDot11IfRTSThreshold"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtWepCipherKeyIndex"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtWepCipherKeyValue"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtWepCipherKeyCharType"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtHtDot11nAmpduEnable"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtHtDot11nGuardIntervalEnable"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtRFProfileWirelessMode"))
)
if mibBuilder.loadTexts:
    ciscoLwappApExtMIBConfigGroup.setStatus("current")

ciscoLwappApExtMIBStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 2, 2, 3)
)
ciscoLwappApExtMIBStatusGroup.setObjects(
      *(("CISCO-LWAPP-AP-EXT-MIB", "clExtApSysManufacturer"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApSysSoftwareName"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApSysSoftwareVersion"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApSysSoftwareVendor"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApTotalPhyInterfaceCount"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApDot11IfIANAType"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApDot11RadioStatsRxByteCount"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApDot11RadioStatsTxByteCount"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApDot11WirelessModeSupported"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApDot11IfOperStatus"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApDot11RadioStatsRetryFrameCount"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApDot11RadioStatsRetryPacketCount"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApDot11RadioStatsRxErrorPacketCount"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApEthernetIfOperStatus"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApEthernetIfRxBcastPkts"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApEthernetIfRxMcastPkts"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApEthernetIfTxBcastPkts"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtApEthernetIfTxMcastPkts"),
        ("CISCO-LWAPP-AP-EXT-MIB", "cLApOperationStatus"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtClientProtocol"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtClientPowerSaveMode"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtClientUpTime"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtClientAuthFailReason"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtClientRxThroughput"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtClientTxThroughput"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtAbnormalOfflineClientCount"))
)
if mibBuilder.loadTexts:
    ciscoLwappApExtMIBStatusGroup.setStatus("current")


# Notification objects

ciscoLwappApAssociatedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 0, 1)
)
ciscoLwappApAssociatedNotify.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApLastRebootReason"),
        ("CISCO-LWAPP-AP-MIB", "cLApDataEncryptionStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappApAssociatedNotify.setStatus(
        "current"
    )

ciscoLwappApDisassociated = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 0, 2)
)
ciscoLwappApDisassociated.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-EXT-MIB", "cLExtApDisassocReason"))
)
if mibBuilder.loadTexts:
    ciscoLwappApDisassociated.setStatus(
        "current"
    )

ciscoLwappExtDot11ClientAuthenticationFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 0, 3)
)
ciscoLwappExtDot11ClientAuthenticationFailTrap.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcApMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSSID"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfSmtDot11Bssid"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssSecurityAuthType"),
        ("CISCO-LWAPP-AP-EXT-MIB", "clExtClientAuthFailReason"))
)
if mibBuilder.loadTexts:
    ciscoLwappExtDot11ClientAuthenticationFailTrap.setStatus(
        "current"
    )

ciscoLwappExtDot11ClientAssocFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 0, 4)
)
ciscoLwappExtDot11ClientAssocFailTrap.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanSsid"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfSmtDot11Bssid"),
        ("CISCO-LWAPP-AP-EXT-MIB", "cLExtDot11ClientAssocFailReason"))
)
if mibBuilder.loadTexts:
    ciscoLwappExtDot11ClientAssocFailTrap.setStatus(
        "current"
    )

ciscoLwappExtAdjChannelOverRssiDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 0, 5)
)
ciscoLwappExtAdjChannelOverRssiDetected.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-EXT-MIB", "cLExtApDetectedMacAddress"),
        ("CISCO-LWAPP-AP-EXT-MIB", "cLExtApDetectedChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApRSSI"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioCurrentChannel"))
)
if mibBuilder.loadTexts:
    ciscoLwappExtAdjChannelOverRssiDetected.setStatus(
        "current"
    )

ciscoLwappExtAdjChannelOverRssiRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 0, 6)
)
ciscoLwappExtAdjChannelOverRssiRemoved.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-EXT-MIB", "cLExtApDetectedMacAddress"),
        ("CISCO-LWAPP-AP-EXT-MIB", "cLExtApDetectedChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioCurrentChannel"))
)
if mibBuilder.loadTexts:
    ciscoLwappExtAdjChannelOverRssiRemoved.setStatus(
        "current"
    )

ciscoLwappExtCurrentChannelOverRssiDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 0, 7)
)
ciscoLwappExtCurrentChannelOverRssiDetected.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-EXT-MIB", "cLExtApDetectedMacAddress"),
        ("CISCO-LWAPP-AP-EXT-MIB", "cLExtApDetectedChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApRSSI"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioCurrentChannel"))
)
if mibBuilder.loadTexts:
    ciscoLwappExtCurrentChannelOverRssiDetected.setStatus(
        "current"
    )

ciscoLwappExtCurrentChannelOverRssiRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 0, 8)
)
ciscoLwappExtCurrentChannelOverRssiRemoved.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-EXT-MIB", "cLExtApDetectedMacAddress"),
        ("CISCO-LWAPP-AP-EXT-MIB", "cLExtApDetectedChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioCurrentChannel"))
)
if mibBuilder.loadTexts:
    ciscoLwappExtCurrentChannelOverRssiRemoved.setStatus(
        "current"
    )

ciscoLwappExtClientOverRssiDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 0, 9)
)
ciscoLwappExtClientOverRssiDetected.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApDot11RadioMACAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioChannelNumber"),
        ("CISCO-LWAPP-AP-EXT-MIB", "cLExtApDetectedMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfSmtDot11Bssid"),
        ("CISCO-LWAPP-AP-EXT-MIB", "cLExtApDetectedChannel"))
)
if mibBuilder.loadTexts:
    ciscoLwappExtClientOverRssiDetected.setStatus(
        "current"
    )

ciscoLwappExtClientOverRssiRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 0, 10)
)
ciscoLwappExtClientOverRssiRemoved.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApDot11RadioMACAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioChannelNumber"),
        ("CISCO-LWAPP-AP-EXT-MIB", "cLExtApDetectedMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfSmtDot11Bssid"),
        ("CISCO-LWAPP-AP-EXT-MIB", "cLExtApDetectedChannel"))
)
if mibBuilder.loadTexts:
    ciscoLwappExtClientOverRssiRemoved.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappApExtMIBNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 2, 2, 2)
)
ciscoLwappApExtMIBNotifsGroup.setObjects(
      *(("CISCO-LWAPP-AP-EXT-MIB", "ciscoLwappApAssociatedNotify"),
        ("CISCO-LWAPP-AP-EXT-MIB", "ciscoLwappApDisassociated"),
        ("CISCO-LWAPP-AP-EXT-MIB", "ciscoLwappExtDot11ClientAuthenticationFailTrap"),
        ("CISCO-LWAPP-AP-EXT-MIB", "ciscoLwappExtDot11ClientAssocFailTrap"),
        ("CISCO-LWAPP-AP-EXT-MIB", "ciscoLwappExtAdjChannelOverRssiDetected"),
        ("CISCO-LWAPP-AP-EXT-MIB", "ciscoLwappExtAdjChannelOverRssiRemoved"),
        ("CISCO-LWAPP-AP-EXT-MIB", "ciscoLwappExtCurrentChannelOverRssiDetected"),
        ("CISCO-LWAPP-AP-EXT-MIB", "ciscoLwappExtCurrentChannelOverRssiRemoved"),
        ("CISCO-LWAPP-AP-EXT-MIB", "ciscoLwappExtClientOverRssiDetected"),
        ("CISCO-LWAPP-AP-EXT-MIB", "ciscoLwappExtClientOverRssiRemoved"))
)
if mibBuilder.loadTexts:
    ciscoLwappApExtMIBNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappApExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 9998, 2, 1, 1)
)
ciscoLwappApExtMIBCompliance.setObjects(
      *(("CISCO-LWAPP-AP-EXT-MIB", "ciscoLwappApExtMIBConfigGroup"),
        ("CISCO-LWAPP-AP-EXT-MIB", "ciscoLwappApExtMIBNotifsGroup"),
        ("CISCO-LWAPP-AP-EXT-MIB", "ciscoLwappApExtMIBStatusGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappApExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-AP-EXT-MIB",
    **{"CLSwitch": CLSwitch,
       "CLExtApDisassocReason": CLExtApDisassocReason,
       "ciscoLwappApExtMIB": ciscoLwappApExtMIB,
       "ciscoLwappApExtMIBNotifs": ciscoLwappApExtMIBNotifs,
       "ciscoLwappApAssociatedNotify": ciscoLwappApAssociatedNotify,
       "ciscoLwappApDisassociated": ciscoLwappApDisassociated,
       "ciscoLwappExtDot11ClientAuthenticationFailTrap": ciscoLwappExtDot11ClientAuthenticationFailTrap,
       "ciscoLwappExtDot11ClientAssocFailTrap": ciscoLwappExtDot11ClientAssocFailTrap,
       "ciscoLwappExtAdjChannelOverRssiDetected": ciscoLwappExtAdjChannelOverRssiDetected,
       "ciscoLwappExtAdjChannelOverRssiRemoved": ciscoLwappExtAdjChannelOverRssiRemoved,
       "ciscoLwappExtCurrentChannelOverRssiDetected": ciscoLwappExtCurrentChannelOverRssiDetected,
       "ciscoLwappExtCurrentChannelOverRssiRemoved": ciscoLwappExtCurrentChannelOverRssiRemoved,
       "ciscoLwappExtClientOverRssiDetected": ciscoLwappExtClientOverRssiDetected,
       "ciscoLwappExtClientOverRssiRemoved": ciscoLwappExtClientOverRssiRemoved,
       "ciscoLwappApExtMIBObjects": ciscoLwappApExtMIBObjects,
       "ciscoLwappApExtConfig": ciscoLwappApExtConfig,
       "clExtSys": clExtSys,
       "clExtNMHeartBeatEnable": clExtNMHeartBeatEnable,
       "clExtAgentResetSystem": clExtAgentResetSystem,
       "clExtAgentClearConfig": clExtAgentClearConfig,
       "clExtSystemCurrentTime": clExtSystemCurrentTime,
       "clExtPortModeConfigTable": clExtPortModeConfigTable,
       "clExtPortModeConfigEntry": clExtPortModeConfigEntry,
       "clExtPortOperStatus": clExtPortOperStatus,
       "clExtSysMaxNewConnectionPerSecond": clExtSysMaxNewConnectionPerSecond,
       "clExtIf": clExtIf,
       "clExtIfTable": clExtIfTable,
       "clExtIfEntry": clExtIfEntry,
       "clExtIfSpeed": clExtIfSpeed,
       "clExtIfSinceLastChange": clExtIfSinceLastChange,
       "clExtAp": clExtAp,
       "clExtApTable": clExtApTable,
       "clExtApEntry": clExtApEntry,
       "clExtApRealTimeStatsModeEnabled": clExtApRealTimeStatsModeEnabled,
       "clExtApMonitorMode": clExtApMonitorMode,
       "clExtApSysManufacturer": clExtApSysManufacturer,
       "clExtApSysSoftwareName": clExtApSysSoftwareName,
       "clExtApSysSoftwareVersion": clExtApSysSoftwareVersion,
       "clExtApSysSoftwareVendor": clExtApSysSoftwareVendor,
       "clExtApQosMinBandwidth": clExtApQosMinBandwidth,
       "clExtApTotalPhyInterfaceCount": clExtApTotalPhyInterfaceCount,
       "clExtApName": clExtApName,
       "clExtApDot11IfTable": clExtApDot11IfTable,
       "clExtApDot11IfEntry": clExtApDot11IfEntry,
       "clExtAp11nChannelBandwidth": clExtAp11nChannelBandwidth,
       "clExtApDot11IfIANAType": clExtApDot11IfIANAType,
       "clExtApIfPhyChannelAssignment": clExtApIfPhyChannelAssignment,
       "clExtApDot11RadioStatsRxByteCount": clExtApDot11RadioStatsRxByteCount,
       "clExtApDot11RadioStatsTxByteCount": clExtApDot11RadioStatsTxByteCount,
       "clExtApDot11WirelessModeSupported": clExtApDot11WirelessModeSupported,
       "clExtApDot11IfAdminStatus": clExtApDot11IfAdminStatus,
       "clExtApDot11IfOperStatus": clExtApDot11IfOperStatus,
       "cLExtAPDot11IfRTSThreshold": cLExtAPDot11IfRTSThreshold,
       "clExtApDot11RadioStatsTable": clExtApDot11RadioStatsTable,
       "clExtApDot11RadioStatsEntry": clExtApDot11RadioStatsEntry,
       "clExtApDot11RadioStatsRetryFrameCount": clExtApDot11RadioStatsRetryFrameCount,
       "clExtApDot11RadioStatsRetryPacketCount": clExtApDot11RadioStatsRetryPacketCount,
       "clExtApDot11RadioStatsRxErrorPacketCount": clExtApDot11RadioStatsRxErrorPacketCount,
       "clExtApEthernetIfTable": clExtApEthernetIfTable,
       "clExtApEthernetIfEntry": clExtApEthernetIfEntry,
       "clExtApEthernetIfOperStatus": clExtApEthernetIfOperStatus,
       "clExtApEthernetIfRxBcastPkts": clExtApEthernetIfRxBcastPkts,
       "clExtApEthernetIfRxMcastPkts": clExtApEthernetIfRxMcastPkts,
       "clExtApEthernetIfTxBcastPkts": clExtApEthernetIfTxBcastPkts,
       "clExtApEthernetIfTxMcastPkts": clExtApEthernetIfTxMcastPkts,
       "cLApOperationInfoTable": cLApOperationInfoTable,
       "cLApOperationInfoEntry": cLApOperationInfoEntry,
       "cLApOperationSysMacAddress": cLApOperationSysMacAddress,
       "cLApOperationStatus": cLApOperationStatus,
       "clExtWlan": clExtWlan,
       "clExtWlanConfigTable": clExtWlanConfigTable,
       "clExtWlanConfigEntry": clExtWlanConfigEntry,
       "clExtWlanAdminStatus": clExtWlanAdminStatus,
       "clExtWlanBroadcastSsidEnable": clExtWlanBroadcastSsidEnable,
       "clExtWlanLoadBalancingMode": clExtWlanLoadBalancingMode,
       "clExtWlanP2PBlocking": clExtWlanP2PBlocking,
       "clExtWlanSecurityAuthType": clExtWlanSecurityAuthType,
       "clExtWlanDot11Auth": clExtWlanDot11Auth,
       "clExtWlanSecurity": clExtWlanSecurity,
       "clExtWlanAuthenMode": clExtWlanAuthenMode,
       "clExtWlanSecurityCiphers": clExtWlanSecurityCiphers,
       "clExtWepCipherKeyIndex": clExtWepCipherKeyIndex,
       "clExtWepCipherKeyValue": clExtWepCipherKeyValue,
       "clExtWepCipherKeyCharType": clExtWepCipherKeyCharType,
       "clExtDot11Client": clExtDot11Client,
       "clExtClientTable": clExtClientTable,
       "clExtClientEntry": clExtClientEntry,
       "clExtClientProtocol": clExtClientProtocol,
       "clExtClientPowerSaveMode": clExtClientPowerSaveMode,
       "clExtClientUpTime": clExtClientUpTime,
       "clExtClientAuthFailReason": clExtClientAuthFailReason,
       "clExtClientRxThroughput": clExtClientRxThroughput,
       "clExtClientTxThroughput": clExtClientTxThroughput,
       "clExtDot11": clExtDot11,
       "clExtHtMacOperationsTable": clExtHtMacOperationsTable,
       "clExtHtMacOperationsEntry": clExtHtMacOperationsEntry,
       "clExtHtDot11nAmpduEnable": clExtHtDot11nAmpduEnable,
       "clExtHtDot11nGuardIntervalEnable": clExtHtDot11nGuardIntervalEnable,
       "clExtRF": clExtRF,
       "clExtRFProfileTable": clExtRFProfileTable,
       "clExtRFProfileEntry": clExtRFProfileEntry,
       "clExtRFProfileWirelessMode": clExtRFProfileWirelessMode,
       "clExtSecurity": clExtSecurity,
       "clExtAbnormalClientSecurityTable": clExtAbnormalClientSecurityTable,
       "clExtAbnormalClientSecurityEntry": clExtAbnormalClientSecurityEntry,
       "clExtSecurityType": clExtSecurityType,
       "clExtAbnormalOfflineClientCount": clExtAbnormalOfflineClientCount,
       "ciscoLwappApExtStats": ciscoLwappApExtStats,
       "ciscoLwappApExtMIBConform": ciscoLwappApExtMIBConform,
       "ciscoLwappApExtMIBCompliances": ciscoLwappApExtMIBCompliances,
       "ciscoLwappApExtMIBCompliance": ciscoLwappApExtMIBCompliance,
       "ciscoLwappApExtMIBGroups": ciscoLwappApExtMIBGroups,
       "ciscoLwappApExtMIBConfigGroup": ciscoLwappApExtMIBConfigGroup,
       "ciscoLwappApExtMIBNotifsGroup": ciscoLwappApExtMIBNotifsGroup,
       "ciscoLwappApExtMIBStatusGroup": ciscoLwappApExtMIBStatusGroup,
       "ciscoLwappApExtMIBNotifObjects": ciscoLwappApExtMIBNotifObjects,
       "cLExtApDisassocReason": cLExtApDisassocReason,
       "cLExtDot11ClientAssocFailReason": cLExtDot11ClientAssocFailReason,
       "cLExtApDetectedMacAddress": cLExtApDetectedMacAddress,
       "cLExtApDetectedChannel": cLExtApDetectedChannel,
       "cLExtApDectedSsid": cLExtApDectedSsid}
)

# SNMP MIB module (RUIJIE-WLAN-FAT-AP-CF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-WLAN-FAT-AP-CF-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:00 2025
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ruijieApgWlanId,) = mibBuilder.importSymbols(
    "RUIJIE-AC-MGMT-MIB",
    "ruijieApgWlanId")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

apStandardmibmodule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80)
)
if mibBuilder.loadTexts:
    apStandardmibmodule.setRevisions(
        ("2010-02-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApStandardSysTraps_ObjectIdentity = ObjectIdentity
apStandardSysTraps = _ApStandardSysTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 0)
)
_ApStandardSysTrapsObjects_ObjectIdentity = ObjectIdentity
apStandardSysTrapsObjects = _ApStandardSysTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 1)
)
_ApOriginalIpAddr_Type = IpAddress
_ApOriginalIpAddr_Object = MibScalar
apOriginalIpAddr = _ApOriginalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 1, 1),
    _ApOriginalIpAddr_Type()
)
apOriginalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOriginalIpAddr.setStatus("current")
_ApCurrentIpAddr_Type = IpAddress
_ApCurrentIpAddr_Object = MibScalar
apCurrentIpAddr = _ApCurrentIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 1, 2),
    _ApCurrentIpAddr_Type()
)
apCurrentIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCurrentIpAddr.setStatus("current")
_ApIpAddr_Type = IpAddress
_ApIpAddr_Object = MibScalar
apIpAddr = _ApIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 1, 3),
    _ApIpAddr_Type()
)
apIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpAddr.setStatus("current")
_ApTimeStamp_Type = TimeTicks
_ApTimeStamp_Object = MibScalar
apTimeStamp = _ApTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 1, 4),
    _ApTimeStamp_Type()
)
apTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTimeStamp.setStatus("current")
_ApAPMac_Type = MacAddress
_ApAPMac_Object = MibScalar
apAPMac = _ApAPMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 1, 5),
    _ApAPMac_Type()
)
apAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAPMac.setStatus("current")
_ApSSIDKey_Type = DisplayString
_ApSSIDKey_Object = MibScalar
apSSIDKey = _ApSSIDKey_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 1, 6),
    _ApSSIDKey_Type()
)
apSSIDKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDKey.setStatus("current")
_ApSSIDKeyConflict_Type = DisplayString
_ApSSIDKeyConflict_Object = MibScalar
apSSIDKeyConflict = _ApSSIDKeyConflict_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 1, 7),
    _ApSSIDKeyConflict_Type()
)
apSSIDKeyConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDKeyConflict.setStatus("current")
_ApCyperIndex_Type = Integer32
_ApCyperIndex_Object = MibScalar
apCyperIndex = _ApCyperIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 1, 8),
    _ApCyperIndex_Type()
)
apCyperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCyperIndex.setStatus("current")
_ApStandardRadioTraps_ObjectIdentity = ObjectIdentity
apStandardRadioTraps = _ApStandardRadioTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 2)
)
_ApStandardRadioTrapsObjects_ObjectIdentity = ObjectIdentity
apStandardRadioTrapsObjects = _ApStandardRadioTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 3)
)
_ApInterruptReason_Type = DisplayString
_ApInterruptReason_Object = MibScalar
apInterruptReason = _ApInterruptReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 3, 1),
    _ApInterruptReason_Type()
)
apInterruptReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInterruptReason.setStatus("current")
_ApWorkingAPRadioIfInfo_Type = MacAddress
_ApWorkingAPRadioIfInfo_Object = MibScalar
apWorkingAPRadioIfInfo = _ApWorkingAPRadioIfInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 3, 2),
    _ApWorkingAPRadioIfInfo_Type()
)
apWorkingAPRadioIfInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWorkingAPRadioIfInfo.setStatus("current")
_ApWorkingAPChannel_Type = Integer32
_ApWorkingAPChannel_Object = MibScalar
apWorkingAPChannel = _ApWorkingAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 3, 3),
    _ApWorkingAPChannel_Type()
)
apWorkingAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWorkingAPChannel.setStatus("current")
_ApInterfAPChannel_Type = Integer32
_ApInterfAPChannel_Object = MibScalar
apInterfAPChannel = _ApInterfAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 3, 4),
    _ApInterfAPChannel_Type()
)
apInterfAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInterfAPChannel.setStatus("current")
_ApInterfAPBSSID_Type = MacAddress
_ApInterfAPBSSID_Object = MibScalar
apInterfAPBSSID = _ApInterfAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 3, 5),
    _ApInterfAPBSSID_Type()
)
apInterfAPBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInterfAPBSSID.setStatus("current")
_ApInterfStaMac_Type = MacAddress
_ApInterfStaMac_Object = MibScalar
apInterfStaMac = _ApInterfStaMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 3, 6),
    _ApInterfStaMac_Type()
)
apInterfStaMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInterfStaMac.setStatus("current")
_ApPermitAssoUser_Type = Integer32
_ApPermitAssoUser_Object = MibScalar
apPermitAssoUser = _ApPermitAssoUser_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 3, 7),
    _ApPermitAssoUser_Type()
)
apPermitAssoUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPermitAssoUser.setStatus("current")
_ApAssoFailReason_Type = DisplayString
_ApAssoFailReason_Object = MibScalar
apAssoFailReason = _ApAssoFailReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 3, 8),
    _ApAssoFailReason_Type()
)
apAssoFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAssoFailReason.setStatus("current")
_ApChannelBeforeChange_Type = Integer32
_ApChannelBeforeChange_Object = MibScalar
apChannelBeforeChange = _ApChannelBeforeChange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 3, 9),
    _ApChannelBeforeChange_Type()
)
apChannelBeforeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChannelBeforeChange.setStatus("current")
_ApChannelAfterChange_Type = Integer32
_ApChannelAfterChange_Object = MibScalar
apChannelAfterChange = _ApChannelAfterChange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 3, 10),
    _ApChannelAfterChange_Type()
)
apChannelAfterChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChannelAfterChange.setStatus("current")
_ApChanChangeMode_Type = Integer32
_ApChanChangeMode_Object = MibScalar
apChanChangeMode = _ApChanChangeMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 3, 11),
    _ApChanChangeMode_Type()
)
apChanChangeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChanChangeMode.setStatus("current")
_ApStandardTerminalTraps_ObjectIdentity = ObjectIdentity
apStandardTerminalTraps = _ApStandardTerminalTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 4)
)
_ApStandardTerminalTrapsObjects_ObjectIdentity = ObjectIdentity
apStandardTerminalTrapsObjects = _ApStandardTerminalTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 5)
)
_ApWorkingAPBSSID_Type = MacAddress
_ApWorkingAPBSSID_Object = MibScalar
apWorkingAPBSSID = _ApWorkingAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 5, 1),
    _ApWorkingAPBSSID_Type()
)
apWorkingAPBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWorkingAPBSSID.setStatus("current")
_ApWorkingAPSSID_Type = MacAddress
_ApWorkingAPSSID_Object = MibScalar
apWorkingAPSSID = _ApWorkingAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 5, 2),
    _ApWorkingAPSSID_Type()
)
apWorkingAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWorkingAPSSID.setStatus("current")
_ApStaMacAddr_Type = MacAddress
_ApStaMacAddr_Object = MibScalar
apStaMacAddr = _ApStaMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 5, 3),
    _ApStaMacAddr_Type()
)
apStaMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaMacAddr.setStatus("current")
_ApAuthMode_Type = Integer32
_ApAuthMode_Object = MibScalar
apAuthMode = _ApAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 5, 4),
    _ApAuthMode_Type()
)
apAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAuthMode.setStatus("current")
_ApAuthFailReason_Type = DisplayString
_ApAuthFailReason_Object = MibScalar
apAuthFailReason = _ApAuthFailReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 5, 5),
    _ApAuthFailReason_Type()
)
apAuthFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAuthFailReason.setStatus("current")
_ApStandardAuthSvrTraps_ObjectIdentity = ObjectIdentity
apStandardAuthSvrTraps = _ApStandardAuthSvrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 6)
)
_ApStandardWapiScrTraps_ObjectIdentity = ObjectIdentity
apStandardWapiScrTraps = _ApStandardWapiScrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 7)
)
_ApConfigInfoObjects_ObjectIdentity = ObjectIdentity
apConfigInfoObjects = _ApConfigInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8)
)
_ApSysInfoObjects_ObjectIdentity = ObjectIdentity
apSysInfoObjects = _ApSysInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1)
)


class _ApSysNetID_Type(DisplayString):
    """Custom type apSysNetID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 255),
    )


_ApSysNetID_Type.__name__ = "DisplayString"
_ApSysNetID_Object = MibScalar
apSysNetID = _ApSysNetID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 1),
    _ApSysNetID_Type()
)
apSysNetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSysNetID.setStatus("current")


class _ApSysHostName_Type(DisplayString):
    """Custom type apSysHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 255),
    )


_ApSysHostName_Type.__name__ = "DisplayString"
_ApSysHostName_Object = MibScalar
apSysHostName = _ApSysHostName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 2),
    _ApSysHostName_Type()
)
apSysHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSysHostName.setStatus("current")
_ApSysDescr_Type = DisplayString
_ApSysDescr_Object = MibScalar
apSysDescr = _ApSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 3),
    _ApSysDescr_Type()
)
apSysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysDescr.setStatus("current")
_ApManufacturer_Type = DisplayString
_ApManufacturer_Object = MibScalar
apManufacturer = _ApManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 4),
    _ApManufacturer_Type()
)
apManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apManufacturer.setStatus("current")
_ApSerialNumber_Type = DisplayString
_ApSerialNumber_Object = MibScalar
apSerialNumber = _ApSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 5),
    _ApSerialNumber_Type()
)
apSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSerialNumber.setStatus("current")
_ApSysModel_Type = DisplayString
_ApSysModel_Object = MibScalar
apSysModel = _ApSysModel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 6),
    _ApSysModel_Type()
)
apSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysModel.setStatus("current")
_ApSysTime_Type = DisplayString
_ApSysTime_Object = MibScalar
apSysTime = _ApSysTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 7),
    _ApSysTime_Type()
)
apSysTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSysTime.setStatus("current")
_ApSysUpTime_Type = TimeTicks
_ApSysUpTime_Object = MibScalar
apSysUpTime = _ApSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 8),
    _ApSysUpTime_Type()
)
apSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysUpTime.setStatus("current")
_ApSysIPAddress_Type = IpAddress
_ApSysIPAddress_Object = MibScalar
apSysIPAddress = _ApSysIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 9),
    _ApSysIPAddress_Type()
)
apSysIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSysIPAddress.setStatus("current")
_ApSysIPNetMask_Type = IpAddress
_ApSysIPNetMask_Object = MibScalar
apSysIPNetMask = _ApSysIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 10),
    _ApSysIPNetMask_Type()
)
apSysIPNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSysIPNetMask.setStatus("current")
_ApSysGWAddr_Type = IpAddress
_ApSysGWAddr_Object = MibScalar
apSysGWAddr = _ApSysGWAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 11),
    _ApSysGWAddr_Type()
)
apSysGWAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSysGWAddr.setStatus("current")
_ApPrimDNSServerIPAdd_Type = IpAddress
_ApPrimDNSServerIPAdd_Object = MibScalar
apPrimDNSServerIPAdd = _ApPrimDNSServerIPAdd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 12),
    _ApPrimDNSServerIPAdd_Type()
)
apPrimDNSServerIPAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPrimDNSServerIPAdd.setStatus("current")
_ApSeconDNSServerIPAdd_Type = IpAddress
_ApSeconDNSServerIPAdd_Object = MibScalar
apSeconDNSServerIPAdd = _ApSeconDNSServerIPAdd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 13),
    _ApSeconDNSServerIPAdd_Type()
)
apSeconDNSServerIPAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSeconDNSServerIPAdd.setStatus("current")
_ApSysMacAddress_Type = MacAddress
_ApSysMacAddress_Object = MibScalar
apSysMacAddress = _ApSysMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 14),
    _ApSysMacAddress_Type()
)
apSysMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysMacAddress.setStatus("current")
_ApReadCommunityName_Type = DisplayString
_ApReadCommunityName_Object = MibScalar
apReadCommunityName = _ApReadCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 15),
    _ApReadCommunityName_Type()
)
apReadCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apReadCommunityName.setStatus("current")
_ApWriteCommunityName_Type = DisplayString
_ApWriteCommunityName_Object = MibScalar
apWriteCommunityName = _ApWriteCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 16),
    _ApWriteCommunityName_Type()
)
apWriteCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWriteCommunityName.setStatus("current")
_ApStatWindowTime_Type = TimeTicks
_ApStatWindowTime_Object = MibScalar
apStatWindowTime = _ApStatWindowTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 17),
    _ApStatWindowTime_Type()
)
apStatWindowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apStatWindowTime.setStatus("current")
_ApSampleTime_Type = Integer32
_ApSampleTime_Object = MibScalar
apSampleTime = _ApSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 18),
    _ApSampleTime_Type()
)
apSampleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSampleTime.setStatus("current")
_ApSysRestart_Type = Integer32
_ApSysRestart_Object = MibScalar
apSysRestart = _ApSysRestart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 19),
    _ApSysRestart_Type()
)
apSysRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSysRestart.setStatus("current")
_ApSysReset_Type = Integer32
_ApSysReset_Object = MibScalar
apSysReset = _ApSysReset_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 20),
    _ApSysReset_Type()
)
apSysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSysReset.setStatus("current")
_ApSoftwareName_Type = DisplayString
_ApSoftwareName_Object = MibScalar
apSoftwareName = _ApSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 21),
    _ApSoftwareName_Type()
)
apSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSoftwareName.setStatus("current")
_ApSoftwareVersion_Type = DisplayString
_ApSoftwareVersion_Object = MibScalar
apSoftwareVersion = _ApSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 22),
    _ApSoftwareVersion_Type()
)
apSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSoftwareVersion.setStatus("current")
_ApSoftwareVendor_Type = DisplayString
_ApSoftwareVendor_Object = MibScalar
apSoftwareVendor = _ApSoftwareVendor_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 23),
    _ApSoftwareVendor_Type()
)
apSoftwareVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSoftwareVendor.setStatus("current")
_ApCPUType_Type = DisplayString
_ApCPUType_Object = MibScalar
apCPUType = _ApCPUType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 24),
    _ApCPUType_Type()
)
apCPUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCPUType.setStatus("current")
_ApMemoryType_Type = DisplayString
_ApMemoryType_Object = MibScalar
apMemoryType = _ApMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 25),
    _ApMemoryType_Type()
)
apMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMemoryType.setStatus("current")
_ApMemorySize_Type = Gauge32
_ApMemorySize_Object = MibScalar
apMemorySize = _ApMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 26),
    _ApMemorySize_Type()
)
apMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMemorySize.setStatus("current")
_ApFlashSize_Type = Gauge32
_ApFlashSize_Object = MibScalar
apFlashSize = _ApFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 1, 27),
    _ApFlashSize_Type()
)
apFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlashSize.setStatus("current")
_ApPhyInterfaceConfig_ObjectIdentity = ObjectIdentity
apPhyInterfaceConfig = _ApPhyInterfaceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 2)
)
_ApIfNumber_Type = Integer32
_ApIfNumber_Object = MibScalar
apIfNumber = _ApIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 2, 1),
    _ApIfNumber_Type()
)
apIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfNumber.setStatus("current")
_ApWiredInterfaceCfgTable_Object = MibTable
apWiredInterfaceCfgTable = _ApWiredInterfaceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 2, 2)
)
if mibBuilder.loadTexts:
    apWiredInterfaceCfgTable.setStatus("current")
_ApWiredInterfaceCfgEntry_Object = MibTableRow
apWiredInterfaceCfgEntry = _ApWiredInterfaceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 2, 2, 1)
)
apWiredInterfaceCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apWiredInterfaceCfgEntry.setStatus("current")
_ApIfDescr_Type = DisplayString
_ApIfDescr_Object = MibTableColumn
apIfDescr = _ApIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 2, 2, 1, 1),
    _ApIfDescr_Type()
)
apIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfDescr.setStatus("current")
_ApIfType_Type = IANAifType
_ApIfType_Object = MibTableColumn
apIfType = _ApIfType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 2, 2, 1, 2),
    _ApIfType_Type()
)
apIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfType.setStatus("current")
_ApIfMTU_Type = Integer32
_ApIfMTU_Object = MibTableColumn
apIfMTU = _ApIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 2, 2, 1, 3),
    _ApIfMTU_Type()
)
apIfMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfMTU.setStatus("current")
_ApIfSpeed_Type = Integer32
_ApIfSpeed_Object = MibTableColumn
apIfSpeed = _ApIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 2, 2, 1, 4),
    _ApIfSpeed_Type()
)
apIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfSpeed.setStatus("current")
_ApIfPhysAddress_Type = MacAddress
_ApIfPhysAddress_Object = MibTableColumn
apIfPhysAddress = _ApIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 2, 2, 1, 5),
    _ApIfPhysAddress_Type()
)
apIfPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfPhysAddress.setStatus("current")
_ApIfAdminStatus_Type = Integer32
_ApIfAdminStatus_Object = MibTableColumn
apIfAdminStatus = _ApIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 2, 2, 1, 6),
    _ApIfAdminStatus_Type()
)
apIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfAdminStatus.setStatus("current")
_ApIfOperStatus_Type = Integer32
_ApIfOperStatus_Object = MibTableColumn
apIfOperStatus = _ApIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 2, 2, 1, 7),
    _ApIfOperStatus_Type()
)
apIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfOperStatus.setStatus("current")
_ApIfLastChange_Type = TimeTicks
_ApIfLastChange_Object = MibTableColumn
apIfLastChange = _ApIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 2, 2, 1, 8),
    _ApIfLastChange_Type()
)
apIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfLastChange.setStatus("current")
_ApRadioInterfaceCfg_ObjectIdentity = ObjectIdentity
apRadioInterfaceCfg = _ApRadioInterfaceCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3)
)
_ApRadioInterfaceInfoTable_Object = MibTable
apRadioInterfaceInfoTable = _ApRadioInterfaceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1)
)
if mibBuilder.loadTexts:
    apRadioInterfaceInfoTable.setStatus("current")
_ApRadioInterfaceInfoEntry_Object = MibTableRow
apRadioInterfaceInfoEntry = _ApRadioInterfaceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1)
)
apRadioInterfaceInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apRadioInterfaceInfoEntry.setStatus("current")
_ApRadioIfDescr_Type = DisplayString
_ApRadioIfDescr_Object = MibTableColumn
apRadioIfDescr = _ApRadioIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 1),
    _ApRadioIfDescr_Type()
)
apRadioIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioIfDescr.setStatus("current")
_ApRadioIfType_Type = IANAifType
_ApRadioIfType_Object = MibTableColumn
apRadioIfType = _ApRadioIfType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 2),
    _ApRadioIfType_Type()
)
apRadioIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioIfType.setStatus("current")
_ApRadioIfMTU_Type = Integer32
_ApRadioIfMTU_Object = MibTableColumn
apRadioIfMTU = _ApRadioIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 3),
    _ApRadioIfMTU_Type()
)
apRadioIfMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioIfMTU.setStatus("current")
_ApRadioIfSpeed_Type = Integer32
_ApRadioIfSpeed_Object = MibTableColumn
apRadioIfSpeed = _ApRadioIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 4),
    _ApRadioIfSpeed_Type()
)
apRadioIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioIfSpeed.setStatus("current")
_ApRadioIfMacAddress_Type = MacAddress
_ApRadioIfMacAddress_Object = MibTableColumn
apRadioIfMacAddress = _ApRadioIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 5),
    _ApRadioIfMacAddress_Type()
)
apRadioIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioIfMacAddress.setStatus("current")


class _ApRadioIfDiversity_Type(Integer32):
    """Custom type apRadioIfDiversity based on Integer32"""
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


_ApRadioIfDiversity_Type.__name__ = "Integer32"
_ApRadioIfDiversity_Object = MibTableColumn
apRadioIfDiversity = _ApRadioIfDiversity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 6),
    _ApRadioIfDiversity_Type()
)
apRadioIfDiversity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioIfDiversity.setStatus("current")


class _ApRadioIfAdminStatus_Type(Integer32):
    """Custom type apRadioIfAdminStatus based on Integer32"""
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
          ("admindown", 3))
    )


_ApRadioIfAdminStatus_Type.__name__ = "Integer32"
_ApRadioIfAdminStatus_Object = MibTableColumn
apRadioIfAdminStatus = _ApRadioIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 7),
    _ApRadioIfAdminStatus_Type()
)
apRadioIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioIfAdminStatus.setStatus("current")


class _ApRadioIfOperStatus_Type(Integer32):
    """Custom type apRadioIfOperStatus based on Integer32"""
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
          ("admindown", 3))
    )


_ApRadioIfOperStatus_Type.__name__ = "Integer32"
_ApRadioIfOperStatus_Object = MibTableColumn
apRadioIfOperStatus = _ApRadioIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 8),
    _ApRadioIfOperStatus_Type()
)
apRadioIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioIfOperStatus.setStatus("current")
_ApRadioIfLastChange_Type = TimeTicks
_ApRadioIfLastChange_Object = MibTableColumn
apRadioIfLastChange = _ApRadioIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 9),
    _ApRadioIfLastChange_Type()
)
apRadioIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioIfLastChange.setStatus("current")
_ApRadioChannelAutoSelectEnable_Type = Integer32
_ApRadioChannelAutoSelectEnable_Object = MibTableColumn
apRadioChannelAutoSelectEnable = _ApRadioChannelAutoSelectEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 10),
    _ApRadioChannelAutoSelectEnable_Type()
)
apRadioChannelAutoSelectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioChannelAutoSelectEnable.setStatus("current")
_ApRadioChannelConfig_Type = Integer32
_ApRadioChannelConfig_Object = MibTableColumn
apRadioChannelConfig = _ApRadioChannelConfig_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 11),
    _ApRadioChannelConfig_Type()
)
apRadioChannelConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioChannelConfig.setStatus("current")
_ApRadioChannelUsing_Type = Integer32
_ApRadioChannelUsing_Object = MibTableColumn
apRadioChannelUsing = _ApRadioChannelUsing_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 12),
    _ApRadioChannelUsing_Type()
)
apRadioChannelUsing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioChannelUsing.setStatus("current")
_ApCurrRadioModeSupport_Type = Integer32
_ApCurrRadioModeSupport_Object = MibTableColumn
apCurrRadioModeSupport = _ApCurrRadioModeSupport_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 13),
    _ApCurrRadioModeSupport_Type()
)
apCurrRadioModeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCurrRadioModeSupport.setStatus("current")
_ApRadioModeConfig_Type = Integer32
_ApRadioModeConfig_Object = MibTableColumn
apRadioModeConfig = _ApRadioModeConfig_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 14),
    _ApRadioModeConfig_Type()
)
apRadioModeConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioModeConfig.setStatus("current")
_ApTransmitSpeedConfig_Type = DisplayString
_ApTransmitSpeedConfig_Object = MibTableColumn
apTransmitSpeedConfig = _ApTransmitSpeedConfig_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 15),
    _ApTransmitSpeedConfig_Type()
)
apTransmitSpeedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTransmitSpeedConfig.setStatus("current")
_ApMaxTxPwrLvl_Type = DisplayString
_ApMaxTxPwrLvl_Object = MibTableColumn
apMaxTxPwrLvl = _ApMaxTxPwrLvl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 16),
    _ApMaxTxPwrLvl_Type()
)
apMaxTxPwrLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMaxTxPwrLvl.setStatus("current")
_ApTxPwr_Type = Integer32
_ApTxPwr_Object = MibTableColumn
apTxPwr = _ApTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 17),
    _ApTxPwr_Type()
)
apTxPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTxPwr.setStatus("current")
_ApPwrAttRange_Type = Integer32
_ApPwrAttRange_Object = MibTableColumn
apPwrAttRange = _ApPwrAttRange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 18),
    _ApPwrAttRange_Type()
)
apPwrAttRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPwrAttRange.setStatus("current")
_ApPwrAttValue_Type = Integer32
_ApPwrAttValue_Object = MibTableColumn
apPwrAttValue = _ApPwrAttValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 19),
    _ApPwrAttValue_Type()
)
apPwrAttValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPwrAttValue.setStatus("current")
_ApAntennaGain_Type = Integer32
_ApAntennaGain_Object = MibTableColumn
apAntennaGain = _ApAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 20),
    _ApAntennaGain_Type()
)
apAntennaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAntennaGain.setStatus("current")
_ApPowerMgmtEnable_Type = TruthValue
_ApPowerMgmtEnable_Object = MibTableColumn
apPowerMgmtEnable = _ApPowerMgmtEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 21),
    _ApPowerMgmtEnable_Type()
)
apPowerMgmtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPowerMgmtEnable.setStatus("current")
_ApMaxStationNumPermitted_Type = Integer32
_ApMaxStationNumPermitted_Object = MibTableColumn
apMaxStationNumPermitted = _ApMaxStationNumPermitted_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 22),
    _ApMaxStationNumPermitted_Type()
)
apMaxStationNumPermitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMaxStationNumPermitted.setStatus("current")
_ApAMPDUEnabled_Type = Integer32
_ApAMPDUEnabled_Object = MibTableColumn
apAMPDUEnabled = _ApAMPDUEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 23),
    _ApAMPDUEnabled_Type()
)
apAMPDUEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAMPDUEnabled.setStatus("current")
_ApBWMode_Type = Integer32
_ApBWMode_Object = MibTableColumn
apBWMode = _ApBWMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 24),
    _ApBWMode_Type()
)
apBWMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBWMode.setStatus("current")
_ApShortGIEnabled_Type = Integer32
_ApShortGIEnabled_Object = MibTableColumn
apShortGIEnabled = _ApShortGIEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 25),
    _ApShortGIEnabled_Type()
)
apShortGIEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apShortGIEnabled.setStatus("current")
_ApIs11nOnly_Type = TruthValue
_ApIs11nOnly_Object = MibTableColumn
apIs11nOnly = _ApIs11nOnly_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 1, 1, 26),
    _ApIs11nOnly_Type()
)
apIs11nOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIs11nOnly.setStatus("current")
_ApRadioInterfacePhyParaTable_Object = MibTable
apRadioInterfacePhyParaTable = _ApRadioInterfacePhyParaTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 2)
)
if mibBuilder.loadTexts:
    apRadioInterfacePhyParaTable.setStatus("current")
_ApRadioInterfacePhyParaEntry_Object = MibTableRow
apRadioInterfacePhyParaEntry = _ApRadioInterfacePhyParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 2, 1)
)
apRadioInterfacePhyParaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apRadioInterfacePhyParaEntry.setStatus("current")
_ApBeaconIntvl_Type = Integer32
_ApBeaconIntvl_Object = MibTableColumn
apBeaconIntvl = _ApBeaconIntvl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 2, 1, 1),
    _ApBeaconIntvl_Type()
)
apBeaconIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBeaconIntvl.setStatus("current")
_ApDtimIntvl_Type = Integer32
_ApDtimIntvl_Object = MibTableColumn
apDtimIntvl = _ApDtimIntvl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 2, 1, 2),
    _ApDtimIntvl_Type()
)
apDtimIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDtimIntvl.setStatus("current")
_ApRtsThreshold_Type = Integer32
_ApRtsThreshold_Object = MibTableColumn
apRtsThreshold = _ApRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 2, 1, 3),
    _ApRtsThreshold_Type()
)
apRtsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRtsThreshold.setStatus("current")
_ApFragThreshlod_Type = Integer32
_ApFragThreshlod_Object = MibTableColumn
apFragThreshlod = _ApFragThreshlod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 2, 1, 4),
    _ApFragThreshlod_Type()
)
apFragThreshlod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFragThreshlod.setStatus("current")
_ApPreambleLen_Type = Integer32
_ApPreambleLen_Object = MibTableColumn
apPreambleLen = _ApPreambleLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 3, 2, 1, 5),
    _ApPreambleLen_Type()
)
apPreambleLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPreambleLen.setStatus("current")
_ApSSIDCfg_ObjectIdentity = ObjectIdentity
apSSIDCfg = _ApSSIDCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4)
)
_ApConfigBSSIDNum_Type = Integer32
_ApConfigBSSIDNum_Object = MibScalar
apConfigBSSIDNum = _ApConfigBSSIDNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4, 1),
    _ApConfigBSSIDNum_Type()
)
apConfigBSSIDNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apConfigBSSIDNum.setStatus("current")
_ApRadioIfSSIDCfgTable_Object = MibTable
apRadioIfSSIDCfgTable = _ApRadioIfSSIDCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4, 2)
)
if mibBuilder.loadTexts:
    apRadioIfSSIDCfgTable.setStatus("current")
_ApRadioIfSSIDCfgEntry_Object = MibTableRow
apRadioIfSSIDCfgEntry = _ApRadioIfSSIDCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4, 2, 1)
)
apRadioIfSSIDCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RUIJIE-WLAN-FAT-AP-CF-MIB", "apWlanId"),
)
if mibBuilder.loadTexts:
    apRadioIfSSIDCfgEntry.setStatus("current")
_ApBSSID_Type = MacAddress
_ApBSSID_Object = MibTableColumn
apBSSID = _ApBSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4, 2, 1, 1),
    _ApBSSID_Type()
)
apBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBSSID.setStatus("current")
_ApSSIDCfgTable_Object = MibTable
apSSIDCfgTable = _ApSSIDCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4, 3)
)
if mibBuilder.loadTexts:
    apSSIDCfgTable.setStatus("current")
_ApSSIDCfgEntry_Object = MibTableRow
apSSIDCfgEntry = _ApSSIDCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4, 3, 1)
)
apSSIDCfgEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FAT-AP-CF-MIB", "apWlanId"),
)
if mibBuilder.loadTexts:
    apSSIDCfgEntry.setStatus("current")
_ApWlanId_Type = Integer32
_ApWlanId_Object = MibTableColumn
apWlanId = _ApWlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4, 3, 1, 1),
    _ApWlanId_Type()
)
apWlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanId.setStatus("current")
_ApSSIDName_Type = DisplayString
_ApSSIDName_Object = MibTableColumn
apSSIDName = _ApSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4, 3, 1, 2),
    _ApSSIDName_Type()
)
apSSIDName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSSIDName.setStatus("current")
_ApSSIDEnabled_Type = TruthValue
_ApSSIDEnabled_Object = MibTableColumn
apSSIDEnabled = _ApSSIDEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4, 3, 1, 3),
    _ApSSIDEnabled_Type()
)
apSSIDEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSSIDEnabled.setStatus("current")
_ApSSIDHidden_Type = TruthValue
_ApSSIDHidden_Object = MibTableColumn
apSSIDHidden = _ApSSIDHidden_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4, 3, 1, 4),
    _ApSSIDHidden_Type()
)
apSSIDHidden.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSSIDHidden.setStatus("current")
_ApStaIsolate_Type = TruthValue
_ApStaIsolate_Object = MibTableColumn
apStaIsolate = _ApStaIsolate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4, 3, 1, 5),
    _ApStaIsolate_Type()
)
apStaIsolate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apStaIsolate.setStatus("current")
_ApDot11Auth_Type = Integer32
_ApDot11Auth_Object = MibTableColumn
apDot11Auth = _ApDot11Auth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4, 3, 1, 6),
    _ApDot11Auth_Type()
)
apDot11Auth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apDot11Auth.setStatus("current")
_ApSecurity_Type = Integer32
_ApSecurity_Object = MibTableColumn
apSecurity = _ApSecurity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4, 3, 1, 7),
    _ApSecurity_Type()
)
apSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSecurity.setStatus("current")
_ApAuthenMode_Type = Integer32
_ApAuthenMode_Object = MibTableColumn
apAuthenMode = _ApAuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4, 3, 1, 8),
    _ApAuthenMode_Type()
)
apAuthenMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAuthenMode.setStatus("current")


class _ApSecurityCiphers_Type(Integer32):
    """Custom type apSecurityCiphers based on Integer32"""
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
          ("wapisms4", 5))
    )


_ApSecurityCiphers_Type.__name__ = "Integer32"
_ApSecurityCiphers_Object = MibTableColumn
apSecurityCiphers = _ApSecurityCiphers_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4, 3, 1, 9),
    _ApSecurityCiphers_Type()
)
apSecurityCiphers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSecurityCiphers.setStatus("current")
_ApVlanId_Type = Integer32
_ApVlanId_Object = MibTableColumn
apVlanId = _ApVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4, 3, 1, 10),
    _ApVlanId_Type()
)
apVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apVlanId.setStatus("current")
_ApMaxSimultUsers_Type = Integer32
_ApMaxSimultUsers_Object = MibTableColumn
apMaxSimultUsers = _ApMaxSimultUsers_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4, 3, 1, 11),
    _ApMaxSimultUsers_Type()
)
apMaxSimultUsers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apMaxSimultUsers.setStatus("current")
_ApStaUplinkMaxRate_Type = Integer32
_ApStaUplinkMaxRate_Object = MibTableColumn
apStaUplinkMaxRate = _ApStaUplinkMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4, 3, 1, 12),
    _ApStaUplinkMaxRate_Type()
)
apStaUplinkMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apStaUplinkMaxRate.setStatus("current")
_ApStaDwlinkMaxRate_Type = Integer32
_ApStaDwlinkMaxRate_Object = MibTableColumn
apStaDwlinkMaxRate = _ApStaDwlinkMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4, 3, 1, 13),
    _ApStaDwlinkMaxRate_Type()
)
apStaDwlinkMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apStaDwlinkMaxRate.setStatus("current")
_ApSSIDCfgStatus_Type = RowStatus
_ApSSIDCfgStatus_Object = MibTableColumn
apSSIDCfgStatus = _ApSSIDCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 4, 3, 1, 14),
    _ApSSIDCfgStatus_Type()
)
apSSIDCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSSIDCfgStatus.setStatus("current")
_ApSecurityCfg_ObjectIdentity = ObjectIdentity
apSecurityCfg = _ApSecurityCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 5)
)
_ApSecurityCfgTable_Object = MibTable
apSecurityCfgTable = _ApSecurityCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 5, 1)
)
if mibBuilder.loadTexts:
    apSecurityCfgTable.setStatus("current")
_ApSecurityCfgEntry_Object = MibTableRow
apSecurityCfgEntry = _ApSecurityCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 5, 1, 1)
)
apSecurityCfgEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FAT-AP-CF-MIB", "apWlanId"),
)
if mibBuilder.loadTexts:
    apSecurityCfgEntry.setStatus("current")
_ApWEPCipherKeyIndex_Type = Integer32
_ApWEPCipherKeyIndex_Object = MibTableColumn
apWEPCipherKeyIndex = _ApWEPCipherKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 5, 1, 1, 1),
    _ApWEPCipherKeyIndex_Type()
)
apWEPCipherKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWEPCipherKeyIndex.setStatus("current")
_ApWEPCipherKeyValue_Type = DisplayString
_ApWEPCipherKeyValue_Object = MibTableColumn
apWEPCipherKeyValue = _ApWEPCipherKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 5, 1, 1, 2),
    _ApWEPCipherKeyValue_Type()
)
apWEPCipherKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWEPCipherKeyValue.setStatus("current")
_ApWEPCipherKeyCharType_Type = Integer32
_ApWEPCipherKeyCharType_Object = MibTableColumn
apWEPCipherKeyCharType = _ApWEPCipherKeyCharType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 5, 1, 1, 3),
    _ApWEPCipherKeyCharType_Type()
)
apWEPCipherKeyCharType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWEPCipherKeyCharType.setStatus("current")
_ApPSKCipherKeyValue_Type = DisplayString
_ApPSKCipherKeyValue_Object = MibTableColumn
apPSKCipherKeyValue = _ApPSKCipherKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 5, 1, 1, 4),
    _ApPSKCipherKeyValue_Type()
)
apPSKCipherKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPSKCipherKeyValue.setStatus("current")
_ApPSKCipherKeyCharType_Type = Integer32
_ApPSKCipherKeyCharType_Object = MibTableColumn
apPSKCipherKeyCharType = _ApPSKCipherKeyCharType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 5, 1, 1, 5),
    _ApPSKCipherKeyCharType_Type()
)
apPSKCipherKeyCharType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPSKCipherKeyCharType.setStatus("current")
_ApWAPIASIPAddress_Type = IpAddress
_ApWAPIASIPAddress_Object = MibTableColumn
apWAPIASIPAddress = _ApWAPIASIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 5, 1, 1, 6),
    _ApWAPIASIPAddress_Type()
)
apWAPIASIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIASIPAddress.setStatus("current")
_ApWAPIIsInstalledCer_Type = TruthValue
_ApWAPIIsInstalledCer_Object = MibTableColumn
apWAPIIsInstalledCer = _ApWAPIIsInstalledCer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 5, 1, 1, 7),
    _ApWAPIIsInstalledCer_Type()
)
apWAPIIsInstalledCer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPIIsInstalledCer.setStatus("current")
_ApTerminalCfg_ObjectIdentity = ObjectIdentity
apTerminalCfg = _ApTerminalCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 6)
)
_ApTerminalInfoTable_Object = MibTable
apTerminalInfoTable = _ApTerminalInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 6, 1)
)
if mibBuilder.loadTexts:
    apTerminalInfoTable.setStatus("current")
_ApTerminalInfoEntry_Object = MibTableRow
apTerminalInfoEntry = _ApTerminalInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 6, 1, 1)
)
apTerminalInfoEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FAT-AP-CF-MIB", "apStaMAC"),
)
if mibBuilder.loadTexts:
    apTerminalInfoEntry.setStatus("current")
_ApStaMAC_Type = MacAddress
_ApStaMAC_Object = MibTableColumn
apStaMAC = _ApStaMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 6, 1, 1, 1),
    _ApStaMAC_Type()
)
apStaMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaMAC.setStatus("current")
_ApStaWMMAttr_Type = Integer32
_ApStaWMMAttr_Object = MibTableColumn
apStaWMMAttr = _ApStaWMMAttr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 6, 1, 1, 2),
    _ApStaWMMAttr_Type()
)
apStaWMMAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaWMMAttr.setStatus("current")
_ApStaIPAddress_Type = IpAddress
_ApStaIPAddress_Object = MibTableColumn
apStaIPAddress = _ApStaIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 6, 1, 1, 3),
    _ApStaIPAddress_Type()
)
apStaIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaIPAddress.setStatus("current")
_ApStaRadioMode_Type = Integer32
_ApStaRadioMode_Object = MibTableColumn
apStaRadioMode = _ApStaRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 6, 1, 1, 4),
    _ApStaRadioMode_Type()
)
apStaRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaRadioMode.setStatus("current")
_ApStaRadioChannel_Type = Integer32
_ApStaRadioChannel_Object = MibTableColumn
apStaRadioChannel = _ApStaRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 6, 1, 1, 5),
    _ApStaRadioChannel_Type()
)
apStaRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaRadioChannel.setStatus("current")
_ApStaTxRates_Type = Integer32
_ApStaTxRates_Object = MibTableColumn
apStaTxRates = _ApStaTxRates_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 6, 1, 1, 6),
    _ApStaTxRates_Type()
)
apStaTxRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaTxRates.setStatus("current")
_ApStaPowerSaveMode_Type = Integer32
_ApStaPowerSaveMode_Object = MibTableColumn
apStaPowerSaveMode = _ApStaPowerSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 6, 1, 1, 7),
    _ApStaPowerSaveMode_Type()
)
apStaPowerSaveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaPowerSaveMode.setStatus("current")
_ApStaVlanId_Type = Integer32
_ApStaVlanId_Object = MibTableColumn
apStaVlanId = _ApStaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 6, 1, 1, 8),
    _ApStaVlanId_Type()
)
apStaVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaVlanId.setStatus("current")
_ApStaSSIDName_Type = DisplayString
_ApStaSSIDName_Object = MibTableColumn
apStaSSIDName = _ApStaSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 6, 1, 1, 9),
    _ApStaSSIDName_Type()
)
apStaSSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaSSIDName.setStatus("current")
_ApStaDot11Auth_Type = Integer32
_ApStaDot11Auth_Object = MibTableColumn
apStaDot11Auth = _ApStaDot11Auth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 6, 1, 1, 10),
    _ApStaDot11Auth_Type()
)
apStaDot11Auth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDot11Auth.setStatus("current")
_ApStaSecurity_Type = Integer32
_ApStaSecurity_Object = MibTableColumn
apStaSecurity = _ApStaSecurity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 6, 1, 1, 11),
    _ApStaSecurity_Type()
)
apStaSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaSecurity.setStatus("current")
_ApStaAuthenMode_Type = Integer32
_ApStaAuthenMode_Object = MibTableColumn
apStaAuthenMode = _ApStaAuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 6, 1, 1, 12),
    _ApStaAuthenMode_Type()
)
apStaAuthenMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaAuthenMode.setStatus("current")
_ApStaSecurityCiphers_Type = Integer32
_ApStaSecurityCiphers_Object = MibTableColumn
apStaSecurityCiphers = _ApStaSecurityCiphers_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 6, 1, 1, 13),
    _ApStaSecurityCiphers_Type()
)
apStaSecurityCiphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaSecurityCiphers.setStatus("current")
_ApQosCfg_ObjectIdentity = ObjectIdentity
apQosCfg = _ApQosCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7)
)
_ApQosRadioIfCfgTable_Object = MibTable
apQosRadioIfCfgTable = _ApQosRadioIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 1)
)
if mibBuilder.loadTexts:
    apQosRadioIfCfgTable.setStatus("current")
_ApQosRadioIfCfgEntry_Object = MibTableRow
apQosRadioIfCfgEntry = _ApQosRadioIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 1, 1)
)
apQosRadioIfCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RUIJIE-WLAN-FAT-AP-CF-MIB", "apQoSTrafficClassIndex"),
)
if mibBuilder.loadTexts:
    apQosRadioIfCfgEntry.setStatus("current")


class _ApQoSTrafficClassIndex_Type(Integer32):
    """Custom type apQoSTrafficClassIndex based on Integer32"""
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
        *(("bestEffort", 0),
          ("background", 1),
          ("video", 2),
          ("voice", 3))
    )


_ApQoSTrafficClassIndex_Type.__name__ = "Integer32"
_ApQoSTrafficClassIndex_Object = MibTableColumn
apQoSTrafficClassIndex = _ApQoSTrafficClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 1, 1, 1),
    _ApQoSTrafficClassIndex_Type()
)
apQoSTrafficClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQoSTrafficClassIndex.setStatus("current")
_ApQosAIFS_Type = Integer32
_ApQosAIFS_Object = MibTableColumn
apQosAIFS = _ApQosAIFS_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 1, 1, 2),
    _ApQosAIFS_Type()
)
apQosAIFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQosAIFS.setStatus("current")
_ApQoSCWmin_Type = Integer32
_ApQoSCWmin_Object = MibTableColumn
apQoSCWmin = _ApQoSCWmin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 1, 1, 3),
    _ApQoSCWmin_Type()
)
apQoSCWmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQoSCWmin.setStatus("current")
_ApQoSCWmax_Type = Integer32
_ApQoSCWmax_Object = MibTableColumn
apQoSCWmax = _ApQoSCWmax_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 1, 1, 4),
    _ApQoSCWmax_Type()
)
apQoSCWmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQoSCWmax.setStatus("current")
_ApQoSTXOPLim_Type = Integer32
_ApQoSTXOPLim_Object = MibTableColumn
apQoSTXOPLim = _ApQoSTXOPLim_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 1, 1, 5),
    _ApQoSTXOPLim_Type()
)
apQoSTXOPLim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQoSTXOPLim.setStatus("current")
_ApQosBaseCfgTable_Object = MibTable
apQosBaseCfgTable = _ApQosBaseCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2)
)
if mibBuilder.loadTexts:
    apQosBaseCfgTable.setStatus("current")
_ApQosBaseCfgEntry_Object = MibTableRow
apQosBaseCfgEntry = _ApQosBaseCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1)
)
apQosBaseCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apQosBaseCfgEntry.setStatus("current")
_ApQoSBaseTrafficClass_Type = Integer32
_ApQoSBaseTrafficClass_Object = MibTableColumn
apQoSBaseTrafficClass = _ApQoSBaseTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 1),
    _ApQoSBaseTrafficClass_Type()
)
apQoSBaseTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQoSBaseTrafficClass.setStatus("current")
_ApQoSEnabled_Type = TruthValue
_ApQoSEnabled_Object = MibTableColumn
apQoSEnabled = _ApQoSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 2),
    _ApQoSEnabled_Type()
)
apQoSEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQoSEnabled.setStatus("current")
_ApQoSBW_Type = Integer32
_ApQoSBW_Object = MibTableColumn
apQoSBW = _ApQoSBW_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 3),
    _ApQoSBW_Type()
)
apQoSBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQoSBW.setStatus("current")
_ApQoSResPercent_Type = Integer32
_ApQoSResPercent_Object = MibTableColumn
apQoSResPercent = _ApQoSResPercent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 4),
    _ApQoSResPercent_Type()
)
apQoSResPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQoSResPercent.setStatus("current")
_ApQoSsharedBW_Type = Integer32
_ApQoSsharedBW_Object = MibTableColumn
apQoSsharedBW = _ApQoSsharedBW_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 5),
    _ApQoSsharedBW_Type()
)
apQoSsharedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQoSsharedBW.setStatus("current")
_ApQoSsharedBWPercent_Type = Integer32
_ApQoSsharedBWPercent_Object = MibTableColumn
apQoSsharedBWPercent = _ApQoSsharedBWPercent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 6),
    _ApQoSsharedBWPercent_Type()
)
apQoSsharedBWPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQoSsharedBWPercent.setStatus("current")
_ApSchedAlgName_Type = DisplayString
_ApSchedAlgName_Object = MibTableColumn
apSchedAlgName = _ApSchedAlgName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 7),
    _ApSchedAlgName_Type()
)
apSchedAlgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSchedAlgName.setStatus("current")
_ApResPolicyEnabled_Type = TruthValue
_ApResPolicyEnabled_Object = MibTableColumn
apResPolicyEnabled = _ApResPolicyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 8),
    _ApResPolicyEnabled_Type()
)
apResPolicyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apResPolicyEnabled.setStatus("current")
_ApResPolicyName_Type = DisplayString
_ApResPolicyName_Object = MibTableColumn
apResPolicyName = _ApResPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 9),
    _ApResPolicyName_Type()
)
apResPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apResPolicyName.setStatus("current")
_ApBackgroundSvcAvgSpeed_Type = Integer32
_ApBackgroundSvcAvgSpeed_Object = MibTableColumn
apBackgroundSvcAvgSpeed = _ApBackgroundSvcAvgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 10),
    _ApBackgroundSvcAvgSpeed_Type()
)
apBackgroundSvcAvgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBackgroundSvcAvgSpeed.setStatus("current")
_ApBackgroundSvcMaxBurst_Type = Integer32
_ApBackgroundSvcMaxBurst_Object = MibTableColumn
apBackgroundSvcMaxBurst = _ApBackgroundSvcMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 11),
    _ApBackgroundSvcMaxBurst_Type()
)
apBackgroundSvcMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBackgroundSvcMaxBurst.setStatus("current")
_ApBackgroundSvcPriority_Type = Integer32
_ApBackgroundSvcPriority_Object = MibTableColumn
apBackgroundSvcPriority = _ApBackgroundSvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 12),
    _ApBackgroundSvcPriority_Type()
)
apBackgroundSvcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBackgroundSvcPriority.setStatus("current")
_ApBackgroundSvcResPriority_Type = Integer32
_ApBackgroundSvcResPriority_Object = MibTableColumn
apBackgroundSvcResPriority = _ApBackgroundSvcResPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 13),
    _ApBackgroundSvcResPriority_Type()
)
apBackgroundSvcResPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBackgroundSvcResPriority.setStatus("current")
_ApBestEffortSvcAvgSpeed_Type = Integer32
_ApBestEffortSvcAvgSpeed_Object = MibTableColumn
apBestEffortSvcAvgSpeed = _ApBestEffortSvcAvgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 14),
    _ApBestEffortSvcAvgSpeed_Type()
)
apBestEffortSvcAvgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBestEffortSvcAvgSpeed.setStatus("current")
_ApBestEffortSvcMaxBurst_Type = Integer32
_ApBestEffortSvcMaxBurst_Object = MibTableColumn
apBestEffortSvcMaxBurst = _ApBestEffortSvcMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 15),
    _ApBestEffortSvcMaxBurst_Type()
)
apBestEffortSvcMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBestEffortSvcMaxBurst.setStatus("current")
_ApBestEffortSvcPriority_Type = Integer32
_ApBestEffortSvcPriority_Object = MibTableColumn
apBestEffortSvcPriority = _ApBestEffortSvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 16),
    _ApBestEffortSvcPriority_Type()
)
apBestEffortSvcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBestEffortSvcPriority.setStatus("current")
_ApBestEffortSvcResPriority_Type = Integer32
_ApBestEffortSvcResPriority_Object = MibTableColumn
apBestEffortSvcResPriority = _ApBestEffortSvcResPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 17),
    _ApBestEffortSvcResPriority_Type()
)
apBestEffortSvcResPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBestEffortSvcResPriority.setStatus("current")
_ApVoiceSvcAvgSpeed_Type = Integer32
_ApVoiceSvcAvgSpeed_Object = MibTableColumn
apVoiceSvcAvgSpeed = _ApVoiceSvcAvgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 18),
    _ApVoiceSvcAvgSpeed_Type()
)
apVoiceSvcAvgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVoiceSvcAvgSpeed.setStatus("current")
_ApVoiceSvcMaxBurst_Type = Integer32
_ApVoiceSvcMaxBurst_Object = MibTableColumn
apVoiceSvcMaxBurst = _ApVoiceSvcMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 19),
    _ApVoiceSvcMaxBurst_Type()
)
apVoiceSvcMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVoiceSvcMaxBurst.setStatus("current")
_ApVoiceSvcPriority_Type = Integer32
_ApVoiceSvcPriority_Object = MibTableColumn
apVoiceSvcPriority = _ApVoiceSvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 20),
    _ApVoiceSvcPriority_Type()
)
apVoiceSvcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVoiceSvcPriority.setStatus("current")
_ApVoiceSvcResPriority_Type = Integer32
_ApVoiceSvcResPriority_Object = MibTableColumn
apVoiceSvcResPriority = _ApVoiceSvcResPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 21),
    _ApVoiceSvcResPriority_Type()
)
apVoiceSvcResPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVoiceSvcResPriority.setStatus("current")
_ApVideoSvcAvgSpeed_Type = Integer32
_ApVideoSvcAvgSpeed_Object = MibTableColumn
apVideoSvcAvgSpeed = _ApVideoSvcAvgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 22),
    _ApVideoSvcAvgSpeed_Type()
)
apVideoSvcAvgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVideoSvcAvgSpeed.setStatus("current")
_ApVideoSvcMaxBurst_Type = Integer32
_ApVideoSvcMaxBurst_Object = MibTableColumn
apVideoSvcMaxBurst = _ApVideoSvcMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 23),
    _ApVideoSvcMaxBurst_Type()
)
apVideoSvcMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVideoSvcMaxBurst.setStatus("current")
_ApVideoSvcPriority_Type = Integer32
_ApVideoSvcPriority_Object = MibTableColumn
apVideoSvcPriority = _ApVideoSvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 24),
    _ApVideoSvcPriority_Type()
)
apVideoSvcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVideoSvcPriority.setStatus("current")
_ApVideoSvcResPriority_Type = Integer32
_ApVideoSvcResPriority_Object = MibTableColumn
apVideoSvcResPriority = _ApVideoSvcResPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 2, 1, 25),
    _ApVideoSvcResPriority_Type()
)
apVideoSvcResPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVideoSvcResPriority.setStatus("current")
_ApQosBackgroundCfgTable_Object = MibTable
apQosBackgroundCfgTable = _ApQosBackgroundCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 3)
)
if mibBuilder.loadTexts:
    apQosBackgroundCfgTable.setStatus("current")
_ApQosBackgroundCfgEntry_Object = MibTableRow
apQosBackgroundCfgEntry = _ApQosBackgroundCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 3, 1)
)
apQosBackgroundCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apQosBackgroundCfgEntry.setStatus("current")
_ApBgMaxSvcCnt_Type = Integer32
_ApBgMaxSvcCnt_Object = MibTableColumn
apBgMaxSvcCnt = _ApBgMaxSvcCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 3, 1, 1),
    _ApBgMaxSvcCnt_Type()
)
apBgMaxSvcCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBgMaxSvcCnt.setStatus("current")
_ApBgSvcBW_Type = Integer32
_ApBgSvcBW_Object = MibTableColumn
apBgSvcBW = _ApBgSvcBW_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 3, 1, 2),
    _ApBgSvcBW_Type()
)
apBgSvcBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBgSvcBW.setStatus("current")
_ApBgSvcBWPercent_Type = Integer32
_ApBgSvcBWPercent_Object = MibTableColumn
apBgSvcBWPercent = _ApBgSvcBWPercent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 3, 1, 3),
    _ApBgSvcBWPercent_Type()
)
apBgSvcBWPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBgSvcBWPercent.setStatus("current")
_ApBgIsUseWREDAlg_Type = TruthValue
_ApBgIsUseWREDAlg_Object = MibTableColumn
apBgIsUseWREDAlg = _ApBgIsUseWREDAlg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 3, 1, 4),
    _ApBgIsUseWREDAlg_Type()
)
apBgIsUseWREDAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBgIsUseWREDAlg.setStatus("current")
_ApBgIsUseTrafficShaping_Type = TruthValue
_ApBgIsUseTrafficShaping_Object = MibTableColumn
apBgIsUseTrafficShaping = _ApBgIsUseTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 3, 1, 5),
    _ApBgIsUseTrafficShaping_Type()
)
apBgIsUseTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBgIsUseTrafficShaping.setStatus("current")
_ApQosBestEffortCfgTable_Object = MibTable
apQosBestEffortCfgTable = _ApQosBestEffortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 4)
)
if mibBuilder.loadTexts:
    apQosBestEffortCfgTable.setStatus("current")
_ApQosBestEffortCfgEntry_Object = MibTableRow
apQosBestEffortCfgEntry = _ApQosBestEffortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 4, 1)
)
apQosBestEffortCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apQosBestEffortCfgEntry.setStatus("current")
_ApBeMaxSvcCnt_Type = Integer32
_ApBeMaxSvcCnt_Object = MibTableColumn
apBeMaxSvcCnt = _ApBeMaxSvcCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 4, 1, 1),
    _ApBeMaxSvcCnt_Type()
)
apBeMaxSvcCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBeMaxSvcCnt.setStatus("current")
_ApBeSvcBW_Type = Integer32
_ApBeSvcBW_Object = MibTableColumn
apBeSvcBW = _ApBeSvcBW_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 4, 1, 2),
    _ApBeSvcBW_Type()
)
apBeSvcBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBeSvcBW.setStatus("current")
_ApBeSvcBWPercent_Type = Integer32
_ApBeSvcBWPercent_Object = MibTableColumn
apBeSvcBWPercent = _ApBeSvcBWPercent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 4, 1, 3),
    _ApBeSvcBWPercent_Type()
)
apBeSvcBWPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBeSvcBWPercent.setStatus("current")
_ApBeIsUseWREDAlg_Type = TruthValue
_ApBeIsUseWREDAlg_Object = MibTableColumn
apBeIsUseWREDAlg = _ApBeIsUseWREDAlg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 4, 1, 4),
    _ApBeIsUseWREDAlg_Type()
)
apBeIsUseWREDAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBeIsUseWREDAlg.setStatus("current")
_ApBeIsUseTrafficShaping_Type = TruthValue
_ApBeIsUseTrafficShaping_Object = MibTableColumn
apBeIsUseTrafficShaping = _ApBeIsUseTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 4, 1, 5),
    _ApBeIsUseTrafficShaping_Type()
)
apBeIsUseTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBeIsUseTrafficShaping.setStatus("current")
_ApQosVoiceCfgTable_Object = MibTable
apQosVoiceCfgTable = _ApQosVoiceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 5)
)
if mibBuilder.loadTexts:
    apQosVoiceCfgTable.setStatus("current")
_ApQosVoiceCfgEntry_Object = MibTableRow
apQosVoiceCfgEntry = _ApQosVoiceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 5, 1)
)
apQosVoiceCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apQosVoiceCfgEntry.setStatus("current")
_ApVoiceMaxSvcCnt_Type = Integer32
_ApVoiceMaxSvcCnt_Object = MibTableColumn
apVoiceMaxSvcCnt = _ApVoiceMaxSvcCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 5, 1, 1),
    _ApVoiceMaxSvcCnt_Type()
)
apVoiceMaxSvcCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVoiceMaxSvcCnt.setStatus("current")
_ApVoiceSvcBW_Type = Integer32
_ApVoiceSvcBW_Object = MibTableColumn
apVoiceSvcBW = _ApVoiceSvcBW_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 5, 1, 2),
    _ApVoiceSvcBW_Type()
)
apVoiceSvcBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVoiceSvcBW.setStatus("current")
_ApVoiceSvcBWPercent_Type = Integer32
_ApVoiceSvcBWPercent_Object = MibTableColumn
apVoiceSvcBWPercent = _ApVoiceSvcBWPercent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 5, 1, 3),
    _ApVoiceSvcBWPercent_Type()
)
apVoiceSvcBWPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVoiceSvcBWPercent.setStatus("current")
_ApVoiceIsUseStreamBasedQueue_Type = TruthValue
_ApVoiceIsUseStreamBasedQueue_Object = MibTableColumn
apVoiceIsUseStreamBasedQueue = _ApVoiceIsUseStreamBasedQueue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 5, 1, 4),
    _ApVoiceIsUseStreamBasedQueue_Type()
)
apVoiceIsUseStreamBasedQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVoiceIsUseStreamBasedQueue.setStatus("current")
_ApVoiceStreamMaxQueueLen_Type = Integer32
_ApVoiceStreamMaxQueueLen_Object = MibTableColumn
apVoiceStreamMaxQueueLen = _ApVoiceStreamMaxQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 5, 1, 5),
    _ApVoiceStreamMaxQueueLen_Type()
)
apVoiceStreamMaxQueueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVoiceStreamMaxQueueLen.setStatus("current")
_ApVoiceStreamAvgSpeed_Type = Integer32
_ApVoiceStreamAvgSpeed_Object = MibTableColumn
apVoiceStreamAvgSpeed = _ApVoiceStreamAvgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 5, 1, 6),
    _ApVoiceStreamAvgSpeed_Type()
)
apVoiceStreamAvgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVoiceStreamAvgSpeed.setStatus("current")
_ApVoiceStreamMaxBurst_Type = Integer32
_ApVoiceStreamMaxBurst_Object = MibTableColumn
apVoiceStreamMaxBurst = _ApVoiceStreamMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 5, 1, 7),
    _ApVoiceStreamMaxBurst_Type()
)
apVoiceStreamMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVoiceStreamMaxBurst.setStatus("current")
_ApVoiceIsUseWREDAlg_Type = TruthValue
_ApVoiceIsUseWREDAlg_Object = MibTableColumn
apVoiceIsUseWREDAlg = _ApVoiceIsUseWREDAlg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 5, 1, 8),
    _ApVoiceIsUseWREDAlg_Type()
)
apVoiceIsUseWREDAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVoiceIsUseWREDAlg.setStatus("current")
_ApVoiceIsUseTrafficShaping_Type = TruthValue
_ApVoiceIsUseTrafficShaping_Object = MibTableColumn
apVoiceIsUseTrafficShaping = _ApVoiceIsUseTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 5, 1, 9),
    _ApVoiceIsUseTrafficShaping_Type()
)
apVoiceIsUseTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVoiceIsUseTrafficShaping.setStatus("current")
_ApQosVedioCfgTable_Object = MibTable
apQosVedioCfgTable = _ApQosVedioCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 6)
)
if mibBuilder.loadTexts:
    apQosVedioCfgTable.setStatus("current")
_ApQosVedioCfgEntry_Object = MibTableRow
apQosVedioCfgEntry = _ApQosVedioCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 6, 1)
)
apQosVedioCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apQosVedioCfgEntry.setStatus("current")
_ApVedioMaxSvcCnt_Type = Integer32
_ApVedioMaxSvcCnt_Object = MibTableColumn
apVedioMaxSvcCnt = _ApVedioMaxSvcCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 6, 1, 1),
    _ApVedioMaxSvcCnt_Type()
)
apVedioMaxSvcCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVedioMaxSvcCnt.setStatus("current")
_ApVedioSvcBW_Type = Integer32
_ApVedioSvcBW_Object = MibTableColumn
apVedioSvcBW = _ApVedioSvcBW_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 6, 1, 2),
    _ApVedioSvcBW_Type()
)
apVedioSvcBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVedioSvcBW.setStatus("current")
_ApVedioSvcBWPercent_Type = Integer32
_ApVedioSvcBWPercent_Object = MibTableColumn
apVedioSvcBWPercent = _ApVedioSvcBWPercent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 6, 1, 3),
    _ApVedioSvcBWPercent_Type()
)
apVedioSvcBWPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVedioSvcBWPercent.setStatus("current")
_ApVedioIsUseStreamBasedQueue_Type = TruthValue
_ApVedioIsUseStreamBasedQueue_Object = MibTableColumn
apVedioIsUseStreamBasedQueue = _ApVedioIsUseStreamBasedQueue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 6, 1, 4),
    _ApVedioIsUseStreamBasedQueue_Type()
)
apVedioIsUseStreamBasedQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVedioIsUseStreamBasedQueue.setStatus("current")
_ApVedioStreamMaxQueueLen_Type = Integer32
_ApVedioStreamMaxQueueLen_Object = MibTableColumn
apVedioStreamMaxQueueLen = _ApVedioStreamMaxQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 6, 1, 5),
    _ApVedioStreamMaxQueueLen_Type()
)
apVedioStreamMaxQueueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVedioStreamMaxQueueLen.setStatus("current")
_ApVedioStreamAvgSpeed_Type = Integer32
_ApVedioStreamAvgSpeed_Object = MibTableColumn
apVedioStreamAvgSpeed = _ApVedioStreamAvgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 6, 1, 6),
    _ApVedioStreamAvgSpeed_Type()
)
apVedioStreamAvgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVedioStreamAvgSpeed.setStatus("current")
_ApVedioStreamMaxBurst_Type = Integer32
_ApVedioStreamMaxBurst_Object = MibTableColumn
apVedioStreamMaxBurst = _ApVedioStreamMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 6, 1, 7),
    _ApVedioStreamMaxBurst_Type()
)
apVedioStreamMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVedioStreamMaxBurst.setStatus("current")
_ApVedioIsUseWREDAlg_Type = TruthValue
_ApVedioIsUseWREDAlg_Object = MibTableColumn
apVedioIsUseWREDAlg = _ApVedioIsUseWREDAlg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 6, 1, 8),
    _ApVedioIsUseWREDAlg_Type()
)
apVedioIsUseWREDAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVedioIsUseWREDAlg.setStatus("current")
_ApVedioIsUseTrafficShaping_Type = TruthValue
_ApVedioIsUseTrafficShaping_Object = MibTableColumn
apVedioIsUseTrafficShaping = _ApVedioIsUseTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 7, 6, 1, 9),
    _ApVedioIsUseTrafficShaping_Type()
)
apVedioIsUseTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVedioIsUseTrafficShaping.setStatus("current")
_ApWapiCfg_ObjectIdentity = ObjectIdentity
apWapiCfg = _ApWapiCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8)
)
_ApWapiProtocolCfgTable_Object = MibTable
apWapiProtocolCfgTable = _ApWapiProtocolCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1)
)
if mibBuilder.loadTexts:
    apWapiProtocolCfgTable.setStatus("current")
_ApWapiProtocolCfgEntry_Object = MibTableRow
apWapiProtocolCfgEntry = _ApWapiProtocolCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1)
)
apWapiProtocolCfgEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FAT-AP-CF-MIB", "apWlanId"),
)
if mibBuilder.loadTexts:
    apWapiProtocolCfgEntry.setStatus("current")
_ApConfigVersion_Type = Integer32
_ApConfigVersion_Object = MibTableColumn
apConfigVersion = _ApConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 1),
    _ApConfigVersion_Type()
)
apConfigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apConfigVersion.setStatus("current")
_ApControlledAuthControl_Type = TruthValue
_ApControlledAuthControl_Object = MibTableColumn
apControlledAuthControl = _ApControlledAuthControl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 2),
    _ApControlledAuthControl_Type()
)
apControlledAuthControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apControlledAuthControl.setStatus("current")
_ApControlledPortControl_Type = Integer32
_ApControlledPortControl_Object = MibTableColumn
apControlledPortControl = _ApControlledPortControl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 3),
    _ApControlledPortControl_Type()
)
apControlledPortControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apControlledPortControl.setStatus("current")
_ApWapiOptionImplemented_Type = TruthValue
_ApWapiOptionImplemented_Object = MibTableColumn
apWapiOptionImplemented = _ApWapiOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 4),
    _ApWapiOptionImplemented_Type()
)
apWapiOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWapiOptionImplemented.setStatus("current")
_ApWapiPreauthImplemented_Type = TruthValue
_ApWapiPreauthImplemented_Object = MibTableColumn
apWapiPreauthImplemented = _ApWapiPreauthImplemented_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 5),
    _ApWapiPreauthImplemented_Type()
)
apWapiPreauthImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWapiPreauthImplemented.setStatus("current")
_ApWapiEnabled_Type = TruthValue
_ApWapiEnabled_Object = MibTableColumn
apWapiEnabled = _ApWapiEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 6),
    _ApWapiEnabled_Type()
)
apWapiEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWapiEnabled.setStatus("current")
_ApWapiPreauthEnabled_Type = TruthValue
_ApWapiPreauthEnabled_Object = MibTableColumn
apWapiPreauthEnabled = _ApWapiPreauthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 7),
    _ApWapiPreauthEnabled_Type()
)
apWapiPreauthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWapiPreauthEnabled.setStatus("current")
_ApUnicastKeysSupported_Type = Unsigned32
_ApUnicastKeysSupported_Object = MibTableColumn
apUnicastKeysSupported = _ApUnicastKeysSupported_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 8),
    _ApUnicastKeysSupported_Type()
)
apUnicastKeysSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUnicastKeysSupported.setStatus("current")
_ApUnicastRekeyMethod_Type = Integer32
_ApUnicastRekeyMethod_Object = MibTableColumn
apUnicastRekeyMethod = _ApUnicastRekeyMethod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 9),
    _ApUnicastRekeyMethod_Type()
)
apUnicastRekeyMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apUnicastRekeyMethod.setStatus("current")
_ApUnicastRekeyTime_Type = Unsigned32
_ApUnicastRekeyTime_Object = MibTableColumn
apUnicastRekeyTime = _ApUnicastRekeyTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 10),
    _ApUnicastRekeyTime_Type()
)
apUnicastRekeyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apUnicastRekeyTime.setStatus("current")
_ApUnicastRekeyPackets_Type = Unsigned32
_ApUnicastRekeyPackets_Object = MibTableColumn
apUnicastRekeyPackets = _ApUnicastRekeyPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 11),
    _ApUnicastRekeyPackets_Type()
)
apUnicastRekeyPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apUnicastRekeyPackets.setStatus("current")
_ApMulticastCipher_Type = OctetString
_ApMulticastCipher_Object = MibTableColumn
apMulticastCipher = _ApMulticastCipher_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 12),
    _ApMulticastCipher_Type()
)
apMulticastCipher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMulticastCipher.setStatus("current")
_ApMulticastRekeyMethod_Type = Integer32
_ApMulticastRekeyMethod_Object = MibTableColumn
apMulticastRekeyMethod = _ApMulticastRekeyMethod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 13),
    _ApMulticastRekeyMethod_Type()
)
apMulticastRekeyMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMulticastRekeyMethod.setStatus("current")
_ApMulticastRekeyTime_Type = Unsigned32
_ApMulticastRekeyTime_Object = MibTableColumn
apMulticastRekeyTime = _ApMulticastRekeyTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 14),
    _ApMulticastRekeyTime_Type()
)
apMulticastRekeyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMulticastRekeyTime.setStatus("current")
_ApMulticastRekeyPackets_Type = Unsigned32
_ApMulticastRekeyPackets_Object = MibTableColumn
apMulticastRekeyPackets = _ApMulticastRekeyPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 15),
    _ApMulticastRekeyPackets_Type()
)
apMulticastRekeyPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMulticastRekeyPackets.setStatus("current")
_ApMulticastRekeyStrict_Type = TruthValue
_ApMulticastRekeyStrict_Object = MibTableColumn
apMulticastRekeyStrict = _ApMulticastRekeyStrict_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 16),
    _ApMulticastRekeyStrict_Type()
)
apMulticastRekeyStrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMulticastRekeyStrict.setStatus("current")
_ApPSKValue_Type = OctetString
_ApPSKValue_Object = MibTableColumn
apPSKValue = _ApPSKValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 17),
    _ApPSKValue_Type()
)
apPSKValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPSKValue.setStatus("current")
_ApPSKPassPhrase_Type = DisplayString
_ApPSKPassPhrase_Object = MibTableColumn
apPSKPassPhrase = _ApPSKPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 18),
    _ApPSKPassPhrase_Type()
)
apPSKPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPSKPassPhrase.setStatus("current")
_ApCertificateUpdateCount_Type = Unsigned32
_ApCertificateUpdateCount_Object = MibTableColumn
apCertificateUpdateCount = _ApCertificateUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 19),
    _ApCertificateUpdateCount_Type()
)
apCertificateUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCertificateUpdateCount.setStatus("current")
_ApMulticastUpdateCount_Type = Unsigned32
_ApMulticastUpdateCount_Object = MibTableColumn
apMulticastUpdateCount = _ApMulticastUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 20),
    _ApMulticastUpdateCount_Type()
)
apMulticastUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMulticastUpdateCount.setStatus("current")
_ApUnicastUpdateCount_Type = Unsigned32
_ApUnicastUpdateCount_Object = MibTableColumn
apUnicastUpdateCount = _ApUnicastUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 21),
    _ApUnicastUpdateCount_Type()
)
apUnicastUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apUnicastUpdateCount.setStatus("current")
_ApMulticastCipherSize_Type = Unsigned32
_ApMulticastCipherSize_Object = MibTableColumn
apMulticastCipherSize = _ApMulticastCipherSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 22),
    _ApMulticastCipherSize_Type()
)
apMulticastCipherSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMulticastCipherSize.setStatus("current")
_ApBKLifetime_Type = Unsigned32
_ApBKLifetime_Object = MibTableColumn
apBKLifetime = _ApBKLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 23),
    _ApBKLifetime_Type()
)
apBKLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBKLifetime.setStatus("current")
_ApBKReauthThreshold_Type = Unsigned32
_ApBKReauthThreshold_Object = MibTableColumn
apBKReauthThreshold = _ApBKReauthThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 24),
    _ApBKReauthThreshold_Type()
)
apBKReauthThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBKReauthThreshold.setStatus("current")
_ApSATimeout_Type = Unsigned32
_ApSATimeout_Object = MibTableColumn
apSATimeout = _ApSATimeout_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 25),
    _ApSATimeout_Type()
)
apSATimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSATimeout.setStatus("current")
_ApAuthSuiteSelected_Type = OctetString
_ApAuthSuiteSelected_Object = MibTableColumn
apAuthSuiteSelected = _ApAuthSuiteSelected_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 26),
    _ApAuthSuiteSelected_Type()
)
apAuthSuiteSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAuthSuiteSelected.setStatus("current")
_ApUnicastCipherSelected_Type = OctetString
_ApUnicastCipherSelected_Object = MibTableColumn
apUnicastCipherSelected = _ApUnicastCipherSelected_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 27),
    _ApUnicastCipherSelected_Type()
)
apUnicastCipherSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUnicastCipherSelected.setStatus("current")
_ApMulticastCipherSelected_Type = OctetString
_ApMulticastCipherSelected_Object = MibTableColumn
apMulticastCipherSelected = _ApMulticastCipherSelected_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 28),
    _ApMulticastCipherSelected_Type()
)
apMulticastCipherSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMulticastCipherSelected.setStatus("current")
_ApBKIDUsed_Type = OctetString
_ApBKIDUsed_Object = MibTableColumn
apBKIDUsed = _ApBKIDUsed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 29),
    _ApBKIDUsed_Type()
)
apBKIDUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBKIDUsed.setStatus("current")
_ApAuthSuiteRequested_Type = OctetString
_ApAuthSuiteRequested_Object = MibTableColumn
apAuthSuiteRequested = _ApAuthSuiteRequested_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 30),
    _ApAuthSuiteRequested_Type()
)
apAuthSuiteRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAuthSuiteRequested.setStatus("current")
_ApUnicastCipherRequested_Type = OctetString
_ApUnicastCipherRequested_Object = MibTableColumn
apUnicastCipherRequested = _ApUnicastCipherRequested_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 31),
    _ApUnicastCipherRequested_Type()
)
apUnicastCipherRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUnicastCipherRequested.setStatus("current")
_ApMulticastCipherRequested_Type = OctetString
_ApMulticastCipherRequested_Object = MibTableColumn
apMulticastCipherRequested = _ApMulticastCipherRequested_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 1, 1, 32),
    _ApMulticastCipherRequested_Type()
)
apMulticastCipherRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMulticastCipherRequested.setStatus("current")
_ApWapiUnicastCfgTable_Object = MibTable
apWapiUnicastCfgTable = _ApWapiUnicastCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 2)
)
if mibBuilder.loadTexts:
    apWapiUnicastCfgTable.setStatus("current")
_ApWapiUnicastCfgEntry_Object = MibTableRow
apWapiUnicastCfgEntry = _ApWapiUnicastCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 2, 1)
)
apWapiUnicastCfgEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FAT-AP-CF-MIB", "apWlanId"),
)
if mibBuilder.loadTexts:
    apWapiUnicastCfgEntry.setStatus("current")
_ApUnicastCipher_Type = OctetString
_ApUnicastCipher_Object = MibTableColumn
apUnicastCipher = _ApUnicastCipher_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 2, 1, 1),
    _ApUnicastCipher_Type()
)
apUnicastCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUnicastCipher.setStatus("current")
_ApUnicastCipherEnabled_Type = TruthValue
_ApUnicastCipherEnabled_Object = MibTableColumn
apUnicastCipherEnabled = _ApUnicastCipherEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 2, 1, 2),
    _ApUnicastCipherEnabled_Type()
)
apUnicastCipherEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apUnicastCipherEnabled.setStatus("current")
_ApUnicastCipherSize_Type = Unsigned32
_ApUnicastCipherSize_Object = MibTableColumn
apUnicastCipherSize = _ApUnicastCipherSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 2, 1, 3),
    _ApUnicastCipherSize_Type()
)
apUnicastCipherSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUnicastCipherSize.setStatus("current")
_ApWapiAKMCfgTable_Object = MibTable
apWapiAKMCfgTable = _ApWapiAKMCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 3)
)
if mibBuilder.loadTexts:
    apWapiAKMCfgTable.setStatus("current")
_ApWapiAKMCfgEntry_Object = MibTableRow
apWapiAKMCfgEntry = _ApWapiAKMCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 3, 1)
)
apWapiAKMCfgEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FAT-AP-CF-MIB", "apWlanId"),
)
if mibBuilder.loadTexts:
    apWapiAKMCfgEntry.setStatus("current")
_ApAuthenticationSuite_Type = OctetString
_ApAuthenticationSuite_Object = MibTableColumn
apAuthenticationSuite = _ApAuthenticationSuite_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 3, 1, 1),
    _ApAuthenticationSuite_Type()
)
apAuthenticationSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAuthenticationSuite.setStatus("current")
_ApAuthenticationSuiteEnabled_Type = TruthValue
_ApAuthenticationSuiteEnabled_Object = MibTableColumn
apAuthenticationSuiteEnabled = _ApAuthenticationSuiteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 8, 3, 1, 2),
    _ApAuthenticationSuiteEnabled_Type()
)
apAuthenticationSuiteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAuthenticationSuiteEnabled.setStatus("current")
_ApSyslogCfg_ObjectIdentity = ObjectIdentity
apSyslogCfg = _ApSyslogCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 9)
)
_ApSyslogSvcEnable_Type = TruthValue
_ApSyslogSvcEnable_Object = MibScalar
apSyslogSvcEnable = _ApSyslogSvcEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 9, 1),
    _ApSyslogSvcEnable_Type()
)
apSyslogSvcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSyslogSvcEnable.setStatus("current")
_ApSyslogReportEventLevel_Type = Integer32
_ApSyslogReportEventLevel_Object = MibScalar
apSyslogReportEventLevel = _ApSyslogReportEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 9, 2),
    _ApSyslogReportEventLevel_Type()
)
apSyslogReportEventLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSyslogReportEventLevel.setStatus("current")
_ApSyslogSvrCfgTable_Object = MibTable
apSyslogSvrCfgTable = _ApSyslogSvrCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 9, 3)
)
if mibBuilder.loadTexts:
    apSyslogSvrCfgTable.setStatus("current")
_ApSyslogSvrCfgEntry_Object = MibTableRow
apSyslogSvrCfgEntry = _ApSyslogSvrCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 9, 3, 1)
)
apSyslogSvrCfgEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FAT-AP-CF-MIB", "apSyslogSvrIndex"),
)
if mibBuilder.loadTexts:
    apSyslogSvrCfgEntry.setStatus("current")
_ApSyslogSvrIndex_Type = Integer32
_ApSyslogSvrIndex_Object = MibTableColumn
apSyslogSvrIndex = _ApSyslogSvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 9, 3, 1, 1),
    _ApSyslogSvrIndex_Type()
)
apSyslogSvrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSyslogSvrIndex.setStatus("current")
_ApSyslogServerAddr_Type = TAddress
_ApSyslogServerAddr_Object = MibTableColumn
apSyslogServerAddr = _ApSyslogServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 9, 3, 1, 2),
    _ApSyslogServerAddr_Type()
)
apSyslogServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSyslogServerAddr.setStatus("current")
_ApSyslogStatus_Type = RowStatus
_ApSyslogStatus_Object = MibTableColumn
apSyslogStatus = _ApSyslogStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 9, 3, 1, 3),
    _ApSyslogStatus_Type()
)
apSyslogStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSyslogStatus.setStatus("current")
_ApSoftwareUpdate_ObjectIdentity = ObjectIdentity
apSoftwareUpdate = _ApSoftwareUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 10)
)
_ApLoadFlag_Type = Integer32
_ApLoadFlag_Object = MibScalar
apLoadFlag = _ApLoadFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 10, 1),
    _ApLoadFlag_Type()
)
apLoadFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLoadFlag.setStatus("current")
_ApFileName_Type = DisplayString
_ApFileName_Object = MibScalar
apFileName = _ApFileName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 10, 2),
    _ApFileName_Type()
)
apFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFileName.setStatus("current")
_ApFileType_Type = Integer32
_ApFileType_Object = MibScalar
apFileType = _ApFileType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 10, 3),
    _ApFileType_Type()
)
apFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFileType.setStatus("current")
_ApTransProtocol_Type = Integer32
_ApTransProtocol_Object = MibScalar
apTransProtocol = _ApTransProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 10, 4),
    _ApTransProtocol_Type()
)
apTransProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTransProtocol.setStatus("current")
_ApServerAddr_Type = IpAddress
_ApServerAddr_Object = MibScalar
apServerAddr = _ApServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 10, 5),
    _ApServerAddr_Type()
)
apServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apServerAddr.setStatus("current")
_ApServerPort_Type = Integer32
_ApServerPort_Object = MibScalar
apServerPort = _ApServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 10, 6),
    _ApServerPort_Type()
)
apServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apServerPort.setStatus("current")
_ApServerUsername_Type = DisplayString
_ApServerUsername_Object = MibScalar
apServerUsername = _ApServerUsername_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 10, 7),
    _ApServerUsername_Type()
)
apServerUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apServerUsername.setStatus("current")
_ApServerPasswd_Type = DisplayString
_ApServerPasswd_Object = MibScalar
apServerPasswd = _ApServerPasswd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 10, 8),
    _ApServerPasswd_Type()
)
apServerPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apServerPasswd.setStatus("current")
_ApTransStatus_Type = Integer32
_ApTransStatus_Object = MibScalar
apTransStatus = _ApTransStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 10, 9),
    _ApTransStatus_Type()
)
apTransStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTransStatus.setStatus("current")
_ApFailReason_Type = DisplayString
_ApFailReason_Object = MibScalar
apFailReason = _ApFailReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 10, 10),
    _ApFailReason_Type()
)
apFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFailReason.setStatus("current")
_ApCfgFileDistribute_ObjectIdentity = ObjectIdentity
apCfgFileDistribute = _ApCfgFileDistribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 11)
)
_ApCfgFileLoadFlag_Type = Integer32
_ApCfgFileLoadFlag_Object = MibScalar
apCfgFileLoadFlag = _ApCfgFileLoadFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 11, 1),
    _ApCfgFileLoadFlag_Type()
)
apCfgFileLoadFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCfgFileLoadFlag.setStatus("current")
_ApCfgFileFileName_Type = DisplayString
_ApCfgFileFileName_Object = MibScalar
apCfgFileFileName = _ApCfgFileFileName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 11, 2),
    _ApCfgFileFileName_Type()
)
apCfgFileFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCfgFileFileName.setStatus("current")
_ApCfgFileFileType_Type = Integer32
_ApCfgFileFileType_Object = MibScalar
apCfgFileFileType = _ApCfgFileFileType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 11, 3),
    _ApCfgFileFileType_Type()
)
apCfgFileFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCfgFileFileType.setStatus("current")
_ApCfgFileTransProtocol_Type = Integer32
_ApCfgFileTransProtocol_Object = MibScalar
apCfgFileTransProtocol = _ApCfgFileTransProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 11, 4),
    _ApCfgFileTransProtocol_Type()
)
apCfgFileTransProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCfgFileTransProtocol.setStatus("current")
_ApCfgFileServerAddr_Type = IpAddress
_ApCfgFileServerAddr_Object = MibScalar
apCfgFileServerAddr = _ApCfgFileServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 11, 5),
    _ApCfgFileServerAddr_Type()
)
apCfgFileServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCfgFileServerAddr.setStatus("current")
_ApCfgFileServerPort_Type = Integer32
_ApCfgFileServerPort_Object = MibScalar
apCfgFileServerPort = _ApCfgFileServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 11, 6),
    _ApCfgFileServerPort_Type()
)
apCfgFileServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCfgFileServerPort.setStatus("current")
_ApCfgFileServerUsername_Type = DisplayString
_ApCfgFileServerUsername_Object = MibScalar
apCfgFileServerUsername = _ApCfgFileServerUsername_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 11, 7),
    _ApCfgFileServerUsername_Type()
)
apCfgFileServerUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCfgFileServerUsername.setStatus("current")
_ApCfgFileServerPasswd_Type = DisplayString
_ApCfgFileServerPasswd_Object = MibScalar
apCfgFileServerPasswd = _ApCfgFileServerPasswd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 11, 8),
    _ApCfgFileServerPasswd_Type()
)
apCfgFileServerPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCfgFileServerPasswd.setStatus("current")
_ApCfgFileTransStatus_Type = Integer32
_ApCfgFileTransStatus_Object = MibScalar
apCfgFileTransStatus = _ApCfgFileTransStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 11, 9),
    _ApCfgFileTransStatus_Type()
)
apCfgFileTransStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCfgFileTransStatus.setStatus("current")
_ApCfgFileFailReason_Type = DisplayString
_ApCfgFileFailReason_Object = MibScalar
apCfgFileFailReason = _ApCfgFileFailReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 11, 10),
    _ApCfgFileFailReason_Type()
)
apCfgFileFailReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCfgFileFailReason.setStatus("current")
_ApAccessControl_ObjectIdentity = ObjectIdentity
apAccessControl = _ApAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 12)
)
_ApTerminalPermitTable_Object = MibTable
apTerminalPermitTable = _ApTerminalPermitTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 12, 1)
)
if mibBuilder.loadTexts:
    apTerminalPermitTable.setStatus("current")
_ApTerminalPermitEntry_Object = MibTableRow
apTerminalPermitEntry = _ApTerminalPermitEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 12, 1, 1)
)
apTerminalPermitEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FAT-AP-CF-MIB", "apWhiteListIndex"),
)
if mibBuilder.loadTexts:
    apTerminalPermitEntry.setStatus("current")
_ApWhiteListIndex_Type = Integer32
_ApWhiteListIndex_Object = MibTableColumn
apWhiteListIndex = _ApWhiteListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 12, 1, 1, 1),
    _ApWhiteListIndex_Type()
)
apWhiteListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWhiteListIndex.setStatus("current")
_ApPermitMAC_Type = MacAddress
_ApPermitMAC_Object = MibTableColumn
apPermitMAC = _ApPermitMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 12, 1, 1, 2),
    _ApPermitMAC_Type()
)
apPermitMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apPermitMAC.setStatus("current")
_ApWhiteListStatus_Type = RowStatus
_ApWhiteListStatus_Object = MibTableColumn
apWhiteListStatus = _ApWhiteListStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 12, 1, 1, 3),
    _ApWhiteListStatus_Type()
)
apWhiteListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apWhiteListStatus.setStatus("current")
_ApTerminalDeniedTable_Object = MibTable
apTerminalDeniedTable = _ApTerminalDeniedTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 12, 2)
)
if mibBuilder.loadTexts:
    apTerminalDeniedTable.setStatus("current")
_ApTerminalDeniedEntry_Object = MibTableRow
apTerminalDeniedEntry = _ApTerminalDeniedEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 12, 2, 1)
)
apTerminalDeniedEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FAT-AP-CF-MIB", "apBlackListIndex"),
)
if mibBuilder.loadTexts:
    apTerminalDeniedEntry.setStatus("current")
_ApBlackListIndex_Type = Integer32
_ApBlackListIndex_Object = MibTableColumn
apBlackListIndex = _ApBlackListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 12, 2, 1, 1),
    _ApBlackListIndex_Type()
)
apBlackListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlackListIndex.setStatus("current")
_ApAttackDeviceMAC_Type = MacAddress
_ApAttackDeviceMAC_Object = MibTableColumn
apAttackDeviceMAC = _ApAttackDeviceMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 12, 2, 1, 2),
    _ApAttackDeviceMAC_Type()
)
apAttackDeviceMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAttackDeviceMAC.setStatus("current")
_ApBlackListStatus_Type = RowStatus
_ApBlackListStatus_Object = MibTableColumn
apBlackListStatus = _ApBlackListStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 12, 2, 1, 3),
    _ApBlackListStatus_Type()
)
apBlackListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apBlackListStatus.setStatus("current")
_ApTrapConfig_ObjectIdentity = ObjectIdentity
apTrapConfig = _ApTrapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 13)
)
_ApTrapResendWaitingTime_Type = Integer32
_ApTrapResendWaitingTime_Object = MibScalar
apTrapResendWaitingTime = _ApTrapResendWaitingTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 13, 1),
    _ApTrapResendWaitingTime_Type()
)
apTrapResendWaitingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrapResendWaitingTime.setStatus("current")
_ApCPUusageThreshhd_Type = Integer32
_ApCPUusageThreshhd_Object = MibScalar
apCPUusageThreshhd = _ApCPUusageThreshhd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 13, 2),
    _ApCPUusageThreshhd_Type()
)
apCPUusageThreshhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCPUusageThreshhd.setStatus("current")
_ApMemUsageThreshhd_Type = Integer32
_ApMemUsageThreshhd_Object = MibScalar
apMemUsageThreshhd = _ApMemUsageThreshhd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 13, 3),
    _ApMemUsageThreshhd_Type()
)
apMemUsageThreshhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMemUsageThreshhd.setStatus("current")
_ApAPCoInterfThreshhd_Type = Integer32
_ApAPCoInterfThreshhd_Object = MibScalar
apAPCoInterfThreshhd = _ApAPCoInterfThreshhd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 13, 4),
    _ApAPCoInterfThreshhd_Type()
)
apAPCoInterfThreshhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAPCoInterfThreshhd.setStatus("current")
_ApAPNeiborInterfThreshhd_Type = Integer32
_ApAPNeiborInterfThreshhd_Object = MibScalar
apAPNeiborInterfThreshhd = _ApAPNeiborInterfThreshhd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 13, 5),
    _ApAPNeiborInterfThreshhd_Type()
)
apAPNeiborInterfThreshhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAPNeiborInterfThreshhd.setStatus("current")
_ApStaInterfNumThreshhd_Type = Integer32
_ApStaInterfNumThreshhd_Object = MibScalar
apStaInterfNumThreshhd = _ApStaInterfNumThreshhd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 13, 6),
    _ApStaInterfNumThreshhd_Type()
)
apStaInterfNumThreshhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apStaInterfNumThreshhd.setStatus("current")
_ApHeartbeatOnOff_Type = Integer32
_ApHeartbeatOnOff_Object = MibScalar
apHeartbeatOnOff = _ApHeartbeatOnOff_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 13, 7),
    _ApHeartbeatOnOff_Type()
)
apHeartbeatOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHeartbeatOnOff.setStatus("current")
_ApHeartbeatPeriod_Type = Integer32
_ApHeartbeatPeriod_Object = MibScalar
apHeartbeatPeriod = _ApHeartbeatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 13, 8),
    _ApHeartbeatPeriod_Type()
)
apHeartbeatPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHeartbeatPeriod.setStatus("current")
_ApTrapAddrTable_Object = MibTable
apTrapAddrTable = _ApTrapAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 13, 9)
)
if mibBuilder.loadTexts:
    apTrapAddrTable.setStatus("current")
_ApTrapAddrEntry_Object = MibTableRow
apTrapAddrEntry = _ApTrapAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 13, 9, 1)
)
apTrapAddrEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FAT-AP-CF-MIB", "apTrapDesAddrIndex"),
)
if mibBuilder.loadTexts:
    apTrapAddrEntry.setStatus("current")
_ApTrapDesAddrIndex_Type = Integer32
_ApTrapDesAddrIndex_Object = MibTableColumn
apTrapDesAddrIndex = _ApTrapDesAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 13, 9, 1, 1),
    _ApTrapDesAddrIndex_Type()
)
apTrapDesAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapDesAddrIndex.setStatus("current")
_ApTrapDesIPAddress_Type = IpAddress
_ApTrapDesIPAddress_Object = MibTableColumn
apTrapDesIPAddress = _ApTrapDesIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 13, 9, 1, 2),
    _ApTrapDesIPAddress_Type()
)
apTrapDesIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apTrapDesIPAddress.setStatus("current")
_ApTrapAddrStatus_Type = RowStatus
_ApTrapAddrStatus_Object = MibTableColumn
apTrapAddrStatus = _ApTrapAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 13, 9, 1, 3),
    _ApTrapAddrStatus_Type()
)
apTrapAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apTrapAddrStatus.setStatus("current")
_ApTrapEnabledTable_Object = MibTable
apTrapEnabledTable = _ApTrapEnabledTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 13, 10)
)
if mibBuilder.loadTexts:
    apTrapEnabledTable.setStatus("current")
_ApTrapEnabledEntry_Object = MibTableRow
apTrapEnabledEntry = _ApTrapEnabledEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 13, 10, 1)
)
apTrapEnabledEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FAT-AP-CF-MIB", "apTrapEnabledIndex"),
)
if mibBuilder.loadTexts:
    apTrapEnabledEntry.setStatus("current")
_ApTrapEnabledIndex_Type = Integer32
_ApTrapEnabledIndex_Object = MibTableColumn
apTrapEnabledIndex = _ApTrapEnabledIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 13, 10, 1, 1),
    _ApTrapEnabledIndex_Type()
)
apTrapEnabledIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapEnabledIndex.setStatus("current")
_ApTrapName_Type = DisplayString
_ApTrapName_Object = MibTableColumn
apTrapName = _ApTrapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 13, 10, 1, 2),
    _ApTrapName_Type()
)
apTrapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapName.setStatus("current")
_ApTrapDescr_Type = DisplayString
_ApTrapDescr_Object = MibTableColumn
apTrapDescr = _ApTrapDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 13, 10, 1, 3),
    _ApTrapDescr_Type()
)
apTrapDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrapDescr.setStatus("current")
_ApTrapOnOff_Type = Integer32
_ApTrapOnOff_Object = MibTableColumn
apTrapOnOff = _ApTrapOnOff_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 13, 10, 1, 4),
    _ApTrapOnOff_Type()
)
apTrapOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrapOnOff.setStatus("current")
_ApVlanConfig_ObjectIdentity = ObjectIdentity
apVlanConfig = _ApVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 14)
)
_ApVlanConfigTable_Object = MibTable
apVlanConfigTable = _ApVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 14, 10)
)
if mibBuilder.loadTexts:
    apVlanConfigTable.setStatus("current")
_ApVlanConfigEntry_Object = MibTableRow
apVlanConfigEntry = _ApVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 14, 10, 1)
)
apVlanConfigEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FAT-AP-CF-MIB", "apWlanId"),
)
if mibBuilder.loadTexts:
    apVlanConfigEntry.setStatus("current")
_ApVlanCfgVlanId_Type = Integer32
_ApVlanCfgVlanId_Object = MibTableColumn
apVlanCfgVlanId = _ApVlanCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 14, 10, 1, 1),
    _ApVlanCfgVlanId_Type()
)
apVlanCfgVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apVlanCfgVlanId.setStatus("current")
_ApVlanCfgStatus_Type = RowStatus
_ApVlanCfgStatus_Object = MibTableColumn
apVlanCfgStatus = _ApVlanCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 14, 10, 1, 2),
    _ApVlanCfgStatus_Type()
)
apVlanCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apVlanCfgStatus.setStatus("current")
_ApHeartbeatConfig_ObjectIdentity = ObjectIdentity
apHeartbeatConfig = _ApHeartbeatConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 15)
)
_ApHeartbeatCycle_Type = Integer32
_ApHeartbeatCycle_Object = MibScalar
apHeartbeatCycle = _ApHeartbeatCycle_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 8, 15, 1),
    _ApHeartbeatCycle_Type()
)
apHeartbeatCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHeartbeatCycle.setStatus("current")
_ApPerformanceStatObjects_ObjectIdentity = ObjectIdentity
apPerformanceStatObjects = _ApPerformanceStatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9)
)
_ApSysPerformanceStat_ObjectIdentity = ObjectIdentity
apSysPerformanceStat = _ApSysPerformanceStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 1)
)
_ApCPURTUsage_Type = Integer32
_ApCPURTUsage_Object = MibScalar
apCPURTUsage = _ApCPURTUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 1, 1),
    _ApCPURTUsage_Type()
)
apCPURTUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCPURTUsage.setStatus("current")
_ApCPUAvgUsage_Type = Integer32
_ApCPUAvgUsage_Object = MibScalar
apCPUAvgUsage = _ApCPUAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 1, 2),
    _ApCPUAvgUsage_Type()
)
apCPUAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCPUAvgUsage.setStatus("current")
_ApMemRTUsage_Type = Integer32
_ApMemRTUsage_Object = MibScalar
apMemRTUsage = _ApMemRTUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 1, 3),
    _ApMemRTUsage_Type()
)
apMemRTUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMemRTUsage.setStatus("current")
_ApMemAvgUsage_Type = Integer32
_ApMemAvgUsage_Object = MibScalar
apMemAvgUsage = _ApMemAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 1, 4),
    _ApMemAvgUsage_Type()
)
apMemAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMemAvgUsage.setStatus("current")
_ApConInfoStat_ObjectIdentity = ObjectIdentity
apConInfoStat = _ApConInfoStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 2)
)
_ApApStationAssocSum_Type = Integer32
_ApApStationAssocSum_Object = MibScalar
apApStationAssocSum = _ApApStationAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 2, 1),
    _ApApStationAssocSum_Type()
)
apApStationAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apApStationAssocSum.setStatus("current")
_ApApStationOnlineSum_Type = Integer32
_ApApStationOnlineSum_Object = MibScalar
apApStationOnlineSum = _ApApStationOnlineSum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 2, 2),
    _ApApStationOnlineSum_Type()
)
apApStationOnlineSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apApStationOnlineSum.setStatus("current")
_ApAssocTimes_Type = Counter32
_ApAssocTimes_Object = MibScalar
apAssocTimes = _ApAssocTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 2, 3),
    _ApAssocTimes_Type()
)
apAssocTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAssocTimes.setStatus("current")
_ApAssocFailTimes_Type = Counter32
_ApAssocFailTimes_Object = MibScalar
apAssocFailTimes = _ApAssocFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 2, 4),
    _ApAssocFailTimes_Type()
)
apAssocFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAssocFailTimes.setStatus("current")
_ApReassocTimes_Type = Counter32
_ApReassocTimes_Object = MibScalar
apReassocTimes = _ApReassocTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 2, 5),
    _ApReassocTimes_Type()
)
apReassocTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apReassocTimes.setStatus("current")
_ApPreAssCannotShiftDeassocFailSum_Type = Counter32
_ApPreAssCannotShiftDeassocFailSum_Object = MibScalar
apPreAssCannotShiftDeassocFailSum = _ApPreAssCannotShiftDeassocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 2, 6),
    _ApPreAssCannotShiftDeassocFailSum_Type()
)
apPreAssCannotShiftDeassocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPreAssCannotShiftDeassocFailSum.setStatus("current")
_ApApStatsDisassociated_Type = Counter32
_ApApStatsDisassociated_Object = MibScalar
apApStatsDisassociated = _ApApStatsDisassociated_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 2, 7),
    _ApApStatsDisassociated_Type()
)
apApStatsDisassociated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apApStatsDisassociated.setStatus("current")
_ApAssocRejectSum_Type = Counter32
_ApAssocRejectSum_Object = MibScalar
apAssocRejectSum = _ApAssocRejectSum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 2, 8),
    _ApAssocRejectSum_Type()
)
apAssocRejectSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAssocRejectSum.setStatus("current")
_ApBSSNotSupportAssocFailSum_Type = Counter32
_ApBSSNotSupportAssocFailSum_Object = MibScalar
apBSSNotSupportAssocFailSum = _ApBSSNotSupportAssocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 2, 9),
    _ApBSSNotSupportAssocFailSum_Type()
)
apBSSNotSupportAssocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBSSNotSupportAssocFailSum.setStatus("current")
_ApIfPeformanceStat_ObjectIdentity = ObjectIdentity
apIfPeformanceStat = _ApIfPeformanceStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3)
)
_ApWiredIfPfmStatTable_Object = MibTable
apWiredIfPfmStatTable = _ApWiredIfPfmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 1)
)
if mibBuilder.loadTexts:
    apWiredIfPfmStatTable.setStatus("current")
_ApWiredIfPfmStatEntry_Object = MibTableRow
apWiredIfPfmStatEntry = _ApWiredIfPfmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 1, 1)
)
apWiredIfPfmStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apWiredIfPfmStatEntry.setStatus("current")
_ApIfInUcastPkts_Type = Counter32
_ApIfInUcastPkts_Object = MibTableColumn
apIfInUcastPkts = _ApIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 1, 1, 1),
    _ApIfInUcastPkts_Type()
)
apIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfInUcastPkts.setStatus("current")
_ApIfInNUcastPkts_Type = Counter32
_ApIfInNUcastPkts_Object = MibTableColumn
apIfInNUcastPkts = _ApIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 1, 1, 2),
    _ApIfInNUcastPkts_Type()
)
apIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfInNUcastPkts.setStatus("current")
_ApIfInOctets_Type = Counter32
_ApIfInOctets_Object = MibTableColumn
apIfInOctets = _ApIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 1, 1, 3),
    _ApIfInOctets_Type()
)
apIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfInOctets.setStatus("current")
_ApIfInDiscardPkts_Type = Counter32
_ApIfInDiscardPkts_Object = MibTableColumn
apIfInDiscardPkts = _ApIfInDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 1, 1, 4),
    _ApIfInDiscardPkts_Type()
)
apIfInDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfInDiscardPkts.setStatus("current")
_ApIfInErrors_Type = Counter32
_ApIfInErrors_Object = MibTableColumn
apIfInErrors = _ApIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 1, 1, 5),
    _ApIfInErrors_Type()
)
apIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfInErrors.setStatus("current")
_ApIfOutUcastPkts_Type = Counter32
_ApIfOutUcastPkts_Object = MibTableColumn
apIfOutUcastPkts = _ApIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 1, 1, 6),
    _ApIfOutUcastPkts_Type()
)
apIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfOutUcastPkts.setStatus("current")
_ApIfOutNUcastPkts_Type = Counter32
_ApIfOutNUcastPkts_Object = MibTableColumn
apIfOutNUcastPkts = _ApIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 1, 1, 7),
    _ApIfOutNUcastPkts_Type()
)
apIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfOutNUcastPkts.setStatus("current")
_ApIfOutOctets_Type = Counter32
_ApIfOutOctets_Object = MibTableColumn
apIfOutOctets = _ApIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 1, 1, 8),
    _ApIfOutOctets_Type()
)
apIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfOutOctets.setStatus("current")
_ApIfOutDiscardPkts_Type = Counter32
_ApIfOutDiscardPkts_Object = MibTableColumn
apIfOutDiscardPkts = _ApIfOutDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 1, 1, 9),
    _ApIfOutDiscardPkts_Type()
)
apIfOutDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfOutDiscardPkts.setStatus("current")
_ApIfOutErrors_Type = Counter32
_ApIfOutErrors_Object = MibTableColumn
apIfOutErrors = _ApIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 1, 1, 10),
    _ApIfOutErrors_Type()
)
apIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfOutErrors.setStatus("current")
_ApIfUpDwnTimes_Type = Counter32
_ApIfUpDwnTimes_Object = MibTableColumn
apIfUpDwnTimes = _ApIfUpDwnTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 1, 1, 11),
    _ApIfUpDwnTimes_Type()
)
apIfUpDwnTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfUpDwnTimes.setStatus("current")
_ApRadioIfPfmStatTable_Object = MibTable
apRadioIfPfmStatTable = _ApRadioIfPfmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2)
)
if mibBuilder.loadTexts:
    apRadioIfPfmStatTable.setStatus("current")
_ApRadioIfPfmStatEntry_Object = MibTableRow
apRadioIfPfmStatEntry = _ApRadioIfPfmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1)
)
apRadioIfPfmStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apRadioIfPfmStatEntry.setStatus("current")
_ApAvgRxSignalStrength_Type = Integer32
_ApAvgRxSignalStrength_Object = MibTableColumn
apAvgRxSignalStrength = _ApAvgRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 1),
    _ApAvgRxSignalStrength_Type()
)
apAvgRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAvgRxSignalStrength.setStatus("current")
_ApHighestRxSignalStrength_Type = Integer32
_ApHighestRxSignalStrength_Object = MibTableColumn
apHighestRxSignalStrength = _ApHighestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 2),
    _ApHighestRxSignalStrength_Type()
)
apHighestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apHighestRxSignalStrength.setStatus("current")
_ApLowestRxSignalStrength_Type = Integer32
_ApLowestRxSignalStrength_Object = MibTableColumn
apLowestRxSignalStrength = _ApLowestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 3),
    _ApLowestRxSignalStrength_Type()
)
apLowestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLowestRxSignalStrength.setStatus("current")
_ApUpdownTimes_Type = Counter32
_ApUpdownTimes_Object = MibTableColumn
apUpdownTimes = _ApUpdownTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 4),
    _ApUpdownTimes_Type()
)
apUpdownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUpdownTimes.setStatus("current")
_ApTxDataPkts_Type = Counter32
_ApTxDataPkts_Object = MibTableColumn
apTxDataPkts = _ApTxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 5),
    _ApTxDataPkts_Type()
)
apTxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTxDataPkts.setStatus("current")
_ApRxDataPkts_Type = Counter32
_ApRxDataPkts_Object = MibTableColumn
apRxDataPkts = _ApRxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 6),
    _ApRxDataPkts_Type()
)
apRxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRxDataPkts.setStatus("current")
_ApUplinkDataOctets_Type = Counter64
_ApUplinkDataOctets_Object = MibTableColumn
apUplinkDataOctets = _ApUplinkDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 7),
    _ApUplinkDataOctets_Type()
)
apUplinkDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUplinkDataOctets.setStatus("current")
_ApDwlinkDataOctets_Type = Counter64
_ApDwlinkDataOctets_Object = MibTableColumn
apDwlinkDataOctets = _ApDwlinkDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 8),
    _ApDwlinkDataOctets_Type()
)
apDwlinkDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDwlinkDataOctets.setStatus("current")
_ApChStatsDwlinkTotRetryPkts_Type = Counter32
_ApChStatsDwlinkTotRetryPkts_Object = MibTableColumn
apChStatsDwlinkTotRetryPkts = _ApChStatsDwlinkTotRetryPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 9),
    _ApChStatsDwlinkTotRetryPkts_Type()
)
apChStatsDwlinkTotRetryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChStatsDwlinkTotRetryPkts.setStatus("current")
_ApChStatsPhyErrPkts_Type = Counter32
_ApChStatsPhyErrPkts_Object = MibTableColumn
apChStatsPhyErrPkts = _ApChStatsPhyErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 10),
    _ApChStatsPhyErrPkts_Type()
)
apChStatsPhyErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChStatsPhyErrPkts.setStatus("current")
_ApChStatsMacFcsErrPkts_Type = Counter32
_ApChStatsMacFcsErrPkts_Object = MibTableColumn
apChStatsMacFcsErrPkts = _ApChStatsMacFcsErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 11),
    _ApChStatsMacFcsErrPkts_Type()
)
apChStatsMacFcsErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChStatsMacFcsErrPkts.setStatus("current")
_ApChStatsMacMicErrPkts_Type = Counter32
_ApChStatsMacMicErrPkts_Object = MibTableColumn
apChStatsMacMicErrPkts = _ApChStatsMacMicErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 12),
    _ApChStatsMacMicErrPkts_Type()
)
apChStatsMacMicErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChStatsMacMicErrPkts.setStatus("current")
_ApChStatsMacDecryptErrPkts_Type = Counter32
_ApChStatsMacDecryptErrPkts_Object = MibTableColumn
apChStatsMacDecryptErrPkts = _ApChStatsMacDecryptErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 13),
    _ApChStatsMacDecryptErrPkts_Type()
)
apChStatsMacDecryptErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChStatsMacDecryptErrPkts.setStatus("current")
_ApChStatsTotalErrPkts_Type = Counter32
_ApChStatsTotalErrPkts_Object = MibTableColumn
apChStatsTotalErrPkts = _ApChStatsTotalErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 14),
    _ApChStatsTotalErrPkts_Type()
)
apChStatsTotalErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChStatsTotalErrPkts.setStatus("current")
_ApRxMgmtFrameCnt_Type = Counter32
_ApRxMgmtFrameCnt_Object = MibTableColumn
apRxMgmtFrameCnt = _ApRxMgmtFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 15),
    _ApRxMgmtFrameCnt_Type()
)
apRxMgmtFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRxMgmtFrameCnt.setStatus("current")
_ApRxCtrlFrameCnt_Type = Counter32
_ApRxCtrlFrameCnt_Object = MibTableColumn
apRxCtrlFrameCnt = _ApRxCtrlFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 16),
    _ApRxCtrlFrameCnt_Type()
)
apRxCtrlFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRxCtrlFrameCnt.setStatus("current")
_ApRxDataFrameCnt_Type = Counter32
_ApRxDataFrameCnt_Object = MibTableColumn
apRxDataFrameCnt = _ApRxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 17),
    _ApRxDataFrameCnt_Type()
)
apRxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRxDataFrameCnt.setStatus("current")
_ApTxMgmtFrameCnt_Type = Counter32
_ApTxMgmtFrameCnt_Object = MibTableColumn
apTxMgmtFrameCnt = _ApTxMgmtFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 18),
    _ApTxMgmtFrameCnt_Type()
)
apTxMgmtFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTxMgmtFrameCnt.setStatus("current")
_ApTxCtrlFrameCnt_Type = Counter32
_ApTxCtrlFrameCnt_Object = MibTableColumn
apTxCtrlFrameCnt = _ApTxCtrlFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 19),
    _ApTxCtrlFrameCnt_Type()
)
apTxCtrlFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTxCtrlFrameCnt.setStatus("current")
_ApTxDataFrameCnt_Type = Counter32
_ApTxDataFrameCnt_Object = MibTableColumn
apTxDataFrameCnt = _ApTxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 20),
    _ApTxDataFrameCnt_Type()
)
apTxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTxDataFrameCnt.setStatus("current")
_ApChStatsFrameErrorCnt_Type = Counter32
_ApChStatsFrameErrorCnt_Object = MibTableColumn
apChStatsFrameErrorCnt = _ApChStatsFrameErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 21),
    _ApChStatsFrameErrorCnt_Type()
)
apChStatsFrameErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChStatsFrameErrorCnt.setStatus("current")
_ApRetryCnt_Type = Counter32
_ApRetryCnt_Object = MibTableColumn
apRetryCnt = _ApRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 22),
    _ApRetryCnt_Type()
)
apRetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRetryCnt.setStatus("current")
_ApCurTxPwr_Type = Integer32
_ApCurTxPwr_Object = MibTableColumn
apCurTxPwr = _ApCurTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 23),
    _ApCurTxPwr_Type()
)
apCurTxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCurTxPwr.setStatus("current")
_ApAPNeighborSSIDList_Type = DisplayString
_ApAPNeighborSSIDList_Object = MibTableColumn
apAPNeighborSSIDList = _ApAPNeighborSSIDList_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 24),
    _ApAPNeighborSSIDList_Type()
)
apAPNeighborSSIDList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAPNeighborSSIDList.setStatus("current")
_ApChanStaNum_Type = Counter32
_ApChanStaNum_Object = MibTableColumn
apChanStaNum = _ApChanStaNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 25),
    _ApChanStaNum_Type()
)
apChanStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChanStaNum.setStatus("current")
_ApChDownUnicastFrame_Type = Counter32
_ApChDownUnicastFrame_Object = MibTableColumn
apChDownUnicastFrame = _ApChDownUnicastFrame_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 26),
    _ApChDownUnicastFrame_Type()
)
apChDownUnicastFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChDownUnicastFrame.setStatus("current")
_ApChDownNonUnicastFrame_Type = Counter32
_ApChDownNonUnicastFrame_Object = MibTableColumn
apChDownNonUnicastFrame = _ApChDownNonUnicastFrame_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 27),
    _ApChDownNonUnicastFrame_Type()
)
apChDownNonUnicastFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChDownNonUnicastFrame.setStatus("current")
_ApChRxAuthFrame_Type = Counter32
_ApChRxAuthFrame_Object = MibTableColumn
apChRxAuthFrame = _ApChRxAuthFrame_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 28),
    _ApChRxAuthFrame_Type()
)
apChRxAuthFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChRxAuthFrame.setStatus("current")
_ApChRxAssoFrame_Type = Counter32
_ApChRxAssoFrame_Object = MibTableColumn
apChRxAssoFrame = _ApChRxAssoFrame_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 29),
    _ApChRxAssoFrame_Type()
)
apChRxAssoFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChRxAssoFrame.setStatus("current")
_ApChTxAuthFrame_Type = Counter32
_ApChTxAuthFrame_Object = MibTableColumn
apChTxAuthFrame = _ApChTxAuthFrame_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 30),
    _ApChTxAuthFrame_Type()
)
apChTxAuthFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChTxAuthFrame.setStatus("current")
_ApChTxAssoFrame_Type = Counter32
_ApChTxAssoFrame_Object = MibTableColumn
apChTxAssoFrame = _ApChTxAssoFrame_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 3, 2, 1, 31),
    _ApChTxAssoFrame_Type()
)
apChTxAssoFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChTxAssoFrame.setStatus("current")
_ApSSIDPeformanceStat_ObjectIdentity = ObjectIdentity
apSSIDPeformanceStat = _ApSSIDPeformanceStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 4)
)
_ApSSIDPfmStatTable_Object = MibTable
apSSIDPfmStatTable = _ApSSIDPfmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 4, 1)
)
if mibBuilder.loadTexts:
    apSSIDPfmStatTable.setStatus("current")
_ApSSIDPfmStatEntry_Object = MibTableRow
apSSIDPfmStatEntry = _ApSSIDPfmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 4, 1, 1)
)
apSSIDPfmStatEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FAT-AP-CF-MIB", "apWlanId"),
)
if mibBuilder.loadTexts:
    apSSIDPfmStatEntry.setStatus("current")
_ApSSIDTxDataPkts_Type = Counter32
_ApSSIDTxDataPkts_Object = MibTableColumn
apSSIDTxDataPkts = _ApSSIDTxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 4, 1, 1, 1),
    _ApSSIDTxDataPkts_Type()
)
apSSIDTxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDTxDataPkts.setStatus("current")
_ApSSIDRxDataPkts_Type = Counter32
_ApSSIDRxDataPkts_Object = MibTableColumn
apSSIDRxDataPkts = _ApSSIDRxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 4, 1, 1, 2),
    _ApSSIDRxDataPkts_Type()
)
apSSIDRxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDRxDataPkts.setStatus("current")
_ApSSIDUplinkDataOctets_Type = Counter64
_ApSSIDUplinkDataOctets_Object = MibTableColumn
apSSIDUplinkDataOctets = _ApSSIDUplinkDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 4, 1, 1, 3),
    _ApSSIDUplinkDataOctets_Type()
)
apSSIDUplinkDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDUplinkDataOctets.setStatus("current")
_ApSSIDDwlinkDataOctets_Type = Counter64
_ApSSIDDwlinkDataOctets_Object = MibTableColumn
apSSIDDwlinkDataOctets = _ApSSIDDwlinkDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 4, 1, 1, 4),
    _ApSSIDDwlinkDataOctets_Type()
)
apSSIDDwlinkDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDDwlinkDataOctets.setStatus("current")
_ApSSIDChStatsDwlinkTotRetryPkts_Type = Counter32
_ApSSIDChStatsDwlinkTotRetryPkts_Object = MibTableColumn
apSSIDChStatsDwlinkTotRetryPkts = _ApSSIDChStatsDwlinkTotRetryPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 4, 1, 1, 5),
    _ApSSIDChStatsDwlinkTotRetryPkts_Type()
)
apSSIDChStatsDwlinkTotRetryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDChStatsDwlinkTotRetryPkts.setStatus("current")
_ApSSIDApChStatsNumStations_Type = Integer32
_ApSSIDApChStatsNumStations_Object = MibTableColumn
apSSIDApChStatsNumStations = _ApSSIDApChStatsNumStations_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 4, 1, 1, 6),
    _ApSSIDApChStatsNumStations_Type()
)
apSSIDApChStatsNumStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDApChStatsNumStations.setStatus("current")
_ApTermPeformanceStat_ObjectIdentity = ObjectIdentity
apTermPeformanceStat = _ApTermPeformanceStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 5)
)
_ApTermPfmStatTable_Object = MibTable
apTermPfmStatTable = _ApTermPfmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 5, 1)
)
if mibBuilder.loadTexts:
    apTermPfmStatTable.setStatus("current")
_ApTermPfmStatEntry_Object = MibTableRow
apTermPfmStatEntry = _ApTermPfmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 5, 1, 1)
)
apTermPfmStatEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FAT-AP-CF-MIB", "apStaAddress"),
)
if mibBuilder.loadTexts:
    apTermPfmStatEntry.setStatus("current")
_ApStaAddress_Type = MacAddress
_ApStaAddress_Object = MibTableColumn
apStaAddress = _ApStaAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 5, 1, 1, 1),
    _ApStaAddress_Type()
)
apStaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaAddress.setStatus("current")
_ApStaUpTime_Type = TimeTicks
_ApStaUpTime_Object = MibTableColumn
apStaUpTime = _ApStaUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 5, 1, 1, 2),
    _ApStaUpTime_Type()
)
apStaUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUpTime.setStatus("current")
_ApAPReceivedStaSignalStrength_Type = Counter32
_ApAPReceivedStaSignalStrength_Object = MibTableColumn
apAPReceivedStaSignalStrength = _ApAPReceivedStaSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 5, 1, 1, 3),
    _ApAPReceivedStaSignalStrength_Type()
)
apAPReceivedStaSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAPReceivedStaSignalStrength.setStatus("current")
_ApAPReceiveStaSNR_Type = Counter32
_ApAPReceiveStaSNR_Object = MibTableColumn
apAPReceiveStaSNR = _ApAPReceiveStaSNR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 5, 1, 1, 4),
    _ApAPReceiveStaSNR_Type()
)
apAPReceiveStaSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAPReceiveStaSNR.setStatus("current")
_ApStaTxPkts_Type = Counter32
_ApStaTxPkts_Object = MibTableColumn
apStaTxPkts = _ApStaTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 5, 1, 1, 5),
    _ApStaTxPkts_Type()
)
apStaTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaTxPkts.setStatus("current")
_ApStaTxBytes_Type = Counter32
_ApStaTxBytes_Object = MibTableColumn
apStaTxBytes = _ApStaTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 5, 1, 1, 6),
    _ApStaTxBytes_Type()
)
apStaTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaTxBytes.setStatus("current")
_ApStaRxPkts_Type = Counter32
_ApStaRxPkts_Object = MibTableColumn
apStaRxPkts = _ApStaRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 5, 1, 1, 7),
    _ApStaRxPkts_Type()
)
apStaRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaRxPkts.setStatus("current")
_ApStaRxBytes_Type = Counter32
_ApStaRxBytes_Object = MibTableColumn
apStaRxBytes = _ApStaRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 5, 1, 1, 8),
    _ApStaRxBytes_Type()
)
apStaRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaRxBytes.setStatus("current")
_ApWAPIPeformanceStat_ObjectIdentity = ObjectIdentity
apWAPIPeformanceStat = _ApWAPIPeformanceStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 6)
)
_ApWAPIPfmStatTable_Object = MibTable
apWAPIPfmStatTable = _ApWAPIPfmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 6, 1)
)
if mibBuilder.loadTexts:
    apWAPIPfmStatTable.setStatus("current")
_ApWAPIPfmStatEntry_Object = MibTableRow
apWAPIPfmStatEntry = _ApWAPIPfmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 6, 1, 1)
)
apWAPIPfmStatEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FAT-AP-CF-MIB", "apSTAAddress"),
)
if mibBuilder.loadTexts:
    apWAPIPfmStatEntry.setStatus("current")
_ApSTAAddress_Type = MacAddress
_ApSTAAddress_Object = MibTableColumn
apSTAAddress = _ApSTAAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 6, 1, 1, 1),
    _ApSTAAddress_Type()
)
apSTAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSTAAddress.setStatus("current")
_ApVersion_Type = Unsigned32
_ApVersion_Object = MibTableColumn
apVersion = _ApVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 6, 1, 1, 2),
    _ApVersion_Type()
)
apVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVersion.setStatus("current")
_ApControlledPortStatus_Type = TruthValue
_ApControlledPortStatus_Object = MibTableColumn
apControlledPortStatus = _ApControlledPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 6, 1, 1, 3),
    _ApControlledPortStatus_Type()
)
apControlledPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apControlledPortStatus.setStatus("current")
_ApSelectedUnicastCipher_Type = OctetString
_ApSelectedUnicastCipher_Object = MibTableColumn
apSelectedUnicastCipher = _ApSelectedUnicastCipher_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 6, 1, 1, 4),
    _ApSelectedUnicastCipher_Type()
)
apSelectedUnicastCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSelectedUnicastCipher.setStatus("current")
_ApWPIReplayCounters_Type = Counter32
_ApWPIReplayCounters_Object = MibTableColumn
apWPIReplayCounters = _ApWPIReplayCounters_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 6, 1, 1, 5),
    _ApWPIReplayCounters_Type()
)
apWPIReplayCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWPIReplayCounters.setStatus("current")
_ApWPIDecryptableErrors_Type = Counter32
_ApWPIDecryptableErrors_Object = MibTableColumn
apWPIDecryptableErrors = _ApWPIDecryptableErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 6, 1, 1, 6),
    _ApWPIDecryptableErrors_Type()
)
apWPIDecryptableErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWPIDecryptableErrors.setStatus("current")
_ApWPIMICErrors_Type = Counter32
_ApWPIMICErrors_Object = MibTableColumn
apWPIMICErrors = _ApWPIMICErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 6, 1, 1, 7),
    _ApWPIMICErrors_Type()
)
apWPIMICErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWPIMICErrors.setStatus("current")
_ApWAISignatureErrors_Type = Counter32
_ApWAISignatureErrors_Object = MibTableColumn
apWAISignatureErrors = _ApWAISignatureErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 6, 1, 1, 8),
    _ApWAISignatureErrors_Type()
)
apWAISignatureErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAISignatureErrors.setStatus("current")
_ApWAIHMACErrors_Type = Counter32
_ApWAIHMACErrors_Object = MibTableColumn
apWAIHMACErrors = _ApWAIHMACErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 6, 1, 1, 9),
    _ApWAIHMACErrors_Type()
)
apWAIHMACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAIHMACErrors.setStatus("current")
_ApWAIAuthResultFailures_Type = Counter32
_ApWAIAuthResultFailures_Object = MibTableColumn
apWAIAuthResultFailures = _ApWAIAuthResultFailures_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 6, 1, 1, 10),
    _ApWAIAuthResultFailures_Type()
)
apWAIAuthResultFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAIAuthResultFailures.setStatus("current")
_ApWAIDiscardCounters_Type = Counter32
_ApWAIDiscardCounters_Object = MibTableColumn
apWAIDiscardCounters = _ApWAIDiscardCounters_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 6, 1, 1, 11),
    _ApWAIDiscardCounters_Type()
)
apWAIDiscardCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAIDiscardCounters.setStatus("current")
_ApWAITimeoutCounters_Type = Counter32
_ApWAITimeoutCounters_Object = MibTableColumn
apWAITimeoutCounters = _ApWAITimeoutCounters_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 6, 1, 1, 12),
    _ApWAITimeoutCounters_Type()
)
apWAITimeoutCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAITimeoutCounters.setStatus("current")
_ApWAIFormatErrors_Type = Counter32
_ApWAIFormatErrors_Object = MibTableColumn
apWAIFormatErrors = _ApWAIFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 6, 1, 1, 13),
    _ApWAIFormatErrors_Type()
)
apWAIFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAIFormatErrors.setStatus("current")
_ApWAICertificateHandshakeFailures_Type = Counter32
_ApWAICertificateHandshakeFailures_Object = MibTableColumn
apWAICertificateHandshakeFailures = _ApWAICertificateHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 6, 1, 1, 14),
    _ApWAICertificateHandshakeFailures_Type()
)
apWAICertificateHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAICertificateHandshakeFailures.setStatus("current")
_ApWAIUnicastHandshakeFailures_Type = Counter32
_ApWAIUnicastHandshakeFailures_Object = MibTableColumn
apWAIUnicastHandshakeFailures = _ApWAIUnicastHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 6, 1, 1, 15),
    _ApWAIUnicastHandshakeFailures_Type()
)
apWAIUnicastHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAIUnicastHandshakeFailures.setStatus("current")
_ApWAIMulticastHandshakeFailures_Type = Counter32
_ApWAIMulticastHandshakeFailures_Object = MibTableColumn
apWAIMulticastHandshakeFailures = _ApWAIMulticastHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 6, 1, 1, 16),
    _ApWAIMulticastHandshakeFailures_Type()
)
apWAIMulticastHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAIMulticastHandshakeFailures.setStatus("current")
_ApQOSPeformanceStat_ObjectIdentity = ObjectIdentity
apQOSPeformanceStat = _ApQOSPeformanceStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7)
)
_ApQosBasePfmStatTable_Object = MibTable
apQosBasePfmStatTable = _ApQosBasePfmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 1)
)
if mibBuilder.loadTexts:
    apQosBasePfmStatTable.setStatus("current")
_ApQosBasePfmStatEntry_Object = MibTableRow
apQosBasePfmStatEntry = _ApQosBasePfmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 1, 1)
)
apQosBasePfmStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apQosBasePfmStatEntry.setStatus("current")
_ApQoSSvcQueAvgLen_Type = Integer32
_ApQoSSvcQueAvgLen_Object = MibTableColumn
apQoSSvcQueAvgLen = _ApQoSSvcQueAvgLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 1, 1, 1),
    _ApQoSSvcQueAvgLen_Type()
)
apQoSSvcQueAvgLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQoSSvcQueAvgLen.setStatus("current")
_ApQoSSvcPktLossRatio_Type = Integer32
_ApQoSSvcPktLossRatio_Object = MibTableColumn
apQoSSvcPktLossRatio = _ApQoSSvcPktLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 1, 1, 2),
    _ApQoSSvcPktLossRatio_Type()
)
apQoSSvcPktLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQoSSvcPktLossRatio.setStatus("current")
_ApAvgTransSpeed_Type = Integer32
_ApAvgTransSpeed_Object = MibTableColumn
apAvgTransSpeed = _ApAvgTransSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 1, 1, 3),
    _ApAvgTransSpeed_Type()
)
apAvgTransSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAvgTransSpeed.setStatus("current")
_ApBackgroundQosPfmStatTable_Object = MibTable
apBackgroundQosPfmStatTable = _ApBackgroundQosPfmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 2)
)
if mibBuilder.loadTexts:
    apBackgroundQosPfmStatTable.setStatus("current")
_ApBackgroundQosPfmStatEntry_Object = MibTableRow
apBackgroundQosPfmStatEntry = _ApBackgroundQosPfmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 2, 1)
)
apBackgroundQosPfmStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apBackgroundQosPfmStatEntry.setStatus("current")
_ApBgQueAvgLen_Type = Integer32
_ApBgQueAvgLen_Object = MibTableColumn
apBgQueAvgLen = _ApBgQueAvgLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 2, 1, 1),
    _ApBgQueAvgLen_Type()
)
apBgQueAvgLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBgQueAvgLen.setStatus("current")
_ApBgAvgBurst_Type = Integer32
_ApBgAvgBurst_Object = MibTableColumn
apBgAvgBurst = _ApBgAvgBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 2, 1, 2),
    _ApBgAvgBurst_Type()
)
apBgAvgBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBgAvgBurst.setStatus("current")
_ApBgPktLossRatio_Type = Integer32
_ApBgPktLossRatio_Object = MibTableColumn
apBgPktLossRatio = _ApBgPktLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 2, 1, 3),
    _ApBgPktLossRatio_Type()
)
apBgPktLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBgPktLossRatio.setStatus("current")
_ApBgAvgTransSpeed_Type = Integer32
_ApBgAvgTransSpeed_Object = MibTableColumn
apBgAvgTransSpeed = _ApBgAvgTransSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 2, 1, 4),
    _ApBgAvgTransSpeed_Type()
)
apBgAvgTransSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBgAvgTransSpeed.setStatus("current")
_ApBgSvcLoss_Type = Integer32
_ApBgSvcLoss_Object = MibTableColumn
apBgSvcLoss = _ApBgSvcLoss_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 2, 1, 5),
    _ApBgSvcLoss_Type()
)
apBgSvcLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBgSvcLoss.setStatus("current")
_ApBestEffortQosPfmStatTable_Object = MibTable
apBestEffortQosPfmStatTable = _ApBestEffortQosPfmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 3)
)
if mibBuilder.loadTexts:
    apBestEffortQosPfmStatTable.setStatus("current")
_ApBestEffortQosPfmStatEntry_Object = MibTableRow
apBestEffortQosPfmStatEntry = _ApBestEffortQosPfmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 3, 1)
)
apBestEffortQosPfmStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apBestEffortQosPfmStatEntry.setStatus("current")
_ApBeQueAvgLen_Type = Integer32
_ApBeQueAvgLen_Object = MibTableColumn
apBeQueAvgLen = _ApBeQueAvgLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 3, 1, 1),
    _ApBeQueAvgLen_Type()
)
apBeQueAvgLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBeQueAvgLen.setStatus("current")
_ApBeAvgBurst_Type = Integer32
_ApBeAvgBurst_Object = MibTableColumn
apBeAvgBurst = _ApBeAvgBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 3, 1, 2),
    _ApBeAvgBurst_Type()
)
apBeAvgBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBeAvgBurst.setStatus("current")
_ApBePktLossRatio_Type = Integer32
_ApBePktLossRatio_Object = MibTableColumn
apBePktLossRatio = _ApBePktLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 3, 1, 3),
    _ApBePktLossRatio_Type()
)
apBePktLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBePktLossRatio.setStatus("current")
_ApBeAvgTransSpeed_Type = Integer32
_ApBeAvgTransSpeed_Object = MibTableColumn
apBeAvgTransSpeed = _ApBeAvgTransSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 3, 1, 4),
    _ApBeAvgTransSpeed_Type()
)
apBeAvgTransSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBeAvgTransSpeed.setStatus("current")
_ApBeSvcLoss_Type = Integer32
_ApBeSvcLoss_Object = MibTableColumn
apBeSvcLoss = _ApBeSvcLoss_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 3, 1, 5),
    _ApBeSvcLoss_Type()
)
apBeSvcLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBeSvcLoss.setStatus("current")
_ApVoiceQosPfmStatTable_Object = MibTable
apVoiceQosPfmStatTable = _ApVoiceQosPfmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 4)
)
if mibBuilder.loadTexts:
    apVoiceQosPfmStatTable.setStatus("current")
_ApVoiceQosPfmStatEntry_Object = MibTableRow
apVoiceQosPfmStatEntry = _ApVoiceQosPfmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 4, 1)
)
apVoiceQosPfmStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apVoiceQosPfmStatEntry.setStatus("current")
_ApVoiceQueAvgLen_Type = Integer32
_ApVoiceQueAvgLen_Object = MibTableColumn
apVoiceQueAvgLen = _ApVoiceQueAvgLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 4, 1, 1),
    _ApVoiceQueAvgLen_Type()
)
apVoiceQueAvgLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVoiceQueAvgLen.setStatus("current")
_ApVoiceAvgBurst_Type = Integer32
_ApVoiceAvgBurst_Object = MibTableColumn
apVoiceAvgBurst = _ApVoiceAvgBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 4, 1, 2),
    _ApVoiceAvgBurst_Type()
)
apVoiceAvgBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVoiceAvgBurst.setStatus("current")
_ApVoicePktLossRatio_Type = Integer32
_ApVoicePktLossRatio_Object = MibTableColumn
apVoicePktLossRatio = _ApVoicePktLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 4, 1, 3),
    _ApVoicePktLossRatio_Type()
)
apVoicePktLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVoicePktLossRatio.setStatus("current")
_ApVoiceAvgTransSpeed_Type = Integer32
_ApVoiceAvgTransSpeed_Object = MibTableColumn
apVoiceAvgTransSpeed = _ApVoiceAvgTransSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 4, 1, 4),
    _ApVoiceAvgTransSpeed_Type()
)
apVoiceAvgTransSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVoiceAvgTransSpeed.setStatus("current")
_ApVoicePutThroughRatio_Type = Integer32
_ApVoicePutThroughRatio_Object = MibTableColumn
apVoicePutThroughRatio = _ApVoicePutThroughRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 4, 1, 5),
    _ApVoicePutThroughRatio_Type()
)
apVoicePutThroughRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVoicePutThroughRatio.setStatus("current")
_ApVoiceDropRatio_Type = Integer32
_ApVoiceDropRatio_Object = MibTableColumn
apVoiceDropRatio = _ApVoiceDropRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 4, 1, 6),
    _ApVoiceDropRatio_Type()
)
apVoiceDropRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVoiceDropRatio.setStatus("current")
_ApVoiceSvcLoss_Type = Integer32
_ApVoiceSvcLoss_Object = MibTableColumn
apVoiceSvcLoss = _ApVoiceSvcLoss_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 4, 1, 7),
    _ApVoiceSvcLoss_Type()
)
apVoiceSvcLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVoiceSvcLoss.setStatus("current")
_ApVoiceExceedMaxUsersRequest_Type = Integer32
_ApVoiceExceedMaxUsersRequest_Object = MibTableColumn
apVoiceExceedMaxUsersRequest = _ApVoiceExceedMaxUsersRequest_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 4, 1, 8),
    _ApVoiceExceedMaxUsersRequest_Type()
)
apVoiceExceedMaxUsersRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVoiceExceedMaxUsersRequest.setStatus("current")
_ApVedioQosPfmStatTable_Object = MibTable
apVedioQosPfmStatTable = _ApVedioQosPfmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 5)
)
if mibBuilder.loadTexts:
    apVedioQosPfmStatTable.setStatus("current")
_ApVedioQosPfmStatEntry_Object = MibTableRow
apVedioQosPfmStatEntry = _ApVedioQosPfmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 5, 1)
)
apVedioQosPfmStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apVedioQosPfmStatEntry.setStatus("current")
_ApVedioQueAvgLen_Type = Integer32
_ApVedioQueAvgLen_Object = MibTableColumn
apVedioQueAvgLen = _ApVedioQueAvgLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 5, 1, 1),
    _ApVedioQueAvgLen_Type()
)
apVedioQueAvgLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVedioQueAvgLen.setStatus("current")
_ApVedioAvgBurst_Type = Integer32
_ApVedioAvgBurst_Object = MibTableColumn
apVedioAvgBurst = _ApVedioAvgBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 5, 1, 2),
    _ApVedioAvgBurst_Type()
)
apVedioAvgBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVedioAvgBurst.setStatus("current")
_ApVedioPktLossRatio_Type = Integer32
_ApVedioPktLossRatio_Object = MibTableColumn
apVedioPktLossRatio = _ApVedioPktLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 5, 1, 3),
    _ApVedioPktLossRatio_Type()
)
apVedioPktLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVedioPktLossRatio.setStatus("current")
_ApVedioAvgTransSpeed_Type = Integer32
_ApVedioAvgTransSpeed_Object = MibTableColumn
apVedioAvgTransSpeed = _ApVedioAvgTransSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 5, 1, 4),
    _ApVedioAvgTransSpeed_Type()
)
apVedioAvgTransSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVedioAvgTransSpeed.setStatus("current")
_ApVedioPutThroughRatio_Type = Integer32
_ApVedioPutThroughRatio_Object = MibTableColumn
apVedioPutThroughRatio = _ApVedioPutThroughRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 5, 1, 5),
    _ApVedioPutThroughRatio_Type()
)
apVedioPutThroughRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVedioPutThroughRatio.setStatus("current")
_ApVedioDropRatio_Type = Integer32
_ApVedioDropRatio_Object = MibTableColumn
apVedioDropRatio = _ApVedioDropRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 5, 1, 6),
    _ApVedioDropRatio_Type()
)
apVedioDropRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVedioDropRatio.setStatus("current")
_ApVedioSvcLoss_Type = Integer32
_ApVedioSvcLoss_Object = MibTableColumn
apVedioSvcLoss = _ApVedioSvcLoss_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 5, 1, 7),
    _ApVedioSvcLoss_Type()
)
apVedioSvcLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVedioSvcLoss.setStatus("current")
_ApVedioExceedMaxUsersRequest_Type = Integer32
_ApVedioExceedMaxUsersRequest_Object = MibTableColumn
apVedioExceedMaxUsersRequest = _ApVedioExceedMaxUsersRequest_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 9, 7, 5, 1, 8),
    _ApVedioExceedMaxUsersRequest_Type()
)
apVedioExceedMaxUsersRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVedioExceedMaxUsersRequest.setStatus("current")

# Managed Objects groups


# Notification objects

apConfigurationErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 0, 1)
)
if mibBuilder.loadTexts:
    apConfigurationErrorTrap.setStatus(
        "current"
    )

apCPUusageTooHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 0, 2)
)
if mibBuilder.loadTexts:
    apCPUusageTooHighTrap.setStatus(
        "current"
    )

apCPUusageTooHighRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 0, 3)
)
if mibBuilder.loadTexts:
    apCPUusageTooHighRecovTrap.setStatus(
        "current"
    )

apMemUsageTooHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 0, 4)
)
if mibBuilder.loadTexts:
    apMemUsageTooHighTrap.setStatus(
        "current"
    )

apMemUsageTooHighRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 0, 5)
)
if mibBuilder.loadTexts:
    apMemUsageTooHighRecovTrap.setStatus(
        "current"
    )

apSystmColdStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 0, 6)
)
if mibBuilder.loadTexts:
    apSystmColdStartTrap.setStatus(
        "current"
    )

apIPAddrChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 0, 7)
)
apIPAddrChangeTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apOriginalIpAddr"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apCurrentIpAddr"))
)
if mibBuilder.loadTexts:
    apIPAddrChangeTrap.setStatus(
        "current"
    )

apAPMtWorkModeChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 0, 8)
)
if mibBuilder.loadTexts:
    apAPMtWorkModeChgTrap.setStatus(
        "current"
    )

apAPSWUpdateFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 0, 9)
)
if mibBuilder.loadTexts:
    apAPSWUpdateFailTrap.setStatus(
        "current"
    )

apSSIDkeyConflictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 0, 10)
)
apSSIDkeyConflictTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apAPMac"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apSSIDKey"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apSSIDKeyConflict"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apCyperIndex"))
)
if mibBuilder.loadTexts:
    apSSIDkeyConflictTrap.setStatus(
        "current"
    )

apFatAPHeartbeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 0, 11)
)
apFatAPHeartbeatTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apIpAddr"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apTimeStamp"))
)
if mibBuilder.loadTexts:
    apFatAPHeartbeatTrap.setStatus(
        "current"
    )

apAPCoInterfDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 2, 1)
)
apAPCoInterfDetectedTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPChannel"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apInterfAPBSSID"))
)
if mibBuilder.loadTexts:
    apAPCoInterfDetectedTrap.setStatus(
        "current"
    )

apAPCoInterfClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 2, 2)
)
apAPCoInterfClearTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPChannel"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apInterfAPBSSID"))
)
if mibBuilder.loadTexts:
    apAPCoInterfClearTrap.setStatus(
        "current"
    )

apAPNerborInterfDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 2, 3)
)
apAPNerborInterfDetectedTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPChannel"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apInterfAPBSSID"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apInterfAPChannel"))
)
if mibBuilder.loadTexts:
    apAPNerborInterfDetectedTrap.setStatus(
        "current"
    )

apAPNeiborInterfClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 2, 4)
)
apAPNeiborInterfClearTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPChannel"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apInterfAPBSSID"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apInterfAPChannel"))
)
if mibBuilder.loadTexts:
    apAPNeiborInterfClearTrap.setStatus(
        "current"
    )

apStaInterfDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 2, 5)
)
apStaInterfDetectedTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPChannel"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apInterfStaMac"))
)
if mibBuilder.loadTexts:
    apStaInterfDetectedTrap.setStatus(
        "current"
    )

apStaInterfClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 2, 6)
)
apStaInterfClearTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPChannel"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apInterfStaMac"))
)
if mibBuilder.loadTexts:
    apStaInterfClearTrap.setStatus(
        "current"
    )

apOtherDeviceInterfDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 2, 7)
)
apOtherDeviceInterfDetectedTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPChannel"))
)
if mibBuilder.loadTexts:
    apOtherDeviceInterfDetectedTrap.setStatus(
        "current"
    )

apOtherDevInterfClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 2, 8)
)
apOtherDevInterfClearTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPChannel"))
)
if mibBuilder.loadTexts:
    apOtherDevInterfClearTrap.setStatus(
        "current"
    )

apRadioDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 2, 9)
)
apRadioDownTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apInterruptReason"))
)
if mibBuilder.loadTexts:
    apRadioDownTrap.setStatus(
        "current"
    )

apRadioDownRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 2, 10)
)
apRadioDownRecovTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apInterruptReason"))
)
if mibBuilder.loadTexts:
    apRadioDownRecovTrap.setStatus(
        "current"
    )

apAPStaFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 2, 11)
)
apAPStaFullTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apPermitAssoUser"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apAssoFailReason"))
)
if mibBuilder.loadTexts:
    apAPStaFullTrap.setStatus(
        "current"
    )

apAPStaFullRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 2, 12)
)
apAPStaFullRecoverTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apPermitAssoUser"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apAssoFailReason"))
)
if mibBuilder.loadTexts:
    apAPStaFullRecoverTrap.setStatus(
        "current"
    )

apAPMtRdoChanlChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 2, 13)
)
apAPMtRdoChanlChgTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apChannelBeforeChange"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apChannelAfterChange"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apChanChangeMode"))
)
if mibBuilder.loadTexts:
    apAPMtRdoChanlChgTrap.setStatus(
        "current"
    )

apStaAuthErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 4, 1)
)
apStaAuthErrorTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPBSSID"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPSSID"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apStaMacAddr"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apAuthMode"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apAuthFailReason"))
)
if mibBuilder.loadTexts:
    apStaAuthErrorTrap.setStatus(
        "current"
    )

apStAssociationFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 4, 2)
)
apStAssociationFailTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPBSSID"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPSSID"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apStaMacAddr"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apAssoFailReason"))
)
if mibBuilder.loadTexts:
    apStAssociationFailTrap.setStatus(
        "current"
    )

apRadiusAuthServerUnavailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 6, 1)
)
if mibBuilder.loadTexts:
    apRadiusAuthServerUnavailableTrap.setStatus(
        "current"
    )

apRadiusAuthServerAvailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 6, 2)
)
if mibBuilder.loadTexts:
    apRadiusAuthServerAvailableTrap.setStatus(
        "current"
    )

apRadioAccServerUnavailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 6, 3)
)
if mibBuilder.loadTexts:
    apRadioAccServerUnavailableTrap.setStatus(
        "current"
    )

apRadiusAccServerAvailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 6, 4)
)
if mibBuilder.loadTexts:
    apRadiusAccServerAvailableTrap.setStatus(
        "current"
    )

apUserWithInvalidCerficationInbreakNetworkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 7, 1)
)
apUserWithInvalidCerficationInbreakNetworkTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPBSSID"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPSSID"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apStaMacAddr"))
)
if mibBuilder.loadTexts:
    apUserWithInvalidCerficationInbreakNetworkTrap.setStatus(
        "current"
    )

apStationRepititiveAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 7, 2)
)
apStationRepititiveAttackTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPBSSID"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPSSID"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apStaMacAddr"))
)
if mibBuilder.loadTexts:
    apStationRepititiveAttackTrap.setStatus(
        "current"
    )

apTamperAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 7, 3)
)
apTamperAttackTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPBSSID"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPSSID"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apStaMacAddr"))
)
if mibBuilder.loadTexts:
    apTamperAttackTrap.setStatus(
        "current"
    )

apLowSafeLevelAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 7, 4)
)
apLowSafeLevelAttackTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPBSSID"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPSSID"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apStaMacAddr"))
)
if mibBuilder.loadTexts:
    apLowSafeLevelAttackTrap.setStatus(
        "current"
    )

apAddressRedirectionAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 80, 7, 5)
)
apAddressRedirectionAttackTrap.setObjects(
      *(("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPBSSID"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apWorkingAPSSID"),
        ("RUIJIE-WLAN-FAT-AP-CF-MIB", "apStaMacAddr"))
)
if mibBuilder.loadTexts:
    apAddressRedirectionAttackTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-WLAN-FAT-AP-CF-MIB",
    **{"apStandardmibmodule": apStandardmibmodule,
       "apStandardSysTraps": apStandardSysTraps,
       "apConfigurationErrorTrap": apConfigurationErrorTrap,
       "apCPUusageTooHighTrap": apCPUusageTooHighTrap,
       "apCPUusageTooHighRecovTrap": apCPUusageTooHighRecovTrap,
       "apMemUsageTooHighTrap": apMemUsageTooHighTrap,
       "apMemUsageTooHighRecovTrap": apMemUsageTooHighRecovTrap,
       "apSystmColdStartTrap": apSystmColdStartTrap,
       "apIPAddrChangeTrap": apIPAddrChangeTrap,
       "apAPMtWorkModeChgTrap": apAPMtWorkModeChgTrap,
       "apAPSWUpdateFailTrap": apAPSWUpdateFailTrap,
       "apSSIDkeyConflictTrap": apSSIDkeyConflictTrap,
       "apFatAPHeartbeatTrap": apFatAPHeartbeatTrap,
       "apStandardSysTrapsObjects": apStandardSysTrapsObjects,
       "apOriginalIpAddr": apOriginalIpAddr,
       "apCurrentIpAddr": apCurrentIpAddr,
       "apIpAddr": apIpAddr,
       "apTimeStamp": apTimeStamp,
       "apAPMac": apAPMac,
       "apSSIDKey": apSSIDKey,
       "apSSIDKeyConflict": apSSIDKeyConflict,
       "apCyperIndex": apCyperIndex,
       "apStandardRadioTraps": apStandardRadioTraps,
       "apAPCoInterfDetectedTrap": apAPCoInterfDetectedTrap,
       "apAPCoInterfClearTrap": apAPCoInterfClearTrap,
       "apAPNerborInterfDetectedTrap": apAPNerborInterfDetectedTrap,
       "apAPNeiborInterfClearTrap": apAPNeiborInterfClearTrap,
       "apStaInterfDetectedTrap": apStaInterfDetectedTrap,
       "apStaInterfClearTrap": apStaInterfClearTrap,
       "apOtherDeviceInterfDetectedTrap": apOtherDeviceInterfDetectedTrap,
       "apOtherDevInterfClearTrap": apOtherDevInterfClearTrap,
       "apRadioDownTrap": apRadioDownTrap,
       "apRadioDownRecovTrap": apRadioDownRecovTrap,
       "apAPStaFullTrap": apAPStaFullTrap,
       "apAPStaFullRecoverTrap": apAPStaFullRecoverTrap,
       "apAPMtRdoChanlChgTrap": apAPMtRdoChanlChgTrap,
       "apStandardRadioTrapsObjects": apStandardRadioTrapsObjects,
       "apInterruptReason": apInterruptReason,
       "apWorkingAPRadioIfInfo": apWorkingAPRadioIfInfo,
       "apWorkingAPChannel": apWorkingAPChannel,
       "apInterfAPChannel": apInterfAPChannel,
       "apInterfAPBSSID": apInterfAPBSSID,
       "apInterfStaMac": apInterfStaMac,
       "apPermitAssoUser": apPermitAssoUser,
       "apAssoFailReason": apAssoFailReason,
       "apChannelBeforeChange": apChannelBeforeChange,
       "apChannelAfterChange": apChannelAfterChange,
       "apChanChangeMode": apChanChangeMode,
       "apStandardTerminalTraps": apStandardTerminalTraps,
       "apStaAuthErrorTrap": apStaAuthErrorTrap,
       "apStAssociationFailTrap": apStAssociationFailTrap,
       "apStandardTerminalTrapsObjects": apStandardTerminalTrapsObjects,
       "apWorkingAPBSSID": apWorkingAPBSSID,
       "apWorkingAPSSID": apWorkingAPSSID,
       "apStaMacAddr": apStaMacAddr,
       "apAuthMode": apAuthMode,
       "apAuthFailReason": apAuthFailReason,
       "apStandardAuthSvrTraps": apStandardAuthSvrTraps,
       "apRadiusAuthServerUnavailableTrap": apRadiusAuthServerUnavailableTrap,
       "apRadiusAuthServerAvailableTrap": apRadiusAuthServerAvailableTrap,
       "apRadioAccServerUnavailableTrap": apRadioAccServerUnavailableTrap,
       "apRadiusAccServerAvailableTrap": apRadiusAccServerAvailableTrap,
       "apStandardWapiScrTraps": apStandardWapiScrTraps,
       "apUserWithInvalidCerficationInbreakNetworkTrap": apUserWithInvalidCerficationInbreakNetworkTrap,
       "apStationRepititiveAttackTrap": apStationRepititiveAttackTrap,
       "apTamperAttackTrap": apTamperAttackTrap,
       "apLowSafeLevelAttackTrap": apLowSafeLevelAttackTrap,
       "apAddressRedirectionAttackTrap": apAddressRedirectionAttackTrap,
       "apConfigInfoObjects": apConfigInfoObjects,
       "apSysInfoObjects": apSysInfoObjects,
       "apSysNetID": apSysNetID,
       "apSysHostName": apSysHostName,
       "apSysDescr": apSysDescr,
       "apManufacturer": apManufacturer,
       "apSerialNumber": apSerialNumber,
       "apSysModel": apSysModel,
       "apSysTime": apSysTime,
       "apSysUpTime": apSysUpTime,
       "apSysIPAddress": apSysIPAddress,
       "apSysIPNetMask": apSysIPNetMask,
       "apSysGWAddr": apSysGWAddr,
       "apPrimDNSServerIPAdd": apPrimDNSServerIPAdd,
       "apSeconDNSServerIPAdd": apSeconDNSServerIPAdd,
       "apSysMacAddress": apSysMacAddress,
       "apReadCommunityName": apReadCommunityName,
       "apWriteCommunityName": apWriteCommunityName,
       "apStatWindowTime": apStatWindowTime,
       "apSampleTime": apSampleTime,
       "apSysRestart": apSysRestart,
       "apSysReset": apSysReset,
       "apSoftwareName": apSoftwareName,
       "apSoftwareVersion": apSoftwareVersion,
       "apSoftwareVendor": apSoftwareVendor,
       "apCPUType": apCPUType,
       "apMemoryType": apMemoryType,
       "apMemorySize": apMemorySize,
       "apFlashSize": apFlashSize,
       "apPhyInterfaceConfig": apPhyInterfaceConfig,
       "apIfNumber": apIfNumber,
       "apWiredInterfaceCfgTable": apWiredInterfaceCfgTable,
       "apWiredInterfaceCfgEntry": apWiredInterfaceCfgEntry,
       "apIfDescr": apIfDescr,
       "apIfType": apIfType,
       "apIfMTU": apIfMTU,
       "apIfSpeed": apIfSpeed,
       "apIfPhysAddress": apIfPhysAddress,
       "apIfAdminStatus": apIfAdminStatus,
       "apIfOperStatus": apIfOperStatus,
       "apIfLastChange": apIfLastChange,
       "apRadioInterfaceCfg": apRadioInterfaceCfg,
       "apRadioInterfaceInfoTable": apRadioInterfaceInfoTable,
       "apRadioInterfaceInfoEntry": apRadioInterfaceInfoEntry,
       "apRadioIfDescr": apRadioIfDescr,
       "apRadioIfType": apRadioIfType,
       "apRadioIfMTU": apRadioIfMTU,
       "apRadioIfSpeed": apRadioIfSpeed,
       "apRadioIfMacAddress": apRadioIfMacAddress,
       "apRadioIfDiversity": apRadioIfDiversity,
       "apRadioIfAdminStatus": apRadioIfAdminStatus,
       "apRadioIfOperStatus": apRadioIfOperStatus,
       "apRadioIfLastChange": apRadioIfLastChange,
       "apRadioChannelAutoSelectEnable": apRadioChannelAutoSelectEnable,
       "apRadioChannelConfig": apRadioChannelConfig,
       "apRadioChannelUsing": apRadioChannelUsing,
       "apCurrRadioModeSupport": apCurrRadioModeSupport,
       "apRadioModeConfig": apRadioModeConfig,
       "apTransmitSpeedConfig": apTransmitSpeedConfig,
       "apMaxTxPwrLvl": apMaxTxPwrLvl,
       "apTxPwr": apTxPwr,
       "apPwrAttRange": apPwrAttRange,
       "apPwrAttValue": apPwrAttValue,
       "apAntennaGain": apAntennaGain,
       "apPowerMgmtEnable": apPowerMgmtEnable,
       "apMaxStationNumPermitted": apMaxStationNumPermitted,
       "apAMPDUEnabled": apAMPDUEnabled,
       "apBWMode": apBWMode,
       "apShortGIEnabled": apShortGIEnabled,
       "apIs11nOnly": apIs11nOnly,
       "apRadioInterfacePhyParaTable": apRadioInterfacePhyParaTable,
       "apRadioInterfacePhyParaEntry": apRadioInterfacePhyParaEntry,
       "apBeaconIntvl": apBeaconIntvl,
       "apDtimIntvl": apDtimIntvl,
       "apRtsThreshold": apRtsThreshold,
       "apFragThreshlod": apFragThreshlod,
       "apPreambleLen": apPreambleLen,
       "apSSIDCfg": apSSIDCfg,
       "apConfigBSSIDNum": apConfigBSSIDNum,
       "apRadioIfSSIDCfgTable": apRadioIfSSIDCfgTable,
       "apRadioIfSSIDCfgEntry": apRadioIfSSIDCfgEntry,
       "apBSSID": apBSSID,
       "apSSIDCfgTable": apSSIDCfgTable,
       "apSSIDCfgEntry": apSSIDCfgEntry,
       "apWlanId": apWlanId,
       "apSSIDName": apSSIDName,
       "apSSIDEnabled": apSSIDEnabled,
       "apSSIDHidden": apSSIDHidden,
       "apStaIsolate": apStaIsolate,
       "apDot11Auth": apDot11Auth,
       "apSecurity": apSecurity,
       "apAuthenMode": apAuthenMode,
       "apSecurityCiphers": apSecurityCiphers,
       "apVlanId": apVlanId,
       "apMaxSimultUsers": apMaxSimultUsers,
       "apStaUplinkMaxRate": apStaUplinkMaxRate,
       "apStaDwlinkMaxRate": apStaDwlinkMaxRate,
       "apSSIDCfgStatus": apSSIDCfgStatus,
       "apSecurityCfg": apSecurityCfg,
       "apSecurityCfgTable": apSecurityCfgTable,
       "apSecurityCfgEntry": apSecurityCfgEntry,
       "apWEPCipherKeyIndex": apWEPCipherKeyIndex,
       "apWEPCipherKeyValue": apWEPCipherKeyValue,
       "apWEPCipherKeyCharType": apWEPCipherKeyCharType,
       "apPSKCipherKeyValue": apPSKCipherKeyValue,
       "apPSKCipherKeyCharType": apPSKCipherKeyCharType,
       "apWAPIASIPAddress": apWAPIASIPAddress,
       "apWAPIIsInstalledCer": apWAPIIsInstalledCer,
       "apTerminalCfg": apTerminalCfg,
       "apTerminalInfoTable": apTerminalInfoTable,
       "apTerminalInfoEntry": apTerminalInfoEntry,
       "apStaMAC": apStaMAC,
       "apStaWMMAttr": apStaWMMAttr,
       "apStaIPAddress": apStaIPAddress,
       "apStaRadioMode": apStaRadioMode,
       "apStaRadioChannel": apStaRadioChannel,
       "apStaTxRates": apStaTxRates,
       "apStaPowerSaveMode": apStaPowerSaveMode,
       "apStaVlanId": apStaVlanId,
       "apStaSSIDName": apStaSSIDName,
       "apStaDot11Auth": apStaDot11Auth,
       "apStaSecurity": apStaSecurity,
       "apStaAuthenMode": apStaAuthenMode,
       "apStaSecurityCiphers": apStaSecurityCiphers,
       "apQosCfg": apQosCfg,
       "apQosRadioIfCfgTable": apQosRadioIfCfgTable,
       "apQosRadioIfCfgEntry": apQosRadioIfCfgEntry,
       "apQoSTrafficClassIndex": apQoSTrafficClassIndex,
       "apQosAIFS": apQosAIFS,
       "apQoSCWmin": apQoSCWmin,
       "apQoSCWmax": apQoSCWmax,
       "apQoSTXOPLim": apQoSTXOPLim,
       "apQosBaseCfgTable": apQosBaseCfgTable,
       "apQosBaseCfgEntry": apQosBaseCfgEntry,
       "apQoSBaseTrafficClass": apQoSBaseTrafficClass,
       "apQoSEnabled": apQoSEnabled,
       "apQoSBW": apQoSBW,
       "apQoSResPercent": apQoSResPercent,
       "apQoSsharedBW": apQoSsharedBW,
       "apQoSsharedBWPercent": apQoSsharedBWPercent,
       "apSchedAlgName": apSchedAlgName,
       "apResPolicyEnabled": apResPolicyEnabled,
       "apResPolicyName": apResPolicyName,
       "apBackgroundSvcAvgSpeed": apBackgroundSvcAvgSpeed,
       "apBackgroundSvcMaxBurst": apBackgroundSvcMaxBurst,
       "apBackgroundSvcPriority": apBackgroundSvcPriority,
       "apBackgroundSvcResPriority": apBackgroundSvcResPriority,
       "apBestEffortSvcAvgSpeed": apBestEffortSvcAvgSpeed,
       "apBestEffortSvcMaxBurst": apBestEffortSvcMaxBurst,
       "apBestEffortSvcPriority": apBestEffortSvcPriority,
       "apBestEffortSvcResPriority": apBestEffortSvcResPriority,
       "apVoiceSvcAvgSpeed": apVoiceSvcAvgSpeed,
       "apVoiceSvcMaxBurst": apVoiceSvcMaxBurst,
       "apVoiceSvcPriority": apVoiceSvcPriority,
       "apVoiceSvcResPriority": apVoiceSvcResPriority,
       "apVideoSvcAvgSpeed": apVideoSvcAvgSpeed,
       "apVideoSvcMaxBurst": apVideoSvcMaxBurst,
       "apVideoSvcPriority": apVideoSvcPriority,
       "apVideoSvcResPriority": apVideoSvcResPriority,
       "apQosBackgroundCfgTable": apQosBackgroundCfgTable,
       "apQosBackgroundCfgEntry": apQosBackgroundCfgEntry,
       "apBgMaxSvcCnt": apBgMaxSvcCnt,
       "apBgSvcBW": apBgSvcBW,
       "apBgSvcBWPercent": apBgSvcBWPercent,
       "apBgIsUseWREDAlg": apBgIsUseWREDAlg,
       "apBgIsUseTrafficShaping": apBgIsUseTrafficShaping,
       "apQosBestEffortCfgTable": apQosBestEffortCfgTable,
       "apQosBestEffortCfgEntry": apQosBestEffortCfgEntry,
       "apBeMaxSvcCnt": apBeMaxSvcCnt,
       "apBeSvcBW": apBeSvcBW,
       "apBeSvcBWPercent": apBeSvcBWPercent,
       "apBeIsUseWREDAlg": apBeIsUseWREDAlg,
       "apBeIsUseTrafficShaping": apBeIsUseTrafficShaping,
       "apQosVoiceCfgTable": apQosVoiceCfgTable,
       "apQosVoiceCfgEntry": apQosVoiceCfgEntry,
       "apVoiceMaxSvcCnt": apVoiceMaxSvcCnt,
       "apVoiceSvcBW": apVoiceSvcBW,
       "apVoiceSvcBWPercent": apVoiceSvcBWPercent,
       "apVoiceIsUseStreamBasedQueue": apVoiceIsUseStreamBasedQueue,
       "apVoiceStreamMaxQueueLen": apVoiceStreamMaxQueueLen,
       "apVoiceStreamAvgSpeed": apVoiceStreamAvgSpeed,
       "apVoiceStreamMaxBurst": apVoiceStreamMaxBurst,
       "apVoiceIsUseWREDAlg": apVoiceIsUseWREDAlg,
       "apVoiceIsUseTrafficShaping": apVoiceIsUseTrafficShaping,
       "apQosVedioCfgTable": apQosVedioCfgTable,
       "apQosVedioCfgEntry": apQosVedioCfgEntry,
       "apVedioMaxSvcCnt": apVedioMaxSvcCnt,
       "apVedioSvcBW": apVedioSvcBW,
       "apVedioSvcBWPercent": apVedioSvcBWPercent,
       "apVedioIsUseStreamBasedQueue": apVedioIsUseStreamBasedQueue,
       "apVedioStreamMaxQueueLen": apVedioStreamMaxQueueLen,
       "apVedioStreamAvgSpeed": apVedioStreamAvgSpeed,
       "apVedioStreamMaxBurst": apVedioStreamMaxBurst,
       "apVedioIsUseWREDAlg": apVedioIsUseWREDAlg,
       "apVedioIsUseTrafficShaping": apVedioIsUseTrafficShaping,
       "apWapiCfg": apWapiCfg,
       "apWapiProtocolCfgTable": apWapiProtocolCfgTable,
       "apWapiProtocolCfgEntry": apWapiProtocolCfgEntry,
       "apConfigVersion": apConfigVersion,
       "apControlledAuthControl": apControlledAuthControl,
       "apControlledPortControl": apControlledPortControl,
       "apWapiOptionImplemented": apWapiOptionImplemented,
       "apWapiPreauthImplemented": apWapiPreauthImplemented,
       "apWapiEnabled": apWapiEnabled,
       "apWapiPreauthEnabled": apWapiPreauthEnabled,
       "apUnicastKeysSupported": apUnicastKeysSupported,
       "apUnicastRekeyMethod": apUnicastRekeyMethod,
       "apUnicastRekeyTime": apUnicastRekeyTime,
       "apUnicastRekeyPackets": apUnicastRekeyPackets,
       "apMulticastCipher": apMulticastCipher,
       "apMulticastRekeyMethod": apMulticastRekeyMethod,
       "apMulticastRekeyTime": apMulticastRekeyTime,
       "apMulticastRekeyPackets": apMulticastRekeyPackets,
       "apMulticastRekeyStrict": apMulticastRekeyStrict,
       "apPSKValue": apPSKValue,
       "apPSKPassPhrase": apPSKPassPhrase,
       "apCertificateUpdateCount": apCertificateUpdateCount,
       "apMulticastUpdateCount": apMulticastUpdateCount,
       "apUnicastUpdateCount": apUnicastUpdateCount,
       "apMulticastCipherSize": apMulticastCipherSize,
       "apBKLifetime": apBKLifetime,
       "apBKReauthThreshold": apBKReauthThreshold,
       "apSATimeout": apSATimeout,
       "apAuthSuiteSelected": apAuthSuiteSelected,
       "apUnicastCipherSelected": apUnicastCipherSelected,
       "apMulticastCipherSelected": apMulticastCipherSelected,
       "apBKIDUsed": apBKIDUsed,
       "apAuthSuiteRequested": apAuthSuiteRequested,
       "apUnicastCipherRequested": apUnicastCipherRequested,
       "apMulticastCipherRequested": apMulticastCipherRequested,
       "apWapiUnicastCfgTable": apWapiUnicastCfgTable,
       "apWapiUnicastCfgEntry": apWapiUnicastCfgEntry,
       "apUnicastCipher": apUnicastCipher,
       "apUnicastCipherEnabled": apUnicastCipherEnabled,
       "apUnicastCipherSize": apUnicastCipherSize,
       "apWapiAKMCfgTable": apWapiAKMCfgTable,
       "apWapiAKMCfgEntry": apWapiAKMCfgEntry,
       "apAuthenticationSuite": apAuthenticationSuite,
       "apAuthenticationSuiteEnabled": apAuthenticationSuiteEnabled,
       "apSyslogCfg": apSyslogCfg,
       "apSyslogSvcEnable": apSyslogSvcEnable,
       "apSyslogReportEventLevel": apSyslogReportEventLevel,
       "apSyslogSvrCfgTable": apSyslogSvrCfgTable,
       "apSyslogSvrCfgEntry": apSyslogSvrCfgEntry,
       "apSyslogSvrIndex": apSyslogSvrIndex,
       "apSyslogServerAddr": apSyslogServerAddr,
       "apSyslogStatus": apSyslogStatus,
       "apSoftwareUpdate": apSoftwareUpdate,
       "apLoadFlag": apLoadFlag,
       "apFileName": apFileName,
       "apFileType": apFileType,
       "apTransProtocol": apTransProtocol,
       "apServerAddr": apServerAddr,
       "apServerPort": apServerPort,
       "apServerUsername": apServerUsername,
       "apServerPasswd": apServerPasswd,
       "apTransStatus": apTransStatus,
       "apFailReason": apFailReason,
       "apCfgFileDistribute": apCfgFileDistribute,
       "apCfgFileLoadFlag": apCfgFileLoadFlag,
       "apCfgFileFileName": apCfgFileFileName,
       "apCfgFileFileType": apCfgFileFileType,
       "apCfgFileTransProtocol": apCfgFileTransProtocol,
       "apCfgFileServerAddr": apCfgFileServerAddr,
       "apCfgFileServerPort": apCfgFileServerPort,
       "apCfgFileServerUsername": apCfgFileServerUsername,
       "apCfgFileServerPasswd": apCfgFileServerPasswd,
       "apCfgFileTransStatus": apCfgFileTransStatus,
       "apCfgFileFailReason": apCfgFileFailReason,
       "apAccessControl": apAccessControl,
       "apTerminalPermitTable": apTerminalPermitTable,
       "apTerminalPermitEntry": apTerminalPermitEntry,
       "apWhiteListIndex": apWhiteListIndex,
       "apPermitMAC": apPermitMAC,
       "apWhiteListStatus": apWhiteListStatus,
       "apTerminalDeniedTable": apTerminalDeniedTable,
       "apTerminalDeniedEntry": apTerminalDeniedEntry,
       "apBlackListIndex": apBlackListIndex,
       "apAttackDeviceMAC": apAttackDeviceMAC,
       "apBlackListStatus": apBlackListStatus,
       "apTrapConfig": apTrapConfig,
       "apTrapResendWaitingTime": apTrapResendWaitingTime,
       "apCPUusageThreshhd": apCPUusageThreshhd,
       "apMemUsageThreshhd": apMemUsageThreshhd,
       "apAPCoInterfThreshhd": apAPCoInterfThreshhd,
       "apAPNeiborInterfThreshhd": apAPNeiborInterfThreshhd,
       "apStaInterfNumThreshhd": apStaInterfNumThreshhd,
       "apHeartbeatOnOff": apHeartbeatOnOff,
       "apHeartbeatPeriod": apHeartbeatPeriod,
       "apTrapAddrTable": apTrapAddrTable,
       "apTrapAddrEntry": apTrapAddrEntry,
       "apTrapDesAddrIndex": apTrapDesAddrIndex,
       "apTrapDesIPAddress": apTrapDesIPAddress,
       "apTrapAddrStatus": apTrapAddrStatus,
       "apTrapEnabledTable": apTrapEnabledTable,
       "apTrapEnabledEntry": apTrapEnabledEntry,
       "apTrapEnabledIndex": apTrapEnabledIndex,
       "apTrapName": apTrapName,
       "apTrapDescr": apTrapDescr,
       "apTrapOnOff": apTrapOnOff,
       "apVlanConfig": apVlanConfig,
       "apVlanConfigTable": apVlanConfigTable,
       "apVlanConfigEntry": apVlanConfigEntry,
       "apVlanCfgVlanId": apVlanCfgVlanId,
       "apVlanCfgStatus": apVlanCfgStatus,
       "apHeartbeatConfig": apHeartbeatConfig,
       "apHeartbeatCycle": apHeartbeatCycle,
       "apPerformanceStatObjects": apPerformanceStatObjects,
       "apSysPerformanceStat": apSysPerformanceStat,
       "apCPURTUsage": apCPURTUsage,
       "apCPUAvgUsage": apCPUAvgUsage,
       "apMemRTUsage": apMemRTUsage,
       "apMemAvgUsage": apMemAvgUsage,
       "apConInfoStat": apConInfoStat,
       "apApStationAssocSum": apApStationAssocSum,
       "apApStationOnlineSum": apApStationOnlineSum,
       "apAssocTimes": apAssocTimes,
       "apAssocFailTimes": apAssocFailTimes,
       "apReassocTimes": apReassocTimes,
       "apPreAssCannotShiftDeassocFailSum": apPreAssCannotShiftDeassocFailSum,
       "apApStatsDisassociated": apApStatsDisassociated,
       "apAssocRejectSum": apAssocRejectSum,
       "apBSSNotSupportAssocFailSum": apBSSNotSupportAssocFailSum,
       "apIfPeformanceStat": apIfPeformanceStat,
       "apWiredIfPfmStatTable": apWiredIfPfmStatTable,
       "apWiredIfPfmStatEntry": apWiredIfPfmStatEntry,
       "apIfInUcastPkts": apIfInUcastPkts,
       "apIfInNUcastPkts": apIfInNUcastPkts,
       "apIfInOctets": apIfInOctets,
       "apIfInDiscardPkts": apIfInDiscardPkts,
       "apIfInErrors": apIfInErrors,
       "apIfOutUcastPkts": apIfOutUcastPkts,
       "apIfOutNUcastPkts": apIfOutNUcastPkts,
       "apIfOutOctets": apIfOutOctets,
       "apIfOutDiscardPkts": apIfOutDiscardPkts,
       "apIfOutErrors": apIfOutErrors,
       "apIfUpDwnTimes": apIfUpDwnTimes,
       "apRadioIfPfmStatTable": apRadioIfPfmStatTable,
       "apRadioIfPfmStatEntry": apRadioIfPfmStatEntry,
       "apAvgRxSignalStrength": apAvgRxSignalStrength,
       "apHighestRxSignalStrength": apHighestRxSignalStrength,
       "apLowestRxSignalStrength": apLowestRxSignalStrength,
       "apUpdownTimes": apUpdownTimes,
       "apTxDataPkts": apTxDataPkts,
       "apRxDataPkts": apRxDataPkts,
       "apUplinkDataOctets": apUplinkDataOctets,
       "apDwlinkDataOctets": apDwlinkDataOctets,
       "apChStatsDwlinkTotRetryPkts": apChStatsDwlinkTotRetryPkts,
       "apChStatsPhyErrPkts": apChStatsPhyErrPkts,
       "apChStatsMacFcsErrPkts": apChStatsMacFcsErrPkts,
       "apChStatsMacMicErrPkts": apChStatsMacMicErrPkts,
       "apChStatsMacDecryptErrPkts": apChStatsMacDecryptErrPkts,
       "apChStatsTotalErrPkts": apChStatsTotalErrPkts,
       "apRxMgmtFrameCnt": apRxMgmtFrameCnt,
       "apRxCtrlFrameCnt": apRxCtrlFrameCnt,
       "apRxDataFrameCnt": apRxDataFrameCnt,
       "apTxMgmtFrameCnt": apTxMgmtFrameCnt,
       "apTxCtrlFrameCnt": apTxCtrlFrameCnt,
       "apTxDataFrameCnt": apTxDataFrameCnt,
       "apChStatsFrameErrorCnt": apChStatsFrameErrorCnt,
       "apRetryCnt": apRetryCnt,
       "apCurTxPwr": apCurTxPwr,
       "apAPNeighborSSIDList": apAPNeighborSSIDList,
       "apChanStaNum": apChanStaNum,
       "apChDownUnicastFrame": apChDownUnicastFrame,
       "apChDownNonUnicastFrame": apChDownNonUnicastFrame,
       "apChRxAuthFrame": apChRxAuthFrame,
       "apChRxAssoFrame": apChRxAssoFrame,
       "apChTxAuthFrame": apChTxAuthFrame,
       "apChTxAssoFrame": apChTxAssoFrame,
       "apSSIDPeformanceStat": apSSIDPeformanceStat,
       "apSSIDPfmStatTable": apSSIDPfmStatTable,
       "apSSIDPfmStatEntry": apSSIDPfmStatEntry,
       "apSSIDTxDataPkts": apSSIDTxDataPkts,
       "apSSIDRxDataPkts": apSSIDRxDataPkts,
       "apSSIDUplinkDataOctets": apSSIDUplinkDataOctets,
       "apSSIDDwlinkDataOctets": apSSIDDwlinkDataOctets,
       "apSSIDChStatsDwlinkTotRetryPkts": apSSIDChStatsDwlinkTotRetryPkts,
       "apSSIDApChStatsNumStations": apSSIDApChStatsNumStations,
       "apTermPeformanceStat": apTermPeformanceStat,
       "apTermPfmStatTable": apTermPfmStatTable,
       "apTermPfmStatEntry": apTermPfmStatEntry,
       "apStaAddress": apStaAddress,
       "apStaUpTime": apStaUpTime,
       "apAPReceivedStaSignalStrength": apAPReceivedStaSignalStrength,
       "apAPReceiveStaSNR": apAPReceiveStaSNR,
       "apStaTxPkts": apStaTxPkts,
       "apStaTxBytes": apStaTxBytes,
       "apStaRxPkts": apStaRxPkts,
       "apStaRxBytes": apStaRxBytes,
       "apWAPIPeformanceStat": apWAPIPeformanceStat,
       "apWAPIPfmStatTable": apWAPIPfmStatTable,
       "apWAPIPfmStatEntry": apWAPIPfmStatEntry,
       "apSTAAddress": apSTAAddress,
       "apVersion": apVersion,
       "apControlledPortStatus": apControlledPortStatus,
       "apSelectedUnicastCipher": apSelectedUnicastCipher,
       "apWPIReplayCounters": apWPIReplayCounters,
       "apWPIDecryptableErrors": apWPIDecryptableErrors,
       "apWPIMICErrors": apWPIMICErrors,
       "apWAISignatureErrors": apWAISignatureErrors,
       "apWAIHMACErrors": apWAIHMACErrors,
       "apWAIAuthResultFailures": apWAIAuthResultFailures,
       "apWAIDiscardCounters": apWAIDiscardCounters,
       "apWAITimeoutCounters": apWAITimeoutCounters,
       "apWAIFormatErrors": apWAIFormatErrors,
       "apWAICertificateHandshakeFailures": apWAICertificateHandshakeFailures,
       "apWAIUnicastHandshakeFailures": apWAIUnicastHandshakeFailures,
       "apWAIMulticastHandshakeFailures": apWAIMulticastHandshakeFailures,
       "apQOSPeformanceStat": apQOSPeformanceStat,
       "apQosBasePfmStatTable": apQosBasePfmStatTable,
       "apQosBasePfmStatEntry": apQosBasePfmStatEntry,
       "apQoSSvcQueAvgLen": apQoSSvcQueAvgLen,
       "apQoSSvcPktLossRatio": apQoSSvcPktLossRatio,
       "apAvgTransSpeed": apAvgTransSpeed,
       "apBackgroundQosPfmStatTable": apBackgroundQosPfmStatTable,
       "apBackgroundQosPfmStatEntry": apBackgroundQosPfmStatEntry,
       "apBgQueAvgLen": apBgQueAvgLen,
       "apBgAvgBurst": apBgAvgBurst,
       "apBgPktLossRatio": apBgPktLossRatio,
       "apBgAvgTransSpeed": apBgAvgTransSpeed,
       "apBgSvcLoss": apBgSvcLoss,
       "apBestEffortQosPfmStatTable": apBestEffortQosPfmStatTable,
       "apBestEffortQosPfmStatEntry": apBestEffortQosPfmStatEntry,
       "apBeQueAvgLen": apBeQueAvgLen,
       "apBeAvgBurst": apBeAvgBurst,
       "apBePktLossRatio": apBePktLossRatio,
       "apBeAvgTransSpeed": apBeAvgTransSpeed,
       "apBeSvcLoss": apBeSvcLoss,
       "apVoiceQosPfmStatTable": apVoiceQosPfmStatTable,
       "apVoiceQosPfmStatEntry": apVoiceQosPfmStatEntry,
       "apVoiceQueAvgLen": apVoiceQueAvgLen,
       "apVoiceAvgBurst": apVoiceAvgBurst,
       "apVoicePktLossRatio": apVoicePktLossRatio,
       "apVoiceAvgTransSpeed": apVoiceAvgTransSpeed,
       "apVoicePutThroughRatio": apVoicePutThroughRatio,
       "apVoiceDropRatio": apVoiceDropRatio,
       "apVoiceSvcLoss": apVoiceSvcLoss,
       "apVoiceExceedMaxUsersRequest": apVoiceExceedMaxUsersRequest,
       "apVedioQosPfmStatTable": apVedioQosPfmStatTable,
       "apVedioQosPfmStatEntry": apVedioQosPfmStatEntry,
       "apVedioQueAvgLen": apVedioQueAvgLen,
       "apVedioAvgBurst": apVedioAvgBurst,
       "apVedioPktLossRatio": apVedioPktLossRatio,
       "apVedioAvgTransSpeed": apVedioAvgTransSpeed,
       "apVedioPutThroughRatio": apVedioPutThroughRatio,
       "apVedioDropRatio": apVedioDropRatio,
       "apVedioSvcLoss": apVedioSvcLoss,
       "apVedioExceedMaxUsersRequest": apVedioExceedMaxUsersRequest}
)

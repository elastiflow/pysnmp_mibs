# SNMP MIB module (RUIJIE-CM-WAPI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-CM-WAPI-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:05:39 2025
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

cmStandardmibmodule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70)
)
if mibBuilder.loadTexts:
    cmStandardmibmodule.setRevisions(
        ("2010-02-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmStandardWAPITraps_ObjectIdentity = ObjectIdentity
cmStandardWAPITraps = _CmStandardWAPITraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 0)
)
_CmStandardMIBObjects_ObjectIdentity = ObjectIdentity
cmStandardMIBObjects = _CmStandardMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1)
)
_ApAttributeInfoTable_Object = MibTable
apAttributeInfoTable = _ApAttributeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 1)
)
if mibBuilder.loadTexts:
    apAttributeInfoTable.setStatus("current")
_ApAttributeInfoEntry_Object = MibTableRow
apAttributeInfoEntry = _ApAttributeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 1, 1)
)
apAttributeInfoEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    apAttributeInfoEntry.setStatus("current")


class _ApSysNEId_Type(DisplayString):
    """Custom type apSysNEId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 255),
    )


_ApSysNEId_Type.__name__ = "DisplayString"
_ApSysNEId_Object = MibTableColumn
apSysNEId = _ApSysNEId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 1, 1, 1),
    _ApSysNEId_Type()
)
apSysNEId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSysNEId.setStatus("current")


class _ApSysHostName_Type(DisplayString):
    """Custom type apSysHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 255),
    )


_ApSysHostName_Type.__name__ = "DisplayString"
_ApSysHostName_Object = MibTableColumn
apSysHostName = _ApSysHostName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 1, 1, 2),
    _ApSysHostName_Type()
)
apSysHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSysHostName.setStatus("current")
_ApSysLocation_Type = DisplayString
_ApSysLocation_Object = MibTableColumn
apSysLocation = _ApSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 1, 1, 3),
    _ApSysLocation_Type()
)
apSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSysLocation.setStatus("current")
_ApManufacturer_Type = DisplayString
_ApManufacturer_Object = MibTableColumn
apManufacturer = _ApManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 1, 1, 4),
    _ApManufacturer_Type()
)
apManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apManufacturer.setStatus("current")
_ApSysVersion_Type = DisplayString
_ApSysVersion_Object = MibTableColumn
apSysVersion = _ApSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 1, 1, 5),
    _ApSysVersion_Type()
)
apSysVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSysVersion.setStatus("current")
_ApMacAddressConnectedWithAC_Type = DisplayString
_ApMacAddressConnectedWithAC_Object = MibTableColumn
apMacAddressConnectedWithAC = _ApMacAddressConnectedWithAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 1, 1, 6),
    _ApMacAddressConnectedWithAC_Type()
)
apMacAddressConnectedWithAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMacAddressConnectedWithAC.setStatus("current")
_ApCurrentBSSID_Type = DisplayString
_ApCurrentBSSID_Object = MibTableColumn
apCurrentBSSID = _ApCurrentBSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 1, 1, 7),
    _ApCurrentBSSID_Type()
)
apCurrentBSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCurrentBSSID.setStatus("current")
_ApMaxSimultUsers_Type = Integer32
_ApMaxSimultUsers_Object = MibTableColumn
apMaxSimultUsers = _ApMaxSimultUsers_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 1, 1, 8),
    _ApMaxSimultUsers_Type()
)
apMaxSimultUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMaxSimultUsers.setStatus("current")
_ApMaxSimultTraffic_Type = Integer32
_ApMaxSimultTraffic_Object = MibTableColumn
apMaxSimultTraffic = _ApMaxSimultTraffic_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 1, 1, 9),
    _ApMaxSimultTraffic_Type()
)
apMaxSimultTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMaxSimultTraffic.setStatus("current")
_ApUpTime_Type = Integer32
_ApUpTime_Object = MibTableColumn
apUpTime = _ApUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 1, 1, 10),
    _ApUpTime_Type()
)
apUpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apUpTime.setStatus("current")
_ApconfigurationInfoTable_Object = MibTable
apconfigurationInfoTable = _ApconfigurationInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 2)
)
if mibBuilder.loadTexts:
    apconfigurationInfoTable.setStatus("current")
_ApconfigurationInfoEntry_Object = MibTableRow
apconfigurationInfoEntry = _ApconfigurationInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 2, 1)
)
apconfigurationInfoEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    apconfigurationInfoEntry.setStatus("current")
_ApIPAddress_Type = IpAddress
_ApIPAddress_Object = MibTableColumn
apIPAddress = _ApIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 2, 1, 1),
    _ApIPAddress_Type()
)
apIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIPAddress.setStatus("current")
_ApIpAdEntNetMask_Type = IpAddress
_ApIpAdEntNetMask_Object = MibTableColumn
apIpAdEntNetMask = _ApIpAdEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 2, 1, 2),
    _ApIpAdEntNetMask_Type()
)
apIpAdEntNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpAdEntNetMask.setStatus("current")
_ApWorkingMode_Type = Integer32
_ApWorkingMode_Object = MibTableColumn
apWorkingMode = _ApWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 2, 1, 3),
    _ApWorkingMode_Type()
)
apWorkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWorkingMode.setStatus("current")
_ApBGmode_Type = Integer32
_ApBGmode_Object = MibTableColumn
apBGmode = _ApBGmode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 2, 1, 4),
    _ApBGmode_Type()
)
apBGmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBGmode.setStatus("current")
_ApacWAPIconfigurationInfoTable_Object = MibTable
apacWAPIconfigurationInfoTable = _ApacWAPIconfigurationInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 3)
)
if mibBuilder.loadTexts:
    apacWAPIconfigurationInfoTable.setStatus("current")
_ApacWAPIconfigurationInfoEntry_Object = MibTableRow
apacWAPIconfigurationInfoEntry = _ApacWAPIconfigurationInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 3, 1)
)
apacWAPIconfigurationInfoEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    apacWAPIconfigurationInfoEntry.setStatus("current")
_ApWAPIAuthMode_Type = TruthValue
_ApWAPIAuthMode_Object = MibTableColumn
apWAPIAuthMode = _ApWAPIAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 3, 1, 1),
    _ApWAPIAuthMode_Type()
)
apWAPIAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIAuthMode.setStatus("current")
_AcWAPIAuthMode_Type = TruthValue
_AcWAPIAuthMode_Object = MibTableColumn
acWAPIAuthMode = _AcWAPIAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 3, 1, 2),
    _AcWAPIAuthMode_Type()
)
acWAPIAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acWAPIAuthMode.setStatus("current")
_AcWAPIASIPAddress_Type = IpAddress
_AcWAPIASIPAddress_Object = MibTableColumn
acWAPIASIPAddress = _AcWAPIASIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 3, 1, 3),
    _AcWAPIASIPAddress_Type()
)
acWAPIASIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acWAPIASIPAddress.setStatus("current")
_AcWAPICertInstalled_Type = TruthValue
_AcWAPICertInstalled_Object = MibTableColumn
acWAPICertInstalled = _AcWAPICertInstalled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 3, 1, 4),
    _AcWAPICertInstalled_Type()
)
acWAPICertInstalled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acWAPICertInstalled.setStatus("current")
_CpuHandleAbility_Type = OctetString
_CpuHandleAbility_Object = MibTableColumn
cpuHandleAbility = _CpuHandleAbility_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 3, 1, 5),
    _CpuHandleAbility_Type()
)
cpuHandleAbility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuHandleAbility.setStatus("current")
_MemoryCapacity_Type = OctetString
_MemoryCapacity_Object = MibTableColumn
memoryCapacity = _MemoryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 3, 1, 6),
    _MemoryCapacity_Type()
)
memoryCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryCapacity.setStatus("current")
_FlashmemCapacity_Type = OctetString
_FlashmemCapacity_Object = MibTableColumn
flashmemCapacity = _FlashmemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 3, 1, 7),
    _FlashmemCapacity_Type()
)
flashmemCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flashmemCapacity.setStatus("current")
_Support80211g_Type = OctetString
_Support80211g_Object = MibTableColumn
support80211g = _Support80211g_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 3, 1, 8),
    _Support80211g_Type()
)
support80211g.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    support80211g.setStatus("current")
_ApWAPIMaxUserNum_Type = Integer32
_ApWAPIMaxUserNum_Object = MibTableColumn
apWAPIMaxUserNum = _ApWAPIMaxUserNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 3, 1, 9),
    _ApWAPIMaxUserNum_Type()
)
apWAPIMaxUserNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIMaxUserNum.setStatus("current")
_PeruserWAPIMaxBindwithAllocated_Type = Integer32
_PeruserWAPIMaxBindwithAllocated_Object = MibTableColumn
peruserWAPIMaxBindwithAllocated = _PeruserWAPIMaxBindwithAllocated_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 3, 1, 10),
    _PeruserWAPIMaxBindwithAllocated_Type()
)
peruserWAPIMaxBindwithAllocated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    peruserWAPIMaxBindwithAllocated.setStatus("current")
_MutiModeAccesssimultStatus_Type = TruthValue
_MutiModeAccesssimultStatus_Object = MibTableColumn
mutiModeAccesssimultStatus = _MutiModeAccesssimultStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 3, 1, 11),
    _MutiModeAccesssimultStatus_Type()
)
mutiModeAccesssimultStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mutiModeAccesssimultStatus.setStatus("current")
_Gb15629dot11wapiConfigExtraTable_Object = MibTable
gb15629dot11wapiConfigExtraTable = _Gb15629dot11wapiConfigExtraTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 4)
)
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigExtraTable.setStatus("current")
_Gb15629dot11wapiConfigExtraEntry_Object = MibTableRow
gb15629dot11wapiConfigExtraEntry = _Gb15629dot11wapiConfigExtraEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 4, 1)
)
gb15629dot11wapiConfigExtraEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigExtraEntry.setStatus("current")
_Gb15629dot11wapiGroupCipherRequested_Type = DisplayString
_Gb15629dot11wapiGroupCipherRequested_Object = MibTableColumn
gb15629dot11wapiGroupCipherRequested = _Gb15629dot11wapiGroupCipherRequested_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 4, 1, 1),
    _Gb15629dot11wapiGroupCipherRequested_Type()
)
gb15629dot11wapiGroupCipherRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiGroupCipherRequested.setStatus("current")
_Gb15629dot11wapiConfigUnicastCipher_Type = DisplayString
_Gb15629dot11wapiConfigUnicastCipher_Object = MibTableColumn
gb15629dot11wapiConfigUnicastCipher = _Gb15629dot11wapiConfigUnicastCipher_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 4, 1, 2),
    _Gb15629dot11wapiConfigUnicastCipher_Type()
)
gb15629dot11wapiConfigUnicastCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigUnicastCipher.setStatus("current")
_Gb15629dot11wapiConfigUnicastCipherEnabled_Type = TruthValue
_Gb15629dot11wapiConfigUnicastCipherEnabled_Object = MibTableColumn
gb15629dot11wapiConfigUnicastCipherEnabled = _Gb15629dot11wapiConfigUnicastCipherEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 4, 1, 3),
    _Gb15629dot11wapiConfigUnicastCipherEnabled_Type()
)
gb15629dot11wapiConfigUnicastCipherEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigUnicastCipherEnabled.setStatus("current")
_Gb15629dot11wapiConfigUnicastCipherSize_Type = Unsigned32
_Gb15629dot11wapiConfigUnicastCipherSize_Object = MibTableColumn
gb15629dot11wapiConfigUnicastCipherSize = _Gb15629dot11wapiConfigUnicastCipherSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 4, 1, 4),
    _Gb15629dot11wapiConfigUnicastCipherSize_Type()
)
gb15629dot11wapiConfigUnicastCipherSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigUnicastCipherSize.setStatus("current")
_Gb15629dot11wapiConfigAuthenticationSuite_Type = DisplayString
_Gb15629dot11wapiConfigAuthenticationSuite_Object = MibTableColumn
gb15629dot11wapiConfigAuthenticationSuite = _Gb15629dot11wapiConfigAuthenticationSuite_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 4, 1, 5),
    _Gb15629dot11wapiConfigAuthenticationSuite_Type()
)
gb15629dot11wapiConfigAuthenticationSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigAuthenticationSuite.setStatus("current")
_Gb15629dot11wapiConfigAuthenticationSuiteEnabled_Type = TruthValue
_Gb15629dot11wapiConfigAuthenticationSuiteEnabled_Object = MibTableColumn
gb15629dot11wapiConfigAuthenticationSuiteEnabled = _Gb15629dot11wapiConfigAuthenticationSuiteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 4, 1, 6),
    _Gb15629dot11wapiConfigAuthenticationSuiteEnabled_Type()
)
gb15629dot11wapiConfigAuthenticationSuiteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigAuthenticationSuiteEnabled.setStatus("current")
_ApacsoftorHardwareconfigInfoTable_Object = MibTable
apacsoftorHardwareconfigInfoTable = _ApacsoftorHardwareconfigInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 5)
)
if mibBuilder.loadTexts:
    apacsoftorHardwareconfigInfoTable.setStatus("current")
_ApacsoftorHardwareconfigInfoEntry_Object = MibTableRow
apacsoftorHardwareconfigInfoEntry = _ApacsoftorHardwareconfigInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 5, 1)
)
apacsoftorHardwareconfigInfoEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    apacsoftorHardwareconfigInfoEntry.setStatus("current")
_ApSoftwareName_Type = OctetString
_ApSoftwareName_Object = MibTableColumn
apSoftwareName = _ApSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 5, 1, 1),
    _ApSoftwareName_Type()
)
apSoftwareName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSoftwareName.setStatus("current")
_ApSoftwareVersion_Type = DisplayString
_ApSoftwareVersion_Object = MibTableColumn
apSoftwareVersion = _ApSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 5, 1, 2),
    _ApSoftwareVersion_Type()
)
apSoftwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSoftwareVersion.setStatus("current")
_ApSoftwareVendor_Type = DisplayString
_ApSoftwareVendor_Object = MibTableColumn
apSoftwareVendor = _ApSoftwareVendor_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 5, 1, 3),
    _ApSoftwareVendor_Type()
)
apSoftwareVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSoftwareVendor.setStatus("current")
_AcSoftwareName_Type = OctetString
_AcSoftwareName_Object = MibTableColumn
acSoftwareName = _AcSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 5, 1, 4),
    _AcSoftwareName_Type()
)
acSoftwareName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSoftwareName.setStatus("current")
_AcSoftwareVersion_Type = DisplayString
_AcSoftwareVersion_Object = MibTableColumn
acSoftwareVersion = _AcSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 5, 1, 5),
    _AcSoftwareVersion_Type()
)
acSoftwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSoftwareVersion.setStatus("current")
_AcSoftwareVendor_Type = DisplayString
_AcSoftwareVendor_Object = MibTableColumn
acSoftwareVendor = _AcSoftwareVendor_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 5, 1, 6),
    _AcSoftwareVendor_Type()
)
acSoftwareVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSoftwareVendor.setStatus("current")
_ApPhyInterfaceConfigurationParametersTable_Object = MibTable
apPhyInterfaceConfigurationParametersTable = _ApPhyInterfaceConfigurationParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 6)
)
if mibBuilder.loadTexts:
    apPhyInterfaceConfigurationParametersTable.setStatus("current")
_ApPhyInterfaceConfigurationParametersEntry_Object = MibTableRow
apPhyInterfaceConfigurationParametersEntry = _ApPhyInterfaceConfigurationParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 6, 1)
)
apPhyInterfaceConfigurationParametersEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    apPhyInterfaceConfigurationParametersEntry.setStatus("current")
_ApIfNumber_Type = Integer32
_ApIfNumber_Object = MibTableColumn
apIfNumber = _ApIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 6, 1, 1),
    _ApIfNumber_Type()
)
apIfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfNumber.setStatus("current")


class _ApIfDescr_Type(DisplayString):
    """Custom type apIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApIfDescr_Type.__name__ = "DisplayString"
_ApIfDescr_Object = MibTableColumn
apIfDescr = _ApIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 6, 1, 2),
    _ApIfDescr_Type()
)
apIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfDescr.setStatus("current")
_ApIfType_Type = Integer32
_ApIfType_Object = MibTableColumn
apIfType = _ApIfType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 6, 1, 3),
    _ApIfType_Type()
)
apIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfType.setStatus("current")
_ApIfMtu_Type = Integer32
_ApIfMtu_Object = MibTableColumn
apIfMtu = _ApIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 6, 1, 4),
    _ApIfMtu_Type()
)
apIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfMtu.setStatus("current")
_ApIfSpeed_Type = Gauge32
_ApIfSpeed_Object = MibTableColumn
apIfSpeed = _ApIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 6, 1, 5),
    _ApIfSpeed_Type()
)
apIfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfSpeed.setStatus("current")
_ApIfPhysAddress_Type = OctetString
_ApIfPhysAddress_Object = MibTableColumn
apIfPhysAddress = _ApIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 6, 1, 6),
    _ApIfPhysAddress_Type()
)
apIfPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfPhysAddress.setStatus("current")
_RadioInterfacePerformanceParameterTable_Object = MibTable
radioInterfacePerformanceParameterTable = _RadioInterfacePerformanceParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 7)
)
if mibBuilder.loadTexts:
    radioInterfacePerformanceParameterTable.setStatus("current")
_RadioInterfacePerformanceParameterEntry_Object = MibTableRow
radioInterfacePerformanceParameterEntry = _RadioInterfacePerformanceParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 7, 1)
)
radioInterfacePerformanceParameterEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    radioInterfacePerformanceParameterEntry.setStatus("current")
_ApUplinkUpdownTimes_Type = Counter32
_ApUplinkUpdownTimes_Object = MibTableColumn
apUplinkUpdownTimes = _ApUplinkUpdownTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 7, 1, 1),
    _ApUplinkUpdownTimes_Type()
)
apUplinkUpdownTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apUplinkUpdownTimes.setStatus("current")
_ApDownlinkUpdownTimes_Type = Counter32
_ApDownlinkUpdownTimes_Object = MibTableColumn
apDownlinkUpdownTimes = _ApDownlinkUpdownTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 1, 7, 1, 2),
    _ApDownlinkUpdownTimes_Type()
)
apDownlinkUpdownTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDownlinkUpdownTimes.setStatus("current")
_CmStandardCompliances_ObjectIdentity = ObjectIdentity
cmStandardCompliances = _CmStandardCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 2)
)
_CmStandardGroup_ObjectIdentity = ObjectIdentity
cmStandardGroup = _CmStandardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 3)
)
_CmStandardWAPITrapsObjects_ObjectIdentity = ObjectIdentity
cmStandardWAPITrapsObjects = _CmStandardWAPITrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 4)
)
_ApOriginalIP_Type = IpAddress
_ApOriginalIP_Object = MibScalar
apOriginalIP = _ApOriginalIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 4, 1),
    _ApOriginalIP_Type()
)
apOriginalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apOriginalIP.setStatus("current")
_ApCurrentIP_Type = IpAddress
_ApCurrentIP_Object = MibScalar
apCurrentIP = _ApCurrentIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 4, 2),
    _ApCurrentIP_Type()
)
apCurrentIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCurrentIP.setStatus("current")
_RuijieWAPIClientIP_Type = IpAddress
_RuijieWAPIClientIP_Object = MibScalar
ruijieWAPIClientIP = _RuijieWAPIClientIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 4, 3),
    _RuijieWAPIClientIP_Type()
)
ruijieWAPIClientIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWAPIClientIP.setStatus("current")
_RuijieWAPIClientOtherInfo_Type = DisplayString
_RuijieWAPIClientOtherInfo_Object = MibScalar
ruijieWAPIClientOtherInfo = _RuijieWAPIClientOtherInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 4, 4),
    _RuijieWAPIClientOtherInfo_Type()
)
ruijieWAPIClientOtherInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWAPIClientOtherInfo.setStatus("current")
_RuijieWAPIIllegalClientIP_Type = IpAddress
_RuijieWAPIIllegalClientIP_Object = MibScalar
ruijieWAPIIllegalClientIP = _RuijieWAPIIllegalClientIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 4, 5),
    _RuijieWAPIIllegalClientIP_Type()
)
ruijieWAPIIllegalClientIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWAPIIllegalClientIP.setStatus("current")
_RuijieWAPIIllegalClientOtherInfo_Type = DisplayString
_RuijieWAPIIllegalClientOtherInfo_Object = MibScalar
ruijieWAPIIllegalClientOtherInfo = _RuijieWAPIIllegalClientOtherInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 4, 6),
    _RuijieWAPIIllegalClientOtherInfo_Type()
)
ruijieWAPIIllegalClientOtherInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWAPIIllegalClientOtherInfo.setStatus("current")

# Managed Objects groups

cmStandardBase = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 3, 1)
)
cmStandardBase.setObjects(
      *(("RUIJIE-CM-WAPI-MIB", "apSysNEId"),
        ("RUIJIE-CM-WAPI-MIB", "apSysHostName"),
        ("RUIJIE-CM-WAPI-MIB", "apSysLocation"),
        ("RUIJIE-CM-WAPI-MIB", "apManufacturer"),
        ("RUIJIE-CM-WAPI-MIB", "apSysVersion"),
        ("RUIJIE-CM-WAPI-MIB", "apMacAddressConnectedWithAC"),
        ("RUIJIE-CM-WAPI-MIB", "apCurrentBSSID"),
        ("RUIJIE-CM-WAPI-MIB", "apMaxSimultUsers"),
        ("RUIJIE-CM-WAPI-MIB", "apMaxSimultTraffic"),
        ("RUIJIE-CM-WAPI-MIB", "apUpTime"),
        ("RUIJIE-CM-WAPI-MIB", "apIPAddress"),
        ("RUIJIE-CM-WAPI-MIB", "apIpAdEntNetMask"),
        ("RUIJIE-CM-WAPI-MIB", "apWorkingMode"),
        ("RUIJIE-CM-WAPI-MIB", "apBGmode"),
        ("RUIJIE-CM-WAPI-MIB", "apWAPIAuthMode"),
        ("RUIJIE-CM-WAPI-MIB", "acWAPIAuthMode"),
        ("RUIJIE-CM-WAPI-MIB", "acWAPIASIPAddress"),
        ("RUIJIE-CM-WAPI-MIB", "acWAPICertInstalled"),
        ("RUIJIE-CM-WAPI-MIB", "cpuHandleAbility"),
        ("RUIJIE-CM-WAPI-MIB", "memoryCapacity"),
        ("RUIJIE-CM-WAPI-MIB", "flashmemCapacity"),
        ("RUIJIE-CM-WAPI-MIB", "support80211g"),
        ("RUIJIE-CM-WAPI-MIB", "apWAPIMaxUserNum"),
        ("RUIJIE-CM-WAPI-MIB", "peruserWAPIMaxBindwithAllocated"),
        ("RUIJIE-CM-WAPI-MIB", "mutiModeAccesssimultStatus"),
        ("RUIJIE-CM-WAPI-MIB", "gb15629dot11wapiGroupCipherRequested"),
        ("RUIJIE-CM-WAPI-MIB", "gb15629dot11wapiConfigUnicastCipher"),
        ("RUIJIE-CM-WAPI-MIB", "gb15629dot11wapiConfigUnicastCipherEnabled"),
        ("RUIJIE-CM-WAPI-MIB", "gb15629dot11wapiConfigUnicastCipherSize"),
        ("RUIJIE-CM-WAPI-MIB", "gb15629dot11wapiConfigAuthenticationSuite"),
        ("RUIJIE-CM-WAPI-MIB", "gb15629dot11wapiConfigAuthenticationSuiteEnabled"),
        ("RUIJIE-CM-WAPI-MIB", "apSoftwareName"),
        ("RUIJIE-CM-WAPI-MIB", "apSoftwareVersion"),
        ("RUIJIE-CM-WAPI-MIB", "apSoftwareVendor"),
        ("RUIJIE-CM-WAPI-MIB", "acSoftwareName"),
        ("RUIJIE-CM-WAPI-MIB", "acSoftwareVersion"),
        ("RUIJIE-CM-WAPI-MIB", "acSoftwareVendor"),
        ("RUIJIE-CM-WAPI-MIB", "apIfNumber"),
        ("RUIJIE-CM-WAPI-MIB", "apIfDescr"),
        ("RUIJIE-CM-WAPI-MIB", "apIfType"),
        ("RUIJIE-CM-WAPI-MIB", "apIfMtu"),
        ("RUIJIE-CM-WAPI-MIB", "apIfSpeed"),
        ("RUIJIE-CM-WAPI-MIB", "apIfPhysAddress"),
        ("RUIJIE-CM-WAPI-MIB", "apUplinkUpdownTimes"),
        ("RUIJIE-CM-WAPI-MIB", "apDownlinkUpdownTimes"),
        ("RUIJIE-CM-WAPI-MIB", "apOriginalIP"),
        ("RUIJIE-CM-WAPI-MIB", "apCurrentIP"),
        ("RUIJIE-CM-WAPI-MIB", "ruijieWAPIClientIP"),
        ("RUIJIE-CM-WAPI-MIB", "ruijieWAPIClientOtherInfo"),
        ("RUIJIE-CM-WAPI-MIB", "ruijieWAPIIllegalClientIP"),
        ("RUIJIE-CM-WAPI-MIB", "ruijieWAPIIllegalClientOtherInfo"))
)
if mibBuilder.loadTexts:
    cmStandardBase.setStatus("current")


# Notification objects

apDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 0, 1)
)
if mibBuilder.loadTexts:
    apDown.setStatus(
        "current"
    )

apSysStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 0, 2)
)
if mibBuilder.loadTexts:
    apSysStart.setStatus(
        "current"
    )

apIPChangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 0, 3)
)
apIPChangeAlarm.setObjects(
      *(("RUIJIE-CM-WAPI-MIB", "apOriginalIP"),
        ("RUIJIE-CM-WAPI-MIB", "apCurrentIP"))
)
if mibBuilder.loadTexts:
    apIPChangeAlarm.setStatus(
        "current"
    )

flashWriteFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 0, 4)
)
if mibBuilder.loadTexts:
    flashWriteFail.setStatus(
        "current"
    )

userwithInvalidCerficationInbreakNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 0, 5)
)
userwithInvalidCerficationInbreakNetwork.setObjects(
      *(("RUIJIE-CM-WAPI-MIB", "ruijieWAPIClientIP"),
        ("RUIJIE-CM-WAPI-MIB", "ruijieWAPIClientOtherInfo"))
)
if mibBuilder.loadTexts:
    userwithInvalidCerficationInbreakNetwork.setStatus(
        "current"
    )

stationRepititiveAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 0, 6)
)
stationRepititiveAttack.setObjects(
      *(("RUIJIE-CM-WAPI-MIB", "ruijieWAPIIllegalClientIP"),
        ("RUIJIE-CM-WAPI-MIB", "ruijieWAPIIllegalClientOtherInfo"))
)
if mibBuilder.loadTexts:
    stationRepititiveAttack.setStatus(
        "current"
    )

tamperAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 0, 7)
)
tamperAttack.setObjects(
      *(("RUIJIE-CM-WAPI-MIB", "ruijieWAPIIllegalClientIP"),
        ("RUIJIE-CM-WAPI-MIB", "ruijieWAPIIllegalClientOtherInfo"))
)
if mibBuilder.loadTexts:
    tamperAttack.setStatus(
        "current"
    )

lowSafeLevelAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 0, 8)
)
lowSafeLevelAttack.setObjects(
      *(("RUIJIE-CM-WAPI-MIB", "ruijieWAPIIllegalClientIP"),
        ("RUIJIE-CM-WAPI-MIB", "ruijieWAPIIllegalClientOtherInfo"))
)
if mibBuilder.loadTexts:
    lowSafeLevelAttack.setStatus(
        "current"
    )

addressRedirectionAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 0, 9)
)
addressRedirectionAttack.setObjects(
      *(("RUIJIE-CM-WAPI-MIB", "ruijieWAPIIllegalClientIP"),
        ("RUIJIE-CM-WAPI-MIB", "ruijieWAPIIllegalClientOtherInfo"))
)
if mibBuilder.loadTexts:
    addressRedirectionAttack.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

cmStandardCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 70, 2, 2)
)
cmStandardCompliance.setObjects(
    ("RUIJIE-CM-WAPI-MIB", "cmStandardBase")
)
if mibBuilder.loadTexts:
    cmStandardCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-CM-WAPI-MIB",
    **{"cmStandardmibmodule": cmStandardmibmodule,
       "cmStandardWAPITraps": cmStandardWAPITraps,
       "apDown": apDown,
       "apSysStart": apSysStart,
       "apIPChangeAlarm": apIPChangeAlarm,
       "flashWriteFail": flashWriteFail,
       "userwithInvalidCerficationInbreakNetwork": userwithInvalidCerficationInbreakNetwork,
       "stationRepititiveAttack": stationRepititiveAttack,
       "tamperAttack": tamperAttack,
       "lowSafeLevelAttack": lowSafeLevelAttack,
       "addressRedirectionAttack": addressRedirectionAttack,
       "cmStandardMIBObjects": cmStandardMIBObjects,
       "apAttributeInfoTable": apAttributeInfoTable,
       "apAttributeInfoEntry": apAttributeInfoEntry,
       "apSysNEId": apSysNEId,
       "apSysHostName": apSysHostName,
       "apSysLocation": apSysLocation,
       "apManufacturer": apManufacturer,
       "apSysVersion": apSysVersion,
       "apMacAddressConnectedWithAC": apMacAddressConnectedWithAC,
       "apCurrentBSSID": apCurrentBSSID,
       "apMaxSimultUsers": apMaxSimultUsers,
       "apMaxSimultTraffic": apMaxSimultTraffic,
       "apUpTime": apUpTime,
       "apconfigurationInfoTable": apconfigurationInfoTable,
       "apconfigurationInfoEntry": apconfigurationInfoEntry,
       "apIPAddress": apIPAddress,
       "apIpAdEntNetMask": apIpAdEntNetMask,
       "apWorkingMode": apWorkingMode,
       "apBGmode": apBGmode,
       "apacWAPIconfigurationInfoTable": apacWAPIconfigurationInfoTable,
       "apacWAPIconfigurationInfoEntry": apacWAPIconfigurationInfoEntry,
       "apWAPIAuthMode": apWAPIAuthMode,
       "acWAPIAuthMode": acWAPIAuthMode,
       "acWAPIASIPAddress": acWAPIASIPAddress,
       "acWAPICertInstalled": acWAPICertInstalled,
       "cpuHandleAbility": cpuHandleAbility,
       "memoryCapacity": memoryCapacity,
       "flashmemCapacity": flashmemCapacity,
       "support80211g": support80211g,
       "apWAPIMaxUserNum": apWAPIMaxUserNum,
       "peruserWAPIMaxBindwithAllocated": peruserWAPIMaxBindwithAllocated,
       "mutiModeAccesssimultStatus": mutiModeAccesssimultStatus,
       "gb15629dot11wapiConfigExtraTable": gb15629dot11wapiConfigExtraTable,
       "gb15629dot11wapiConfigExtraEntry": gb15629dot11wapiConfigExtraEntry,
       "gb15629dot11wapiGroupCipherRequested": gb15629dot11wapiGroupCipherRequested,
       "gb15629dot11wapiConfigUnicastCipher": gb15629dot11wapiConfigUnicastCipher,
       "gb15629dot11wapiConfigUnicastCipherEnabled": gb15629dot11wapiConfigUnicastCipherEnabled,
       "gb15629dot11wapiConfigUnicastCipherSize": gb15629dot11wapiConfigUnicastCipherSize,
       "gb15629dot11wapiConfigAuthenticationSuite": gb15629dot11wapiConfigAuthenticationSuite,
       "gb15629dot11wapiConfigAuthenticationSuiteEnabled": gb15629dot11wapiConfigAuthenticationSuiteEnabled,
       "apacsoftorHardwareconfigInfoTable": apacsoftorHardwareconfigInfoTable,
       "apacsoftorHardwareconfigInfoEntry": apacsoftorHardwareconfigInfoEntry,
       "apSoftwareName": apSoftwareName,
       "apSoftwareVersion": apSoftwareVersion,
       "apSoftwareVendor": apSoftwareVendor,
       "acSoftwareName": acSoftwareName,
       "acSoftwareVersion": acSoftwareVersion,
       "acSoftwareVendor": acSoftwareVendor,
       "apPhyInterfaceConfigurationParametersTable": apPhyInterfaceConfigurationParametersTable,
       "apPhyInterfaceConfigurationParametersEntry": apPhyInterfaceConfigurationParametersEntry,
       "apIfNumber": apIfNumber,
       "apIfDescr": apIfDescr,
       "apIfType": apIfType,
       "apIfMtu": apIfMtu,
       "apIfSpeed": apIfSpeed,
       "apIfPhysAddress": apIfPhysAddress,
       "radioInterfacePerformanceParameterTable": radioInterfacePerformanceParameterTable,
       "radioInterfacePerformanceParameterEntry": radioInterfacePerformanceParameterEntry,
       "apUplinkUpdownTimes": apUplinkUpdownTimes,
       "apDownlinkUpdownTimes": apDownlinkUpdownTimes,
       "cmStandardCompliances": cmStandardCompliances,
       "cmStandardCompliance": cmStandardCompliance,
       "cmStandardGroup": cmStandardGroup,
       "cmStandardBase": cmStandardBase,
       "cmStandardWAPITrapsObjects": cmStandardWAPITrapsObjects,
       "apOriginalIP": apOriginalIP,
       "apCurrentIP": apCurrentIP,
       "ruijieWAPIClientIP": ruijieWAPIClientIP,
       "ruijieWAPIClientOtherInfo": ruijieWAPIClientOtherInfo,
       "ruijieWAPIIllegalClientIP": ruijieWAPIIllegalClientIP,
       "ruijieWAPIIllegalClientOtherInfo": ruijieWAPIIllegalClientOtherInfo}
)

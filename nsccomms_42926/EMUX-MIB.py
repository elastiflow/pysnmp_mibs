# SNMP MIB module (EMUX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nsccomms_42926/EMUX-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:13:34 2025
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

(dot1dBridge,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBridge")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(rstpMIB,) = mibBuilder.importSymbols(
    "RSTP-MIB",
    "rstpMIB")

(usmStats,) = mibBuilder.importSymbols(
    "SNMP-USER-BASED-SM-MIB",
    "usmStats")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")

(Float,) = mibBuilder.importSymbols(
    "UCD-SNMP-MIB",
    "Float")


# MODULE-IDENTITY

nsc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42926)
)
if mibBuilder.loadTexts:
    nsc.setRevisions(
        ("2018-07-31 00:00",
         "2018-01-18 00:00",
         "2017-06-01 00:00",
         "2017-03-02 00:00",
         "2016-03-25 00:00",
         "2015-06-03 00:00",
         "2015-01-15 00:00",
         "2012-09-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TimeSlotMask(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"


class E1Status(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("nos", 0),
          ("ais", 1),
          ("azs", 2),
          ("los", 3),
          ("rai", 4),
          ("prbserr", 5),
          ("testerr", 6),
          ("loopdet", 7),
          ("txlock", 8),
          ("codeerr", 9),
          ("fastpulseerr", 10),
          ("rarepulseerr", 11),
          ("mfaserr", 12),
          ("rcrc4err", 13),
          ("crc4err", 14),
          ("ok", 16))
    )


class CRC4Status(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("check", 0),
          ("send", 1),
          ("reicheck", 2),
          ("reisend", 3))
    )


# MIB Managed Objects in the order of their OIDs

_Emux_ObjectIdentity = ObjectIdentity
emux = _Emux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42926, 2)
)
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3)
)
_Basic_ObjectIdentity = ObjectIdentity
basic = _Basic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 1)
)
_SysHWVer_Type = DisplayString
_SysHWVer_Object = MibScalar
sysHWVer = _SysHWVer_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 1, 1),
    _SysHWVer_Type()
)
sysHWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHWVer.setStatus("current")
_SysOSVer_Type = DisplayString
_SysOSVer_Object = MibScalar
sysOSVer = _SysOSVer_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 1, 2),
    _SysOSVer_Type()
)
sysOSVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysOSVer.setStatus("current")
_HwDescr_Type = DisplayString
_HwDescr_Object = MibScalar
hwDescr = _HwDescr_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 1, 3),
    _HwDescr_Type()
)
hwDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDescr.setStatus("current")
_ManContact_Type = DisplayString
_ManContact_Object = MibScalar
manContact = _ManContact_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 1, 4),
    _ManContact_Type()
)
manContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manContact.setStatus("current")
_SysDevname_Type = DisplayString
_SysDevname_Object = MibScalar
sysDevname = _SysDevname_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 1, 5),
    _SysDevname_Type()
)
sysDevname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevname.setStatus("current")
_DevLocation_Type = DisplayString
_DevLocation_Object = MibScalar
devLocation = _DevLocation_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 1, 6),
    _DevLocation_Type()
)
devLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devLocation.setStatus("current")
_SysReset_Type = DisplayString
_SysReset_Object = MibScalar
sysReset = _SysReset_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 1, 7),
    _SysReset_Type()
)
sysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysReset.setStatus("current")
_SysID_Type = DisplayString
_SysID_Object = MibScalar
sysID = _SysID_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 1, 8),
    _SysID_Type()
)
sysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysID.setStatus("current")
_SysDateTime_Type = DisplayString
_SysDateTime_Object = MibScalar
sysDateTime = _SysDateTime_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 1, 9),
    _SysDateTime_Type()
)
sysDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDateTime.setStatus("current")


class _SysLicenseValid_Type(Integer32):
    """Custom type sysLicenseValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_SysLicenseValid_Type.__name__ = "Integer32"
_SysLicenseValid_Object = MibScalar
sysLicenseValid = _SysLicenseValid_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 1, 10),
    _SysLicenseValid_Type()
)
sysLicenseValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicenseValid.setStatus("current")
_SysSaveConfig_Type = DisplayString
_SysSaveConfig_Object = MibScalar
sysSaveConfig = _SysSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 1, 11),
    _SysSaveConfig_Type()
)
sysSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSaveConfig.setStatus("current")
_SysUpdate_Type = DisplayString
_SysUpdate_Object = MibScalar
sysUpdate = _SysUpdate_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 1, 12),
    _SysUpdate_Type()
)
sysUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysUpdate.setStatus("current")
_SysVendor_Type = DisplayString
_SysVendor_Object = MibScalar
sysVendor = _SysVendor_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 1, 13),
    _SysVendor_Type()
)
sysVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVendor.setStatus("current")
_OldSysID_Type = DisplayString
_OldSysID_Object = MibScalar
oldSysID = _OldSysID_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 1, 14),
    _OldSysID_Type()
)
oldSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oldSysID.setStatus("current")
_Muxip_ObjectIdentity = ObjectIdentity
muxip = _Muxip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2)
)
_Ipcurrent_ObjectIdentity = ObjectIdentity
ipcurrent = _Ipcurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 1)
)
_CNetIP_Type = IpAddress
_CNetIP_Object = MibScalar
cNetIP = _CNetIP_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 1, 1),
    _CNetIP_Type()
)
cNetIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNetIP.setStatus("current")
_CNetMask_Type = IpAddress
_CNetMask_Object = MibScalar
cNetMask = _CNetMask_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 1, 2),
    _CNetMask_Type()
)
cNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNetMask.setStatus("current")
_CNetGateway_Type = IpAddress
_CNetGateway_Object = MibScalar
cNetGateway = _CNetGateway_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 1, 3),
    _CNetGateway_Type()
)
cNetGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNetGateway.setStatus("current")
_CDefaultVlan_Type = Integer32
_CDefaultVlan_Object = MibScalar
cDefaultVlan = _CDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 1, 4),
    _CDefaultVlan_Type()
)
cDefaultVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDefaultVlan.setStatus("current")
_CDefaultVlanPri_Type = Integer32
_CDefaultVlanPri_Object = MibScalar
cDefaultVlanPri = _CDefaultVlanPri_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 1, 5),
    _CDefaultVlanPri_Type()
)
cDefaultVlanPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDefaultVlanPri.setStatus("current")


class _CNetTrustAll_Type(Integer32):
    """Custom type cNetTrustAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_CNetTrustAll_Type.__name__ = "Integer32"
_CNetTrustAll_Object = MibScalar
cNetTrustAll = _CNetTrustAll_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 1, 6),
    _CNetTrustAll_Type()
)
cNetTrustAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNetTrustAll.setStatus("current")


class _CNetTrustLocal_Type(Integer32):
    """Custom type cNetTrustLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_CNetTrustLocal_Type.__name__ = "Integer32"
_CNetTrustLocal_Object = MibScalar
cNetTrustLocal = _CNetTrustLocal_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 1, 7),
    _CNetTrustLocal_Type()
)
cNetTrustLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNetTrustLocal.setStatus("current")


class _CNetTrustUnkVlan_Type(Integer32):
    """Custom type cNetTrustUnkVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_CNetTrustUnkVlan_Type.__name__ = "Integer32"
_CNetTrustUnkVlan_Object = MibScalar
cNetTrustUnkVlan = _CNetTrustUnkVlan_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 1, 8),
    _CNetTrustUnkVlan_Type()
)
cNetTrustUnkVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNetTrustUnkVlan.setStatus("current")
_CDNS1_Type = IpAddress
_CDNS1_Object = MibScalar
cDNS1 = _CDNS1_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 1, 9),
    _CDNS1_Type()
)
cDNS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDNS1.setStatus("current")
_CPhysicalAddr_Type = MacAddress
_CPhysicalAddr_Object = MibScalar
cPhysicalAddr = _CPhysicalAddr_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 1, 10),
    _CPhysicalAddr_Type()
)
cPhysicalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPhysicalAddr.setStatus("current")
_CSecondaryMAC_Type = MacAddress
_CSecondaryMAC_Object = MibScalar
cSecondaryMAC = _CSecondaryMAC_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 1, 11),
    _CSecondaryMAC_Type()
)
cSecondaryMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSecondaryMAC.setStatus("current")
_Ipstored_ObjectIdentity = ObjectIdentity
ipstored = _Ipstored_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 2)
)
_SNetIP_Type = IpAddress
_SNetIP_Object = MibScalar
sNetIP = _SNetIP_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 2, 1),
    _SNetIP_Type()
)
sNetIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNetIP.setStatus("current")
_SNetMask_Type = IpAddress
_SNetMask_Object = MibScalar
sNetMask = _SNetMask_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 2, 2),
    _SNetMask_Type()
)
sNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNetMask.setStatus("current")
_SNetGateway_Type = IpAddress
_SNetGateway_Object = MibScalar
sNetGateway = _SNetGateway_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 2, 3),
    _SNetGateway_Type()
)
sNetGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNetGateway.setStatus("current")
_SDefaultVlan_Type = Integer32
_SDefaultVlan_Object = MibScalar
sDefaultVlan = _SDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 2, 4),
    _SDefaultVlan_Type()
)
sDefaultVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sDefaultVlan.setStatus("current")
_SDefaultVlanPri_Type = Integer32
_SDefaultVlanPri_Object = MibScalar
sDefaultVlanPri = _SDefaultVlanPri_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 2, 5),
    _SDefaultVlanPri_Type()
)
sDefaultVlanPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sDefaultVlanPri.setStatus("current")


class _SNetTrustAll_Type(Integer32):
    """Custom type sNetTrustAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_SNetTrustAll_Type.__name__ = "Integer32"
_SNetTrustAll_Object = MibScalar
sNetTrustAll = _SNetTrustAll_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 2, 6),
    _SNetTrustAll_Type()
)
sNetTrustAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNetTrustAll.setStatus("current")


class _SNetTrustLocal_Type(Integer32):
    """Custom type sNetTrustLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_SNetTrustLocal_Type.__name__ = "Integer32"
_SNetTrustLocal_Object = MibScalar
sNetTrustLocal = _SNetTrustLocal_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 2, 7),
    _SNetTrustLocal_Type()
)
sNetTrustLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNetTrustLocal.setStatus("current")


class _SNetTrustUnkVlan_Type(Integer32):
    """Custom type sNetTrustUnkVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_SNetTrustUnkVlan_Type.__name__ = "Integer32"
_SNetTrustUnkVlan_Object = MibScalar
sNetTrustUnkVlan = _SNetTrustUnkVlan_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 2, 8),
    _SNetTrustUnkVlan_Type()
)
sNetTrustUnkVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNetTrustUnkVlan.setStatus("current")
_SDNS1_Type = IpAddress
_SDNS1_Object = MibScalar
sDNS1 = _SDNS1_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 2, 9),
    _SDNS1_Type()
)
sDNS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sDNS1.setStatus("current")
_SPhysicalAddr_Type = MacAddress
_SPhysicalAddr_Object = MibScalar
sPhysicalAddr = _SPhysicalAddr_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 2, 10),
    _SPhysicalAddr_Type()
)
sPhysicalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPhysicalAddr.setStatus("current")
_SSecondaryMAC_Type = MacAddress
_SSecondaryMAC_Object = MibScalar
sSecondaryMAC = _SSecondaryMAC_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 2, 11),
    _SSecondaryMAC_Type()
)
sSecondaryMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSecondaryMAC.setStatus("current")
_HostsTable_Object = MibTable
hostsTable = _HostsTable_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 3)
)
if mibBuilder.loadTexts:
    hostsTable.setStatus("current")
_HostsTableEntry_Object = MibTableRow
hostsTableEntry = _HostsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 3, 1)
)
hostsTableEntry.setIndexNames(
    (0, "EMUX-MIB", "hostIndex"),
)
if mibBuilder.loadTexts:
    hostsTableEntry.setStatus("current")


class _HostIndex_Type(Integer32):
    """Custom type hostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_HostIndex_Type.__name__ = "Integer32"
_HostIndex_Object = MibTableColumn
hostIndex = _HostIndex_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 3, 1, 1),
    _HostIndex_Type()
)
hostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hostIndex.setStatus("current")
_HostNetwork_Type = IpAddress
_HostNetwork_Object = MibTableColumn
hostNetwork = _HostNetwork_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 3, 1, 2),
    _HostNetwork_Type()
)
hostNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostNetwork.setStatus("current")
_HostMask_Type = IpAddress
_HostMask_Object = MibTableColumn
hostMask = _HostMask_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 3, 2, 3, 1, 3),
    _HostMask_Type()
)
hostMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostMask.setStatus("current")
_E1_ObjectIdentity = ObjectIdentity
e1 = _E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18)
)
_E1Number_Type = Integer32
_E1Number_Object = MibScalar
e1Number = _E1Number_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 1),
    _E1Number_Type()
)
e1Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1Number.setStatus("current")
_E1ConfigTable_Object = MibTable
e1ConfigTable = _E1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6)
)
if mibBuilder.loadTexts:
    e1ConfigTable.setStatus("current")
_E1ConfigTableEntry_Object = MibTableRow
e1ConfigTableEntry = _E1ConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6, 1)
)
e1ConfigTableEntry.setIndexNames(
    (0, "EMUX-MIB", "e1ChIndex"),
)
if mibBuilder.loadTexts:
    e1ConfigTableEntry.setStatus("current")


class _E1ChIndex_Type(Integer32):
    """Custom type e1ChIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_E1ChIndex_Type.__name__ = "Integer32"
_E1ChIndex_Object = MibTableColumn
e1ChIndex = _E1ChIndex_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6, 1, 1),
    _E1ChIndex_Type()
)
e1ChIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e1ChIndex.setStatus("current")
_E1ChStatus_Type = DisplayString
_E1ChStatus_Object = MibTableColumn
e1ChStatus = _E1ChStatus_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6, 1, 2),
    _E1ChStatus_Type()
)
e1ChStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1ChStatus.setStatus("current")


class _E1ChLinkStatus_Type(Integer32):
    """Custom type e1ChLinkStatus based on Integer32"""
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


_E1ChLinkStatus_Type.__name__ = "Integer32"
_E1ChLinkStatus_Object = MibTableColumn
e1ChLinkStatus = _E1ChLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6, 1, 3),
    _E1ChLinkStatus_Type()
)
e1ChLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1ChLinkStatus.setStatus("current")


class _E1ChLinkEnable_Type(Integer32):
    """Custom type e1ChLinkEnable based on Integer32"""
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


_E1ChLinkEnable_Type.__name__ = "Integer32"
_E1ChLinkEnable_Object = MibTableColumn
e1ChLinkEnable = _E1ChLinkEnable_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6, 1, 4),
    _E1ChLinkEnable_Type()
)
e1ChLinkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1ChLinkEnable.setStatus("current")
_E1ChResetConfig_Type = DisplayString
_E1ChResetConfig_Object = MibTableColumn
e1ChResetConfig = _E1ChResetConfig_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6, 1, 5),
    _E1ChResetConfig_Type()
)
e1ChResetConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1ChResetConfig.setStatus("current")


class _E1LocalLoopback_Type(Integer32):
    """Custom type e1LocalLoopback based on Integer32"""
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


_E1LocalLoopback_Type.__name__ = "Integer32"
_E1LocalLoopback_Object = MibTableColumn
e1LocalLoopback = _E1LocalLoopback_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6, 1, 7),
    _E1LocalLoopback_Type()
)
e1LocalLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1LocalLoopback.setStatus("current")


class _E1RecvUnframed_Type(Integer32):
    """Custom type e1RecvUnframed based on Integer32"""
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


_E1RecvUnframed_Type.__name__ = "Integer32"
_E1RecvUnframed_Object = MibTableColumn
e1RecvUnframed = _E1RecvUnframed_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6, 1, 8),
    _E1RecvUnframed_Type()
)
e1RecvUnframed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1RecvUnframed.setStatus("current")


class _E1SendType_Type(Integer32):
    """Custom type e1SendType based on Integer32"""
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
        *(("ais", 0),
          ("azs", 1),
          ("prbs", 2),
          ("testFrames", 3),
          ("tdmop", 4))
    )


_E1SendType_Type.__name__ = "Integer32"
_E1SendType_Object = MibTableColumn
e1SendType = _E1SendType_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6, 1, 10),
    _E1SendType_Type()
)
e1SendType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1SendType.setStatus("current")


class _E1SyncSource_Type(Integer32):
    """Custom type e1SyncSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("restore", -1)
    )


_E1SyncSource_Type.__name__ = "Integer32"
_E1SyncSource_Object = MibTableColumn
e1SyncSource = _E1SyncSource_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6, 1, 11),
    _E1SyncSource_Type()
)
e1SyncSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1SyncSource.setStatus("current")
_E1TxSpeed_Type = Integer32
_E1TxSpeed_Object = MibTableColumn
e1TxSpeed = _E1TxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6, 1, 15),
    _E1TxSpeed_Type()
)
e1TxSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1TxSpeed.setStatus("current")
if mibBuilder.loadTexts:
    e1TxSpeed.setUnits("ppb")
_E1TestFrameRTT_Type = Gauge32
_E1TestFrameRTT_Object = MibTableColumn
e1TestFrameRTT = _E1TestFrameRTT_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6, 1, 16),
    _E1TestFrameRTT_Type()
)
e1TestFrameRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1TestFrameRTT.setStatus("current")
if mibBuilder.loadTexts:
    e1TestFrameRTT.setUnits("UI")
_E1RecvStatus_Type = E1Status
_E1RecvStatus_Object = MibTableColumn
e1RecvStatus = _E1RecvStatus_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6, 1, 17),
    _E1RecvStatus_Type()
)
e1RecvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1RecvStatus.setStatus("current")
_E1SendStatus_Type = E1Status
_E1SendStatus_Object = MibTableColumn
e1SendStatus = _E1SendStatus_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6, 1, 18),
    _E1SendStatus_Type()
)
e1SendStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1SendStatus.setStatus("current")
_E1RXSpeed_Type = Integer32
_E1RXSpeed_Object = MibTableColumn
e1RXSpeed = _E1RXSpeed_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6, 1, 21),
    _E1RXSpeed_Type()
)
e1RXSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1RXSpeed.setStatus("current")
if mibBuilder.loadTexts:
    e1RXSpeed.setUnits("ppb")


class _E1LongLine_Type(Integer32):
    """Custom type e1LongLine based on Integer32"""
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


_E1LongLine_Type.__name__ = "Integer32"
_E1LongLine_Object = MibTableColumn
e1LongLine = _E1LongLine_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6, 1, 22),
    _E1LongLine_Type()
)
e1LongLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1LongLine.setStatus("current")
_E1SignalLevel_Type = DisplayString
_E1SignalLevel_Object = MibTableColumn
e1SignalLevel = _E1SignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6, 1, 23),
    _E1SignalLevel_Type()
)
e1SignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1SignalLevel.setStatus("current")
_E1NoLogEvents_Type = E1Status
_E1NoLogEvents_Object = MibTableColumn
e1NoLogEvents = _E1NoLogEvents_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6, 1, 24),
    _E1NoLogEvents_Type()
)
e1NoLogEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1NoLogEvents.setStatus("current")
_E1CRC4_Type = CRC4Status
_E1CRC4_Object = MibTableColumn
e1CRC4 = _E1CRC4_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6, 1, 25),
    _E1CRC4_Type()
)
e1CRC4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CRC4.setStatus("current")


class _E1PRBSCheck_Type(Integer32):
    """Custom type e1PRBSCheck based on Integer32"""
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


_E1PRBSCheck_Type.__name__ = "Integer32"
_E1PRBSCheck_Object = MibTableColumn
e1PRBSCheck = _E1PRBSCheck_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 6, 1, 26),
    _E1PRBSCheck_Type()
)
e1PRBSCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1PRBSCheck.setStatus("current")
_TdmConfigTable_Object = MibTable
tdmConfigTable = _TdmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7)
)
if mibBuilder.loadTexts:
    tdmConfigTable.setStatus("current")
_TdmConfigTableEntry_Object = MibTableRow
tdmConfigTableEntry = _TdmConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1)
)
tdmConfigTableEntry.setIndexNames(
    (0, "EMUX-MIB", "tdmChIndex"),
)
if mibBuilder.loadTexts:
    tdmConfigTableEntry.setStatus("current")


class _TdmChIndex_Type(Integer32):
    """Custom type tdmChIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TdmChIndex_Type.__name__ = "Integer32"
_TdmChIndex_Object = MibTableColumn
tdmChIndex = _TdmChIndex_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 1),
    _TdmChIndex_Type()
)
tdmChIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmChIndex.setStatus("current")
_TdmStatus_Type = DisplayString
_TdmStatus_Object = MibTableColumn
tdmStatus = _TdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 2),
    _TdmStatus_Type()
)
tdmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmStatus.setStatus("current")


class _TdmLinkStatus_Type(Integer32):
    """Custom type tdmLinkStatus based on Integer32"""
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


_TdmLinkStatus_Type.__name__ = "Integer32"
_TdmLinkStatus_Object = MibTableColumn
tdmLinkStatus = _TdmLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 3),
    _TdmLinkStatus_Type()
)
tdmLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmLinkStatus.setStatus("current")


class _TdmAdminStatus_Type(Integer32):
    """Custom type tdmAdminStatus based on Integer32"""
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
        *(("listen", 0),
          ("connect", 1),
          ("blocked", 2),
          ("alwaysSend", 3))
    )


_TdmAdminStatus_Type.__name__ = "Integer32"
_TdmAdminStatus_Object = MibTableColumn
tdmAdminStatus = _TdmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 5),
    _TdmAdminStatus_Type()
)
tdmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmAdminStatus.setStatus("current")
_TdmResetConfig_Type = DisplayString
_TdmResetConfig_Object = MibTableColumn
tdmResetConfig = _TdmResetConfig_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 7),
    _TdmResetConfig_Type()
)
tdmResetConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmResetConfig.setStatus("current")
_TdmFrameSize_Type = Integer32
_TdmFrameSize_Object = MibTableColumn
tdmFrameSize = _TdmFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 8),
    _TdmFrameSize_Type()
)
tdmFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    tdmFrameSize.setUnits("1/2ms")
_TdmJBSize_Type = Integer32
_TdmJBSize_Object = MibTableColumn
tdmJBSize = _TdmJBSize_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 9),
    _TdmJBSize_Type()
)
tdmJBSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmJBSize.setStatus("current")
if mibBuilder.loadTexts:
    tdmJBSize.setUnits("ms")
_TdmCurrentTimeout_Type = Integer32
_TdmCurrentTimeout_Object = MibTableColumn
tdmCurrentTimeout = _TdmCurrentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 10),
    _TdmCurrentTimeout_Type()
)
tdmCurrentTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmCurrentTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tdmCurrentTimeout.setUnits("ms")


class _TdmMode_Type(Integer32):
    """Custom type tdmMode based on Integer32"""
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
        *(("down", 0),
          ("waitingSync", 1),
          ("accumulating", 2),
          ("working", 3))
    )


_TdmMode_Type.__name__ = "Integer32"
_TdmMode_Object = MibTableColumn
tdmMode = _TdmMode_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 11),
    _TdmMode_Type()
)
tdmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmMode.setStatus("current")


class _TdmHasData_Type(Integer32):
    """Custom type tdmHasData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("nodata", 2))
    )


_TdmHasData_Type.__name__ = "Integer32"
_TdmHasData_Object = MibTableColumn
tdmHasData = _TdmHasData_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 12),
    _TdmHasData_Type()
)
tdmHasData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmHasData.setStatus("current")
_TdmCurrentJBSize_Type = Integer32
_TdmCurrentJBSize_Object = MibTableColumn
tdmCurrentJBSize = _TdmCurrentJBSize_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 13),
    _TdmCurrentJBSize_Type()
)
tdmCurrentJBSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmCurrentJBSize.setStatus("current")
if mibBuilder.loadTexts:
    tdmCurrentJBSize.setUnits("us")
_TdmLocalTSMask_Type = TimeSlotMask
_TdmLocalTSMask_Object = MibTableColumn
tdmLocalTSMask = _TdmLocalTSMask_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 14),
    _TdmLocalTSMask_Type()
)
tdmLocalTSMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmLocalTSMask.setStatus("current")
_TdmRemoteTSMask_Type = TimeSlotMask
_TdmRemoteTSMask_Object = MibTableColumn
tdmRemoteTSMask = _TdmRemoteTSMask_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 15),
    _TdmRemoteTSMask_Type()
)
tdmRemoteTSMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmRemoteTSMask.setStatus("current")
_TdmVLANID_Type = Integer32
_TdmVLANID_Object = MibTableColumn
tdmVLANID = _TdmVLANID_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 16),
    _TdmVLANID_Type()
)
tdmVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmVLANID.setStatus("current")
_TdmVLANPri_Type = Integer32
_TdmVLANPri_Object = MibTableColumn
tdmVLANPri = _TdmVLANPri_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 17),
    _TdmVLANPri_Type()
)
tdmVLANPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmVLANPri.setStatus("current")


class _TdmUseIP_Type(Integer32):
    """Custom type tdmUseIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("use", 1),
          ("dontuse", 2))
    )


_TdmUseIP_Type.__name__ = "Integer32"
_TdmUseIP_Object = MibTableColumn
tdmUseIP = _TdmUseIP_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 18),
    _TdmUseIP_Type()
)
tdmUseIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmUseIP.setStatus("current")


class _TdmLostRequest_Type(Integer32):
    """Custom type tdmLostRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("request", 1),
          ("ignore", 2))
    )


_TdmLostRequest_Type.__name__ = "Integer32"
_TdmLostRequest_Object = MibTableColumn
tdmLostRequest = _TdmLostRequest_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 19),
    _TdmLostRequest_Type()
)
tdmLostRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmLostRequest.setStatus("current")
_TdmRedirectedIP_Type = IpAddress
_TdmRedirectedIP_Object = MibTableColumn
tdmRedirectedIP = _TdmRedirectedIP_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 20),
    _TdmRedirectedIP_Type()
)
tdmRedirectedIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmRedirectedIP.setStatus("current")
_TdmRedirectedMAC_Type = MacAddress
_TdmRedirectedMAC_Object = MibTableColumn
tdmRedirectedMAC = _TdmRedirectedMAC_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 21),
    _TdmRedirectedMAC_Type()
)
tdmRedirectedMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmRedirectedMAC.setStatus("current")
_TdmRedirectedChannel_Type = Integer32
_TdmRedirectedChannel_Object = MibTableColumn
tdmRedirectedChannel = _TdmRedirectedChannel_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 22),
    _TdmRedirectedChannel_Type()
)
tdmRedirectedChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmRedirectedChannel.setStatus("current")
_TdmOriginalIP_Type = IpAddress
_TdmOriginalIP_Object = MibTableColumn
tdmOriginalIP = _TdmOriginalIP_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 23),
    _TdmOriginalIP_Type()
)
tdmOriginalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmOriginalIP.setStatus("current")
_TdmOriginalMAC_Type = MacAddress
_TdmOriginalMAC_Object = MibTableColumn
tdmOriginalMAC = _TdmOriginalMAC_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 24),
    _TdmOriginalMAC_Type()
)
tdmOriginalMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmOriginalMAC.setStatus("current")
_TdmOriginalChannel_Type = Integer32
_TdmOriginalChannel_Object = MibTableColumn
tdmOriginalChannel = _TdmOriginalChannel_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 25),
    _TdmOriginalChannel_Type()
)
tdmOriginalChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmOriginalChannel.setStatus("current")


class _TdmRemoteLoop_Type(Integer32):
    """Custom type tdmRemoteLoop based on Integer32"""
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


_TdmRemoteLoop_Type.__name__ = "Integer32"
_TdmRemoteLoop_Object = MibTableColumn
tdmRemoteLoop = _TdmRemoteLoop_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 28),
    _TdmRemoteLoop_Type()
)
tdmRemoteLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmRemoteLoop.setStatus("current")
_TdmTos_Type = Integer32
_TdmTos_Object = MibTableColumn
tdmTos = _TdmTos_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 29),
    _TdmTos_Type()
)
tdmTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmTos.setStatus("current")
_TdmSpeedRegualator_Type = DisplayString
_TdmSpeedRegualator_Object = MibTableColumn
tdmSpeedRegualator = _TdmSpeedRegualator_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 30),
    _TdmSpeedRegualator_Type()
)
tdmSpeedRegualator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmSpeedRegualator.setStatus("current")
_TdmSpeed_Type = Integer32
_TdmSpeed_Object = MibTableColumn
tdmSpeed = _TdmSpeed_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 31),
    _TdmSpeed_Type()
)
tdmSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmSpeed.setStatus("current")
if mibBuilder.loadTexts:
    tdmSpeed.setUnits("ppb")


class _TdmConfigured_Type(Integer32):
    """Custom type tdmConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("notConfigured", 2))
    )


_TdmConfigured_Type.__name__ = "Integer32"
_TdmConfigured_Object = MibTableColumn
tdmConfigured = _TdmConfigured_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 32),
    _TdmConfigured_Type()
)
tdmConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmConfigured.setStatus("current")


class _TdmUseConstSpeed_Type(Integer32):
    """Custom type tdmUseConstSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("const", 1),
          ("restored", 2))
    )


_TdmUseConstSpeed_Type.__name__ = "Integer32"
_TdmUseConstSpeed_Object = MibTableColumn
tdmUseConstSpeed = _TdmUseConstSpeed_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 33),
    _TdmUseConstSpeed_Type()
)
tdmUseConstSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmUseConstSpeed.setStatus("current")
_TdmMaxTimeout_Type = Integer32
_TdmMaxTimeout_Object = MibTableColumn
tdmMaxTimeout = _TdmMaxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 34),
    _TdmMaxTimeout_Type()
)
tdmMaxTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmMaxTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tdmMaxTimeout.setUnits("ms")
_TdmUsedTimeSlots_Type = Integer32
_TdmUsedTimeSlots_Object = MibTableColumn
tdmUsedTimeSlots = _TdmUsedTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 35),
    _TdmUsedTimeSlots_Type()
)
tdmUsedTimeSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmUsedTimeSlots.setStatus("current")


class _TdmCompression_Type(Integer32):
    """Custom type tdmCompression based on Integer32"""
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


_TdmCompression_Type.__name__ = "Integer32"
_TdmCompression_Object = MibTableColumn
tdmCompression = _TdmCompression_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 36),
    _TdmCompression_Type()
)
tdmCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmCompression.setStatus("current")
_TdmKeyFrameInterval_Type = Integer32
_TdmKeyFrameInterval_Object = MibTableColumn
tdmKeyFrameInterval = _TdmKeyFrameInterval_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 37),
    _TdmKeyFrameInterval_Type()
)
tdmKeyFrameInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmKeyFrameInterval.setStatus("current")
_TdmDescription_Type = DisplayString
_TdmDescription_Object = MibTableColumn
tdmDescription = _TdmDescription_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 38),
    _TdmDescription_Type()
)
tdmDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmDescription.setStatus("current")
_TdmDoubleSend_Type = Integer32
_TdmDoubleSend_Object = MibTableColumn
tdmDoubleSend = _TdmDoubleSend_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 39),
    _TdmDoubleSend_Type()
)
tdmDoubleSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmDoubleSend.setStatus("current")
if mibBuilder.loadTexts:
    tdmDoubleSend.setUnits("frames")
_TdmConstSpeed_Type = Integer32
_TdmConstSpeed_Object = MibTableColumn
tdmConstSpeed = _TdmConstSpeed_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 40),
    _TdmConstSpeed_Type()
)
tdmConstSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmConstSpeed.setStatus("current")
if mibBuilder.loadTexts:
    tdmConstSpeed.setUnits("ppb")


class _TdmInterpMode_Type(Integer32):
    """Custom type tdmInterpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("prevdata", 0),
          ("ais", 1))
    )


_TdmInterpMode_Type.__name__ = "Integer32"
_TdmInterpMode_Object = MibTableColumn
tdmInterpMode = _TdmInterpMode_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 41),
    _TdmInterpMode_Type()
)
tdmInterpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmInterpMode.setStatus("current")


class _TdmProtocol_Type(Integer32):
    """Custom type tdmProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tdmop", 0),
          ("satop", 1),
          ("cesopsn", 2))
    )


_TdmProtocol_Type.__name__ = "Integer32"
_TdmProtocol_Object = MibTableColumn
tdmProtocol = _TdmProtocol_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 42),
    _TdmProtocol_Type()
)
tdmProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmProtocol.setStatus("current")
_TdmDSCP_Type = DisplayString
_TdmDSCP_Object = MibTableColumn
tdmDSCP = _TdmDSCP_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 7, 1, 43),
    _TdmDSCP_Type()
)
tdmDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmDSCP.setStatus("current")
_E1StatisticsTable_Object = MibTable
e1StatisticsTable = _E1StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8)
)
if mibBuilder.loadTexts:
    e1StatisticsTable.setStatus("current")
_E1StatisticsTableEntry_Object = MibTableRow
e1StatisticsTableEntry = _E1StatisticsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1)
)
e1StatisticsTableEntry.setIndexNames(
    (0, "EMUX-MIB", "e1StChIndex"),
)
if mibBuilder.loadTexts:
    e1StatisticsTableEntry.setStatus("current")


class _E1StChIndex_Type(Integer32):
    """Custom type e1StChIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_E1StChIndex_Type.__name__ = "Integer32"
_E1StChIndex_Object = MibTableColumn
e1StChIndex = _E1StChIndex_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 1),
    _E1StChIndex_Type()
)
e1StChIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e1StChIndex.setStatus("current")
_E1rxOkCnt_Type = Counter32
_E1rxOkCnt_Object = MibTableColumn
e1rxOkCnt = _E1rxOkCnt_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 2),
    _E1rxOkCnt_Type()
)
e1rxOkCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1rxOkCnt.setStatus("current")
if mibBuilder.loadTexts:
    e1rxOkCnt.setUnits("s")
_E1rxNOS_Type = Counter32
_E1rxNOS_Object = MibTableColumn
e1rxNOS = _E1rxNOS_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 3),
    _E1rxNOS_Type()
)
e1rxNOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1rxNOS.setStatus("current")
if mibBuilder.loadTexts:
    e1rxNOS.setUnits("s")
_E1rxAIS_Type = Counter32
_E1rxAIS_Object = MibTableColumn
e1rxAIS = _E1rxAIS_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 4),
    _E1rxAIS_Type()
)
e1rxAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1rxAIS.setStatus("current")
if mibBuilder.loadTexts:
    e1rxAIS.setUnits("s")
_E1rxAZS_Type = Counter32
_E1rxAZS_Object = MibTableColumn
e1rxAZS = _E1rxAZS_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 5),
    _E1rxAZS_Type()
)
e1rxAZS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1rxAZS.setStatus("current")
if mibBuilder.loadTexts:
    e1rxAZS.setUnits("s")
_E1rxLOS_Type = Counter32
_E1rxLOS_Object = MibTableColumn
e1rxLOS = _E1rxLOS_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 6),
    _E1rxLOS_Type()
)
e1rxLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1rxLOS.setStatus("current")
if mibBuilder.loadTexts:
    e1rxLOS.setUnits("s")
_E1rxRAI_Type = Counter32
_E1rxRAI_Object = MibTableColumn
e1rxRAI = _E1rxRAI_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 7),
    _E1rxRAI_Type()
)
e1rxRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1rxRAI.setStatus("current")
if mibBuilder.loadTexts:
    e1rxRAI.setUnits("s")
_E1rxPRBS_Type = Counter32
_E1rxPRBS_Object = MibTableColumn
e1rxPRBS = _E1rxPRBS_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 8),
    _E1rxPRBS_Type()
)
e1rxPRBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1rxPRBS.setStatus("current")
if mibBuilder.loadTexts:
    e1rxPRBS.setUnits("s")
_E1rxTest_Type = Counter32
_E1rxTest_Object = MibTableColumn
e1rxTest = _E1rxTest_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 9),
    _E1rxTest_Type()
)
e1rxTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1rxTest.setStatus("current")
if mibBuilder.loadTexts:
    e1rxTest.setUnits("s")
_E1rxCodeErr_Type = Counter32
_E1rxCodeErr_Object = MibTableColumn
e1rxCodeErr = _E1rxCodeErr_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 11),
    _E1rxCodeErr_Type()
)
e1rxCodeErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1rxCodeErr.setStatus("current")
if mibBuilder.loadTexts:
    e1rxCodeErr.setUnits("s")
_E1rxRareErr_Type = Counter32
_E1rxRareErr_Object = MibTableColumn
e1rxRareErr = _E1rxRareErr_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 12),
    _E1rxRareErr_Type()
)
e1rxRareErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1rxRareErr.setStatus("current")
if mibBuilder.loadTexts:
    e1rxRareErr.setUnits("s")
_E1rxFastErr_Type = Counter32
_E1rxFastErr_Object = MibTableColumn
e1rxFastErr = _E1rxFastErr_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 13),
    _E1rxFastErr_Type()
)
e1rxFastErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1rxFastErr.setStatus("current")
if mibBuilder.loadTexts:
    e1rxFastErr.setUnits("s")
_E1rxFDev_Type = Integer32
_E1rxFDev_Object = MibTableColumn
e1rxFDev = _E1rxFDev_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 14),
    _E1rxFDev_Type()
)
e1rxFDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1rxFDev.setStatus("current")
if mibBuilder.loadTexts:
    e1rxFDev.setUnits("ppb")
_E1rxCRC4_Type = Counter64
_E1rxCRC4_Object = MibTableColumn
e1rxCRC4 = _E1rxCRC4_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 15),
    _E1rxCRC4_Type()
)
e1rxCRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1rxCRC4.setStatus("current")
if mibBuilder.loadTexts:
    e1rxCRC4.setUnits("s")
_E1rxCRC4Sec_Type = Counter32
_E1rxCRC4Sec_Object = MibTableColumn
e1rxCRC4Sec = _E1rxCRC4Sec_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 16),
    _E1rxCRC4Sec_Type()
)
e1rxCRC4Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1rxCRC4Sec.setStatus("current")
if mibBuilder.loadTexts:
    e1rxCRC4Sec.setUnits("s")
_E1rxCRC4Rem_Type = Counter32
_E1rxCRC4Rem_Object = MibTableColumn
e1rxCRC4Rem = _E1rxCRC4Rem_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 17),
    _E1rxCRC4Rem_Type()
)
e1rxCRC4Rem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1rxCRC4Rem.setStatus("current")
if mibBuilder.loadTexts:
    e1rxCRC4Rem.setUnits("s")
_E1rxMfAS_Type = Counter32
_E1rxMfAS_Object = MibTableColumn
e1rxMfAS = _E1rxMfAS_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 18),
    _E1rxMfAS_Type()
)
e1rxMfAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1rxMfAS.setStatus("current")
if mibBuilder.loadTexts:
    e1rxMfAS.setUnits("s")
_E1txOkCnt_Type = Counter32
_E1txOkCnt_Object = MibTableColumn
e1txOkCnt = _E1txOkCnt_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 102),
    _E1txOkCnt_Type()
)
e1txOkCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1txOkCnt.setStatus("current")
if mibBuilder.loadTexts:
    e1txOkCnt.setUnits("s")
_E1txNOS_Type = Counter32
_E1txNOS_Object = MibTableColumn
e1txNOS = _E1txNOS_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 103),
    _E1txNOS_Type()
)
e1txNOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1txNOS.setStatus("current")
if mibBuilder.loadTexts:
    e1txNOS.setUnits("s")
_E1txAIS_Type = Counter32
_E1txAIS_Object = MibTableColumn
e1txAIS = _E1txAIS_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 104),
    _E1txAIS_Type()
)
e1txAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1txAIS.setStatus("current")
if mibBuilder.loadTexts:
    e1txAIS.setUnits("s")
_E1txAZS_Type = Counter32
_E1txAZS_Object = MibTableColumn
e1txAZS = _E1txAZS_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 105),
    _E1txAZS_Type()
)
e1txAZS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1txAZS.setStatus("current")
if mibBuilder.loadTexts:
    e1txAZS.setUnits("s")
_E1txLOS_Type = Counter32
_E1txLOS_Object = MibTableColumn
e1txLOS = _E1txLOS_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 106),
    _E1txLOS_Type()
)
e1txLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1txLOS.setStatus("current")
if mibBuilder.loadTexts:
    e1txLOS.setUnits("s")
_E1txRAI_Type = Counter32
_E1txRAI_Object = MibTableColumn
e1txRAI = _E1txRAI_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 107),
    _E1txRAI_Type()
)
e1txRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1txRAI.setStatus("current")
if mibBuilder.loadTexts:
    e1txRAI.setUnits("s")
_E1txPRBS_Type = Counter32
_E1txPRBS_Object = MibTableColumn
e1txPRBS = _E1txPRBS_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 108),
    _E1txPRBS_Type()
)
e1txPRBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1txPRBS.setStatus("current")
if mibBuilder.loadTexts:
    e1txPRBS.setUnits("s")
_E1txLock_Type = Counter32
_E1txLock_Object = MibTableColumn
e1txLock = _E1txLock_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 112),
    _E1txLock_Type()
)
e1txLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1txLock.setStatus("current")
if mibBuilder.loadTexts:
    e1txLock.setUnits("s")
_E1Start_Type = DateAndTime
_E1Start_Object = MibTableColumn
e1Start = _E1Start_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 113),
    _E1Start_Type()
)
e1Start.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1Start.setStatus("current")
_E1Finish_Type = DateAndTime
_E1Finish_Object = MibTableColumn
e1Finish = _E1Finish_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 114),
    _E1Finish_Type()
)
e1Finish.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1Finish.setStatus("current")
_E1Total_Type = Counter32
_E1Total_Object = MibTableColumn
e1Total = _E1Total_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 115),
    _E1Total_Type()
)
e1Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1Total.setStatus("current")
if mibBuilder.loadTexts:
    e1Total.setUnits("s")
_E1txFDev_Type = Integer32
_E1txFDev_Object = MibTableColumn
e1txFDev = _E1txFDev_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 116),
    _E1txFDev_Type()
)
e1txFDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1txFDev.setStatus("current")
if mibBuilder.loadTexts:
    e1txFDev.setUnits("ppb")
_E1txCRC4Sec_Type = Counter32
_E1txCRC4Sec_Object = MibTableColumn
e1txCRC4Sec = _E1txCRC4Sec_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 117),
    _E1txCRC4Sec_Type()
)
e1txCRC4Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1txCRC4Sec.setStatus("current")
if mibBuilder.loadTexts:
    e1txCRC4Sec.setUnits("s")
_E1txCRC4Rem_Type = Counter32
_E1txCRC4Rem_Object = MibTableColumn
e1txCRC4Rem = _E1txCRC4Rem_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 118),
    _E1txCRC4Rem_Type()
)
e1txCRC4Rem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1txCRC4Rem.setStatus("current")
if mibBuilder.loadTexts:
    e1txCRC4Rem.setUnits("s")
_E1txMfAS_Type = Counter32
_E1txMfAS_Object = MibTableColumn
e1txMfAS = _E1txMfAS_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 8, 1, 119),
    _E1txMfAS_Type()
)
e1txMfAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1txMfAS.setStatus("current")
if mibBuilder.loadTexts:
    e1txMfAS.setUnits("s")
_TdmStatisticsTable_Object = MibTable
tdmStatisticsTable = _TdmStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9)
)
if mibBuilder.loadTexts:
    tdmStatisticsTable.setStatus("current")
_TdmStatisticsTableEntry_Object = MibTableRow
tdmStatisticsTableEntry = _TdmStatisticsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1)
)
tdmStatisticsTableEntry.setIndexNames(
    (0, "EMUX-MIB", "tdmStChIndex"),
)
if mibBuilder.loadTexts:
    tdmStatisticsTableEntry.setStatus("current")


class _TdmStChIndex_Type(Integer32):
    """Custom type tdmStChIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TdmStChIndex_Type.__name__ = "Integer32"
_TdmStChIndex_Object = MibTableColumn
tdmStChIndex = _TdmStChIndex_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 1),
    _TdmStChIndex_Type()
)
tdmStChIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmStChIndex.setStatus("current")
_TdmResend_Type = Counter32
_TdmResend_Object = MibTableColumn
tdmResend = _TdmResend_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 2),
    _TdmResend_Type()
)
tdmResend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmResend.setStatus("current")
if mibBuilder.loadTexts:
    tdmResend.setUnits("frames")
_TdmLost_Type = Counter32
_TdmLost_Object = MibTableColumn
tdmLost = _TdmLost_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 3),
    _TdmLost_Type()
)
tdmLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmLost.setStatus("current")
if mibBuilder.loadTexts:
    tdmLost.setUnits("frames")
_TdmOvf_Type = Counter32
_TdmOvf_Object = MibTableColumn
tdmOvf = _TdmOvf_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 4),
    _TdmOvf_Type()
)
tdmOvf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmOvf.setStatus("current")
if mibBuilder.loadTexts:
    tdmOvf.setUnits("times")
_TdmUndf_Type = Counter32
_TdmUndf_Object = MibTableColumn
tdmUndf = _TdmUndf_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 5),
    _TdmUndf_Type()
)
tdmUndf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmUndf.setStatus("current")
if mibBuilder.loadTexts:
    tdmUndf.setUnits("Times")
_TdmIgnored_Type = Counter32
_TdmIgnored_Object = MibTableColumn
tdmIgnored = _TdmIgnored_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 6),
    _TdmIgnored_Type()
)
tdmIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmIgnored.setStatus("current")
if mibBuilder.loadTexts:
    tdmIgnored.setUnits("frames")
_TdmInterp_Type = Counter32
_TdmInterp_Object = MibTableColumn
tdmInterp = _TdmInterp_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 7),
    _TdmInterp_Type()
)
tdmInterp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmInterp.setStatus("current")
if mibBuilder.loadTexts:
    tdmInterp.setUnits("125us")
_TdmResync_Type = Counter32
_TdmResync_Object = MibTableColumn
tdmResync = _TdmResync_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 8),
    _TdmResync_Type()
)
tdmResync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmResync.setStatus("current")
if mibBuilder.loadTexts:
    tdmResync.setUnits("times")
_TdmValid_Type = Counter32
_TdmValid_Object = MibTableColumn
tdmValid = _TdmValid_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 9),
    _TdmValid_Type()
)
tdmValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmValid.setStatus("current")
if mibBuilder.loadTexts:
    tdmValid.setUnits("frames")
_TdmSlipAdd_Type = Counter32
_TdmSlipAdd_Object = MibTableColumn
tdmSlipAdd = _TdmSlipAdd_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 10),
    _TdmSlipAdd_Type()
)
tdmSlipAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmSlipAdd.setStatus("current")
if mibBuilder.loadTexts:
    tdmSlipAdd.setUnits("times")
_TdmSlipRem_Type = Counter32
_TdmSlipRem_Object = MibTableColumn
tdmSlipRem = _TdmSlipRem_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 11),
    _TdmSlipRem_Type()
)
tdmSlipRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmSlipRem.setStatus("current")
if mibBuilder.loadTexts:
    tdmSlipRem.setUnits("times")
_TdmLostReq_Type = Counter32
_TdmLostReq_Object = MibTableColumn
tdmLostReq = _TdmLostReq_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 12),
    _TdmLostReq_Type()
)
tdmLostReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmLostReq.setStatus("current")
if mibBuilder.loadTexts:
    tdmLostReq.setUnits("frames")
_TdmRestored_Type = Counter32
_TdmRestored_Object = MibTableColumn
tdmRestored = _TdmRestored_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 13),
    _TdmRestored_Type()
)
tdmRestored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmRestored.setStatus("current")
if mibBuilder.loadTexts:
    tdmRestored.setUnits("frames")
_TdmStart_Type = DateAndTime
_TdmStart_Object = MibTableColumn
tdmStart = _TdmStart_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 14),
    _TdmStart_Type()
)
tdmStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmStart.setStatus("current")
_TdmFinish_Type = DateAndTime
_TdmFinish_Object = MibTableColumn
tdmFinish = _TdmFinish_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 15),
    _TdmFinish_Type()
)
tdmFinish.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmFinish.setStatus("current")
_TdmAvgSpeed_Type = Integer32
_TdmAvgSpeed_Object = MibTableColumn
tdmAvgSpeed = _TdmAvgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 16),
    _TdmAvgSpeed_Type()
)
tdmAvgSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmAvgSpeed.setStatus("current")
if mibBuilder.loadTexts:
    tdmAvgSpeed.setUnits("ppb")
_TdmAvgJB_Type = Integer32
_TdmAvgJB_Object = MibTableColumn
tdmAvgJB = _TdmAvgJB_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 17),
    _TdmAvgJB_Type()
)
tdmAvgJB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmAvgJB.setStatus("current")
if mibBuilder.loadTexts:
    tdmAvgJB.setUnits("us")
_TdmMinJB_Type = Integer32
_TdmMinJB_Object = MibTableColumn
tdmMinJB = _TdmMinJB_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 18),
    _TdmMinJB_Type()
)
tdmMinJB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmMinJB.setStatus("current")
if mibBuilder.loadTexts:
    tdmMinJB.setUnits("ms")
_TdmMaxJB_Type = Integer32
_TdmMaxJB_Object = MibTableColumn
tdmMaxJB = _TdmMaxJB_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 19),
    _TdmMaxJB_Type()
)
tdmMaxJB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmMaxJB.setStatus("current")
if mibBuilder.loadTexts:
    tdmMaxJB.setUnits("ms")
_TdmRecommenedJB_Type = Integer32
_TdmRecommenedJB_Object = MibTableColumn
tdmRecommenedJB = _TdmRecommenedJB_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 20),
    _TdmRecommenedJB_Type()
)
tdmRecommenedJB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmRecommenedJB.setStatus("current")
if mibBuilder.loadTexts:
    tdmRecommenedJB.setUnits("ms")
_TdmFatal_Type = Counter32
_TdmFatal_Object = MibTableColumn
tdmFatal = _TdmFatal_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 21),
    _TdmFatal_Type()
)
tdmFatal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmFatal.setStatus("current")
if mibBuilder.loadTexts:
    tdmFatal.setUnits("frames")
_TdmTxDiscards_Type = Counter32
_TdmTxDiscards_Object = MibTableColumn
tdmTxDiscards = _TdmTxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 22),
    _TdmTxDiscards_Type()
)
tdmTxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmTxDiscards.setStatus("current")
if mibBuilder.loadTexts:
    tdmTxDiscards.setUnits("frames")
_TdmBandwidth_Type = Integer32
_TdmBandwidth_Object = MibTableColumn
tdmBandwidth = _TdmBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 9, 1, 23),
    _TdmBandwidth_Type()
)
tdmBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    tdmBandwidth.setUnits("kbps")
_E1traps_ObjectIdentity = ObjectIdentity
e1traps = _E1traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 10)
)
_E1trapsPrefix_ObjectIdentity = ObjectIdentity
e1trapsPrefix = _E1trapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 10, 0)
)
_TdmRedundancyTable_Object = MibTable
tdmRedundancyTable = _TdmRedundancyTable_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 11)
)
if mibBuilder.loadTexts:
    tdmRedundancyTable.setStatus("current")
_TdmRedundancyTableEntry_Object = MibTableRow
tdmRedundancyTableEntry = _TdmRedundancyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 11, 1)
)
tdmRedundancyTableEntry.setIndexNames(
    (0, "EMUX-MIB", "tdmRedundancyIndex"),
)
if mibBuilder.loadTexts:
    tdmRedundancyTableEntry.setStatus("current")


class _TdmRedundancyIndex_Type(Integer32):
    """Custom type tdmRedundancyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TdmRedundancyIndex_Type.__name__ = "Integer32"
_TdmRedundancyIndex_Object = MibTableColumn
tdmRedundancyIndex = _TdmRedundancyIndex_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 11, 1, 1),
    _TdmRedundancyIndex_Type()
)
tdmRedundancyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmRedundancyIndex.setStatus("current")


class _TdmRedundancyEnabled_Type(Integer32):
    """Custom type tdmRedundancyEnabled based on Integer32"""
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


_TdmRedundancyEnabled_Type.__name__ = "Integer32"
_TdmRedundancyEnabled_Object = MibTableColumn
tdmRedundancyEnabled = _TdmRedundancyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 11, 1, 2),
    _TdmRedundancyEnabled_Type()
)
tdmRedundancyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmRedundancyEnabled.setStatus("current")
_TdmRedundancyRemoteIP_Type = IpAddress
_TdmRedundancyRemoteIP_Object = MibTableColumn
tdmRedundancyRemoteIP = _TdmRedundancyRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 11, 1, 3),
    _TdmRedundancyRemoteIP_Type()
)
tdmRedundancyRemoteIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmRedundancyRemoteIP.setStatus("current")
_TdmRedundancyVLANID_Type = Integer32
_TdmRedundancyVLANID_Object = MibTableColumn
tdmRedundancyVLANID = _TdmRedundancyVLANID_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 11, 1, 4),
    _TdmRedundancyVLANID_Type()
)
tdmRedundancyVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmRedundancyVLANID.setStatus("current")
_TdmRedundancyDSCP_Type = DisplayString
_TdmRedundancyDSCP_Object = MibTableColumn
tdmRedundancyDSCP = _TdmRedundancyDSCP_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 11, 1, 5),
    _TdmRedundancyDSCP_Type()
)
tdmRedundancyDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmRedundancyDSCP.setStatus("current")


class _TdmRedundancyUseIP_Type(Integer32):
    """Custom type tdmRedundancyUseIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("use", 1),
          ("dontuse", 2))
    )


_TdmRedundancyUseIP_Type.__name__ = "Integer32"
_TdmRedundancyUseIP_Object = MibTableColumn
tdmRedundancyUseIP = _TdmRedundancyUseIP_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 11, 1, 6),
    _TdmRedundancyUseIP_Type()
)
tdmRedundancyUseIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmRedundancyUseIP.setStatus("current")
_TdmRedundancyVLANPri_Type = Integer32
_TdmRedundancyVLANPri_Object = MibTableColumn
tdmRedundancyVLANPri = _TdmRedundancyVLANPri_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 11, 1, 7),
    _TdmRedundancyVLANPri_Type()
)
tdmRedundancyVLANPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmRedundancyVLANPri.setStatus("current")
_Eth_ObjectIdentity = ObjectIdentity
eth = _Eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42926, 2, 19)
)
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 19, 3)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanTableEntry_Object = MibTableRow
vlanTableEntry = _VlanTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 19, 3, 1)
)
vlanTableEntry.setIndexNames(
    (0, "EMUX-MIB", "vlanID"),
)
if mibBuilder.loadTexts:
    vlanTableEntry.setStatus("current")


class _VlanID_Type(Integer32):
    """Custom type vlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VlanID_Type.__name__ = "Integer32"
_VlanID_Object = MibTableColumn
vlanID = _VlanID_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 19, 3, 1, 1),
    _VlanID_Type()
)
vlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanID.setStatus("current")
_Adc_ObjectIdentity = ObjectIdentity
adc = _Adc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42926, 2, 21)
)
_AdcTable_Object = MibTable
adcTable = _AdcTable_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 21, 1)
)
if mibBuilder.loadTexts:
    adcTable.setStatus("current")
_AdcTableEntry_Object = MibTableRow
adcTableEntry = _AdcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 21, 1, 1)
)
adcTableEntry.setIndexNames(
    (0, "EMUX-MIB", "adcIndex"),
)
if mibBuilder.loadTexts:
    adcTableEntry.setStatus("current")


class _AdcIndex_Type(Integer32):
    """Custom type adcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AdcIndex_Type.__name__ = "Integer32"
_AdcIndex_Object = MibTableColumn
adcIndex = _AdcIndex_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 21, 1, 1, 1),
    _AdcIndex_Type()
)
adcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adcIndex.setStatus("current")
_AdcName_Type = DisplayString
_AdcName_Object = MibTableColumn
adcName = _AdcName_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 21, 1, 1, 2),
    _AdcName_Type()
)
adcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adcName.setStatus("current")
_AdcValue_Type = Float
_AdcValue_Object = MibTableColumn
adcValue = _AdcValue_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 21, 1, 1, 3),
    _AdcValue_Type()
)
adcValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adcValue.setStatus("current")
_AdcType_Type = DisplayString
_AdcType_Object = MibTableColumn
adcType = _AdcType_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 21, 1, 1, 4),
    _AdcType_Type()
)
adcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adcType.setStatus("current")


class _AdcState_Type(Integer32):
    """Custom type adcState based on Integer32"""
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
        *(("normal", 0),
          ("errHigh", 1),
          ("errLow", 2),
          ("warnHigh", 3),
          ("warnLow", 4),
          ("down", 5))
    )


_AdcState_Type.__name__ = "Integer32"
_AdcState_Object = MibTableColumn
adcState = _AdcState_Object(
    (1, 3, 6, 1, 4, 1, 42926, 2, 21, 1, 1, 5),
    _AdcState_Type()
)
adcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adcState.setStatus("current")
_DyingGaspNotifications_ObjectIdentity = ObjectIdentity
dyingGaspNotifications = _DyingGaspNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42926, 2, 22)
)
_DyingGaspTraps_ObjectIdentity = ObjectIdentity
dyingGaspTraps = _DyingGaspTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42926, 2, 22, 0)
)
_MuxConformance_ObjectIdentity = ObjectIdentity
muxConformance = _MuxConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42926, 2, 30)
)
_MuxGroups_ObjectIdentity = ObjectIdentity
muxGroups = _MuxGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42926, 2, 30, 1)
)
_MuxCompliances_ObjectIdentity = ObjectIdentity
muxCompliances = _MuxCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42926, 2, 30, 2)
)

# Managed Objects groups

muxBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42926, 2, 30, 1, 1)
)
muxBaseGroup.setObjects(
      *(("EMUX-MIB", "sysHWVer"),
        ("EMUX-MIB", "sysOSVer"),
        ("EMUX-MIB", "hwDescr"),
        ("EMUX-MIB", "manContact"),
        ("EMUX-MIB", "sysDevname"),
        ("EMUX-MIB", "devLocation"),
        ("EMUX-MIB", "sysReset"),
        ("EMUX-MIB", "sysID"),
        ("EMUX-MIB", "sysDateTime"),
        ("EMUX-MIB", "sysLicenseValid"),
        ("EMUX-MIB", "sysSaveConfig"),
        ("EMUX-MIB", "sysUpdate"),
        ("EMUX-MIB", "sysVendor"),
        ("EMUX-MIB", "oldSysID"))
)
if mibBuilder.loadTexts:
    muxBaseGroup.setStatus("current")

e1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42926, 2, 30, 1, 2)
)
e1Group.setObjects(
      *(("EMUX-MIB", "e1Number"),
        ("EMUX-MIB", "e1ChStatus"),
        ("EMUX-MIB", "e1ChLinkStatus"),
        ("EMUX-MIB", "e1ChLinkEnable"),
        ("EMUX-MIB", "e1ChResetConfig"),
        ("EMUX-MIB", "e1LocalLoopback"),
        ("EMUX-MIB", "e1RecvUnframed"),
        ("EMUX-MIB", "e1SendType"),
        ("EMUX-MIB", "e1SyncSource"),
        ("EMUX-MIB", "e1TxSpeed"),
        ("EMUX-MIB", "e1TestFrameRTT"),
        ("EMUX-MIB", "e1RecvStatus"),
        ("EMUX-MIB", "e1SendStatus"),
        ("EMUX-MIB", "e1RXSpeed"),
        ("EMUX-MIB", "e1LongLine"),
        ("EMUX-MIB", "e1SignalLevel"),
        ("EMUX-MIB", "e1NoLogEvents"),
        ("EMUX-MIB", "e1CRC4"),
        ("EMUX-MIB", "e1PRBSCheck"))
)
if mibBuilder.loadTexts:
    e1Group.setStatus("current")

tdmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42926, 2, 30, 1, 3)
)
tdmGroup.setObjects(
      *(("EMUX-MIB", "tdmStatus"),
        ("EMUX-MIB", "tdmLinkStatus"),
        ("EMUX-MIB", "tdmAdminStatus"),
        ("EMUX-MIB", "tdmResetConfig"),
        ("EMUX-MIB", "tdmFrameSize"),
        ("EMUX-MIB", "tdmJBSize"),
        ("EMUX-MIB", "tdmCurrentTimeout"),
        ("EMUX-MIB", "tdmMode"),
        ("EMUX-MIB", "tdmHasData"),
        ("EMUX-MIB", "tdmCurrentJBSize"),
        ("EMUX-MIB", "tdmLocalTSMask"),
        ("EMUX-MIB", "tdmRemoteTSMask"),
        ("EMUX-MIB", "tdmVLANID"),
        ("EMUX-MIB", "tdmVLANPri"),
        ("EMUX-MIB", "tdmUseIP"),
        ("EMUX-MIB", "tdmLostRequest"),
        ("EMUX-MIB", "tdmRedirectedIP"),
        ("EMUX-MIB", "tdmRedirectedMAC"),
        ("EMUX-MIB", "tdmRedirectedChannel"),
        ("EMUX-MIB", "tdmOriginalIP"),
        ("EMUX-MIB", "tdmOriginalMAC"),
        ("EMUX-MIB", "tdmOriginalChannel"),
        ("EMUX-MIB", "tdmRemoteLoop"),
        ("EMUX-MIB", "tdmTos"),
        ("EMUX-MIB", "tdmSpeedRegualator"),
        ("EMUX-MIB", "tdmSpeed"),
        ("EMUX-MIB", "tdmConfigured"),
        ("EMUX-MIB", "tdmUseConstSpeed"),
        ("EMUX-MIB", "tdmMaxTimeout"),
        ("EMUX-MIB", "tdmUsedTimeSlots"),
        ("EMUX-MIB", "tdmCompression"),
        ("EMUX-MIB", "tdmKeyFrameInterval"),
        ("EMUX-MIB", "tdmDescription"),
        ("EMUX-MIB", "tdmDoubleSend"),
        ("EMUX-MIB", "tdmConstSpeed"),
        ("EMUX-MIB", "tdmInterpMode"),
        ("EMUX-MIB", "tdmProtocol"),
        ("EMUX-MIB", "tdmDSCP"))
)
if mibBuilder.loadTexts:
    tdmGroup.setStatus("current")

e1GroupStat = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42926, 2, 30, 1, 4)
)
e1GroupStat.setObjects(
      *(("EMUX-MIB", "e1rxOkCnt"),
        ("EMUX-MIB", "e1rxNOS"),
        ("EMUX-MIB", "e1rxAIS"),
        ("EMUX-MIB", "e1rxAZS"),
        ("EMUX-MIB", "e1rxLOS"),
        ("EMUX-MIB", "e1rxRAI"),
        ("EMUX-MIB", "e1rxPRBS"),
        ("EMUX-MIB", "e1rxTest"),
        ("EMUX-MIB", "e1rxCodeErr"),
        ("EMUX-MIB", "e1rxRareErr"),
        ("EMUX-MIB", "e1rxFastErr"),
        ("EMUX-MIB", "e1rxFDev"),
        ("EMUX-MIB", "e1rxCRC4"),
        ("EMUX-MIB", "e1rxCRC4Sec"),
        ("EMUX-MIB", "e1rxCRC4Rem"),
        ("EMUX-MIB", "e1rxMfAS"),
        ("EMUX-MIB", "e1txOkCnt"),
        ("EMUX-MIB", "e1txNOS"),
        ("EMUX-MIB", "e1txAIS"),
        ("EMUX-MIB", "e1txAZS"),
        ("EMUX-MIB", "e1txLOS"),
        ("EMUX-MIB", "e1txRAI"),
        ("EMUX-MIB", "e1txPRBS"),
        ("EMUX-MIB", "e1txLock"),
        ("EMUX-MIB", "e1Start"),
        ("EMUX-MIB", "e1Finish"),
        ("EMUX-MIB", "e1Total"),
        ("EMUX-MIB", "e1txFDev"),
        ("EMUX-MIB", "e1txCRC4Sec"),
        ("EMUX-MIB", "e1txCRC4Rem"),
        ("EMUX-MIB", "e1txMfAS"))
)
if mibBuilder.loadTexts:
    e1GroupStat.setStatus("current")

tdmGroupStat = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42926, 2, 30, 1, 5)
)
tdmGroupStat.setObjects(
      *(("EMUX-MIB", "tdmResend"),
        ("EMUX-MIB", "tdmLost"),
        ("EMUX-MIB", "tdmOvf"),
        ("EMUX-MIB", "tdmUndf"),
        ("EMUX-MIB", "tdmIgnored"),
        ("EMUX-MIB", "tdmInterp"),
        ("EMUX-MIB", "tdmResync"),
        ("EMUX-MIB", "tdmValid"),
        ("EMUX-MIB", "tdmSlipAdd"),
        ("EMUX-MIB", "tdmSlipRem"),
        ("EMUX-MIB", "tdmLostReq"),
        ("EMUX-MIB", "tdmRestored"),
        ("EMUX-MIB", "tdmStart"),
        ("EMUX-MIB", "tdmFinish"),
        ("EMUX-MIB", "tdmAvgSpeed"),
        ("EMUX-MIB", "tdmAvgJB"),
        ("EMUX-MIB", "tdmMinJB"),
        ("EMUX-MIB", "tdmMaxJB"),
        ("EMUX-MIB", "tdmRecommenedJB"),
        ("EMUX-MIB", "tdmFatal"),
        ("EMUX-MIB", "tdmTxDiscards"),
        ("EMUX-MIB", "tdmBandwidth"))
)
if mibBuilder.loadTexts:
    tdmGroupStat.setStatus("current")

vlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42926, 2, 30, 1, 6)
)
vlanGroup.setObjects(
    ("EMUX-MIB", "vlanID")
)
if mibBuilder.loadTexts:
    vlanGroup.setStatus("current")

ipcurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42926, 2, 30, 1, 7)
)
ipcurrentGroup.setObjects(
      *(("EMUX-MIB", "cNetIP"),
        ("EMUX-MIB", "cNetMask"),
        ("EMUX-MIB", "cNetGateway"),
        ("EMUX-MIB", "cDefaultVlan"),
        ("EMUX-MIB", "cDefaultVlanPri"),
        ("EMUX-MIB", "cNetTrustAll"),
        ("EMUX-MIB", "cNetTrustLocal"),
        ("EMUX-MIB", "cNetTrustUnkVlan"),
        ("EMUX-MIB", "cDNS1"),
        ("EMUX-MIB", "cPhysicalAddr"),
        ("EMUX-MIB", "cSecondaryMAC"))
)
if mibBuilder.loadTexts:
    ipcurrentGroup.setStatus("current")

ipstoredGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42926, 2, 30, 1, 8)
)
ipstoredGroup.setObjects(
      *(("EMUX-MIB", "sNetIP"),
        ("EMUX-MIB", "sNetMask"),
        ("EMUX-MIB", "sNetGateway"),
        ("EMUX-MIB", "sDefaultVlan"),
        ("EMUX-MIB", "sDefaultVlanPri"),
        ("EMUX-MIB", "sNetTrustAll"),
        ("EMUX-MIB", "sNetTrustLocal"),
        ("EMUX-MIB", "sNetTrustUnkVlan"),
        ("EMUX-MIB", "sDNS1"),
        ("EMUX-MIB", "sPhysicalAddr"),
        ("EMUX-MIB", "sSecondaryMAC"))
)
if mibBuilder.loadTexts:
    ipstoredGroup.setStatus("current")

hostsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42926, 2, 30, 1, 9)
)
hostsGroup.setObjects(
      *(("EMUX-MIB", "hostNetwork"),
        ("EMUX-MIB", "hostMask"))
)
if mibBuilder.loadTexts:
    hostsGroup.setStatus("current")

adcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42926, 2, 30, 1, 10)
)
adcGroup.setObjects(
      *(("EMUX-MIB", "adcName"),
        ("EMUX-MIB", "adcValue"),
        ("EMUX-MIB", "adcType"),
        ("EMUX-MIB", "adcState"))
)
if mibBuilder.loadTexts:
    adcGroup.setStatus("current")

tdmRedundancyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42926, 2, 30, 1, 13)
)
tdmRedundancyGroup.setObjects(
      *(("EMUX-MIB", "tdmRedundancyEnabled"),
        ("EMUX-MIB", "tdmRedundancyRemoteIP"),
        ("EMUX-MIB", "tdmRedundancyVLANID"),
        ("EMUX-MIB", "tdmRedundancyDSCP"),
        ("EMUX-MIB", "tdmRedundancyUseIP"),
        ("EMUX-MIB", "tdmRedundancyVLANPri"))
)
if mibBuilder.loadTexts:
    tdmRedundancyGroup.setStatus("current")


# Notification objects

e1LinkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 10, 0, 1)
)
e1LinkChange.setObjects(
      *(("EMUX-MIB", "e1RecvStatus"),
        ("EMUX-MIB", "e1SendStatus"))
)
if mibBuilder.loadTexts:
    e1LinkChange.setStatus(
        "current"
    )

tdmLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 10, 0, 2)
)
tdmLinkDown.setObjects(
      *(("EMUX-MIB", "tdmAdminStatus"),
        ("EMUX-MIB", "tdmLinkStatus"))
)
if mibBuilder.loadTexts:
    tdmLinkDown.setStatus(
        "current"
    )

tdmLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 42926, 2, 18, 10, 0, 3)
)
tdmLinkUp.setObjects(
      *(("EMUX-MIB", "tdmAdminStatus"),
        ("EMUX-MIB", "tdmLinkStatus"))
)
if mibBuilder.loadTexts:
    tdmLinkUp.setStatus(
        "current"
    )

dyingGaspTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42926, 2, 22, 0, 1)
)
if mibBuilder.loadTexts:
    dyingGaspTrap.setStatus(
        "current"
    )


# Notifications groups

e1trapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 42926, 2, 30, 1, 11)
)
e1trapsGroup.setObjects(
      *(("EMUX-MIB", "e1LinkChange"),
        ("EMUX-MIB", "tdmLinkDown"),
        ("EMUX-MIB", "tdmLinkUp"))
)
if mibBuilder.loadTexts:
    e1trapsGroup.setStatus(
        "current"
    )

dyingGaspTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 42926, 2, 30, 1, 12)
)
dyingGaspTrapsGroup.setObjects(
    ("EMUX-MIB", "dyingGaspTrap")
)
if mibBuilder.loadTexts:
    dyingGaspTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

emuxCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 42926, 2, 30, 2, 1)
)
emuxCompliance.setObjects(
      *(("EMUX-MIB", "muxBaseGroup"),
        ("EMUX-MIB", "e1Group"),
        ("EMUX-MIB", "tdmGroup"),
        ("EMUX-MIB", "e1GroupStat"),
        ("EMUX-MIB", "tdmGroupStat"),
        ("EMUX-MIB", "e1trapsGroup"),
        ("EMUX-MIB", "vlanGroup"),
        ("EMUX-MIB", "ipcurrentGroup"),
        ("EMUX-MIB", "ipstoredGroup"),
        ("EMUX-MIB", "hostsGroup"),
        ("EMUX-MIB", "adcGroup"),
        ("EMUX-MIB", "tdmRedundancyGroup"),
        ("EMUX-MIB", "dyingGaspTrapsGroup"))
)
if mibBuilder.loadTexts:
    emuxCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EMUX-MIB",
    **{"TimeSlotMask": TimeSlotMask,
       "E1Status": E1Status,
       "CRC4Status": CRC4Status,
       "nsc": nsc,
       "emux": emux,
       "general": general,
       "basic": basic,
       "sysHWVer": sysHWVer,
       "sysOSVer": sysOSVer,
       "hwDescr": hwDescr,
       "manContact": manContact,
       "sysDevname": sysDevname,
       "devLocation": devLocation,
       "sysReset": sysReset,
       "sysID": sysID,
       "sysDateTime": sysDateTime,
       "sysLicenseValid": sysLicenseValid,
       "sysSaveConfig": sysSaveConfig,
       "sysUpdate": sysUpdate,
       "sysVendor": sysVendor,
       "oldSysID": oldSysID,
       "muxip": muxip,
       "ipcurrent": ipcurrent,
       "cNetIP": cNetIP,
       "cNetMask": cNetMask,
       "cNetGateway": cNetGateway,
       "cDefaultVlan": cDefaultVlan,
       "cDefaultVlanPri": cDefaultVlanPri,
       "cNetTrustAll": cNetTrustAll,
       "cNetTrustLocal": cNetTrustLocal,
       "cNetTrustUnkVlan": cNetTrustUnkVlan,
       "cDNS1": cDNS1,
       "cPhysicalAddr": cPhysicalAddr,
       "cSecondaryMAC": cSecondaryMAC,
       "ipstored": ipstored,
       "sNetIP": sNetIP,
       "sNetMask": sNetMask,
       "sNetGateway": sNetGateway,
       "sDefaultVlan": sDefaultVlan,
       "sDefaultVlanPri": sDefaultVlanPri,
       "sNetTrustAll": sNetTrustAll,
       "sNetTrustLocal": sNetTrustLocal,
       "sNetTrustUnkVlan": sNetTrustUnkVlan,
       "sDNS1": sDNS1,
       "sPhysicalAddr": sPhysicalAddr,
       "sSecondaryMAC": sSecondaryMAC,
       "hostsTable": hostsTable,
       "hostsTableEntry": hostsTableEntry,
       "hostIndex": hostIndex,
       "hostNetwork": hostNetwork,
       "hostMask": hostMask,
       "e1": e1,
       "e1Number": e1Number,
       "e1ConfigTable": e1ConfigTable,
       "e1ConfigTableEntry": e1ConfigTableEntry,
       "e1ChIndex": e1ChIndex,
       "e1ChStatus": e1ChStatus,
       "e1ChLinkStatus": e1ChLinkStatus,
       "e1ChLinkEnable": e1ChLinkEnable,
       "e1ChResetConfig": e1ChResetConfig,
       "e1LocalLoopback": e1LocalLoopback,
       "e1RecvUnframed": e1RecvUnframed,
       "e1SendType": e1SendType,
       "e1SyncSource": e1SyncSource,
       "e1TxSpeed": e1TxSpeed,
       "e1TestFrameRTT": e1TestFrameRTT,
       "e1RecvStatus": e1RecvStatus,
       "e1SendStatus": e1SendStatus,
       "e1RXSpeed": e1RXSpeed,
       "e1LongLine": e1LongLine,
       "e1SignalLevel": e1SignalLevel,
       "e1NoLogEvents": e1NoLogEvents,
       "e1CRC4": e1CRC4,
       "e1PRBSCheck": e1PRBSCheck,
       "tdmConfigTable": tdmConfigTable,
       "tdmConfigTableEntry": tdmConfigTableEntry,
       "tdmChIndex": tdmChIndex,
       "tdmStatus": tdmStatus,
       "tdmLinkStatus": tdmLinkStatus,
       "tdmAdminStatus": tdmAdminStatus,
       "tdmResetConfig": tdmResetConfig,
       "tdmFrameSize": tdmFrameSize,
       "tdmJBSize": tdmJBSize,
       "tdmCurrentTimeout": tdmCurrentTimeout,
       "tdmMode": tdmMode,
       "tdmHasData": tdmHasData,
       "tdmCurrentJBSize": tdmCurrentJBSize,
       "tdmLocalTSMask": tdmLocalTSMask,
       "tdmRemoteTSMask": tdmRemoteTSMask,
       "tdmVLANID": tdmVLANID,
       "tdmVLANPri": tdmVLANPri,
       "tdmUseIP": tdmUseIP,
       "tdmLostRequest": tdmLostRequest,
       "tdmRedirectedIP": tdmRedirectedIP,
       "tdmRedirectedMAC": tdmRedirectedMAC,
       "tdmRedirectedChannel": tdmRedirectedChannel,
       "tdmOriginalIP": tdmOriginalIP,
       "tdmOriginalMAC": tdmOriginalMAC,
       "tdmOriginalChannel": tdmOriginalChannel,
       "tdmRemoteLoop": tdmRemoteLoop,
       "tdmTos": tdmTos,
       "tdmSpeedRegualator": tdmSpeedRegualator,
       "tdmSpeed": tdmSpeed,
       "tdmConfigured": tdmConfigured,
       "tdmUseConstSpeed": tdmUseConstSpeed,
       "tdmMaxTimeout": tdmMaxTimeout,
       "tdmUsedTimeSlots": tdmUsedTimeSlots,
       "tdmCompression": tdmCompression,
       "tdmKeyFrameInterval": tdmKeyFrameInterval,
       "tdmDescription": tdmDescription,
       "tdmDoubleSend": tdmDoubleSend,
       "tdmConstSpeed": tdmConstSpeed,
       "tdmInterpMode": tdmInterpMode,
       "tdmProtocol": tdmProtocol,
       "tdmDSCP": tdmDSCP,
       "e1StatisticsTable": e1StatisticsTable,
       "e1StatisticsTableEntry": e1StatisticsTableEntry,
       "e1StChIndex": e1StChIndex,
       "e1rxOkCnt": e1rxOkCnt,
       "e1rxNOS": e1rxNOS,
       "e1rxAIS": e1rxAIS,
       "e1rxAZS": e1rxAZS,
       "e1rxLOS": e1rxLOS,
       "e1rxRAI": e1rxRAI,
       "e1rxPRBS": e1rxPRBS,
       "e1rxTest": e1rxTest,
       "e1rxCodeErr": e1rxCodeErr,
       "e1rxRareErr": e1rxRareErr,
       "e1rxFastErr": e1rxFastErr,
       "e1rxFDev": e1rxFDev,
       "e1rxCRC4": e1rxCRC4,
       "e1rxCRC4Sec": e1rxCRC4Sec,
       "e1rxCRC4Rem": e1rxCRC4Rem,
       "e1rxMfAS": e1rxMfAS,
       "e1txOkCnt": e1txOkCnt,
       "e1txNOS": e1txNOS,
       "e1txAIS": e1txAIS,
       "e1txAZS": e1txAZS,
       "e1txLOS": e1txLOS,
       "e1txRAI": e1txRAI,
       "e1txPRBS": e1txPRBS,
       "e1txLock": e1txLock,
       "e1Start": e1Start,
       "e1Finish": e1Finish,
       "e1Total": e1Total,
       "e1txFDev": e1txFDev,
       "e1txCRC4Sec": e1txCRC4Sec,
       "e1txCRC4Rem": e1txCRC4Rem,
       "e1txMfAS": e1txMfAS,
       "tdmStatisticsTable": tdmStatisticsTable,
       "tdmStatisticsTableEntry": tdmStatisticsTableEntry,
       "tdmStChIndex": tdmStChIndex,
       "tdmResend": tdmResend,
       "tdmLost": tdmLost,
       "tdmOvf": tdmOvf,
       "tdmUndf": tdmUndf,
       "tdmIgnored": tdmIgnored,
       "tdmInterp": tdmInterp,
       "tdmResync": tdmResync,
       "tdmValid": tdmValid,
       "tdmSlipAdd": tdmSlipAdd,
       "tdmSlipRem": tdmSlipRem,
       "tdmLostReq": tdmLostReq,
       "tdmRestored": tdmRestored,
       "tdmStart": tdmStart,
       "tdmFinish": tdmFinish,
       "tdmAvgSpeed": tdmAvgSpeed,
       "tdmAvgJB": tdmAvgJB,
       "tdmMinJB": tdmMinJB,
       "tdmMaxJB": tdmMaxJB,
       "tdmRecommenedJB": tdmRecommenedJB,
       "tdmFatal": tdmFatal,
       "tdmTxDiscards": tdmTxDiscards,
       "tdmBandwidth": tdmBandwidth,
       "e1traps": e1traps,
       "e1trapsPrefix": e1trapsPrefix,
       "e1LinkChange": e1LinkChange,
       "tdmLinkDown": tdmLinkDown,
       "tdmLinkUp": tdmLinkUp,
       "tdmRedundancyTable": tdmRedundancyTable,
       "tdmRedundancyTableEntry": tdmRedundancyTableEntry,
       "tdmRedundancyIndex": tdmRedundancyIndex,
       "tdmRedundancyEnabled": tdmRedundancyEnabled,
       "tdmRedundancyRemoteIP": tdmRedundancyRemoteIP,
       "tdmRedundancyVLANID": tdmRedundancyVLANID,
       "tdmRedundancyDSCP": tdmRedundancyDSCP,
       "tdmRedundancyUseIP": tdmRedundancyUseIP,
       "tdmRedundancyVLANPri": tdmRedundancyVLANPri,
       "eth": eth,
       "vlanTable": vlanTable,
       "vlanTableEntry": vlanTableEntry,
       "vlanID": vlanID,
       "adc": adc,
       "adcTable": adcTable,
       "adcTableEntry": adcTableEntry,
       "adcIndex": adcIndex,
       "adcName": adcName,
       "adcValue": adcValue,
       "adcType": adcType,
       "adcState": adcState,
       "dyingGaspNotifications": dyingGaspNotifications,
       "dyingGaspTraps": dyingGaspTraps,
       "dyingGaspTrap": dyingGaspTrap,
       "muxConformance": muxConformance,
       "muxGroups": muxGroups,
       "muxBaseGroup": muxBaseGroup,
       "e1Group": e1Group,
       "tdmGroup": tdmGroup,
       "e1GroupStat": e1GroupStat,
       "tdmGroupStat": tdmGroupStat,
       "vlanGroup": vlanGroup,
       "ipcurrentGroup": ipcurrentGroup,
       "ipstoredGroup": ipstoredGroup,
       "hostsGroup": hostsGroup,
       "adcGroup": adcGroup,
       "e1trapsGroup": e1trapsGroup,
       "dyingGaspTrapsGroup": dyingGaspTrapsGroup,
       "tdmRedundancyGroup": tdmRedundancyGroup,
       "muxCompliances": muxCompliances,
       "emuxCompliance": emuxCompliance}
)

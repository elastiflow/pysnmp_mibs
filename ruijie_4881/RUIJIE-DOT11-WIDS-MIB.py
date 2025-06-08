# SNMP MIB module (RUIJIE-DOT11-WIDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-DOT11-WIDS-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:21 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieDot11WIDSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62)
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSMIB.setRevisions(
        ("2009-04-15 09:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieDot11WIDSTraps_ObjectIdentity = ObjectIdentity
ruijieDot11WIDSTraps = _RuijieDot11WIDSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 0)
)
_RuijieDot11WIDSConfigObjects_ObjectIdentity = ObjectIdentity
ruijieDot11WIDSConfigObjects = _RuijieDot11WIDSConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1)
)
_RuijieDot11WIDSPermitVendorTable_Object = MibTable
ruijieDot11WIDSPermitVendorTable = _RuijieDot11WIDSPermitVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSPermitVendorTable.setStatus("current")
_RuijieDot11WIDSPermitVendorEntry_Object = MibTableRow
ruijieDot11WIDSPermitVendorEntry = _RuijieDot11WIDSPermitVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 1, 1)
)
ruijieDot11WIDSPermitVendorEntry.setIndexNames(
    (0, "RUIJIE-DOT11-WIDS-MIB", "ruijieDot11VendorOUI"),
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSPermitVendorEntry.setStatus("current")
_RuijieDot11VendorOUI_Type = Integer32
_RuijieDot11VendorOUI_Object = MibTableColumn
ruijieDot11VendorOUI = _RuijieDot11VendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 1, 1, 1),
    _RuijieDot11VendorOUI_Type()
)
ruijieDot11VendorOUI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDot11VendorOUI.setStatus("current")
_RuijieDot11VendorOper_Type = Integer32
_RuijieDot11VendorOper_Object = MibTableColumn
ruijieDot11VendorOper = _RuijieDot11VendorOper_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 1, 1, 2),
    _RuijieDot11VendorOper_Type()
)
ruijieDot11VendorOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11VendorOper.setStatus("current")
_RuijieDot11VendorName_Type = MacAddress
_RuijieDot11VendorName_Object = MibTableColumn
ruijieDot11VendorName = _RuijieDot11VendorName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 1, 1, 3),
    _RuijieDot11VendorName_Type()
)
ruijieDot11VendorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11VendorName.setStatus("current")
_RuijieDot11WIDSPermitSSIDTable_Object = MibTable
ruijieDot11WIDSPermitSSIDTable = _RuijieDot11WIDSPermitSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSPermitSSIDTable.setStatus("current")
_RuijieDot11WIDSPermitSSIDEntry_Object = MibTableRow
ruijieDot11WIDSPermitSSIDEntry = _RuijieDot11WIDSPermitSSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 2, 1)
)
ruijieDot11WIDSPermitSSIDEntry.setIndexNames(
    (0, "RUIJIE-DOT11-WIDS-MIB", "ruijieDot11PermitNum"),
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSPermitSSIDEntry.setStatus("current")
_RuijieDot11PermitNum_Type = Integer32
_RuijieDot11PermitNum_Object = MibTableColumn
ruijieDot11PermitNum = _RuijieDot11PermitNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 2, 1, 1),
    _RuijieDot11PermitNum_Type()
)
ruijieDot11PermitNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDot11PermitNum.setStatus("current")
_RuijieDot11PermitOper_Type = Integer32
_RuijieDot11PermitOper_Object = MibTableColumn
ruijieDot11PermitOper = _RuijieDot11PermitOper_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 2, 1, 2),
    _RuijieDot11PermitOper_Type()
)
ruijieDot11PermitOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11PermitOper.setStatus("current")


class _RuijieDot11PermitSSID_Type(DisplayString):
    """Custom type ruijieDot11PermitSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieDot11PermitSSID_Type.__name__ = "DisplayString"
_RuijieDot11PermitSSID_Object = MibTableColumn
ruijieDot11PermitSSID = _RuijieDot11PermitSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 2, 1, 3),
    _RuijieDot11PermitSSID_Type()
)
ruijieDot11PermitSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11PermitSSID.setStatus("current")
_RuijieDot11WIDSDeviceAttackMacaddressListTable_Object = MibTable
ruijieDot11WIDSDeviceAttackMacaddressListTable = _RuijieDot11WIDSDeviceAttackMacaddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSDeviceAttackMacaddressListTable.setStatus("current")
_RuijieDot11WIDSDeviceAttackMacaddressListEntry_Object = MibTableRow
ruijieDot11WIDSDeviceAttackMacaddressListEntry = _RuijieDot11WIDSDeviceAttackMacaddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 3, 1)
)
ruijieDot11WIDSDeviceAttackMacaddressListEntry.setIndexNames(
    (0, "RUIJIE-DOT11-WIDS-MIB", "ruijieDot11AttackNum"),
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSDeviceAttackMacaddressListEntry.setStatus("current")
_RuijieDot11AttackNum_Type = Integer32
_RuijieDot11AttackNum_Object = MibTableColumn
ruijieDot11AttackNum = _RuijieDot11AttackNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 3, 1, 1),
    _RuijieDot11AttackNum_Type()
)
ruijieDot11AttackNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDot11AttackNum.setStatus("current")
_RuijieDot11AttackOper_Type = Integer32
_RuijieDot11AttackOper_Object = MibTableColumn
ruijieDot11AttackOper = _RuijieDot11AttackOper_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 3, 1, 2),
    _RuijieDot11AttackOper_Type()
)
ruijieDot11AttackOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11AttackOper.setStatus("current")
_RuijieDot11AttackMAC_Type = MacAddress
_RuijieDot11AttackMAC_Object = MibTableColumn
ruijieDot11AttackMAC = _RuijieDot11AttackMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 3, 1, 3),
    _RuijieDot11AttackMAC_Type()
)
ruijieDot11AttackMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11AttackMAC.setStatus("current")


class _RuijieDot11AttackInfo_Type(DisplayString):
    """Custom type ruijieDot11AttackInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieDot11AttackInfo_Type.__name__ = "DisplayString"
_RuijieDot11AttackInfo_Object = MibTableColumn
ruijieDot11AttackInfo = _RuijieDot11AttackInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 3, 1, 4),
    _RuijieDot11AttackInfo_Type()
)
ruijieDot11AttackInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11AttackInfo.setStatus("current")
_RuijieDot11WIDSDevicePermitMacaddressListTable_Object = MibTable
ruijieDot11WIDSDevicePermitMacaddressListTable = _RuijieDot11WIDSDevicePermitMacaddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSDevicePermitMacaddressListTable.setStatus("current")
_RuijieDot11WIDSDevicePermitMacaddressListEntry_Object = MibTableRow
ruijieDot11WIDSDevicePermitMacaddressListEntry = _RuijieDot11WIDSDevicePermitMacaddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 4, 1)
)
ruijieDot11WIDSDevicePermitMacaddressListEntry.setIndexNames(
    (0, "RUIJIE-DOT11-WIDS-MIB", "ruijieDot11PermitMACNum"),
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSDevicePermitMacaddressListEntry.setStatus("current")
_RuijieDot11PermitMACNum_Type = Integer32
_RuijieDot11PermitMACNum_Object = MibTableColumn
ruijieDot11PermitMACNum = _RuijieDot11PermitMACNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 4, 1, 1),
    _RuijieDot11PermitMACNum_Type()
)
ruijieDot11PermitMACNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDot11PermitMACNum.setStatus("current")
_RuijieDot11PermitMACOper_Type = Integer32
_RuijieDot11PermitMACOper_Object = MibTableColumn
ruijieDot11PermitMACOper = _RuijieDot11PermitMACOper_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 4, 1, 2),
    _RuijieDot11PermitMACOper_Type()
)
ruijieDot11PermitMACOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11PermitMACOper.setStatus("current")
_RuijieDot11PermitMACAddr_Type = MacAddress
_RuijieDot11PermitMACAddr_Object = MibTableColumn
ruijieDot11PermitMACAddr = _RuijieDot11PermitMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 4, 1, 3),
    _RuijieDot11PermitMACAddr_Type()
)
ruijieDot11PermitMACAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11PermitMACAddr.setStatus("current")
_RuijieDot11WIDSDeviceagingDuration_Type = Integer32
_RuijieDot11WIDSDeviceagingDuration_Object = MibScalar
ruijieDot11WIDSDeviceagingDuration = _RuijieDot11WIDSDeviceagingDuration_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 5),
    _RuijieDot11WIDSDeviceagingDuration_Type()
)
ruijieDot11WIDSDeviceagingDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSDeviceagingDuration.setStatus("current")
_RuijieDot11WIDSCountermeasuresMode_Type = Integer32
_RuijieDot11WIDSCountermeasuresMode_Object = MibScalar
ruijieDot11WIDSCountermeasuresMode = _RuijieDot11WIDSCountermeasuresMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 6),
    _RuijieDot11WIDSCountermeasuresMode_Type()
)
ruijieDot11WIDSCountermeasuresMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSCountermeasuresMode.setStatus("current")
_RuijieDot11WIDSCountermeasureSet_Type = Integer32
_RuijieDot11WIDSCountermeasureSet_Object = MibScalar
ruijieDot11WIDSCountermeasureSet = _RuijieDot11WIDSCountermeasureSet_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 7),
    _RuijieDot11WIDSCountermeasureSet_Type()
)
ruijieDot11WIDSCountermeasureSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSCountermeasureSet.setStatus("current")
_RuijieDot11WIDSModeTable_Object = MibTable
ruijieDot11WIDSModeTable = _RuijieDot11WIDSModeTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 8)
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSModeTable.setStatus("current")
_RuijieDot11WIDSModeEntry_Object = MibTableRow
ruijieDot11WIDSModeEntry = _RuijieDot11WIDSModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 8, 1)
)
ruijieDot11WIDSModeEntry.setIndexNames(
    (0, "RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSAPID"),
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSModeEntry.setStatus("current")
_RuijieDot11WIDSAPID_Type = Integer32
_RuijieDot11WIDSAPID_Object = MibTableColumn
ruijieDot11WIDSAPID = _RuijieDot11WIDSAPID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 8, 1, 1),
    _RuijieDot11WIDSAPID_Type()
)
ruijieDot11WIDSAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDot11WIDSAPID.setStatus("current")
_RuijieDot11WIDSDeviceMode_Type = Integer32
_RuijieDot11WIDSDeviceMode_Object = MibTableColumn
ruijieDot11WIDSDeviceMode = _RuijieDot11WIDSDeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 8, 1, 2),
    _RuijieDot11WIDSDeviceMode_Type()
)
ruijieDot11WIDSDeviceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSDeviceMode.setStatus("current")
_RuijieDot11WIDSWhitelistMacaddressListTable_Object = MibTable
ruijieDot11WIDSWhitelistMacaddressListTable = _RuijieDot11WIDSWhitelistMacaddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 9)
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSWhitelistMacaddressListTable.setStatus("current")
_RuijieDot11WIDSWhitelistMacaddressListEntry_Object = MibTableRow
ruijieDot11WIDSWhitelistMacaddressListEntry = _RuijieDot11WIDSWhitelistMacaddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 9, 1)
)
ruijieDot11WIDSWhitelistMacaddressListEntry.setIndexNames(
    (0, "RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WhitelistNum"),
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSWhitelistMacaddressListEntry.setStatus("current")
_RuijieDot11WhitelistNum_Type = Integer32
_RuijieDot11WhitelistNum_Object = MibTableColumn
ruijieDot11WhitelistNum = _RuijieDot11WhitelistNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 9, 1, 1),
    _RuijieDot11WhitelistNum_Type()
)
ruijieDot11WhitelistNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDot11WhitelistNum.setStatus("current")
_RuijieDot11WhitelistOper_Type = Integer32
_RuijieDot11WhitelistOper_Object = MibTableColumn
ruijieDot11WhitelistOper = _RuijieDot11WhitelistOper_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 9, 1, 2),
    _RuijieDot11WhitelistOper_Type()
)
ruijieDot11WhitelistOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WhitelistOper.setStatus("current")
_RuijieDot11WhitelistMAC_Type = MacAddress
_RuijieDot11WhitelistMAC_Object = MibTableColumn
ruijieDot11WhitelistMAC = _RuijieDot11WhitelistMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 9, 1, 3),
    _RuijieDot11WhitelistMAC_Type()
)
ruijieDot11WhitelistMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WhitelistMAC.setStatus("current")
_RuijieDot11WIDSStaticblackListTable_Object = MibTable
ruijieDot11WIDSStaticblackListTable = _RuijieDot11WIDSStaticblackListTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 10)
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSStaticblackListTable.setStatus("current")
_RuijieDot11WIDSStaticblackListEntry_Object = MibTableRow
ruijieDot11WIDSStaticblackListEntry = _RuijieDot11WIDSStaticblackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 10, 1)
)
ruijieDot11WIDSStaticblackListEntry.setIndexNames(
    (0, "RUIJIE-DOT11-WIDS-MIB", "ruijieDot11StaticblacklistNum"),
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSStaticblackListEntry.setStatus("current")
_RuijieDot11StaticblacklistNum_Type = Integer32
_RuijieDot11StaticblacklistNum_Object = MibTableColumn
ruijieDot11StaticblacklistNum = _RuijieDot11StaticblacklistNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 10, 1, 1),
    _RuijieDot11StaticblacklistNum_Type()
)
ruijieDot11StaticblacklistNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDot11StaticblacklistNum.setStatus("current")
_RuijieDot11StaticblacklistOper_Type = Integer32
_RuijieDot11StaticblacklistOper_Object = MibTableColumn
ruijieDot11StaticblacklistOper = _RuijieDot11StaticblacklistOper_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 10, 1, 2),
    _RuijieDot11StaticblacklistOper_Type()
)
ruijieDot11StaticblacklistOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11StaticblacklistOper.setStatus("current")
_RuijieDot11StaticblacklistMAC_Type = MacAddress
_RuijieDot11StaticblacklistMAC_Object = MibTableColumn
ruijieDot11StaticblacklistMAC = _RuijieDot11StaticblacklistMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 10, 1, 3),
    _RuijieDot11StaticblacklistMAC_Type()
)
ruijieDot11StaticblacklistMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11StaticblacklistMAC.setStatus("current")
_RuijieDot11WIDSDynamicblacklistEnable_Type = TruthValue
_RuijieDot11WIDSDynamicblacklistEnable_Object = MibScalar
ruijieDot11WIDSDynamicblacklistEnable = _RuijieDot11WIDSDynamicblacklistEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 11),
    _RuijieDot11WIDSDynamicblacklistEnable_Type()
)
ruijieDot11WIDSDynamicblacklistEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSDynamicblacklistEnable.setStatus("current")
_RuijieDot11WIDSDynamicblacklistLifetime_Type = Integer32
_RuijieDot11WIDSDynamicblacklistLifetime_Object = MibScalar
ruijieDot11WIDSDynamicblacklistLifetime = _RuijieDot11WIDSDynamicblacklistLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 12),
    _RuijieDot11WIDSDynamicblacklistLifetime_Type()
)
ruijieDot11WIDSDynamicblacklistLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSDynamicblacklistLifetime.setStatus("current")
_RuijieDot11WIDSAttackDetectionMode_Type = Integer32
_RuijieDot11WIDSAttackDetectionMode_Object = MibScalar
ruijieDot11WIDSAttackDetectionMode = _RuijieDot11WIDSAttackDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 13),
    _RuijieDot11WIDSAttackDetectionMode_Type()
)
ruijieDot11WIDSAttackDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSAttackDetectionMode.setStatus("current")
_RuijieDot11WIDSRogueInfoTable_Object = MibTable
ruijieDot11WIDSRogueInfoTable = _RuijieDot11WIDSRogueInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 14)
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSRogueInfoTable.setStatus("current")
_RuijieDot11WIDSRogueInfoEntry_Object = MibTableRow
ruijieDot11WIDSRogueInfoEntry = _RuijieDot11WIDSRogueInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 14, 1)
)
ruijieDot11WIDSRogueInfoEntry.setIndexNames(
    (0, "RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSRogueInfoNUM"),
    (0, "RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSRogueInfoTYPE"),
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSRogueInfoEntry.setStatus("current")
_RuijieDot11WIDSRogueInfoNUM_Type = Integer32
_RuijieDot11WIDSRogueInfoNUM_Object = MibTableColumn
ruijieDot11WIDSRogueInfoNUM = _RuijieDot11WIDSRogueInfoNUM_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 14, 1, 1),
    _RuijieDot11WIDSRogueInfoNUM_Type()
)
ruijieDot11WIDSRogueInfoNUM.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDot11WIDSRogueInfoNUM.setStatus("current")
_RuijieDot11WIDSRogueInfoTYPE_Type = Integer32
_RuijieDot11WIDSRogueInfoTYPE_Object = MibTableColumn
ruijieDot11WIDSRogueInfoTYPE = _RuijieDot11WIDSRogueInfoTYPE_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 14, 1, 2),
    _RuijieDot11WIDSRogueInfoTYPE_Type()
)
ruijieDot11WIDSRogueInfoTYPE.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDot11WIDSRogueInfoTYPE.setStatus("current")
_RuijieDot11WIDSRogueInfoOper_Type = Integer32
_RuijieDot11WIDSRogueInfoOper_Object = MibTableColumn
ruijieDot11WIDSRogueInfoOper = _RuijieDot11WIDSRogueInfoOper_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 14, 1, 3),
    _RuijieDot11WIDSRogueInfoOper_Type()
)
ruijieDot11WIDSRogueInfoOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSRogueInfoOper.setStatus("current")
_RuijieDot11WIDSRogueInfoMAC_Type = MacAddress
_RuijieDot11WIDSRogueInfoMAC_Object = MibTableColumn
ruijieDot11WIDSRogueInfoMAC = _RuijieDot11WIDSRogueInfoMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 14, 1, 4),
    _RuijieDot11WIDSRogueInfoMAC_Type()
)
ruijieDot11WIDSRogueInfoMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSRogueInfoMAC.setStatus("current")
_RuijieDot11WIDSRogueInfoString_Type = DisplayString
_RuijieDot11WIDSRogueInfoString_Object = MibTableColumn
ruijieDot11WIDSRogueInfoString = _RuijieDot11WIDSRogueInfoString_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 14, 1, 5),
    _RuijieDot11WIDSRogueInfoString_Type()
)
ruijieDot11WIDSRogueInfoString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSRogueInfoString.setStatus("current")
_RuijieDot11WIDSPermitmaclistEnableTable_Object = MibTable
ruijieDot11WIDSPermitmaclistEnableTable = _RuijieDot11WIDSPermitmaclistEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 15)
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSPermitmaclistEnableTable.setStatus("current")
_RuijieDot11WIDSPermitmaclistEnableEntry_Object = MibTableRow
ruijieDot11WIDSPermitmaclistEnableEntry = _RuijieDot11WIDSPermitmaclistEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 15, 1)
)
ruijieDot11WIDSPermitmaclistEnableEntry.setIndexNames(
    (0, "RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSEnableVlanPermitmaclistNum"),
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSPermitmaclistEnableEntry.setStatus("current")
_RuijieDot11WIDSEnableVlanPermitmaclistNum_Type = Integer32
_RuijieDot11WIDSEnableVlanPermitmaclistNum_Object = MibTableColumn
ruijieDot11WIDSEnableVlanPermitmaclistNum = _RuijieDot11WIDSEnableVlanPermitmaclistNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 15, 1, 1),
    _RuijieDot11WIDSEnableVlanPermitmaclistNum_Type()
)
ruijieDot11WIDSEnableVlanPermitmaclistNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDot11WIDSEnableVlanPermitmaclistNum.setStatus("current")
_RuijieDot11WIDSEnableVlanPermitmaclistOper_Type = Integer32
_RuijieDot11WIDSEnableVlanPermitmaclistOper_Object = MibTableColumn
ruijieDot11WIDSEnableVlanPermitmaclistOper = _RuijieDot11WIDSEnableVlanPermitmaclistOper_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 15, 1, 2),
    _RuijieDot11WIDSEnableVlanPermitmaclistOper_Type()
)
ruijieDot11WIDSEnableVlanPermitmaclistOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSEnableVlanPermitmaclistOper.setStatus("current")
_RuijieDot11WIDSEnableVlanPermitmaclist_Type = MacAddress
_RuijieDot11WIDSEnableVlanPermitmaclist_Object = MibTableColumn
ruijieDot11WIDSEnableVlanPermitmaclist = _RuijieDot11WIDSEnableVlanPermitmaclist_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 15, 1, 3),
    _RuijieDot11WIDSEnableVlanPermitmaclist_Type()
)
ruijieDot11WIDSEnableVlanPermitmaclist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSEnableVlanPermitmaclist.setStatus("current")
_RuijieDot11WIDSResetStatistics_Type = TruthValue
_RuijieDot11WIDSResetStatistics_Object = MibScalar
ruijieDot11WIDSResetStatistics = _RuijieDot11WIDSResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 18),
    _RuijieDot11WIDSResetStatistics_Type()
)
ruijieDot11WIDSResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSResetStatistics.setStatus("current")
_RuijieDot11WIDSResetRoguehistoryStatistics_Type = Integer32
_RuijieDot11WIDSResetRoguehistoryStatistics_Object = MibScalar
ruijieDot11WIDSResetRoguehistoryStatistics = _RuijieDot11WIDSResetRoguehistoryStatistics_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 19),
    _RuijieDot11WIDSResetRoguehistoryStatistics_Type()
)
ruijieDot11WIDSResetRoguehistoryStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSResetRoguehistoryStatistics.setStatus("current")
_RuijieDot11WIDSResethistory_Type = Integer32
_RuijieDot11WIDSResethistory_Object = MibScalar
ruijieDot11WIDSResethistory = _RuijieDot11WIDSResethistory_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 20),
    _RuijieDot11WIDSResethistory_Type()
)
ruijieDot11WIDSResethistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSResethistory.setStatus("current")
_RuijieDot11WIDSResetDynamicBlacklistTable_Object = MibTable
ruijieDot11WIDSResetDynamicBlacklistTable = _RuijieDot11WIDSResetDynamicBlacklistTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 21)
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSResetDynamicBlacklistTable.setStatus("current")
_RuijieDot11WIDSResetDynamicBlacklistEntry_Object = MibTableRow
ruijieDot11WIDSResetDynamicBlacklistEntry = _RuijieDot11WIDSResetDynamicBlacklistEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 21, 1)
)
ruijieDot11WIDSResetDynamicBlacklistEntry.setIndexNames(
    (0, "RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSResetDynamicBlacklistMac"),
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSResetDynamicBlacklistEntry.setStatus("current")
_RuijieDot11WIDSResetDynamicBlacklistMac_Type = MacAddress
_RuijieDot11WIDSResetDynamicBlacklistMac_Object = MibTableColumn
ruijieDot11WIDSResetDynamicBlacklistMac = _RuijieDot11WIDSResetDynamicBlacklistMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 21, 1, 1),
    _RuijieDot11WIDSResetDynamicBlacklistMac_Type()
)
ruijieDot11WIDSResetDynamicBlacklistMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDot11WIDSResetDynamicBlacklistMac.setStatus("current")
_RuijieDot11WIDSResetDynamicBlacklistType_Type = Integer32
_RuijieDot11WIDSResetDynamicBlacklistType_Object = MibTableColumn
ruijieDot11WIDSResetDynamicBlacklistType = _RuijieDot11WIDSResetDynamicBlacklistType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 21, 1, 2),
    _RuijieDot11WIDSResetDynamicBlacklistType_Type()
)
ruijieDot11WIDSResetDynamicBlacklistType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSResetDynamicBlacklistType.setStatus("current")
_RuijieDot11WIDResetUserisolationStatistics_Type = Integer32
_RuijieDot11WIDResetUserisolationStatistics_Object = MibScalar
ruijieDot11WIDResetUserisolationStatistics = _RuijieDot11WIDResetUserisolationStatistics_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 22),
    _RuijieDot11WIDResetUserisolationStatistics_Type()
)
ruijieDot11WIDResetUserisolationStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDResetUserisolationStatistics.setStatus("current")
_RuijieDot11WIDUserisolationAC_Type = Integer32
_RuijieDot11WIDUserisolationAC_Object = MibScalar
ruijieDot11WIDUserisolationAC = _RuijieDot11WIDUserisolationAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 23),
    _RuijieDot11WIDUserisolationAC_Type()
)
ruijieDot11WIDUserisolationAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDUserisolationAC.setStatus("current")
_RuijieDot11WIDUserisolationAP_Type = Integer32
_RuijieDot11WIDUserisolationAP_Object = MibScalar
ruijieDot11WIDUserisolationAP = _RuijieDot11WIDUserisolationAP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 24),
    _RuijieDot11WIDUserisolationAP_Type()
)
ruijieDot11WIDUserisolationAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDUserisolationAP.setStatus("current")
_RuijieDot11WIDSShowStaticsTable_Object = MibTable
ruijieDot11WIDSShowStaticsTable = _RuijieDot11WIDSShowStaticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 25)
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSShowStaticsTable.setStatus("current")
_RuijieDot11WIDSShowStaticsEntry_Object = MibTableRow
ruijieDot11WIDSShowStaticsEntry = _RuijieDot11WIDSShowStaticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 25, 1)
)
ruijieDot11WIDSShowStaticsEntry.setIndexNames(
    (0, "RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSShowStaticsNum"),
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSShowStaticsEntry.setStatus("current")
_RuijieDot11WIDSShowStaticsNum_Type = Integer32
_RuijieDot11WIDSShowStaticsNum_Object = MibTableColumn
ruijieDot11WIDSShowStaticsNum = _RuijieDot11WIDSShowStaticsNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 25, 1, 1),
    _RuijieDot11WIDSShowStaticsNum_Type()
)
ruijieDot11WIDSShowStaticsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDot11WIDSShowStaticsNum.setStatus("current")
_RuijieDot11WIDSShowStaticsOper_Type = Integer32
_RuijieDot11WIDSShowStaticsOper_Object = MibTableColumn
ruijieDot11WIDSShowStaticsOper = _RuijieDot11WIDSShowStaticsOper_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 25, 1, 2),
    _RuijieDot11WIDSShowStaticsOper_Type()
)
ruijieDot11WIDSShowStaticsOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSShowStaticsOper.setStatus("current")
_RuijieDot11WIDSShowStaticsMac_Type = MacAddress
_RuijieDot11WIDSShowStaticsMac_Object = MibTableColumn
ruijieDot11WIDSShowStaticsMac = _RuijieDot11WIDSShowStaticsMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 25, 1, 3),
    _RuijieDot11WIDSShowStaticsMac_Type()
)
ruijieDot11WIDSShowStaticsMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSShowStaticsMac.setStatus("current")


class _RuijieDot11WIDSShowStaticsInfo_Type(DisplayString):
    """Custom type ruijieDot11WIDSShowStaticsInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieDot11WIDSShowStaticsInfo_Type.__name__ = "DisplayString"
_RuijieDot11WIDSShowStaticsInfo_Object = MibTableColumn
ruijieDot11WIDSShowStaticsInfo = _RuijieDot11WIDSShowStaticsInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 25, 1, 4),
    _RuijieDot11WIDSShowStaticsInfo_Type()
)
ruijieDot11WIDSShowStaticsInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSShowStaticsInfo.setStatus("current")
_RuijieDot11WIDSAssociationFailureTotalTimes_Type = Integer32
_RuijieDot11WIDSAssociationFailureTotalTimes_Object = MibScalar
ruijieDot11WIDSAssociationFailureTotalTimes = _RuijieDot11WIDSAssociationFailureTotalTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 26),
    _RuijieDot11WIDSAssociationFailureTotalTimes_Type()
)
ruijieDot11WIDSAssociationFailureTotalTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSAssociationFailureTotalTimes.setStatus("current")
_RuijieDot11WIDSSuspiciousAPInfoTable_Object = MibTable
ruijieDot11WIDSSuspiciousAPInfoTable = _RuijieDot11WIDSSuspiciousAPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 27)
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousAPInfoTable.setStatus("current")
_RuijieDot11WIDSSuspiciousAPInfoEntry_Object = MibTableRow
ruijieDot11WIDSSuspiciousAPInfoEntry = _RuijieDot11WIDSSuspiciousAPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 27, 1)
)
ruijieDot11WIDSSuspiciousAPInfoEntry.setIndexNames(
    (0, "RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSuspiciousAPBSS"),
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousAPInfoEntry.setStatus("current")
_RuijieDot11WIDSSuspiciousAPBSS_Type = MacAddress
_RuijieDot11WIDSSuspiciousAPBSS_Object = MibTableColumn
ruijieDot11WIDSSuspiciousAPBSS = _RuijieDot11WIDSSuspiciousAPBSS_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 27, 1, 1),
    _RuijieDot11WIDSSuspiciousAPBSS_Type()
)
ruijieDot11WIDSSuspiciousAPBSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousAPBSS.setStatus("current")
_RuijieDot11WIDSSuspiciousAPCount_Type = Integer32
_RuijieDot11WIDSSuspiciousAPCount_Object = MibTableColumn
ruijieDot11WIDSSuspiciousAPCount = _RuijieDot11WIDSSuspiciousAPCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 27, 1, 2),
    _RuijieDot11WIDSSuspiciousAPCount_Type()
)
ruijieDot11WIDSSuspiciousAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousAPCount.setStatus("current")
_RuijieDot11WIDSMomentFirstTimeDetectedSusAP_Type = TimeTicks
_RuijieDot11WIDSMomentFirstTimeDetectedSusAP_Object = MibTableColumn
ruijieDot11WIDSMomentFirstTimeDetectedSusAP = _RuijieDot11WIDSMomentFirstTimeDetectedSusAP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 27, 1, 3),
    _RuijieDot11WIDSMomentFirstTimeDetectedSusAP_Type()
)
ruijieDot11WIDSMomentFirstTimeDetectedSusAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSMomentFirstTimeDetectedSusAP.setStatus("current")
_RuijieDot11WIDSMomentLastTimeDetectedSusAP_Type = TimeTicks
_RuijieDot11WIDSMomentLastTimeDetectedSusAP_Object = MibTableColumn
ruijieDot11WIDSMomentLastTimeDetectedSusAP = _RuijieDot11WIDSMomentLastTimeDetectedSusAP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 27, 1, 4),
    _RuijieDot11WIDSMomentLastTimeDetectedSusAP_Type()
)
ruijieDot11WIDSMomentLastTimeDetectedSusAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSMomentLastTimeDetectedSusAP.setStatus("current")
_RuijieDot11WIDSSuspiciousAPSSID_Type = DisplayString
_RuijieDot11WIDSSuspiciousAPSSID_Object = MibTableColumn
ruijieDot11WIDSSuspiciousAPSSID = _RuijieDot11WIDSSuspiciousAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 27, 1, 5),
    _RuijieDot11WIDSSuspiciousAPSSID_Type()
)
ruijieDot11WIDSSuspiciousAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousAPSSID.setStatus("current")
_RuijieDot11WIDSSuspiciousAPMaxSignalStrength_Type = Integer32
_RuijieDot11WIDSSuspiciousAPMaxSignalStrength_Object = MibTableColumn
ruijieDot11WIDSSuspiciousAPMaxSignalStrength = _RuijieDot11WIDSSuspiciousAPMaxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 27, 1, 6),
    _RuijieDot11WIDSSuspiciousAPMaxSignalStrength_Type()
)
ruijieDot11WIDSSuspiciousAPMaxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousAPMaxSignalStrength.setStatus("current")
_RuijieDot11WIDSSuspiciousAPUsingChannel_Type = Integer32
_RuijieDot11WIDSSuspiciousAPUsingChannel_Object = MibTableColumn
ruijieDot11WIDSSuspiciousAPUsingChannel = _RuijieDot11WIDSSuspiciousAPUsingChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 27, 1, 7),
    _RuijieDot11WIDSSuspiciousAPUsingChannel_Type()
)
ruijieDot11WIDSSuspiciousAPUsingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousAPUsingChannel.setStatus("current")
_RuijieDot11WIDSSuspiciousAPFrameEncrption_Type = Integer32
_RuijieDot11WIDSSuspiciousAPFrameEncrption_Object = MibTableColumn
ruijieDot11WIDSSuspiciousAPFrameEncrption = _RuijieDot11WIDSSuspiciousAPFrameEncrption_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 27, 1, 8),
    _RuijieDot11WIDSSuspiciousAPFrameEncrption_Type()
)
ruijieDot11WIDSSuspiciousAPFrameEncrption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousAPFrameEncrption.setStatus("current")
_RuijieDot11WIDSSuspiciousAPNeedsDealingTag_Type = TruthValue
_RuijieDot11WIDSSuspiciousAPNeedsDealingTag_Object = MibTableColumn
ruijieDot11WIDSSuspiciousAPNeedsDealingTag = _RuijieDot11WIDSSuspiciousAPNeedsDealingTag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 27, 1, 9),
    _RuijieDot11WIDSSuspiciousAPNeedsDealingTag_Type()
)
ruijieDot11WIDSSuspiciousAPNeedsDealingTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousAPNeedsDealingTag.setStatus("current")
_RuijieDot11WIDSSuspiciousAPIgnoredTag_Type = TruthValue
_RuijieDot11WIDSSuspiciousAPIgnoredTag_Object = MibTableColumn
ruijieDot11WIDSSuspiciousAPIgnoredTag = _RuijieDot11WIDSSuspiciousAPIgnoredTag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 27, 1, 10),
    _RuijieDot11WIDSSuspiciousAPIgnoredTag_Type()
)
ruijieDot11WIDSSuspiciousAPIgnoredTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousAPIgnoredTag.setStatus("current")
_RuijieDot11WIDSSuspiciousSTAInfoTable_Object = MibTable
ruijieDot11WIDSSuspiciousSTAInfoTable = _RuijieDot11WIDSSuspiciousSTAInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 28)
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousSTAInfoTable.setStatus("current")
_RuijieDot11WIDSSuspiciousSTAInfoEntry_Object = MibTableRow
ruijieDot11WIDSSuspiciousSTAInfoEntry = _RuijieDot11WIDSSuspiciousSTAInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 28, 1)
)
ruijieDot11WIDSSuspiciousSTAInfoEntry.setIndexNames(
    (0, "RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSuspiciousSTAMAC"),
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousSTAInfoEntry.setStatus("current")
_RuijieDot11WIDSSuspiciousSTAMAC_Type = MacAddress
_RuijieDot11WIDSSuspiciousSTAMAC_Object = MibTableColumn
ruijieDot11WIDSSuspiciousSTAMAC = _RuijieDot11WIDSSuspiciousSTAMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 28, 1, 1),
    _RuijieDot11WIDSSuspiciousSTAMAC_Type()
)
ruijieDot11WIDSSuspiciousSTAMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousSTAMAC.setStatus("current")
_RuijieDot11WIDSAPCountDetectingSuspiciousSTA_Type = Integer32
_RuijieDot11WIDSAPCountDetectingSuspiciousSTA_Object = MibTableColumn
ruijieDot11WIDSAPCountDetectingSuspiciousSTA = _RuijieDot11WIDSAPCountDetectingSuspiciousSTA_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 28, 1, 2),
    _RuijieDot11WIDSAPCountDetectingSuspiciousSTA_Type()
)
ruijieDot11WIDSAPCountDetectingSuspiciousSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSAPCountDetectingSuspiciousSTA.setStatus("current")
_RuijieDot11WIDSMomentFirstTimeDetectedSusSTA_Type = TimeTicks
_RuijieDot11WIDSMomentFirstTimeDetectedSusSTA_Object = MibTableColumn
ruijieDot11WIDSMomentFirstTimeDetectedSusSTA = _RuijieDot11WIDSMomentFirstTimeDetectedSusSTA_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 28, 1, 3),
    _RuijieDot11WIDSMomentFirstTimeDetectedSusSTA_Type()
)
ruijieDot11WIDSMomentFirstTimeDetectedSusSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSMomentFirstTimeDetectedSusSTA.setStatus("current")
_RuijieDot11WIDSMomentLastTimeDetectedSusSTA_Type = TimeTicks
_RuijieDot11WIDSMomentLastTimeDetectedSusSTA_Object = MibTableColumn
ruijieDot11WIDSMomentLastTimeDetectedSusSTA = _RuijieDot11WIDSMomentLastTimeDetectedSusSTA_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 28, 1, 4),
    _RuijieDot11WIDSMomentLastTimeDetectedSusSTA_Type()
)
ruijieDot11WIDSMomentLastTimeDetectedSusSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSMomentLastTimeDetectedSusSTA.setStatus("current")
_RuijieDot11WIDSBSSIDSuspiciousSTAAccessing_Type = MacAddress
_RuijieDot11WIDSBSSIDSuspiciousSTAAccessing_Object = MibTableColumn
ruijieDot11WIDSBSSIDSuspiciousSTAAccessing = _RuijieDot11WIDSBSSIDSuspiciousSTAAccessing_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 28, 1, 5),
    _RuijieDot11WIDSBSSIDSuspiciousSTAAccessing_Type()
)
ruijieDot11WIDSBSSIDSuspiciousSTAAccessing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSBSSIDSuspiciousSTAAccessing.setStatus("current")
_RuijieDot11WIDSSuspiciousSTAMaxSignalStrength_Type = Integer32
_RuijieDot11WIDSSuspiciousSTAMaxSignalStrength_Object = MibTableColumn
ruijieDot11WIDSSuspiciousSTAMaxSignalStrength = _RuijieDot11WIDSSuspiciousSTAMaxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 28, 1, 6),
    _RuijieDot11WIDSSuspiciousSTAMaxSignalStrength_Type()
)
ruijieDot11WIDSSuspiciousSTAMaxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousSTAMaxSignalStrength.setStatus("current")
_RuijieDot11WIDSSuspiciousSTAUsingChannel_Type = Integer32
_RuijieDot11WIDSSuspiciousSTAUsingChannel_Object = MibTableColumn
ruijieDot11WIDSSuspiciousSTAUsingChannel = _RuijieDot11WIDSSuspiciousSTAUsingChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 28, 1, 7),
    _RuijieDot11WIDSSuspiciousSTAUsingChannel_Type()
)
ruijieDot11WIDSSuspiciousSTAUsingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousSTAUsingChannel.setStatus("current")
_RuijieDot11WIDSSuspiciousSTAWorksInAdhocMode_Type = TruthValue
_RuijieDot11WIDSSuspiciousSTAWorksInAdhocMode_Object = MibTableColumn
ruijieDot11WIDSSuspiciousSTAWorksInAdhocMode = _RuijieDot11WIDSSuspiciousSTAWorksInAdhocMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 28, 1, 8),
    _RuijieDot11WIDSSuspiciousSTAWorksInAdhocMode_Type()
)
ruijieDot11WIDSSuspiciousSTAWorksInAdhocMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousSTAWorksInAdhocMode.setStatus("current")
_RuijieDot11WIDSSuspiciousSTANeedsDealingTag_Type = TruthValue
_RuijieDot11WIDSSuspiciousSTANeedsDealingTag_Object = MibTableColumn
ruijieDot11WIDSSuspiciousSTANeedsDealingTag = _RuijieDot11WIDSSuspiciousSTANeedsDealingTag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 28, 1, 9),
    _RuijieDot11WIDSSuspiciousSTANeedsDealingTag_Type()
)
ruijieDot11WIDSSuspiciousSTANeedsDealingTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousSTANeedsDealingTag.setStatus("current")
_RuijieDot11WIDSSuspiciousSTAIgnoredTag_Type = TruthValue
_RuijieDot11WIDSSuspiciousSTAIgnoredTag_Object = MibTableColumn
ruijieDot11WIDSSuspiciousSTAIgnoredTag = _RuijieDot11WIDSSuspiciousSTAIgnoredTag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 1, 28, 1, 10),
    _RuijieDot11WIDSSuspiciousSTAIgnoredTag_Type()
)
ruijieDot11WIDSSuspiciousSTAIgnoredTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousSTAIgnoredTag.setStatus("current")
_RuijieDot11WIDSDetectObjects_ObjectIdentity = ObjectIdentity
ruijieDot11WIDSDetectObjects = _RuijieDot11WIDSDetectObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 2)
)
_RuijieDot11WIDSShowDot11IdsAttacklistTable_Object = MibTable
ruijieDot11WIDSShowDot11IdsAttacklistTable = _RuijieDot11WIDSShowDot11IdsAttacklistTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSShowDot11IdsAttacklistTable.setStatus("current")
_RuijieDot11WIDSShowDot11IdsAttacklistEntry_Object = MibTableRow
ruijieDot11WIDSShowDot11IdsAttacklistEntry = _RuijieDot11WIDSShowDot11IdsAttacklistEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 2, 1, 1)
)
ruijieDot11WIDSShowDot11IdsAttacklistEntry.setIndexNames(
    (0, "RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSShowDot11IdsAttacklistNum"),
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSShowDot11IdsAttacklistEntry.setStatus("current")
_RuijieDot11WIDSShowDot11IdsAttacklistNum_Type = Integer32
_RuijieDot11WIDSShowDot11IdsAttacklistNum_Object = MibTableColumn
ruijieDot11WIDSShowDot11IdsAttacklistNum = _RuijieDot11WIDSShowDot11IdsAttacklistNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 2, 1, 1, 1),
    _RuijieDot11WIDSShowDot11IdsAttacklistNum_Type()
)
ruijieDot11WIDSShowDot11IdsAttacklistNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDot11WIDSShowDot11IdsAttacklistNum.setStatus("current")
_RuijieDot11WIDSShowDot11IdsAttacklistOper_Type = Integer32
_RuijieDot11WIDSShowDot11IdsAttacklistOper_Object = MibTableColumn
ruijieDot11WIDSShowDot11IdsAttacklistOper = _RuijieDot11WIDSShowDot11IdsAttacklistOper_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 2, 1, 1, 2),
    _RuijieDot11WIDSShowDot11IdsAttacklistOper_Type()
)
ruijieDot11WIDSShowDot11IdsAttacklistOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSShowDot11IdsAttacklistOper.setStatus("current")
_RuijieDot11WIDSShowDot11IdsAttacklistMac_Type = MacAddress
_RuijieDot11WIDSShowDot11IdsAttacklistMac_Object = MibTableColumn
ruijieDot11WIDSShowDot11IdsAttacklistMac = _RuijieDot11WIDSShowDot11IdsAttacklistMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 2, 1, 1, 3),
    _RuijieDot11WIDSShowDot11IdsAttacklistMac_Type()
)
ruijieDot11WIDSShowDot11IdsAttacklistMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSShowDot11IdsAttacklistMac.setStatus("current")


class _RuijieDot11WIDSShowDot11IdsAttacklistInfo_Type(DisplayString):
    """Custom type ruijieDot11WIDSShowDot11IdsAttacklistInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieDot11WIDSShowDot11IdsAttacklistInfo_Type.__name__ = "DisplayString"
_RuijieDot11WIDSShowDot11IdsAttacklistInfo_Object = MibTableColumn
ruijieDot11WIDSShowDot11IdsAttacklistInfo = _RuijieDot11WIDSShowDot11IdsAttacklistInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 2, 1, 1, 4),
    _RuijieDot11WIDSShowDot11IdsAttacklistInfo_Type()
)
ruijieDot11WIDSShowDot11IdsAttacklistInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSShowDot11IdsAttacklistInfo.setStatus("current")
_RuijieDot11WIDSTrapsObjects_ObjectIdentity = ObjectIdentity
ruijieDot11WIDSTrapsObjects = _RuijieDot11WIDSTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 3)
)
_RuijieDot11WIDSSTAMAC_Type = MacAddress
_RuijieDot11WIDSSTAMAC_Object = MibScalar
ruijieDot11WIDSSTAMAC = _RuijieDot11WIDSSTAMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 3, 1),
    _RuijieDot11WIDSSTAMAC_Type()
)
ruijieDot11WIDSSTAMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSTAMAC.setStatus("current")


class _RuijieDot11WIDSAPBSSID_Type(DisplayString):
    """Custom type ruijieDot11WIDSAPBSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieDot11WIDSAPBSSID_Type.__name__ = "DisplayString"
_RuijieDot11WIDSAPBSSID_Object = MibScalar
ruijieDot11WIDSAPBSSID = _RuijieDot11WIDSAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 3, 2),
    _RuijieDot11WIDSAPBSSID_Type()
)
ruijieDot11WIDSAPBSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSAPBSSID.setStatus("current")


class _RuijieDot11WIDSInformation_Type(DisplayString):
    """Custom type ruijieDot11WIDSInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieDot11WIDSInformation_Type.__name__ = "DisplayString"
_RuijieDot11WIDSInformation_Object = MibScalar
ruijieDot11WIDSInformation = _RuijieDot11WIDSInformation_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 3, 3),
    _RuijieDot11WIDSInformation_Type()
)
ruijieDot11WIDSInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSInformation.setStatus("current")


class _RuijieDot11WIDSextinfo_Type(DisplayString):
    """Custom type ruijieDot11WIDSextinfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieDot11WIDSextinfo_Type.__name__ = "DisplayString"
_RuijieDot11WIDSextinfo_Object = MibScalar
ruijieDot11WIDSextinfo = _RuijieDot11WIDSextinfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 3, 4),
    _RuijieDot11WIDSextinfo_Type()
)
ruijieDot11WIDSextinfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSextinfo.setStatus("current")
_RuijieDot11WIDSDeviceInfoNUM_Type = Integer32
_RuijieDot11WIDSDeviceInfoNUM_Object = MibScalar
ruijieDot11WIDSDeviceInfoNUM = _RuijieDot11WIDSDeviceInfoNUM_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 3, 5),
    _RuijieDot11WIDSDeviceInfoNUM_Type()
)
ruijieDot11WIDSDeviceInfoNUM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSDeviceInfoNUM.setStatus("current")
_RuijieDot11WIDSDeviceInfoTYPE_Type = Integer32
_RuijieDot11WIDSDeviceInfoTYPE_Object = MibScalar
ruijieDot11WIDSDeviceInfoTYPE = _RuijieDot11WIDSDeviceInfoTYPE_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 3, 6),
    _RuijieDot11WIDSDeviceInfoTYPE_Type()
)
ruijieDot11WIDSDeviceInfoTYPE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSDeviceInfoTYPE.setStatus("current")
_RuijieDot11WIDSDeviceInfoOper_Type = Integer32
_RuijieDot11WIDSDeviceInfoOper_Object = MibScalar
ruijieDot11WIDSDeviceInfoOper = _RuijieDot11WIDSDeviceInfoOper_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 3, 7),
    _RuijieDot11WIDSDeviceInfoOper_Type()
)
ruijieDot11WIDSDeviceInfoOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSDeviceInfoOper.setStatus("current")
_RuijieDot11WIDSDeviceInfoMAC_Type = MacAddress
_RuijieDot11WIDSDeviceInfoMAC_Object = MibScalar
ruijieDot11WIDSDeviceInfoMAC = _RuijieDot11WIDSDeviceInfoMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 3, 8),
    _RuijieDot11WIDSDeviceInfoMAC_Type()
)
ruijieDot11WIDSDeviceInfoMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSDeviceInfoMAC.setStatus("current")


class _RuijieDot11WIDSDeviceInfoString_Type(DisplayString):
    """Custom type ruijieDot11WIDSDeviceInfoString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieDot11WIDSDeviceInfoString_Type.__name__ = "DisplayString"
_RuijieDot11WIDSDeviceInfoString_Object = MibScalar
ruijieDot11WIDSDeviceInfoString = _RuijieDot11WIDSDeviceInfoString_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 3, 9),
    _RuijieDot11WIDSDeviceInfoString_Type()
)
ruijieDot11WIDSDeviceInfoString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSDeviceInfoString.setStatus("current")
_RuijieDot11WIDSSuspiciousDeviceMac_Type = MacAddress
_RuijieDot11WIDSSuspiciousDeviceMac_Object = MibScalar
ruijieDot11WIDSSuspiciousDeviceMac = _RuijieDot11WIDSSuspiciousDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 3, 10),
    _RuijieDot11WIDSSuspiciousDeviceMac_Type()
)
ruijieDot11WIDSSuspiciousDeviceMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousDeviceMac.setStatus("current")
_RuijieDot11WIDSSuspiciousDeviceExtensionInfo_Type = DisplayString
_RuijieDot11WIDSSuspiciousDeviceExtensionInfo_Object = MibScalar
ruijieDot11WIDSSuspiciousDeviceExtensionInfo = _RuijieDot11WIDSSuspiciousDeviceExtensionInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 3, 11),
    _RuijieDot11WIDSSuspiciousDeviceExtensionInfo_Type()
)
ruijieDot11WIDSSuspiciousDeviceExtensionInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousDeviceExtensionInfo.setStatus("current")
_RuijieDot11WIDSUnauthorizedSSID_Type = DisplayString
_RuijieDot11WIDSUnauthorizedSSID_Object = MibScalar
ruijieDot11WIDSUnauthorizedSSID = _RuijieDot11WIDSUnauthorizedSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 3, 12),
    _RuijieDot11WIDSUnauthorizedSSID_Type()
)
ruijieDot11WIDSUnauthorizedSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSUnauthorizedSSID.setStatus("current")
_RuijieDot11WIDSSUnauthorizedSSIDExtensionInfo_Type = DisplayString
_RuijieDot11WIDSSUnauthorizedSSIDExtensionInfo_Object = MibScalar
ruijieDot11WIDSSUnauthorizedSSIDExtensionInfo = _RuijieDot11WIDSSUnauthorizedSSIDExtensionInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 3, 13),
    _RuijieDot11WIDSSUnauthorizedSSIDExtensionInfo_Type()
)
ruijieDot11WIDSSUnauthorizedSSIDExtensionInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSUnauthorizedSSIDExtensionInfo.setStatus("current")
_RuijieDot11WIDSAttackingDeviceMac_Type = MacAddress
_RuijieDot11WIDSAttackingDeviceMac_Object = MibScalar
ruijieDot11WIDSAttackingDeviceMac = _RuijieDot11WIDSAttackingDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 3, 14),
    _RuijieDot11WIDSAttackingDeviceMac_Type()
)
ruijieDot11WIDSAttackingDeviceMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSAttackingDeviceMac.setStatus("current")
_RuijieDot11WIDSAttackType_Type = Integer32
_RuijieDot11WIDSAttackType_Object = MibScalar
ruijieDot11WIDSAttackType = _RuijieDot11WIDSAttackType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 3, 15),
    _RuijieDot11WIDSAttackType_Type()
)
ruijieDot11WIDSAttackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSAttackType.setStatus("current")
_RuijieDot11WIDSAttackExtensionInfo_Type = DisplayString
_RuijieDot11WIDSAttackExtensionInfo_Object = MibScalar
ruijieDot11WIDSAttackExtensionInfo = _RuijieDot11WIDSAttackExtensionInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 3, 16),
    _RuijieDot11WIDSAttackExtensionInfo_Type()
)
ruijieDot11WIDSAttackExtensionInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSAttackExtensionInfo.setStatus("current")
_RuijieDot11WIDSMIBConform_ObjectIdentity = ObjectIdentity
ruijieDot11WIDSMIBConform = _RuijieDot11WIDSMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 4)
)
_RuijieDot11WIDSMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieDot11WIDSMIBCompliances = _RuijieDot11WIDSMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 4, 1)
)
_RuijieDot11WIDSMIBGroups_ObjectIdentity = ObjectIdentity
ruijieDot11WIDSMIBGroups = _RuijieDot11WIDSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 4, 2)
)

# Managed Objects groups

ruijieDot11WIDSMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 4, 2, 1)
)
ruijieDot11WIDSMIBGroup.setObjects(
      *(("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11VendorOper"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11VendorName"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11PermitOper"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11PermitSSID"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11AttackOper"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11AttackMAC"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11AttackInfo"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11PermitMACOper"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11PermitMACAddr"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSDeviceagingDuration"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSCountermeasuresMode"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSCountermeasureSet"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSDeviceMode"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WhitelistOper"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WhitelistMAC"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11StaticblacklistOper"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11StaticblacklistMAC"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSDynamicblacklistEnable"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSDynamicblacklistLifetime"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSAttackDetectionMode"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSRogueInfoOper"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSRogueInfoMAC"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSRogueInfoString"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSEnableVlanPermitmaclistOper"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSEnableVlanPermitmaclist"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSResetStatistics"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSResetRoguehistoryStatistics"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSResethistory"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSResetDynamicBlacklistType"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDResetUserisolationStatistics"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSShowDot11IdsAttacklistOper"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSShowDot11IdsAttacklistMac"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSShowDot11IdsAttacklistInfo"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDUserisolationAC"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDUserisolationAP"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSShowStaticsOper"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSShowStaticsMac"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSShowStaticsInfo"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSAssociationFailureTotalTimes"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSuspiciousAPCount"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSMomentFirstTimeDetectedSusAP"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSMomentLastTimeDetectedSusAP"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSuspiciousAPSSID"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSuspiciousAPMaxSignalStrength"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSuspiciousAPUsingChannel"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSuspiciousAPFrameEncrption"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSuspiciousAPNeedsDealingTag"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSuspiciousAPIgnoredTag"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSAPCountDetectingSuspiciousSTA"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSMomentFirstTimeDetectedSusSTA"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSMomentLastTimeDetectedSusSTA"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSBSSIDSuspiciousSTAAccessing"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSuspiciousSTAMaxSignalStrength"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSuspiciousSTAUsingChannel"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSuspiciousSTAWorksInAdhocMode"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSuspiciousSTANeedsDealingTag"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSuspiciousSTAIgnoredTag"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSuspiciousDeviceMac"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSuspiciousDeviceExtensionInfo"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSUnauthorizedSSID"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSUnauthorizedSSIDExtensionInfo"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSAttackingDeviceMac"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSAttackType"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSAttackExtensionInfo"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSTAMAC"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSAPBSSID"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSInformation"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSextinfo"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSDeviceInfoNUM"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSDeviceInfoTYPE"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSDeviceInfoOper"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSDeviceInfoMAC"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSDeviceInfoString"))
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSMIBGroup.setStatus("current")


# Notification objects

ruijieDot11WIDSWirelessUserConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 0, 1)
)
ruijieDot11WIDSWirelessUserConnect.setObjects(
      *(("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSTAMAC"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSAPBSSID"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSInformation"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSextinfo"))
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSWirelessUserConnect.setStatus(
        "current"
    )

ruijieDot11WIDSWirelessUserDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 0, 2)
)
ruijieDot11WIDSWirelessUserDisconnect.setObjects(
      *(("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSTAMAC"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSAPBSSID"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSInformation"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSextinfo"))
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSWirelessUserDisconnect.setStatus(
        "current"
    )

ruijieDot11WIDSWirelessUserReauthentication = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 0, 3)
)
ruijieDot11WIDSWirelessUserReauthentication.setObjects(
      *(("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSTAMAC"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSAPBSSID"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSInformation"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSextinfo"))
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSWirelessUserReauthentication.setStatus(
        "current"
    )

ruijieDot11WIDSWirelessUserAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 0, 4)
)
ruijieDot11WIDSWirelessUserAuthenticationFailure.setObjects(
      *(("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSTAMAC"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSAPBSSID"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSInformation"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSextinfo"))
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSWirelessUserAuthenticationFailure.setStatus(
        "current"
    )

ruijieDot11WIDSWirelessUserConnectFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 0, 5)
)
ruijieDot11WIDSWirelessUserConnectFailure.setObjects(
      *(("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSTAMAC"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSAPBSSID"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSInformation"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSextinfo"))
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSWirelessUserConnectFailure.setStatus(
        "current"
    )

ruijieDot11WIDSDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 0, 6)
)
ruijieDot11WIDSDevice.setObjects(
      *(("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSDeviceInfoNUM"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSDeviceInfoTYPE"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSDeviceInfoOper"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSDeviceInfoMAC"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSDeviceInfoString"))
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSDevice.setStatus(
        "current"
    )

ruijieDot11WIDSSuspiciousDeviceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 0, 7)
)
ruijieDot11WIDSSuspiciousDeviceTrap.setObjects(
      *(("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSuspiciousDeviceMac"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSuspiciousDeviceExtensionInfo"))
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousDeviceTrap.setStatus(
        "current"
    )

ruijieDot11WIDSUnauthorizedSSIDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 0, 8)
)
ruijieDot11WIDSUnauthorizedSSIDTrap.setObjects(
      *(("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSUnauthorizedSSID"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSSUnauthorizedSSIDExtensionInfo"))
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSUnauthorizedSSIDTrap.setStatus(
        "current"
    )

ruijieDot11WIDSDetectingAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 0, 9)
)
ruijieDot11WIDSDetectingAttackTrap.setObjects(
      *(("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSAttackingDeviceMac"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSAttackType"),
        ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSAttackExtensionInfo"))
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSDetectingAttackTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijieDot11WIDSMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 62, 4, 1, 1)
)
ruijieDot11WIDSMIBCompliance.setObjects(
    ("RUIJIE-DOT11-WIDS-MIB", "ruijieDot11WIDSMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-DOT11-WIDS-MIB",
    **{"ruijieDot11WIDSMIB": ruijieDot11WIDSMIB,
       "ruijieDot11WIDSTraps": ruijieDot11WIDSTraps,
       "ruijieDot11WIDSWirelessUserConnect": ruijieDot11WIDSWirelessUserConnect,
       "ruijieDot11WIDSWirelessUserDisconnect": ruijieDot11WIDSWirelessUserDisconnect,
       "ruijieDot11WIDSWirelessUserReauthentication": ruijieDot11WIDSWirelessUserReauthentication,
       "ruijieDot11WIDSWirelessUserAuthenticationFailure": ruijieDot11WIDSWirelessUserAuthenticationFailure,
       "ruijieDot11WIDSWirelessUserConnectFailure": ruijieDot11WIDSWirelessUserConnectFailure,
       "ruijieDot11WIDSDevice": ruijieDot11WIDSDevice,
       "ruijieDot11WIDSSuspiciousDeviceTrap": ruijieDot11WIDSSuspiciousDeviceTrap,
       "ruijieDot11WIDSUnauthorizedSSIDTrap": ruijieDot11WIDSUnauthorizedSSIDTrap,
       "ruijieDot11WIDSDetectingAttackTrap": ruijieDot11WIDSDetectingAttackTrap,
       "ruijieDot11WIDSConfigObjects": ruijieDot11WIDSConfigObjects,
       "ruijieDot11WIDSPermitVendorTable": ruijieDot11WIDSPermitVendorTable,
       "ruijieDot11WIDSPermitVendorEntry": ruijieDot11WIDSPermitVendorEntry,
       "ruijieDot11VendorOUI": ruijieDot11VendorOUI,
       "ruijieDot11VendorOper": ruijieDot11VendorOper,
       "ruijieDot11VendorName": ruijieDot11VendorName,
       "ruijieDot11WIDSPermitSSIDTable": ruijieDot11WIDSPermitSSIDTable,
       "ruijieDot11WIDSPermitSSIDEntry": ruijieDot11WIDSPermitSSIDEntry,
       "ruijieDot11PermitNum": ruijieDot11PermitNum,
       "ruijieDot11PermitOper": ruijieDot11PermitOper,
       "ruijieDot11PermitSSID": ruijieDot11PermitSSID,
       "ruijieDot11WIDSDeviceAttackMacaddressListTable": ruijieDot11WIDSDeviceAttackMacaddressListTable,
       "ruijieDot11WIDSDeviceAttackMacaddressListEntry": ruijieDot11WIDSDeviceAttackMacaddressListEntry,
       "ruijieDot11AttackNum": ruijieDot11AttackNum,
       "ruijieDot11AttackOper": ruijieDot11AttackOper,
       "ruijieDot11AttackMAC": ruijieDot11AttackMAC,
       "ruijieDot11AttackInfo": ruijieDot11AttackInfo,
       "ruijieDot11WIDSDevicePermitMacaddressListTable": ruijieDot11WIDSDevicePermitMacaddressListTable,
       "ruijieDot11WIDSDevicePermitMacaddressListEntry": ruijieDot11WIDSDevicePermitMacaddressListEntry,
       "ruijieDot11PermitMACNum": ruijieDot11PermitMACNum,
       "ruijieDot11PermitMACOper": ruijieDot11PermitMACOper,
       "ruijieDot11PermitMACAddr": ruijieDot11PermitMACAddr,
       "ruijieDot11WIDSDeviceagingDuration": ruijieDot11WIDSDeviceagingDuration,
       "ruijieDot11WIDSCountermeasuresMode": ruijieDot11WIDSCountermeasuresMode,
       "ruijieDot11WIDSCountermeasureSet": ruijieDot11WIDSCountermeasureSet,
       "ruijieDot11WIDSModeTable": ruijieDot11WIDSModeTable,
       "ruijieDot11WIDSModeEntry": ruijieDot11WIDSModeEntry,
       "ruijieDot11WIDSAPID": ruijieDot11WIDSAPID,
       "ruijieDot11WIDSDeviceMode": ruijieDot11WIDSDeviceMode,
       "ruijieDot11WIDSWhitelistMacaddressListTable": ruijieDot11WIDSWhitelistMacaddressListTable,
       "ruijieDot11WIDSWhitelistMacaddressListEntry": ruijieDot11WIDSWhitelistMacaddressListEntry,
       "ruijieDot11WhitelistNum": ruijieDot11WhitelistNum,
       "ruijieDot11WhitelistOper": ruijieDot11WhitelistOper,
       "ruijieDot11WhitelistMAC": ruijieDot11WhitelistMAC,
       "ruijieDot11WIDSStaticblackListTable": ruijieDot11WIDSStaticblackListTable,
       "ruijieDot11WIDSStaticblackListEntry": ruijieDot11WIDSStaticblackListEntry,
       "ruijieDot11StaticblacklistNum": ruijieDot11StaticblacklistNum,
       "ruijieDot11StaticblacklistOper": ruijieDot11StaticblacklistOper,
       "ruijieDot11StaticblacklistMAC": ruijieDot11StaticblacklistMAC,
       "ruijieDot11WIDSDynamicblacklistEnable": ruijieDot11WIDSDynamicblacklistEnable,
       "ruijieDot11WIDSDynamicblacklistLifetime": ruijieDot11WIDSDynamicblacklistLifetime,
       "ruijieDot11WIDSAttackDetectionMode": ruijieDot11WIDSAttackDetectionMode,
       "ruijieDot11WIDSRogueInfoTable": ruijieDot11WIDSRogueInfoTable,
       "ruijieDot11WIDSRogueInfoEntry": ruijieDot11WIDSRogueInfoEntry,
       "ruijieDot11WIDSRogueInfoNUM": ruijieDot11WIDSRogueInfoNUM,
       "ruijieDot11WIDSRogueInfoTYPE": ruijieDot11WIDSRogueInfoTYPE,
       "ruijieDot11WIDSRogueInfoOper": ruijieDot11WIDSRogueInfoOper,
       "ruijieDot11WIDSRogueInfoMAC": ruijieDot11WIDSRogueInfoMAC,
       "ruijieDot11WIDSRogueInfoString": ruijieDot11WIDSRogueInfoString,
       "ruijieDot11WIDSPermitmaclistEnableTable": ruijieDot11WIDSPermitmaclistEnableTable,
       "ruijieDot11WIDSPermitmaclistEnableEntry": ruijieDot11WIDSPermitmaclistEnableEntry,
       "ruijieDot11WIDSEnableVlanPermitmaclistNum": ruijieDot11WIDSEnableVlanPermitmaclistNum,
       "ruijieDot11WIDSEnableVlanPermitmaclistOper": ruijieDot11WIDSEnableVlanPermitmaclistOper,
       "ruijieDot11WIDSEnableVlanPermitmaclist": ruijieDot11WIDSEnableVlanPermitmaclist,
       "ruijieDot11WIDSResetStatistics": ruijieDot11WIDSResetStatistics,
       "ruijieDot11WIDSResetRoguehistoryStatistics": ruijieDot11WIDSResetRoguehistoryStatistics,
       "ruijieDot11WIDSResethistory": ruijieDot11WIDSResethistory,
       "ruijieDot11WIDSResetDynamicBlacklistTable": ruijieDot11WIDSResetDynamicBlacklistTable,
       "ruijieDot11WIDSResetDynamicBlacklistEntry": ruijieDot11WIDSResetDynamicBlacklistEntry,
       "ruijieDot11WIDSResetDynamicBlacklistMac": ruijieDot11WIDSResetDynamicBlacklistMac,
       "ruijieDot11WIDSResetDynamicBlacklistType": ruijieDot11WIDSResetDynamicBlacklistType,
       "ruijieDot11WIDResetUserisolationStatistics": ruijieDot11WIDResetUserisolationStatistics,
       "ruijieDot11WIDUserisolationAC": ruijieDot11WIDUserisolationAC,
       "ruijieDot11WIDUserisolationAP": ruijieDot11WIDUserisolationAP,
       "ruijieDot11WIDSShowStaticsTable": ruijieDot11WIDSShowStaticsTable,
       "ruijieDot11WIDSShowStaticsEntry": ruijieDot11WIDSShowStaticsEntry,
       "ruijieDot11WIDSShowStaticsNum": ruijieDot11WIDSShowStaticsNum,
       "ruijieDot11WIDSShowStaticsOper": ruijieDot11WIDSShowStaticsOper,
       "ruijieDot11WIDSShowStaticsMac": ruijieDot11WIDSShowStaticsMac,
       "ruijieDot11WIDSShowStaticsInfo": ruijieDot11WIDSShowStaticsInfo,
       "ruijieDot11WIDSAssociationFailureTotalTimes": ruijieDot11WIDSAssociationFailureTotalTimes,
       "ruijieDot11WIDSSuspiciousAPInfoTable": ruijieDot11WIDSSuspiciousAPInfoTable,
       "ruijieDot11WIDSSuspiciousAPInfoEntry": ruijieDot11WIDSSuspiciousAPInfoEntry,
       "ruijieDot11WIDSSuspiciousAPBSS": ruijieDot11WIDSSuspiciousAPBSS,
       "ruijieDot11WIDSSuspiciousAPCount": ruijieDot11WIDSSuspiciousAPCount,
       "ruijieDot11WIDSMomentFirstTimeDetectedSusAP": ruijieDot11WIDSMomentFirstTimeDetectedSusAP,
       "ruijieDot11WIDSMomentLastTimeDetectedSusAP": ruijieDot11WIDSMomentLastTimeDetectedSusAP,
       "ruijieDot11WIDSSuspiciousAPSSID": ruijieDot11WIDSSuspiciousAPSSID,
       "ruijieDot11WIDSSuspiciousAPMaxSignalStrength": ruijieDot11WIDSSuspiciousAPMaxSignalStrength,
       "ruijieDot11WIDSSuspiciousAPUsingChannel": ruijieDot11WIDSSuspiciousAPUsingChannel,
       "ruijieDot11WIDSSuspiciousAPFrameEncrption": ruijieDot11WIDSSuspiciousAPFrameEncrption,
       "ruijieDot11WIDSSuspiciousAPNeedsDealingTag": ruijieDot11WIDSSuspiciousAPNeedsDealingTag,
       "ruijieDot11WIDSSuspiciousAPIgnoredTag": ruijieDot11WIDSSuspiciousAPIgnoredTag,
       "ruijieDot11WIDSSuspiciousSTAInfoTable": ruijieDot11WIDSSuspiciousSTAInfoTable,
       "ruijieDot11WIDSSuspiciousSTAInfoEntry": ruijieDot11WIDSSuspiciousSTAInfoEntry,
       "ruijieDot11WIDSSuspiciousSTAMAC": ruijieDot11WIDSSuspiciousSTAMAC,
       "ruijieDot11WIDSAPCountDetectingSuspiciousSTA": ruijieDot11WIDSAPCountDetectingSuspiciousSTA,
       "ruijieDot11WIDSMomentFirstTimeDetectedSusSTA": ruijieDot11WIDSMomentFirstTimeDetectedSusSTA,
       "ruijieDot11WIDSMomentLastTimeDetectedSusSTA": ruijieDot11WIDSMomentLastTimeDetectedSusSTA,
       "ruijieDot11WIDSBSSIDSuspiciousSTAAccessing": ruijieDot11WIDSBSSIDSuspiciousSTAAccessing,
       "ruijieDot11WIDSSuspiciousSTAMaxSignalStrength": ruijieDot11WIDSSuspiciousSTAMaxSignalStrength,
       "ruijieDot11WIDSSuspiciousSTAUsingChannel": ruijieDot11WIDSSuspiciousSTAUsingChannel,
       "ruijieDot11WIDSSuspiciousSTAWorksInAdhocMode": ruijieDot11WIDSSuspiciousSTAWorksInAdhocMode,
       "ruijieDot11WIDSSuspiciousSTANeedsDealingTag": ruijieDot11WIDSSuspiciousSTANeedsDealingTag,
       "ruijieDot11WIDSSuspiciousSTAIgnoredTag": ruijieDot11WIDSSuspiciousSTAIgnoredTag,
       "ruijieDot11WIDSDetectObjects": ruijieDot11WIDSDetectObjects,
       "ruijieDot11WIDSShowDot11IdsAttacklistTable": ruijieDot11WIDSShowDot11IdsAttacklistTable,
       "ruijieDot11WIDSShowDot11IdsAttacklistEntry": ruijieDot11WIDSShowDot11IdsAttacklistEntry,
       "ruijieDot11WIDSShowDot11IdsAttacklistNum": ruijieDot11WIDSShowDot11IdsAttacklistNum,
       "ruijieDot11WIDSShowDot11IdsAttacklistOper": ruijieDot11WIDSShowDot11IdsAttacklistOper,
       "ruijieDot11WIDSShowDot11IdsAttacklistMac": ruijieDot11WIDSShowDot11IdsAttacklistMac,
       "ruijieDot11WIDSShowDot11IdsAttacklistInfo": ruijieDot11WIDSShowDot11IdsAttacklistInfo,
       "ruijieDot11WIDSTrapsObjects": ruijieDot11WIDSTrapsObjects,
       "ruijieDot11WIDSSTAMAC": ruijieDot11WIDSSTAMAC,
       "ruijieDot11WIDSAPBSSID": ruijieDot11WIDSAPBSSID,
       "ruijieDot11WIDSInformation": ruijieDot11WIDSInformation,
       "ruijieDot11WIDSextinfo": ruijieDot11WIDSextinfo,
       "ruijieDot11WIDSDeviceInfoNUM": ruijieDot11WIDSDeviceInfoNUM,
       "ruijieDot11WIDSDeviceInfoTYPE": ruijieDot11WIDSDeviceInfoTYPE,
       "ruijieDot11WIDSDeviceInfoOper": ruijieDot11WIDSDeviceInfoOper,
       "ruijieDot11WIDSDeviceInfoMAC": ruijieDot11WIDSDeviceInfoMAC,
       "ruijieDot11WIDSDeviceInfoString": ruijieDot11WIDSDeviceInfoString,
       "ruijieDot11WIDSSuspiciousDeviceMac": ruijieDot11WIDSSuspiciousDeviceMac,
       "ruijieDot11WIDSSuspiciousDeviceExtensionInfo": ruijieDot11WIDSSuspiciousDeviceExtensionInfo,
       "ruijieDot11WIDSUnauthorizedSSID": ruijieDot11WIDSUnauthorizedSSID,
       "ruijieDot11WIDSSUnauthorizedSSIDExtensionInfo": ruijieDot11WIDSSUnauthorizedSSIDExtensionInfo,
       "ruijieDot11WIDSAttackingDeviceMac": ruijieDot11WIDSAttackingDeviceMac,
       "ruijieDot11WIDSAttackType": ruijieDot11WIDSAttackType,
       "ruijieDot11WIDSAttackExtensionInfo": ruijieDot11WIDSAttackExtensionInfo,
       "ruijieDot11WIDSMIBConform": ruijieDot11WIDSMIBConform,
       "ruijieDot11WIDSMIBCompliances": ruijieDot11WIDSMIBCompliances,
       "ruijieDot11WIDSMIBCompliance": ruijieDot11WIDSMIBCompliance,
       "ruijieDot11WIDSMIBGroups": ruijieDot11WIDSMIBGroups,
       "ruijieDot11WIDSMIBGroup": ruijieDot11WIDSMIBGroup}
)

# SNMP MIB module (ZYXEL-ES-WIRELESS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-ES-WIRELESS.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:16:50 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

esWireless = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlanControllerAPTable_Object = MibTable
wlanControllerAPTable = _WlanControllerAPTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 11)
)
if mibBuilder.loadTexts:
    wlanControllerAPTable.setStatus("current")
_WlanControllerAPEntry_Object = MibTableRow
wlanControllerAPEntry = _WlanControllerAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 11, 1)
)
wlanControllerAPEntry.setIndexNames(
    (0, "ZYXEL-ES-WIRELESS", "wlanControllerAPIndex"),
)
if mibBuilder.loadTexts:
    wlanControllerAPEntry.setStatus("current")


class _WlanControllerAPIndex_Type(Integer32):
    """Custom type wlanControllerAPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WlanControllerAPIndex_Type.__name__ = "Integer32"
_WlanControllerAPIndex_Object = MibTableColumn
wlanControllerAPIndex = _WlanControllerAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 11, 1, 1),
    _WlanControllerAPIndex_Type()
)
wlanControllerAPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerAPIndex.setStatus("current")


class _WlanControllerAPMac_Type(OctetString):
    """Custom type wlanControllerAPMac based on OctetString"""
    defaultValue = OctetString("public")


_WlanControllerAPMac_Type.__name__ = "OctetString"
_WlanControllerAPMac_Object = MibTableColumn
wlanControllerAPMac = _WlanControllerAPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 11, 1, 2),
    _WlanControllerAPMac_Type()
)
wlanControllerAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerAPMac.setStatus("current")
_WlanControllerAPDescription_Type = OctetString
_WlanControllerAPDescription_Object = MibTableColumn
wlanControllerAPDescription = _WlanControllerAPDescription_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 11, 1, 3),
    _WlanControllerAPDescription_Type()
)
wlanControllerAPDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerAPDescription.setStatus("current")
_WlanControllerAPMgmtIPAddr_Type = IpAddress
_WlanControllerAPMgmtIPAddr_Object = MibTableColumn
wlanControllerAPMgmtIPAddr = _WlanControllerAPMgmtIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 11, 1, 4),
    _WlanControllerAPMgmtIPAddr_Type()
)
wlanControllerAPMgmtIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerAPMgmtIPAddr.setStatus("current")
_WlanControllerAPStationNum_Type = Unsigned32
_WlanControllerAPStationNum_Object = MibTableColumn
wlanControllerAPStationNum = _WlanControllerAPStationNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 11, 1, 5),
    _WlanControllerAPStationNum_Type()
)
wlanControllerAPStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerAPStationNum.setStatus("current")
_WlanControllerAPRadioTable_Object = MibTable
wlanControllerAPRadioTable = _WlanControllerAPRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 12)
)
if mibBuilder.loadTexts:
    wlanControllerAPRadioTable.setStatus("current")
_WlanControllerAPRadioEntry_Object = MibTableRow
wlanControllerAPRadioEntry = _WlanControllerAPRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 12, 1)
)
wlanControllerAPRadioEntry.setIndexNames(
    (0, "ZYXEL-ES-WIRELESS", "wlanControllerRadioIndex"),
)
if mibBuilder.loadTexts:
    wlanControllerAPRadioEntry.setStatus("current")


class _WlanControllerRadioIndex_Type(Integer32):
    """Custom type wlanControllerRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WlanControllerRadioIndex_Type.__name__ = "Integer32"
_WlanControllerRadioIndex_Object = MibTableColumn
wlanControllerRadioIndex = _WlanControllerRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 12, 1, 1),
    _WlanControllerRadioIndex_Type()
)
wlanControllerRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioIndex.setStatus("current")
_WlanControllerRadioStationNum_Type = Unsigned32
_WlanControllerRadioStationNum_Object = MibTableColumn
wlanControllerRadioStationNum = _WlanControllerRadioStationNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 12, 1, 2),
    _WlanControllerRadioStationNum_Type()
)
wlanControllerRadioStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioStationNum.setStatus("current")


class _WlanControllerRadioCurrentChannel_Type(Integer32):
    """Custom type wlanControllerRadioCurrentChannel based on Integer32"""
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
              13,
              36,
              40,
              44,
              48,
              52,
              56,
              60,
              64,
              100,
              104,
              108,
              112,
              116,
              120,
              124,
              128,
              132,
              136,
              140,
              149,
              153,
              157,
              161,
              165)
        )
    )
    namedValues = NamedValues(
        *(("device_is_disable", 0),
          ("channel-01_2412mhz", 1),
          ("channel-02_2417mhz", 2),
          ("channel-03_2422mhz", 3),
          ("channel-04_2427mhz", 4),
          ("channel-05_2432mhz", 5),
          ("channel-06_2437mhz", 6),
          ("channel-07_2442mhz", 7),
          ("channel-08_2447mhz", 8),
          ("channel-09_2452mhz", 9),
          ("channel-10_2457mhz", 10),
          ("channel-11_2462mhz", 11),
          ("channel-12_2467mhz", 12),
          ("channel-13_2472mhz", 13),
          ("channel-36_5180mhz", 36),
          ("channel-40_5200mhz", 40),
          ("channel-44_5220mhz", 44),
          ("channel-48_5240mhz", 48),
          ("channel-52_5260mhz", 52),
          ("channel-56_5280mhz", 56),
          ("channel-60_5300mhz", 60),
          ("channel-64_5320mhz", 64),
          ("channel-100_5500mhz", 100),
          ("channel-104_5520mhz", 104),
          ("channel-108_5540mhz", 108),
          ("channel-112_5560mhz", 112),
          ("channel-116_5580mhz", 116),
          ("channel-120_5600mhz", 120),
          ("channel-124_5620mhz", 124),
          ("channel-128_5640mhz", 128),
          ("channel-132_5660mhz", 132),
          ("channel-136_5680mhz", 136),
          ("channel-140_5700mhz", 140),
          ("channel-149_5745mhz", 149),
          ("channel-153_5765mhz", 153),
          ("channel-157_5785mhz", 157),
          ("channel-161_5805mhz", 161),
          ("channel-165_5825mhz", 165))
    )


_WlanControllerRadioCurrentChannel_Type.__name__ = "Integer32"
_WlanControllerRadioCurrentChannel_Object = MibTableColumn
wlanControllerRadioCurrentChannel = _WlanControllerRadioCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 12, 1, 3),
    _WlanControllerRadioCurrentChannel_Type()
)
wlanControllerRadioCurrentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioCurrentChannel.setStatus("current")


class _WlanControllerRadioOperationMode_Type(Integer32):
    """Custom type wlanControllerRadioOperationMode based on Integer32"""
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
        *(("na", 0),
          ("ap", 1),
          ("monitor", 2),
          ("mesh-Root", 3),
          ("mesh-repeater", 4))
    )


_WlanControllerRadioOperationMode_Type.__name__ = "Integer32"
_WlanControllerRadioOperationMode_Object = MibTableColumn
wlanControllerRadioOperationMode = _WlanControllerRadioOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 12, 1, 4),
    _WlanControllerRadioOperationMode_Type()
)
wlanControllerRadioOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioOperationMode.setStatus("current")


class _WlanControllerRadioBand_Type(Integer32):
    """Custom type wlanControllerRadioBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("mode_2_4G", 1),
          ("mode_5G", 2))
    )


_WlanControllerRadioBand_Type.__name__ = "Integer32"
_WlanControllerRadioBand_Object = MibTableColumn
wlanControllerRadioBand = _WlanControllerRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 12, 1, 5),
    _WlanControllerRadioBand_Type()
)
wlanControllerRadioBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioBand.setStatus("current")
_WlanControllerRadioTxPkt_Type = Counter32
_WlanControllerRadioTxPkt_Object = MibTableColumn
wlanControllerRadioTxPkt = _WlanControllerRadioTxPkt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 12, 1, 6),
    _WlanControllerRadioTxPkt_Type()
)
wlanControllerRadioTxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioTxPkt.setStatus("current")
_WlanControllerRadioRxPkt_Type = Counter32
_WlanControllerRadioRxPkt_Object = MibTableColumn
wlanControllerRadioRxPkt = _WlanControllerRadioRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 12, 1, 7),
    _WlanControllerRadioRxPkt_Type()
)
wlanControllerRadioRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioRxPkt.setStatus("current")
_WlanControllerRadioTxPower_Type = Integer32
_WlanControllerRadioTxPower_Object = MibTableColumn
wlanControllerRadioTxPower = _WlanControllerRadioTxPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 12, 1, 8),
    _WlanControllerRadioTxPower_Type()
)
wlanControllerRadioTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioTxPower.setStatus("current")
_WlanControllerAPVAPTable_Object = MibTable
wlanControllerAPVAPTable = _WlanControllerAPVAPTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 13)
)
if mibBuilder.loadTexts:
    wlanControllerAPVAPTable.setStatus("current")
_WlanControllerAPVAPEntry_Object = MibTableRow
wlanControllerAPVAPEntry = _WlanControllerAPVAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 13, 1)
)
wlanControllerAPVAPEntry.setIndexNames(
    (0, "ZYXEL-ES-WIRELESS", "wlanControllerRadioVAPIndex"),
)
if mibBuilder.loadTexts:
    wlanControllerAPVAPEntry.setStatus("current")


class _WlanControllerRadioVAPIndex_Type(Integer32):
    """Custom type wlanControllerRadioVAPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WlanControllerRadioVAPIndex_Type.__name__ = "Integer32"
_WlanControllerRadioVAPIndex_Object = MibTableColumn
wlanControllerRadioVAPIndex = _WlanControllerRadioVAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 13, 1, 1),
    _WlanControllerRadioVAPIndex_Type()
)
wlanControllerRadioVAPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioVAPIndex.setStatus("current")
_WlanControllerRadioVAPSSIDName_Type = OctetString
_WlanControllerRadioVAPSSIDName_Object = MibTableColumn
wlanControllerRadioVAPSSIDName = _WlanControllerRadioVAPSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 13, 1, 2),
    _WlanControllerRadioVAPSSIDName_Type()
)
wlanControllerRadioVAPSSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioVAPSSIDName.setStatus("current")


class _WlanControllerRadioVAPVLANID_Type(Integer32):
    """Custom type wlanControllerRadioVAPVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_WlanControllerRadioVAPVLANID_Type.__name__ = "Integer32"
_WlanControllerRadioVAPVLANID_Object = MibTableColumn
wlanControllerRadioVAPVLANID = _WlanControllerRadioVAPVLANID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 13, 1, 3),
    _WlanControllerRadioVAPVLANID_Type()
)
wlanControllerRadioVAPVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioVAPVLANID.setStatus("current")
_WlanControllerRadioVAPSecMode_Type = OctetString
_WlanControllerRadioVAPSecMode_Object = MibTableColumn
wlanControllerRadioVAPSecMode = _WlanControllerRadioVAPSecMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 13, 1, 4),
    _WlanControllerRadioVAPSecMode_Type()
)
wlanControllerRadioVAPSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioVAPSecMode.setStatus("current")
_WlanControllerStationTable_Object = MibTable
wlanControllerStationTable = _WlanControllerStationTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14)
)
if mibBuilder.loadTexts:
    wlanControllerStationTable.setStatus("current")
_WlanControllerStationEntry_Object = MibTableRow
wlanControllerStationEntry = _WlanControllerStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14, 1)
)
wlanControllerStationEntry.setIndexNames(
    (0, "ZYXEL-ES-WIRELESS", "wlanControllerStationIndex"),
)
if mibBuilder.loadTexts:
    wlanControllerStationEntry.setStatus("current")


class _WlanControllerStationIndex_Type(Integer32):
    """Custom type wlanControllerStationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WlanControllerStationIndex_Type.__name__ = "Integer32"
_WlanControllerStationIndex_Object = MibTableColumn
wlanControllerStationIndex = _WlanControllerStationIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14, 1, 1),
    _WlanControllerStationIndex_Type()
)
wlanControllerStationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerStationIndex.setStatus("current")


class _WlanControllerStationMacAddress_Type(OctetString):
    """Custom type wlanControllerStationMacAddress based on OctetString"""
    defaultValue = OctetString("public")


_WlanControllerStationMacAddress_Type.__name__ = "OctetString"
_WlanControllerStationMacAddress_Object = MibTableColumn
wlanControllerStationMacAddress = _WlanControllerStationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14, 1, 2),
    _WlanControllerStationMacAddress_Type()
)
wlanControllerStationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerStationMacAddress.setStatus("current")
_WlanControllerStationAssociatedTime_Type = OctetString
_WlanControllerStationAssociatedTime_Object = MibTableColumn
wlanControllerStationAssociatedTime = _WlanControllerStationAssociatedTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14, 1, 3),
    _WlanControllerStationAssociatedTime_Type()
)
wlanControllerStationAssociatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerStationAssociatedTime.setStatus("current")
_WlanControllerStationSSID_Type = OctetString
_WlanControllerStationSSID_Object = MibTableColumn
wlanControllerStationSSID = _WlanControllerStationSSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14, 1, 4),
    _WlanControllerStationSSID_Type()
)
wlanControllerStationSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerStationSSID.setStatus("current")
_WlanControllerStationIPAddr_Type = IpAddress
_WlanControllerStationIPAddr_Object = MibTableColumn
wlanControllerStationIPAddr = _WlanControllerStationIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14, 1, 5),
    _WlanControllerStationIPAddr_Type()
)
wlanControllerStationIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerStationIPAddr.setStatus("current")
_WlanControllerStationAssociatedAPMac_Type = OctetString
_WlanControllerStationAssociatedAPMac_Object = MibTableColumn
wlanControllerStationAssociatedAPMac = _WlanControllerStationAssociatedAPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14, 1, 6),
    _WlanControllerStationAssociatedAPMac_Type()
)
wlanControllerStationAssociatedAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerStationAssociatedAPMac.setStatus("current")
_WlanControllerStationSignalStrength_Type = OctetString
_WlanControllerStationSignalStrength_Object = MibTableColumn
wlanControllerStationSignalStrength = _WlanControllerStationSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14, 1, 7),
    _WlanControllerStationSignalStrength_Type()
)
wlanControllerStationSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerStationSignalStrength.setStatus("current")
_WlanControllerStationTxPkt_Type = Counter32
_WlanControllerStationTxPkt_Object = MibTableColumn
wlanControllerStationTxPkt = _WlanControllerStationTxPkt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14, 1, 8),
    _WlanControllerStationTxPkt_Type()
)
wlanControllerStationTxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerStationTxPkt.setStatus("current")
_WlanControllerStationRxPkt_Type = Counter32
_WlanControllerStationRxPkt_Object = MibTableColumn
wlanControllerStationRxPkt = _WlanControllerStationRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14, 1, 9),
    _WlanControllerStationRxPkt_Type()
)
wlanControllerStationRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerStationRxPkt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ES-WIRELESS",
    **{"esWireless": esWireless,
       "wlanControllerAPTable": wlanControllerAPTable,
       "wlanControllerAPEntry": wlanControllerAPEntry,
       "wlanControllerAPIndex": wlanControllerAPIndex,
       "wlanControllerAPMac": wlanControllerAPMac,
       "wlanControllerAPDescription": wlanControllerAPDescription,
       "wlanControllerAPMgmtIPAddr": wlanControllerAPMgmtIPAddr,
       "wlanControllerAPStationNum": wlanControllerAPStationNum,
       "wlanControllerAPRadioTable": wlanControllerAPRadioTable,
       "wlanControllerAPRadioEntry": wlanControllerAPRadioEntry,
       "wlanControllerRadioIndex": wlanControllerRadioIndex,
       "wlanControllerRadioStationNum": wlanControllerRadioStationNum,
       "wlanControllerRadioCurrentChannel": wlanControllerRadioCurrentChannel,
       "wlanControllerRadioOperationMode": wlanControllerRadioOperationMode,
       "wlanControllerRadioBand": wlanControllerRadioBand,
       "wlanControllerRadioTxPkt": wlanControllerRadioTxPkt,
       "wlanControllerRadioRxPkt": wlanControllerRadioRxPkt,
       "wlanControllerRadioTxPower": wlanControllerRadioTxPower,
       "wlanControllerAPVAPTable": wlanControllerAPVAPTable,
       "wlanControllerAPVAPEntry": wlanControllerAPVAPEntry,
       "wlanControllerRadioVAPIndex": wlanControllerRadioVAPIndex,
       "wlanControllerRadioVAPSSIDName": wlanControllerRadioVAPSSIDName,
       "wlanControllerRadioVAPVLANID": wlanControllerRadioVAPVLANID,
       "wlanControllerRadioVAPSecMode": wlanControllerRadioVAPSecMode,
       "wlanControllerStationTable": wlanControllerStationTable,
       "wlanControllerStationEntry": wlanControllerStationEntry,
       "wlanControllerStationIndex": wlanControllerStationIndex,
       "wlanControllerStationMacAddress": wlanControllerStationMacAddress,
       "wlanControllerStationAssociatedTime": wlanControllerStationAssociatedTime,
       "wlanControllerStationSSID": wlanControllerStationSSID,
       "wlanControllerStationIPAddr": wlanControllerStationIPAddr,
       "wlanControllerStationAssociatedAPMac": wlanControllerStationAssociatedAPMac,
       "wlanControllerStationSignalStrength": wlanControllerStationSignalStrength,
       "wlanControllerStationTxPkt": wlanControllerStationTxPkt,
       "wlanControllerStationRxPkt": wlanControllerStationRxPkt}
)

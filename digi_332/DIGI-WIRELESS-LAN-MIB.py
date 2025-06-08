# SNMP MIB module (DIGI-WIRELESS-LAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-WIRELESS-LAN-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:54:31 2025
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

(digiWLan,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiWLan")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlanTable_Object = MibTable
wlanTable = _WlanTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13, 11)
)
if mibBuilder.loadTexts:
    wlanTable.setStatus("mandatory")
_WlanEntry_Object = MibTableRow
wlanEntry = _WlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13, 11, 1)
)
wlanEntry.setIndexNames(
    (0, "DIGI-WIRELESS-LAN-MIB", "wlanIndex"),
)
if mibBuilder.loadTexts:
    wlanEntry.setStatus("mandatory")


class _WlanDiversity_Type(Integer32):
    """Custom type wlanDiversity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("tx_pri_rx_div", 3))
    )


_WlanDiversity_Type.__name__ = "Integer32"
_WlanDiversity_Object = MibTableColumn
wlanDiversity = _WlanDiversity_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13, 11, 1, 11),
    _WlanDiversity_Type()
)
wlanDiversity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanDiversity.setStatus("mandatory")


class _WlanRtsThreshold_Type(Integer32):
    """Custom type wlanRtsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_WlanRtsThreshold_Type.__name__ = "Integer32"
_WlanRtsThreshold_Object = MibTableColumn
wlanRtsThreshold = _WlanRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13, 11, 1, 12),
    _WlanRtsThreshold_Type()
)
wlanRtsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRtsThreshold.setStatus("mandatory")


class _WlanFragmentationThreshold_Type(Integer32):
    """Custom type wlanFragmentationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_WlanFragmentationThreshold_Type.__name__ = "Integer32"
_WlanFragmentationThreshold_Object = MibTableColumn
wlanFragmentationThreshold = _WlanFragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13, 11, 1, 13),
    _WlanFragmentationThreshold_Type()
)
wlanFragmentationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanFragmentationThreshold.setStatus("mandatory")
_WlanCountryCode_Type = Integer32
_WlanCountryCode_Object = MibTableColumn
wlanCountryCode = _WlanCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13, 11, 1, 14),
    _WlanCountryCode_Type()
)
wlanCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCountryCode.setStatus("mandatory")


class _WlanAuthentication_Type(Integer32):
    """Custom type wlanAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open_system", 1),
          ("shared_key", 2))
    )


_WlanAuthentication_Type.__name__ = "Integer32"
_WlanAuthentication_Object = MibTableColumn
wlanAuthentication = _WlanAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13, 11, 1, 15),
    _WlanAuthentication_Type()
)
wlanAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthentication.setStatus("mandatory")


class _WlanDensity_Type(Integer32):
    """Custom type wlanDensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("medium", 2),
          ("high", 3))
    )


_WlanDensity_Type.__name__ = "Integer32"
_WlanDensity_Object = MibTableColumn
wlanDensity = _WlanDensity_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13, 11, 1, 16),
    _WlanDensity_Type()
)
wlanDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanDensity.setStatus("mandatory")


class _WlanAutoSsid_Type(Integer32):
    """Custom type wlanAutoSsid based on Integer32"""
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


_WlanAutoSsid_Type.__name__ = "Integer32"
_WlanAutoSsid_Object = MibTableColumn
wlanAutoSsid = _WlanAutoSsid_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13, 11, 1, 17),
    _WlanAutoSsid_Type()
)
wlanAutoSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAutoSsid.setStatus("mandatory")


class _WlanDesiredSsid_Type(OctetString):
    """Custom type wlanDesiredSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlanDesiredSsid_Type.__name__ = "OctetString"
_WlanDesiredSsid_Object = MibTableColumn
wlanDesiredSsid = _WlanDesiredSsid_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13, 11, 1, 18),
    _WlanDesiredSsid_Type()
)
wlanDesiredSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanDesiredSsid.setStatus("mandatory")


class _WlanEncryptionMode_Type(Integer32):
    """Custom type wlanEncryptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("em_none", 1),
          ("em_64_bit", 2),
          ("em_128_bit", 3))
    )


_WlanEncryptionMode_Type.__name__ = "Integer32"
_WlanEncryptionMode_Object = MibTableColumn
wlanEncryptionMode = _WlanEncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13, 11, 1, 19),
    _WlanEncryptionMode_Type()
)
wlanEncryptionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanEncryptionMode.setStatus("mandatory")


class _WlanEncryptionKey_Type(OctetString):
    """Custom type wlanEncryptionKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(10, 10),
        ValueSizeConstraint(26, 26),
    )


_WlanEncryptionKey_Type.__name__ = "OctetString"
_WlanEncryptionKey_Object = MibTableColumn
wlanEncryptionKey = _WlanEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13, 11, 1, 20),
    _WlanEncryptionKey_Type()
)
wlanEncryptionKey.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wlanEncryptionKey.setStatus("mandatory")
_WlanCurrentChannel_Type = Integer32
_WlanCurrentChannel_Object = MibTableColumn
wlanCurrentChannel = _WlanCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13, 11, 1, 21),
    _WlanCurrentChannel_Type()
)
wlanCurrentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanCurrentChannel.setStatus("mandatory")


class _WlanCurrentSsid_Type(OctetString):
    """Custom type wlanCurrentSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlanCurrentSsid_Type.__name__ = "OctetString"
_WlanCurrentSsid_Object = MibTableColumn
wlanCurrentSsid = _WlanCurrentSsid_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13, 11, 1, 22),
    _WlanCurrentSsid_Type()
)
wlanCurrentSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanCurrentSsid.setStatus("mandatory")


class _WlanRadioFirmwareVersion_Type(OctetString):
    """Custom type wlanRadioFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlanRadioFirmwareVersion_Type.__name__ = "OctetString"
_WlanRadioFirmwareVersion_Object = MibTableColumn
wlanRadioFirmwareVersion = _WlanRadioFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13, 11, 1, 23),
    _WlanRadioFirmwareVersion_Type()
)
wlanRadioFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadioFirmwareVersion.setStatus("mandatory")


class _WlanRadioHardwareVersion_Type(OctetString):
    """Custom type wlanRadioHardwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlanRadioHardwareVersion_Type.__name__ = "OctetString"
_WlanRadioHardwareVersion_Object = MibTableColumn
wlanRadioHardwareVersion = _WlanRadioHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13, 11, 1, 24),
    _WlanRadioHardwareVersion_Type()
)
wlanRadioHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadioHardwareVersion.setStatus("mandatory")
_WlanReceiveSignalStrength_Type = Integer32
_WlanReceiveSignalStrength_Object = MibTableColumn
wlanReceiveSignalStrength = _WlanReceiveSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13, 11, 1, 25),
    _WlanReceiveSignalStrength_Type()
)
wlanReceiveSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanReceiveSignalStrength.setStatus("mandatory")
_WlanCurrentTransmitPower_Type = Integer32
_WlanCurrentTransmitPower_Object = MibTableColumn
wlanCurrentTransmitPower = _WlanCurrentTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13, 11, 1, 26),
    _WlanCurrentTransmitPower_Type()
)
wlanCurrentTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanCurrentTransmitPower.setStatus("mandatory")


class _WlanCurrentTransmitSpeed_Type(Integer32):
    """Custom type wlanCurrentTransmitSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("rate_1Mb", 1),
          ("rate_2Mb", 2),
          ("rate_5_5Mb", 4),
          ("rate_11Mb", 8))
    )


_WlanCurrentTransmitSpeed_Type.__name__ = "Integer32"
_WlanCurrentTransmitSpeed_Object = MibTableColumn
wlanCurrentTransmitSpeed = _WlanCurrentTransmitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13, 11, 1, 27),
    _WlanCurrentTransmitSpeed_Type()
)
wlanCurrentTransmitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanCurrentTransmitSpeed.setStatus("mandatory")


class _WlanCurrentLinkStatus_Type(Integer32):
    """Custom type wlanCurrentLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("searching", 2),
          ("i_associated", 3),
          ("e_associated", 4),
          ("w_associated", 6))
    )


_WlanCurrentLinkStatus_Type.__name__ = "Integer32"
_WlanCurrentLinkStatus_Object = MibTableColumn
wlanCurrentLinkStatus = _WlanCurrentLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13, 11, 1, 28),
    _WlanCurrentLinkStatus_Type()
)
wlanCurrentLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanCurrentLinkStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-WIRELESS-LAN-MIB",
    **{"DisplayString": DisplayString,
       "wlanTable": wlanTable,
       "wlanEntry": wlanEntry,
       "wlanDiversity": wlanDiversity,
       "wlanRtsThreshold": wlanRtsThreshold,
       "wlanFragmentationThreshold": wlanFragmentationThreshold,
       "wlanCountryCode": wlanCountryCode,
       "wlanAuthentication": wlanAuthentication,
       "wlanDensity": wlanDensity,
       "wlanAutoSsid": wlanAutoSsid,
       "wlanDesiredSsid": wlanDesiredSsid,
       "wlanEncryptionMode": wlanEncryptionMode,
       "wlanEncryptionKey": wlanEncryptionKey,
       "wlanCurrentChannel": wlanCurrentChannel,
       "wlanCurrentSsid": wlanCurrentSsid,
       "wlanRadioFirmwareVersion": wlanRadioFirmwareVersion,
       "wlanRadioHardwareVersion": wlanRadioHardwareVersion,
       "wlanReceiveSignalStrength": wlanReceiveSignalStrength,
       "wlanCurrentTransmitPower": wlanCurrentTransmitPower,
       "wlanCurrentTransmitSpeed": wlanCurrentTransmitSpeed,
       "wlanCurrentLinkStatus": wlanCurrentLinkStatus}
)

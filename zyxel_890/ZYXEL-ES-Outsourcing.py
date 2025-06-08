# SNMP MIB module (ZYXEL-ES-Outsourcing) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-ES-Outsourcing.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:25:25 2025
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

(esProductSpecific,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esProductSpecific")


# MODULE-IDENTITY

esOutsourcing = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1)
)
if mibBuilder.loadTexts:
    wireless.setStatus("current")
_WlanRadioTable_ObjectIdentity = ObjectIdentity
wlanRadioTable = _WlanRadioTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    wlanRadioTable.setStatus("current")


class _WlanESSID_Type(OctetString):
    """Custom type wlanESSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlanESSID_Type.__name__ = "OctetString"
_WlanESSID_Object = MibScalar
wlanESSID = _WlanESSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 1, 1),
    _WlanESSID_Type()
)
wlanESSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanESSID.setStatus("current")


class _WlanChannel_Type(Integer32):
    """Custom type wlanChannel based on Integer32"""
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
        *(("device-is-disable", 0),
          ("channel-01-2412mhz", 1),
          ("channel-02-2417mhz", 2),
          ("channel-03-2422mhz", 3),
          ("channel-04-2427mhz", 4),
          ("channel-05-2432mhz", 5),
          ("channel-06-2437mhz", 6),
          ("channel-07-2442mhz", 7),
          ("channel-08-2447mhz", 8),
          ("channel-09-2452mhz", 9),
          ("channel-10-2457mhz", 10),
          ("channel-11-2462mhz", 11),
          ("channel-12-2467mhz", 12),
          ("channel-13-2472mhz", 13))
    )


_WlanChannel_Type.__name__ = "Integer32"
_WlanChannel_Object = MibScalar
wlanChannel = _WlanChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 1, 2),
    _WlanChannel_Type()
)
wlanChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanChannel.setStatus("current")


class _WlanRadioMode_Type(Integer32):
    """Custom type wlanRadioMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("mode-802-11bgn", 1),
          ("mode-802-11ng", 2),
          ("mode-802-11bg", 3),
          ("mode-802-11n", 4),
          ("mode-802-11g", 5),
          ("mode-802-11b", 6))
    )


_WlanRadioMode_Type.__name__ = "Integer32"
_WlanRadioMode_Object = MibScalar
wlanRadioMode = _WlanRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 1, 3),
    _WlanRadioMode_Type()
)
wlanRadioMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadioMode.setStatus("current")


class _WlanChannelWidth_Type(Integer32):
    """Custom type wlanChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channelwidth-auto", 1),
          ("channelwidth-20MHz", 2))
    )


_WlanChannelWidth_Type.__name__ = "Integer32"
_WlanChannelWidth_Object = MibScalar
wlanChannelWidth = _WlanChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 1, 4),
    _WlanChannelWidth_Type()
)
wlanChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanChannelWidth.setStatus("current")


class _WlanTransmitPower_Type(Integer32):
    """Custom type wlanTransmitPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("txpower-25", 1),
          ("txpower-50", 2),
          ("txpower-100", 3))
    )


_WlanTransmitPower_Type.__name__ = "Integer32"
_WlanTransmitPower_Object = MibScalar
wlanTransmitPower = _WlanTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 1, 5),
    _WlanTransmitPower_Type()
)
wlanTransmitPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanTransmitPower.setStatus("current")


class _WlanBeaconInterval_Type(Integer32):
    """Custom type wlanBeaconInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WlanBeaconInterval_Type.__name__ = "Integer32"
_WlanBeaconInterval_Object = MibScalar
wlanBeaconInterval = _WlanBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 1, 6),
    _WlanBeaconInterval_Type()
)
wlanBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanBeaconInterval.setStatus("current")


class _WlanRTSThreshold_Type(Integer32):
    """Custom type wlanRTSThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2432),
    )


_WlanRTSThreshold_Type.__name__ = "Integer32"
_WlanRTSThreshold_Object = MibScalar
wlanRTSThreshold = _WlanRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 1, 7),
    _WlanRTSThreshold_Type()
)
wlanRTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRTSThreshold.setStatus("current")


class _WlanFragmentationThreshold_Type(Integer32):
    """Custom type wlanFragmentationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(800, 2432),
    )


_WlanFragmentationThreshold_Type.__name__ = "Integer32"
_WlanFragmentationThreshold_Object = MibScalar
wlanFragmentationThreshold = _WlanFragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 1, 8),
    _WlanFragmentationThreshold_Type()
)
wlanFragmentationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanFragmentationThreshold.setStatus("current")


class _WlanPreambleType_Type(Integer32):
    """Custom type wlanPreambleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("preambletype-dynamic", 1),
          ("preambletype-short", 2),
          ("preambletype-long", 3))
    )


_WlanPreambleType_Type.__name__ = "Integer32"
_WlanPreambleType_Object = MibScalar
wlanPreambleType = _WlanPreambleType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 1, 9),
    _WlanPreambleType_Type()
)
wlanPreambleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanPreambleType.setStatus("current")
_WlanSecurityControl_ObjectIdentity = ObjectIdentity
wlanSecurityControl = _WlanSecurityControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    wlanSecurityControl.setStatus("current")


class _WlanSecMode_Type(Integer32):
    """Custom type wlanSecMode based on Integer32"""
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
        *(("disable", 1),
          ("wpa", 2),
          ("wpa2", 3),
          ("wpa-wpa2", 4),
          ("wep", 5))
    )


_WlanSecMode_Type.__name__ = "Integer32"
_WlanSecMode_Object = MibScalar
wlanSecMode = _WlanSecMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 2, 1),
    _WlanSecMode_Type()
)
wlanSecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSecMode.setStatus("current")
_WlanWPAGroupKeyRekey_Type = Integer32
_WlanWPAGroupKeyRekey_Object = MibScalar
wlanWPAGroupKeyRekey = _WlanWPAGroupKeyRekey_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 2, 2),
    _WlanWPAGroupKeyRekey_Type()
)
wlanWPAGroupKeyRekey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWPAGroupKeyRekey.setStatus("current")


class _Wlan8021xSupport_Type(Integer32):
    """Custom type wlan8021xSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wlan8021x-disable", 1),
          ("wlan8021x-enable", 2))
    )


_Wlan8021xSupport_Type.__name__ = "Integer32"
_Wlan8021xSupport_Object = MibScalar
wlan8021xSupport = _Wlan8021xSupport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 2, 3),
    _Wlan8021xSupport_Type()
)
wlan8021xSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan8021xSupport.setStatus("current")


class _WlanWPAPreSharedKey_Type(OctetString):
    """Custom type wlanWPAPreSharedKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_WlanWPAPreSharedKey_Type.__name__ = "OctetString"
_WlanWPAPreSharedKey_Object = MibScalar
wlanWPAPreSharedKey = _WlanWPAPreSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 2, 4),
    _WlanWPAPreSharedKey_Type()
)
wlanWPAPreSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWPAPreSharedKey.setStatus("current")
_WlanRadiusSrvInfo_Type = OctetString
_WlanRadiusSrvInfo_Object = MibScalar
wlanRadiusSrvInfo = _WlanRadiusSrvInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 2, 5),
    _WlanRadiusSrvInfo_Type()
)
wlanRadiusSrvInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusSrvInfo.setStatus("current")
_WlanRadiusSrvAuthPort_Type = Integer32
_WlanRadiusSrvAuthPort_Object = MibScalar
wlanRadiusSrvAuthPort = _WlanRadiusSrvAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 2, 6),
    _WlanRadiusSrvAuthPort_Type()
)
wlanRadiusSrvAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusSrvAuthPort.setStatus("current")
_WlanRadiusSrvSharedSecretKey_Type = OctetString
_WlanRadiusSrvSharedSecretKey_Object = MibScalar
wlanRadiusSrvSharedSecretKey = _WlanRadiusSrvSharedSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 2, 7),
    _WlanRadiusSrvSharedSecretKey_Type()
)
wlanRadiusSrvSharedSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusSrvSharedSecretKey.setStatus("current")


class _WlanRadiusSrvAuthMethod_Type(Integer32):
    """Custom type wlanRadiusSrvAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authmethod-opensystem", 1),
          ("authmethod-sharedkey", 2),
          ("authmethod-both", 3))
    )


_WlanRadiusSrvAuthMethod_Type.__name__ = "Integer32"
_WlanRadiusSrvAuthMethod_Object = MibScalar
wlanRadiusSrvAuthMethod = _WlanRadiusSrvAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 2, 8),
    _WlanRadiusSrvAuthMethod_Type()
)
wlanRadiusSrvAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusSrvAuthMethod.setStatus("current")


class _WlanWEPEncryption_Type(Integer32):
    """Custom type wlanWEPEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("encrypt-64-bit", 1),
          ("encyrpt-128-bit", 2))
    )


_WlanWEPEncryption_Type.__name__ = "Integer32"
_WlanWEPEncryption_Object = MibScalar
wlanWEPEncryption = _WlanWEPEncryption_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 2, 9),
    _WlanWEPEncryption_Type()
)
wlanWEPEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWEPEncryption.setStatus("current")


class _WlanWEPMode_Type(Integer32):
    """Custom type wlanWEPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wepmode-hex", 1),
          ("wepmode-ascii", 2))
    )


_WlanWEPMode_Type.__name__ = "Integer32"
_WlanWEPMode_Object = MibScalar
wlanWEPMode = _WlanWEPMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 2, 10),
    _WlanWEPMode_Type()
)
wlanWEPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWEPMode.setStatus("current")
_WlanWEPKeyIndex_Type = Integer32
_WlanWEPKeyIndex_Object = MibScalar
wlanWEPKeyIndex = _WlanWEPKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 2, 11),
    _WlanWEPKeyIndex_Type()
)
wlanWEPKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWEPKeyIndex.setStatus("current")


class _WlanWEPKey1_Type(OctetString):
    """Custom type wlanWEPKey1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 26),
    )


_WlanWEPKey1_Type.__name__ = "OctetString"
_WlanWEPKey1_Object = MibScalar
wlanWEPKey1 = _WlanWEPKey1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 2, 12),
    _WlanWEPKey1_Type()
)
wlanWEPKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWEPKey1.setStatus("current")


class _WlanWEPKey2_Type(OctetString):
    """Custom type wlanWEPKey2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 26),
    )


_WlanWEPKey2_Type.__name__ = "OctetString"
_WlanWEPKey2_Object = MibScalar
wlanWEPKey2 = _WlanWEPKey2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 2, 13),
    _WlanWEPKey2_Type()
)
wlanWEPKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWEPKey2.setStatus("current")


class _WlanWEPKey3_Type(OctetString):
    """Custom type wlanWEPKey3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 26),
    )


_WlanWEPKey3_Type.__name__ = "OctetString"
_WlanWEPKey3_Object = MibScalar
wlanWEPKey3 = _WlanWEPKey3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 2, 14),
    _WlanWEPKey3_Type()
)
wlanWEPKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWEPKey3.setStatus("current")


class _WlanWEPKey4_Type(OctetString):
    """Custom type wlanWEPKey4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 26),
    )


_WlanWEPKey4_Type.__name__ = "OctetString"
_WlanWEPKey4_Object = MibScalar
wlanWEPKey4 = _WlanWEPKey4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 2, 15),
    _WlanWEPKey4_Type()
)
wlanWEPKey4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWEPKey4.setStatus("current")


class _WlanWEPAuthMethod_Type(Integer32):
    """Custom type wlanWEPAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authmethod-opensystem", 1),
          ("authmethod-sharedkey", 2),
          ("authmethod-both", 3))
    )


_WlanWEPAuthMethod_Type.__name__ = "Integer32"
_WlanWEPAuthMethod_Object = MibScalar
wlanWEPAuthMethod = _WlanWEPAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 2, 16),
    _WlanWEPAuthMethod_Type()
)
wlanWEPAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWEPAuthMethod.setStatus("current")
_WlanStatistics_ObjectIdentity = ObjectIdentity
wlanStatistics = _WlanStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 3)
)
if mibBuilder.loadTexts:
    wlanStatistics.setStatus("current")
_Dot11TransmittedCount_Type = Integer32
_Dot11TransmittedCount_Object = MibScalar
dot11TransmittedCount = _Dot11TransmittedCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 3, 1),
    _Dot11TransmittedCount_Type()
)
dot11TransmittedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedCount.setStatus("current")
_Dot11ReceivedCount_Type = Integer32
_Dot11ReceivedCount_Object = MibScalar
dot11ReceivedCount = _Dot11ReceivedCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 3, 2),
    _Dot11ReceivedCount_Type()
)
dot11ReceivedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedCount.setStatus("current")
_Dot11RetryCount_Type = Integer32
_Dot11RetryCount_Object = MibScalar
dot11RetryCount = _Dot11RetryCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 3, 3),
    _Dot11RetryCount_Type()
)
dot11RetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RetryCount.setStatus("current")
_WlanStationCount_Type = Integer32
_WlanStationCount_Object = MibScalar
wlanStationCount = _WlanStationCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 3, 4),
    _WlanStationCount_Type()
)
wlanStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStationCount.setStatus("current")
_WlanTraps_ObjectIdentity = ObjectIdentity
wlanTraps = _WlanTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 4)
)
if mibBuilder.loadTexts:
    wlanTraps.setStatus("current")
_WlanTrapsControl_ObjectIdentity = ObjectIdentity
wlanTrapsControl = _WlanTrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    wlanTrapsControl.setStatus("current")


class _TrapWirelessControl_Type(Integer32):
    """Custom type trapWirelessControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapWirelessControl_Type.__name__ = "Integer32"
_TrapWirelessControl_Object = MibScalar
trapWirelessControl = _TrapWirelessControl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 4, 1, 1),
    _TrapWirelessControl_Type()
)
trapWirelessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapWirelessControl.setStatus("current")
_WlanTrapsFormat_ObjectIdentity = ObjectIdentity
wlanTrapsFormat = _WlanTrapsFormat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    wlanTrapsFormat.setStatus("current")
_TrapGenericMessage_Type = DisplayString
_TrapGenericMessage_Object = MibScalar
trapGenericMessage = _TrapGenericMessage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 4, 2, 1),
    _TrapGenericMessage_Type()
)
trapGenericMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapGenericMessage.setStatus("current")
_TrapMACAddress_Type = MacAddress
_TrapMACAddress_Object = MibScalar
trapMACAddress = _TrapMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 4, 2, 2),
    _TrapMACAddress_Type()
)
trapMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapMACAddress.setStatus("current")
_TrapWlanSSID_Type = DisplayString
_TrapWlanSSID_Object = MibScalar
trapWlanSSID = _TrapWlanSSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 4, 2, 3),
    _TrapWlanSSID_Type()
)
trapWlanSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapWlanSSID.setStatus("current")
_WlanTrapsItems_ObjectIdentity = ObjectIdentity
wlanTrapsItems = _WlanTrapsItems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    wlanTrapsItems.setStatus("current")
_DeviceTraps_ObjectIdentity = ObjectIdentity
deviceTraps = _DeviceTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 2)
)
if mibBuilder.loadTexts:
    deviceTraps.setStatus("current")
_DeviceTrapsControl_ObjectIdentity = ObjectIdentity
deviceTrapsControl = _DeviceTrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    deviceTrapsControl.setStatus("current")


class _TrapDeviceInfoControl_Type(Integer32):
    """Custom type trapDeviceInfoControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapDeviceInfoControl_Type.__name__ = "Integer32"
_TrapDeviceInfoControl_Object = MibScalar
trapDeviceInfoControl = _TrapDeviceInfoControl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 2, 1, 1),
    _TrapDeviceInfoControl_Type()
)
trapDeviceInfoControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDeviceInfoControl.setStatus("current")
_DeviceTrapsItems_ObjectIdentity = ObjectIdentity
deviceTrapsItems = _DeviceTrapsItems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    deviceTrapsItems.setStatus("current")

# Managed Objects groups


# Notification objects

wlanStaAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    wlanStaAssociation.setStatus(
        "current"
    )

wlanStaDisassociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    wlanStaDisassociation.setStatus(
        "current"
    )

wlanStaAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 1, 4, 3, 3)
)
if mibBuilder.loadTexts:
    wlanStaAuthFail.setStatus(
        "current"
    )

trapDeviceEthIPAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    trapDeviceEthIPAddr.setStatus(
        "current"
    )

trapDeviceEthMACAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    trapDeviceEthMACAddr.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ES-Outsourcing",
    **{"esOutsourcing": esOutsourcing,
       "wireless": wireless,
       "wlanRadioTable": wlanRadioTable,
       "wlanESSID": wlanESSID,
       "wlanChannel": wlanChannel,
       "wlanRadioMode": wlanRadioMode,
       "wlanChannelWidth": wlanChannelWidth,
       "wlanTransmitPower": wlanTransmitPower,
       "wlanBeaconInterval": wlanBeaconInterval,
       "wlanRTSThreshold": wlanRTSThreshold,
       "wlanFragmentationThreshold": wlanFragmentationThreshold,
       "wlanPreambleType": wlanPreambleType,
       "wlanSecurityControl": wlanSecurityControl,
       "wlanSecMode": wlanSecMode,
       "wlanWPAGroupKeyRekey": wlanWPAGroupKeyRekey,
       "wlan8021xSupport": wlan8021xSupport,
       "wlanWPAPreSharedKey": wlanWPAPreSharedKey,
       "wlanRadiusSrvInfo": wlanRadiusSrvInfo,
       "wlanRadiusSrvAuthPort": wlanRadiusSrvAuthPort,
       "wlanRadiusSrvSharedSecretKey": wlanRadiusSrvSharedSecretKey,
       "wlanRadiusSrvAuthMethod": wlanRadiusSrvAuthMethod,
       "wlanWEPEncryption": wlanWEPEncryption,
       "wlanWEPMode": wlanWEPMode,
       "wlanWEPKeyIndex": wlanWEPKeyIndex,
       "wlanWEPKey1": wlanWEPKey1,
       "wlanWEPKey2": wlanWEPKey2,
       "wlanWEPKey3": wlanWEPKey3,
       "wlanWEPKey4": wlanWEPKey4,
       "wlanWEPAuthMethod": wlanWEPAuthMethod,
       "wlanStatistics": wlanStatistics,
       "dot11TransmittedCount": dot11TransmittedCount,
       "dot11ReceivedCount": dot11ReceivedCount,
       "dot11RetryCount": dot11RetryCount,
       "wlanStationCount": wlanStationCount,
       "wlanTraps": wlanTraps,
       "wlanTrapsControl": wlanTrapsControl,
       "trapWirelessControl": trapWirelessControl,
       "wlanTrapsFormat": wlanTrapsFormat,
       "trapGenericMessage": trapGenericMessage,
       "trapMACAddress": trapMACAddress,
       "trapWlanSSID": trapWlanSSID,
       "wlanTrapsItems": wlanTrapsItems,
       "wlanStaAssociation": wlanStaAssociation,
       "wlanStaDisassociation": wlanStaDisassociation,
       "wlanStaAuthFail": wlanStaAuthFail,
       "deviceTraps": deviceTraps,
       "deviceTrapsControl": deviceTrapsControl,
       "trapDeviceInfoControl": trapDeviceInfoControl,
       "deviceTrapsItems": deviceTrapsItems,
       "trapDeviceEthIPAddr": trapDeviceEthIPAddr,
       "trapDeviceEthMACAddr": trapDeviceEthMACAddr}
)

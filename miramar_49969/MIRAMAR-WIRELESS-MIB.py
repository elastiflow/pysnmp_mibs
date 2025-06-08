# SNMP MIB module (MIRAMAR-WIRELESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/miramar_49969/MIRAMAR-WIRELESS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:32:26 2025
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

mirWirelessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Miramar_ObjectIdentity = ObjectIdentity
miramar = _Miramar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49969)
)
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49969, 8)
)
_Miramarnet_ObjectIdentity = ObjectIdentity
miramarnet = _Miramarnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20)
)
_Settings_ObjectIdentity = ObjectIdentity
settings = _Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6)
)


class _Ccq_Type(DisplayString):
    """Custom type ccq based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Ccq_Type.__name__ = "DisplayString"
_Ccq_Object = MibScalar
ccq = _Ccq_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 1),
    _Ccq_Type()
)
ccq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccq.setStatus("current")


class _Bw_Type(DisplayString):
    """Custom type bw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Bw_Type.__name__ = "DisplayString"
_Bw_Object = MibScalar
bw = _Bw_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 2),
    _Bw_Type()
)
bw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bw.setStatus("current")


class _Bssid_Type(DisplayString):
    """Custom type bssid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Bssid_Type.__name__ = "DisplayString"
_Bssid_Object = MibScalar
bssid = _Bssid_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 3),
    _Bssid_Type()
)
bssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bssid.setStatus("current")


class _Channel_Type(DisplayString):
    """Custom type channel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Channel_Type.__name__ = "DisplayString"
_Channel_Object = MibScalar
channel = _Channel_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 4),
    _Channel_Type()
)
channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channel.setStatus("current")


class _Distance_Type(DisplayString):
    """Custom type distance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Distance_Type.__name__ = "DisplayString"
_Distance_Object = MibScalar
distance = _Distance_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 5),
    _Distance_Type()
)
distance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    distance.setStatus("current")


class _Frequency_Type(DisplayString):
    """Custom type frequency based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Frequency_Type.__name__ = "DisplayString"
_Frequency_Object = MibScalar
frequency = _Frequency_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 6),
    _Frequency_Type()
)
frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frequency.setStatus("current")


class _Ipaddr_Type(DisplayString):
    """Custom type ipaddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Ipaddr_Type.__name__ = "DisplayString"
_Ipaddr_Object = MibScalar
ipaddr = _Ipaddr_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 7),
    _Ipaddr_Type()
)
ipaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddr.setStatus("current")


class _Mcs_Type(DisplayString):
    """Custom type mcs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Mcs_Type.__name__ = "DisplayString"
_Mcs_Object = MibScalar
mcs = _Mcs_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 8),
    _Mcs_Type()
)
mcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcs.setStatus("current")


class _Modulation_Type(DisplayString):
    """Custom type modulation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Modulation_Type.__name__ = "DisplayString"
_Modulation_Object = MibScalar
modulation = _Modulation_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 9),
    _Modulation_Type()
)
modulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulation.setStatus("current")


class _Offbandssid_Type(DisplayString):
    """Custom type offbandssid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Offbandssid_Type.__name__ = "DisplayString"
_Offbandssid_Object = MibScalar
offbandssid = _Offbandssid_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 10),
    _Offbandssid_Type()
)
offbandssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    offbandssid.setStatus("current")


class _Name_Type(DisplayString):
    """Custom type name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Name_Type.__name__ = "DisplayString"
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 11),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("current")


class _Netmask_Type(DisplayString):
    """Custom type netmask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Netmask_Type.__name__ = "DisplayString"
_Netmask_Object = MibScalar
netmask = _Netmask_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 12),
    _Netmask_Type()
)
netmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netmask.setStatus("current")


class _Peermac_Type(DisplayString):
    """Custom type peermac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Peermac_Type.__name__ = "DisplayString"
_Peermac_Object = MibScalar
peermac = _Peermac_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 13),
    _Peermac_Type()
)
peermac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peermac.setStatus("current")


class _Product_Type(DisplayString):
    """Custom type product based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Product_Type.__name__ = "DisplayString"
_Product_Object = MibScalar
product = _Product_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 14),
    _Product_Type()
)
product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    product.setStatus("current")


class _Rfmac_Type(DisplayString):
    """Custom type rfmac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Rfmac_Type.__name__ = "DisplayString"
_Rfmac_Object = MibScalar
rfmac = _Rfmac_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 15),
    _Rfmac_Type()
)
rfmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfmac.setStatus("current")


class _Serial_Type(DisplayString):
    """Custom type serial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Serial_Type.__name__ = "DisplayString"
_Serial_Object = MibScalar
serial = _Serial_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 16),
    _Serial_Type()
)
serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serial.setStatus("current")


class _Ssid_Type(DisplayString):
    """Custom type ssid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Ssid_Type.__name__ = "DisplayString"
_Ssid_Object = MibScalar
ssid = _Ssid_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 17),
    _Ssid_Type()
)
ssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssid.setStatus("current")


class _Sysmode_Type(DisplayString):
    """Custom type sysmode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Sysmode_Type.__name__ = "DisplayString"
_Sysmode_Object = MibScalar
sysmode = _Sysmode_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 18),
    _Sysmode_Type()
)
sysmode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysmode.setStatus("current")


class _Tpcrssi_Type(DisplayString):
    """Custom type tpcrssi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Tpcrssi_Type.__name__ = "DisplayString"
_Tpcrssi_Object = MibScalar
tpcrssi = _Tpcrssi_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 19),
    _Tpcrssi_Type()
)
tpcrssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpcrssi.setStatus("current")


class _Txpower_Type(DisplayString):
    """Custom type txpower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Txpower_Type.__name__ = "DisplayString"
_Txpower_Object = MibScalar
txpower = _Txpower_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 20),
    _Txpower_Type()
)
txpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txpower.setStatus("current")


class _Version_Type(DisplayString):
    """Custom type version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Version_Type.__name__ = "DisplayString"
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 21),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")


class _Vlanid_Type(DisplayString):
    """Custom type vlanid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Vlanid_Type.__name__ = "DisplayString"
_Vlanid_Object = MibScalar
vlanid = _Vlanid_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 22),
    _Vlanid_Type()
)
vlanid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanid.setStatus("current")


class _Rssi_Type(DisplayString):
    """Custom type rssi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Rssi_Type.__name__ = "DisplayString"
_Rssi_Object = MibScalar
rssi = _Rssi_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 23),
    _Rssi_Type()
)
rssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rssi.setStatus("current")


class _Snr_Type(DisplayString):
    """Custom type snr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Snr_Type.__name__ = "DisplayString"
_Snr_Object = MibScalar
snr = _Snr_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 24),
    _Snr_Type()
)
snr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snr.setStatus("current")


class _Location_Type(DisplayString):
    """Custom type location based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Location_Type.__name__ = "DisplayString"
_Location_Object = MibScalar
location = _Location_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 25),
    _Location_Type()
)
location.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    location.setStatus("current")


class _Uptime_Type(DisplayString):
    """Custom type uptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Uptime_Type.__name__ = "DisplayString"
_Uptime_Object = MibScalar
uptime = _Uptime_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 26),
    _Uptime_Type()
)
uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uptime.setStatus("current")


class _Bitrate_Type(DisplayString):
    """Custom type bitrate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Bitrate_Type.__name__ = "DisplayString"
_Bitrate_Object = MibScalar
bitrate = _Bitrate_Object(
    (1, 3, 6, 1, 4, 1, 49969, 8, 1, 20, 6, 27),
    _Bitrate_Type()
)
bitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitrate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIRAMAR-WIRELESS-MIB",
    **{"miramar": miramar,
       "wireless": wireless,
       "mirWirelessMIB": mirWirelessMIB,
       "miramarnet": miramarnet,
       "settings": settings,
       "ccq": ccq,
       "bw": bw,
       "bssid": bssid,
       "channel": channel,
       "distance": distance,
       "frequency": frequency,
       "ipaddr": ipaddr,
       "mcs": mcs,
       "modulation": modulation,
       "offbandssid": offbandssid,
       "name": name,
       "netmask": netmask,
       "peermac": peermac,
       "product": product,
       "rfmac": rfmac,
       "serial": serial,
       "ssid": ssid,
       "sysmode": sysmode,
       "tpcrssi": tpcrssi,
       "txpower": txpower,
       "version": version,
       "vlanid": vlanid,
       "rssi": rssi,
       "snr": snr,
       "location": location,
       "uptime": uptime,
       "bitrate": bitrate}
)

# SNMP MIB module (DIGI-WI-POINT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-WI-POINT-MIB.mib
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

(digiWiPoint,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiWiPoint")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 2)
)


class _TimeZone_Type(Integer32):
    """Custom type timeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-120,
              -110,
              -100,
              -90,
              -80,
              -70,
              -60,
              -50,
              -40,
              -35,
              -30,
              -20,
              -10,
              0,
              10,
              20,
              30,
              40,
              50,
              60,
              70,
              80,
              90,
              100,
              110,
              120)
        )
    )
    namedValues = NamedValues(
        *(("kwajalein", -120),
          ("midwayIslandSamoa", -110),
          ("hawaii", -100),
          ("alaska", -90),
          ("pacificTimeofUSACanada", -80),
          ("arizonaMountainTimeofUSACanada", -70),
          ("mexicoCentralTimeofUSACanada", -60),
          ("indianaEastColombiaPanamaEasternTimeofUSACanada", -50),
          ("boliviaVenezuelaAtlanticTimeofCanadaBrazilWest", -40),
          ("newfoundland", -35),
          ("guyanaBrazilEastGreenland", -30),
          ("midAtlantic", -20),
          ("azores", -10),
          ("gambiaLiberiaMoroccoEngland", 0),
          ("tunisiaFranceGermanyItaly", 10),
          ("southAfricaGreeceUkraineRomaniaTurkey", 20),
          ("iraqJordanKuwait", 30),
          ("armenia", 40),
          ("pakistanRussia", 50),
          ("bangladeshRussia", 60),
          ("thailandRussia", 70),
          ("chinaHongKongAustraliaWesternSingaporeTaiwanRussia", 80),
          ("japanKorea", 90),
          ("guamRussiaAustralia", 100),
          ("solomonIslands", 110),
          ("fijiNewZealand", 120))
    )


_TimeZone_Type.__name__ = "Integer32"
_TimeZone_Object = MibScalar
timeZone = _TimeZone_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 2, 2),
    _TimeZone_Type()
)
timeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeZone.setStatus("current")


class _TimeEnablesummertime_Type(Integer32):
    """Custom type timeEnablesummertime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TimeEnablesummertime_Type.__name__ = "Integer32"
_TimeEnablesummertime_Object = MibScalar
timeEnablesummertime = _TimeEnablesummertime_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 2, 3),
    _TimeEnablesummertime_Type()
)
timeEnablesummertime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeEnablesummertime.setStatus("current")
_TimeNtpserver_Type = IpAddress
_TimeNtpserver_Object = MibScalar
timeNtpserver = _TimeNtpserver_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 2, 4),
    _TimeNtpserver_Type()
)
timeNtpserver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeNtpserver.setStatus("current")


class _LogOutput_Type(Integer32):
    """Custom type logOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sendToWebGUI", 0),
          ("sendToremoteServer", 1),
          ("sendToconsole", 2))
    )


_LogOutput_Type.__name__ = "Integer32"
_LogOutput_Object = MibScalar
logOutput = _LogOutput_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 2, 5),
    _LogOutput_Type()
)
logOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logOutput.setStatus("current")
_LogServer_Type = IpAddress
_LogServer_Object = MibScalar
logServer = _LogServer_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 2, 6),
    _LogServer_Type()
)
logServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logServer.setStatus("current")
_SerialNumber_Type = OctetString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 2, 7),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_MacAddress_Type = OctetString
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 2, 8),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")
_Model_Type = OctetString
_Model_Object = MibScalar
model = _Model_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 2, 9),
    _Model_Type()
)
model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model.setStatus("current")
_FwVersion_Type = OctetString
_FwVersion_Object = MibScalar
fwVersion = _FwVersion_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 2, 10),
    _FwVersion_Type()
)
fwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVersion.setStatus("current")
_Interfaces_ObjectIdentity = ObjectIdentity
interfaces = _Interfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3)
)
_Lan_ObjectIdentity = ObjectIdentity
lan = _Lan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 1)
)
_LanIpaddress_Type = IpAddress
_LanIpaddress_Object = MibScalar
lanIpaddress = _LanIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 1, 1),
    _LanIpaddress_Type()
)
lanIpaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanIpaddress.setStatus("current")
_LanNetmask_Type = IpAddress
_LanNetmask_Object = MibScalar
lanNetmask = _LanNetmask_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 1, 2),
    _LanNetmask_Type()
)
lanNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanNetmask.setStatus("current")
_Wl_ObjectIdentity = ObjectIdentity
wl = _Wl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 1, 3)
)


class _WlSsid_Type(OctetString):
    """Custom type wlSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 63),
    )


_WlSsid_Type.__name__ = "OctetString"
_WlSsid_Object = MibScalar
wlSsid = _WlSsid_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 1, 3, 1),
    _WlSsid_Type()
)
wlSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSsid.setStatus("current")


class _WlClosed_Type(Integer32):
    """Custom type wlClosed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WlClosed_Type.__name__ = "Integer32"
_WlClosed_Object = MibScalar
wlClosed = _WlClosed_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 1, 3, 2),
    _WlClosed_Type()
)
wlClosed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlClosed.setStatus("current")


class _WlChannel_Type(Integer32):
    """Custom type wlChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_WlChannel_Type.__name__ = "Integer32"
_WlChannel_Object = MibScalar
wlChannel = _WlChannel_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 1, 3, 3),
    _WlChannel_Type()
)
wlChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlChannel.setStatus("current")


class _WlGmode_Type(Integer32):
    """Custom type wlGmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("b-only", 0),
          ("mixed", 1),
          ("g-only", 2))
    )


_WlGmode_Type.__name__ = "Integer32"
_WlGmode_Object = MibScalar
wlGmode = _WlGmode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 1, 3, 4),
    _WlGmode_Type()
)
wlGmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlGmode.setStatus("current")


class _WlIsolation_Type(Integer32):
    """Custom type wlIsolation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WlIsolation_Type.__name__ = "Integer32"
_WlIsolation_Object = MibScalar
wlIsolation = _WlIsolation_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 1, 3, 5),
    _WlIsolation_Type()
)
wlIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlIsolation.setStatus("current")


class _WlMaxassociations_Type(Integer32):
    """Custom type wlMaxassociations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_WlMaxassociations_Type.__name__ = "Integer32"
_WlMaxassociations_Object = MibScalar
wlMaxassociations = _WlMaxassociations_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 1, 3, 6),
    _WlMaxassociations_Type()
)
wlMaxassociations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlMaxassociations.setStatus("current")


class _WlSecuritymode_Type(Integer32):
    """Custom type wlSecuritymode based on Integer32"""
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
        *(("disabled", 0),
          ("open-wep", 1),
          ("shared-wep", 2),
          ("wpa-psk-TKIP", 3),
          ("wpa-psk-AES", 4),
          ("wpa-psk-TKIPAES", 5))
    )


_WlSecuritymode_Type.__name__ = "Integer32"
_WlSecuritymode_Object = MibScalar
wlSecuritymode = _WlSecuritymode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 1, 3, 7),
    _WlSecuritymode_Type()
)
wlSecuritymode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecuritymode.setStatus("current")


class _WlRadio_Type(Integer32):
    """Custom type wlRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WlRadio_Type.__name__ = "Integer32"
_WlRadio_Object = MibScalar
wlRadio = _WlRadio_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 1, 3, 14),
    _WlRadio_Type()
)
wlRadio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlRadio.setStatus("current")
_Wan_ObjectIdentity = ObjectIdentity
wan = _Wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 2)
)


class _WanEnable_Type(Integer32):
    """Custom type wanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WanEnable_Type.__name__ = "Integer32"
_WanEnable_Object = MibScalar
wanEnable = _WanEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 2, 1),
    _WanEnable_Type()
)
wanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanEnable.setStatus("current")
_WanIpaddress_Type = IpAddress
_WanIpaddress_Object = MibScalar
wanIpaddress = _WanIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 2, 2),
    _WanIpaddress_Type()
)
wanIpaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanIpaddress.setStatus("current")


class _WanProto_Type(Integer32):
    """Custom type wanProto based on Integer32"""
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
        *(("disabled", 0),
          ("dhcp", 1),
          ("static", 2),
          ("pppoe", 3),
          ("wwan", 4))
    )


_WanProto_Type.__name__ = "Integer32"
_WanProto_Object = MibScalar
wanProto = _WanProto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 2, 3),
    _WanProto_Type()
)
wanProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanProto.setStatus("current")


class _Wankeepalive_Type(Integer32):
    """Custom type wankeepalive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Wankeepalive_Type.__name__ = "Integer32"
_Wankeepalive_Object = MibScalar
wankeepalive = _Wankeepalive_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 2, 6),
    _Wankeepalive_Type()
)
wankeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wankeepalive.setStatus("current")


class _Wankeepaliveinterval_Type(Integer32):
    """Custom type wankeepaliveinterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_Wankeepaliveinterval_Type.__name__ = "Integer32"
_Wankeepaliveinterval_Object = MibScalar
wankeepaliveinterval = _Wankeepaliveinterval_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 2, 7),
    _Wankeepaliveinterval_Type()
)
wankeepaliveinterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wankeepaliveinterval.setStatus("current")


class _WanDialmode_Type(Integer32):
    """Custom type wanDialmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("dialondemand", 2),
          ("manual", 3))
    )


_WanDialmode_Type.__name__ = "Integer32"
_WanDialmode_Object = MibScalar
wanDialmode = _WanDialmode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 2, 8),
    _WanDialmode_Type()
)
wanDialmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDialmode.setStatus("current")


class _WanDialondemandinterval_Type(Integer32):
    """Custom type wanDialondemandinterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 1800),
    )


_WanDialondemandinterval_Type.__name__ = "Integer32"
_WanDialondemandinterval_Object = MibScalar
wanDialondemandinterval = _WanDialondemandinterval_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 2, 9),
    _WanDialondemandinterval_Type()
)
wanDialondemandinterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDialondemandinterval.setStatus("current")
_WanHWDescriptor_Type = OctetString
_WanHWDescriptor_Object = MibScalar
wanHWDescriptor = _WanHWDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 3, 2, 10),
    _WanHWDescriptor_Type()
)
wanHWDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHWDescriptor.setStatus("current")
_NetworkServices_ObjectIdentity = ObjectIdentity
networkServices = _NetworkServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 4)
)
_Http_ObjectIdentity = ObjectIdentity
http = _Http_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 4, 1)
)


class _HttpLanport_Type(Integer32):
    """Custom type httpLanport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HttpLanport_Type.__name__ = "Integer32"
_HttpLanport_Object = MibScalar
httpLanport = _HttpLanport_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 4, 1, 1),
    _HttpLanport_Type()
)
httpLanport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpLanport.setStatus("current")


class _HttpWanport_Type(Integer32):
    """Custom type httpWanport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HttpWanport_Type.__name__ = "Integer32"
_HttpWanport_Object = MibScalar
httpWanport = _HttpWanport_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 4, 1, 2),
    _HttpWanport_Type()
)
httpWanport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpWanport.setStatus("current")


class _HttpWanEnabled_Type(Integer32):
    """Custom type httpWanEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HttpWanEnabled_Type.__name__ = "Integer32"
_HttpWanEnabled_Object = MibScalar
httpWanEnabled = _HttpWanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 4, 1, 5),
    _HttpWanEnabled_Type()
)
httpWanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpWanEnabled.setStatus("current")
_Dhcp_ObjectIdentity = ObjectIdentity
dhcp = _Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 4, 3)
)


class _DhcpEnable_Type(Integer32):
    """Custom type dhcpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DhcpEnable_Type.__name__ = "Integer32"
_DhcpEnable_Object = MibScalar
dhcpEnable = _DhcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 4, 3, 1),
    _DhcpEnable_Type()
)
dhcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpEnable.setStatus("current")
_DhcpStart_Type = IpAddress
_DhcpStart_Object = MibScalar
dhcpStart = _DhcpStart_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 4, 3, 2),
    _DhcpStart_Type()
)
dhcpStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpStart.setStatus("current")
_DhcpEnd_Type = IpAddress
_DhcpEnd_Object = MibScalar
dhcpEnd = _DhcpEnd_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 4, 3, 3),
    _DhcpEnd_Type()
)
dhcpEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpEnd.setStatus("current")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 10)
)
_StatusGlobal_ObjectIdentity = ObjectIdentity
statusGlobal = _StatusGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 10, 1)
)


class _WanStatus_Type(Integer32):
    """Custom type wanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("connecting", 1),
          ("connected", 2))
    )


_WanStatus_Type.__name__ = "Integer32"
_WanStatus_Object = MibScalar
wanStatus = _WanStatus_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 10, 1, 1),
    _WanStatus_Type()
)
wanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanStatus.setStatus("current")
_GpsLocation_Type = OctetString
_GpsLocation_Object = MibScalar
gpsLocation = _GpsLocation_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 10, 1, 2),
    _GpsLocation_Type()
)
gpsLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsLocation.setStatus("current")
_DhcpLease_ObjectIdentity = ObjectIdentity
dhcpLease = _DhcpLease_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 10, 2)
)
_DhcpLeaseNumber_Type = Integer32
_DhcpLeaseNumber_Object = MibScalar
dhcpLeaseNumber = _DhcpLeaseNumber_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 10, 2, 1),
    _DhcpLeaseNumber_Type()
)
dhcpLeaseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseNumber.setStatus("current")
_DhcpLeaseTable_Object = MibTable
dhcpLeaseTable = _DhcpLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 10, 2, 2)
)
if mibBuilder.loadTexts:
    dhcpLeaseTable.setStatus("current")
_DhcpLeaseEntry_Object = MibTableRow
dhcpLeaseEntry = _DhcpLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 10, 2, 2, 1)
)
dhcpLeaseEntry.setIndexNames(
    (0, "DIGI-WI-POINT-MIB", "dhcpLeaseIndex"),
)
if mibBuilder.loadTexts:
    dhcpLeaseEntry.setStatus("current")
_DhcpLeaseIndex_Type = Integer32
_DhcpLeaseIndex_Object = MibTableColumn
dhcpLeaseIndex = _DhcpLeaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 10, 2, 2, 1, 1),
    _DhcpLeaseIndex_Type()
)
dhcpLeaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseIndex.setStatus("current")
_DhcpIPAddress_Type = IpAddress
_DhcpIPAddress_Object = MibTableColumn
dhcpIPAddress = _DhcpIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 10, 2, 2, 1, 2),
    _DhcpIPAddress_Type()
)
dhcpIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpIPAddress.setStatus("current")


class _DhcpMACAddress_Type(OctetString):
    """Custom type dhcpMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_DhcpMACAddress_Type.__name__ = "OctetString"
_DhcpMACAddress_Object = MibTableColumn
dhcpMACAddress = _DhcpMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 10, 2, 2, 1, 3),
    _DhcpMACAddress_Type()
)
dhcpMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpMACAddress.setStatus("current")
_DhcpHostName_Type = OctetString
_DhcpHostName_Object = MibTableColumn
dhcpHostName = _DhcpHostName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 10, 2, 2, 1, 4),
    _DhcpHostName_Type()
)
dhcpHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpHostName.setStatus("current")
_DhcpRemainingTime_Type = TimeTicks
_DhcpRemainingTime_Object = MibTableColumn
dhcpRemainingTime = _DhcpRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 9, 1, 10, 2, 2, 1, 5),
    _DhcpRemainingTime_Type()
)
dhcpRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRemainingTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-WI-POINT-MIB",
    **{"general": general,
       "system": system,
       "timeZone": timeZone,
       "timeEnablesummertime": timeEnablesummertime,
       "timeNtpserver": timeNtpserver,
       "logOutput": logOutput,
       "logServer": logServer,
       "serialNumber": serialNumber,
       "macAddress": macAddress,
       "model": model,
       "fwVersion": fwVersion,
       "interfaces": interfaces,
       "lan": lan,
       "lanIpaddress": lanIpaddress,
       "lanNetmask": lanNetmask,
       "wl": wl,
       "wlSsid": wlSsid,
       "wlClosed": wlClosed,
       "wlChannel": wlChannel,
       "wlGmode": wlGmode,
       "wlIsolation": wlIsolation,
       "wlMaxassociations": wlMaxassociations,
       "wlSecuritymode": wlSecuritymode,
       "wlRadio": wlRadio,
       "wan": wan,
       "wanEnable": wanEnable,
       "wanIpaddress": wanIpaddress,
       "wanProto": wanProto,
       "wankeepalive": wankeepalive,
       "wankeepaliveinterval": wankeepaliveinterval,
       "wanDialmode": wanDialmode,
       "wanDialondemandinterval": wanDialondemandinterval,
       "wanHWDescriptor": wanHWDescriptor,
       "networkServices": networkServices,
       "http": http,
       "httpLanport": httpLanport,
       "httpWanport": httpWanport,
       "httpWanEnabled": httpWanEnabled,
       "dhcp": dhcp,
       "dhcpEnable": dhcpEnable,
       "dhcpStart": dhcpStart,
       "dhcpEnd": dhcpEnd,
       "status": status,
       "statusGlobal": statusGlobal,
       "wanStatus": wanStatus,
       "gpsLocation": gpsLocation,
       "dhcpLease": dhcpLease,
       "dhcpLeaseNumber": dhcpLeaseNumber,
       "dhcpLeaseTable": dhcpLeaseTable,
       "dhcpLeaseEntry": dhcpLeaseEntry,
       "dhcpLeaseIndex": dhcpLeaseIndex,
       "dhcpIPAddress": dhcpIPAddress,
       "dhcpMACAddress": dhcpMACAddress,
       "dhcpHostName": dhcpHostName,
       "dhcpRemainingTime": dhcpRemainingTime}
)

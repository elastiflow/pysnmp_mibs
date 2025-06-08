# SNMP MIB module (RTCPXR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/RTCPXR-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 15:01:16 2025
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

rtcpXrMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 255)
)
if mibBuilder.loadTexts:
    rtcpXrMIB.setRevisions(
        ("2005-02-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LeveldB(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-120, 120),
        ValueRangeConstraint(127, 127),
    )



class Rfactor(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
        ValueRangeConstraint(127, 127),
    )



class ScaledMOSscore(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 50),
        ValueRangeConstraint(127, 127),
    )



class Percentage(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs

_RtcpXrMIBObjects_ObjectIdentity = ObjectIdentity
rtcpXrMIBObjects = _RtcpXrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 255, 1)
)
_RtcpXrSessionIDTable_Object = MibTable
rtcpXrSessionIDTable = _RtcpXrSessionIDTable_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1)
)
if mibBuilder.loadTexts:
    rtcpXrSessionIDTable.setStatus("current")
_RtcpXrSessionIDEntry_Object = MibTableRow
rtcpXrSessionIDEntry = _RtcpXrSessionIDEntry_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1)
)
rtcpXrSessionIDEntry.setIndexNames(
    (0, "RTCPXR-MIB", "rtcpXrSessionIDIndex"),
)
if mibBuilder.loadTexts:
    rtcpXrSessionIDEntry.setStatus("current")


class _RtcpXrSessionIDIndex_Type(Unsigned32):
    """Custom type rtcpXrSessionIDIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RtcpXrSessionIDIndex_Type.__name__ = "Unsigned32"
_RtcpXrSessionIDIndex_Object = MibTableColumn
rtcpXrSessionIDIndex = _RtcpXrSessionIDIndex_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1, 1),
    _RtcpXrSessionIDIndex_Type()
)
rtcpXrSessionIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtcpXrSessionIDIndex.setStatus("current")


class _RtcpXrSessionIDSessionIdentifier_Type(OctetString):
    """Custom type rtcpXrSessionIDSessionIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RtcpXrSessionIDSessionIdentifier_Type.__name__ = "OctetString"
_RtcpXrSessionIDSessionIdentifier_Object = MibTableColumn
rtcpXrSessionIDSessionIdentifier = _RtcpXrSessionIDSessionIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1, 2),
    _RtcpXrSessionIDSessionIdentifier_Type()
)
rtcpXrSessionIDSessionIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrSessionIDSessionIdentifier.setStatus("current")
_RtcpXrSessionIDCallStartTime_Type = TimeStamp
_RtcpXrSessionIDCallStartTime_Object = MibTableColumn
rtcpXrSessionIDCallStartTime = _RtcpXrSessionIDCallStartTime_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1, 3),
    _RtcpXrSessionIDCallStartTime_Type()
)
rtcpXrSessionIDCallStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrSessionIDCallStartTime.setStatus("current")
_RtcpXrSessionIDCallStopTime_Type = TimeStamp
_RtcpXrSessionIDCallStopTime_Object = MibTableColumn
rtcpXrSessionIDCallStopTime = _RtcpXrSessionIDCallStopTime_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1, 4),
    _RtcpXrSessionIDCallStopTime_Type()
)
rtcpXrSessionIDCallStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrSessionIDCallStopTime.setStatus("current")
_RtcpXrSessionIDSourceIPtype_Type = InetAddressType
_RtcpXrSessionIDSourceIPtype_Object = MibTableColumn
rtcpXrSessionIDSourceIPtype = _RtcpXrSessionIDSourceIPtype_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1, 5),
    _RtcpXrSessionIDSourceIPtype_Type()
)
rtcpXrSessionIDSourceIPtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrSessionIDSourceIPtype.setStatus("current")
_RtcpXrSessionIDSourceIPaddress_Type = InetAddress
_RtcpXrSessionIDSourceIPaddress_Object = MibTableColumn
rtcpXrSessionIDSourceIPaddress = _RtcpXrSessionIDSourceIPaddress_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1, 6),
    _RtcpXrSessionIDSourceIPaddress_Type()
)
rtcpXrSessionIDSourceIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrSessionIDSourceIPaddress.setStatus("current")
_RtcpXrSessionIDSourceRTPport_Type = InetPortNumber
_RtcpXrSessionIDSourceRTPport_Object = MibTableColumn
rtcpXrSessionIDSourceRTPport = _RtcpXrSessionIDSourceRTPport_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1, 7),
    _RtcpXrSessionIDSourceRTPport_Type()
)
rtcpXrSessionIDSourceRTPport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrSessionIDSourceRTPport.setStatus("current")
_RtcpXrSessionIDSourceRTCPport_Type = InetPortNumber
_RtcpXrSessionIDSourceRTCPport_Object = MibTableColumn
rtcpXrSessionIDSourceRTCPport = _RtcpXrSessionIDSourceRTCPport_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1, 8),
    _RtcpXrSessionIDSourceRTCPport_Type()
)
rtcpXrSessionIDSourceRTCPport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrSessionIDSourceRTCPport.setStatus("current")
_RtcpXrSessionIDDestIPtype_Type = InetAddressType
_RtcpXrSessionIDDestIPtype_Object = MibTableColumn
rtcpXrSessionIDDestIPtype = _RtcpXrSessionIDDestIPtype_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1, 9),
    _RtcpXrSessionIDDestIPtype_Type()
)
rtcpXrSessionIDDestIPtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrSessionIDDestIPtype.setStatus("current")
_RtcpXrSessionIDDestIPaddress_Type = InetAddress
_RtcpXrSessionIDDestIPaddress_Object = MibTableColumn
rtcpXrSessionIDDestIPaddress = _RtcpXrSessionIDDestIPaddress_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1, 10),
    _RtcpXrSessionIDDestIPaddress_Type()
)
rtcpXrSessionIDDestIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrSessionIDDestIPaddress.setStatus("current")
_RtcpXrSessionIDDestRTPport_Type = InetPortNumber
_RtcpXrSessionIDDestRTPport_Object = MibTableColumn
rtcpXrSessionIDDestRTPport = _RtcpXrSessionIDDestRTPport_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1, 11),
    _RtcpXrSessionIDDestRTPport_Type()
)
rtcpXrSessionIDDestRTPport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrSessionIDDestRTPport.setStatus("current")
_RtcpXrSessionIDDestRTCPport_Type = InetPortNumber
_RtcpXrSessionIDDestRTCPport_Object = MibTableColumn
rtcpXrSessionIDDestRTCPport = _RtcpXrSessionIDDestRTCPport_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1, 12),
    _RtcpXrSessionIDDestRTCPport_Type()
)
rtcpXrSessionIDDestRTCPport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrSessionIDDestRTCPport.setStatus("current")


class _RtcpXrSessionIDSrceIdenType_Type(Integer32):
    """Custom type rtcpXrSessionIDSrceIdenType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dialedNumber", 1),
          ("urlID", 2),
          ("other", 3))
    )


_RtcpXrSessionIDSrceIdenType_Type.__name__ = "Integer32"
_RtcpXrSessionIDSrceIdenType_Object = MibTableColumn
rtcpXrSessionIDSrceIdenType = _RtcpXrSessionIDSrceIdenType_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1, 13),
    _RtcpXrSessionIDSrceIdenType_Type()
)
rtcpXrSessionIDSrceIdenType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrSessionIDSrceIdenType.setStatus("current")


class _RtcpXrSessionIDSrceIdentifier_Type(OctetString):
    """Custom type rtcpXrSessionIDSrceIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RtcpXrSessionIDSrceIdentifier_Type.__name__ = "OctetString"
_RtcpXrSessionIDSrceIdentifier_Object = MibTableColumn
rtcpXrSessionIDSrceIdentifier = _RtcpXrSessionIDSrceIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1, 14),
    _RtcpXrSessionIDSrceIdentifier_Type()
)
rtcpXrSessionIDSrceIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrSessionIDSrceIdentifier.setStatus("current")


class _RtcpXrSessionIDDestIdenType_Type(Integer32):
    """Custom type rtcpXrSessionIDDestIdenType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dialedNumber", 1),
          ("urlID", 2),
          ("other", 3))
    )


_RtcpXrSessionIDDestIdenType_Type.__name__ = "Integer32"
_RtcpXrSessionIDDestIdenType_Object = MibTableColumn
rtcpXrSessionIDDestIdenType = _RtcpXrSessionIDDestIdenType_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1, 15),
    _RtcpXrSessionIDDestIdenType_Type()
)
rtcpXrSessionIDDestIdenType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrSessionIDDestIdenType.setStatus("current")


class _RtcpXrSessionIDDestIdentifier_Type(OctetString):
    """Custom type rtcpXrSessionIDDestIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RtcpXrSessionIDDestIdentifier_Type.__name__ = "OctetString"
_RtcpXrSessionIDDestIdentifier_Object = MibTableColumn
rtcpXrSessionIDDestIdentifier = _RtcpXrSessionIDDestIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1, 16),
    _RtcpXrSessionIDDestIdentifier_Type()
)
rtcpXrSessionIDDestIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrSessionIDDestIdentifier.setStatus("current")


class _RtcpXrSessionIDMeasurePt_Type(Integer32):
    """Custom type rtcpXrSessionIDMeasurePt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localEndpoint", 1),
          ("remoteEndpoint", 2),
          ("midStream", 3))
    )


_RtcpXrSessionIDMeasurePt_Type.__name__ = "Integer32"
_RtcpXrSessionIDMeasurePt_Object = MibTableColumn
rtcpXrSessionIDMeasurePt = _RtcpXrSessionIDMeasurePt_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1, 17),
    _RtcpXrSessionIDMeasurePt_Type()
)
rtcpXrSessionIDMeasurePt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrSessionIDMeasurePt.setStatus("current")


class _RtcpXrSessionIDMeasurePtID_Type(OctetString):
    """Custom type rtcpXrSessionIDMeasurePtID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RtcpXrSessionIDMeasurePtID_Type.__name__ = "OctetString"
_RtcpXrSessionIDMeasurePtID_Object = MibTableColumn
rtcpXrSessionIDMeasurePtID = _RtcpXrSessionIDMeasurePtID_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1, 18),
    _RtcpXrSessionIDMeasurePtID_Type()
)
rtcpXrSessionIDMeasurePtID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrSessionIDMeasurePtID.setStatus("current")
_RtcpXrSessionIDReverseSession_Type = RowPointer
_RtcpXrSessionIDReverseSession_Object = MibTableColumn
rtcpXrSessionIDReverseSession = _RtcpXrSessionIDReverseSession_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1, 19),
    _RtcpXrSessionIDReverseSession_Type()
)
rtcpXrSessionIDReverseSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrSessionIDReverseSession.setStatus("current")
_RtcpXrSessionIDAltMeasurePt_Type = RowPointer
_RtcpXrSessionIDAltMeasurePt_Object = MibTableColumn
rtcpXrSessionIDAltMeasurePt = _RtcpXrSessionIDAltMeasurePt_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 1, 1, 20),
    _RtcpXrSessionIDAltMeasurePt_Type()
)
rtcpXrSessionIDAltMeasurePt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrSessionIDAltMeasurePt.setStatus("current")
_RtcpXrBaseParamTable_Object = MibTable
rtcpXrBaseParamTable = _RtcpXrBaseParamTable_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2)
)
if mibBuilder.loadTexts:
    rtcpXrBaseParamTable.setStatus("current")
_RtcpXrBaseParamEntry_Object = MibTableRow
rtcpXrBaseParamEntry = _RtcpXrBaseParamEntry_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1)
)
rtcpXrBaseParamEntry.setIndexNames(
    (0, "RTCPXR-MIB", "rtcpXrSessionIDIndex"),
)
if mibBuilder.loadTexts:
    rtcpXrBaseParamEntry.setStatus("current")


class _RtcpXrBaseParamVocoderType_Type(OctetString):
    """Custom type rtcpXrBaseParamVocoderType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RtcpXrBaseParamVocoderType_Type.__name__ = "OctetString"
_RtcpXrBaseParamVocoderType_Object = MibTableColumn
rtcpXrBaseParamVocoderType = _RtcpXrBaseParamVocoderType_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1, 1),
    _RtcpXrBaseParamVocoderType_Type()
)
rtcpXrBaseParamVocoderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrBaseParamVocoderType.setStatus("current")
_RtcpXrBaseParamVocoderRate_Type = Unsigned32
_RtcpXrBaseParamVocoderRate_Object = MibTableColumn
rtcpXrBaseParamVocoderRate = _RtcpXrBaseParamVocoderRate_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1, 2),
    _RtcpXrBaseParamVocoderRate_Type()
)
rtcpXrBaseParamVocoderRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrBaseParamVocoderRate.setStatus("current")


class _RtcpXrBaseParamFrameDuration_Type(Unsigned32):
    """Custom type rtcpXrBaseParamFrameDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_RtcpXrBaseParamFrameDuration_Type.__name__ = "Unsigned32"
_RtcpXrBaseParamFrameDuration_Object = MibTableColumn
rtcpXrBaseParamFrameDuration = _RtcpXrBaseParamFrameDuration_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1, 3),
    _RtcpXrBaseParamFrameDuration_Type()
)
rtcpXrBaseParamFrameDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrBaseParamFrameDuration.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrBaseParamFrameDuration.setUnits("sample clock ticks")


class _RtcpXrBaseParamSampleRate_Type(Unsigned32):
    """Custom type rtcpXrBaseParamSampleRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_RtcpXrBaseParamSampleRate_Type.__name__ = "Unsigned32"
_RtcpXrBaseParamSampleRate_Object = MibTableColumn
rtcpXrBaseParamSampleRate = _RtcpXrBaseParamSampleRate_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1, 4),
    _RtcpXrBaseParamSampleRate_Type()
)
rtcpXrBaseParamSampleRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrBaseParamSampleRate.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrBaseParamSampleRate.setUnits("samples per second")
_RtcpXrBaseParamDurationMs_Type = Counter32
_RtcpXrBaseParamDurationMs_Object = MibTableColumn
rtcpXrBaseParamDurationMs = _RtcpXrBaseParamDurationMs_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1, 5),
    _RtcpXrBaseParamDurationMs_Type()
)
rtcpXrBaseParamDurationMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrBaseParamDurationMs.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrBaseParamDurationMs.setUnits("milliseconds")
_RtcpXrBaseParamNetworkLossRate_Type = Percentage
_RtcpXrBaseParamNetworkLossRate_Object = MibTableColumn
rtcpXrBaseParamNetworkLossRate = _RtcpXrBaseParamNetworkLossRate_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1, 6),
    _RtcpXrBaseParamNetworkLossRate_Type()
)
rtcpXrBaseParamNetworkLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrBaseParamNetworkLossRate.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrBaseParamNetworkLossRate.setUnits("percent")
_RtcpXrBaseParamAvgDiscardRate_Type = Percentage
_RtcpXrBaseParamAvgDiscardRate_Object = MibTableColumn
rtcpXrBaseParamAvgDiscardRate = _RtcpXrBaseParamAvgDiscardRate_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1, 7),
    _RtcpXrBaseParamAvgDiscardRate_Type()
)
rtcpXrBaseParamAvgDiscardRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrBaseParamAvgDiscardRate.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrBaseParamAvgDiscardRate.setUnits("percent")
_RtcpXrBaseParamBurstLossDensity_Type = Percentage
_RtcpXrBaseParamBurstLossDensity_Object = MibTableColumn
rtcpXrBaseParamBurstLossDensity = _RtcpXrBaseParamBurstLossDensity_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1, 8),
    _RtcpXrBaseParamBurstLossDensity_Type()
)
rtcpXrBaseParamBurstLossDensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrBaseParamBurstLossDensity.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrBaseParamBurstLossDensity.setUnits("percent")
_RtcpXrBaseParamBurstLenMs_Type = Gauge32
_RtcpXrBaseParamBurstLenMs_Object = MibTableColumn
rtcpXrBaseParamBurstLenMs = _RtcpXrBaseParamBurstLenMs_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1, 9),
    _RtcpXrBaseParamBurstLenMs_Type()
)
rtcpXrBaseParamBurstLenMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrBaseParamBurstLenMs.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrBaseParamBurstLenMs.setUnits("milliseconds")
_RtcpXrBaseParamGapLossDensity_Type = Percentage
_RtcpXrBaseParamGapLossDensity_Object = MibTableColumn
rtcpXrBaseParamGapLossDensity = _RtcpXrBaseParamGapLossDensity_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1, 10),
    _RtcpXrBaseParamGapLossDensity_Type()
)
rtcpXrBaseParamGapLossDensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrBaseParamGapLossDensity.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrBaseParamGapLossDensity.setUnits("percent")
_RtcpXrBaseParamGapLenMs_Type = Gauge32
_RtcpXrBaseParamGapLenMs_Object = MibTableColumn
rtcpXrBaseParamGapLenMs = _RtcpXrBaseParamGapLenMs_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1, 11),
    _RtcpXrBaseParamGapLenMs_Type()
)
rtcpXrBaseParamGapLenMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrBaseParamGapLenMs.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrBaseParamGapLenMs.setUnits("milliseconds")
_RtcpXrBaseParamAvgOWDelay_Type = Gauge32
_RtcpXrBaseParamAvgOWDelay_Object = MibTableColumn
rtcpXrBaseParamAvgOWDelay = _RtcpXrBaseParamAvgOWDelay_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1, 12),
    _RtcpXrBaseParamAvgOWDelay_Type()
)
rtcpXrBaseParamAvgOWDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrBaseParamAvgOWDelay.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrBaseParamAvgOWDelay.setUnits("milliseconds")
_RtcpXrBaseParamAvgEndSysDelay_Type = Gauge32
_RtcpXrBaseParamAvgEndSysDelay_Object = MibTableColumn
rtcpXrBaseParamAvgEndSysDelay = _RtcpXrBaseParamAvgEndSysDelay_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1, 13),
    _RtcpXrBaseParamAvgEndSysDelay_Type()
)
rtcpXrBaseParamAvgEndSysDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrBaseParamAvgEndSysDelay.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrBaseParamAvgEndSysDelay.setUnits("milliseconds")


class _RtcpXrBaseParamPlcType_Type(Integer32):
    """Custom type rtcpXrBaseParamPlcType based on Integer32"""
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
        *(("disabled", 1),
          ("enhanced", 2),
          ("standard", 3),
          ("unspecified", 4))
    )


_RtcpXrBaseParamPlcType_Type.__name__ = "Integer32"
_RtcpXrBaseParamPlcType_Object = MibTableColumn
rtcpXrBaseParamPlcType = _RtcpXrBaseParamPlcType_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1, 14),
    _RtcpXrBaseParamPlcType_Type()
)
rtcpXrBaseParamPlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrBaseParamPlcType.setStatus("current")


class _RtcpXrBaseParamJBuffAdaptMode_Type(Integer32):
    """Custom type rtcpXrBaseParamJBuffAdaptMode based on Integer32"""
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
        *(("reserved", 1),
          ("nonAdaptive", 2),
          ("adaptive", 3),
          ("unknown", 4))
    )


_RtcpXrBaseParamJBuffAdaptMode_Type.__name__ = "Integer32"
_RtcpXrBaseParamJBuffAdaptMode_Object = MibTableColumn
rtcpXrBaseParamJBuffAdaptMode = _RtcpXrBaseParamJBuffAdaptMode_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1, 15),
    _RtcpXrBaseParamJBuffAdaptMode_Type()
)
rtcpXrBaseParamJBuffAdaptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrBaseParamJBuffAdaptMode.setStatus("current")


class _RtcpXrBaseParamJBuffAdaptRate_Type(Unsigned32):
    """Custom type rtcpXrBaseParamJBuffAdaptRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RtcpXrBaseParamJBuffAdaptRate_Type.__name__ = "Unsigned32"
_RtcpXrBaseParamJBuffAdaptRate_Object = MibTableColumn
rtcpXrBaseParamJBuffAdaptRate = _RtcpXrBaseParamJBuffAdaptRate_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1, 16),
    _RtcpXrBaseParamJBuffAdaptRate_Type()
)
rtcpXrBaseParamJBuffAdaptRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrBaseParamJBuffAdaptRate.setStatus("current")
_RtcpXrBaseParamJBuffAverageDelay_Type = Gauge32
_RtcpXrBaseParamJBuffAverageDelay_Object = MibTableColumn
rtcpXrBaseParamJBuffAverageDelay = _RtcpXrBaseParamJBuffAverageDelay_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1, 17),
    _RtcpXrBaseParamJBuffAverageDelay_Type()
)
rtcpXrBaseParamJBuffAverageDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrBaseParamJBuffAverageDelay.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrBaseParamJBuffAverageDelay.setUnits("milliseconds")
_RtcpXrBaseParamJBuffMaximumDelay_Type = Gauge32
_RtcpXrBaseParamJBuffMaximumDelay_Object = MibTableColumn
rtcpXrBaseParamJBuffMaximumDelay = _RtcpXrBaseParamJBuffMaximumDelay_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1, 18),
    _RtcpXrBaseParamJBuffMaximumDelay_Type()
)
rtcpXrBaseParamJBuffMaximumDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrBaseParamJBuffMaximumDelay.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrBaseParamJBuffMaximumDelay.setUnits("milliseconds")
_RtcpXrBaseParamJBuffAbsMaxDelay_Type = Gauge32
_RtcpXrBaseParamJBuffAbsMaxDelay_Object = MibTableColumn
rtcpXrBaseParamJBuffAbsMaxDelay = _RtcpXrBaseParamJBuffAbsMaxDelay_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1, 19),
    _RtcpXrBaseParamJBuffAbsMaxDelay_Type()
)
rtcpXrBaseParamJBuffAbsMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrBaseParamJBuffAbsMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrBaseParamJBuffAbsMaxDelay.setUnits("milliseconds")
_RtcpXrBaseParamJitterLevel_Type = Gauge32
_RtcpXrBaseParamJitterLevel_Object = MibTableColumn
rtcpXrBaseParamJitterLevel = _RtcpXrBaseParamJitterLevel_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 2, 1, 20),
    _RtcpXrBaseParamJitterLevel_Type()
)
rtcpXrBaseParamJitterLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrBaseParamJitterLevel.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrBaseParamJitterLevel.setUnits("milliseconds")
_RtcpXrCallQualityTable_Object = MibTable
rtcpXrCallQualityTable = _RtcpXrCallQualityTable_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 3)
)
if mibBuilder.loadTexts:
    rtcpXrCallQualityTable.setStatus("current")
_RtcpXrCallQualityEntry_Object = MibTableRow
rtcpXrCallQualityEntry = _RtcpXrCallQualityEntry_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 3, 1)
)
rtcpXrCallQualityEntry.setIndexNames(
    (0, "RTCPXR-MIB", "rtcpXrSessionIDIndex"),
)
if mibBuilder.loadTexts:
    rtcpXrCallQualityEntry.setStatus("current")
_RtcpXrCallQualityNoiseLeveldBm_Type = LeveldB
_RtcpXrCallQualityNoiseLeveldBm_Object = MibTableColumn
rtcpXrCallQualityNoiseLeveldBm = _RtcpXrCallQualityNoiseLeveldBm_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 3, 1, 1),
    _RtcpXrCallQualityNoiseLeveldBm_Type()
)
rtcpXrCallQualityNoiseLeveldBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrCallQualityNoiseLeveldBm.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrCallQualityNoiseLeveldBm.setUnits("dBm0")
_RtcpXrCallQualitySignalLeveldBm_Type = LeveldB
_RtcpXrCallQualitySignalLeveldBm_Object = MibTableColumn
rtcpXrCallQualitySignalLeveldBm = _RtcpXrCallQualitySignalLeveldBm_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 3, 1, 2),
    _RtcpXrCallQualitySignalLeveldBm_Type()
)
rtcpXrCallQualitySignalLeveldBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrCallQualitySignalLeveldBm.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrCallQualitySignalLeveldBm.setUnits("dBm0")
_RtcpXrCallQualityLocalRERLdB_Type = LeveldB
_RtcpXrCallQualityLocalRERLdB_Object = MibTableColumn
rtcpXrCallQualityLocalRERLdB = _RtcpXrCallQualityLocalRERLdB_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 3, 1, 3),
    _RtcpXrCallQualityLocalRERLdB_Type()
)
rtcpXrCallQualityLocalRERLdB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrCallQualityLocalRERLdB.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrCallQualityLocalRERLdB.setUnits("dBm")
_RtcpXrCallQualityRemoteRERLdB_Type = LeveldB
_RtcpXrCallQualityRemoteRERLdB_Object = MibTableColumn
rtcpXrCallQualityRemoteRERLdB = _RtcpXrCallQualityRemoteRERLdB_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 3, 1, 4),
    _RtcpXrCallQualityRemoteRERLdB_Type()
)
rtcpXrCallQualityRemoteRERLdB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrCallQualityRemoteRERLdB.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrCallQualityRemoteRERLdB.setUnits("dBm")
_RtcpXrCallQualityRCQ_Type = Rfactor
_RtcpXrCallQualityRCQ_Object = MibTableColumn
rtcpXrCallQualityRCQ = _RtcpXrCallQualityRCQ_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 3, 1, 5),
    _RtcpXrCallQualityRCQ_Type()
)
rtcpXrCallQualityRCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrCallQualityRCQ.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrCallQualityRCQ.setUnits("R factor")
_RtcpXrCallQualityRLQ_Type = Rfactor
_RtcpXrCallQualityRLQ_Object = MibTableColumn
rtcpXrCallQualityRLQ = _RtcpXrCallQualityRLQ_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 3, 1, 6),
    _RtcpXrCallQualityRLQ_Type()
)
rtcpXrCallQualityRLQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrCallQualityRLQ.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrCallQualityRLQ.setUnits("R factor")
_RtcpXrCallQualityExternalRCQ_Type = Rfactor
_RtcpXrCallQualityExternalRCQ_Object = MibTableColumn
rtcpXrCallQualityExternalRCQ = _RtcpXrCallQualityExternalRCQ_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 3, 1, 7),
    _RtcpXrCallQualityExternalRCQ_Type()
)
rtcpXrCallQualityExternalRCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrCallQualityExternalRCQ.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrCallQualityExternalRCQ.setUnits("R factor")
_RtcpXrCallQualityMOSCQ_Type = ScaledMOSscore
_RtcpXrCallQualityMOSCQ_Object = MibTableColumn
rtcpXrCallQualityMOSCQ = _RtcpXrCallQualityMOSCQ_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 3, 1, 8),
    _RtcpXrCallQualityMOSCQ_Type()
)
rtcpXrCallQualityMOSCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrCallQualityMOSCQ.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrCallQualityMOSCQ.setUnits("MOS x 10")
_RtcpXrCallQualityMOSLQ_Type = ScaledMOSscore
_RtcpXrCallQualityMOSLQ_Object = MibTableColumn
rtcpXrCallQualityMOSLQ = _RtcpXrCallQualityMOSLQ_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 3, 1, 9),
    _RtcpXrCallQualityMOSLQ_Type()
)
rtcpXrCallQualityMOSLQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrCallQualityMOSLQ.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrCallQualityMOSLQ.setUnits("MOS x 10")


class _RtcpXrCallQualityAlgorithm_Type(OctetString):
    """Custom type rtcpXrCallQualityAlgorithm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RtcpXrCallQualityAlgorithm_Type.__name__ = "OctetString"
_RtcpXrCallQualityAlgorithm_Object = MibTableColumn
rtcpXrCallQualityAlgorithm = _RtcpXrCallQualityAlgorithm_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 3, 1, 10),
    _RtcpXrCallQualityAlgorithm_Type()
)
rtcpXrCallQualityAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrCallQualityAlgorithm.setStatus("current")
_RtcpXrHistoryTable_Object = MibTable
rtcpXrHistoryTable = _RtcpXrHistoryTable_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4)
)
if mibBuilder.loadTexts:
    rtcpXrHistoryTable.setStatus("current")
_RtcpXrHistoryEntry_Object = MibTableRow
rtcpXrHistoryEntry = _RtcpXrHistoryEntry_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1)
)
rtcpXrHistoryEntry.setIndexNames(
    (0, "RTCPXR-MIB", "rtcpXrHistoryIndex"),
)
if mibBuilder.loadTexts:
    rtcpXrHistoryEntry.setStatus("current")


class _RtcpXrHistoryIndex_Type(Unsigned32):
    """Custom type rtcpXrHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RtcpXrHistoryIndex_Type.__name__ = "Unsigned32"
_RtcpXrHistoryIndex_Object = MibTableColumn
rtcpXrHistoryIndex = _RtcpXrHistoryIndex_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 1),
    _RtcpXrHistoryIndex_Type()
)
rtcpXrHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtcpXrHistoryIndex.setStatus("current")


class _RtcpXrHistoryGroupName_Type(OctetString):
    """Custom type rtcpXrHistoryGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RtcpXrHistoryGroupName_Type.__name__ = "OctetString"
_RtcpXrHistoryGroupName_Object = MibTableColumn
rtcpXrHistoryGroupName = _RtcpXrHistoryGroupName_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 2),
    _RtcpXrHistoryGroupName_Type()
)
rtcpXrHistoryGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryGroupName.setStatus("current")
_RtcpXrHistoryStartTime_Type = TimeStamp
_RtcpXrHistoryStartTime_Object = MibTableColumn
rtcpXrHistoryStartTime = _RtcpXrHistoryStartTime_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 3),
    _RtcpXrHistoryStartTime_Type()
)
rtcpXrHistoryStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryStartTime.setStatus("current")
_RtcpXrHistoryStopTime_Type = TimeStamp
_RtcpXrHistoryStopTime_Object = MibTableColumn
rtcpXrHistoryStopTime = _RtcpXrHistoryStopTime_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 4),
    _RtcpXrHistoryStopTime_Type()
)
rtcpXrHistoryStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryStopTime.setStatus("current")
_RtcpXrHistoryNumOfSessions_Type = Counter32
_RtcpXrHistoryNumOfSessions_Object = MibTableColumn
rtcpXrHistoryNumOfSessions = _RtcpXrHistoryNumOfSessions_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 5),
    _RtcpXrHistoryNumOfSessions_Type()
)
rtcpXrHistoryNumOfSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryNumOfSessions.setStatus("current")
_RtcpXrHistoryMinDurationMs_Type = Gauge32
_RtcpXrHistoryMinDurationMs_Object = MibTableColumn
rtcpXrHistoryMinDurationMs = _RtcpXrHistoryMinDurationMs_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 6),
    _RtcpXrHistoryMinDurationMs_Type()
)
rtcpXrHistoryMinDurationMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinDurationMs.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinDurationMs.setUnits("milliseconds")
_RtcpXrHistoryMaxDurationMs_Type = Gauge32
_RtcpXrHistoryMaxDurationMs_Object = MibTableColumn
rtcpXrHistoryMaxDurationMs = _RtcpXrHistoryMaxDurationMs_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 7),
    _RtcpXrHistoryMaxDurationMs_Type()
)
rtcpXrHistoryMaxDurationMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxDurationMs.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxDurationMs.setUnits("milliseconds")
_RtcpXrHistoryAvgDurationMs_Type = Gauge32
_RtcpXrHistoryAvgDurationMs_Object = MibTableColumn
rtcpXrHistoryAvgDurationMs = _RtcpXrHistoryAvgDurationMs_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 8),
    _RtcpXrHistoryAvgDurationMs_Type()
)
rtcpXrHistoryAvgDurationMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgDurationMs.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgDurationMs.setUnits("milliseconds")
_RtcpXrHistoryMaxNetworkLossRate_Type = Percentage
_RtcpXrHistoryMaxNetworkLossRate_Object = MibTableColumn
rtcpXrHistoryMaxNetworkLossRate = _RtcpXrHistoryMaxNetworkLossRate_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 9),
    _RtcpXrHistoryMaxNetworkLossRate_Type()
)
rtcpXrHistoryMaxNetworkLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxNetworkLossRate.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxNetworkLossRate.setUnits("percent")
_RtcpXrHistoryAvgNetworkLossRate_Type = Percentage
_RtcpXrHistoryAvgNetworkLossRate_Object = MibTableColumn
rtcpXrHistoryAvgNetworkLossRate = _RtcpXrHistoryAvgNetworkLossRate_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 10),
    _RtcpXrHistoryAvgNetworkLossRate_Type()
)
rtcpXrHistoryAvgNetworkLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgNetworkLossRate.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgNetworkLossRate.setUnits("percent")
_RtcpXrHistoryMaxDiscardRate_Type = Percentage
_RtcpXrHistoryMaxDiscardRate_Object = MibTableColumn
rtcpXrHistoryMaxDiscardRate = _RtcpXrHistoryMaxDiscardRate_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 11),
    _RtcpXrHistoryMaxDiscardRate_Type()
)
rtcpXrHistoryMaxDiscardRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxDiscardRate.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxDiscardRate.setUnits("percent")
_RtcpXrHistoryAvgDiscardRate_Type = Percentage
_RtcpXrHistoryAvgDiscardRate_Object = MibTableColumn
rtcpXrHistoryAvgDiscardRate = _RtcpXrHistoryAvgDiscardRate_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 12),
    _RtcpXrHistoryAvgDiscardRate_Type()
)
rtcpXrHistoryAvgDiscardRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgDiscardRate.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgDiscardRate.setUnits("percent")
_RtcpXrHistoryMaxBurstLossDensity_Type = Percentage
_RtcpXrHistoryMaxBurstLossDensity_Object = MibTableColumn
rtcpXrHistoryMaxBurstLossDensity = _RtcpXrHistoryMaxBurstLossDensity_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 13),
    _RtcpXrHistoryMaxBurstLossDensity_Type()
)
rtcpXrHistoryMaxBurstLossDensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxBurstLossDensity.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxBurstLossDensity.setUnits("percent")
_RtcpXrHistoryAvgBurstLossDensity_Type = Percentage
_RtcpXrHistoryAvgBurstLossDensity_Object = MibTableColumn
rtcpXrHistoryAvgBurstLossDensity = _RtcpXrHistoryAvgBurstLossDensity_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 14),
    _RtcpXrHistoryAvgBurstLossDensity_Type()
)
rtcpXrHistoryAvgBurstLossDensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgBurstLossDensity.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgBurstLossDensity.setUnits("percent")
_RtcpXrHistoryMinBurstLenMs_Type = Gauge32
_RtcpXrHistoryMinBurstLenMs_Object = MibTableColumn
rtcpXrHistoryMinBurstLenMs = _RtcpXrHistoryMinBurstLenMs_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 15),
    _RtcpXrHistoryMinBurstLenMs_Type()
)
rtcpXrHistoryMinBurstLenMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinBurstLenMs.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinBurstLenMs.setUnits("milliseconds")
_RtcpXrHistoryMaxBurstLenMs_Type = Gauge32
_RtcpXrHistoryMaxBurstLenMs_Object = MibTableColumn
rtcpXrHistoryMaxBurstLenMs = _RtcpXrHistoryMaxBurstLenMs_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 16),
    _RtcpXrHistoryMaxBurstLenMs_Type()
)
rtcpXrHistoryMaxBurstLenMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxBurstLenMs.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxBurstLenMs.setUnits("milliseconds")
_RtcpXrHistoryAvgBurstLenMs_Type = Gauge32
_RtcpXrHistoryAvgBurstLenMs_Object = MibTableColumn
rtcpXrHistoryAvgBurstLenMs = _RtcpXrHistoryAvgBurstLenMs_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 17),
    _RtcpXrHistoryAvgBurstLenMs_Type()
)
rtcpXrHistoryAvgBurstLenMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgBurstLenMs.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgBurstLenMs.setUnits("milliseconds")
_RtcpXrHistoryMaxGapLossDensity_Type = Percentage
_RtcpXrHistoryMaxGapLossDensity_Object = MibTableColumn
rtcpXrHistoryMaxGapLossDensity = _RtcpXrHistoryMaxGapLossDensity_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 18),
    _RtcpXrHistoryMaxGapLossDensity_Type()
)
rtcpXrHistoryMaxGapLossDensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxGapLossDensity.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxGapLossDensity.setUnits("percent")
_RtcpXrHistoryAvgGapLossDensity_Type = Percentage
_RtcpXrHistoryAvgGapLossDensity_Object = MibTableColumn
rtcpXrHistoryAvgGapLossDensity = _RtcpXrHistoryAvgGapLossDensity_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 19),
    _RtcpXrHistoryAvgGapLossDensity_Type()
)
rtcpXrHistoryAvgGapLossDensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgGapLossDensity.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgGapLossDensity.setUnits("percent")
_RtcpXrHistoryMinGapLenMs_Type = Gauge32
_RtcpXrHistoryMinGapLenMs_Object = MibTableColumn
rtcpXrHistoryMinGapLenMs = _RtcpXrHistoryMinGapLenMs_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 20),
    _RtcpXrHistoryMinGapLenMs_Type()
)
rtcpXrHistoryMinGapLenMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinGapLenMs.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinGapLenMs.setUnits("milliseconds")
_RtcpXrHistoryMaxGapLenMs_Type = Gauge32
_RtcpXrHistoryMaxGapLenMs_Object = MibTableColumn
rtcpXrHistoryMaxGapLenMs = _RtcpXrHistoryMaxGapLenMs_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 21),
    _RtcpXrHistoryMaxGapLenMs_Type()
)
rtcpXrHistoryMaxGapLenMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxGapLenMs.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxGapLenMs.setUnits("milliseconds")
_RtcpXrHistoryAvgGapLenMs_Type = Gauge32
_RtcpXrHistoryAvgGapLenMs_Object = MibTableColumn
rtcpXrHistoryAvgGapLenMs = _RtcpXrHistoryAvgGapLenMs_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 22),
    _RtcpXrHistoryAvgGapLenMs_Type()
)
rtcpXrHistoryAvgGapLenMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgGapLenMs.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgGapLenMs.setUnits("milliseconds")
_RtcpXrHistoryMinOneWayDelay_Type = Gauge32
_RtcpXrHistoryMinOneWayDelay_Object = MibTableColumn
rtcpXrHistoryMinOneWayDelay = _RtcpXrHistoryMinOneWayDelay_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 23),
    _RtcpXrHistoryMinOneWayDelay_Type()
)
rtcpXrHistoryMinOneWayDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinOneWayDelay.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinOneWayDelay.setUnits("milliseconds")
_RtcpXrHistoryMaxOneWayDelay_Type = Gauge32
_RtcpXrHistoryMaxOneWayDelay_Object = MibTableColumn
rtcpXrHistoryMaxOneWayDelay = _RtcpXrHistoryMaxOneWayDelay_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 24),
    _RtcpXrHistoryMaxOneWayDelay_Type()
)
rtcpXrHistoryMaxOneWayDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxOneWayDelay.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxOneWayDelay.setUnits("milliseconds")
_RtcpXrHistoryAvgOneWayDelay_Type = Gauge32
_RtcpXrHistoryAvgOneWayDelay_Object = MibTableColumn
rtcpXrHistoryAvgOneWayDelay = _RtcpXrHistoryAvgOneWayDelay_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 25),
    _RtcpXrHistoryAvgOneWayDelay_Type()
)
rtcpXrHistoryAvgOneWayDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgOneWayDelay.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgOneWayDelay.setUnits("milliseconds")
_RtcpXrHistoryMinEndSystemDelay_Type = Gauge32
_RtcpXrHistoryMinEndSystemDelay_Object = MibTableColumn
rtcpXrHistoryMinEndSystemDelay = _RtcpXrHistoryMinEndSystemDelay_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 26),
    _RtcpXrHistoryMinEndSystemDelay_Type()
)
rtcpXrHistoryMinEndSystemDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinEndSystemDelay.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinEndSystemDelay.setUnits("milliseconds")
_RtcpXrHistoryMaxEndSystemDelay_Type = Gauge32
_RtcpXrHistoryMaxEndSystemDelay_Object = MibTableColumn
rtcpXrHistoryMaxEndSystemDelay = _RtcpXrHistoryMaxEndSystemDelay_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 27),
    _RtcpXrHistoryMaxEndSystemDelay_Type()
)
rtcpXrHistoryMaxEndSystemDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxEndSystemDelay.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxEndSystemDelay.setUnits("milliseconds")
_RtcpXrHistoryAvgEndSystemDelay_Type = Gauge32
_RtcpXrHistoryAvgEndSystemDelay_Object = MibTableColumn
rtcpXrHistoryAvgEndSystemDelay = _RtcpXrHistoryAvgEndSystemDelay_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 28),
    _RtcpXrHistoryAvgEndSystemDelay_Type()
)
rtcpXrHistoryAvgEndSystemDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgEndSystemDelay.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgEndSystemDelay.setUnits("milliseconds")
_RtcpXrHistoryMinJitterLevel_Type = Gauge32
_RtcpXrHistoryMinJitterLevel_Object = MibTableColumn
rtcpXrHistoryMinJitterLevel = _RtcpXrHistoryMinJitterLevel_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 29),
    _RtcpXrHistoryMinJitterLevel_Type()
)
rtcpXrHistoryMinJitterLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinJitterLevel.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinJitterLevel.setUnits("milliseconds")
_RtcpXrHistoryMaxJitterLevel_Type = Gauge32
_RtcpXrHistoryMaxJitterLevel_Object = MibTableColumn
rtcpXrHistoryMaxJitterLevel = _RtcpXrHistoryMaxJitterLevel_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 30),
    _RtcpXrHistoryMaxJitterLevel_Type()
)
rtcpXrHistoryMaxJitterLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxJitterLevel.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxJitterLevel.setUnits("milliseconds")
_RtcpXrHistoryAvgJitterLevel_Type = Gauge32
_RtcpXrHistoryAvgJitterLevel_Object = MibTableColumn
rtcpXrHistoryAvgJitterLevel = _RtcpXrHistoryAvgJitterLevel_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 31),
    _RtcpXrHistoryAvgJitterLevel_Type()
)
rtcpXrHistoryAvgJitterLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgJitterLevel.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgJitterLevel.setUnits("milliseconds")
_RtcpXrHistoryMinNoiseLeveldBm_Type = LeveldB
_RtcpXrHistoryMinNoiseLeveldBm_Object = MibTableColumn
rtcpXrHistoryMinNoiseLeveldBm = _RtcpXrHistoryMinNoiseLeveldBm_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 32),
    _RtcpXrHistoryMinNoiseLeveldBm_Type()
)
rtcpXrHistoryMinNoiseLeveldBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinNoiseLeveldBm.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinNoiseLeveldBm.setUnits("dBm0")
_RtcpXrHistoryMaxNoiseLeveldBm_Type = LeveldB
_RtcpXrHistoryMaxNoiseLeveldBm_Object = MibTableColumn
rtcpXrHistoryMaxNoiseLeveldBm = _RtcpXrHistoryMaxNoiseLeveldBm_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 33),
    _RtcpXrHistoryMaxNoiseLeveldBm_Type()
)
rtcpXrHistoryMaxNoiseLeveldBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxNoiseLeveldBm.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxNoiseLeveldBm.setUnits("dBm0")
_RtcpXrHistoryAvgNoiseLeveldBm_Type = LeveldB
_RtcpXrHistoryAvgNoiseLeveldBm_Object = MibTableColumn
rtcpXrHistoryAvgNoiseLeveldBm = _RtcpXrHistoryAvgNoiseLeveldBm_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 34),
    _RtcpXrHistoryAvgNoiseLeveldBm_Type()
)
rtcpXrHistoryAvgNoiseLeveldBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgNoiseLeveldBm.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgNoiseLeveldBm.setUnits("dBm0")
_RtcpXrHistoryNoiseLevelCount_Type = Counter32
_RtcpXrHistoryNoiseLevelCount_Object = MibTableColumn
rtcpXrHistoryNoiseLevelCount = _RtcpXrHistoryNoiseLevelCount_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 35),
    _RtcpXrHistoryNoiseLevelCount_Type()
)
rtcpXrHistoryNoiseLevelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryNoiseLevelCount.setStatus("current")
_RtcpXrHistoryMinSignalLeveldBm_Type = LeveldB
_RtcpXrHistoryMinSignalLeveldBm_Object = MibTableColumn
rtcpXrHistoryMinSignalLeveldBm = _RtcpXrHistoryMinSignalLeveldBm_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 36),
    _RtcpXrHistoryMinSignalLeveldBm_Type()
)
rtcpXrHistoryMinSignalLeveldBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinSignalLeveldBm.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinSignalLeveldBm.setUnits("dBm0")
_RtcpXrHistoryMaxSignalLeveldBm_Type = LeveldB
_RtcpXrHistoryMaxSignalLeveldBm_Object = MibTableColumn
rtcpXrHistoryMaxSignalLeveldBm = _RtcpXrHistoryMaxSignalLeveldBm_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 37),
    _RtcpXrHistoryMaxSignalLeveldBm_Type()
)
rtcpXrHistoryMaxSignalLeveldBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxSignalLeveldBm.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxSignalLeveldBm.setUnits("dBm0")
_RtcpXrHistoryAvgSignalLeveldBm_Type = LeveldB
_RtcpXrHistoryAvgSignalLeveldBm_Object = MibTableColumn
rtcpXrHistoryAvgSignalLeveldBm = _RtcpXrHistoryAvgSignalLeveldBm_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 38),
    _RtcpXrHistoryAvgSignalLeveldBm_Type()
)
rtcpXrHistoryAvgSignalLeveldBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgSignalLeveldBm.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgSignalLeveldBm.setUnits("dBm0")
_RtcpXrHistorySignalLevelCount_Type = Counter32
_RtcpXrHistorySignalLevelCount_Object = MibTableColumn
rtcpXrHistorySignalLevelCount = _RtcpXrHistorySignalLevelCount_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 39),
    _RtcpXrHistorySignalLevelCount_Type()
)
rtcpXrHistorySignalLevelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistorySignalLevelCount.setStatus("current")
_RtcpXrHistoryMinLocalRERLdB_Type = LeveldB
_RtcpXrHistoryMinLocalRERLdB_Object = MibTableColumn
rtcpXrHistoryMinLocalRERLdB = _RtcpXrHistoryMinLocalRERLdB_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 40),
    _RtcpXrHistoryMinLocalRERLdB_Type()
)
rtcpXrHistoryMinLocalRERLdB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinLocalRERLdB.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinLocalRERLdB.setUnits("dBm")
_RtcpXrHistoryMaxLocalRERLdB_Type = LeveldB
_RtcpXrHistoryMaxLocalRERLdB_Object = MibTableColumn
rtcpXrHistoryMaxLocalRERLdB = _RtcpXrHistoryMaxLocalRERLdB_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 41),
    _RtcpXrHistoryMaxLocalRERLdB_Type()
)
rtcpXrHistoryMaxLocalRERLdB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxLocalRERLdB.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxLocalRERLdB.setUnits("dBm")
_RtcpXrHistoryAvgLocalRERLdB_Type = LeveldB
_RtcpXrHistoryAvgLocalRERLdB_Object = MibTableColumn
rtcpXrHistoryAvgLocalRERLdB = _RtcpXrHistoryAvgLocalRERLdB_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 42),
    _RtcpXrHistoryAvgLocalRERLdB_Type()
)
rtcpXrHistoryAvgLocalRERLdB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgLocalRERLdB.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgLocalRERLdB.setUnits("dBm")
_RtcpXrHistoryLocalRERLCount_Type = Counter32
_RtcpXrHistoryLocalRERLCount_Object = MibTableColumn
rtcpXrHistoryLocalRERLCount = _RtcpXrHistoryLocalRERLCount_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 43),
    _RtcpXrHistoryLocalRERLCount_Type()
)
rtcpXrHistoryLocalRERLCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryLocalRERLCount.setStatus("current")
_RtcpXrHistoryMinRemoteRERLdB_Type = LeveldB
_RtcpXrHistoryMinRemoteRERLdB_Object = MibTableColumn
rtcpXrHistoryMinRemoteRERLdB = _RtcpXrHistoryMinRemoteRERLdB_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 44),
    _RtcpXrHistoryMinRemoteRERLdB_Type()
)
rtcpXrHistoryMinRemoteRERLdB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinRemoteRERLdB.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinRemoteRERLdB.setUnits("dBm")
_RtcpXrHistoryMaxRemoteRERLdB_Type = LeveldB
_RtcpXrHistoryMaxRemoteRERLdB_Object = MibTableColumn
rtcpXrHistoryMaxRemoteRERLdB = _RtcpXrHistoryMaxRemoteRERLdB_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 45),
    _RtcpXrHistoryMaxRemoteRERLdB_Type()
)
rtcpXrHistoryMaxRemoteRERLdB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxRemoteRERLdB.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxRemoteRERLdB.setUnits("dBm")
_RtcpXrHistoryAvgRemoteRERLdB_Type = LeveldB
_RtcpXrHistoryAvgRemoteRERLdB_Object = MibTableColumn
rtcpXrHistoryAvgRemoteRERLdB = _RtcpXrHistoryAvgRemoteRERLdB_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 46),
    _RtcpXrHistoryAvgRemoteRERLdB_Type()
)
rtcpXrHistoryAvgRemoteRERLdB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgRemoteRERLdB.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgRemoteRERLdB.setUnits("dBm")
_RtcpXrHistoryRemoteRERLCount_Type = Counter32
_RtcpXrHistoryRemoteRERLCount_Object = MibTableColumn
rtcpXrHistoryRemoteRERLCount = _RtcpXrHistoryRemoteRERLCount_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 47),
    _RtcpXrHistoryRemoteRERLCount_Type()
)
rtcpXrHistoryRemoteRERLCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryRemoteRERLCount.setStatus("current")
_RtcpXrHistoryMinRCQ_Type = Rfactor
_RtcpXrHistoryMinRCQ_Object = MibTableColumn
rtcpXrHistoryMinRCQ = _RtcpXrHistoryMinRCQ_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 48),
    _RtcpXrHistoryMinRCQ_Type()
)
rtcpXrHistoryMinRCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinRCQ.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinRCQ.setUnits("R factor")
_RtcpXrHistoryMaxRCQ_Type = Rfactor
_RtcpXrHistoryMaxRCQ_Object = MibTableColumn
rtcpXrHistoryMaxRCQ = _RtcpXrHistoryMaxRCQ_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 49),
    _RtcpXrHistoryMaxRCQ_Type()
)
rtcpXrHistoryMaxRCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxRCQ.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxRCQ.setUnits("R factor")
_RtcpXrHistoryAvgRCQ_Type = Rfactor
_RtcpXrHistoryAvgRCQ_Object = MibTableColumn
rtcpXrHistoryAvgRCQ = _RtcpXrHistoryAvgRCQ_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 50),
    _RtcpXrHistoryAvgRCQ_Type()
)
rtcpXrHistoryAvgRCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgRCQ.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgRCQ.setUnits("R factor")
_RtcpXrHistoryRCQCount_Type = Counter32
_RtcpXrHistoryRCQCount_Object = MibTableColumn
rtcpXrHistoryRCQCount = _RtcpXrHistoryRCQCount_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 51),
    _RtcpXrHistoryRCQCount_Type()
)
rtcpXrHistoryRCQCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryRCQCount.setStatus("current")
_RtcpXrHistoryMinRLQ_Type = Rfactor
_RtcpXrHistoryMinRLQ_Object = MibTableColumn
rtcpXrHistoryMinRLQ = _RtcpXrHistoryMinRLQ_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 52),
    _RtcpXrHistoryMinRLQ_Type()
)
rtcpXrHistoryMinRLQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinRLQ.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinRLQ.setUnits("R factor")
_RtcpXrHistoryMaxRLQ_Type = Rfactor
_RtcpXrHistoryMaxRLQ_Object = MibTableColumn
rtcpXrHistoryMaxRLQ = _RtcpXrHistoryMaxRLQ_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 53),
    _RtcpXrHistoryMaxRLQ_Type()
)
rtcpXrHistoryMaxRLQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxRLQ.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxRLQ.setUnits("R factor")
_RtcpXrHistoryAvgRLQ_Type = Rfactor
_RtcpXrHistoryAvgRLQ_Object = MibTableColumn
rtcpXrHistoryAvgRLQ = _RtcpXrHistoryAvgRLQ_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 54),
    _RtcpXrHistoryAvgRLQ_Type()
)
rtcpXrHistoryAvgRLQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgRLQ.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgRLQ.setUnits("R factor")
_RtcpXrHistoryRLQCount_Type = Counter32
_RtcpXrHistoryRLQCount_Object = MibTableColumn
rtcpXrHistoryRLQCount = _RtcpXrHistoryRLQCount_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 55),
    _RtcpXrHistoryRLQCount_Type()
)
rtcpXrHistoryRLQCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryRLQCount.setStatus("current")
_RtcpXrHistoryMinMOSCQ_Type = ScaledMOSscore
_RtcpXrHistoryMinMOSCQ_Object = MibTableColumn
rtcpXrHistoryMinMOSCQ = _RtcpXrHistoryMinMOSCQ_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 56),
    _RtcpXrHistoryMinMOSCQ_Type()
)
rtcpXrHistoryMinMOSCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinMOSCQ.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinMOSCQ.setUnits("MOS x 10")
_RtcpXrHistoryMaxMOSCQ_Type = ScaledMOSscore
_RtcpXrHistoryMaxMOSCQ_Object = MibTableColumn
rtcpXrHistoryMaxMOSCQ = _RtcpXrHistoryMaxMOSCQ_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 57),
    _RtcpXrHistoryMaxMOSCQ_Type()
)
rtcpXrHistoryMaxMOSCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxMOSCQ.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxMOSCQ.setUnits("MOS x 10")
_RtcpXrHistoryAvgMOSCQ_Type = ScaledMOSscore
_RtcpXrHistoryAvgMOSCQ_Object = MibTableColumn
rtcpXrHistoryAvgMOSCQ = _RtcpXrHistoryAvgMOSCQ_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 58),
    _RtcpXrHistoryAvgMOSCQ_Type()
)
rtcpXrHistoryAvgMOSCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgMOSCQ.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgMOSCQ.setUnits("MOS x 10")
_RtcpXrHistoryMOSCQCount_Type = Counter32
_RtcpXrHistoryMOSCQCount_Object = MibTableColumn
rtcpXrHistoryMOSCQCount = _RtcpXrHistoryMOSCQCount_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 59),
    _RtcpXrHistoryMOSCQCount_Type()
)
rtcpXrHistoryMOSCQCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMOSCQCount.setStatus("current")
_RtcpXrHistoryMinMOSLQ_Type = ScaledMOSscore
_RtcpXrHistoryMinMOSLQ_Object = MibTableColumn
rtcpXrHistoryMinMOSLQ = _RtcpXrHistoryMinMOSLQ_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 60),
    _RtcpXrHistoryMinMOSLQ_Type()
)
rtcpXrHistoryMinMOSLQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinMOSLQ.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMinMOSLQ.setUnits("MOS x 10")
_RtcpXrHistoryMaxMOSLQ_Type = ScaledMOSscore
_RtcpXrHistoryMaxMOSLQ_Object = MibTableColumn
rtcpXrHistoryMaxMOSLQ = _RtcpXrHistoryMaxMOSLQ_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 61),
    _RtcpXrHistoryMaxMOSLQ_Type()
)
rtcpXrHistoryMaxMOSLQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxMOSLQ.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryMaxMOSLQ.setUnits("MOS x 10")
_RtcpXrHistoryAvgMOSLQ_Type = ScaledMOSscore
_RtcpXrHistoryAvgMOSLQ_Object = MibTableColumn
rtcpXrHistoryAvgMOSLQ = _RtcpXrHistoryAvgMOSLQ_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 62),
    _RtcpXrHistoryAvgMOSLQ_Type()
)
rtcpXrHistoryAvgMOSLQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgMOSLQ.setStatus("current")
if mibBuilder.loadTexts:
    rtcpXrHistoryAvgMOSLQ.setUnits("MOS x 10")
_RtcpXrHistoryMOSLQCount_Type = Counter32
_RtcpXrHistoryMOSLQCount_Object = MibTableColumn
rtcpXrHistoryMOSLQCount = _RtcpXrHistoryMOSLQCount_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 63),
    _RtcpXrHistoryMOSLQCount_Type()
)
rtcpXrHistoryMOSLQCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryMOSLQCount.setStatus("current")


class _RtcpXrHistoryCQAlgorithm_Type(OctetString):
    """Custom type rtcpXrHistoryCQAlgorithm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RtcpXrHistoryCQAlgorithm_Type.__name__ = "OctetString"
_RtcpXrHistoryCQAlgorithm_Object = MibTableColumn
rtcpXrHistoryCQAlgorithm = _RtcpXrHistoryCQAlgorithm_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 64),
    _RtcpXrHistoryCQAlgorithm_Type()
)
rtcpXrHistoryCQAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrHistoryCQAlgorithm.setStatus("current")


class _RtcpXrHistoryReset_Type(Integer32):
    """Custom type rtcpXrHistoryReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stop", 2),
          ("reset", 3))
    )


_RtcpXrHistoryReset_Type.__name__ = "Integer32"
_RtcpXrHistoryReset_Object = MibTableColumn
rtcpXrHistoryReset = _RtcpXrHistoryReset_Object(
    (1, 3, 6, 1, 2, 1, 255, 1, 4, 1, 65),
    _RtcpXrHistoryReset_Type()
)
rtcpXrHistoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtcpXrHistoryReset.setStatus("current")
_RtcpXrConformance_ObjectIdentity = ObjectIdentity
rtcpXrConformance = _RtcpXrConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 255, 2)
)
_RtcpXrCompliances_ObjectIdentity = ObjectIdentity
rtcpXrCompliances = _RtcpXrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 255, 2, 1)
)
_RtcpXrGroups_ObjectIdentity = ObjectIdentity
rtcpXrGroups = _RtcpXrGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 255, 2, 2)
)
_RtcpXrEvents_ObjectIdentity = ObjectIdentity
rtcpXrEvents = _RtcpXrEvents_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 255, 3)
)
_RtcpXrEventParam_ObjectIdentity = ObjectIdentity
rtcpXrEventParam = _RtcpXrEventParam_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 255, 3, 2)
)
_RtcpXrVoipAlertType_Type = SnmpAdminString
_RtcpXrVoipAlertType_Object = MibScalar
rtcpXrVoipAlertType = _RtcpXrVoipAlertType_Object(
    (1, 3, 6, 1, 2, 1, 255, 3, 2, 1),
    _RtcpXrVoipAlertType_Type()
)
rtcpXrVoipAlertType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrVoipAlertType.setStatus("current")


class _RtcpXrVoipAlertInfoType_Type(Integer32):
    """Custom type rtcpXrVoipAlertInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminStringOnly", 1),
          ("sessionPointer", 2),
          ("historyPointer", 3))
    )


_RtcpXrVoipAlertInfoType_Type.__name__ = "Integer32"
_RtcpXrVoipAlertInfoType_Object = MibScalar
rtcpXrVoipAlertInfoType = _RtcpXrVoipAlertInfoType_Object(
    (1, 3, 6, 1, 2, 1, 255, 3, 2, 2),
    _RtcpXrVoipAlertInfoType_Type()
)
rtcpXrVoipAlertInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrVoipAlertInfoType.setStatus("current")
_RtcpXrVoipAlertPointer_Type = RowPointer
_RtcpXrVoipAlertPointer_Object = MibScalar
rtcpXrVoipAlertPointer = _RtcpXrVoipAlertPointer_Object(
    (1, 3, 6, 1, 2, 1, 255, 3, 2, 3),
    _RtcpXrVoipAlertPointer_Type()
)
rtcpXrVoipAlertPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrVoipAlertPointer.setStatus("current")


class _RtcpXrVoipAlertSeverity_Type(Integer32):
    """Custom type rtcpXrVoipAlertSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_RtcpXrVoipAlertSeverity_Type.__name__ = "Integer32"
_RtcpXrVoipAlertSeverity_Object = MibScalar
rtcpXrVoipAlertSeverity = _RtcpXrVoipAlertSeverity_Object(
    (1, 3, 6, 1, 2, 1, 255, 3, 2, 4),
    _RtcpXrVoipAlertSeverity_Type()
)
rtcpXrVoipAlertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcpXrVoipAlertSeverity.setStatus("current")

# Managed Objects groups

rtcpXrSessionIDGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 255, 2, 2, 1)
)
rtcpXrSessionIDGroup.setObjects(
      *(("RTCPXR-MIB", "rtcpXrSessionIDSessionIdentifier"),
        ("RTCPXR-MIB", "rtcpXrSessionIDCallStartTime"),
        ("RTCPXR-MIB", "rtcpXrSessionIDCallStopTime"),
        ("RTCPXR-MIB", "rtcpXrSessionIDSourceIPtype"),
        ("RTCPXR-MIB", "rtcpXrSessionIDSourceIPaddress"),
        ("RTCPXR-MIB", "rtcpXrSessionIDSourceRTPport"),
        ("RTCPXR-MIB", "rtcpXrSessionIDSourceRTCPport"),
        ("RTCPXR-MIB", "rtcpXrSessionIDDestIPtype"),
        ("RTCPXR-MIB", "rtcpXrSessionIDDestIPaddress"),
        ("RTCPXR-MIB", "rtcpXrSessionIDDestRTPport"),
        ("RTCPXR-MIB", "rtcpXrSessionIDDestRTCPport"),
        ("RTCPXR-MIB", "rtcpXrSessionIDDestIdentifier"),
        ("RTCPXR-MIB", "rtcpXrSessionIDDestIdenType"),
        ("RTCPXR-MIB", "rtcpXrSessionIDSrceIdentifier"),
        ("RTCPXR-MIB", "rtcpXrSessionIDSrceIdenType"),
        ("RTCPXR-MIB", "rtcpXrSessionIDMeasurePt"),
        ("RTCPXR-MIB", "rtcpXrSessionIDMeasurePtID"),
        ("RTCPXR-MIB", "rtcpXrSessionIDReverseSession"),
        ("RTCPXR-MIB", "rtcpXrSessionIDAltMeasurePt"))
)
if mibBuilder.loadTexts:
    rtcpXrSessionIDGroup.setStatus("current")

rtcpXrBaseParamGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 255, 2, 2, 2)
)
rtcpXrBaseParamGroup.setObjects(
      *(("RTCPXR-MIB", "rtcpXrBaseParamVocoderType"),
        ("RTCPXR-MIB", "rtcpXrBaseParamVocoderRate"),
        ("RTCPXR-MIB", "rtcpXrBaseParamFrameDuration"),
        ("RTCPXR-MIB", "rtcpXrBaseParamSampleRate"),
        ("RTCPXR-MIB", "rtcpXrBaseParamDurationMs"),
        ("RTCPXR-MIB", "rtcpXrBaseParamNetworkLossRate"),
        ("RTCPXR-MIB", "rtcpXrBaseParamAvgDiscardRate"),
        ("RTCPXR-MIB", "rtcpXrBaseParamBurstLossDensity"),
        ("RTCPXR-MIB", "rtcpXrBaseParamBurstLenMs"),
        ("RTCPXR-MIB", "rtcpXrBaseParamGapLossDensity"),
        ("RTCPXR-MIB", "rtcpXrBaseParamGapLenMs"),
        ("RTCPXR-MIB", "rtcpXrBaseParamAvgOWDelay"),
        ("RTCPXR-MIB", "rtcpXrBaseParamAvgEndSysDelay"),
        ("RTCPXR-MIB", "rtcpXrBaseParamPlcType"),
        ("RTCPXR-MIB", "rtcpXrBaseParamJBuffAdaptMode"),
        ("RTCPXR-MIB", "rtcpXrBaseParamJBuffAdaptRate"),
        ("RTCPXR-MIB", "rtcpXrBaseParamJBuffAverageDelay"),
        ("RTCPXR-MIB", "rtcpXrBaseParamJBuffMaximumDelay"),
        ("RTCPXR-MIB", "rtcpXrBaseParamJBuffAbsMaxDelay"),
        ("RTCPXR-MIB", "rtcpXrBaseParamJitterLevel"))
)
if mibBuilder.loadTexts:
    rtcpXrBaseParamGroup.setStatus("current")

rtcpXrCallQualityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 255, 2, 2, 3)
)
rtcpXrCallQualityGroup.setObjects(
      *(("RTCPXR-MIB", "rtcpXrCallQualityNoiseLeveldBm"),
        ("RTCPXR-MIB", "rtcpXrCallQualitySignalLeveldBm"),
        ("RTCPXR-MIB", "rtcpXrCallQualityLocalRERLdB"),
        ("RTCPXR-MIB", "rtcpXrCallQualityRemoteRERLdB"),
        ("RTCPXR-MIB", "rtcpXrCallQualityRCQ"),
        ("RTCPXR-MIB", "rtcpXrCallQualityRLQ"),
        ("RTCPXR-MIB", "rtcpXrCallQualityExternalRCQ"),
        ("RTCPXR-MIB", "rtcpXrCallQualityMOSCQ"),
        ("RTCPXR-MIB", "rtcpXrCallQualityMOSLQ"),
        ("RTCPXR-MIB", "rtcpXrCallQualityAlgorithm"))
)
if mibBuilder.loadTexts:
    rtcpXrCallQualityGroup.setStatus("current")

rtcpXrMIBHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 255, 2, 2, 4)
)
rtcpXrMIBHistoryGroup.setObjects(
      *(("RTCPXR-MIB", "rtcpXrHistoryGroupName"),
        ("RTCPXR-MIB", "rtcpXrHistoryStartTime"),
        ("RTCPXR-MIB", "rtcpXrHistoryStopTime"),
        ("RTCPXR-MIB", "rtcpXrHistoryNumOfSessions"),
        ("RTCPXR-MIB", "rtcpXrHistoryMinDurationMs"),
        ("RTCPXR-MIB", "rtcpXrHistoryMaxDurationMs"),
        ("RTCPXR-MIB", "rtcpXrHistoryAvgDurationMs"),
        ("RTCPXR-MIB", "rtcpXrHistoryMaxNetworkLossRate"),
        ("RTCPXR-MIB", "rtcpXrHistoryAvgNetworkLossRate"),
        ("RTCPXR-MIB", "rtcpXrHistoryMaxDiscardRate"),
        ("RTCPXR-MIB", "rtcpXrHistoryAvgDiscardRate"),
        ("RTCPXR-MIB", "rtcpXrHistoryMaxBurstLossDensity"),
        ("RTCPXR-MIB", "rtcpXrHistoryAvgBurstLossDensity"),
        ("RTCPXR-MIB", "rtcpXrHistoryMinBurstLenMs"),
        ("RTCPXR-MIB", "rtcpXrHistoryMaxBurstLenMs"),
        ("RTCPXR-MIB", "rtcpXrHistoryAvgBurstLenMs"),
        ("RTCPXR-MIB", "rtcpXrHistoryMaxGapLossDensity"),
        ("RTCPXR-MIB", "rtcpXrHistoryAvgGapLossDensity"),
        ("RTCPXR-MIB", "rtcpXrHistoryMinGapLenMs"),
        ("RTCPXR-MIB", "rtcpXrHistoryMaxGapLenMs"),
        ("RTCPXR-MIB", "rtcpXrHistoryAvgGapLenMs"),
        ("RTCPXR-MIB", "rtcpXrHistoryMinOneWayDelay"),
        ("RTCPXR-MIB", "rtcpXrHistoryMaxOneWayDelay"),
        ("RTCPXR-MIB", "rtcpXrHistoryAvgOneWayDelay"),
        ("RTCPXR-MIB", "rtcpXrHistoryMinEndSystemDelay"),
        ("RTCPXR-MIB", "rtcpXrHistoryMaxEndSystemDelay"),
        ("RTCPXR-MIB", "rtcpXrHistoryAvgEndSystemDelay"),
        ("RTCPXR-MIB", "rtcpXrHistoryAvgJitterLevel"),
        ("RTCPXR-MIB", "rtcpXrHistoryMinJitterLevel"),
        ("RTCPXR-MIB", "rtcpXrHistoryMaxJitterLevel"),
        ("RTCPXR-MIB", "rtcpXrHistoryMinNoiseLeveldBm"),
        ("RTCPXR-MIB", "rtcpXrHistoryMaxNoiseLeveldBm"),
        ("RTCPXR-MIB", "rtcpXrHistoryAvgNoiseLeveldBm"),
        ("RTCPXR-MIB", "rtcpXrHistoryNoiseLevelCount"),
        ("RTCPXR-MIB", "rtcpXrHistoryMinSignalLeveldBm"),
        ("RTCPXR-MIB", "rtcpXrHistoryMaxSignalLeveldBm"),
        ("RTCPXR-MIB", "rtcpXrHistoryAvgSignalLeveldBm"),
        ("RTCPXR-MIB", "rtcpXrHistorySignalLevelCount"),
        ("RTCPXR-MIB", "rtcpXrHistoryMinLocalRERLdB"),
        ("RTCPXR-MIB", "rtcpXrHistoryMaxLocalRERLdB"),
        ("RTCPXR-MIB", "rtcpXrHistoryAvgLocalRERLdB"),
        ("RTCPXR-MIB", "rtcpXrHistoryLocalRERLCount"),
        ("RTCPXR-MIB", "rtcpXrHistoryMinRemoteRERLdB"),
        ("RTCPXR-MIB", "rtcpXrHistoryMaxRemoteRERLdB"),
        ("RTCPXR-MIB", "rtcpXrHistoryAvgRemoteRERLdB"),
        ("RTCPXR-MIB", "rtcpXrHistoryRemoteRERLCount"),
        ("RTCPXR-MIB", "rtcpXrHistoryMinRCQ"),
        ("RTCPXR-MIB", "rtcpXrHistoryMaxRCQ"),
        ("RTCPXR-MIB", "rtcpXrHistoryAvgRCQ"),
        ("RTCPXR-MIB", "rtcpXrHistoryRCQCount"),
        ("RTCPXR-MIB", "rtcpXrHistoryMinRLQ"),
        ("RTCPXR-MIB", "rtcpXrHistoryMaxRLQ"),
        ("RTCPXR-MIB", "rtcpXrHistoryAvgRLQ"),
        ("RTCPXR-MIB", "rtcpXrHistoryRLQCount"),
        ("RTCPXR-MIB", "rtcpXrHistoryMinMOSCQ"),
        ("RTCPXR-MIB", "rtcpXrHistoryMaxMOSCQ"),
        ("RTCPXR-MIB", "rtcpXrHistoryAvgMOSCQ"),
        ("RTCPXR-MIB", "rtcpXrHistoryMOSCQCount"),
        ("RTCPXR-MIB", "rtcpXrHistoryMinMOSLQ"),
        ("RTCPXR-MIB", "rtcpXrHistoryMaxMOSLQ"),
        ("RTCPXR-MIB", "rtcpXrHistoryAvgMOSLQ"),
        ("RTCPXR-MIB", "rtcpXrHistoryMOSLQCount"),
        ("RTCPXR-MIB", "rtcpXrHistoryCQAlgorithm"),
        ("RTCPXR-MIB", "rtcpXrHistoryReset"))
)
if mibBuilder.loadTexts:
    rtcpXrMIBHistoryGroup.setStatus("current")

rtcpXrNotificationParmsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 255, 2, 2, 5)
)
rtcpXrNotificationParmsGroup.setObjects(
      *(("RTCPXR-MIB", "rtcpXrVoipAlertSeverity"),
        ("RTCPXR-MIB", "rtcpXrVoipAlertType"),
        ("RTCPXR-MIB", "rtcpXrVoipAlertInfoType"),
        ("RTCPXR-MIB", "rtcpXrVoipAlertPointer"))
)
if mibBuilder.loadTexts:
    rtcpXrNotificationParmsGroup.setStatus("current")


# Notification objects

rtcpXrVoipThresholdViolation = NotificationType(
    (1, 3, 6, 1, 2, 1, 255, 3, 1)
)
rtcpXrVoipThresholdViolation.setObjects(
      *(("RTCPXR-MIB", "rtcpXrVoipAlertSeverity"),
        ("RTCPXR-MIB", "rtcpXrVoipAlertType"),
        ("RTCPXR-MIB", "rtcpXrVoipAlertInfoType"),
        ("RTCPXR-MIB", "rtcpXrVoipAlertPointer"))
)
if mibBuilder.loadTexts:
    rtcpXrVoipThresholdViolation.setStatus(
        "current"
    )


# Notifications groups

rtcpXrNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 255, 2, 2, 6)
)
rtcpXrNotificationsGroup.setObjects(
    ("RTCPXR-MIB", "rtcpXrVoipThresholdViolation")
)
if mibBuilder.loadTexts:
    rtcpXrNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rtcpXrFullMetricsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 255, 2, 1, 1)
)
rtcpXrFullMetricsCompliance.setObjects(
      *(("RTCPXR-MIB", "rtcpXrSessionIDGroup"),
        ("RTCPXR-MIB", "rtcpXrBaseParamGroup"),
        ("RTCPXR-MIB", "rtcpXrCallQualityGroup"))
)
if mibBuilder.loadTexts:
    rtcpXrFullMetricsCompliance.setStatus(
        "current"
    )

rtcpXrMetricsAlertsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 255, 2, 1, 2)
)
rtcpXrMetricsAlertsCompliance.setObjects(
      *(("RTCPXR-MIB", "rtcpXrSessionIDGroup"),
        ("RTCPXR-MIB", "rtcpXrBaseParamGroup"),
        ("RTCPXR-MIB", "rtcpXrCallQualityGroup"),
        ("RTCPXR-MIB", "rtcpXrNotificationParmsGroup"),
        ("RTCPXR-MIB", "rtcpXrNotificationsGroup"))
)
if mibBuilder.loadTexts:
    rtcpXrMetricsAlertsCompliance.setStatus(
        "current"
    )

rtcpXrMetricsHistoryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 255, 2, 1, 3)
)
rtcpXrMetricsHistoryCompliance.setObjects(
      *(("RTCPXR-MIB", "rtcpXrSessionIDGroup"),
        ("RTCPXR-MIB", "rtcpXrBaseParamGroup"),
        ("RTCPXR-MIB", "rtcpXrCallQualityGroup"),
        ("RTCPXR-MIB", "rtcpXrMIBHistoryGroup"),
        ("RTCPXR-MIB", "rtcpXrNotificationParmsGroup"),
        ("RTCPXR-MIB", "rtcpXrNotificationsGroup"))
)
if mibBuilder.loadTexts:
    rtcpXrMetricsHistoryCompliance.setStatus(
        "current"
    )

rtcpXrMinimalCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 255, 2, 1, 4)
)
rtcpXrMinimalCompliance.setObjects(
      *(("RTCPXR-MIB", "rtcpXrSessionIDGroup"),
        ("RTCPXR-MIB", "rtcpXrBaseParamGroup"))
)
if mibBuilder.loadTexts:
    rtcpXrMinimalCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RTCPXR-MIB",
    **{"LeveldB": LeveldB,
       "Rfactor": Rfactor,
       "ScaledMOSscore": ScaledMOSscore,
       "Percentage": Percentage,
       "rtcpXrMIB": rtcpXrMIB,
       "rtcpXrMIBObjects": rtcpXrMIBObjects,
       "rtcpXrSessionIDTable": rtcpXrSessionIDTable,
       "rtcpXrSessionIDEntry": rtcpXrSessionIDEntry,
       "rtcpXrSessionIDIndex": rtcpXrSessionIDIndex,
       "rtcpXrSessionIDSessionIdentifier": rtcpXrSessionIDSessionIdentifier,
       "rtcpXrSessionIDCallStartTime": rtcpXrSessionIDCallStartTime,
       "rtcpXrSessionIDCallStopTime": rtcpXrSessionIDCallStopTime,
       "rtcpXrSessionIDSourceIPtype": rtcpXrSessionIDSourceIPtype,
       "rtcpXrSessionIDSourceIPaddress": rtcpXrSessionIDSourceIPaddress,
       "rtcpXrSessionIDSourceRTPport": rtcpXrSessionIDSourceRTPport,
       "rtcpXrSessionIDSourceRTCPport": rtcpXrSessionIDSourceRTCPport,
       "rtcpXrSessionIDDestIPtype": rtcpXrSessionIDDestIPtype,
       "rtcpXrSessionIDDestIPaddress": rtcpXrSessionIDDestIPaddress,
       "rtcpXrSessionIDDestRTPport": rtcpXrSessionIDDestRTPport,
       "rtcpXrSessionIDDestRTCPport": rtcpXrSessionIDDestRTCPport,
       "rtcpXrSessionIDSrceIdenType": rtcpXrSessionIDSrceIdenType,
       "rtcpXrSessionIDSrceIdentifier": rtcpXrSessionIDSrceIdentifier,
       "rtcpXrSessionIDDestIdenType": rtcpXrSessionIDDestIdenType,
       "rtcpXrSessionIDDestIdentifier": rtcpXrSessionIDDestIdentifier,
       "rtcpXrSessionIDMeasurePt": rtcpXrSessionIDMeasurePt,
       "rtcpXrSessionIDMeasurePtID": rtcpXrSessionIDMeasurePtID,
       "rtcpXrSessionIDReverseSession": rtcpXrSessionIDReverseSession,
       "rtcpXrSessionIDAltMeasurePt": rtcpXrSessionIDAltMeasurePt,
       "rtcpXrBaseParamTable": rtcpXrBaseParamTable,
       "rtcpXrBaseParamEntry": rtcpXrBaseParamEntry,
       "rtcpXrBaseParamVocoderType": rtcpXrBaseParamVocoderType,
       "rtcpXrBaseParamVocoderRate": rtcpXrBaseParamVocoderRate,
       "rtcpXrBaseParamFrameDuration": rtcpXrBaseParamFrameDuration,
       "rtcpXrBaseParamSampleRate": rtcpXrBaseParamSampleRate,
       "rtcpXrBaseParamDurationMs": rtcpXrBaseParamDurationMs,
       "rtcpXrBaseParamNetworkLossRate": rtcpXrBaseParamNetworkLossRate,
       "rtcpXrBaseParamAvgDiscardRate": rtcpXrBaseParamAvgDiscardRate,
       "rtcpXrBaseParamBurstLossDensity": rtcpXrBaseParamBurstLossDensity,
       "rtcpXrBaseParamBurstLenMs": rtcpXrBaseParamBurstLenMs,
       "rtcpXrBaseParamGapLossDensity": rtcpXrBaseParamGapLossDensity,
       "rtcpXrBaseParamGapLenMs": rtcpXrBaseParamGapLenMs,
       "rtcpXrBaseParamAvgOWDelay": rtcpXrBaseParamAvgOWDelay,
       "rtcpXrBaseParamAvgEndSysDelay": rtcpXrBaseParamAvgEndSysDelay,
       "rtcpXrBaseParamPlcType": rtcpXrBaseParamPlcType,
       "rtcpXrBaseParamJBuffAdaptMode": rtcpXrBaseParamJBuffAdaptMode,
       "rtcpXrBaseParamJBuffAdaptRate": rtcpXrBaseParamJBuffAdaptRate,
       "rtcpXrBaseParamJBuffAverageDelay": rtcpXrBaseParamJBuffAverageDelay,
       "rtcpXrBaseParamJBuffMaximumDelay": rtcpXrBaseParamJBuffMaximumDelay,
       "rtcpXrBaseParamJBuffAbsMaxDelay": rtcpXrBaseParamJBuffAbsMaxDelay,
       "rtcpXrBaseParamJitterLevel": rtcpXrBaseParamJitterLevel,
       "rtcpXrCallQualityTable": rtcpXrCallQualityTable,
       "rtcpXrCallQualityEntry": rtcpXrCallQualityEntry,
       "rtcpXrCallQualityNoiseLeveldBm": rtcpXrCallQualityNoiseLeveldBm,
       "rtcpXrCallQualitySignalLeveldBm": rtcpXrCallQualitySignalLeveldBm,
       "rtcpXrCallQualityLocalRERLdB": rtcpXrCallQualityLocalRERLdB,
       "rtcpXrCallQualityRemoteRERLdB": rtcpXrCallQualityRemoteRERLdB,
       "rtcpXrCallQualityRCQ": rtcpXrCallQualityRCQ,
       "rtcpXrCallQualityRLQ": rtcpXrCallQualityRLQ,
       "rtcpXrCallQualityExternalRCQ": rtcpXrCallQualityExternalRCQ,
       "rtcpXrCallQualityMOSCQ": rtcpXrCallQualityMOSCQ,
       "rtcpXrCallQualityMOSLQ": rtcpXrCallQualityMOSLQ,
       "rtcpXrCallQualityAlgorithm": rtcpXrCallQualityAlgorithm,
       "rtcpXrHistoryTable": rtcpXrHistoryTable,
       "rtcpXrHistoryEntry": rtcpXrHistoryEntry,
       "rtcpXrHistoryIndex": rtcpXrHistoryIndex,
       "rtcpXrHistoryGroupName": rtcpXrHistoryGroupName,
       "rtcpXrHistoryStartTime": rtcpXrHistoryStartTime,
       "rtcpXrHistoryStopTime": rtcpXrHistoryStopTime,
       "rtcpXrHistoryNumOfSessions": rtcpXrHistoryNumOfSessions,
       "rtcpXrHistoryMinDurationMs": rtcpXrHistoryMinDurationMs,
       "rtcpXrHistoryMaxDurationMs": rtcpXrHistoryMaxDurationMs,
       "rtcpXrHistoryAvgDurationMs": rtcpXrHistoryAvgDurationMs,
       "rtcpXrHistoryMaxNetworkLossRate": rtcpXrHistoryMaxNetworkLossRate,
       "rtcpXrHistoryAvgNetworkLossRate": rtcpXrHistoryAvgNetworkLossRate,
       "rtcpXrHistoryMaxDiscardRate": rtcpXrHistoryMaxDiscardRate,
       "rtcpXrHistoryAvgDiscardRate": rtcpXrHistoryAvgDiscardRate,
       "rtcpXrHistoryMaxBurstLossDensity": rtcpXrHistoryMaxBurstLossDensity,
       "rtcpXrHistoryAvgBurstLossDensity": rtcpXrHistoryAvgBurstLossDensity,
       "rtcpXrHistoryMinBurstLenMs": rtcpXrHistoryMinBurstLenMs,
       "rtcpXrHistoryMaxBurstLenMs": rtcpXrHistoryMaxBurstLenMs,
       "rtcpXrHistoryAvgBurstLenMs": rtcpXrHistoryAvgBurstLenMs,
       "rtcpXrHistoryMaxGapLossDensity": rtcpXrHistoryMaxGapLossDensity,
       "rtcpXrHistoryAvgGapLossDensity": rtcpXrHistoryAvgGapLossDensity,
       "rtcpXrHistoryMinGapLenMs": rtcpXrHistoryMinGapLenMs,
       "rtcpXrHistoryMaxGapLenMs": rtcpXrHistoryMaxGapLenMs,
       "rtcpXrHistoryAvgGapLenMs": rtcpXrHistoryAvgGapLenMs,
       "rtcpXrHistoryMinOneWayDelay": rtcpXrHistoryMinOneWayDelay,
       "rtcpXrHistoryMaxOneWayDelay": rtcpXrHistoryMaxOneWayDelay,
       "rtcpXrHistoryAvgOneWayDelay": rtcpXrHistoryAvgOneWayDelay,
       "rtcpXrHistoryMinEndSystemDelay": rtcpXrHistoryMinEndSystemDelay,
       "rtcpXrHistoryMaxEndSystemDelay": rtcpXrHistoryMaxEndSystemDelay,
       "rtcpXrHistoryAvgEndSystemDelay": rtcpXrHistoryAvgEndSystemDelay,
       "rtcpXrHistoryMinJitterLevel": rtcpXrHistoryMinJitterLevel,
       "rtcpXrHistoryMaxJitterLevel": rtcpXrHistoryMaxJitterLevel,
       "rtcpXrHistoryAvgJitterLevel": rtcpXrHistoryAvgJitterLevel,
       "rtcpXrHistoryMinNoiseLeveldBm": rtcpXrHistoryMinNoiseLeveldBm,
       "rtcpXrHistoryMaxNoiseLeveldBm": rtcpXrHistoryMaxNoiseLeveldBm,
       "rtcpXrHistoryAvgNoiseLeveldBm": rtcpXrHistoryAvgNoiseLeveldBm,
       "rtcpXrHistoryNoiseLevelCount": rtcpXrHistoryNoiseLevelCount,
       "rtcpXrHistoryMinSignalLeveldBm": rtcpXrHistoryMinSignalLeveldBm,
       "rtcpXrHistoryMaxSignalLeveldBm": rtcpXrHistoryMaxSignalLeveldBm,
       "rtcpXrHistoryAvgSignalLeveldBm": rtcpXrHistoryAvgSignalLeveldBm,
       "rtcpXrHistorySignalLevelCount": rtcpXrHistorySignalLevelCount,
       "rtcpXrHistoryMinLocalRERLdB": rtcpXrHistoryMinLocalRERLdB,
       "rtcpXrHistoryMaxLocalRERLdB": rtcpXrHistoryMaxLocalRERLdB,
       "rtcpXrHistoryAvgLocalRERLdB": rtcpXrHistoryAvgLocalRERLdB,
       "rtcpXrHistoryLocalRERLCount": rtcpXrHistoryLocalRERLCount,
       "rtcpXrHistoryMinRemoteRERLdB": rtcpXrHistoryMinRemoteRERLdB,
       "rtcpXrHistoryMaxRemoteRERLdB": rtcpXrHistoryMaxRemoteRERLdB,
       "rtcpXrHistoryAvgRemoteRERLdB": rtcpXrHistoryAvgRemoteRERLdB,
       "rtcpXrHistoryRemoteRERLCount": rtcpXrHistoryRemoteRERLCount,
       "rtcpXrHistoryMinRCQ": rtcpXrHistoryMinRCQ,
       "rtcpXrHistoryMaxRCQ": rtcpXrHistoryMaxRCQ,
       "rtcpXrHistoryAvgRCQ": rtcpXrHistoryAvgRCQ,
       "rtcpXrHistoryRCQCount": rtcpXrHistoryRCQCount,
       "rtcpXrHistoryMinRLQ": rtcpXrHistoryMinRLQ,
       "rtcpXrHistoryMaxRLQ": rtcpXrHistoryMaxRLQ,
       "rtcpXrHistoryAvgRLQ": rtcpXrHistoryAvgRLQ,
       "rtcpXrHistoryRLQCount": rtcpXrHistoryRLQCount,
       "rtcpXrHistoryMinMOSCQ": rtcpXrHistoryMinMOSCQ,
       "rtcpXrHistoryMaxMOSCQ": rtcpXrHistoryMaxMOSCQ,
       "rtcpXrHistoryAvgMOSCQ": rtcpXrHistoryAvgMOSCQ,
       "rtcpXrHistoryMOSCQCount": rtcpXrHistoryMOSCQCount,
       "rtcpXrHistoryMinMOSLQ": rtcpXrHistoryMinMOSLQ,
       "rtcpXrHistoryMaxMOSLQ": rtcpXrHistoryMaxMOSLQ,
       "rtcpXrHistoryAvgMOSLQ": rtcpXrHistoryAvgMOSLQ,
       "rtcpXrHistoryMOSLQCount": rtcpXrHistoryMOSLQCount,
       "rtcpXrHistoryCQAlgorithm": rtcpXrHistoryCQAlgorithm,
       "rtcpXrHistoryReset": rtcpXrHistoryReset,
       "rtcpXrConformance": rtcpXrConformance,
       "rtcpXrCompliances": rtcpXrCompliances,
       "rtcpXrFullMetricsCompliance": rtcpXrFullMetricsCompliance,
       "rtcpXrMetricsAlertsCompliance": rtcpXrMetricsAlertsCompliance,
       "rtcpXrMetricsHistoryCompliance": rtcpXrMetricsHistoryCompliance,
       "rtcpXrMinimalCompliance": rtcpXrMinimalCompliance,
       "rtcpXrGroups": rtcpXrGroups,
       "rtcpXrSessionIDGroup": rtcpXrSessionIDGroup,
       "rtcpXrBaseParamGroup": rtcpXrBaseParamGroup,
       "rtcpXrCallQualityGroup": rtcpXrCallQualityGroup,
       "rtcpXrMIBHistoryGroup": rtcpXrMIBHistoryGroup,
       "rtcpXrNotificationParmsGroup": rtcpXrNotificationParmsGroup,
       "rtcpXrNotificationsGroup": rtcpXrNotificationsGroup,
       "rtcpXrEvents": rtcpXrEvents,
       "rtcpXrVoipThresholdViolation": rtcpXrVoipThresholdViolation,
       "rtcpXrEventParam": rtcpXrEventParam,
       "rtcpXrVoipAlertType": rtcpXrVoipAlertType,
       "rtcpXrVoipAlertInfoType": rtcpXrVoipAlertInfoType,
       "rtcpXrVoipAlertPointer": rtcpXrVoipAlertPointer,
       "rtcpXrVoipAlertSeverity": rtcpXrVoipAlertSeverity}
)

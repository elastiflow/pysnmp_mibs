# SNMP MIB module (ME1200-LLDPMED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-LLDPMED-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:30 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

(ME1200DisplayString,
 ME1200Integer64,
 ME1200InterfaceIndex,
 ME1200RowEditorState,
 ME1200Unsigned16,
 ME1200Unsigned8) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString",
    "ME1200Integer64",
    "ME1200InterfaceIndex",
    "ME1200RowEditorState",
    "ME1200Unsigned16",
    "ME1200Unsigned8")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

me1200LldpmedMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71)
)
if mibBuilder.loadTexts:
    me1200LldpmedMib.setRevisions(
        ("2013-10-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200lldpmedAltitudeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("meters", 1),
          ("floor", 2))
    )



class ME1200lldpmedDatumType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wgs84", 1),
          ("nad83navd88", 2),
          ("nad83mllw", 3))
    )



class ME1200lldpmedDeviceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("connectivity", 0),
          ("endpoint", 1))
    )



class ME1200lldpmedRemoteDeviceType(TextualConvention, Integer32):
    status = "current"
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
        *(("notDefined", 0),
          ("endpointClassI", 1),
          ("endpointClassII", 2),
          ("endpointClassIII", 3),
          ("networkConnectivity", 4),
          ("reserved", 5))
    )



class ME1200lldpmedRemoteNetworkPolicyApplicationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("voice", 1),
          ("voiceSignaling", 2),
          ("guestVoice", 3),
          ("gustVoiceSignaling", 4),
          ("softphoneVoice", 5),
          ("videoConferencing", 6),
          ("streamingVideo", 7),
          ("videoSignaling", 8))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200LldpmedMibObjects_ObjectIdentity = ObjectIdentity
me1200LldpmedMibObjects = _Me1200LldpmedMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1)
)
_Me1200LldpmedConfig_ObjectIdentity = ObjectIdentity
me1200LldpmedConfig = _Me1200LldpmedConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2)
)
_Me1200LldpmedConfigGlobal_ObjectIdentity = ObjectIdentity
me1200LldpmedConfigGlobal = _Me1200LldpmedConfigGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 1)
)


class _Me1200LldpmedConfigGlobalFastRepeatCount_Type(ME1200Unsigned8):
    """Custom type me1200LldpmedConfigGlobalFastRepeatCount based on ME1200Unsigned8"""
    subtypeSpec = ME1200Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Me1200LldpmedConfigGlobalFastRepeatCount_Type.__name__ = "ME1200Unsigned8"
_Me1200LldpmedConfigGlobalFastRepeatCount_Object = MibScalar
me1200LldpmedConfigGlobalFastRepeatCount = _Me1200LldpmedConfigGlobalFastRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 1, 1),
    _Me1200LldpmedConfigGlobalFastRepeatCount_Type()
)
me1200LldpmedConfigGlobalFastRepeatCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigGlobalFastRepeatCount.setStatus("current")
_Me1200LldpmedConfigGlobalLatitude_Type = ME1200Integer64
_Me1200LldpmedConfigGlobalLatitude_Object = MibScalar
me1200LldpmedConfigGlobalLatitude = _Me1200LldpmedConfigGlobalLatitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 1, 2),
    _Me1200LldpmedConfigGlobalLatitude_Type()
)
me1200LldpmedConfigGlobalLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigGlobalLatitude.setStatus("current")
_Me1200LldpmedConfigGlobalLongitude_Type = ME1200Integer64
_Me1200LldpmedConfigGlobalLongitude_Object = MibScalar
me1200LldpmedConfigGlobalLongitude = _Me1200LldpmedConfigGlobalLongitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 1, 3),
    _Me1200LldpmedConfigGlobalLongitude_Type()
)
me1200LldpmedConfigGlobalLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigGlobalLongitude.setStatus("current")
_Me1200LldpmedConfigGlobalAltitudeType_Type = ME1200lldpmedAltitudeType
_Me1200LldpmedConfigGlobalAltitudeType_Object = MibScalar
me1200LldpmedConfigGlobalAltitudeType = _Me1200LldpmedConfigGlobalAltitudeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 1, 4),
    _Me1200LldpmedConfigGlobalAltitudeType_Type()
)
me1200LldpmedConfigGlobalAltitudeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigGlobalAltitudeType.setStatus("current")
_Me1200LldpmedConfigGlobalAltitude_Type = Integer32
_Me1200LldpmedConfigGlobalAltitude_Object = MibScalar
me1200LldpmedConfigGlobalAltitude = _Me1200LldpmedConfigGlobalAltitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 1, 5),
    _Me1200LldpmedConfigGlobalAltitude_Type()
)
me1200LldpmedConfigGlobalAltitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigGlobalAltitude.setStatus("current")


class _Me1200LldpmedConfigGlobalElinAddr_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigGlobalElinAddr based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_Me1200LldpmedConfigGlobalElinAddr_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigGlobalElinAddr_Object = MibScalar
me1200LldpmedConfigGlobalElinAddr = _Me1200LldpmedConfigGlobalElinAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 1, 6),
    _Me1200LldpmedConfigGlobalElinAddr_Type()
)
me1200LldpmedConfigGlobalElinAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigGlobalElinAddr.setStatus("current")
_Me1200LldpmedConfigGlobalDatum_Type = ME1200lldpmedDatumType
_Me1200LldpmedConfigGlobalDatum_Object = MibScalar
me1200LldpmedConfigGlobalDatum = _Me1200LldpmedConfigGlobalDatum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 1, 7),
    _Me1200LldpmedConfigGlobalDatum_Type()
)
me1200LldpmedConfigGlobalDatum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigGlobalDatum.setStatus("current")
_Me1200LldpmedConfigLocationInformation_ObjectIdentity = ObjectIdentity
me1200LldpmedConfigLocationInformation = _Me1200LldpmedConfigLocationInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2)
)


class _Me1200LldpmedConfigLocationInformationState_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationState based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationState_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationState_Object = MibScalar
me1200LldpmedConfigLocationInformationState = _Me1200LldpmedConfigLocationInformationState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 1),
    _Me1200LldpmedConfigLocationInformationState_Type()
)
me1200LldpmedConfigLocationInformationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationState.setStatus("current")


class _Me1200LldpmedConfigLocationInformationCounty_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationCounty based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationCounty_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationCounty_Object = MibScalar
me1200LldpmedConfigLocationInformationCounty = _Me1200LldpmedConfigLocationInformationCounty_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 2),
    _Me1200LldpmedConfigLocationInformationCounty_Type()
)
me1200LldpmedConfigLocationInformationCounty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationCounty.setStatus("current")


class _Me1200LldpmedConfigLocationInformationCity_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationCity based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationCity_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationCity_Object = MibScalar
me1200LldpmedConfigLocationInformationCity = _Me1200LldpmedConfigLocationInformationCity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 3),
    _Me1200LldpmedConfigLocationInformationCity_Type()
)
me1200LldpmedConfigLocationInformationCity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationCity.setStatus("current")


class _Me1200LldpmedConfigLocationInformationCityDistrict_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationCityDistrict based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationCityDistrict_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationCityDistrict_Object = MibScalar
me1200LldpmedConfigLocationInformationCityDistrict = _Me1200LldpmedConfigLocationInformationCityDistrict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 4),
    _Me1200LldpmedConfigLocationInformationCityDistrict_Type()
)
me1200LldpmedConfigLocationInformationCityDistrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationCityDistrict.setStatus("current")


class _Me1200LldpmedConfigLocationInformationBlock_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationBlock based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationBlock_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationBlock_Object = MibScalar
me1200LldpmedConfigLocationInformationBlock = _Me1200LldpmedConfigLocationInformationBlock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 5),
    _Me1200LldpmedConfigLocationInformationBlock_Type()
)
me1200LldpmedConfigLocationInformationBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationBlock.setStatus("current")


class _Me1200LldpmedConfigLocationInformationStreet_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationStreet based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationStreet_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationStreet_Object = MibScalar
me1200LldpmedConfigLocationInformationStreet = _Me1200LldpmedConfigLocationInformationStreet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 6),
    _Me1200LldpmedConfigLocationInformationStreet_Type()
)
me1200LldpmedConfigLocationInformationStreet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationStreet.setStatus("current")


class _Me1200LldpmedConfigLocationInformationLeadingStreetDirection_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationLeadingStreetDirection based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationLeadingStreetDirection_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationLeadingStreetDirection_Object = MibScalar
me1200LldpmedConfigLocationInformationLeadingStreetDirection = _Me1200LldpmedConfigLocationInformationLeadingStreetDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 7),
    _Me1200LldpmedConfigLocationInformationLeadingStreetDirection_Type()
)
me1200LldpmedConfigLocationInformationLeadingStreetDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationLeadingStreetDirection.setStatus("current")


class _Me1200LldpmedConfigLocationInformationTrailingStreetSuffix_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationTrailingStreetSuffix based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationTrailingStreetSuffix_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationTrailingStreetSuffix_Object = MibScalar
me1200LldpmedConfigLocationInformationTrailingStreetSuffix = _Me1200LldpmedConfigLocationInformationTrailingStreetSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 8),
    _Me1200LldpmedConfigLocationInformationTrailingStreetSuffix_Type()
)
me1200LldpmedConfigLocationInformationTrailingStreetSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationTrailingStreetSuffix.setStatus("current")


class _Me1200LldpmedConfigLocationInformationStreetSuffix_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationStreetSuffix based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationStreetSuffix_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationStreetSuffix_Object = MibScalar
me1200LldpmedConfigLocationInformationStreetSuffix = _Me1200LldpmedConfigLocationInformationStreetSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 9),
    _Me1200LldpmedConfigLocationInformationStreetSuffix_Type()
)
me1200LldpmedConfigLocationInformationStreetSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationStreetSuffix.setStatus("current")


class _Me1200LldpmedConfigLocationInformationHouseNo_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationHouseNo based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationHouseNo_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationHouseNo_Object = MibScalar
me1200LldpmedConfigLocationInformationHouseNo = _Me1200LldpmedConfigLocationInformationHouseNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 10),
    _Me1200LldpmedConfigLocationInformationHouseNo_Type()
)
me1200LldpmedConfigLocationInformationHouseNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationHouseNo.setStatus("current")


class _Me1200LldpmedConfigLocationInformationHouseNoSuffix_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationHouseNoSuffix based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationHouseNoSuffix_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationHouseNoSuffix_Object = MibScalar
me1200LldpmedConfigLocationInformationHouseNoSuffix = _Me1200LldpmedConfigLocationInformationHouseNoSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 11),
    _Me1200LldpmedConfigLocationInformationHouseNoSuffix_Type()
)
me1200LldpmedConfigLocationInformationHouseNoSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationHouseNoSuffix.setStatus("current")


class _Me1200LldpmedConfigLocationInformationLandmark_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationLandmark based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationLandmark_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationLandmark_Object = MibScalar
me1200LldpmedConfigLocationInformationLandmark = _Me1200LldpmedConfigLocationInformationLandmark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 12),
    _Me1200LldpmedConfigLocationInformationLandmark_Type()
)
me1200LldpmedConfigLocationInformationLandmark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationLandmark.setStatus("current")


class _Me1200LldpmedConfigLocationInformationAdditionalInfo_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationAdditionalInfo based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationAdditionalInfo_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationAdditionalInfo_Object = MibScalar
me1200LldpmedConfigLocationInformationAdditionalInfo = _Me1200LldpmedConfigLocationInformationAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 13),
    _Me1200LldpmedConfigLocationInformationAdditionalInfo_Type()
)
me1200LldpmedConfigLocationInformationAdditionalInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationAdditionalInfo.setStatus("current")


class _Me1200LldpmedConfigLocationInformationName_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationName_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationName_Object = MibScalar
me1200LldpmedConfigLocationInformationName = _Me1200LldpmedConfigLocationInformationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 14),
    _Me1200LldpmedConfigLocationInformationName_Type()
)
me1200LldpmedConfigLocationInformationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationName.setStatus("current")


class _Me1200LldpmedConfigLocationInformationZipCode_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationZipCode based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationZipCode_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationZipCode_Object = MibScalar
me1200LldpmedConfigLocationInformationZipCode = _Me1200LldpmedConfigLocationInformationZipCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 15),
    _Me1200LldpmedConfigLocationInformationZipCode_Type()
)
me1200LldpmedConfigLocationInformationZipCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationZipCode.setStatus("current")


class _Me1200LldpmedConfigLocationInformationBuilding_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationBuilding based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationBuilding_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationBuilding_Object = MibScalar
me1200LldpmedConfigLocationInformationBuilding = _Me1200LldpmedConfigLocationInformationBuilding_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 16),
    _Me1200LldpmedConfigLocationInformationBuilding_Type()
)
me1200LldpmedConfigLocationInformationBuilding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationBuilding.setStatus("current")


class _Me1200LldpmedConfigLocationInformationApartment_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationApartment based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationApartment_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationApartment_Object = MibScalar
me1200LldpmedConfigLocationInformationApartment = _Me1200LldpmedConfigLocationInformationApartment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 17),
    _Me1200LldpmedConfigLocationInformationApartment_Type()
)
me1200LldpmedConfigLocationInformationApartment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationApartment.setStatus("current")


class _Me1200LldpmedConfigLocationInformationFloor_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationFloor based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationFloor_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationFloor_Object = MibScalar
me1200LldpmedConfigLocationInformationFloor = _Me1200LldpmedConfigLocationInformationFloor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 18),
    _Me1200LldpmedConfigLocationInformationFloor_Type()
)
me1200LldpmedConfigLocationInformationFloor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationFloor.setStatus("current")


class _Me1200LldpmedConfigLocationInformationRoomNumber_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationRoomNumber based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationRoomNumber_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationRoomNumber_Object = MibScalar
me1200LldpmedConfigLocationInformationRoomNumber = _Me1200LldpmedConfigLocationInformationRoomNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 19),
    _Me1200LldpmedConfigLocationInformationRoomNumber_Type()
)
me1200LldpmedConfigLocationInformationRoomNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationRoomNumber.setStatus("current")


class _Me1200LldpmedConfigLocationInformationPlaceType_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationPlaceType based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationPlaceType_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationPlaceType_Object = MibScalar
me1200LldpmedConfigLocationInformationPlaceType = _Me1200LldpmedConfigLocationInformationPlaceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 20),
    _Me1200LldpmedConfigLocationInformationPlaceType_Type()
)
me1200LldpmedConfigLocationInformationPlaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationPlaceType.setStatus("current")


class _Me1200LldpmedConfigLocationInformationPostalCommunityName_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationPostalCommunityName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationPostalCommunityName_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationPostalCommunityName_Object = MibScalar
me1200LldpmedConfigLocationInformationPostalCommunityName = _Me1200LldpmedConfigLocationInformationPostalCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 21),
    _Me1200LldpmedConfigLocationInformationPostalCommunityName_Type()
)
me1200LldpmedConfigLocationInformationPostalCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationPostalCommunityName.setStatus("current")


class _Me1200LldpmedConfigLocationInformationPoBox_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationPoBox based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationPoBox_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationPoBox_Object = MibScalar
me1200LldpmedConfigLocationInformationPoBox = _Me1200LldpmedConfigLocationInformationPoBox_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 22),
    _Me1200LldpmedConfigLocationInformationPoBox_Type()
)
me1200LldpmedConfigLocationInformationPoBox.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationPoBox.setStatus("current")


class _Me1200LldpmedConfigLocationInformationAdditionalCode_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationAdditionalCode based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedConfigLocationInformationAdditionalCode_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationAdditionalCode_Object = MibScalar
me1200LldpmedConfigLocationInformationAdditionalCode = _Me1200LldpmedConfigLocationInformationAdditionalCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 23),
    _Me1200LldpmedConfigLocationInformationAdditionalCode_Type()
)
me1200LldpmedConfigLocationInformationAdditionalCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationAdditionalCode.setStatus("current")


class _Me1200LldpmedConfigLocationInformationCountryCode_Type(ME1200DisplayString):
    """Custom type me1200LldpmedConfigLocationInformationCountryCode based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_Me1200LldpmedConfigLocationInformationCountryCode_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedConfigLocationInformationCountryCode_Object = MibScalar
me1200LldpmedConfigLocationInformationCountryCode = _Me1200LldpmedConfigLocationInformationCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 2, 24),
    _Me1200LldpmedConfigLocationInformationCountryCode_Type()
)
me1200LldpmedConfigLocationInformationCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationCountryCode.setStatus("current")
_Me1200LldpmedConfigTable_Object = MibTable
me1200LldpmedConfigTable = _Me1200LldpmedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 3)
)
if mibBuilder.loadTexts:
    me1200LldpmedConfigTable.setStatus("current")
_Me1200LldpmedConfigEntry_Object = MibTableRow
me1200LldpmedConfigEntry = _Me1200LldpmedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 3, 1)
)
me1200LldpmedConfigEntry.setIndexNames(
    (0, "ME1200-LLDPMED-MIB", "me1200LldpmedConfigIfIndex"),
)
if mibBuilder.loadTexts:
    me1200LldpmedConfigEntry.setStatus("current")
_Me1200LldpmedConfigIfIndex_Type = ME1200InterfaceIndex
_Me1200LldpmedConfigIfIndex_Object = MibTableColumn
me1200LldpmedConfigIfIndex = _Me1200LldpmedConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 3, 1, 1),
    _Me1200LldpmedConfigIfIndex_Type()
)
me1200LldpmedConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LldpmedConfigIfIndex.setStatus("current")


class _Me1200LldpmedConfigOptionalTlvs_Type(ME1200Unsigned8):
    """Custom type me1200LldpmedConfigOptionalTlvs based on ME1200Unsigned8"""
    subtypeSpec = ME1200Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Me1200LldpmedConfigOptionalTlvs_Type.__name__ = "ME1200Unsigned8"
_Me1200LldpmedConfigOptionalTlvs_Object = MibTableColumn
me1200LldpmedConfigOptionalTlvs = _Me1200LldpmedConfigOptionalTlvs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 3, 1, 3),
    _Me1200LldpmedConfigOptionalTlvs_Type()
)
me1200LldpmedConfigOptionalTlvs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigOptionalTlvs.setStatus("current")
_Me1200LldpmedConfigDeviceType_Type = ME1200lldpmedDeviceType
_Me1200LldpmedConfigDeviceType_Object = MibTableColumn
me1200LldpmedConfigDeviceType = _Me1200LldpmedConfigDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 3, 1, 4),
    _Me1200LldpmedConfigDeviceType_Type()
)
me1200LldpmedConfigDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigDeviceType.setStatus("current")
_Me1200LldpmedConfigPolicyTable_Object = MibTable
me1200LldpmedConfigPolicyTable = _Me1200LldpmedConfigPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 4)
)
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyTable.setStatus("current")
_Me1200LldpmedConfigPolicyEntry_Object = MibTableRow
me1200LldpmedConfigPolicyEntry = _Me1200LldpmedConfigPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 4, 1)
)
me1200LldpmedConfigPolicyEntry.setIndexNames(
    (0, "ME1200-LLDPMED-MIB", "me1200LldpmedConfigPolicyLldpmedPolicy"),
)
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyEntry.setStatus("current")


class _Me1200LldpmedConfigPolicyLldpmedPolicy_Type(Integer32):
    """Custom type me1200LldpmedConfigPolicyLldpmedPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Me1200LldpmedConfigPolicyLldpmedPolicy_Type.__name__ = "Integer32"
_Me1200LldpmedConfigPolicyLldpmedPolicy_Object = MibTableColumn
me1200LldpmedConfigPolicyLldpmedPolicy = _Me1200LldpmedConfigPolicyLldpmedPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 4, 1, 1),
    _Me1200LldpmedConfigPolicyLldpmedPolicy_Type()
)
me1200LldpmedConfigPolicyLldpmedPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyLldpmedPolicy.setStatus("current")
_Me1200LldpmedConfigPolicyApplicationType_Type = ME1200lldpmedRemoteNetworkPolicyApplicationType
_Me1200LldpmedConfigPolicyApplicationType_Object = MibTableColumn
me1200LldpmedConfigPolicyApplicationType = _Me1200LldpmedConfigPolicyApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 4, 1, 2),
    _Me1200LldpmedConfigPolicyApplicationType_Type()
)
me1200LldpmedConfigPolicyApplicationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyApplicationType.setStatus("current")
_Me1200LldpmedConfigPolicyTagged_Type = TruthValue
_Me1200LldpmedConfigPolicyTagged_Object = MibTableColumn
me1200LldpmedConfigPolicyTagged = _Me1200LldpmedConfigPolicyTagged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 4, 1, 3),
    _Me1200LldpmedConfigPolicyTagged_Type()
)
me1200LldpmedConfigPolicyTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyTagged.setStatus("current")


class _Me1200LldpmedConfigPolicyVlanId_Type(ME1200Unsigned16):
    """Custom type me1200LldpmedConfigPolicyVlanId based on ME1200Unsigned16"""
    subtypeSpec = ME1200Unsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Me1200LldpmedConfigPolicyVlanId_Type.__name__ = "ME1200Unsigned16"
_Me1200LldpmedConfigPolicyVlanId_Object = MibTableColumn
me1200LldpmedConfigPolicyVlanId = _Me1200LldpmedConfigPolicyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 4, 1, 4),
    _Me1200LldpmedConfigPolicyVlanId_Type()
)
me1200LldpmedConfigPolicyVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyVlanId.setStatus("current")


class _Me1200LldpmedConfigPolicyL2Priority_Type(ME1200Unsigned8):
    """Custom type me1200LldpmedConfigPolicyL2Priority based on ME1200Unsigned8"""
    subtypeSpec = ME1200Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Me1200LldpmedConfigPolicyL2Priority_Type.__name__ = "ME1200Unsigned8"
_Me1200LldpmedConfigPolicyL2Priority_Object = MibTableColumn
me1200LldpmedConfigPolicyL2Priority = _Me1200LldpmedConfigPolicyL2Priority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 4, 1, 5),
    _Me1200LldpmedConfigPolicyL2Priority_Type()
)
me1200LldpmedConfigPolicyL2Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyL2Priority.setStatus("current")


class _Me1200LldpmedConfigPolicyDscp_Type(ME1200Unsigned8):
    """Custom type me1200LldpmedConfigPolicyDscp based on ME1200Unsigned8"""
    subtypeSpec = ME1200Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Me1200LldpmedConfigPolicyDscp_Type.__name__ = "ME1200Unsigned8"
_Me1200LldpmedConfigPolicyDscp_Object = MibTableColumn
me1200LldpmedConfigPolicyDscp = _Me1200LldpmedConfigPolicyDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 4, 1, 6),
    _Me1200LldpmedConfigPolicyDscp_Type()
)
me1200LldpmedConfigPolicyDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyDscp.setStatus("current")
_Me1200LldpmedConfigPolicyAction_Type = ME1200RowEditorState
_Me1200LldpmedConfigPolicyAction_Object = MibTableColumn
me1200LldpmedConfigPolicyAction = _Me1200LldpmedConfigPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 4, 1, 100),
    _Me1200LldpmedConfigPolicyAction_Type()
)
me1200LldpmedConfigPolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyAction.setStatus("current")
_Me1200LldpmedConfigPolicyListTable_Object = MibTable
me1200LldpmedConfigPolicyListTable = _Me1200LldpmedConfigPolicyListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 5)
)
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyListTable.setStatus("current")
_Me1200LldpmedConfigPolicyListEntry_Object = MibTableRow
me1200LldpmedConfigPolicyListEntry = _Me1200LldpmedConfigPolicyListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 5, 1)
)
me1200LldpmedConfigPolicyListEntry.setIndexNames(
    (0, "ME1200-LLDPMED-MIB", "me1200LldpmedConfigPolicyListIfIndex"),
    (0, "ME1200-LLDPMED-MIB", "me1200LldpmedConfigPolicyListPolicyIndex"),
)
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyListEntry.setStatus("current")
_Me1200LldpmedConfigPolicyListIfIndex_Type = ME1200InterfaceIndex
_Me1200LldpmedConfigPolicyListIfIndex_Object = MibTableColumn
me1200LldpmedConfigPolicyListIfIndex = _Me1200LldpmedConfigPolicyListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 5, 1, 1),
    _Me1200LldpmedConfigPolicyListIfIndex_Type()
)
me1200LldpmedConfigPolicyListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyListIfIndex.setStatus("current")
_Me1200LldpmedConfigPolicyListPolicyIndex_Type = Integer32
_Me1200LldpmedConfigPolicyListPolicyIndex_Object = MibTableColumn
me1200LldpmedConfigPolicyListPolicyIndex = _Me1200LldpmedConfigPolicyListPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 5, 1, 2),
    _Me1200LldpmedConfigPolicyListPolicyIndex_Type()
)
me1200LldpmedConfigPolicyListPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyListPolicyIndex.setStatus("current")
_Me1200LldpmedConfigPolicyListLldpmedPoliciesList_Type = TruthValue
_Me1200LldpmedConfigPolicyListLldpmedPoliciesList_Object = MibTableColumn
me1200LldpmedConfigPolicyListLldpmedPoliciesList = _Me1200LldpmedConfigPolicyListLldpmedPoliciesList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 5, 1, 3),
    _Me1200LldpmedConfigPolicyListLldpmedPoliciesList_Type()
)
me1200LldpmedConfigPolicyListLldpmedPoliciesList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyListLldpmedPoliciesList.setStatus("current")
_Me1200LldpmedConfigPolicyRowEditor_ObjectIdentity = ObjectIdentity
me1200LldpmedConfigPolicyRowEditor = _Me1200LldpmedConfigPolicyRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 6)
)


class _Me1200LldpmedConfigPolicyRowEditorLldpmedPolicy_Type(Integer32):
    """Custom type me1200LldpmedConfigPolicyRowEditorLldpmedPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Me1200LldpmedConfigPolicyRowEditorLldpmedPolicy_Type.__name__ = "Integer32"
_Me1200LldpmedConfigPolicyRowEditorLldpmedPolicy_Object = MibScalar
me1200LldpmedConfigPolicyRowEditorLldpmedPolicy = _Me1200LldpmedConfigPolicyRowEditorLldpmedPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 6, 1),
    _Me1200LldpmedConfigPolicyRowEditorLldpmedPolicy_Type()
)
me1200LldpmedConfigPolicyRowEditorLldpmedPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyRowEditorLldpmedPolicy.setStatus("current")
_Me1200LldpmedConfigPolicyRowEditorApplicationType_Type = ME1200lldpmedRemoteNetworkPolicyApplicationType
_Me1200LldpmedConfigPolicyRowEditorApplicationType_Object = MibScalar
me1200LldpmedConfigPolicyRowEditorApplicationType = _Me1200LldpmedConfigPolicyRowEditorApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 6, 2),
    _Me1200LldpmedConfigPolicyRowEditorApplicationType_Type()
)
me1200LldpmedConfigPolicyRowEditorApplicationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyRowEditorApplicationType.setStatus("current")
_Me1200LldpmedConfigPolicyRowEditorTagged_Type = TruthValue
_Me1200LldpmedConfigPolicyRowEditorTagged_Object = MibScalar
me1200LldpmedConfigPolicyRowEditorTagged = _Me1200LldpmedConfigPolicyRowEditorTagged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 6, 3),
    _Me1200LldpmedConfigPolicyRowEditorTagged_Type()
)
me1200LldpmedConfigPolicyRowEditorTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyRowEditorTagged.setStatus("current")


class _Me1200LldpmedConfigPolicyRowEditorVlanId_Type(ME1200Unsigned16):
    """Custom type me1200LldpmedConfigPolicyRowEditorVlanId based on ME1200Unsigned16"""
    subtypeSpec = ME1200Unsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Me1200LldpmedConfigPolicyRowEditorVlanId_Type.__name__ = "ME1200Unsigned16"
_Me1200LldpmedConfigPolicyRowEditorVlanId_Object = MibScalar
me1200LldpmedConfigPolicyRowEditorVlanId = _Me1200LldpmedConfigPolicyRowEditorVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 6, 4),
    _Me1200LldpmedConfigPolicyRowEditorVlanId_Type()
)
me1200LldpmedConfigPolicyRowEditorVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyRowEditorVlanId.setStatus("current")


class _Me1200LldpmedConfigPolicyRowEditorL2Priority_Type(ME1200Unsigned8):
    """Custom type me1200LldpmedConfigPolicyRowEditorL2Priority based on ME1200Unsigned8"""
    subtypeSpec = ME1200Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Me1200LldpmedConfigPolicyRowEditorL2Priority_Type.__name__ = "ME1200Unsigned8"
_Me1200LldpmedConfigPolicyRowEditorL2Priority_Object = MibScalar
me1200LldpmedConfigPolicyRowEditorL2Priority = _Me1200LldpmedConfigPolicyRowEditorL2Priority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 6, 5),
    _Me1200LldpmedConfigPolicyRowEditorL2Priority_Type()
)
me1200LldpmedConfigPolicyRowEditorL2Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyRowEditorL2Priority.setStatus("current")


class _Me1200LldpmedConfigPolicyRowEditorDscp_Type(ME1200Unsigned8):
    """Custom type me1200LldpmedConfigPolicyRowEditorDscp based on ME1200Unsigned8"""
    subtypeSpec = ME1200Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Me1200LldpmedConfigPolicyRowEditorDscp_Type.__name__ = "ME1200Unsigned8"
_Me1200LldpmedConfigPolicyRowEditorDscp_Object = MibScalar
me1200LldpmedConfigPolicyRowEditorDscp = _Me1200LldpmedConfigPolicyRowEditorDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 6, 6),
    _Me1200LldpmedConfigPolicyRowEditorDscp_Type()
)
me1200LldpmedConfigPolicyRowEditorDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyRowEditorDscp.setStatus("current")
_Me1200LldpmedConfigPolicyRowEditorAction_Type = ME1200RowEditorState
_Me1200LldpmedConfigPolicyRowEditorAction_Object = MibScalar
me1200LldpmedConfigPolicyRowEditorAction = _Me1200LldpmedConfigPolicyRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 2, 6, 100),
    _Me1200LldpmedConfigPolicyRowEditorAction_Type()
)
me1200LldpmedConfigPolicyRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyRowEditorAction.setStatus("current")
_Me1200LldpmedStatus_ObjectIdentity = ObjectIdentity
me1200LldpmedStatus = _Me1200LldpmedStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3)
)
_Me1200LldpmedStatusRemoteDeviceInfoTable_Object = MibTable
me1200LldpmedStatusRemoteDeviceInfoTable = _Me1200LldpmedStatusRemoteDeviceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3)
)
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoTable.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceInfoEntry_Object = MibTableRow
me1200LldpmedStatusRemoteDeviceInfoEntry = _Me1200LldpmedStatusRemoteDeviceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1)
)
me1200LldpmedStatusRemoteDeviceInfoEntry.setIndexNames(
    (0, "ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoIfIndex"),
    (0, "ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoLldpmedIndex"),
)
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoEntry.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceInfoIfIndex_Type = ME1200InterfaceIndex
_Me1200LldpmedStatusRemoteDeviceInfoIfIndex_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoIfIndex = _Me1200LldpmedStatusRemoteDeviceInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 1),
    _Me1200LldpmedStatusRemoteDeviceInfoIfIndex_Type()
)
me1200LldpmedStatusRemoteDeviceInfoIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoIfIndex.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceInfoLldpmedIndex_Type(Integer32):
    """Custom type me1200LldpmedStatusRemoteDeviceInfoLldpmedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_Me1200LldpmedStatusRemoteDeviceInfoLldpmedIndex_Type.__name__ = "Integer32"
_Me1200LldpmedStatusRemoteDeviceInfoLldpmedIndex_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoLldpmedIndex = _Me1200LldpmedStatusRemoteDeviceInfoLldpmedIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 2),
    _Me1200LldpmedStatusRemoteDeviceInfoLldpmedIndex_Type()
)
me1200LldpmedStatusRemoteDeviceInfoLldpmedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoLldpmedIndex.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceInfoCapabilities_Type = ME1200Unsigned16
_Me1200LldpmedStatusRemoteDeviceInfoCapabilities_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoCapabilities = _Me1200LldpmedStatusRemoteDeviceInfoCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 4),
    _Me1200LldpmedStatusRemoteDeviceInfoCapabilities_Type()
)
me1200LldpmedStatusRemoteDeviceInfoCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoCapabilities.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceInfoCapabilitiesEnabled_Type = ME1200Unsigned16
_Me1200LldpmedStatusRemoteDeviceInfoCapabilitiesEnabled_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoCapabilitiesEnabled = _Me1200LldpmedStatusRemoteDeviceInfoCapabilitiesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 5),
    _Me1200LldpmedStatusRemoteDeviceInfoCapabilitiesEnabled_Type()
)
me1200LldpmedStatusRemoteDeviceInfoCapabilitiesEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoCapabilitiesEnabled.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceInfoLatitude_Type = ME1200Integer64
_Me1200LldpmedStatusRemoteDeviceInfoLatitude_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoLatitude = _Me1200LldpmedStatusRemoteDeviceInfoLatitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 6),
    _Me1200LldpmedStatusRemoteDeviceInfoLatitude_Type()
)
me1200LldpmedStatusRemoteDeviceInfoLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoLatitude.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceInfoLongitude_Type = ME1200Integer64
_Me1200LldpmedStatusRemoteDeviceInfoLongitude_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoLongitude = _Me1200LldpmedStatusRemoteDeviceInfoLongitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 7),
    _Me1200LldpmedStatusRemoteDeviceInfoLongitude_Type()
)
me1200LldpmedStatusRemoteDeviceInfoLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoLongitude.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceInfoAltitudeType_Type = ME1200lldpmedAltitudeType
_Me1200LldpmedStatusRemoteDeviceInfoAltitudeType_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoAltitudeType = _Me1200LldpmedStatusRemoteDeviceInfoAltitudeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 8),
    _Me1200LldpmedStatusRemoteDeviceInfoAltitudeType_Type()
)
me1200LldpmedStatusRemoteDeviceInfoAltitudeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoAltitudeType.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceInfoAltitude_Type = Integer32
_Me1200LldpmedStatusRemoteDeviceInfoAltitude_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoAltitude = _Me1200LldpmedStatusRemoteDeviceInfoAltitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 9),
    _Me1200LldpmedStatusRemoteDeviceInfoAltitude_Type()
)
me1200LldpmedStatusRemoteDeviceInfoAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoAltitude.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceInfoDatum_Type = ME1200lldpmedDatumType
_Me1200LldpmedStatusRemoteDeviceInfoDatum_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoDatum = _Me1200LldpmedStatusRemoteDeviceInfoDatum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 10),
    _Me1200LldpmedStatusRemoteDeviceInfoDatum_Type()
)
me1200LldpmedStatusRemoteDeviceInfoDatum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoDatum.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceInfoElinAddr_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceInfoElinAddr based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_Me1200LldpmedStatusRemoteDeviceInfoElinAddr_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceInfoElinAddr_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoElinAddr = _Me1200LldpmedStatusRemoteDeviceInfoElinAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 12),
    _Me1200LldpmedStatusRemoteDeviceInfoElinAddr_Type()
)
me1200LldpmedStatusRemoteDeviceInfoElinAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoElinAddr.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceInfoDeviceType_Type = ME1200lldpmedRemoteDeviceType
_Me1200LldpmedStatusRemoteDeviceInfoDeviceType_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoDeviceType = _Me1200LldpmedStatusRemoteDeviceInfoDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 13),
    _Me1200LldpmedStatusRemoteDeviceInfoDeviceType_Type()
)
me1200LldpmedStatusRemoteDeviceInfoDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoDeviceType.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceInfoHwRev_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceInfoHwRev based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Me1200LldpmedStatusRemoteDeviceInfoHwRev_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceInfoHwRev_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoHwRev = _Me1200LldpmedStatusRemoteDeviceInfoHwRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 14),
    _Me1200LldpmedStatusRemoteDeviceInfoHwRev_Type()
)
me1200LldpmedStatusRemoteDeviceInfoHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoHwRev.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceInfoFwRev_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceInfoFwRev based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Me1200LldpmedStatusRemoteDeviceInfoFwRev_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceInfoFwRev_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoFwRev = _Me1200LldpmedStatusRemoteDeviceInfoFwRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 15),
    _Me1200LldpmedStatusRemoteDeviceInfoFwRev_Type()
)
me1200LldpmedStatusRemoteDeviceInfoFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoFwRev.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceInfoSwRev_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceInfoSwRev based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Me1200LldpmedStatusRemoteDeviceInfoSwRev_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceInfoSwRev_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoSwRev = _Me1200LldpmedStatusRemoteDeviceInfoSwRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 16),
    _Me1200LldpmedStatusRemoteDeviceInfoSwRev_Type()
)
me1200LldpmedStatusRemoteDeviceInfoSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoSwRev.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceInfoSerialNo_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceInfoSerialNo based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Me1200LldpmedStatusRemoteDeviceInfoSerialNo_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceInfoSerialNo_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoSerialNo = _Me1200LldpmedStatusRemoteDeviceInfoSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 17),
    _Me1200LldpmedStatusRemoteDeviceInfoSerialNo_Type()
)
me1200LldpmedStatusRemoteDeviceInfoSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoSerialNo.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceInfoManufacturerName_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceInfoManufacturerName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Me1200LldpmedStatusRemoteDeviceInfoManufacturerName_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceInfoManufacturerName_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoManufacturerName = _Me1200LldpmedStatusRemoteDeviceInfoManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 18),
    _Me1200LldpmedStatusRemoteDeviceInfoManufacturerName_Type()
)
me1200LldpmedStatusRemoteDeviceInfoManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoManufacturerName.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceInfoModelName_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceInfoModelName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Me1200LldpmedStatusRemoteDeviceInfoModelName_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceInfoModelName_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoModelName = _Me1200LldpmedStatusRemoteDeviceInfoModelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 19),
    _Me1200LldpmedStatusRemoteDeviceInfoModelName_Type()
)
me1200LldpmedStatusRemoteDeviceInfoModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoModelName.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceInfoAssetId_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceInfoAssetId based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Me1200LldpmedStatusRemoteDeviceInfoAssetId_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceInfoAssetId_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoAssetId = _Me1200LldpmedStatusRemoteDeviceInfoAssetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 20),
    _Me1200LldpmedStatusRemoteDeviceInfoAssetId_Type()
)
me1200LldpmedStatusRemoteDeviceInfoAssetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoAssetId.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceInfoEeeRxTwSys_Type = ME1200Unsigned16
_Me1200LldpmedStatusRemoteDeviceInfoEeeRxTwSys_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoEeeRxTwSys = _Me1200LldpmedStatusRemoteDeviceInfoEeeRxTwSys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 21),
    _Me1200LldpmedStatusRemoteDeviceInfoEeeRxTwSys_Type()
)
me1200LldpmedStatusRemoteDeviceInfoEeeRxTwSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoEeeRxTwSys.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceInfoEeeTxTwSys_Type = ME1200Unsigned16
_Me1200LldpmedStatusRemoteDeviceInfoEeeTxTwSys_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoEeeTxTwSys = _Me1200LldpmedStatusRemoteDeviceInfoEeeTxTwSys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 22),
    _Me1200LldpmedStatusRemoteDeviceInfoEeeTxTwSys_Type()
)
me1200LldpmedStatusRemoteDeviceInfoEeeTxTwSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoEeeTxTwSys.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceInfoEeeFbTwSys_Type = ME1200Unsigned16
_Me1200LldpmedStatusRemoteDeviceInfoEeeFbTwSys_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoEeeFbTwSys = _Me1200LldpmedStatusRemoteDeviceInfoEeeFbTwSys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 23),
    _Me1200LldpmedStatusRemoteDeviceInfoEeeFbTwSys_Type()
)
me1200LldpmedStatusRemoteDeviceInfoEeeFbTwSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoEeeFbTwSys.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceInfoEeeTxTwSysEcho_Type = ME1200Unsigned16
_Me1200LldpmedStatusRemoteDeviceInfoEeeTxTwSysEcho_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoEeeTxTwSysEcho = _Me1200LldpmedStatusRemoteDeviceInfoEeeTxTwSysEcho_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 24),
    _Me1200LldpmedStatusRemoteDeviceInfoEeeTxTwSysEcho_Type()
)
me1200LldpmedStatusRemoteDeviceInfoEeeTxTwSysEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoEeeTxTwSysEcho.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceInfoEeeRxTwSysEcho_Type = ME1200Unsigned16
_Me1200LldpmedStatusRemoteDeviceInfoEeeRxTwSysEcho_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceInfoEeeRxTwSysEcho = _Me1200LldpmedStatusRemoteDeviceInfoEeeRxTwSysEcho_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 3, 1, 25),
    _Me1200LldpmedStatusRemoteDeviceInfoEeeRxTwSysEcho_Type()
)
me1200LldpmedStatusRemoteDeviceInfoEeeRxTwSysEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoEeeRxTwSysEcho.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceLocInfoTable_Object = MibTable
me1200LldpmedStatusRemoteDeviceLocInfoTable = _Me1200LldpmedStatusRemoteDeviceLocInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4)
)
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoTable.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceLocInfoEntry_Object = MibTableRow
me1200LldpmedStatusRemoteDeviceLocInfoEntry = _Me1200LldpmedStatusRemoteDeviceLocInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1)
)
me1200LldpmedStatusRemoteDeviceLocInfoEntry.setIndexNames(
    (0, "ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoIfIndex"),
    (0, "ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoLldpmedIndex"),
)
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoEntry.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceLocInfoIfIndex_Type = ME1200InterfaceIndex
_Me1200LldpmedStatusRemoteDeviceLocInfoIfIndex_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoIfIndex = _Me1200LldpmedStatusRemoteDeviceLocInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 1),
    _Me1200LldpmedStatusRemoteDeviceLocInfoIfIndex_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoIfIndex.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoLldpmedIndex_Type(Integer32):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoLldpmedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoLldpmedIndex_Type.__name__ = "Integer32"
_Me1200LldpmedStatusRemoteDeviceLocInfoLldpmedIndex_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoLldpmedIndex = _Me1200LldpmedStatusRemoteDeviceLocInfoLldpmedIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 2),
    _Me1200LldpmedStatusRemoteDeviceLocInfoLldpmedIndex_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoLldpmedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoLldpmedIndex.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoState_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoState based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoState_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoState_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoState = _Me1200LldpmedStatusRemoteDeviceLocInfoState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 5),
    _Me1200LldpmedStatusRemoteDeviceLocInfoState_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoState.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoCounty_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoCounty based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoCounty_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoCounty_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoCounty = _Me1200LldpmedStatusRemoteDeviceLocInfoCounty_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 6),
    _Me1200LldpmedStatusRemoteDeviceLocInfoCounty_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoCounty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoCounty.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoCity_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoCity based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoCity_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoCity_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoCity = _Me1200LldpmedStatusRemoteDeviceLocInfoCity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 7),
    _Me1200LldpmedStatusRemoteDeviceLocInfoCity_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoCity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoCity.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoCityDistrict_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoCityDistrict based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoCityDistrict_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoCityDistrict_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoCityDistrict = _Me1200LldpmedStatusRemoteDeviceLocInfoCityDistrict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 8),
    _Me1200LldpmedStatusRemoteDeviceLocInfoCityDistrict_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoCityDistrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoCityDistrict.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoBlock_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoBlock based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoBlock_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoBlock_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoBlock = _Me1200LldpmedStatusRemoteDeviceLocInfoBlock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 9),
    _Me1200LldpmedStatusRemoteDeviceLocInfoBlock_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoBlock.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoStreet_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoStreet based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoStreet_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoStreet_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoStreet = _Me1200LldpmedStatusRemoteDeviceLocInfoStreet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 10),
    _Me1200LldpmedStatusRemoteDeviceLocInfoStreet_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoStreet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoStreet.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoLeadingStreetDirection_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoLeadingStreetDirection based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoLeadingStreetDirection_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoLeadingStreetDirection_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoLeadingStreetDirection = _Me1200LldpmedStatusRemoteDeviceLocInfoLeadingStreetDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 11),
    _Me1200LldpmedStatusRemoteDeviceLocInfoLeadingStreetDirection_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoLeadingStreetDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoLeadingStreetDirection.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoTrailingStreetSuffix_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoTrailingStreetSuffix based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoTrailingStreetSuffix_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoTrailingStreetSuffix_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoTrailingStreetSuffix = _Me1200LldpmedStatusRemoteDeviceLocInfoTrailingStreetSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 12),
    _Me1200LldpmedStatusRemoteDeviceLocInfoTrailingStreetSuffix_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoTrailingStreetSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoTrailingStreetSuffix.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoStreetSuffix_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoStreetSuffix based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoStreetSuffix_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoStreetSuffix_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoStreetSuffix = _Me1200LldpmedStatusRemoteDeviceLocInfoStreetSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 13),
    _Me1200LldpmedStatusRemoteDeviceLocInfoStreetSuffix_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoStreetSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoStreetSuffix.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoHouseNo_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoHouseNo based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoHouseNo_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoHouseNo_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoHouseNo = _Me1200LldpmedStatusRemoteDeviceLocInfoHouseNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 14),
    _Me1200LldpmedStatusRemoteDeviceLocInfoHouseNo_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoHouseNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoHouseNo.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoHouseNoSuffix_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoHouseNoSuffix based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoHouseNoSuffix_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoHouseNoSuffix_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoHouseNoSuffix = _Me1200LldpmedStatusRemoteDeviceLocInfoHouseNoSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 15),
    _Me1200LldpmedStatusRemoteDeviceLocInfoHouseNoSuffix_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoHouseNoSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoHouseNoSuffix.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoLandmark_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoLandmark based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoLandmark_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoLandmark_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoLandmark = _Me1200LldpmedStatusRemoteDeviceLocInfoLandmark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 16),
    _Me1200LldpmedStatusRemoteDeviceLocInfoLandmark_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoLandmark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoLandmark.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoAdditionalInfo_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoAdditionalInfo based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoAdditionalInfo_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoAdditionalInfo_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoAdditionalInfo = _Me1200LldpmedStatusRemoteDeviceLocInfoAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 17),
    _Me1200LldpmedStatusRemoteDeviceLocInfoAdditionalInfo_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoAdditionalInfo.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoName_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoName_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoName_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoName = _Me1200LldpmedStatusRemoteDeviceLocInfoName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 18),
    _Me1200LldpmedStatusRemoteDeviceLocInfoName_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoName.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoZipCode_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoZipCode based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoZipCode_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoZipCode_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoZipCode = _Me1200LldpmedStatusRemoteDeviceLocInfoZipCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 19),
    _Me1200LldpmedStatusRemoteDeviceLocInfoZipCode_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoZipCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoZipCode.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoBuilding_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoBuilding based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoBuilding_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoBuilding_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoBuilding = _Me1200LldpmedStatusRemoteDeviceLocInfoBuilding_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 20),
    _Me1200LldpmedStatusRemoteDeviceLocInfoBuilding_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoBuilding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoBuilding.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoApartment_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoApartment based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoApartment_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoApartment_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoApartment = _Me1200LldpmedStatusRemoteDeviceLocInfoApartment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 21),
    _Me1200LldpmedStatusRemoteDeviceLocInfoApartment_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoApartment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoApartment.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoFloor_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoFloor based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoFloor_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoFloor_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoFloor = _Me1200LldpmedStatusRemoteDeviceLocInfoFloor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 22),
    _Me1200LldpmedStatusRemoteDeviceLocInfoFloor_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoFloor.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoRoomNumber_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoRoomNumber based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoRoomNumber_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoRoomNumber_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoRoomNumber = _Me1200LldpmedStatusRemoteDeviceLocInfoRoomNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 23),
    _Me1200LldpmedStatusRemoteDeviceLocInfoRoomNumber_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoRoomNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoRoomNumber.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoPlaceType_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoPlaceType based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoPlaceType_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoPlaceType_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoPlaceType = _Me1200LldpmedStatusRemoteDeviceLocInfoPlaceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 24),
    _Me1200LldpmedStatusRemoteDeviceLocInfoPlaceType_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoPlaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoPlaceType.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoPostalCommunityName_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoPostalCommunityName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoPostalCommunityName_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoPostalCommunityName_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoPostalCommunityName = _Me1200LldpmedStatusRemoteDeviceLocInfoPostalCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 25),
    _Me1200LldpmedStatusRemoteDeviceLocInfoPostalCommunityName_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoPostalCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoPostalCommunityName.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoPoBox_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoPoBox based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoPoBox_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoPoBox_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoPoBox = _Me1200LldpmedStatusRemoteDeviceLocInfoPoBox_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 26),
    _Me1200LldpmedStatusRemoteDeviceLocInfoPoBox_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoPoBox.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoPoBox.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoAdditionalCode_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoAdditionalCode based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoAdditionalCode_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoAdditionalCode_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoAdditionalCode = _Me1200LldpmedStatusRemoteDeviceLocInfoAdditionalCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 27),
    _Me1200LldpmedStatusRemoteDeviceLocInfoAdditionalCode_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoAdditionalCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoAdditionalCode.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceLocInfoCountryCode_Type(ME1200DisplayString):
    """Custom type me1200LldpmedStatusRemoteDeviceLocInfoCountryCode based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_Me1200LldpmedStatusRemoteDeviceLocInfoCountryCode_Type.__name__ = "ME1200DisplayString"
_Me1200LldpmedStatusRemoteDeviceLocInfoCountryCode_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceLocInfoCountryCode = _Me1200LldpmedStatusRemoteDeviceLocInfoCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 4, 1, 28),
    _Me1200LldpmedStatusRemoteDeviceLocInfoCountryCode_Type()
)
me1200LldpmedStatusRemoteDeviceLocInfoCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoCountryCode.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoTable_Object = MibTable
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoTable = _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 5)
)
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoTable.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoEntry_Object = MibTableRow
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoEntry = _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 5, 1)
)
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoEntry.setIndexNames(
    (0, "ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoIfIndex"),
    (0, "ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoLldpmedIndex"),
    (0, "ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoPolicyIndex"),
)
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoEntry.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoIfIndex_Type = ME1200InterfaceIndex
_Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoIfIndex_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoIfIndex = _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 5, 1, 1),
    _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoIfIndex_Type()
)
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoIfIndex.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoLldpmedIndex_Type(Integer32):
    """Custom type me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoLldpmedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoLldpmedIndex_Type.__name__ = "Integer32"
_Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoLldpmedIndex_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoLldpmedIndex = _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoLldpmedIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 5, 1, 2),
    _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoLldpmedIndex_Type()
)
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoLldpmedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoLldpmedIndex.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoPolicyIndex_Type = Integer32
_Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoPolicyIndex_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoPolicyIndex = _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 5, 1, 3),
    _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoPolicyIndex_Type()
)
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoPolicyIndex.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoApplicationType_Type = ME1200lldpmedRemoteNetworkPolicyApplicationType
_Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoApplicationType_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoApplicationType = _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 5, 1, 5),
    _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoApplicationType_Type()
)
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoApplicationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoApplicationType.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoUnknownPolicy_Type = TruthValue
_Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoUnknownPolicy_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoUnknownPolicy = _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoUnknownPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 5, 1, 6),
    _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoUnknownPolicy_Type()
)
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoUnknownPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoUnknownPolicy.setStatus("current")
_Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoTagged_Type = TruthValue
_Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoTagged_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoTagged = _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoTagged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 5, 1, 7),
    _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoTagged_Type()
)
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoTagged.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoVlanId_Type(ME1200Unsigned16):
    """Custom type me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoVlanId based on ME1200Unsigned16"""
    subtypeSpec = ME1200Unsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoVlanId_Type.__name__ = "ME1200Unsigned16"
_Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoVlanId_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoVlanId = _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 5, 1, 8),
    _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoVlanId_Type()
)
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoVlanId.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoL2Priority_Type(ME1200Unsigned8):
    """Custom type me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoL2Priority based on ME1200Unsigned8"""
    subtypeSpec = ME1200Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoL2Priority_Type.__name__ = "ME1200Unsigned8"
_Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoL2Priority_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoL2Priority = _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoL2Priority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 5, 1, 9),
    _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoL2Priority_Type()
)
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoL2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoL2Priority.setStatus("current")


class _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoDscp_Type(ME1200Unsigned8):
    """Custom type me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoDscp based on ME1200Unsigned8"""
    subtypeSpec = ME1200Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoDscp_Type.__name__ = "ME1200Unsigned8"
_Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoDscp_Object = MibTableColumn
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoDscp = _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 3, 5, 1, 10),
    _Me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoDscp_Type()
)
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoDscp.setStatus("current")
_Me1200LldpmedControl_ObjectIdentity = ObjectIdentity
me1200LldpmedControl = _Me1200LldpmedControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 1, 4)
)
_Me1200LldpmedMibConformance_ObjectIdentity = ObjectIdentity
me1200LldpmedMibConformance = _Me1200LldpmedMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 2)
)
_Me1200LldpmedMibCompliances_ObjectIdentity = ObjectIdentity
me1200LldpmedMibCompliances = _Me1200LldpmedMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 2, 1)
)
_Me1200LldpmedMibGroups_ObjectIdentity = ObjectIdentity
me1200LldpmedMibGroups = _Me1200LldpmedMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 2, 2)
)

# Managed Objects groups

me1200LldpmedConfigGlobalInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 2, 2, 1)
)
me1200LldpmedConfigGlobalInfoGroup.setObjects(
      *(("ME1200-LLDPMED-MIB", "me1200LldpmedConfigGlobalFastRepeatCount"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigGlobalLatitude"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigGlobalLongitude"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigGlobalAltitudeType"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigGlobalAltitude"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigGlobalElinAddr"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigGlobalDatum"))
)
if mibBuilder.loadTexts:
    me1200LldpmedConfigGlobalInfoGroup.setStatus("current")

me1200LldpmedConfigLocationInformationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 2, 2, 2)
)
me1200LldpmedConfigLocationInformationInfoGroup.setObjects(
      *(("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationState"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationCounty"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationCity"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationCityDistrict"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationBlock"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationStreet"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationLeadingStreetDirection"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationTrailingStreetSuffix"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationStreetSuffix"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationHouseNo"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationHouseNoSuffix"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationLandmark"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationAdditionalInfo"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationName"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationZipCode"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationBuilding"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationApartment"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationFloor"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationRoomNumber"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationPlaceType"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationPostalCommunityName"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationPoBox"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationAdditionalCode"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationCountryCode"))
)
if mibBuilder.loadTexts:
    me1200LldpmedConfigLocationInformationInfoGroup.setStatus("current")

me1200LldpmedConfigInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 2, 2, 3)
)
me1200LldpmedConfigInfoGroup.setObjects(
      *(("ME1200-LLDPMED-MIB", "me1200LldpmedConfigOptionalTlvs"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigDeviceType"))
)
if mibBuilder.loadTexts:
    me1200LldpmedConfigInfoGroup.setStatus("current")

me1200LldpmedConfigPolicyInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 2, 2, 4)
)
me1200LldpmedConfigPolicyInfoGroup.setObjects(
      *(("ME1200-LLDPMED-MIB", "me1200LldpmedConfigPolicyApplicationType"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigPolicyTagged"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigPolicyVlanId"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigPolicyL2Priority"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigPolicyDscp"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigPolicyAction"))
)
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyInfoGroup.setStatus("current")

me1200LldpmedConfigPolicyListInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 2, 2, 5)
)
me1200LldpmedConfigPolicyListInfoGroup.setObjects(
    ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigPolicyListLldpmedPoliciesList")
)
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyListInfoGroup.setStatus("current")

me1200LldpmedConfigPolicyRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 2, 2, 6)
)
me1200LldpmedConfigPolicyRowEditorInfoGroup.setObjects(
      *(("ME1200-LLDPMED-MIB", "me1200LldpmedConfigPolicyRowEditorLldpmedPolicy"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigPolicyRowEditorApplicationType"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigPolicyRowEditorTagged"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigPolicyRowEditorVlanId"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigPolicyRowEditorL2Priority"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigPolicyRowEditorDscp"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigPolicyRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200LldpmedConfigPolicyRowEditorInfoGroup.setStatus("current")

me1200LldpmedStatusRemoteDeviceInfoInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 2, 2, 7)
)
me1200LldpmedStatusRemoteDeviceInfoInfoGroup.setObjects(
      *(("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoCapabilities"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoCapabilitiesEnabled"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoLatitude"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoLongitude"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoAltitudeType"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoAltitude"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoDatum"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoElinAddr"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoDeviceType"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoHwRev"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoFwRev"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoSwRev"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoSerialNo"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoManufacturerName"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoModelName"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoAssetId"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoEeeRxTwSys"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoEeeTxTwSys"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoEeeFbTwSys"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoEeeTxTwSysEcho"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoEeeRxTwSysEcho"))
)
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceInfoInfoGroup.setStatus("current")

me1200LldpmedStatusRemoteDeviceLocInfoInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 2, 2, 8)
)
me1200LldpmedStatusRemoteDeviceLocInfoInfoGroup.setObjects(
      *(("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoState"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoCounty"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoCity"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoCityDistrict"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoBlock"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoStreet"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoLeadingStreetDirection"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoTrailingStreetSuffix"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoStreetSuffix"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoHouseNo"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoHouseNoSuffix"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoLandmark"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoAdditionalInfo"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoName"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoZipCode"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoBuilding"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoApartment"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoFloor"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoRoomNumber"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoPlaceType"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoPostalCommunityName"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoPoBox"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoAdditionalCode"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoCountryCode"))
)
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceLocInfoInfoGroup.setStatus("current")

me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 2, 2, 9)
)
me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoInfoGroup.setObjects(
      *(("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoApplicationType"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoUnknownPolicy"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoTagged"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoVlanId"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoL2Priority"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoDscp"))
)
if mibBuilder.loadTexts:
    me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200LldpmedMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 71, 2, 1, 1)
)
me1200LldpmedMibCompliance.setObjects(
      *(("ME1200-LLDPMED-MIB", "me1200LldpmedConfigGlobalInfoGroup"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigLocationInformationInfoGroup"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigInfoGroup"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigPolicyInfoGroup"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigPolicyListInfoGroup"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedConfigPolicyRowEditorInfoGroup"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceInfoInfoGroup"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceLocInfoInfoGroup"),
        ("ME1200-LLDPMED-MIB", "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200LldpmedMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-LLDPMED-MIB",
    **{"ME1200lldpmedAltitudeType": ME1200lldpmedAltitudeType,
       "ME1200lldpmedDatumType": ME1200lldpmedDatumType,
       "ME1200lldpmedDeviceType": ME1200lldpmedDeviceType,
       "ME1200lldpmedRemoteDeviceType": ME1200lldpmedRemoteDeviceType,
       "ME1200lldpmedRemoteNetworkPolicyApplicationType": ME1200lldpmedRemoteNetworkPolicyApplicationType,
       "me1200LldpmedMib": me1200LldpmedMib,
       "me1200LldpmedMibObjects": me1200LldpmedMibObjects,
       "me1200LldpmedConfig": me1200LldpmedConfig,
       "me1200LldpmedConfigGlobal": me1200LldpmedConfigGlobal,
       "me1200LldpmedConfigGlobalFastRepeatCount": me1200LldpmedConfigGlobalFastRepeatCount,
       "me1200LldpmedConfigGlobalLatitude": me1200LldpmedConfigGlobalLatitude,
       "me1200LldpmedConfigGlobalLongitude": me1200LldpmedConfigGlobalLongitude,
       "me1200LldpmedConfigGlobalAltitudeType": me1200LldpmedConfigGlobalAltitudeType,
       "me1200LldpmedConfigGlobalAltitude": me1200LldpmedConfigGlobalAltitude,
       "me1200LldpmedConfigGlobalElinAddr": me1200LldpmedConfigGlobalElinAddr,
       "me1200LldpmedConfigGlobalDatum": me1200LldpmedConfigGlobalDatum,
       "me1200LldpmedConfigLocationInformation": me1200LldpmedConfigLocationInformation,
       "me1200LldpmedConfigLocationInformationState": me1200LldpmedConfigLocationInformationState,
       "me1200LldpmedConfigLocationInformationCounty": me1200LldpmedConfigLocationInformationCounty,
       "me1200LldpmedConfigLocationInformationCity": me1200LldpmedConfigLocationInformationCity,
       "me1200LldpmedConfigLocationInformationCityDistrict": me1200LldpmedConfigLocationInformationCityDistrict,
       "me1200LldpmedConfigLocationInformationBlock": me1200LldpmedConfigLocationInformationBlock,
       "me1200LldpmedConfigLocationInformationStreet": me1200LldpmedConfigLocationInformationStreet,
       "me1200LldpmedConfigLocationInformationLeadingStreetDirection": me1200LldpmedConfigLocationInformationLeadingStreetDirection,
       "me1200LldpmedConfigLocationInformationTrailingStreetSuffix": me1200LldpmedConfigLocationInformationTrailingStreetSuffix,
       "me1200LldpmedConfigLocationInformationStreetSuffix": me1200LldpmedConfigLocationInformationStreetSuffix,
       "me1200LldpmedConfigLocationInformationHouseNo": me1200LldpmedConfigLocationInformationHouseNo,
       "me1200LldpmedConfigLocationInformationHouseNoSuffix": me1200LldpmedConfigLocationInformationHouseNoSuffix,
       "me1200LldpmedConfigLocationInformationLandmark": me1200LldpmedConfigLocationInformationLandmark,
       "me1200LldpmedConfigLocationInformationAdditionalInfo": me1200LldpmedConfigLocationInformationAdditionalInfo,
       "me1200LldpmedConfigLocationInformationName": me1200LldpmedConfigLocationInformationName,
       "me1200LldpmedConfigLocationInformationZipCode": me1200LldpmedConfigLocationInformationZipCode,
       "me1200LldpmedConfigLocationInformationBuilding": me1200LldpmedConfigLocationInformationBuilding,
       "me1200LldpmedConfigLocationInformationApartment": me1200LldpmedConfigLocationInformationApartment,
       "me1200LldpmedConfigLocationInformationFloor": me1200LldpmedConfigLocationInformationFloor,
       "me1200LldpmedConfigLocationInformationRoomNumber": me1200LldpmedConfigLocationInformationRoomNumber,
       "me1200LldpmedConfigLocationInformationPlaceType": me1200LldpmedConfigLocationInformationPlaceType,
       "me1200LldpmedConfigLocationInformationPostalCommunityName": me1200LldpmedConfigLocationInformationPostalCommunityName,
       "me1200LldpmedConfigLocationInformationPoBox": me1200LldpmedConfigLocationInformationPoBox,
       "me1200LldpmedConfigLocationInformationAdditionalCode": me1200LldpmedConfigLocationInformationAdditionalCode,
       "me1200LldpmedConfigLocationInformationCountryCode": me1200LldpmedConfigLocationInformationCountryCode,
       "me1200LldpmedConfigTable": me1200LldpmedConfigTable,
       "me1200LldpmedConfigEntry": me1200LldpmedConfigEntry,
       "me1200LldpmedConfigIfIndex": me1200LldpmedConfigIfIndex,
       "me1200LldpmedConfigOptionalTlvs": me1200LldpmedConfigOptionalTlvs,
       "me1200LldpmedConfigDeviceType": me1200LldpmedConfigDeviceType,
       "me1200LldpmedConfigPolicyTable": me1200LldpmedConfigPolicyTable,
       "me1200LldpmedConfigPolicyEntry": me1200LldpmedConfigPolicyEntry,
       "me1200LldpmedConfigPolicyLldpmedPolicy": me1200LldpmedConfigPolicyLldpmedPolicy,
       "me1200LldpmedConfigPolicyApplicationType": me1200LldpmedConfigPolicyApplicationType,
       "me1200LldpmedConfigPolicyTagged": me1200LldpmedConfigPolicyTagged,
       "me1200LldpmedConfigPolicyVlanId": me1200LldpmedConfigPolicyVlanId,
       "me1200LldpmedConfigPolicyL2Priority": me1200LldpmedConfigPolicyL2Priority,
       "me1200LldpmedConfigPolicyDscp": me1200LldpmedConfigPolicyDscp,
       "me1200LldpmedConfigPolicyAction": me1200LldpmedConfigPolicyAction,
       "me1200LldpmedConfigPolicyListTable": me1200LldpmedConfigPolicyListTable,
       "me1200LldpmedConfigPolicyListEntry": me1200LldpmedConfigPolicyListEntry,
       "me1200LldpmedConfigPolicyListIfIndex": me1200LldpmedConfigPolicyListIfIndex,
       "me1200LldpmedConfigPolicyListPolicyIndex": me1200LldpmedConfigPolicyListPolicyIndex,
       "me1200LldpmedConfigPolicyListLldpmedPoliciesList": me1200LldpmedConfigPolicyListLldpmedPoliciesList,
       "me1200LldpmedConfigPolicyRowEditor": me1200LldpmedConfigPolicyRowEditor,
       "me1200LldpmedConfigPolicyRowEditorLldpmedPolicy": me1200LldpmedConfigPolicyRowEditorLldpmedPolicy,
       "me1200LldpmedConfigPolicyRowEditorApplicationType": me1200LldpmedConfigPolicyRowEditorApplicationType,
       "me1200LldpmedConfigPolicyRowEditorTagged": me1200LldpmedConfigPolicyRowEditorTagged,
       "me1200LldpmedConfigPolicyRowEditorVlanId": me1200LldpmedConfigPolicyRowEditorVlanId,
       "me1200LldpmedConfigPolicyRowEditorL2Priority": me1200LldpmedConfigPolicyRowEditorL2Priority,
       "me1200LldpmedConfigPolicyRowEditorDscp": me1200LldpmedConfigPolicyRowEditorDscp,
       "me1200LldpmedConfigPolicyRowEditorAction": me1200LldpmedConfigPolicyRowEditorAction,
       "me1200LldpmedStatus": me1200LldpmedStatus,
       "me1200LldpmedStatusRemoteDeviceInfoTable": me1200LldpmedStatusRemoteDeviceInfoTable,
       "me1200LldpmedStatusRemoteDeviceInfoEntry": me1200LldpmedStatusRemoteDeviceInfoEntry,
       "me1200LldpmedStatusRemoteDeviceInfoIfIndex": me1200LldpmedStatusRemoteDeviceInfoIfIndex,
       "me1200LldpmedStatusRemoteDeviceInfoLldpmedIndex": me1200LldpmedStatusRemoteDeviceInfoLldpmedIndex,
       "me1200LldpmedStatusRemoteDeviceInfoCapabilities": me1200LldpmedStatusRemoteDeviceInfoCapabilities,
       "me1200LldpmedStatusRemoteDeviceInfoCapabilitiesEnabled": me1200LldpmedStatusRemoteDeviceInfoCapabilitiesEnabled,
       "me1200LldpmedStatusRemoteDeviceInfoLatitude": me1200LldpmedStatusRemoteDeviceInfoLatitude,
       "me1200LldpmedStatusRemoteDeviceInfoLongitude": me1200LldpmedStatusRemoteDeviceInfoLongitude,
       "me1200LldpmedStatusRemoteDeviceInfoAltitudeType": me1200LldpmedStatusRemoteDeviceInfoAltitudeType,
       "me1200LldpmedStatusRemoteDeviceInfoAltitude": me1200LldpmedStatusRemoteDeviceInfoAltitude,
       "me1200LldpmedStatusRemoteDeviceInfoDatum": me1200LldpmedStatusRemoteDeviceInfoDatum,
       "me1200LldpmedStatusRemoteDeviceInfoElinAddr": me1200LldpmedStatusRemoteDeviceInfoElinAddr,
       "me1200LldpmedStatusRemoteDeviceInfoDeviceType": me1200LldpmedStatusRemoteDeviceInfoDeviceType,
       "me1200LldpmedStatusRemoteDeviceInfoHwRev": me1200LldpmedStatusRemoteDeviceInfoHwRev,
       "me1200LldpmedStatusRemoteDeviceInfoFwRev": me1200LldpmedStatusRemoteDeviceInfoFwRev,
       "me1200LldpmedStatusRemoteDeviceInfoSwRev": me1200LldpmedStatusRemoteDeviceInfoSwRev,
       "me1200LldpmedStatusRemoteDeviceInfoSerialNo": me1200LldpmedStatusRemoteDeviceInfoSerialNo,
       "me1200LldpmedStatusRemoteDeviceInfoManufacturerName": me1200LldpmedStatusRemoteDeviceInfoManufacturerName,
       "me1200LldpmedStatusRemoteDeviceInfoModelName": me1200LldpmedStatusRemoteDeviceInfoModelName,
       "me1200LldpmedStatusRemoteDeviceInfoAssetId": me1200LldpmedStatusRemoteDeviceInfoAssetId,
       "me1200LldpmedStatusRemoteDeviceInfoEeeRxTwSys": me1200LldpmedStatusRemoteDeviceInfoEeeRxTwSys,
       "me1200LldpmedStatusRemoteDeviceInfoEeeTxTwSys": me1200LldpmedStatusRemoteDeviceInfoEeeTxTwSys,
       "me1200LldpmedStatusRemoteDeviceInfoEeeFbTwSys": me1200LldpmedStatusRemoteDeviceInfoEeeFbTwSys,
       "me1200LldpmedStatusRemoteDeviceInfoEeeTxTwSysEcho": me1200LldpmedStatusRemoteDeviceInfoEeeTxTwSysEcho,
       "me1200LldpmedStatusRemoteDeviceInfoEeeRxTwSysEcho": me1200LldpmedStatusRemoteDeviceInfoEeeRxTwSysEcho,
       "me1200LldpmedStatusRemoteDeviceLocInfoTable": me1200LldpmedStatusRemoteDeviceLocInfoTable,
       "me1200LldpmedStatusRemoteDeviceLocInfoEntry": me1200LldpmedStatusRemoteDeviceLocInfoEntry,
       "me1200LldpmedStatusRemoteDeviceLocInfoIfIndex": me1200LldpmedStatusRemoteDeviceLocInfoIfIndex,
       "me1200LldpmedStatusRemoteDeviceLocInfoLldpmedIndex": me1200LldpmedStatusRemoteDeviceLocInfoLldpmedIndex,
       "me1200LldpmedStatusRemoteDeviceLocInfoState": me1200LldpmedStatusRemoteDeviceLocInfoState,
       "me1200LldpmedStatusRemoteDeviceLocInfoCounty": me1200LldpmedStatusRemoteDeviceLocInfoCounty,
       "me1200LldpmedStatusRemoteDeviceLocInfoCity": me1200LldpmedStatusRemoteDeviceLocInfoCity,
       "me1200LldpmedStatusRemoteDeviceLocInfoCityDistrict": me1200LldpmedStatusRemoteDeviceLocInfoCityDistrict,
       "me1200LldpmedStatusRemoteDeviceLocInfoBlock": me1200LldpmedStatusRemoteDeviceLocInfoBlock,
       "me1200LldpmedStatusRemoteDeviceLocInfoStreet": me1200LldpmedStatusRemoteDeviceLocInfoStreet,
       "me1200LldpmedStatusRemoteDeviceLocInfoLeadingStreetDirection": me1200LldpmedStatusRemoteDeviceLocInfoLeadingStreetDirection,
       "me1200LldpmedStatusRemoteDeviceLocInfoTrailingStreetSuffix": me1200LldpmedStatusRemoteDeviceLocInfoTrailingStreetSuffix,
       "me1200LldpmedStatusRemoteDeviceLocInfoStreetSuffix": me1200LldpmedStatusRemoteDeviceLocInfoStreetSuffix,
       "me1200LldpmedStatusRemoteDeviceLocInfoHouseNo": me1200LldpmedStatusRemoteDeviceLocInfoHouseNo,
       "me1200LldpmedStatusRemoteDeviceLocInfoHouseNoSuffix": me1200LldpmedStatusRemoteDeviceLocInfoHouseNoSuffix,
       "me1200LldpmedStatusRemoteDeviceLocInfoLandmark": me1200LldpmedStatusRemoteDeviceLocInfoLandmark,
       "me1200LldpmedStatusRemoteDeviceLocInfoAdditionalInfo": me1200LldpmedStatusRemoteDeviceLocInfoAdditionalInfo,
       "me1200LldpmedStatusRemoteDeviceLocInfoName": me1200LldpmedStatusRemoteDeviceLocInfoName,
       "me1200LldpmedStatusRemoteDeviceLocInfoZipCode": me1200LldpmedStatusRemoteDeviceLocInfoZipCode,
       "me1200LldpmedStatusRemoteDeviceLocInfoBuilding": me1200LldpmedStatusRemoteDeviceLocInfoBuilding,
       "me1200LldpmedStatusRemoteDeviceLocInfoApartment": me1200LldpmedStatusRemoteDeviceLocInfoApartment,
       "me1200LldpmedStatusRemoteDeviceLocInfoFloor": me1200LldpmedStatusRemoteDeviceLocInfoFloor,
       "me1200LldpmedStatusRemoteDeviceLocInfoRoomNumber": me1200LldpmedStatusRemoteDeviceLocInfoRoomNumber,
       "me1200LldpmedStatusRemoteDeviceLocInfoPlaceType": me1200LldpmedStatusRemoteDeviceLocInfoPlaceType,
       "me1200LldpmedStatusRemoteDeviceLocInfoPostalCommunityName": me1200LldpmedStatusRemoteDeviceLocInfoPostalCommunityName,
       "me1200LldpmedStatusRemoteDeviceLocInfoPoBox": me1200LldpmedStatusRemoteDeviceLocInfoPoBox,
       "me1200LldpmedStatusRemoteDeviceLocInfoAdditionalCode": me1200LldpmedStatusRemoteDeviceLocInfoAdditionalCode,
       "me1200LldpmedStatusRemoteDeviceLocInfoCountryCode": me1200LldpmedStatusRemoteDeviceLocInfoCountryCode,
       "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoTable": me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoTable,
       "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoEntry": me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoEntry,
       "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoIfIndex": me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoIfIndex,
       "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoLldpmedIndex": me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoLldpmedIndex,
       "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoPolicyIndex": me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoPolicyIndex,
       "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoApplicationType": me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoApplicationType,
       "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoUnknownPolicy": me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoUnknownPolicy,
       "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoTagged": me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoTagged,
       "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoVlanId": me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoVlanId,
       "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoL2Priority": me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoL2Priority,
       "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoDscp": me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoDscp,
       "me1200LldpmedControl": me1200LldpmedControl,
       "me1200LldpmedMibConformance": me1200LldpmedMibConformance,
       "me1200LldpmedMibCompliances": me1200LldpmedMibCompliances,
       "me1200LldpmedMibCompliance": me1200LldpmedMibCompliance,
       "me1200LldpmedMibGroups": me1200LldpmedMibGroups,
       "me1200LldpmedConfigGlobalInfoGroup": me1200LldpmedConfigGlobalInfoGroup,
       "me1200LldpmedConfigLocationInformationInfoGroup": me1200LldpmedConfigLocationInformationInfoGroup,
       "me1200LldpmedConfigInfoGroup": me1200LldpmedConfigInfoGroup,
       "me1200LldpmedConfigPolicyInfoGroup": me1200LldpmedConfigPolicyInfoGroup,
       "me1200LldpmedConfigPolicyListInfoGroup": me1200LldpmedConfigPolicyListInfoGroup,
       "me1200LldpmedConfigPolicyRowEditorInfoGroup": me1200LldpmedConfigPolicyRowEditorInfoGroup,
       "me1200LldpmedStatusRemoteDeviceInfoInfoGroup": me1200LldpmedStatusRemoteDeviceInfoInfoGroup,
       "me1200LldpmedStatusRemoteDeviceLocInfoInfoGroup": me1200LldpmedStatusRemoteDeviceLocInfoInfoGroup,
       "me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoInfoGroup": me1200LldpmedStatusRemoteDeviceNetworkPolicyInfoInfoGroup}
)

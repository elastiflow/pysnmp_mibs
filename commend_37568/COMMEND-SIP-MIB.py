# SNMP MIB module (COMMEND-SIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/commend_37568/COMMEND-SIP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:51:50 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

commend = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37568)
)
if mibBuilder.loadTexts:
    commend.setRevisions(
        ("2012-05-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CommendStationObjects_ObjectIdentity = ObjectIdentity
commendStationObjects = _CommendStationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2)
)
_CommendStationObjectEntry_ObjectIdentity = ObjectIdentity
commendStationObjectEntry = _CommendStationObjectEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1)
)
_CommendStationCommon_ObjectIdentity = ObjectIdentity
commendStationCommon = _CommendStationCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 1)
)


class _CommendStationCommonStationType_Type(OctetString):
    """Custom type commendStationCommonStationType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationCommonStationType_Type.__name__ = "OctetString"
_CommendStationCommonStationType_Object = MibScalar
commendStationCommonStationType = _CommendStationCommonStationType_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 1, 1),
    _CommendStationCommonStationType_Type()
)
commendStationCommonStationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationCommonStationType.setStatus("current")


class _CommendStationCommonStationSubType_Type(OctetString):
    """Custom type commendStationCommonStationSubType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationCommonStationSubType_Type.__name__ = "OctetString"
_CommendStationCommonStationSubType_Object = MibScalar
commendStationCommonStationSubType = _CommendStationCommonStationSubType_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 1, 2),
    _CommendStationCommonStationSubType_Type()
)
commendStationCommonStationSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationCommonStationSubType.setStatus("current")


class _CommendStationCommonStationSoftwareVersion_Type(OctetString):
    """Custom type commendStationCommonStationSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationCommonStationSoftwareVersion_Type.__name__ = "OctetString"
_CommendStationCommonStationSoftwareVersion_Object = MibScalar
commendStationCommonStationSoftwareVersion = _CommendStationCommonStationSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 1, 3),
    _CommendStationCommonStationSoftwareVersion_Type()
)
commendStationCommonStationSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationCommonStationSoftwareVersion.setStatus("current")


class _CommendStationCommonStationHardwareVersion_Type(OctetString):
    """Custom type commendStationCommonStationHardwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationCommonStationHardwareVersion_Type.__name__ = "OctetString"
_CommendStationCommonStationHardwareVersion_Object = MibScalar
commendStationCommonStationHardwareVersion = _CommendStationCommonStationHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 1, 4),
    _CommendStationCommonStationHardwareVersion_Type()
)
commendStationCommonStationHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationCommonStationHardwareVersion.setStatus("current")


class _CommendStationCommonStationCallNumber_Type(OctetString):
    """Custom type commendStationCommonStationCallNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationCommonStationCallNumber_Type.__name__ = "OctetString"
_CommendStationCommonStationCallNumber_Object = MibScalar
commendStationCommonStationCallNumber = _CommendStationCommonStationCallNumber_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 1, 10),
    _CommendStationCommonStationCallNumber_Type()
)
commendStationCommonStationCallNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationCommonStationCallNumber.setStatus("current")


class _CommendStationCommonStationStationName_Type(OctetString):
    """Custom type commendStationCommonStationStationName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationCommonStationStationName_Type.__name__ = "OctetString"
_CommendStationCommonStationStationName_Object = MibScalar
commendStationCommonStationStationName = _CommendStationCommonStationStationName_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 1, 11),
    _CommendStationCommonStationStationName_Type()
)
commendStationCommonStationStationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationCommonStationStationName.setStatus("current")


class _CommendStationCommonStationLocation_Type(OctetString):
    """Custom type commendStationCommonStationLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationCommonStationLocation_Type.__name__ = "OctetString"
_CommendStationCommonStationLocation_Object = MibScalar
commendStationCommonStationLocation = _CommendStationCommonStationLocation_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 1, 12),
    _CommendStationCommonStationLocation_Type()
)
commendStationCommonStationLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationCommonStationLocation.setStatus("current")


class _CommendStationCommonStationSystemState_Type(OctetString):
    """Custom type commendStationCommonStationSystemState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationCommonStationSystemState_Type.__name__ = "OctetString"
_CommendStationCommonStationSystemState_Object = MibScalar
commendStationCommonStationSystemState = _CommendStationCommonStationSystemState_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 1, 20),
    _CommendStationCommonStationSystemState_Type()
)
commendStationCommonStationSystemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationCommonStationSystemState.setStatus("current")


class _CommendStationCommonStationSequenceName_Type(OctetString):
    """Custom type commendStationCommonStationSequenceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationCommonStationSequenceName_Type.__name__ = "OctetString"
_CommendStationCommonStationSequenceName_Object = MibScalar
commendStationCommonStationSequenceName = _CommendStationCommonStationSequenceName_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 1, 30),
    _CommendStationCommonStationSequenceName_Type()
)
commendStationCommonStationSequenceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationCommonStationSequenceName.setStatus("current")


class _CommendStationCommonStationCallState_Type(OctetString):
    """Custom type commendStationCommonStationCallState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationCommonStationCallState_Type.__name__ = "OctetString"
_CommendStationCommonStationCallState_Object = MibScalar
commendStationCommonStationCallState = _CommendStationCommonStationCallState_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 1, 80),
    _CommendStationCommonStationCallState_Type()
)
commendStationCommonStationCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationCommonStationCallState.setStatus("current")
_CommendStationConnectivity_ObjectIdentity = ObjectIdentity
commendStationConnectivity = _CommendStationConnectivity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 2)
)
_CommendStationConnectivityType_Type = Integer32
_CommendStationConnectivityType_Object = MibScalar
commendStationConnectivityType = _CommendStationConnectivityType_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 2, 1),
    _CommendStationConnectivityType_Type()
)
commendStationConnectivityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationConnectivityType.setStatus("current")
_CommendStationConnectivityAnalog_ObjectIdentity = ObjectIdentity
commendStationConnectivityAnalog = _CommendStationConnectivityAnalog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 2, 2)
)
_CommendStationConnectivityDigital_ObjectIdentity = ObjectIdentity
commendStationConnectivityDigital = _CommendStationConnectivityDigital_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 2, 3)
)
_CommendStationConnectivityIp_ObjectIdentity = ObjectIdentity
commendStationConnectivityIp = _CommendStationConnectivityIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 2, 4)
)
_CommendStationConnectivitySip_ObjectIdentity = ObjectIdentity
commendStationConnectivitySip = _CommendStationConnectivitySip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 2, 5)
)


class _CommendStationConnectivitySipPrimaryRegistration_Type(OctetString):
    """Custom type commendStationConnectivitySipPrimaryRegistration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationConnectivitySipPrimaryRegistration_Type.__name__ = "OctetString"
_CommendStationConnectivitySipPrimaryRegistration_Object = MibScalar
commendStationConnectivitySipPrimaryRegistration = _CommendStationConnectivitySipPrimaryRegistration_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 2, 5, 1),
    _CommendStationConnectivitySipPrimaryRegistration_Type()
)
commendStationConnectivitySipPrimaryRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationConnectivitySipPrimaryRegistration.setStatus("current")


class _CommendStationConnectivitySipPrimaryLastRegistration_Type(OctetString):
    """Custom type commendStationConnectivitySipPrimaryLastRegistration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationConnectivitySipPrimaryLastRegistration_Type.__name__ = "OctetString"
_CommendStationConnectivitySipPrimaryLastRegistration_Object = MibScalar
commendStationConnectivitySipPrimaryLastRegistration = _CommendStationConnectivitySipPrimaryLastRegistration_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 2, 5, 2),
    _CommendStationConnectivitySipPrimaryLastRegistration_Type()
)
commendStationConnectivitySipPrimaryLastRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationConnectivitySipPrimaryLastRegistration.setStatus("current")


class _CommendStationConnectivitySipDhcp_Type(OctetString):
    """Custom type commendStationConnectivitySipDhcp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationConnectivitySipDhcp_Type.__name__ = "OctetString"
_CommendStationConnectivitySipDhcp_Object = MibScalar
commendStationConnectivitySipDhcp = _CommendStationConnectivitySipDhcp_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 2, 5, 3),
    _CommendStationConnectivitySipDhcp_Type()
)
commendStationConnectivitySipDhcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationConnectivitySipDhcp.setStatus("current")


class _CommendStationConnectivitySipDns_Type(OctetString):
    """Custom type commendStationConnectivitySipDns based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationConnectivitySipDns_Type.__name__ = "OctetString"
_CommendStationConnectivitySipDns_Object = MibScalar
commendStationConnectivitySipDns = _CommendStationConnectivitySipDns_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 2, 5, 4),
    _CommendStationConnectivitySipDns_Type()
)
commendStationConnectivitySipDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationConnectivitySipDns.setStatus("current")


class _CommendStationConnectivitySipSecondaryRegistration_Type(OctetString):
    """Custom type commendStationConnectivitySipSecondaryRegistration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationConnectivitySipSecondaryRegistration_Type.__name__ = "OctetString"
_CommendStationConnectivitySipSecondaryRegistration_Object = MibScalar
commendStationConnectivitySipSecondaryRegistration = _CommendStationConnectivitySipSecondaryRegistration_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 2, 5, 10),
    _CommendStationConnectivitySipSecondaryRegistration_Type()
)
commendStationConnectivitySipSecondaryRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationConnectivitySipSecondaryRegistration.setStatus("current")


class _CommendStationConnectivitySipSecondaryLastRegistration_Type(OctetString):
    """Custom type commendStationConnectivitySipSecondaryLastRegistration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationConnectivitySipSecondaryLastRegistration_Type.__name__ = "OctetString"
_CommendStationConnectivitySipSecondaryLastRegistration_Object = MibScalar
commendStationConnectivitySipSecondaryLastRegistration = _CommendStationConnectivitySipSecondaryLastRegistration_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 2, 5, 11),
    _CommendStationConnectivitySipSecondaryLastRegistration_Type()
)
commendStationConnectivitySipSecondaryLastRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationConnectivitySipSecondaryLastRegistration.setStatus("current")


class _CommendStationConnectivitySipTertiaryRegistration_Type(OctetString):
    """Custom type commendStationConnectivitySipTertiaryRegistration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationConnectivitySipTertiaryRegistration_Type.__name__ = "OctetString"
_CommendStationConnectivitySipTertiaryRegistration_Object = MibScalar
commendStationConnectivitySipTertiaryRegistration = _CommendStationConnectivitySipTertiaryRegistration_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 2, 5, 20),
    _CommendStationConnectivitySipTertiaryRegistration_Type()
)
commendStationConnectivitySipTertiaryRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationConnectivitySipTertiaryRegistration.setStatus("current")


class _CommendStationConnectivitySipTertiaryLastRegistration_Type(OctetString):
    """Custom type commendStationConnectivitySipTertiaryLastRegistration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationConnectivitySipTertiaryLastRegistration_Type.__name__ = "OctetString"
_CommendStationConnectivitySipTertiaryLastRegistration_Object = MibScalar
commendStationConnectivitySipTertiaryLastRegistration = _CommendStationConnectivitySipTertiaryLastRegistration_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 2, 5, 21),
    _CommendStationConnectivitySipTertiaryLastRegistration_Type()
)
commendStationConnectivitySipTertiaryLastRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationConnectivitySipTertiaryLastRegistration.setStatus("current")
_CommendStationAudio_ObjectIdentity = ObjectIdentity
commendStationAudio = _CommendStationAudio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3)
)
_CommendStationAudioMic1_ObjectIdentity = ObjectIdentity
commendStationAudioMic1 = _CommendStationAudioMic1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3, 1)
)


class _CommendStationAudioMic1Type_Type(OctetString):
    """Custom type commendStationAudioMic1Type based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationAudioMic1Type_Type.__name__ = "OctetString"
_CommendStationAudioMic1Type_Object = MibScalar
commendStationAudioMic1Type = _CommendStationAudioMic1Type_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3, 1, 1),
    _CommendStationAudioMic1Type_Type()
)
commendStationAudioMic1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationAudioMic1Type.setStatus("current")


class _CommendStationAudioMic1Sensitivity_Type(OctetString):
    """Custom type commendStationAudioMic1Sensitivity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationAudioMic1Sensitivity_Type.__name__ = "OctetString"
_CommendStationAudioMic1Sensitivity_Object = MibScalar
commendStationAudioMic1Sensitivity = _CommendStationAudioMic1Sensitivity_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3, 1, 2),
    _CommendStationAudioMic1Sensitivity_Type()
)
commendStationAudioMic1Sensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationAudioMic1Sensitivity.setStatus("current")
_CommendStationAudioMic2_ObjectIdentity = ObjectIdentity
commendStationAudioMic2 = _CommendStationAudioMic2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3, 2)
)
_CommendStationAudioMic3_ObjectIdentity = ObjectIdentity
commendStationAudioMic3 = _CommendStationAudioMic3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3, 3)
)
_CommendStationAudioLsMic_ObjectIdentity = ObjectIdentity
commendStationAudioLsMic = _CommendStationAudioLsMic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3, 4)
)


class _CommendStationAudioLsMicStatus_Type(OctetString):
    """Custom type commendStationAudioLsMicStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationAudioLsMicStatus_Type.__name__ = "OctetString"
_CommendStationAudioLsMicStatus_Object = MibScalar
commendStationAudioLsMicStatus = _CommendStationAudioLsMicStatus_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3, 4, 1),
    _CommendStationAudioLsMicStatus_Type()
)
commendStationAudioLsMicStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationAudioLsMicStatus.setStatus("current")
_CommendStationAudioAmp1_ObjectIdentity = ObjectIdentity
commendStationAudioAmp1 = _CommendStationAudioAmp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3, 10)
)


class _CommendStationAudioAmp1Type_Type(OctetString):
    """Custom type commendStationAudioAmp1Type based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationAudioAmp1Type_Type.__name__ = "OctetString"
_CommendStationAudioAmp1Type_Object = MibScalar
commendStationAudioAmp1Type = _CommendStationAudioAmp1Type_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3, 10, 1),
    _CommendStationAudioAmp1Type_Type()
)
commendStationAudioAmp1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationAudioAmp1Type.setStatus("current")


class _CommendStationAudioAmp1Sensitivity_Type(OctetString):
    """Custom type commendStationAudioAmp1Sensitivity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationAudioAmp1Sensitivity_Type.__name__ = "OctetString"
_CommendStationAudioAmp1Sensitivity_Object = MibScalar
commendStationAudioAmp1Sensitivity = _CommendStationAudioAmp1Sensitivity_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3, 10, 2),
    _CommendStationAudioAmp1Sensitivity_Type()
)
commendStationAudioAmp1Sensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationAudioAmp1Sensitivity.setStatus("current")


class _CommendStationAudioSpeakerCompressor_Type(OctetString):
    """Custom type commendStationAudioSpeakerCompressor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationAudioSpeakerCompressor_Type.__name__ = "OctetString"
_CommendStationAudioSpeakerCompressor_Object = MibScalar
commendStationAudioSpeakerCompressor = _CommendStationAudioSpeakerCompressor_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3, 10, 3),
    _CommendStationAudioSpeakerCompressor_Type()
)
commendStationAudioSpeakerCompressor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationAudioSpeakerCompressor.setStatus("current")
_CommendStationAudioAEC_ObjectIdentity = ObjectIdentity
commendStationAudioAEC = _CommendStationAudioAEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3, 50)
)


class _CommendStationAudioAECMode_Type(OctetString):
    """Custom type commendStationAudioAECMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationAudioAECMode_Type.__name__ = "OctetString"
_CommendStationAudioAECMode_Object = MibScalar
commendStationAudioAECMode = _CommendStationAudioAECMode_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3, 50, 1),
    _CommendStationAudioAECMode_Type()
)
commendStationAudioAECMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationAudioAECMode.setStatus("current")


class _CommendStationAudioNgClosedGain_Type(OctetString):
    """Custom type commendStationAudioNgClosedGain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationAudioNgClosedGain_Type.__name__ = "OctetString"
_CommendStationAudioNgClosedGain_Object = MibScalar
commendStationAudioNgClosedGain = _CommendStationAudioNgClosedGain_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3, 50, 2),
    _CommendStationAudioNgClosedGain_Type()
)
commendStationAudioNgClosedGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationAudioNgClosedGain.setStatus("current")


class _CommendStationAudioPgClosedGain_Type(OctetString):
    """Custom type commendStationAudioPgClosedGain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationAudioPgClosedGain_Type.__name__ = "OctetString"
_CommendStationAudioPgClosedGain_Object = MibScalar
commendStationAudioPgClosedGain = _CommendStationAudioPgClosedGain_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3, 50, 3),
    _CommendStationAudioPgClosedGain_Type()
)
commendStationAudioPgClosedGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationAudioPgClosedGain.setStatus("current")


class _CommendStationAudioNgEnabled_Type(OctetString):
    """Custom type commendStationAudioNgEnabled based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationAudioNgEnabled_Type.__name__ = "OctetString"
_CommendStationAudioNgEnabled_Object = MibScalar
commendStationAudioNgEnabled = _CommendStationAudioNgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3, 50, 4),
    _CommendStationAudioNgEnabled_Type()
)
commendStationAudioNgEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationAudioNgEnabled.setStatus("current")


class _CommendStationAudioPgEnabled_Type(OctetString):
    """Custom type commendStationAudioPgEnabled based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationAudioPgEnabled_Type.__name__ = "OctetString"
_CommendStationAudioPgEnabled_Object = MibScalar
commendStationAudioPgEnabled = _CommendStationAudioPgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3, 50, 5),
    _CommendStationAudioPgEnabled_Type()
)
commendStationAudioPgEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationAudioPgEnabled.setStatus("current")
_CommendStationAudioNC_ObjectIdentity = ObjectIdentity
commendStationAudioNC = _CommendStationAudioNC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3, 51)
)


class _CommendStationAudioNCMode_Type(OctetString):
    """Custom type commendStationAudioNCMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationAudioNCMode_Type.__name__ = "OctetString"
_CommendStationAudioNCMode_Object = MibScalar
commendStationAudioNCMode = _CommendStationAudioNCMode_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3, 51, 1),
    _CommendStationAudioNCMode_Type()
)
commendStationAudioNCMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationAudioNCMode.setStatus("current")
_CommendStationInputs_ObjectIdentity = ObjectIdentity
commendStationInputs = _CommendStationInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4)
)
_CommendStationInput1_ObjectIdentity = ObjectIdentity
commendStationInput1 = _CommendStationInput1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 1)
)


class _CommendStationInputType1_Type(OctetString):
    """Custom type commendStationInputType1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputType1_Type.__name__ = "OctetString"
_CommendStationInputType1_Object = MibScalar
commendStationInputType1 = _CommendStationInputType1_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 1, 1),
    _CommendStationInputType1_Type()
)
commendStationInputType1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputType1.setStatus("current")


class _CommendStationInputState1_Type(OctetString):
    """Custom type commendStationInputState1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputState1_Type.__name__ = "OctetString"
_CommendStationInputState1_Object = MibScalar
commendStationInputState1 = _CommendStationInputState1_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 1, 2),
    _CommendStationInputState1_Type()
)
commendStationInputState1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputState1.setStatus("current")
_CommendStationInput2_ObjectIdentity = ObjectIdentity
commendStationInput2 = _CommendStationInput2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 2)
)


class _CommendStationInputType2_Type(OctetString):
    """Custom type commendStationInputType2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputType2_Type.__name__ = "OctetString"
_CommendStationInputType2_Object = MibScalar
commendStationInputType2 = _CommendStationInputType2_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 2, 1),
    _CommendStationInputType2_Type()
)
commendStationInputType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputType2.setStatus("current")


class _CommendStationInputState2_Type(OctetString):
    """Custom type commendStationInputState2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputState2_Type.__name__ = "OctetString"
_CommendStationInputState2_Object = MibScalar
commendStationInputState2 = _CommendStationInputState2_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 2, 2),
    _CommendStationInputState2_Type()
)
commendStationInputState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputState2.setStatus("current")
_CommendStationInput3_ObjectIdentity = ObjectIdentity
commendStationInput3 = _CommendStationInput3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 3)
)


class _CommendStationInputType3_Type(OctetString):
    """Custom type commendStationInputType3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputType3_Type.__name__ = "OctetString"
_CommendStationInputType3_Object = MibScalar
commendStationInputType3 = _CommendStationInputType3_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 3, 1),
    _CommendStationInputType3_Type()
)
commendStationInputType3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputType3.setStatus("current")


class _CommendStationInputState3_Type(OctetString):
    """Custom type commendStationInputState3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputState3_Type.__name__ = "OctetString"
_CommendStationInputState3_Object = MibScalar
commendStationInputState3 = _CommendStationInputState3_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 3, 2),
    _CommendStationInputState3_Type()
)
commendStationInputState3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputState3.setStatus("current")
_CommendStationEB2E2AInput1_ObjectIdentity = ObjectIdentity
commendStationEB2E2AInput1 = _CommendStationEB2E2AInput1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 4)
)


class _CommendStationEB2E2AInputType1_Type(OctetString):
    """Custom type commendStationEB2E2AInputType1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationEB2E2AInputType1_Type.__name__ = "OctetString"
_CommendStationEB2E2AInputType1_Object = MibScalar
commendStationEB2E2AInputType1 = _CommendStationEB2E2AInputType1_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 4, 1),
    _CommendStationEB2E2AInputType1_Type()
)
commendStationEB2E2AInputType1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationEB2E2AInputType1.setStatus("current")


class _CommendStationEB2E2AInputState1_Type(OctetString):
    """Custom type commendStationEB2E2AInputState1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationEB2E2AInputState1_Type.__name__ = "OctetString"
_CommendStationEB2E2AInputState1_Object = MibScalar
commendStationEB2E2AInputState1 = _CommendStationEB2E2AInputState1_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 4, 2),
    _CommendStationEB2E2AInputState1_Type()
)
commendStationEB2E2AInputState1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationEB2E2AInputState1.setStatus("current")
_CommendStationEB2E2AInput2_ObjectIdentity = ObjectIdentity
commendStationEB2E2AInput2 = _CommendStationEB2E2AInput2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 5)
)


class _CommendStationEB2E2AInputType2_Type(OctetString):
    """Custom type commendStationEB2E2AInputType2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationEB2E2AInputType2_Type.__name__ = "OctetString"
_CommendStationEB2E2AInputType2_Object = MibScalar
commendStationEB2E2AInputType2 = _CommendStationEB2E2AInputType2_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 5, 1),
    _CommendStationEB2E2AInputType2_Type()
)
commendStationEB2E2AInputType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationEB2E2AInputType2.setStatus("current")


class _CommendStationEB2E2AInputState2_Type(OctetString):
    """Custom type commendStationEB2E2AInputState2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationEB2E2AInputState2_Type.__name__ = "OctetString"
_CommendStationEB2E2AInputState2_Object = MibScalar
commendStationEB2E2AInputState2 = _CommendStationEB2E2AInputState2_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 5, 2),
    _CommendStationEB2E2AInputState2_Type()
)
commendStationEB2E2AInputState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationEB2E2AInputState2.setStatus("current")
_CommendStationInputKeyboard_ObjectIdentity = ObjectIdentity
commendStationInputKeyboard = _CommendStationInputKeyboard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 10)
)


class _CommendStationInputKeyboardButton1_Type(OctetString):
    """Custom type commendStationInputKeyboardButton1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputKeyboardButton1_Type.__name__ = "OctetString"
_CommendStationInputKeyboardButton1_Object = MibScalar
commendStationInputKeyboardButton1 = _CommendStationInputKeyboardButton1_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 10, 1),
    _CommendStationInputKeyboardButton1_Type()
)
commendStationInputKeyboardButton1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputKeyboardButton1.setStatus("current")


class _CommendStationInputKeyboardButton2_Type(OctetString):
    """Custom type commendStationInputKeyboardButton2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputKeyboardButton2_Type.__name__ = "OctetString"
_CommendStationInputKeyboardButton2_Object = MibScalar
commendStationInputKeyboardButton2 = _CommendStationInputKeyboardButton2_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 10, 2),
    _CommendStationInputKeyboardButton2_Type()
)
commendStationInputKeyboardButton2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputKeyboardButton2.setStatus("current")


class _CommendStationInputKeyboardButton3_Type(OctetString):
    """Custom type commendStationInputKeyboardButton3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputKeyboardButton3_Type.__name__ = "OctetString"
_CommendStationInputKeyboardButton3_Object = MibScalar
commendStationInputKeyboardButton3 = _CommendStationInputKeyboardButton3_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 10, 3),
    _CommendStationInputKeyboardButton3_Type()
)
commendStationInputKeyboardButton3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputKeyboardButton3.setStatus("current")
_CommendStationInputFullKeyboard_ObjectIdentity = ObjectIdentity
commendStationInputFullKeyboard = _CommendStationInputFullKeyboard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 11)
)


class _CommendStationInputFullKeyboardButton1_Type(OctetString):
    """Custom type commendStationInputFullKeyboardButton1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputFullKeyboardButton1_Type.__name__ = "OctetString"
_CommendStationInputFullKeyboardButton1_Object = MibScalar
commendStationInputFullKeyboardButton1 = _CommendStationInputFullKeyboardButton1_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 11, 1),
    _CommendStationInputFullKeyboardButton1_Type()
)
commendStationInputFullKeyboardButton1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputFullKeyboardButton1.setStatus("current")


class _CommendStationInputFullKeyboardButton2_Type(OctetString):
    """Custom type commendStationInputFullKeyboardButton2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputFullKeyboardButton2_Type.__name__ = "OctetString"
_CommendStationInputFullKeyboardButton2_Object = MibScalar
commendStationInputFullKeyboardButton2 = _CommendStationInputFullKeyboardButton2_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 11, 2),
    _CommendStationInputFullKeyboardButton2_Type()
)
commendStationInputFullKeyboardButton2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputFullKeyboardButton2.setStatus("current")


class _CommendStationInputFullKeyboardButton3_Type(OctetString):
    """Custom type commendStationInputFullKeyboardButton3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputFullKeyboardButton3_Type.__name__ = "OctetString"
_CommendStationInputFullKeyboardButton3_Object = MibScalar
commendStationInputFullKeyboardButton3 = _CommendStationInputFullKeyboardButton3_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 11, 3),
    _CommendStationInputFullKeyboardButton3_Type()
)
commendStationInputFullKeyboardButton3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputFullKeyboardButton3.setStatus("current")


class _CommendStationInputFullKeyboardButton4_Type(OctetString):
    """Custom type commendStationInputFullKeyboardButton4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputFullKeyboardButton4_Type.__name__ = "OctetString"
_CommendStationInputFullKeyboardButton4_Object = MibScalar
commendStationInputFullKeyboardButton4 = _CommendStationInputFullKeyboardButton4_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 11, 4),
    _CommendStationInputFullKeyboardButton4_Type()
)
commendStationInputFullKeyboardButton4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputFullKeyboardButton4.setStatus("current")


class _CommendStationInputFullKeyboardButton5_Type(OctetString):
    """Custom type commendStationInputFullKeyboardButton5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputFullKeyboardButton5_Type.__name__ = "OctetString"
_CommendStationInputFullKeyboardButton5_Object = MibScalar
commendStationInputFullKeyboardButton5 = _CommendStationInputFullKeyboardButton5_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 11, 5),
    _CommendStationInputFullKeyboardButton5_Type()
)
commendStationInputFullKeyboardButton5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputFullKeyboardButton5.setStatus("current")


class _CommendStationInputFullKeyboardButton6_Type(OctetString):
    """Custom type commendStationInputFullKeyboardButton6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputFullKeyboardButton6_Type.__name__ = "OctetString"
_CommendStationInputFullKeyboardButton6_Object = MibScalar
commendStationInputFullKeyboardButton6 = _CommendStationInputFullKeyboardButton6_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 11, 6),
    _CommendStationInputFullKeyboardButton6_Type()
)
commendStationInputFullKeyboardButton6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputFullKeyboardButton6.setStatus("current")


class _CommendStationInputFullKeyboardButton7_Type(OctetString):
    """Custom type commendStationInputFullKeyboardButton7 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputFullKeyboardButton7_Type.__name__ = "OctetString"
_CommendStationInputFullKeyboardButton7_Object = MibScalar
commendStationInputFullKeyboardButton7 = _CommendStationInputFullKeyboardButton7_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 11, 7),
    _CommendStationInputFullKeyboardButton7_Type()
)
commendStationInputFullKeyboardButton7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputFullKeyboardButton7.setStatus("current")


class _CommendStationInputFullKeyboardButton8_Type(OctetString):
    """Custom type commendStationInputFullKeyboardButton8 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputFullKeyboardButton8_Type.__name__ = "OctetString"
_CommendStationInputFullKeyboardButton8_Object = MibScalar
commendStationInputFullKeyboardButton8 = _CommendStationInputFullKeyboardButton8_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 11, 8),
    _CommendStationInputFullKeyboardButton8_Type()
)
commendStationInputFullKeyboardButton8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputFullKeyboardButton8.setStatus("current")


class _CommendStationInputFullKeyboardButton9_Type(OctetString):
    """Custom type commendStationInputFullKeyboardButton9 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputFullKeyboardButton9_Type.__name__ = "OctetString"
_CommendStationInputFullKeyboardButton9_Object = MibScalar
commendStationInputFullKeyboardButton9 = _CommendStationInputFullKeyboardButton9_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 11, 9),
    _CommendStationInputFullKeyboardButton9_Type()
)
commendStationInputFullKeyboardButton9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputFullKeyboardButton9.setStatus("current")


class _CommendStationInputFullKeyboardButton0_Type(OctetString):
    """Custom type commendStationInputFullKeyboardButton0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputFullKeyboardButton0_Type.__name__ = "OctetString"
_CommendStationInputFullKeyboardButton0_Object = MibScalar
commendStationInputFullKeyboardButton0 = _CommendStationInputFullKeyboardButton0_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 11, 10),
    _CommendStationInputFullKeyboardButton0_Type()
)
commendStationInputFullKeyboardButton0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputFullKeyboardButton0.setStatus("current")


class _CommendStationInputFullKeyboardButtonX_Type(OctetString):
    """Custom type commendStationInputFullKeyboardButtonX based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputFullKeyboardButtonX_Type.__name__ = "OctetString"
_CommendStationInputFullKeyboardButtonX_Object = MibScalar
commendStationInputFullKeyboardButtonX = _CommendStationInputFullKeyboardButtonX_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 11, 11),
    _CommendStationInputFullKeyboardButtonX_Type()
)
commendStationInputFullKeyboardButtonX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputFullKeyboardButtonX.setStatus("current")


class _CommendStationInputFullKeyboardButtonT_Type(OctetString):
    """Custom type commendStationInputFullKeyboardButtonT based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputFullKeyboardButtonT_Type.__name__ = "OctetString"
_CommendStationInputFullKeyboardButtonT_Object = MibScalar
commendStationInputFullKeyboardButtonT = _CommendStationInputFullKeyboardButtonT_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 11, 12),
    _CommendStationInputFullKeyboardButtonT_Type()
)
commendStationInputFullKeyboardButtonT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputFullKeyboardButtonT.setStatus("current")


class _CommendStationInputFullKeyboardButtonUP_Type(OctetString):
    """Custom type commendStationInputFullKeyboardButtonUP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputFullKeyboardButtonUP_Type.__name__ = "OctetString"
_CommendStationInputFullKeyboardButtonUP_Object = MibScalar
commendStationInputFullKeyboardButtonUP = _CommendStationInputFullKeyboardButtonUP_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 11, 13),
    _CommendStationInputFullKeyboardButtonUP_Type()
)
commendStationInputFullKeyboardButtonUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputFullKeyboardButtonUP.setStatus("current")


class _CommendStationInputFullKeyboardButtonDOWN_Type(OctetString):
    """Custom type commendStationInputFullKeyboardButtonDOWN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputFullKeyboardButtonDOWN_Type.__name__ = "OctetString"
_CommendStationInputFullKeyboardButtonDOWN_Object = MibScalar
commendStationInputFullKeyboardButtonDOWN = _CommendStationInputFullKeyboardButtonDOWN_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 11, 14),
    _CommendStationInputFullKeyboardButtonDOWN_Type()
)
commendStationInputFullKeyboardButtonDOWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputFullKeyboardButtonDOWN.setStatus("current")


class _CommendStationInputFullKeyboardButtonMENU_Type(OctetString):
    """Custom type commendStationInputFullKeyboardButtonMENU based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputFullKeyboardButtonMENU_Type.__name__ = "OctetString"
_CommendStationInputFullKeyboardButtonMENU_Object = MibScalar
commendStationInputFullKeyboardButtonMENU = _CommendStationInputFullKeyboardButtonMENU_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 11, 15),
    _CommendStationInputFullKeyboardButtonMENU_Type()
)
commendStationInputFullKeyboardButtonMENU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputFullKeyboardButtonMENU.setStatus("current")


class _CommendStationInputFullKeyboardButtonENTER_Type(OctetString):
    """Custom type commendStationInputFullKeyboardButtonENTER based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationInputFullKeyboardButtonENTER_Type.__name__ = "OctetString"
_CommendStationInputFullKeyboardButtonENTER_Object = MibScalar
commendStationInputFullKeyboardButtonENTER = _CommendStationInputFullKeyboardButtonENTER_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 11, 16),
    _CommendStationInputFullKeyboardButtonENTER_Type()
)
commendStationInputFullKeyboardButtonENTER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationInputFullKeyboardButtonENTER.setStatus("current")
_CommendStationInputStatus_ObjectIdentity = ObjectIdentity
commendStationInputStatus = _CommendStationInputStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 5)
)
_CommendStationOutputs_ObjectIdentity = ObjectIdentity
commendStationOutputs = _CommendStationOutputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 5)
)


class _CommendStationLastInputChange_Type(OctetString):
    """Custom type commendStationLastInputChange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationLastInputChange_Type.__name__ = "OctetString"
_CommendStationLastInputChange_Object = MibScalar
commendStationLastInputChange = _CommendStationLastInputChange_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 5, 1),
    _CommendStationLastInputChange_Type()
)
commendStationLastInputChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationLastInputChange.setStatus("current")
_CommendStationOutput1_ObjectIdentity = ObjectIdentity
commendStationOutput1 = _CommendStationOutput1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 5, 1)
)


class _CommendStationOutputName1_Type(OctetString):
    """Custom type commendStationOutputName1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationOutputName1_Type.__name__ = "OctetString"
_CommendStationOutputName1_Object = MibScalar
commendStationOutputName1 = _CommendStationOutputName1_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 5, 1, 1),
    _CommendStationOutputName1_Type()
)
commendStationOutputName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationOutputName1.setStatus("current")


class _CommendStationOutputState1_Type(OctetString):
    """Custom type commendStationOutputState1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationOutputState1_Type.__name__ = "OctetString"
_CommendStationOutputState1_Object = MibScalar
commendStationOutputState1 = _CommendStationOutputState1_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 5, 1, 2),
    _CommendStationOutputState1_Type()
)
commendStationOutputState1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationOutputState1.setStatus("current")


class _CommendStationLastButtonStuck_Type(OctetString):
    """Custom type commendStationLastButtonStuck based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationLastButtonStuck_Type.__name__ = "OctetString"
_CommendStationLastButtonStuck_Object = MibScalar
commendStationLastButtonStuck = _CommendStationLastButtonStuck_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 5, 2),
    _CommendStationLastButtonStuck_Type()
)
commendStationLastButtonStuck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationLastButtonStuck.setStatus("current")
_CommendStationOutput2_ObjectIdentity = ObjectIdentity
commendStationOutput2 = _CommendStationOutput2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 5, 2)
)


class _CommendStationOutputName2_Type(OctetString):
    """Custom type commendStationOutputName2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationOutputName2_Type.__name__ = "OctetString"
_CommendStationOutputName2_Object = MibScalar
commendStationOutputName2 = _CommendStationOutputName2_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 5, 2, 1),
    _CommendStationOutputName2_Type()
)
commendStationOutputName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationOutputName2.setStatus("current")


class _CommendStationOutputState2_Type(OctetString):
    """Custom type commendStationOutputState2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationOutputState2_Type.__name__ = "OctetString"
_CommendStationOutputState2_Object = MibScalar
commendStationOutputState2 = _CommendStationOutputState2_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 5, 2, 2),
    _CommendStationOutputState2_Type()
)
commendStationOutputState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationOutputState2.setStatus("current")
_CommendStationEB2E2AOutput1_ObjectIdentity = ObjectIdentity
commendStationEB2E2AOutput1 = _CommendStationEB2E2AOutput1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 5, 3)
)


class _CommendStationEB2E2AOutputName1_Type(OctetString):
    """Custom type commendStationEB2E2AOutputName1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationEB2E2AOutputName1_Type.__name__ = "OctetString"
_CommendStationEB2E2AOutputName1_Object = MibScalar
commendStationEB2E2AOutputName1 = _CommendStationEB2E2AOutputName1_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 5, 3, 1),
    _CommendStationEB2E2AOutputName1_Type()
)
commendStationEB2E2AOutputName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationEB2E2AOutputName1.setStatus("current")


class _CommendStationEB2E2AOutputState1_Type(OctetString):
    """Custom type commendStationEB2E2AOutputState1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationEB2E2AOutputState1_Type.__name__ = "OctetString"
_CommendStationEB2E2AOutputState1_Object = MibScalar
commendStationEB2E2AOutputState1 = _CommendStationEB2E2AOutputState1_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 5, 3, 2),
    _CommendStationEB2E2AOutputState1_Type()
)
commendStationEB2E2AOutputState1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationEB2E2AOutputState1.setStatus("current")
_CommendStationEB2E2AOutput2_ObjectIdentity = ObjectIdentity
commendStationEB2E2AOutput2 = _CommendStationEB2E2AOutput2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 5, 4)
)


class _CommendStationEB2E2AOutputName2_Type(OctetString):
    """Custom type commendStationEB2E2AOutputName2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationEB2E2AOutputName2_Type.__name__ = "OctetString"
_CommendStationEB2E2AOutputName2_Object = MibScalar
commendStationEB2E2AOutputName2 = _CommendStationEB2E2AOutputName2_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 5, 4, 1),
    _CommendStationEB2E2AOutputName2_Type()
)
commendStationEB2E2AOutputName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationEB2E2AOutputName2.setStatus("current")


class _CommendStationEB2E2AOutputState2_Type(OctetString):
    """Custom type commendStationEB2E2AOutputState2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CommendStationEB2E2AOutputState2_Type.__name__ = "OctetString"
_CommendStationEB2E2AOutputState2_Object = MibScalar
commendStationEB2E2AOutputState2 = _CommendStationEB2E2AOutputState2_Object(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 5, 4, 2),
    _CommendStationEB2E2AOutputState2_Type()
)
commendStationEB2E2AOutputState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commendStationEB2E2AOutputState2.setStatus("current")

# Managed Objects groups


# Notification objects

commendStationAudioLsMicSurveillanceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 3, 11)
)
if mibBuilder.loadTexts:
    commendStationAudioLsMicSurveillanceNotification.setStatus(
        "current"
    )

commendStationInputNotifications = NotificationType(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 9)
)
if mibBuilder.loadTexts:
    commendStationInputNotifications.setStatus(
        "current"
    )

commendStationInputButtonStuckNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 9, 1)
)
if mibBuilder.loadTexts:
    commendStationInputButtonStuckNotification.setStatus(
        "current"
    )

commendStationInputHandsetOffhookNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 9, 2)
)
if mibBuilder.loadTexts:
    commendStationInputHandsetOffhookNotification.setStatus(
        "current"
    )

commendStationInputChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 4, 9, 3)
)
if mibBuilder.loadTexts:
    commendStationInputChangedNotification.setStatus(
        "current"
    )

commendStationOutput1Notifications = NotificationType(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 5, 1, 10)
)
if mibBuilder.loadTexts:
    commendStationOutput1Notifications.setStatus(
        "current"
    )

commendStationOutput2Notifications = NotificationType(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 5, 2, 10)
)
if mibBuilder.loadTexts:
    commendStationOutput2Notifications.setStatus(
        "current"
    )

commendStationEB2E2AOutput1Notifications = NotificationType(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 5, 3, 10)
)
if mibBuilder.loadTexts:
    commendStationEB2E2AOutput1Notifications.setStatus(
        "current"
    )

commendStationEB2E2AOutput2Notifications = NotificationType(
    (1, 3, 6, 1, 4, 1, 37568, 2, 1, 5, 4, 10)
)
if mibBuilder.loadTexts:
    commendStationEB2E2AOutput2Notifications.setStatus(
        "current"
    )

commendStationObjectStatusNotifications = NotificationType(
    (1, 3, 6, 1, 4, 1, 37568, 2, 10)
)
if mibBuilder.loadTexts:
    commendStationObjectStatusNotifications.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COMMEND-SIP-MIB",
    **{"commend": commend,
       "commendStationObjects": commendStationObjects,
       "commendStationObjectEntry": commendStationObjectEntry,
       "commendStationCommon": commendStationCommon,
       "commendStationCommonStationType": commendStationCommonStationType,
       "commendStationCommonStationSubType": commendStationCommonStationSubType,
       "commendStationCommonStationSoftwareVersion": commendStationCommonStationSoftwareVersion,
       "commendStationCommonStationHardwareVersion": commendStationCommonStationHardwareVersion,
       "commendStationCommonStationCallNumber": commendStationCommonStationCallNumber,
       "commendStationCommonStationStationName": commendStationCommonStationStationName,
       "commendStationCommonStationLocation": commendStationCommonStationLocation,
       "commendStationCommonStationSystemState": commendStationCommonStationSystemState,
       "commendStationCommonStationSequenceName": commendStationCommonStationSequenceName,
       "commendStationCommonStationCallState": commendStationCommonStationCallState,
       "commendStationConnectivity": commendStationConnectivity,
       "commendStationConnectivityType": commendStationConnectivityType,
       "commendStationConnectivityAnalog": commendStationConnectivityAnalog,
       "commendStationConnectivityDigital": commendStationConnectivityDigital,
       "commendStationConnectivityIp": commendStationConnectivityIp,
       "commendStationConnectivitySip": commendStationConnectivitySip,
       "commendStationConnectivitySipPrimaryRegistration": commendStationConnectivitySipPrimaryRegistration,
       "commendStationConnectivitySipPrimaryLastRegistration": commendStationConnectivitySipPrimaryLastRegistration,
       "commendStationConnectivitySipDhcp": commendStationConnectivitySipDhcp,
       "commendStationConnectivitySipDns": commendStationConnectivitySipDns,
       "commendStationConnectivitySipSecondaryRegistration": commendStationConnectivitySipSecondaryRegistration,
       "commendStationConnectivitySipSecondaryLastRegistration": commendStationConnectivitySipSecondaryLastRegistration,
       "commendStationConnectivitySipTertiaryRegistration": commendStationConnectivitySipTertiaryRegistration,
       "commendStationConnectivitySipTertiaryLastRegistration": commendStationConnectivitySipTertiaryLastRegistration,
       "commendStationAudio": commendStationAudio,
       "commendStationAudioMic1": commendStationAudioMic1,
       "commendStationAudioMic1Type": commendStationAudioMic1Type,
       "commendStationAudioMic1Sensitivity": commendStationAudioMic1Sensitivity,
       "commendStationAudioMic2": commendStationAudioMic2,
       "commendStationAudioMic3": commendStationAudioMic3,
       "commendStationAudioLsMic": commendStationAudioLsMic,
       "commendStationAudioLsMicStatus": commendStationAudioLsMicStatus,
       "commendStationAudioAmp1": commendStationAudioAmp1,
       "commendStationAudioAmp1Type": commendStationAudioAmp1Type,
       "commendStationAudioAmp1Sensitivity": commendStationAudioAmp1Sensitivity,
       "commendStationAudioSpeakerCompressor": commendStationAudioSpeakerCompressor,
       "commendStationAudioLsMicSurveillanceNotification": commendStationAudioLsMicSurveillanceNotification,
       "commendStationAudioAEC": commendStationAudioAEC,
       "commendStationAudioAECMode": commendStationAudioAECMode,
       "commendStationAudioNgClosedGain": commendStationAudioNgClosedGain,
       "commendStationAudioPgClosedGain": commendStationAudioPgClosedGain,
       "commendStationAudioNgEnabled": commendStationAudioNgEnabled,
       "commendStationAudioPgEnabled": commendStationAudioPgEnabled,
       "commendStationAudioNC": commendStationAudioNC,
       "commendStationAudioNCMode": commendStationAudioNCMode,
       "commendStationInputs": commendStationInputs,
       "commendStationInput1": commendStationInput1,
       "commendStationInputType1": commendStationInputType1,
       "commendStationInputState1": commendStationInputState1,
       "commendStationInput2": commendStationInput2,
       "commendStationInputType2": commendStationInputType2,
       "commendStationInputState2": commendStationInputState2,
       "commendStationInput3": commendStationInput3,
       "commendStationInputType3": commendStationInputType3,
       "commendStationInputState3": commendStationInputState3,
       "commendStationEB2E2AInput1": commendStationEB2E2AInput1,
       "commendStationEB2E2AInputType1": commendStationEB2E2AInputType1,
       "commendStationEB2E2AInputState1": commendStationEB2E2AInputState1,
       "commendStationEB2E2AInput2": commendStationEB2E2AInput2,
       "commendStationEB2E2AInputType2": commendStationEB2E2AInputType2,
       "commendStationEB2E2AInputState2": commendStationEB2E2AInputState2,
       "commendStationInputNotifications": commendStationInputNotifications,
       "commendStationInputButtonStuckNotification": commendStationInputButtonStuckNotification,
       "commendStationInputHandsetOffhookNotification": commendStationInputHandsetOffhookNotification,
       "commendStationInputChangedNotification": commendStationInputChangedNotification,
       "commendStationInputKeyboard": commendStationInputKeyboard,
       "commendStationInputKeyboardButton1": commendStationInputKeyboardButton1,
       "commendStationInputKeyboardButton2": commendStationInputKeyboardButton2,
       "commendStationInputKeyboardButton3": commendStationInputKeyboardButton3,
       "commendStationInputFullKeyboard": commendStationInputFullKeyboard,
       "commendStationInputFullKeyboardButton1": commendStationInputFullKeyboardButton1,
       "commendStationInputFullKeyboardButton2": commendStationInputFullKeyboardButton2,
       "commendStationInputFullKeyboardButton3": commendStationInputFullKeyboardButton3,
       "commendStationInputFullKeyboardButton4": commendStationInputFullKeyboardButton4,
       "commendStationInputFullKeyboardButton5": commendStationInputFullKeyboardButton5,
       "commendStationInputFullKeyboardButton6": commendStationInputFullKeyboardButton6,
       "commendStationInputFullKeyboardButton7": commendStationInputFullKeyboardButton7,
       "commendStationInputFullKeyboardButton8": commendStationInputFullKeyboardButton8,
       "commendStationInputFullKeyboardButton9": commendStationInputFullKeyboardButton9,
       "commendStationInputFullKeyboardButton0": commendStationInputFullKeyboardButton0,
       "commendStationInputFullKeyboardButtonX": commendStationInputFullKeyboardButtonX,
       "commendStationInputFullKeyboardButtonT": commendStationInputFullKeyboardButtonT,
       "commendStationInputFullKeyboardButtonUP": commendStationInputFullKeyboardButtonUP,
       "commendStationInputFullKeyboardButtonDOWN": commendStationInputFullKeyboardButtonDOWN,
       "commendStationInputFullKeyboardButtonMENU": commendStationInputFullKeyboardButtonMENU,
       "commendStationInputFullKeyboardButtonENTER": commendStationInputFullKeyboardButtonENTER,
       "commendStationInputStatus": commendStationInputStatus,
       "commendStationOutputs": commendStationOutputs,
       "commendStationLastInputChange": commendStationLastInputChange,
       "commendStationOutput1": commendStationOutput1,
       "commendStationOutputName1": commendStationOutputName1,
       "commendStationOutputState1": commendStationOutputState1,
       "commendStationOutput1Notifications": commendStationOutput1Notifications,
       "commendStationLastButtonStuck": commendStationLastButtonStuck,
       "commendStationOutput2": commendStationOutput2,
       "commendStationOutputName2": commendStationOutputName2,
       "commendStationOutputState2": commendStationOutputState2,
       "commendStationOutput2Notifications": commendStationOutput2Notifications,
       "commendStationEB2E2AOutput1": commendStationEB2E2AOutput1,
       "commendStationEB2E2AOutputName1": commendStationEB2E2AOutputName1,
       "commendStationEB2E2AOutputState1": commendStationEB2E2AOutputState1,
       "commendStationEB2E2AOutput1Notifications": commendStationEB2E2AOutput1Notifications,
       "commendStationEB2E2AOutput2": commendStationEB2E2AOutput2,
       "commendStationEB2E2AOutputName2": commendStationEB2E2AOutputName2,
       "commendStationEB2E2AOutputState2": commendStationEB2E2AOutputState2,
       "commendStationEB2E2AOutput2Notifications": commendStationEB2E2AOutput2Notifications,
       "commendStationObjectStatusNotifications": commendStationObjectStatusNotifications}
)

# SNMP MIB module (NDS-DTH3-OFDM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/news_digital_1855/NDS-DTH3-OFDM.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:44:39 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ndsDTH3Encoder = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OfdmEnc_ObjectIdentity = ObjectIdentity
ofdmEnc = _OfdmEnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15)
)


class _OfdmHardwareRelease_Type(DisplayString):
    """Custom type ofdmHardwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_OfdmHardwareRelease_Type.__name__ = "DisplayString"
_OfdmHardwareRelease_Object = MibScalar
ofdmHardwareRelease = _OfdmHardwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 1),
    _OfdmHardwareRelease_Type()
)
ofdmHardwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofdmHardwareRelease.setStatus("current")


class _OfdmSoftwareRelease_Type(DisplayString):
    """Custom type ofdmSoftwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_OfdmSoftwareRelease_Type.__name__ = "DisplayString"
_OfdmSoftwareRelease_Object = MibScalar
ofdmSoftwareRelease = _OfdmSoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 2),
    _OfdmSoftwareRelease_Type()
)
ofdmSoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofdmSoftwareRelease.setStatus("current")


class _OfdmFirmwareRelease_Type(DisplayString):
    """Custom type ofdmFirmwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_OfdmFirmwareRelease_Type.__name__ = "DisplayString"
_OfdmFirmwareRelease_Object = MibScalar
ofdmFirmwareRelease = _OfdmFirmwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 3),
    _OfdmFirmwareRelease_Type()
)
ofdmFirmwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofdmFirmwareRelease.setStatus("current")
_OfdmnextTimeDate_Type = DateAndTime
_OfdmnextTimeDate_Object = MibScalar
ofdmnextTimeDate = _OfdmnextTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 4),
    _OfdmnextTimeDate_Type()
)
ofdmnextTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofdmnextTimeDate.setStatus("current")
_OfdmTable_Object = MibTable
ofdmTable = _OfdmTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 5)
)
if mibBuilder.loadTexts:
    ofdmTable.setStatus("current")
_OfdmEntry_Object = MibTableRow
ofdmEntry = _OfdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 5, 1)
)
ofdmEntry.setIndexNames(
    (0, "NDS-DTH3-OFDM", "ofdmCurrentNextIndex"),
)
if mibBuilder.loadTexts:
    ofdmEntry.setStatus("current")


class _OfdmCurrentNextIndex_Type(Integer32):
    """Custom type ofdmCurrentNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("index-current", 1),
          ("index-next", 2))
    )


_OfdmCurrentNextIndex_Type.__name__ = "Integer32"
_OfdmCurrentNextIndex_Object = MibTableColumn
ofdmCurrentNextIndex = _OfdmCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 5, 1, 1),
    _OfdmCurrentNextIndex_Type()
)
ofdmCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofdmCurrentNextIndex.setStatus("current")


class _OfdmOutput_Type(Integer32):
    """Custom type ofdmOutput based on Integer32"""
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


_OfdmOutput_Type.__name__ = "Integer32"
_OfdmOutput_Object = MibTableColumn
ofdmOutput = _OfdmOutput_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 5, 1, 2),
    _OfdmOutput_Type()
)
ofdmOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofdmOutput.setStatus("current")


class _OfdmModulationMode_Type(Integer32):
    """Custom type ofdmModulationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modQPSK", 0),
          ("mod16QAM", 1),
          ("mod64QAM", 2))
    )


_OfdmModulationMode_Type.__name__ = "Integer32"
_OfdmModulationMode_Object = MibTableColumn
ofdmModulationMode = _OfdmModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 5, 1, 3),
    _OfdmModulationMode_Type()
)
ofdmModulationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofdmModulationMode.setStatus("current")


class _OfdmGuardInterval_Type(Integer32):
    """Custom type ofdmGuardInterval based on Integer32"""
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
        *(("guard-1-4", 0),
          ("guard-1-8", 1),
          ("guard-1-16", 2),
          ("guard-1-32", 3))
    )


_OfdmGuardInterval_Type.__name__ = "Integer32"
_OfdmGuardInterval_Object = MibTableColumn
ofdmGuardInterval = _OfdmGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 5, 1, 4),
    _OfdmGuardInterval_Type()
)
ofdmGuardInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofdmGuardInterval.setStatus("current")


class _OfdmFECRate_Type(Integer32):
    """Custom type ofdmFECRate based on Integer32"""
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
        *(("fec1-2", 0),
          ("fec2-3", 1),
          ("fec3-4", 2),
          ("fec5-6", 3),
          ("fec7-8", 4))
    )


_OfdmFECRate_Type.__name__ = "Integer32"
_OfdmFECRate_Object = MibTableColumn
ofdmFECRate = _OfdmFECRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 5, 1, 5),
    _OfdmFECRate_Type()
)
ofdmFECRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofdmFECRate.setStatus("current")


class _OfdmTransmissionMode_Type(Integer32):
    """Custom type ofdmTransmissionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mode2k", 0),
          ("mode8k", 1))
    )


_OfdmTransmissionMode_Type.__name__ = "Integer32"
_OfdmTransmissionMode_Object = MibTableColumn
ofdmTransmissionMode = _OfdmTransmissionMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 5, 1, 6),
    _OfdmTransmissionMode_Type()
)
ofdmTransmissionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofdmTransmissionMode.setStatus("current")


class _OfdmSpectrumPolarity_Type(Integer32):
    """Custom type ofdmSpectrumPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high-side-IF", 0),
          ("low-side-IF", 1))
    )


_OfdmSpectrumPolarity_Type.__name__ = "Integer32"
_OfdmSpectrumPolarity_Object = MibTableColumn
ofdmSpectrumPolarity = _OfdmSpectrumPolarity_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 5, 1, 7),
    _OfdmSpectrumPolarity_Type()
)
ofdmSpectrumPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofdmSpectrumPolarity.setStatus("current")


class _OfdmBandwidth_Type(Integer32):
    """Custom type ofdmBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6000000, 12000000),
    )


_OfdmBandwidth_Type.__name__ = "Integer32"
_OfdmBandwidth_Object = MibTableColumn
ofdmBandwidth = _OfdmBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 5, 1, 8),
    _OfdmBandwidth_Type()
)
ofdmBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofdmBandwidth.setStatus("current")


class _OfdmDataRate188_Type(Integer32):
    """Custom type ofdmDataRate188 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )


_OfdmDataRate188_Type.__name__ = "Integer32"
_OfdmDataRate188_Object = MibTableColumn
ofdmDataRate188 = _OfdmDataRate188_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 5, 1, 9),
    _OfdmDataRate188_Type()
)
ofdmDataRate188.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofdmDataRate188.setStatus("current")


class _OfdmDataRate204_Type(Integer32):
    """Custom type ofdmDataRate204 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )


_OfdmDataRate204_Type.__name__ = "Integer32"
_OfdmDataRate204_Object = MibTableColumn
ofdmDataRate204 = _OfdmDataRate204_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 5, 1, 10),
    _OfdmDataRate204_Type()
)
ofdmDataRate204.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofdmDataRate204.setStatus("current")


class _OfdmUHFChannel_Type(DisplayString):
    """Custom type ofdmUHFChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_OfdmUHFChannel_Type.__name__ = "DisplayString"
_OfdmUHFChannel_Object = MibTableColumn
ofdmUHFChannel = _OfdmUHFChannel_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 5, 1, 11),
    _OfdmUHFChannel_Type()
)
ofdmUHFChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofdmUHFChannel.setStatus("current")


class _OfdmCentreFrequency_Type(Integer32):
    """Custom type ofdmCentreFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OfdmCentreFrequency_Type.__name__ = "Integer32"
_OfdmCentreFrequency_Object = MibTableColumn
ofdmCentreFrequency = _OfdmCentreFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 5, 1, 12),
    _OfdmCentreFrequency_Type()
)
ofdmCentreFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofdmCentreFrequency.setStatus("current")


class _OfdmSetBandwidth_Type(Integer32):
    """Custom type ofdmSetBandwidth based on Integer32"""
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
        *(("bandwidth-6MHz", 0),
          ("bandwidth-7MHz", 1),
          ("bandwidth-8MHz", 2),
          ("bandwidth-10MHz", 3),
          ("bandwidth-12MHz", 4))
    )


_OfdmSetBandwidth_Type.__name__ = "Integer32"
_OfdmSetBandwidth_Object = MibTableColumn
ofdmSetBandwidth = _OfdmSetBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 5, 1, 13),
    _OfdmSetBandwidth_Type()
)
ofdmSetBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofdmSetBandwidth.setStatus("current")


class _OfdmBandPlan_Type(DisplayString):
    """Custom type ofdmBandPlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_OfdmBandPlan_Type.__name__ = "DisplayString"
_OfdmBandPlan_Object = MibTableColumn
ofdmBandPlan = _OfdmBandPlan_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 5, 1, 14),
    _OfdmBandPlan_Type()
)
ofdmBandPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofdmBandPlan.setStatus("current")


class _OfdmMainBoardType_Type(DisplayString):
    """Custom type ofdmMainBoardType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_OfdmMainBoardType_Type.__name__ = "DisplayString"
_OfdmMainBoardType_Object = MibScalar
ofdmMainBoardType = _OfdmMainBoardType_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 6),
    _OfdmMainBoardType_Type()
)
ofdmMainBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofdmMainBoardType.setStatus("current")
_OfdmDaughterBoardTable_Object = MibTable
ofdmDaughterBoardTable = _OfdmDaughterBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 7)
)
if mibBuilder.loadTexts:
    ofdmDaughterBoardTable.setStatus("current")
_OfdmDaughterBoardEntry_Object = MibTableRow
ofdmDaughterBoardEntry = _OfdmDaughterBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 7, 1)
)
ofdmDaughterBoardEntry.setIndexNames(
    (0, "NDS-DTH3-OFDM", "ofdmDaughterBoardIndex"),
)
if mibBuilder.loadTexts:
    ofdmDaughterBoardEntry.setStatus("current")


class _OfdmDaughterBoardIndex_Type(Integer32):
    """Custom type ofdmDaughterBoardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_OfdmDaughterBoardIndex_Type.__name__ = "Integer32"
_OfdmDaughterBoardIndex_Object = MibTableColumn
ofdmDaughterBoardIndex = _OfdmDaughterBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 7, 1, 1),
    _OfdmDaughterBoardIndex_Type()
)
ofdmDaughterBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofdmDaughterBoardIndex.setStatus("current")


class _OfdmDaughterBoardType_Type(DisplayString):
    """Custom type ofdmDaughterBoardType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_OfdmDaughterBoardType_Type.__name__ = "DisplayString"
_OfdmDaughterBoardType_Object = MibTableColumn
ofdmDaughterBoardType = _OfdmDaughterBoardType_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 7, 1, 2),
    _OfdmDaughterBoardType_Type()
)
ofdmDaughterBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofdmDaughterBoardType.setStatus("current")


class _OfdmDaughterBoardVersion_Type(DisplayString):
    """Custom type ofdmDaughterBoardVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_OfdmDaughterBoardVersion_Type.__name__ = "DisplayString"
_OfdmDaughterBoardVersion_Object = MibTableColumn
ofdmDaughterBoardVersion = _OfdmDaughterBoardVersion_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 7, 1, 3),
    _OfdmDaughterBoardVersion_Type()
)
ofdmDaughterBoardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofdmDaughterBoardVersion.setStatus("current")


class _OfdmFeatures_Type(Integer32):
    """Custom type ofdmFeatures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OfdmFeatures_Type.__name__ = "Integer32"
_OfdmFeatures_Object = MibScalar
ofdmFeatures = _OfdmFeatures_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 8),
    _OfdmFeatures_Type()
)
ofdmFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofdmFeatures.setStatus("current")


class _OfdmBandwidthFlags_Type(Integer32):
    """Custom type ofdmBandwidthFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OfdmBandwidthFlags_Type.__name__ = "Integer32"
_OfdmBandwidthFlags_Object = MibScalar
ofdmBandwidthFlags = _OfdmBandwidthFlags_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 15, 9),
    _OfdmBandwidthFlags_Type()
)
ofdmBandwidthFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofdmBandwidthFlags.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NDS-DTH3-OFDM",
    **{"ndsDTH3Encoder": ndsDTH3Encoder,
       "ofdmEnc": ofdmEnc,
       "ofdmHardwareRelease": ofdmHardwareRelease,
       "ofdmSoftwareRelease": ofdmSoftwareRelease,
       "ofdmFirmwareRelease": ofdmFirmwareRelease,
       "ofdmnextTimeDate": ofdmnextTimeDate,
       "ofdmTable": ofdmTable,
       "ofdmEntry": ofdmEntry,
       "ofdmCurrentNextIndex": ofdmCurrentNextIndex,
       "ofdmOutput": ofdmOutput,
       "ofdmModulationMode": ofdmModulationMode,
       "ofdmGuardInterval": ofdmGuardInterval,
       "ofdmFECRate": ofdmFECRate,
       "ofdmTransmissionMode": ofdmTransmissionMode,
       "ofdmSpectrumPolarity": ofdmSpectrumPolarity,
       "ofdmBandwidth": ofdmBandwidth,
       "ofdmDataRate188": ofdmDataRate188,
       "ofdmDataRate204": ofdmDataRate204,
       "ofdmUHFChannel": ofdmUHFChannel,
       "ofdmCentreFrequency": ofdmCentreFrequency,
       "ofdmSetBandwidth": ofdmSetBandwidth,
       "ofdmBandPlan": ofdmBandPlan,
       "ofdmMainBoardType": ofdmMainBoardType,
       "ofdmDaughterBoardTable": ofdmDaughterBoardTable,
       "ofdmDaughterBoardEntry": ofdmDaughterBoardEntry,
       "ofdmDaughterBoardIndex": ofdmDaughterBoardIndex,
       "ofdmDaughterBoardType": ofdmDaughterBoardType,
       "ofdmDaughterBoardVersion": ofdmDaughterBoardVersion,
       "ofdmFeatures": ofdmFeatures,
       "ofdmBandwidthFlags": ofdmBandwidthFlags}
)

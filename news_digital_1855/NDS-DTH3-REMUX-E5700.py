# SNMP MIB module (NDS-DTH3-REMUX-E5700) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/news_digital_1855/NDS-DTH3-REMUX-E5700.mib
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
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

_RemuxE5700_ObjectIdentity = ObjectIdentity
remuxE5700 = _RemuxE5700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16)
)


class _RemuxSoftwareRelease_Type(DisplayString):
    """Custom type remuxSoftwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RemuxSoftwareRelease_Type.__name__ = "DisplayString"
_RemuxSoftwareRelease_Object = MibScalar
remuxSoftwareRelease = _RemuxSoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 1),
    _RemuxSoftwareRelease_Type()
)
remuxSoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxSoftwareRelease.setStatus("current")


class _RemuxFirmwareRelease_Type(DisplayString):
    """Custom type remuxFirmwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RemuxFirmwareRelease_Type.__name__ = "DisplayString"
_RemuxFirmwareRelease_Object = MibScalar
remuxFirmwareRelease = _RemuxFirmwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 2),
    _RemuxFirmwareRelease_Type()
)
remuxFirmwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxFirmwareRelease.setStatus("current")


class _RemuxOutputBitrate_Type(Integer32):
    """Custom type remuxOutputBitrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_RemuxOutputBitrate_Type.__name__ = "Integer32"
_RemuxOutputBitrate_Object = MibScalar
remuxOutputBitrate = _RemuxOutputBitrate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 3),
    _RemuxOutputBitrate_Type()
)
remuxOutputBitrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remuxOutputBitrate.setStatus("current")


class _RemuxPacketLength_Type(Integer32):
    """Custom type remuxPacketLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("length-188-bytes", 0),
          ("length-204-bytes", 1))
    )


_RemuxPacketLength_Type.__name__ = "Integer32"
_RemuxPacketLength_Object = MibScalar
remuxPacketLength = _RemuxPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 4),
    _RemuxPacketLength_Type()
)
remuxPacketLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remuxPacketLength.setStatus("current")


class _RemuxOutputEnabled_Type(Integer32):
    """Custom type remuxOutputEnabled based on Integer32"""
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


_RemuxOutputEnabled_Type.__name__ = "Integer32"
_RemuxOutputEnabled_Object = MibScalar
remuxOutputEnabled = _RemuxOutputEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 5),
    _RemuxOutputEnabled_Type()
)
remuxOutputEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxOutputEnabled.setStatus("current")
_RemuxInputInformationTable_Object = MibTable
remuxInputInformationTable = _RemuxInputInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 6)
)
if mibBuilder.loadTexts:
    remuxInputInformationTable.setStatus("current")
_RemuxInputInformationEntry_Object = MibTableRow
remuxInputInformationEntry = _RemuxInputInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 6, 1)
)
remuxInputInformationEntry.setIndexNames(
    (0, "NDS-DTH3-REMUX-E5700", "remuxInputChannel"),
)
if mibBuilder.loadTexts:
    remuxInputInformationEntry.setStatus("current")


class _RemuxInputChannel_Type(Integer32):
    """Custom type remuxInputChannel based on Integer32"""
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
        *(("local", 1),
          ("bnc1", 2),
          ("bnc2", 3),
          ("bnc3", 4))
    )


_RemuxInputChannel_Type.__name__ = "Integer32"
_RemuxInputChannel_Object = MibTableColumn
remuxInputChannel = _RemuxInputChannel_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 6, 1, 1),
    _RemuxInputChannel_Type()
)
remuxInputChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxInputChannel.setStatus("current")


class _RemuxInputDataRate_Type(Integer32):
    """Custom type remuxInputDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40000000),
    )


_RemuxInputDataRate_Type.__name__ = "Integer32"
_RemuxInputDataRate_Object = MibTableColumn
remuxInputDataRate = _RemuxInputDataRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 6, 1, 2),
    _RemuxInputDataRate_Type()
)
remuxInputDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxInputDataRate.setStatus("current")


class _RemuxInputPeakDataRate_Type(Integer32):
    """Custom type remuxInputPeakDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40000000),
    )


_RemuxInputPeakDataRate_Type.__name__ = "Integer32"
_RemuxInputPeakDataRate_Object = MibTableColumn
remuxInputPeakDataRate = _RemuxInputPeakDataRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 6, 1, 3),
    _RemuxInputPeakDataRate_Type()
)
remuxInputPeakDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxInputPeakDataRate.setStatus("current")


class _RemuxInputTSRate_Type(Integer32):
    """Custom type remuxInputTSRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40000000),
    )


_RemuxInputTSRate_Type.__name__ = "Integer32"
_RemuxInputTSRate_Object = MibTableColumn
remuxInputTSRate = _RemuxInputTSRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 6, 1, 4),
    _RemuxInputTSRate_Type()
)
remuxInputTSRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxInputTSRate.setStatus("current")


class _RemuxInputPATFilterVersion_Type(Integer32):
    """Custom type remuxInputPATFilterVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_RemuxInputPATFilterVersion_Type.__name__ = "Integer32"
_RemuxInputPATFilterVersion_Object = MibTableColumn
remuxInputPATFilterVersion = _RemuxInputPATFilterVersion_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 6, 1, 5),
    _RemuxInputPATFilterVersion_Type()
)
remuxInputPATFilterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxInputPATFilterVersion.setStatus("current")


class _RemuxInputSDTFilterVersion_Type(Integer32):
    """Custom type remuxInputSDTFilterVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_RemuxInputSDTFilterVersion_Type.__name__ = "Integer32"
_RemuxInputSDTFilterVersion_Object = MibTableColumn
remuxInputSDTFilterVersion = _RemuxInputSDTFilterVersion_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 6, 1, 6),
    _RemuxInputSDTFilterVersion_Type()
)
remuxInputSDTFilterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxInputSDTFilterVersion.setStatus("current")


class _RemuxInputMGTFilterVersion_Type(Integer32):
    """Custom type remuxInputMGTFilterVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_RemuxInputMGTFilterVersion_Type.__name__ = "Integer32"
_RemuxInputMGTFilterVersion_Object = MibTableColumn
remuxInputMGTFilterVersion = _RemuxInputMGTFilterVersion_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 6, 1, 7),
    _RemuxInputMGTFilterVersion_Type()
)
remuxInputMGTFilterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxInputMGTFilterVersion.setStatus("current")


class _RemuxInputTVCTFilterVersion_Type(Integer32):
    """Custom type remuxInputTVCTFilterVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_RemuxInputTVCTFilterVersion_Type.__name__ = "Integer32"
_RemuxInputTVCTFilterVersion_Object = MibTableColumn
remuxInputTVCTFilterVersion = _RemuxInputTVCTFilterVersion_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 6, 1, 8),
    _RemuxInputTVCTFilterVersion_Type()
)
remuxInputTVCTFilterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxInputTVCTFilterVersion.setStatus("current")


class _RemuxInputCVCTFilterVersion_Type(Integer32):
    """Custom type remuxInputCVCTFilterVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_RemuxInputCVCTFilterVersion_Type.__name__ = "Integer32"
_RemuxInputCVCTFilterVersion_Object = MibTableColumn
remuxInputCVCTFilterVersion = _RemuxInputCVCTFilterVersion_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 6, 1, 9),
    _RemuxInputCVCTFilterVersion_Type()
)
remuxInputCVCTFilterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxInputCVCTFilterVersion.setStatus("current")
_RemuxSITable_Object = MibTable
remuxSITable = _RemuxSITable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7)
)
if mibBuilder.loadTexts:
    remuxSITable.setStatus("current")
_RemuxSIEntry_Object = MibTableRow
remuxSIEntry = _RemuxSIEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1)
)
remuxSIEntry.setIndexNames(
    (0, "NDS-DTH3-REMUX-E5700", "remuxInputNumber"),
)
if mibBuilder.loadTexts:
    remuxSIEntry.setStatus("current")


class _RemuxInputNumber_Type(Integer32):
    """Custom type remuxInputNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RemuxInputNumber_Type.__name__ = "Integer32"
_RemuxInputNumber_Object = MibTableColumn
remuxInputNumber = _RemuxInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 1),
    _RemuxInputNumber_Type()
)
remuxInputNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxInputNumber.setStatus("current")


class _RemuxSIPATFilterVersion_Type(Integer32):
    """Custom type remuxSIPATFilterVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RemuxSIPATFilterVersion_Type.__name__ = "Integer32"
_RemuxSIPATFilterVersion_Object = MibTableColumn
remuxSIPATFilterVersion = _RemuxSIPATFilterVersion_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 2),
    _RemuxSIPATFilterVersion_Type()
)
remuxSIPATFilterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxSIPATFilterVersion.setStatus("current")


class _RemuxSISDTFilterVersion_Type(Integer32):
    """Custom type remuxSISDTFilterVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RemuxSISDTFilterVersion_Type.__name__ = "Integer32"
_RemuxSISDTFilterVersion_Object = MibTableColumn
remuxSISDTFilterVersion = _RemuxSISDTFilterVersion_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 3),
    _RemuxSISDTFilterVersion_Type()
)
remuxSISDTFilterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxSISDTFilterVersion.setStatus("current")


class _RemuxSIPMTFilterVersion_Type(Integer32):
    """Custom type remuxSIPMTFilterVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RemuxSIPMTFilterVersion_Type.__name__ = "Integer32"
_RemuxSIPMTFilterVersion_Object = MibTableColumn
remuxSIPMTFilterVersion = _RemuxSIPMTFilterVersion_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 4),
    _RemuxSIPMTFilterVersion_Type()
)
remuxSIPMTFilterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxSIPMTFilterVersion.setStatus("current")


class _RemuxSIEnabled_Type(Integer32):
    """Custom type remuxSIEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("on-ras", 2),
          ("on-BISS-mux-key", 3),
          ("on-BISS-mode-1", 4),
          ("on-BISS-E", 5),
          ("on-input-scrambled", 6))
    )


_RemuxSIEnabled_Type.__name__ = "Integer32"
_RemuxSIEnabled_Object = MibTableColumn
remuxSIEnabled = _RemuxSIEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 5),
    _RemuxSIEnabled_Type()
)
remuxSIEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remuxSIEnabled.setStatus("current")


class _RemuxSIOutputServiceId_Type(Integer32):
    """Custom type remuxSIOutputServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RemuxSIOutputServiceId_Type.__name__ = "Integer32"
_RemuxSIOutputServiceId_Object = MibTableColumn
remuxSIOutputServiceId = _RemuxSIOutputServiceId_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 6),
    _RemuxSIOutputServiceId_Type()
)
remuxSIOutputServiceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remuxSIOutputServiceId.setStatus("current")


class _RemuxSIOriginalServiceName_Type(DisplayString):
    """Custom type remuxSIOriginalServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RemuxSIOriginalServiceName_Type.__name__ = "DisplayString"
_RemuxSIOriginalServiceName_Object = MibTableColumn
remuxSIOriginalServiceName = _RemuxSIOriginalServiceName_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 7),
    _RemuxSIOriginalServiceName_Type()
)
remuxSIOriginalServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxSIOriginalServiceName.setStatus("current")


class _RemuxSIModifiedServiceName_Type(DisplayString):
    """Custom type remuxSIModifiedServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RemuxSIModifiedServiceName_Type.__name__ = "DisplayString"
_RemuxSIModifiedServiceName_Object = MibTableColumn
remuxSIModifiedServiceName = _RemuxSIModifiedServiceName_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 8),
    _RemuxSIModifiedServiceName_Type()
)
remuxSIModifiedServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remuxSIModifiedServiceName.setStatus("current")


class _RemuxSIBitRate_Type(Integer32):
    """Custom type remuxSIBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_RemuxSIBitRate_Type.__name__ = "Integer32"
_RemuxSIBitRate_Object = MibTableColumn
remuxSIBitRate = _RemuxSIBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 9),
    _RemuxSIBitRate_Type()
)
remuxSIBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxSIBitRate.setStatus("current")


class _RemuxSIOriginalServiceProvider_Type(DisplayString):
    """Custom type remuxSIOriginalServiceProvider based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RemuxSIOriginalServiceProvider_Type.__name__ = "DisplayString"
_RemuxSIOriginalServiceProvider_Object = MibTableColumn
remuxSIOriginalServiceProvider = _RemuxSIOriginalServiceProvider_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 10),
    _RemuxSIOriginalServiceProvider_Type()
)
remuxSIOriginalServiceProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxSIOriginalServiceProvider.setStatus("current")


class _RemuxSIModifiedServiceProvider_Type(DisplayString):
    """Custom type remuxSIModifiedServiceProvider based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RemuxSIModifiedServiceProvider_Type.__name__ = "DisplayString"
_RemuxSIModifiedServiceProvider_Object = MibTableColumn
remuxSIModifiedServiceProvider = _RemuxSIModifiedServiceProvider_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 11),
    _RemuxSIModifiedServiceProvider_Type()
)
remuxSIModifiedServiceProvider.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remuxSIModifiedServiceProvider.setStatus("current")


class _RemuxSIInputServiceId_Type(Integer32):
    """Custom type remuxSIInputServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RemuxSIInputServiceId_Type.__name__ = "Integer32"
_RemuxSIInputServiceId_Object = MibTableColumn
remuxSIInputServiceId = _RemuxSIInputServiceId_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 12),
    _RemuxSIInputServiceId_Type()
)
remuxSIInputServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxSIInputServiceId.setStatus("current")


class _RemuxSIChannelNo_Type(Integer32):
    """Custom type remuxSIChannelNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_RemuxSIChannelNo_Type.__name__ = "Integer32"
_RemuxSIChannelNo_Object = MibTableColumn
remuxSIChannelNo = _RemuxSIChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 13),
    _RemuxSIChannelNo_Type()
)
remuxSIChannelNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remuxSIChannelNo.setStatus("current")


class _RemuxSIMGTFilterVersion_Type(Integer32):
    """Custom type remuxSIMGTFilterVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RemuxSIMGTFilterVersion_Type.__name__ = "Integer32"
_RemuxSIMGTFilterVersion_Object = MibTableColumn
remuxSIMGTFilterVersion = _RemuxSIMGTFilterVersion_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 14),
    _RemuxSIMGTFilterVersion_Type()
)
remuxSIMGTFilterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxSIMGTFilterVersion.setStatus("current")


class _RemuxSIInputPort_Type(Integer32):
    """Custom type remuxSIInputPort based on Integer32"""
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
        *(("local", 1),
          ("bnc1", 2),
          ("bnc2", 3),
          ("bnc3", 4))
    )


_RemuxSIInputPort_Type.__name__ = "Integer32"
_RemuxSIInputPort_Object = MibTableColumn
remuxSIInputPort = _RemuxSIInputPort_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 15),
    _RemuxSIInputPort_Type()
)
remuxSIInputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxSIInputPort.setStatus("current")


class _RemuxSIValid_Type(Integer32):
    """Custom type remuxSIValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-valid", 0),
          ("valid", 1))
    )


_RemuxSIValid_Type.__name__ = "Integer32"
_RemuxSIValid_Object = MibTableColumn
remuxSIValid = _RemuxSIValid_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 16),
    _RemuxSIValid_Type()
)
remuxSIValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxSIValid.setStatus("current")


class _RemuxSIInputScrambled_Type(Integer32):
    """Custom type remuxSIInputScrambled based on Integer32"""
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
        *(("in-the-clear", 0),
          ("biss-mode-1", 1),
          ("biss-mode-2", 2),
          ("ras", 3),
          ("unknown-format", 4))
    )


_RemuxSIInputScrambled_Type.__name__ = "Integer32"
_RemuxSIInputScrambled_Object = MibTableColumn
remuxSIInputScrambled = _RemuxSIInputScrambled_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 17),
    _RemuxSIInputScrambled_Type()
)
remuxSIInputScrambled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxSIInputScrambled.setStatus("current")


class _RemuxBISSSessionWord_Type(OctetString):
    """Custom type remuxBISSSessionWord based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 7),
    )


_RemuxBISSSessionWord_Type.__name__ = "OctetString"
_RemuxBISSSessionWord_Object = MibTableColumn
remuxBISSSessionWord = _RemuxBISSSessionWord_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 18),
    _RemuxBISSSessionWord_Type()
)
remuxBISSSessionWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remuxBISSSessionWord.setStatus("current")


class _RemuxBISSEncryptedSessionWord_Type(OctetString):
    """Custom type remuxBISSEncryptedSessionWord based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_RemuxBISSEncryptedSessionWord_Type.__name__ = "OctetString"
_RemuxBISSEncryptedSessionWord_Object = MibTableColumn
remuxBISSEncryptedSessionWord = _RemuxBISSEncryptedSessionWord_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 19),
    _RemuxBISSEncryptedSessionWord_Type()
)
remuxBISSEncryptedSessionWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remuxBISSEncryptedSessionWord.setStatus("current")


class _RemuxMaxBitRateLimit_Type(Integer32):
    """Custom type remuxMaxBitRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )


_RemuxMaxBitRateLimit_Type.__name__ = "Integer32"
_RemuxMaxBitRateLimit_Object = MibTableColumn
remuxMaxBitRateLimit = _RemuxMaxBitRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 20),
    _RemuxMaxBitRateLimit_Type()
)
remuxMaxBitRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remuxMaxBitRateLimit.setStatus("current")


class _RemuxSIClosedCaption_Type(Integer32):
    """Custom type remuxSIClosedCaption based on Integer32"""
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


_RemuxSIClosedCaption_Type.__name__ = "Integer32"
_RemuxSIClosedCaption_Object = MibTableColumn
remuxSIClosedCaption = _RemuxSIClosedCaption_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 21),
    _RemuxSIClosedCaption_Type()
)
remuxSIClosedCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxSIClosedCaption.setStatus("current")


class _RemuxSIServiceType_Type(Integer32):
    """Custom type remuxSIServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RemuxSIServiceType_Type.__name__ = "Integer32"
_RemuxSIServiceType_Object = MibTableColumn
remuxSIServiceType = _RemuxSIServiceType_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 7, 1, 22),
    _RemuxSIServiceType_Type()
)
remuxSIServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxSIServiceType.setStatus("current")
_RemuxSIPIDTable_Object = MibTable
remuxSIPIDTable = _RemuxSIPIDTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 8)
)
if mibBuilder.loadTexts:
    remuxSIPIDTable.setStatus("current")
_RemuxSIPIDEntry_Object = MibTableRow
remuxSIPIDEntry = _RemuxSIPIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 8, 1)
)
remuxSIPIDEntry.setIndexNames(
    (0, "NDS-DTH3-REMUX-E5700", "remuxInputNumber"),
    (0, "NDS-DTH3-REMUX-E5700", "remuxPIDEntryIndex"),
)
if mibBuilder.loadTexts:
    remuxSIPIDEntry.setStatus("current")


class _RemuxPIDEntryIndex_Type(Integer32):
    """Custom type remuxPIDEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RemuxPIDEntryIndex_Type.__name__ = "Integer32"
_RemuxPIDEntryIndex_Object = MibTableColumn
remuxPIDEntryIndex = _RemuxPIDEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 8, 1, 1),
    _RemuxPIDEntryIndex_Type()
)
remuxPIDEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxPIDEntryIndex.setStatus("current")


class _RemuxServiceType_Type(Integer32):
    """Custom type remuxServiceType based on Integer32"""
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
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("pmt", 1),
          ("video", 2),
          ("mpeg-2-audio", 3),
          ("ac3-audio", 4),
          ("linear-pcm-audio", 5),
          ("mpeg-1-audio", 6),
          ("rs232", 7),
          ("rs422", 8),
          ("teletext", 9),
          ("vbi", 10),
          ("pcr", 11),
          ("private-data", 12),
          ("ecm", 13),
          ("other", 14),
          ("dts-audio", 15))
    )


_RemuxServiceType_Type.__name__ = "Integer32"
_RemuxServiceType_Object = MibTableColumn
remuxServiceType = _RemuxServiceType_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 8, 1, 2),
    _RemuxServiceType_Type()
)
remuxServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxServiceType.setStatus("current")


class _RemuxOriginalPID_Type(Integer32):
    """Custom type remuxOriginalPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_RemuxOriginalPID_Type.__name__ = "Integer32"
_RemuxOriginalPID_Object = MibTableColumn
remuxOriginalPID = _RemuxOriginalPID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 8, 1, 3),
    _RemuxOriginalPID_Type()
)
remuxOriginalPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxOriginalPID.setStatus("current")


class _RemuxModifiedPID_Type(Integer32):
    """Custom type remuxModifiedPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_RemuxModifiedPID_Type.__name__ = "Integer32"
_RemuxModifiedPID_Object = MibTableColumn
remuxModifiedPID = _RemuxModifiedPID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 8, 1, 4),
    _RemuxModifiedPID_Type()
)
remuxModifiedPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remuxModifiedPID.setStatus("current")
_RemuxSIAudioLanguageTable_Object = MibTable
remuxSIAudioLanguageTable = _RemuxSIAudioLanguageTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 9)
)
if mibBuilder.loadTexts:
    remuxSIAudioLanguageTable.setStatus("current")
_RemuxSIAudioLanguageEntry_Object = MibTableRow
remuxSIAudioLanguageEntry = _RemuxSIAudioLanguageEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 9, 1)
)
remuxSIAudioLanguageEntry.setIndexNames(
    (0, "NDS-DTH3-REMUX-E5700", "remuxInputNumber"),
    (0, "NDS-DTH3-REMUX-E5700", "remuxAudioEntryIndex"),
)
if mibBuilder.loadTexts:
    remuxSIAudioLanguageEntry.setStatus("current")


class _RemuxAudioEntryIndex_Type(Integer32):
    """Custom type remuxAudioEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RemuxAudioEntryIndex_Type.__name__ = "Integer32"
_RemuxAudioEntryIndex_Object = MibTableColumn
remuxAudioEntryIndex = _RemuxAudioEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 9, 1, 1),
    _RemuxAudioEntryIndex_Type()
)
remuxAudioEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxAudioEntryIndex.setStatus("current")


class _RemuxAudioLanguageLeft_Type(DisplayString):
    """Custom type remuxAudioLanguageLeft based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_RemuxAudioLanguageLeft_Type.__name__ = "DisplayString"
_RemuxAudioLanguageLeft_Object = MibTableColumn
remuxAudioLanguageLeft = _RemuxAudioLanguageLeft_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 9, 1, 2),
    _RemuxAudioLanguageLeft_Type()
)
remuxAudioLanguageLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxAudioLanguageLeft.setStatus("current")


class _RemuxAudioLanguageRight_Type(DisplayString):
    """Custom type remuxAudioLanguageRight based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_RemuxAudioLanguageRight_Type.__name__ = "DisplayString"
_RemuxAudioLanguageRight_Object = MibTableColumn
remuxAudioLanguageRight = _RemuxAudioLanguageRight_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 9, 1, 3),
    _RemuxAudioLanguageRight_Type()
)
remuxAudioLanguageRight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remuxAudioLanguageRight.setStatus("current")


class _RemuxMode_Type(Integer32):
    """Custom type remuxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("intelligent", 0),
          ("dumb", 1))
    )


_RemuxMode_Type.__name__ = "Integer32"
_RemuxMode_Object = MibScalar
remuxMode = _RemuxMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 10),
    _RemuxMode_Type()
)
remuxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remuxMode.setStatus("current")


class _RemuxSNMPDisplay_Type(Integer32):
    """Custom type remuxSNMPDisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("showAllServices", 0),
          ("showValidServicesOnly", 1))
    )


_RemuxSNMPDisplay_Type.__name__ = "Integer32"
_RemuxSNMPDisplay_Object = MibScalar
remuxSNMPDisplay = _RemuxSNMPDisplay_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 11),
    _RemuxSNMPDisplay_Type()
)
remuxSNMPDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remuxSNMPDisplay.setStatus("current")


class _RemuxHostBitrate188_Type(Integer32):
    """Custom type remuxHostBitrate188 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_RemuxHostBitrate188_Type.__name__ = "Integer32"
_RemuxHostBitrate188_Object = MibScalar
remuxHostBitrate188 = _RemuxHostBitrate188_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 16, 12),
    _RemuxHostBitrate188_Type()
)
remuxHostBitrate188.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remuxHostBitrate188.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NDS-DTH3-REMUX-E5700",
    **{"ndsDTH3Encoder": ndsDTH3Encoder,
       "remuxE5700": remuxE5700,
       "remuxSoftwareRelease": remuxSoftwareRelease,
       "remuxFirmwareRelease": remuxFirmwareRelease,
       "remuxOutputBitrate": remuxOutputBitrate,
       "remuxPacketLength": remuxPacketLength,
       "remuxOutputEnabled": remuxOutputEnabled,
       "remuxInputInformationTable": remuxInputInformationTable,
       "remuxInputInformationEntry": remuxInputInformationEntry,
       "remuxInputChannel": remuxInputChannel,
       "remuxInputDataRate": remuxInputDataRate,
       "remuxInputPeakDataRate": remuxInputPeakDataRate,
       "remuxInputTSRate": remuxInputTSRate,
       "remuxInputPATFilterVersion": remuxInputPATFilterVersion,
       "remuxInputSDTFilterVersion": remuxInputSDTFilterVersion,
       "remuxInputMGTFilterVersion": remuxInputMGTFilterVersion,
       "remuxInputTVCTFilterVersion": remuxInputTVCTFilterVersion,
       "remuxInputCVCTFilterVersion": remuxInputCVCTFilterVersion,
       "remuxSITable": remuxSITable,
       "remuxSIEntry": remuxSIEntry,
       "remuxInputNumber": remuxInputNumber,
       "remuxSIPATFilterVersion": remuxSIPATFilterVersion,
       "remuxSISDTFilterVersion": remuxSISDTFilterVersion,
       "remuxSIPMTFilterVersion": remuxSIPMTFilterVersion,
       "remuxSIEnabled": remuxSIEnabled,
       "remuxSIOutputServiceId": remuxSIOutputServiceId,
       "remuxSIOriginalServiceName": remuxSIOriginalServiceName,
       "remuxSIModifiedServiceName": remuxSIModifiedServiceName,
       "remuxSIBitRate": remuxSIBitRate,
       "remuxSIOriginalServiceProvider": remuxSIOriginalServiceProvider,
       "remuxSIModifiedServiceProvider": remuxSIModifiedServiceProvider,
       "remuxSIInputServiceId": remuxSIInputServiceId,
       "remuxSIChannelNo": remuxSIChannelNo,
       "remuxSIMGTFilterVersion": remuxSIMGTFilterVersion,
       "remuxSIInputPort": remuxSIInputPort,
       "remuxSIValid": remuxSIValid,
       "remuxSIInputScrambled": remuxSIInputScrambled,
       "remuxBISSSessionWord": remuxBISSSessionWord,
       "remuxBISSEncryptedSessionWord": remuxBISSEncryptedSessionWord,
       "remuxMaxBitRateLimit": remuxMaxBitRateLimit,
       "remuxSIClosedCaption": remuxSIClosedCaption,
       "remuxSIServiceType": remuxSIServiceType,
       "remuxSIPIDTable": remuxSIPIDTable,
       "remuxSIPIDEntry": remuxSIPIDEntry,
       "remuxPIDEntryIndex": remuxPIDEntryIndex,
       "remuxServiceType": remuxServiceType,
       "remuxOriginalPID": remuxOriginalPID,
       "remuxModifiedPID": remuxModifiedPID,
       "remuxSIAudioLanguageTable": remuxSIAudioLanguageTable,
       "remuxSIAudioLanguageEntry": remuxSIAudioLanguageEntry,
       "remuxAudioEntryIndex": remuxAudioEntryIndex,
       "remuxAudioLanguageLeft": remuxAudioLanguageLeft,
       "remuxAudioLanguageRight": remuxAudioLanguageRight,
       "remuxMode": remuxMode,
       "remuxSNMPDisplay": remuxSNMPDisplay,
       "remuxHostBitrate188": remuxHostBitrate188}
)

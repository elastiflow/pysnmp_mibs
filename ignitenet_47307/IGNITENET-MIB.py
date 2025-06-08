# SNMP MIB module (IGNITENET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ignitenet_47307/IGNITENET-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:48:39 2025
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

ignitenetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47307, 1)
)
if mibBuilder.loadTexts:
    ignitenetMIB.setRevisions(
        ("2016-02-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RadioIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class EthernetIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class FrequencyGHz(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )



class RadioMcsRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              49)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("mcs-6m", 4),
          ("mcs-9M", 5),
          ("mcs-12M", 6),
          ("mcs-18M", 7),
          ("mcs-24M", 8),
          ("mcs-36M", 9),
          ("mcs-48M", 10),
          ("mcs-54M", 11),
          ("mcs0", 12),
          ("mcs1", 13),
          ("mcs2", 14),
          ("mcs3", 15),
          ("mcs4", 16),
          ("mcs5", 17),
          ("mcs6", 18),
          ("mcs7", 19),
          ("mcs8", 20),
          ("mcs9", 21),
          ("mcs10", 22),
          ("mcs11", 23),
          ("mcs12", 24),
          ("mcs13", 25),
          ("mcs14", 26),
          ("mcs15", 27),
          ("nss1-mcs0", 30),
          ("nss1-mcs1", 31),
          ("nss1-mcs2", 32),
          ("nss1-mcs3", 33),
          ("nss1-mcs4", 34),
          ("nss1-mcs5", 35),
          ("nss1-mcs6", 36),
          ("nss1-mcs7", 37),
          ("nss1-mcs8", 38),
          ("nss1-mcs9", 39),
          ("nss2-mcs1", 40),
          ("nss2-mcs2", 41),
          ("nss2-mcs3", 42),
          ("nss2-mcs4", 43),
          ("nss2-mcs5", 44),
          ("nss2-mcs6", 45),
          ("nss2-mcs7", 46),
          ("nss2-mcs8", 47),
          ("nss2-mcs9", 49))
    )



# MIB Managed Objects in the order of their OIDs

_Ignitenet_ObjectIdentity = ObjectIdentity
ignitenet = _Ignitenet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47307)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47307, 1, 1)
)


class _Model_Type(DisplayString):
    """Custom type model based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Model_Type.__name__ = "DisplayString"
_Model_Object = MibScalar
model = _Model_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 1, 1),
    _Model_Type()
)
model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model.setStatus("current")


class _HwVersion_Type(DisplayString):
    """Custom type hwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwVersion_Type.__name__ = "DisplayString"
_HwVersion_Object = MibScalar
hwVersion = _HwVersion_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 1, 2),
    _HwVersion_Type()
)
hwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVersion.setStatus("current")


class _FwVersion_Type(DisplayString):
    """Custom type fwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwVersion_Type.__name__ = "DisplayString"
_FwVersion_Object = MibScalar
fwVersion = _FwVersion_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 1, 3),
    _FwVersion_Type()
)
fwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVersion.setStatus("current")
_EthernetPorts_ObjectIdentity = ObjectIdentity
ethernetPorts = _EthernetPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47307, 1, 2)
)
_EthNumber_Type = Integer32
_EthNumber_Object = MibScalar
ethNumber = _EthNumber_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 2, 1),
    _EthNumber_Type()
)
ethNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethNumber.setStatus("current")
_EthInfoTable_Object = MibTable
ethInfoTable = _EthInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ethInfoTable.setStatus("current")
_EthInfoEntry_Object = MibTableRow
ethInfoEntry = _EthInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 2, 2, 1)
)
ethInfoEntry.setIndexNames(
    (0, "IGNITENET-MIB", "ethNumber"),
)
if mibBuilder.loadTexts:
    ethInfoEntry.setStatus("current")
_EthInfoIndex_Type = EthernetIndex
_EthInfoIndex_Object = MibTableColumn
ethInfoIndex = _EthInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 2, 2, 1, 1),
    _EthInfoIndex_Type()
)
ethInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethInfoIndex.setStatus("current")


class _EthDescr_Type(DisplayString):
    """Custom type ethDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EthDescr_Type.__name__ = "DisplayString"
_EthDescr_Object = MibTableColumn
ethDescr = _EthDescr_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 2, 2, 1, 2),
    _EthDescr_Type()
)
ethDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDescr.setStatus("current")
_EthInfoSpeed_Type = Integer32
_EthInfoSpeed_Object = MibTableColumn
ethInfoSpeed = _EthInfoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 2, 2, 1, 3),
    _EthInfoSpeed_Type()
)
ethInfoSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethInfoSpeed.setStatus("current")


class _EthInfoDuplex_Type(Integer32):
    """Custom type ethInfoDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("half", 1),
          ("full", 2))
    )


_EthInfoDuplex_Type.__name__ = "Integer32"
_EthInfoDuplex_Object = MibTableColumn
ethInfoDuplex = _EthInfoDuplex_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 2, 2, 1, 4),
    _EthInfoDuplex_Type()
)
ethInfoDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethInfoDuplex.setStatus("current")
_Radios_ObjectIdentity = ObjectIdentity
radios = _Radios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47307, 1, 3)
)
_MetrolinqRadios_ObjectIdentity = ObjectIdentity
metrolinqRadios = _MetrolinqRadios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4)
)
_MlRadioNumber_Type = Integer32
_MlRadioNumber_Object = MibScalar
mlRadioNumber = _MlRadioNumber_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 1),
    _MlRadioNumber_Type()
)
mlRadioNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioNumber.setStatus("current")
_MlRadioInfoTable_Object = MibTable
mlRadioInfoTable = _MlRadioInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 2)
)
if mibBuilder.loadTexts:
    mlRadioInfoTable.setStatus("current")
_MlRadioInfoEntry_Object = MibTableRow
mlRadioInfoEntry = _MlRadioInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 2, 1)
)
mlRadioInfoEntry.setIndexNames(
    (0, "IGNITENET-MIB", "mlRadioNumber"),
)
if mibBuilder.loadTexts:
    mlRadioInfoEntry.setStatus("current")
_MlRadioInfoIndex_Type = RadioIndex
_MlRadioInfoIndex_Object = MibTableColumn
mlRadioInfoIndex = _MlRadioInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 2, 1, 1),
    _MlRadioInfoIndex_Type()
)
mlRadioInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioInfoIndex.setStatus("current")


class _MlRadioInfoEnabled_Type(Integer32):
    """Custom type mlRadioInfoEnabled based on Integer32"""
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


_MlRadioInfoEnabled_Type.__name__ = "Integer32"
_MlRadioInfoEnabled_Object = MibTableColumn
mlRadioInfoEnabled = _MlRadioInfoEnabled_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 2, 1, 2),
    _MlRadioInfoEnabled_Type()
)
mlRadioInfoEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioInfoEnabled.setStatus("current")


class _MlRadioInfoRegDomain_Type(DisplayString):
    """Custom type mlRadioInfoRegDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MlRadioInfoRegDomain_Type.__name__ = "DisplayString"
_MlRadioInfoRegDomain_Object = MibTableColumn
mlRadioInfoRegDomain = _MlRadioInfoRegDomain_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 2, 1, 3),
    _MlRadioInfoRegDomain_Type()
)
mlRadioInfoRegDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioInfoRegDomain.setStatus("current")
_MlRadioInfoFrequency_Type = FrequencyGHz
_MlRadioInfoFrequency_Object = MibTableColumn
mlRadioInfoFrequency = _MlRadioInfoFrequency_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 2, 1, 4),
    _MlRadioInfoFrequency_Type()
)
mlRadioInfoFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioInfoFrequency.setStatus("current")
_MlRadioInfomcs_Type = RadioMcsRate
_MlRadioInfomcs_Object = MibTableColumn
mlRadioInfomcs = _MlRadioInfomcs_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 2, 1, 5),
    _MlRadioInfomcs_Type()
)
mlRadioInfomcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioInfomcs.setStatus("current")
_MlRadioInfoAckTimeout_Type = Integer32
_MlRadioInfoAckTimeout_Object = MibTableColumn
mlRadioInfoAckTimeout = _MlRadioInfoAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 2, 1, 6),
    _MlRadioInfoAckTimeout_Type()
)
mlRadioInfoAckTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioInfoAckTimeout.setStatus("current")
_MlRadioInfoTxPower_Type = Integer32
_MlRadioInfoTxPower_Object = MibTableColumn
mlRadioInfoTxPower = _MlRadioInfoTxPower_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 2, 1, 7),
    _MlRadioInfoTxPower_Type()
)
mlRadioInfoTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioInfoTxPower.setStatus("current")


class _MlRadioInfoAMSDU_Type(Integer32):
    """Custom type mlRadioInfoAMSDU based on Integer32"""
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


_MlRadioInfoAMSDU_Type.__name__ = "Integer32"
_MlRadioInfoAMSDU_Object = MibTableColumn
mlRadioInfoAMSDU = _MlRadioInfoAMSDU_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 2, 1, 8),
    _MlRadioInfoAMSDU_Type()
)
mlRadioInfoAMSDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioInfoAMSDU.setStatus("current")


class _MlRadioInfoAMPDU_Type(Integer32):
    """Custom type mlRadioInfoAMPDU based on Integer32"""
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


_MlRadioInfoAMPDU_Type.__name__ = "Integer32"
_MlRadioInfoAMPDU_Object = MibTableColumn
mlRadioInfoAMPDU = _MlRadioInfoAMPDU_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 2, 1, 9),
    _MlRadioInfoAMPDU_Type()
)
mlRadioInfoAMPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioInfoAMPDU.setStatus("current")
_MlRadioInfoRSSILocal_Type = Integer32
_MlRadioInfoRSSILocal_Object = MibTableColumn
mlRadioInfoRSSILocal = _MlRadioInfoRSSILocal_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 2, 1, 10),
    _MlRadioInfoRSSILocal_Type()
)
mlRadioInfoRSSILocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioInfoRSSILocal.setStatus("current")
_MlRadioInfoRSSIRemote_Type = Integer32
_MlRadioInfoRSSIRemote_Object = MibTableColumn
mlRadioInfoRSSIRemote = _MlRadioInfoRSSIRemote_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 2, 1, 11),
    _MlRadioInfoRSSIRemote_Type()
)
mlRadioInfoRSSIRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioInfoRSSIRemote.setStatus("current")


class _MlRadioInfoEncryption_Type(Integer32):
    """Custom type mlRadioInfoEncryption based on Integer32"""
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


_MlRadioInfoEncryption_Type.__name__ = "Integer32"
_MlRadioInfoEncryption_Object = MibTableColumn
mlRadioInfoEncryption = _MlRadioInfoEncryption_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 2, 1, 12),
    _MlRadioInfoEncryption_Type()
)
mlRadioInfoEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioInfoEncryption.setStatus("current")


class _MlRadioInfoSSID_Type(DisplayString):
    """Custom type mlRadioInfoSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MlRadioInfoSSID_Type.__name__ = "DisplayString"
_MlRadioInfoSSID_Object = MibTableColumn
mlRadioInfoSSID = _MlRadioInfoSSID_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 2, 1, 13),
    _MlRadioInfoSSID_Type()
)
mlRadioInfoSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioInfoSSID.setStatus("current")


class _MlRadioInfoFailover_Type(Integer32):
    """Custom type mlRadioInfoFailover based on Integer32"""
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


_MlRadioInfoFailover_Type.__name__ = "Integer32"
_MlRadioInfoFailover_Object = MibTableColumn
mlRadioInfoFailover = _MlRadioInfoFailover_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 2, 1, 14),
    _MlRadioInfoFailover_Type()
)
mlRadioInfoFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioInfoFailover.setStatus("current")
_MlRadioStatusTable_Object = MibTable
mlRadioStatusTable = _MlRadioStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 3)
)
if mibBuilder.loadTexts:
    mlRadioStatusTable.setStatus("current")
_MlRadioStatusEntry_Object = MibTableRow
mlRadioStatusEntry = _MlRadioStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 3, 1)
)
mlRadioStatusEntry.setIndexNames(
    (0, "IGNITENET-MIB", "mlRadioNumber"),
)
if mibBuilder.loadTexts:
    mlRadioStatusEntry.setStatus("current")
_MlRadioStatusIndex_Type = RadioIndex
_MlRadioStatusIndex_Object = MibTableColumn
mlRadioStatusIndex = _MlRadioStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 3, 1, 1),
    _MlRadioStatusIndex_Type()
)
mlRadioStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioStatusIndex.setStatus("current")


class _MlRadioStatusFailoverStatus_Type(Integer32):
    """Custom type mlRadioStatusFailoverStatus based on Integer32"""
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


_MlRadioStatusFailoverStatus_Type.__name__ = "Integer32"
_MlRadioStatusFailoverStatus_Object = MibTableColumn
mlRadioStatusFailoverStatus = _MlRadioStatusFailoverStatus_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 3, 1, 2),
    _MlRadioStatusFailoverStatus_Type()
)
mlRadioStatusFailoverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioStatusFailoverStatus.setStatus("current")
_MlRadioStatusFailoverStats_Type = Integer32
_MlRadioStatusFailoverStats_Object = MibTableColumn
mlRadioStatusFailoverStats = _MlRadioStatusFailoverStats_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 3, 1, 3),
    _MlRadioStatusFailoverStats_Type()
)
mlRadioStatusFailoverStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioStatusFailoverStats.setStatus("current")
_MlRadioStatusCRCErrors_Type = Integer32
_MlRadioStatusCRCErrors_Object = MibTableColumn
mlRadioStatusCRCErrors = _MlRadioStatusCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 3, 1, 4),
    _MlRadioStatusCRCErrors_Type()
)
mlRadioStatusCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioStatusCRCErrors.setStatus("current")
_MlRadioStatusDrops_Type = Integer32
_MlRadioStatusDrops_Object = MibTableColumn
mlRadioStatusDrops = _MlRadioStatusDrops_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 3, 1, 5),
    _MlRadioStatusDrops_Type()
)
mlRadioStatusDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioStatusDrops.setStatus("current")
_MlRadioStatusRetries_Type = Integer32
_MlRadioStatusRetries_Object = MibTableColumn
mlRadioStatusRetries = _MlRadioStatusRetries_Object(
    (1, 3, 6, 1, 4, 1, 47307, 1, 4, 3, 1, 6),
    _MlRadioStatusRetries_Type()
)
mlRadioStatusRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlRadioStatusRetries.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IGNITENET-MIB",
    **{"RadioIndex": RadioIndex,
       "EthernetIndex": EthernetIndex,
       "FrequencyGHz": FrequencyGHz,
       "RadioMcsRate": RadioMcsRate,
       "ignitenet": ignitenet,
       "ignitenetMIB": ignitenetMIB,
       "product": product,
       "model": model,
       "hwVersion": hwVersion,
       "fwVersion": fwVersion,
       "ethernetPorts": ethernetPorts,
       "ethNumber": ethNumber,
       "ethInfoTable": ethInfoTable,
       "ethInfoEntry": ethInfoEntry,
       "ethInfoIndex": ethInfoIndex,
       "ethDescr": ethDescr,
       "ethInfoSpeed": ethInfoSpeed,
       "ethInfoDuplex": ethInfoDuplex,
       "radios": radios,
       "metrolinqRadios": metrolinqRadios,
       "mlRadioNumber": mlRadioNumber,
       "mlRadioInfoTable": mlRadioInfoTable,
       "mlRadioInfoEntry": mlRadioInfoEntry,
       "mlRadioInfoIndex": mlRadioInfoIndex,
       "mlRadioInfoEnabled": mlRadioInfoEnabled,
       "mlRadioInfoRegDomain": mlRadioInfoRegDomain,
       "mlRadioInfoFrequency": mlRadioInfoFrequency,
       "mlRadioInfomcs": mlRadioInfomcs,
       "mlRadioInfoAckTimeout": mlRadioInfoAckTimeout,
       "mlRadioInfoTxPower": mlRadioInfoTxPower,
       "mlRadioInfoAMSDU": mlRadioInfoAMSDU,
       "mlRadioInfoAMPDU": mlRadioInfoAMPDU,
       "mlRadioInfoRSSILocal": mlRadioInfoRSSILocal,
       "mlRadioInfoRSSIRemote": mlRadioInfoRSSIRemote,
       "mlRadioInfoEncryption": mlRadioInfoEncryption,
       "mlRadioInfoSSID": mlRadioInfoSSID,
       "mlRadioInfoFailover": mlRadioInfoFailover,
       "mlRadioStatusTable": mlRadioStatusTable,
       "mlRadioStatusEntry": mlRadioStatusEntry,
       "mlRadioStatusIndex": mlRadioStatusIndex,
       "mlRadioStatusFailoverStatus": mlRadioStatusFailoverStatus,
       "mlRadioStatusFailoverStats": mlRadioStatusFailoverStats,
       "mlRadioStatusCRCErrors": mlRadioStatusCRCErrors,
       "mlRadioStatusDrops": mlRadioStatusDrops,
       "mlRadioStatusRetries": mlRadioStatusRetries}
)

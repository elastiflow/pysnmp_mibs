# SNMP MIB module (PKTC-SIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/PKTC-SP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:41:44 2025
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

(clabProjPacketCable,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjPacketCable")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 Bits,
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pktcSigMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2)
)
if mibBuilder.loadTexts:
    pktcSigMib.setRevisions(
        ("2007-11-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PktcCodecType(TextualConvention, Integer32):
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
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("g729", 3),
          ("reserved", 4),
          ("g729E", 5),
          ("pcmu", 6),
          ("g726at32", 7),
          ("g728", 8),
          ("pcma", 9),
          ("g726at16", 10),
          ("g726at24", 11),
          ("g726at40", 12))
    )



class PktcRingCadence(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("interval1", 0),
          ("interval2", 1),
          ("interval3", 2),
          ("interval4", 3),
          ("interval5", 4),
          ("interval6", 5),
          ("interval7", 6),
          ("interval8", 7),
          ("interval9", 8),
          ("interval10", 9),
          ("interval11", 10),
          ("interval12", 11),
          ("interval13", 12),
          ("interval14", 13),
          ("interval15", 14),
          ("interval16", 15),
          ("interval17", 16),
          ("interval18", 17),
          ("interval19", 18),
          ("interval20", 19),
          ("interval21", 20),
          ("interval22", 21),
          ("interval23", 22),
          ("interval24", 23),
          ("interval25", 24),
          ("interval26", 25),
          ("interval27", 26),
          ("interval28", 27),
          ("interval29", 28),
          ("interval30", 29),
          ("interval31", 30),
          ("interval32", 31),
          ("interval33", 32),
          ("interval34", 33),
          ("interval35", 34),
          ("interval36", 35),
          ("interval37", 36),
          ("interval38", 37),
          ("interval39", 38),
          ("interval40", 39),
          ("interval41", 40),
          ("interval42", 41),
          ("interval43", 42),
          ("interval44", 43),
          ("interval45", 44),
          ("interval46", 45),
          ("interval47", 46),
          ("interval48", 47),
          ("interval49", 48),
          ("interval50", 49),
          ("interval51", 50),
          ("interval52", 51),
          ("interval53", 52),
          ("interval54", 53),
          ("interval55", 54),
          ("interval56", 55),
          ("interval57", 56),
          ("interval58", 57),
          ("interval59", 58),
          ("interval60", 59),
          ("interval61", 60),
          ("interval62", 61),
          ("interval63", 62),
          ("interval64", 63))
    )


class PktcSigType(TextualConvention, Integer32):
    status = "current"
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
        *(("other", 1),
          ("unknown", 2),
          ("ncs", 3),
          ("dcs", 4))
    )



# MIB Managed Objects in the order of their OIDs

_PktcSigMibObjects_ObjectIdentity = ObjectIdentity
pktcSigMibObjects = _PktcSigMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1)
)
_PktcSigDevConfigObjects_ObjectIdentity = ObjectIdentity
pktcSigDevConfigObjects = _PktcSigDevConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1)
)
_PktcSigDevCodecTable_Object = MibTable
pktcSigDevCodecTable = _PktcSigDevCodecTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pktcSigDevCodecTable.setStatus("current")
_PktcSigDevCodecEntry_Object = MibTableRow
pktcSigDevCodecEntry = _PktcSigDevCodecEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 1, 1)
)
pktcSigDevCodecEntry.setIndexNames(
    (0, "PKTC-SIG-MIB", "pktcSigDevCodecIndex"),
)
if mibBuilder.loadTexts:
    pktcSigDevCodecEntry.setStatus("current")


class _PktcSigDevCodecIndex_Type(Integer32):
    """Custom type pktcSigDevCodecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_PktcSigDevCodecIndex_Type.__name__ = "Integer32"
_PktcSigDevCodecIndex_Object = MibTableColumn
pktcSigDevCodecIndex = _PktcSigDevCodecIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 1, 1, 1),
    _PktcSigDevCodecIndex_Type()
)
pktcSigDevCodecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcSigDevCodecIndex.setStatus("current")
_PktcSigDevCodecType_Type = PktcCodecType
_PktcSigDevCodecType_Object = MibTableColumn
pktcSigDevCodecType = _PktcSigDevCodecType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 1, 1, 2),
    _PktcSigDevCodecType_Type()
)
pktcSigDevCodecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevCodecType.setStatus("current")


class _PktcSigDevCodecMax_Type(Integer32):
    """Custom type pktcSigDevCodecMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_PktcSigDevCodecMax_Type.__name__ = "Integer32"
_PktcSigDevCodecMax_Object = MibTableColumn
pktcSigDevCodecMax = _PktcSigDevCodecMax_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 1, 1, 3),
    _PktcSigDevCodecMax_Type()
)
pktcSigDevCodecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevCodecMax.setStatus("current")
_PktcSigDevEchoCancellation_Type = TruthValue
_PktcSigDevEchoCancellation_Object = MibScalar
pktcSigDevEchoCancellation = _PktcSigDevEchoCancellation_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 2),
    _PktcSigDevEchoCancellation_Type()
)
pktcSigDevEchoCancellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevEchoCancellation.setStatus("current")
_PktcSigDevSilenceSuppression_Type = TruthValue
_PktcSigDevSilenceSuppression_Object = MibScalar
pktcSigDevSilenceSuppression = _PktcSigDevSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 3),
    _PktcSigDevSilenceSuppression_Type()
)
pktcSigDevSilenceSuppression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevSilenceSuppression.setStatus("current")


class _PktcSigDevConnectionMode_Type(Bits):
    """Custom type pktcSigDevConnectionMode based on Bits"""
    namedValues = NamedValues(
        *(("voice", 0),
          ("fax", 1),
          ("modem", 2))
    )

_PktcSigDevConnectionMode_Type.__name__ = "Bits"
_PktcSigDevConnectionMode_Object = MibScalar
pktcSigDevConnectionMode = _PktcSigDevConnectionMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 4),
    _PktcSigDevConnectionMode_Type()
)
pktcSigDevConnectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevConnectionMode.setStatus("current")


class _PktcSigDevR0Cadence_Type(PktcRingCadence):
    """Custom type pktcSigDevR0Cadence based on PktcRingCadence"""
    defaultBinValue = "11111111111111111111"


_PktcSigDevR0Cadence_Type.__name__ = "PktcRingCadence"
_PktcSigDevR0Cadence_Object = MibScalar
pktcSigDevR0Cadence = _PktcSigDevR0Cadence_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 5),
    _PktcSigDevR0Cadence_Type()
)
pktcSigDevR0Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR0Cadence.setStatus("current")


class _PktcSigDevR6Cadence_Type(PktcRingCadence):
    """Custom type pktcSigDevR6Cadence based on PktcRingCadence"""
    defaultBinValue = "11111111111111111111"


_PktcSigDevR6Cadence_Type.__name__ = "PktcRingCadence"
_PktcSigDevR6Cadence_Object = MibScalar
pktcSigDevR6Cadence = _PktcSigDevR6Cadence_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 6),
    _PktcSigDevR6Cadence_Type()
)
pktcSigDevR6Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR6Cadence.setStatus("current")


class _PktcSigDevR7Cadence_Type(PktcRingCadence):
    """Custom type pktcSigDevR7Cadence based on PktcRingCadence"""
    defaultBinValue = "11111111111111111111"


_PktcSigDevR7Cadence_Type.__name__ = "PktcRingCadence"
_PktcSigDevR7Cadence_Object = MibScalar
pktcSigDevR7Cadence = _PktcSigDevR7Cadence_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 7),
    _PktcSigDevR7Cadence_Type()
)
pktcSigDevR7Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR7Cadence.setStatus("current")


class _PktcSigDefCallSigTos_Type(Integer32):
    """Custom type pktcSigDefCallSigTos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PktcSigDefCallSigTos_Type.__name__ = "Integer32"
_PktcSigDefCallSigTos_Object = MibScalar
pktcSigDefCallSigTos = _PktcSigDefCallSigTos_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 8),
    _PktcSigDefCallSigTos_Type()
)
pktcSigDefCallSigTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDefCallSigTos.setStatus("current")


class _PktcSigDefMediaStreamTos_Type(Integer32):
    """Custom type pktcSigDefMediaStreamTos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PktcSigDefMediaStreamTos_Type.__name__ = "Integer32"
_PktcSigDefMediaStreamTos_Object = MibScalar
pktcSigDefMediaStreamTos = _PktcSigDefMediaStreamTos_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 9),
    _PktcSigDefMediaStreamTos_Type()
)
pktcSigDefMediaStreamTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDefMediaStreamTos.setStatus("current")


class _PktcSigTosFormatSelector_Type(Integer32):
    """Custom type pktcSigTosFormatSelector based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4TOSOctet", 1),
          ("dscpCodepoint", 2))
    )


_PktcSigTosFormatSelector_Type.__name__ = "Integer32"
_PktcSigTosFormatSelector_Object = MibScalar
pktcSigTosFormatSelector = _PktcSigTosFormatSelector_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 10),
    _PktcSigTosFormatSelector_Type()
)
pktcSigTosFormatSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigTosFormatSelector.setStatus("current")
_PktcSigCapabilityTable_Object = MibTable
pktcSigCapabilityTable = _PktcSigCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 11)
)
if mibBuilder.loadTexts:
    pktcSigCapabilityTable.setStatus("current")
_PktcSigCapabilityEntry_Object = MibTableRow
pktcSigCapabilityEntry = _PktcSigCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 11, 1)
)
pktcSigCapabilityEntry.setIndexNames(
    (0, "PKTC-SIG-MIB", "pktcSignalingIndex"),
)
if mibBuilder.loadTexts:
    pktcSigCapabilityEntry.setStatus("current")


class _PktcSignalingIndex_Type(Integer32):
    """Custom type pktcSignalingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_PktcSignalingIndex_Type.__name__ = "Integer32"
_PktcSignalingIndex_Object = MibTableColumn
pktcSignalingIndex = _PktcSignalingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 11, 1, 1),
    _PktcSignalingIndex_Type()
)
pktcSignalingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcSignalingIndex.setStatus("current")
_PktcSignalingType_Type = PktcSigType
_PktcSignalingType_Object = MibTableColumn
pktcSignalingType = _PktcSignalingType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 11, 1, 2),
    _PktcSignalingType_Type()
)
pktcSignalingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSignalingType.setStatus("current")
_PktcSignalingVersion_Type = SnmpAdminString
_PktcSignalingVersion_Object = MibTableColumn
pktcSignalingVersion = _PktcSignalingVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 11, 1, 3),
    _PktcSignalingVersion_Type()
)
pktcSignalingVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSignalingVersion.setStatus("current")
_PktcSignalingVendorExtension_Type = SnmpAdminString
_PktcSignalingVendorExtension_Object = MibTableColumn
pktcSignalingVendorExtension = _PktcSignalingVendorExtension_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 11, 1, 4),
    _PktcSignalingVendorExtension_Type()
)
pktcSignalingVendorExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSignalingVendorExtension.setStatus("current")


class _PktcSigDefNcsReceiveUdpPort_Type(Integer32):
    """Custom type pktcSigDefNcsReceiveUdpPort based on Integer32"""
    defaultValue = 2427

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_PktcSigDefNcsReceiveUdpPort_Type.__name__ = "Integer32"
_PktcSigDefNcsReceiveUdpPort_Object = MibScalar
pktcSigDefNcsReceiveUdpPort = _PktcSigDefNcsReceiveUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 12),
    _PktcSigDefNcsReceiveUdpPort_Type()
)
pktcSigDefNcsReceiveUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDefNcsReceiveUdpPort.setStatus("current")


class _PktcSigServiceClassNameUS_Type(SnmpAdminString):
    """Custom type pktcSigServiceClassNameUS based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PktcSigServiceClassNameUS_Type.__name__ = "SnmpAdminString"
_PktcSigServiceClassNameUS_Object = MibScalar
pktcSigServiceClassNameUS = _PktcSigServiceClassNameUS_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 13),
    _PktcSigServiceClassNameUS_Type()
)
pktcSigServiceClassNameUS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigServiceClassNameUS.setStatus("obsolete")


class _PktcSigServiceClassNameDS_Type(SnmpAdminString):
    """Custom type pktcSigServiceClassNameDS based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PktcSigServiceClassNameDS_Type.__name__ = "SnmpAdminString"
_PktcSigServiceClassNameDS_Object = MibScalar
pktcSigServiceClassNameDS = _PktcSigServiceClassNameDS_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 14),
    _PktcSigServiceClassNameDS_Type()
)
pktcSigServiceClassNameDS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigServiceClassNameDS.setStatus("obsolete")


class _PktcSigServiceClassNameMask_Type(Integer32):
    """Custom type pktcSigServiceClassNameMask based on Integer32"""
    defaultValue = 0


_PktcSigServiceClassNameMask_Type.__name__ = "Integer32"
_PktcSigServiceClassNameMask_Object = MibScalar
pktcSigServiceClassNameMask = _PktcSigServiceClassNameMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 15),
    _PktcSigServiceClassNameMask_Type()
)
pktcSigServiceClassNameMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigServiceClassNameMask.setStatus("obsolete")


class _PktcSigNcsServiceFlowState_Type(Integer32):
    """Custom type pktcSigNcsServiceFlowState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notactive", 1),
          ("active", 2),
          ("error", 3))
    )


_PktcSigNcsServiceFlowState_Type.__name__ = "Integer32"
_PktcSigNcsServiceFlowState_Object = MibScalar
pktcSigNcsServiceFlowState = _PktcSigNcsServiceFlowState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 16),
    _PktcSigNcsServiceFlowState_Type()
)
pktcSigNcsServiceFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigNcsServiceFlowState.setStatus("obsolete")


class _PktcSigDevR1Cadence_Type(PktcRingCadence):
    """Custom type pktcSigDevR1Cadence based on PktcRingCadence"""
    defaultBinValue = "11111111111111111111"


_PktcSigDevR1Cadence_Type.__name__ = "PktcRingCadence"
_PktcSigDevR1Cadence_Object = MibScalar
pktcSigDevR1Cadence = _PktcSigDevR1Cadence_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 17),
    _PktcSigDevR1Cadence_Type()
)
pktcSigDevR1Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR1Cadence.setStatus("current")


class _PktcSigDevR2Cadence_Type(PktcRingCadence):
    """Custom type pktcSigDevR2Cadence based on PktcRingCadence"""
    defaultBinValue = "11111111000011111111"


_PktcSigDevR2Cadence_Type.__name__ = "PktcRingCadence"
_PktcSigDevR2Cadence_Object = MibScalar
pktcSigDevR2Cadence = _PktcSigDevR2Cadence_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 18),
    _PktcSigDevR2Cadence_Type()
)
pktcSigDevR2Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR2Cadence.setStatus("current")


class _PktcSigDevR3Cadence_Type(PktcRingCadence):
    """Custom type pktcSigDevR3Cadence based on PktcRingCadence"""
    defaultBinValue = "11110011110011111111"


_PktcSigDevR3Cadence_Type.__name__ = "PktcRingCadence"
_PktcSigDevR3Cadence_Object = MibScalar
pktcSigDevR3Cadence = _PktcSigDevR3Cadence_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 19),
    _PktcSigDevR3Cadence_Type()
)
pktcSigDevR3Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR3Cadence.setStatus("current")


class _PktcSigDevR4Cadence_Type(PktcRingCadence):
    """Custom type pktcSigDevR4Cadence based on PktcRingCadence"""
    defaultBinValue = "11100111111111100111"


_PktcSigDevR4Cadence_Type.__name__ = "PktcRingCadence"
_PktcSigDevR4Cadence_Object = MibScalar
pktcSigDevR4Cadence = _PktcSigDevR4Cadence_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 20),
    _PktcSigDevR4Cadence_Type()
)
pktcSigDevR4Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR4Cadence.setStatus("current")


class _PktcSigDevR5Cadence_Type(PktcRingCadence):
    """Custom type pktcSigDevR5Cadence based on PktcRingCadence"""
    defaultBinValue = "1111100000000000000000000000000000000000000000000000000000001"


_PktcSigDevR5Cadence_Type.__name__ = "PktcRingCadence"
_PktcSigDevR5Cadence_Object = MibScalar
pktcSigDevR5Cadence = _PktcSigDevR5Cadence_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 21),
    _PktcSigDevR5Cadence_Type()
)
pktcSigDevR5Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR5Cadence.setStatus("current")


class _PktcSigDevRgCadence_Type(PktcRingCadence):
    """Custom type pktcSigDevRgCadence based on PktcRingCadence"""
    defaultBinValue = "11111111111111111111"


_PktcSigDevRgCadence_Type.__name__ = "PktcRingCadence"
_PktcSigDevRgCadence_Object = MibScalar
pktcSigDevRgCadence = _PktcSigDevRgCadence_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 22),
    _PktcSigDevRgCadence_Type()
)
pktcSigDevRgCadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevRgCadence.setStatus("current")


class _PktcSigDevRsCadence_Type(PktcRingCadence):
    """Custom type pktcSigDevRsCadence based on PktcRingCadence"""
    defaultBinValue = "1111100000000000000000000000000000000000000000000000000000001"


_PktcSigDevRsCadence_Type.__name__ = "PktcRingCadence"
_PktcSigDevRsCadence_Object = MibScalar
pktcSigDevRsCadence = _PktcSigDevRsCadence_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 23),
    _PktcSigDevRsCadence_Type()
)
pktcSigDevRsCadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevRsCadence.setStatus("current")


class _PktcSigDevRtCadence_Type(PktcRingCadence):
    """Custom type pktcSigDevRtCadence based on PktcRingCadence"""
    defaultBinValue = "11111111111111111111"


_PktcSigDevRtCadence_Type.__name__ = "PktcRingCadence"
_PktcSigDevRtCadence_Object = MibScalar
pktcSigDevRtCadence = _PktcSigDevRtCadence_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 1, 24),
    _PktcSigDevRtCadence_Type()
)
pktcSigDevRtCadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevRtCadence.setStatus("current")
_PktcNcsEndPntConfigObjects_ObjectIdentity = ObjectIdentity
pktcNcsEndPntConfigObjects = _PktcNcsEndPntConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2)
)
_PktcNcsEndPntConfigTable_Object = MibTable
pktcNcsEndPntConfigTable = _PktcNcsEndPntConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigTable.setStatus("current")
_PktcNcsEndPntConfigEntry_Object = MibTableRow
pktcNcsEndPntConfigEntry = _PktcNcsEndPntConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1)
)
pktcNcsEndPntConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigEntry.setStatus("current")


class _PktcNcsEndPntConfigCallAgentId_Type(SnmpAdminString):
    """Custom type pktcNcsEndPntConfigCallAgentId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 255),
    )


_PktcNcsEndPntConfigCallAgentId_Type.__name__ = "SnmpAdminString"
_PktcNcsEndPntConfigCallAgentId_Object = MibTableColumn
pktcNcsEndPntConfigCallAgentId = _PktcNcsEndPntConfigCallAgentId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 1),
    _PktcNcsEndPntConfigCallAgentId_Type()
)
pktcNcsEndPntConfigCallAgentId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigCallAgentId.setStatus("current")


class _PktcNcsEndPntConfigCallAgentUdpPort_Type(Integer32):
    """Custom type pktcNcsEndPntConfigCallAgentUdpPort based on Integer32"""
    defaultValue = 2727

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_PktcNcsEndPntConfigCallAgentUdpPort_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigCallAgentUdpPort_Object = MibTableColumn
pktcNcsEndPntConfigCallAgentUdpPort = _PktcNcsEndPntConfigCallAgentUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 2),
    _PktcNcsEndPntConfigCallAgentUdpPort_Type()
)
pktcNcsEndPntConfigCallAgentUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigCallAgentUdpPort.setStatus("current")


class _PktcNcsEndPntConfigPartialDialTO_Type(Integer32):
    """Custom type pktcNcsEndPntConfigPartialDialTO based on Integer32"""
    defaultValue = 16


_PktcNcsEndPntConfigPartialDialTO_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigPartialDialTO_Object = MibTableColumn
pktcNcsEndPntConfigPartialDialTO = _PktcNcsEndPntConfigPartialDialTO_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 3),
    _PktcNcsEndPntConfigPartialDialTO_Type()
)
pktcNcsEndPntConfigPartialDialTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigPartialDialTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigPartialDialTO.setUnits("seconds")


class _PktcNcsEndPntConfigCriticalDialTO_Type(Integer32):
    """Custom type pktcNcsEndPntConfigCriticalDialTO based on Integer32"""
    defaultValue = 4


_PktcNcsEndPntConfigCriticalDialTO_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigCriticalDialTO_Object = MibTableColumn
pktcNcsEndPntConfigCriticalDialTO = _PktcNcsEndPntConfigCriticalDialTO_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 4),
    _PktcNcsEndPntConfigCriticalDialTO_Type()
)
pktcNcsEndPntConfigCriticalDialTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigCriticalDialTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigCriticalDialTO.setUnits("seconds")


class _PktcNcsEndPntConfigBusyToneTO_Type(Integer32):
    """Custom type pktcNcsEndPntConfigBusyToneTO based on Integer32"""
    defaultValue = 30


_PktcNcsEndPntConfigBusyToneTO_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigBusyToneTO_Object = MibTableColumn
pktcNcsEndPntConfigBusyToneTO = _PktcNcsEndPntConfigBusyToneTO_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 5),
    _PktcNcsEndPntConfigBusyToneTO_Type()
)
pktcNcsEndPntConfigBusyToneTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigBusyToneTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigBusyToneTO.setUnits("seconds")


class _PktcNcsEndPntConfigDialToneTO_Type(Integer32):
    """Custom type pktcNcsEndPntConfigDialToneTO based on Integer32"""
    defaultValue = 16


_PktcNcsEndPntConfigDialToneTO_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigDialToneTO_Object = MibTableColumn
pktcNcsEndPntConfigDialToneTO = _PktcNcsEndPntConfigDialToneTO_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 6),
    _PktcNcsEndPntConfigDialToneTO_Type()
)
pktcNcsEndPntConfigDialToneTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigDialToneTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigDialToneTO.setUnits("seconds")


class _PktcNcsEndPntConfigMessageWaitingTO_Type(Integer32):
    """Custom type pktcNcsEndPntConfigMessageWaitingTO based on Integer32"""
    defaultValue = 16


_PktcNcsEndPntConfigMessageWaitingTO_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigMessageWaitingTO_Object = MibTableColumn
pktcNcsEndPntConfigMessageWaitingTO = _PktcNcsEndPntConfigMessageWaitingTO_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 7),
    _PktcNcsEndPntConfigMessageWaitingTO_Type()
)
pktcNcsEndPntConfigMessageWaitingTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigMessageWaitingTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigMessageWaitingTO.setUnits("seconds")


class _PktcNcsEndPntConfigOffHookWarnToneTO_Type(Integer32):
    """Custom type pktcNcsEndPntConfigOffHookWarnToneTO based on Integer32"""
    defaultValue = 0


_PktcNcsEndPntConfigOffHookWarnToneTO_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigOffHookWarnToneTO_Object = MibTableColumn
pktcNcsEndPntConfigOffHookWarnToneTO = _PktcNcsEndPntConfigOffHookWarnToneTO_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 8),
    _PktcNcsEndPntConfigOffHookWarnToneTO_Type()
)
pktcNcsEndPntConfigOffHookWarnToneTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigOffHookWarnToneTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigOffHookWarnToneTO.setUnits("seconds")


class _PktcNcsEndPntConfigRingingTO_Type(Integer32):
    """Custom type pktcNcsEndPntConfigRingingTO based on Integer32"""
    defaultValue = 180


_PktcNcsEndPntConfigRingingTO_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigRingingTO_Object = MibTableColumn
pktcNcsEndPntConfigRingingTO = _PktcNcsEndPntConfigRingingTO_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 9),
    _PktcNcsEndPntConfigRingingTO_Type()
)
pktcNcsEndPntConfigRingingTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigRingingTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigRingingTO.setUnits("seconds")


class _PktcNcsEndPntConfigRingBackTO_Type(Integer32):
    """Custom type pktcNcsEndPntConfigRingBackTO based on Integer32"""
    defaultValue = 180


_PktcNcsEndPntConfigRingBackTO_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigRingBackTO_Object = MibTableColumn
pktcNcsEndPntConfigRingBackTO = _PktcNcsEndPntConfigRingBackTO_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 10),
    _PktcNcsEndPntConfigRingBackTO_Type()
)
pktcNcsEndPntConfigRingBackTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigRingBackTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigRingBackTO.setUnits("seconds")


class _PktcNcsEndPntConfigReorderToneTO_Type(Integer32):
    """Custom type pktcNcsEndPntConfigReorderToneTO based on Integer32"""
    defaultValue = 30


_PktcNcsEndPntConfigReorderToneTO_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigReorderToneTO_Object = MibTableColumn
pktcNcsEndPntConfigReorderToneTO = _PktcNcsEndPntConfigReorderToneTO_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 11),
    _PktcNcsEndPntConfigReorderToneTO_Type()
)
pktcNcsEndPntConfigReorderToneTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigReorderToneTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigReorderToneTO.setUnits("seconds")


class _PktcNcsEndPntConfigStutterDialToneTO_Type(Integer32):
    """Custom type pktcNcsEndPntConfigStutterDialToneTO based on Integer32"""
    defaultValue = 16


_PktcNcsEndPntConfigStutterDialToneTO_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigStutterDialToneTO_Object = MibTableColumn
pktcNcsEndPntConfigStutterDialToneTO = _PktcNcsEndPntConfigStutterDialToneTO_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 12),
    _PktcNcsEndPntConfigStutterDialToneTO_Type()
)
pktcNcsEndPntConfigStutterDialToneTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigStutterDialToneTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigStutterDialToneTO.setUnits("seconds")


class _PktcNcsEndPntConfigTSMax_Type(Integer32):
    """Custom type pktcNcsEndPntConfigTSMax based on Integer32"""
    defaultValue = 20


_PktcNcsEndPntConfigTSMax_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigTSMax_Object = MibTableColumn
pktcNcsEndPntConfigTSMax = _PktcNcsEndPntConfigTSMax_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 13),
    _PktcNcsEndPntConfigTSMax_Type()
)
pktcNcsEndPntConfigTSMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigTSMax.setStatus("current")


class _PktcNcsEndPntConfigMax1_Type(Integer32):
    """Custom type pktcNcsEndPntConfigMax1 based on Integer32"""
    defaultValue = 5


_PktcNcsEndPntConfigMax1_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigMax1_Object = MibTableColumn
pktcNcsEndPntConfigMax1 = _PktcNcsEndPntConfigMax1_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 14),
    _PktcNcsEndPntConfigMax1_Type()
)
pktcNcsEndPntConfigMax1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigMax1.setStatus("current")


class _PktcNcsEndPntConfigMax2_Type(Integer32):
    """Custom type pktcNcsEndPntConfigMax2 based on Integer32"""
    defaultValue = 7


_PktcNcsEndPntConfigMax2_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigMax2_Object = MibTableColumn
pktcNcsEndPntConfigMax2 = _PktcNcsEndPntConfigMax2_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 15),
    _PktcNcsEndPntConfigMax2_Type()
)
pktcNcsEndPntConfigMax2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigMax2.setStatus("current")


class _PktcNcsEndPntConfigMax1QEnable_Type(TruthValue):
    """Custom type pktcNcsEndPntConfigMax1QEnable based on TruthValue"""
    defaultValue = 1


_PktcNcsEndPntConfigMax1QEnable_Type.__name__ = "TruthValue"
_PktcNcsEndPntConfigMax1QEnable_Object = MibTableColumn
pktcNcsEndPntConfigMax1QEnable = _PktcNcsEndPntConfigMax1QEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 16),
    _PktcNcsEndPntConfigMax1QEnable_Type()
)
pktcNcsEndPntConfigMax1QEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigMax1QEnable.setStatus("current")


class _PktcNcsEndPntConfigMax2QEnable_Type(TruthValue):
    """Custom type pktcNcsEndPntConfigMax2QEnable based on TruthValue"""
    defaultValue = 1


_PktcNcsEndPntConfigMax2QEnable_Type.__name__ = "TruthValue"
_PktcNcsEndPntConfigMax2QEnable_Object = MibTableColumn
pktcNcsEndPntConfigMax2QEnable = _PktcNcsEndPntConfigMax2QEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 17),
    _PktcNcsEndPntConfigMax2QEnable_Type()
)
pktcNcsEndPntConfigMax2QEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigMax2QEnable.setStatus("current")


class _PktcNcsEndPntConfigMWD_Type(Integer32):
    """Custom type pktcNcsEndPntConfigMWD based on Integer32"""
    defaultValue = 600


_PktcNcsEndPntConfigMWD_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigMWD_Object = MibTableColumn
pktcNcsEndPntConfigMWD = _PktcNcsEndPntConfigMWD_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 18),
    _PktcNcsEndPntConfigMWD_Type()
)
pktcNcsEndPntConfigMWD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigMWD.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigMWD.setUnits("seconds")


class _PktcNcsEndPntConfigTdinit_Type(Integer32):
    """Custom type pktcNcsEndPntConfigTdinit based on Integer32"""
    defaultValue = 15


_PktcNcsEndPntConfigTdinit_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigTdinit_Object = MibTableColumn
pktcNcsEndPntConfigTdinit = _PktcNcsEndPntConfigTdinit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 19),
    _PktcNcsEndPntConfigTdinit_Type()
)
pktcNcsEndPntConfigTdinit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigTdinit.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigTdinit.setUnits("seconds")


class _PktcNcsEndPntConfigTdmin_Type(Integer32):
    """Custom type pktcNcsEndPntConfigTdmin based on Integer32"""
    defaultValue = 15


_PktcNcsEndPntConfigTdmin_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigTdmin_Object = MibTableColumn
pktcNcsEndPntConfigTdmin = _PktcNcsEndPntConfigTdmin_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 20),
    _PktcNcsEndPntConfigTdmin_Type()
)
pktcNcsEndPntConfigTdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigTdmin.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigTdmin.setUnits("seconds")


class _PktcNcsEndPntConfigTdmax_Type(Integer32):
    """Custom type pktcNcsEndPntConfigTdmax based on Integer32"""
    defaultValue = 600


_PktcNcsEndPntConfigTdmax_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigTdmax_Object = MibTableColumn
pktcNcsEndPntConfigTdmax = _PktcNcsEndPntConfigTdmax_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 21),
    _PktcNcsEndPntConfigTdmax_Type()
)
pktcNcsEndPntConfigTdmax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigTdmax.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigTdmax.setUnits("seconds")


class _PktcNcsEndPntConfigRtoMax_Type(Integer32):
    """Custom type pktcNcsEndPntConfigRtoMax based on Integer32"""
    defaultValue = 4


_PktcNcsEndPntConfigRtoMax_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigRtoMax_Object = MibTableColumn
pktcNcsEndPntConfigRtoMax = _PktcNcsEndPntConfigRtoMax_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 22),
    _PktcNcsEndPntConfigRtoMax_Type()
)
pktcNcsEndPntConfigRtoMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigRtoMax.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigRtoMax.setUnits("seconds")


class _PktcNcsEndPntConfigRtoInit_Type(Integer32):
    """Custom type pktcNcsEndPntConfigRtoInit based on Integer32"""
    defaultValue = 200


_PktcNcsEndPntConfigRtoInit_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigRtoInit_Object = MibTableColumn
pktcNcsEndPntConfigRtoInit = _PktcNcsEndPntConfigRtoInit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 23),
    _PktcNcsEndPntConfigRtoInit_Type()
)
pktcNcsEndPntConfigRtoInit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigRtoInit.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigRtoInit.setUnits("milliseconds")


class _PktcNcsEndPntConfigLongDurationKeepAlive_Type(Integer32):
    """Custom type pktcNcsEndPntConfigLongDurationKeepAlive based on Integer32"""
    defaultValue = 60


_PktcNcsEndPntConfigLongDurationKeepAlive_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigLongDurationKeepAlive_Object = MibTableColumn
pktcNcsEndPntConfigLongDurationKeepAlive = _PktcNcsEndPntConfigLongDurationKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 24),
    _PktcNcsEndPntConfigLongDurationKeepAlive_Type()
)
pktcNcsEndPntConfigLongDurationKeepAlive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigLongDurationKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigLongDurationKeepAlive.setUnits("minutes")


class _PktcNcsEndPntConfigThist_Type(Integer32):
    """Custom type pktcNcsEndPntConfigThist based on Integer32"""
    defaultValue = 30


_PktcNcsEndPntConfigThist_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigThist_Object = MibTableColumn
pktcNcsEndPntConfigThist = _PktcNcsEndPntConfigThist_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 25),
    _PktcNcsEndPntConfigThist_Type()
)
pktcNcsEndPntConfigThist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigThist.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigThist.setUnits("seconds")
_PktcNcsEndPntConfigStatus_Type = RowStatus
_PktcNcsEndPntConfigStatus_Object = MibTableColumn
pktcNcsEndPntConfigStatus = _PktcNcsEndPntConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 26),
    _PktcNcsEndPntConfigStatus_Type()
)
pktcNcsEndPntConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigStatus.setStatus("current")


class _PktcNcsEndPntConfigCallWaitingMaxRep_Type(Integer32):
    """Custom type pktcNcsEndPntConfigCallWaitingMaxRep based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PktcNcsEndPntConfigCallWaitingMaxRep_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigCallWaitingMaxRep_Object = MibTableColumn
pktcNcsEndPntConfigCallWaitingMaxRep = _PktcNcsEndPntConfigCallWaitingMaxRep_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 27),
    _PktcNcsEndPntConfigCallWaitingMaxRep_Type()
)
pktcNcsEndPntConfigCallWaitingMaxRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigCallWaitingMaxRep.setStatus("current")


class _PktcNcsEndPntConfigCallWaitingDelay_Type(Integer32):
    """Custom type pktcNcsEndPntConfigCallWaitingDelay based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PktcNcsEndPntConfigCallWaitingDelay_Type.__name__ = "Integer32"
_PktcNcsEndPntConfigCallWaitingDelay_Object = MibTableColumn
pktcNcsEndPntConfigCallWaitingDelay = _PktcNcsEndPntConfigCallWaitingDelay_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 28),
    _PktcNcsEndPntConfigCallWaitingDelay_Type()
)
pktcNcsEndPntConfigCallWaitingDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigCallWaitingDelay.setStatus("current")
if mibBuilder.loadTexts:
    pktcNcsEndPntConfigCallWaitingDelay.setUnits("seconds")
_PktcNcsEndPntStatusCallIpAddress_Type = IpAddress
_PktcNcsEndPntStatusCallIpAddress_Object = MibTableColumn
pktcNcsEndPntStatusCallIpAddress = _PktcNcsEndPntStatusCallIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 29),
    _PktcNcsEndPntStatusCallIpAddress_Type()
)
pktcNcsEndPntStatusCallIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcNcsEndPntStatusCallIpAddress.setStatus("current")


class _PktcNcsEndPntStatusError_Type(Integer32):
    """Custom type pktcNcsEndPntStatusError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("noSecurityAssociation", 2),
          ("disconnected", 3))
    )


_PktcNcsEndPntStatusError_Type.__name__ = "Integer32"
_PktcNcsEndPntStatusError_Object = MibTableColumn
pktcNcsEndPntStatusError = _PktcNcsEndPntStatusError_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 2, 1, 1, 30),
    _PktcNcsEndPntStatusError_Type()
)
pktcNcsEndPntStatusError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcNcsEndPntStatusError.setStatus("current")
_PktcSigEndPntConfigObjects_ObjectIdentity = ObjectIdentity
pktcSigEndPntConfigObjects = _PktcSigEndPntConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 3)
)
_PktcSigEndPntConfigTable_Object = MibTable
pktcSigEndPntConfigTable = _PktcSigEndPntConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pktcSigEndPntConfigTable.setStatus("current")
_PktcSigEndPntConfigEntry_Object = MibTableRow
pktcSigEndPntConfigEntry = _PktcSigEndPntConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 3, 1, 1)
)
pktcSigEndPntConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktcSigEndPntConfigEntry.setStatus("current")


class _PktcSigEndPntCapabilityIndex_Type(Integer32):
    """Custom type pktcSigEndPntCapabilityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_PktcSigEndPntCapabilityIndex_Type.__name__ = "Integer32"
_PktcSigEndPntCapabilityIndex_Object = MibTableColumn
pktcSigEndPntCapabilityIndex = _PktcSigEndPntCapabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 3, 1, 1, 1),
    _PktcSigEndPntCapabilityIndex_Type()
)
pktcSigEndPntCapabilityIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntCapabilityIndex.setStatus("current")
_PktcDcsEndPntConfigObjects_ObjectIdentity = ObjectIdentity
pktcDcsEndPntConfigObjects = _PktcDcsEndPntConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 1, 4)
)
_PktcSigNotificationPrefix_ObjectIdentity = ObjectIdentity
pktcSigNotificationPrefix = _PktcSigNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 2)
)
_PktcSigNotification_ObjectIdentity = ObjectIdentity
pktcSigNotification = _PktcSigNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 2, 0)
)
_PktcSigConformance_ObjectIdentity = ObjectIdentity
pktcSigConformance = _PktcSigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 3)
)
_PktcSigCompliances_ObjectIdentity = ObjectIdentity
pktcSigCompliances = _PktcSigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 3, 1)
)
_PktcSigGroups_ObjectIdentity = ObjectIdentity
pktcSigGroups = _PktcSigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 3, 2)
)

# Managed Objects groups

pktcSigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 3, 2, 1)
)
pktcSigGroup.setObjects(
      *(("PKTC-SIG-MIB", "pktcSigDevCodecType"),
        ("PKTC-SIG-MIB", "pktcSigDevCodecMax"),
        ("PKTC-SIG-MIB", "pktcSigDevEchoCancellation"),
        ("PKTC-SIG-MIB", "pktcSigDevSilenceSuppression"),
        ("PKTC-SIG-MIB", "pktcSigDevConnectionMode"),
        ("PKTC-SIG-MIB", "pktcSigDevR0Cadence"),
        ("PKTC-SIG-MIB", "pktcSigDevR6Cadence"),
        ("PKTC-SIG-MIB", "pktcSigDevR7Cadence"),
        ("PKTC-SIG-MIB", "pktcSigDefCallSigTos"),
        ("PKTC-SIG-MIB", "pktcSigDefMediaStreamTos"),
        ("PKTC-SIG-MIB", "pktcSigTosFormatSelector"),
        ("PKTC-SIG-MIB", "pktcSignalingType"),
        ("PKTC-SIG-MIB", "pktcSignalingVersion"),
        ("PKTC-SIG-MIB", "pktcSignalingVendorExtension"),
        ("PKTC-SIG-MIB", "pktcSigEndPntCapabilityIndex"),
        ("PKTC-SIG-MIB", "pktcSigDefNcsReceiveUdpPort"),
        ("PKTC-SIG-MIB", "pktcSigDevR1Cadence"),
        ("PKTC-SIG-MIB", "pktcSigDevR2Cadence"),
        ("PKTC-SIG-MIB", "pktcSigDevR3Cadence"),
        ("PKTC-SIG-MIB", "pktcSigDevR4Cadence"),
        ("PKTC-SIG-MIB", "pktcSigDevR5Cadence"),
        ("PKTC-SIG-MIB", "pktcSigDevRgCadence"),
        ("PKTC-SIG-MIB", "pktcSigDevRsCadence"),
        ("PKTC-SIG-MIB", "pktcSigDevRtCadence"))
)
if mibBuilder.loadTexts:
    pktcSigGroup.setStatus("current")

pktcNcsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 3, 2, 2)
)
pktcNcsGroup.setObjects(
      *(("PKTC-SIG-MIB", "pktcNcsEndPntConfigCallAgentId"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigCallAgentUdpPort"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigPartialDialTO"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigCriticalDialTO"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigBusyToneTO"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigDialToneTO"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigMessageWaitingTO"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigOffHookWarnToneTO"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigRingingTO"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigRingBackTO"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigReorderToneTO"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigStutterDialToneTO"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigTSMax"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigMax1"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigMax2"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigMax1QEnable"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigMax2QEnable"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigMWD"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigTdinit"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigTdmin"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigTdmax"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigRtoMax"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigRtoInit"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigLongDurationKeepAlive"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigThist"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigStatus"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigCallWaitingMaxRep"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntConfigCallWaitingDelay"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntStatusCallIpAddress"),
        ("PKTC-SIG-MIB", "pktcNcsEndPntStatusError"))
)
if mibBuilder.loadTexts:
    pktcNcsGroup.setStatus("current")

pktcSigObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 3, 2, 3)
)
pktcSigObsoleteGroup.setObjects(
      *(("PKTC-SIG-MIB", "pktcSigServiceClassNameUS"),
        ("PKTC-SIG-MIB", "pktcSigServiceClassNameDS"),
        ("PKTC-SIG-MIB", "pktcSigServiceClassNameMask"),
        ("PKTC-SIG-MIB", "pktcSigNcsServiceFlowState"))
)
if mibBuilder.loadTexts:
    pktcSigObsoleteGroup.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcSigBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 2, 3, 1, 1)
)
pktcSigBasicCompliance.setObjects(
      *(("PKTC-SIG-MIB", "pktcSigGroup"),
        ("PKTC-SIG-MIB", "pktcNcsGroup"))
)
if mibBuilder.loadTexts:
    pktcSigBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PKTC-SIG-MIB",
    **{"PktcCodecType": PktcCodecType,
       "PktcRingCadence": PktcRingCadence,
       "PktcSigType": PktcSigType,
       "pktcSigMib": pktcSigMib,
       "pktcSigMibObjects": pktcSigMibObjects,
       "pktcSigDevConfigObjects": pktcSigDevConfigObjects,
       "pktcSigDevCodecTable": pktcSigDevCodecTable,
       "pktcSigDevCodecEntry": pktcSigDevCodecEntry,
       "pktcSigDevCodecIndex": pktcSigDevCodecIndex,
       "pktcSigDevCodecType": pktcSigDevCodecType,
       "pktcSigDevCodecMax": pktcSigDevCodecMax,
       "pktcSigDevEchoCancellation": pktcSigDevEchoCancellation,
       "pktcSigDevSilenceSuppression": pktcSigDevSilenceSuppression,
       "pktcSigDevConnectionMode": pktcSigDevConnectionMode,
       "pktcSigDevR0Cadence": pktcSigDevR0Cadence,
       "pktcSigDevR6Cadence": pktcSigDevR6Cadence,
       "pktcSigDevR7Cadence": pktcSigDevR7Cadence,
       "pktcSigDefCallSigTos": pktcSigDefCallSigTos,
       "pktcSigDefMediaStreamTos": pktcSigDefMediaStreamTos,
       "pktcSigTosFormatSelector": pktcSigTosFormatSelector,
       "pktcSigCapabilityTable": pktcSigCapabilityTable,
       "pktcSigCapabilityEntry": pktcSigCapabilityEntry,
       "pktcSignalingIndex": pktcSignalingIndex,
       "pktcSignalingType": pktcSignalingType,
       "pktcSignalingVersion": pktcSignalingVersion,
       "pktcSignalingVendorExtension": pktcSignalingVendorExtension,
       "pktcSigDefNcsReceiveUdpPort": pktcSigDefNcsReceiveUdpPort,
       "pktcSigServiceClassNameUS": pktcSigServiceClassNameUS,
       "pktcSigServiceClassNameDS": pktcSigServiceClassNameDS,
       "pktcSigServiceClassNameMask": pktcSigServiceClassNameMask,
       "pktcSigNcsServiceFlowState": pktcSigNcsServiceFlowState,
       "pktcSigDevR1Cadence": pktcSigDevR1Cadence,
       "pktcSigDevR2Cadence": pktcSigDevR2Cadence,
       "pktcSigDevR3Cadence": pktcSigDevR3Cadence,
       "pktcSigDevR4Cadence": pktcSigDevR4Cadence,
       "pktcSigDevR5Cadence": pktcSigDevR5Cadence,
       "pktcSigDevRgCadence": pktcSigDevRgCadence,
       "pktcSigDevRsCadence": pktcSigDevRsCadence,
       "pktcSigDevRtCadence": pktcSigDevRtCadence,
       "pktcNcsEndPntConfigObjects": pktcNcsEndPntConfigObjects,
       "pktcNcsEndPntConfigTable": pktcNcsEndPntConfigTable,
       "pktcNcsEndPntConfigEntry": pktcNcsEndPntConfigEntry,
       "pktcNcsEndPntConfigCallAgentId": pktcNcsEndPntConfigCallAgentId,
       "pktcNcsEndPntConfigCallAgentUdpPort": pktcNcsEndPntConfigCallAgentUdpPort,
       "pktcNcsEndPntConfigPartialDialTO": pktcNcsEndPntConfigPartialDialTO,
       "pktcNcsEndPntConfigCriticalDialTO": pktcNcsEndPntConfigCriticalDialTO,
       "pktcNcsEndPntConfigBusyToneTO": pktcNcsEndPntConfigBusyToneTO,
       "pktcNcsEndPntConfigDialToneTO": pktcNcsEndPntConfigDialToneTO,
       "pktcNcsEndPntConfigMessageWaitingTO": pktcNcsEndPntConfigMessageWaitingTO,
       "pktcNcsEndPntConfigOffHookWarnToneTO": pktcNcsEndPntConfigOffHookWarnToneTO,
       "pktcNcsEndPntConfigRingingTO": pktcNcsEndPntConfigRingingTO,
       "pktcNcsEndPntConfigRingBackTO": pktcNcsEndPntConfigRingBackTO,
       "pktcNcsEndPntConfigReorderToneTO": pktcNcsEndPntConfigReorderToneTO,
       "pktcNcsEndPntConfigStutterDialToneTO": pktcNcsEndPntConfigStutterDialToneTO,
       "pktcNcsEndPntConfigTSMax": pktcNcsEndPntConfigTSMax,
       "pktcNcsEndPntConfigMax1": pktcNcsEndPntConfigMax1,
       "pktcNcsEndPntConfigMax2": pktcNcsEndPntConfigMax2,
       "pktcNcsEndPntConfigMax1QEnable": pktcNcsEndPntConfigMax1QEnable,
       "pktcNcsEndPntConfigMax2QEnable": pktcNcsEndPntConfigMax2QEnable,
       "pktcNcsEndPntConfigMWD": pktcNcsEndPntConfigMWD,
       "pktcNcsEndPntConfigTdinit": pktcNcsEndPntConfigTdinit,
       "pktcNcsEndPntConfigTdmin": pktcNcsEndPntConfigTdmin,
       "pktcNcsEndPntConfigTdmax": pktcNcsEndPntConfigTdmax,
       "pktcNcsEndPntConfigRtoMax": pktcNcsEndPntConfigRtoMax,
       "pktcNcsEndPntConfigRtoInit": pktcNcsEndPntConfigRtoInit,
       "pktcNcsEndPntConfigLongDurationKeepAlive": pktcNcsEndPntConfigLongDurationKeepAlive,
       "pktcNcsEndPntConfigThist": pktcNcsEndPntConfigThist,
       "pktcNcsEndPntConfigStatus": pktcNcsEndPntConfigStatus,
       "pktcNcsEndPntConfigCallWaitingMaxRep": pktcNcsEndPntConfigCallWaitingMaxRep,
       "pktcNcsEndPntConfigCallWaitingDelay": pktcNcsEndPntConfigCallWaitingDelay,
       "pktcNcsEndPntStatusCallIpAddress": pktcNcsEndPntStatusCallIpAddress,
       "pktcNcsEndPntStatusError": pktcNcsEndPntStatusError,
       "pktcSigEndPntConfigObjects": pktcSigEndPntConfigObjects,
       "pktcSigEndPntConfigTable": pktcSigEndPntConfigTable,
       "pktcSigEndPntConfigEntry": pktcSigEndPntConfigEntry,
       "pktcSigEndPntCapabilityIndex": pktcSigEndPntCapabilityIndex,
       "pktcDcsEndPntConfigObjects": pktcDcsEndPntConfigObjects,
       "pktcSigNotificationPrefix": pktcSigNotificationPrefix,
       "pktcSigNotification": pktcSigNotification,
       "pktcSigConformance": pktcSigConformance,
       "pktcSigCompliances": pktcSigCompliances,
       "pktcSigBasicCompliance": pktcSigBasicCompliance,
       "pktcSigGroups": pktcSigGroups,
       "pktcSigGroup": pktcSigGroup,
       "pktcNcsGroup": pktcNcsGroup,
       "pktcSigObsoleteGroup": pktcSigObsoleteGroup}
)

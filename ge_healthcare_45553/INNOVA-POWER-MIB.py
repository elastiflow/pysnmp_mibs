# SNMP MIB module (INNOVA-POWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ge_healthcare_45553/INNOVA-POWER-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:03:41 2025
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gehc_eng_ObjectIdentity = ObjectIdentity
gehc_eng = _Gehc_eng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45553)
)
_PduSnmpAgent_ObjectIdentity = ObjectIdentity
pduSnmpAgent = _PduSnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45553, 1)
)
_PduSnmpAgentName_Type = DisplayString
_PduSnmpAgentName_Object = MibScalar
pduSnmpAgentName = _PduSnmpAgentName_Object(
    (1, 3, 6, 1, 4, 1, 45553, 1, 1),
    _PduSnmpAgentName_Type()
)
pduSnmpAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduSnmpAgentName.setStatus("mandatory")
_PduSnmpAgentVersion_Type = DisplayString
_PduSnmpAgentVersion_Object = MibScalar
pduSnmpAgentVersion = _PduSnmpAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 45553, 1, 2),
    _PduSnmpAgentVersion_Type()
)
pduSnmpAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduSnmpAgentVersion.setStatus("mandatory")
_PduSnmpAgentDate_Type = DisplayString
_PduSnmpAgentDate_Object = MibScalar
pduSnmpAgentDate = _PduSnmpAgentDate_Object(
    (1, 3, 6, 1, 4, 1, 45553, 1, 3),
    _PduSnmpAgentDate_Type()
)
pduSnmpAgentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduSnmpAgentDate.setStatus("mandatory")
_PduTrapReceiver_ObjectIdentity = ObjectIdentity
pduTrapReceiver = _PduTrapReceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45553, 2)
)
_TrapTable_Object = MibTable
trapTable = _TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 45553, 2, 1)
)
if mibBuilder.loadTexts:
    trapTable.setStatus("mandatory")
_TrapEntry_Object = MibTableRow
trapEntry = _TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 45553, 2, 1, 1)
)
trapEntry.setIndexNames(
    (0, "INNOVA-POWER-MIB", "trapReceiverNumber"),
)
if mibBuilder.loadTexts:
    trapEntry.setStatus("mandatory")


class _TrapReceiverNumber_Type(Integer32):
    """Custom type trapReceiverNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_TrapReceiverNumber_Type.__name__ = "Integer32"
_TrapReceiverNumber_Object = MibTableColumn
trapReceiverNumber = _TrapReceiverNumber_Object(
    (1, 3, 6, 1, 4, 1, 45553, 2, 1, 1, 1),
    _TrapReceiverNumber_Type()
)
trapReceiverNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapReceiverNumber.setStatus("mandatory")


class _TrapEnabled_Type(Integer32):
    """Custom type trapEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TrapEnabled_Type.__name__ = "Integer32"
_TrapEnabled_Object = MibTableColumn
trapEnabled = _TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45553, 2, 1, 1, 2),
    _TrapEnabled_Type()
)
trapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapEnabled.setStatus("mandatory")
_TrapReceiverIPAddress_Type = IpAddress
_TrapReceiverIPAddress_Object = MibTableColumn
trapReceiverIPAddress = _TrapReceiverIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 45553, 2, 1, 1, 3),
    _TrapReceiverIPAddress_Type()
)
trapReceiverIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReceiverIPAddress.setStatus("mandatory")


class _TrapCommunity_Type(DisplayString):
    """Custom type trapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_TrapCommunity_Type.__name__ = "DisplayString"
_TrapCommunity_Object = MibTableColumn
trapCommunity = _TrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 45553, 2, 1, 1, 4),
    _TrapCommunity_Type()
)
trapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCommunity.setStatus("mandatory")
_PduId_ObjectIdentity = ObjectIdentity
pduId = _PduId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45553, 3)
)
_PduUniqueId_Type = DisplayString
_PduUniqueId_Object = MibScalar
pduUniqueId = _PduUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 45553, 3, 1),
    _PduUniqueId_Type()
)
pduUniqueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUniqueId.setStatus("mandatory")
_PduFirmwareRevision_Type = DisplayString
_PduFirmwareRevision_Object = MibScalar
pduFirmwareRevision = _PduFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 45553, 3, 2),
    _PduFirmwareRevision_Type()
)
pduFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduFirmwareRevision.setStatus("mandatory")
_PduControl_ObjectIdentity = ObjectIdentity
pduControl = _PduControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45553, 4)
)


class _PduControlOffDelayed_Type(Integer32):
    """Custom type pduControlOffDelayed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("noDelayedOffRequested", 0)
    )


_PduControlOffDelayed_Type.__name__ = "Integer32"
_PduControlOffDelayed_Object = MibScalar
pduControlOffDelayed = _PduControlOffDelayed_Object(
    (1, 3, 6, 1, 4, 1, 45553, 4, 1),
    _PduControlOffDelayed_Type()
)
pduControlOffDelayed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduControlOffDelayed.setStatus("mandatory")


class _PduControlGeneratorPowerSupply_Type(Integer32):
    """Custom type pduControlGeneratorPowerSupply based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mains", 1),
          ("ups", 2))
    )


_PduControlGeneratorPowerSupply_Type.__name__ = "Integer32"
_PduControlGeneratorPowerSupply_Object = MibScalar
pduControlGeneratorPowerSupply = _PduControlGeneratorPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 45553, 4, 2),
    _PduControlGeneratorPowerSupply_Type()
)
pduControlGeneratorPowerSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduControlGeneratorPowerSupply.setStatus("mandatory")


class _PduControlChillerAndTubePumpPowerSupply_Type(Integer32):
    """Custom type pduControlChillerAndTubePumpPowerSupply based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_PduControlChillerAndTubePumpPowerSupply_Type.__name__ = "Integer32"
_PduControlChillerAndTubePumpPowerSupply_Object = MibScalar
pduControlChillerAndTubePumpPowerSupply = _PduControlChillerAndTubePumpPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 45553, 4, 3),
    _PduControlChillerAndTubePumpPowerSupply_Type()
)
pduControlChillerAndTubePumpPowerSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduControlChillerAndTubePumpPowerSupply.setStatus("mandatory")


class _PduControlOutput1_Type(Integer32):
    """Custom type pduControlOutput1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opened", 1),
          ("closed", 2))
    )


_PduControlOutput1_Type.__name__ = "Integer32"
_PduControlOutput1_Object = MibScalar
pduControlOutput1 = _PduControlOutput1_Object(
    (1, 3, 6, 1, 4, 1, 45553, 4, 4),
    _PduControlOutput1_Type()
)
pduControlOutput1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduControlOutput1.setStatus("mandatory")


class _PduControlOutput2_Type(Integer32):
    """Custom type pduControlOutput2 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opened", 1),
          ("closed", 2))
    )


_PduControlOutput2_Type.__name__ = "Integer32"
_PduControlOutput2_Object = MibScalar
pduControlOutput2 = _PduControlOutput2_Object(
    (1, 3, 6, 1, 4, 1, 45553, 4, 5),
    _PduControlOutput2_Type()
)
pduControlOutput2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduControlOutput2.setStatus("mandatory")


class _PduControlXrayLight_Type(Integer32):
    """Custom type pduControlXrayLight based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("copyHardwareInput", 3))
    )


_PduControlXrayLight_Type.__name__ = "Integer32"
_PduControlXrayLight_Object = MibScalar
pduControlXrayLight = _PduControlXrayLight_Object(
    (1, 3, 6, 1, 4, 1, 45553, 4, 6),
    _PduControlXrayLight_Type()
)
pduControlXrayLight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduControlXrayLight.setStatus("mandatory")


class _PduControlRoomLight_Type(Integer32):
    """Custom type pduControlRoomLight based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("copyHardwareInput", 3))
    )


_PduControlRoomLight_Type.__name__ = "Integer32"
_PduControlRoomLight_Object = MibScalar
pduControlRoomLight = _PduControlRoomLight_Object(
    (1, 3, 6, 1, 4, 1, 45553, 4, 7),
    _PduControlRoomLight_Type()
)
pduControlRoomLight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduControlRoomLight.setStatus("mandatory")
_PduStatus_ObjectIdentity = ObjectIdentity
pduStatus = _PduStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45553, 5)
)


class _PduStatusOffCountDown_Type(Integer32):
    """Custom type pduStatusOffCountDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("noCountDownPerformedNoDelayedOffRequested", 0)
    )


_PduStatusOffCountDown_Type.__name__ = "Integer32"
_PduStatusOffCountDown_Object = MibScalar
pduStatusOffCountDown = _PduStatusOffCountDown_Object(
    (1, 3, 6, 1, 4, 1, 45553, 5, 1),
    _PduStatusOffCountDown_Type()
)
pduStatusOffCountDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatusOffCountDown.setStatus("mandatory")


class _PduStatusGeneratorPowerSupply_Type(Integer32):
    """Custom type pduStatusGeneratorPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mains", 1),
          ("ups", 2))
    )


_PduStatusGeneratorPowerSupply_Type.__name__ = "Integer32"
_PduStatusGeneratorPowerSupply_Object = MibScalar
pduStatusGeneratorPowerSupply = _PduStatusGeneratorPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 45553, 5, 2),
    _PduStatusGeneratorPowerSupply_Type()
)
pduStatusGeneratorPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatusGeneratorPowerSupply.setStatus("mandatory")


class _PduStatusInput1_Type(Integer32):
    """Custom type pduStatusInput1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opened", 1),
          ("closed", 2))
    )


_PduStatusInput1_Type.__name__ = "Integer32"
_PduStatusInput1_Object = MibScalar
pduStatusInput1 = _PduStatusInput1_Object(
    (1, 3, 6, 1, 4, 1, 45553, 5, 3),
    _PduStatusInput1_Type()
)
pduStatusInput1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatusInput1.setStatus("mandatory")


class _PduStatusInput2_Type(Integer32):
    """Custom type pduStatusInput2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opened", 1),
          ("closed", 2))
    )


_PduStatusInput2_Type.__name__ = "Integer32"
_PduStatusInput2_Object = MibScalar
pduStatusInput2 = _PduStatusInput2_Object(
    (1, 3, 6, 1, 4, 1, 45553, 5, 4),
    _PduStatusInput2_Type()
)
pduStatusInput2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatusInput2.setStatus("mandatory")
_PduStatusInternal24V1_Type = Integer32
_PduStatusInternal24V1_Object = MibScalar
pduStatusInternal24V1 = _PduStatusInternal24V1_Object(
    (1, 3, 6, 1, 4, 1, 45553, 5, 5),
    _PduStatusInternal24V1_Type()
)
pduStatusInternal24V1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatusInternal24V1.setStatus("mandatory")
_PduStatusInternal24V2_Type = Integer32
_PduStatusInternal24V2_Object = MibScalar
pduStatusInternal24V2 = _PduStatusInternal24V2_Object(
    (1, 3, 6, 1, 4, 1, 45553, 5, 6),
    _PduStatusInternal24V2_Type()
)
pduStatusInternal24V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatusInternal24V2.setStatus("mandatory")
_PduStatusIntTemp_Type = Integer32
_PduStatusIntTemp_Object = MibScalar
pduStatusIntTemp = _PduStatusIntTemp_Object(
    (1, 3, 6, 1, 4, 1, 45553, 5, 7),
    _PduStatusIntTemp_Type()
)
pduStatusIntTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatusIntTemp.setStatus("mandatory")
_PduStatusExtTemp1_Type = Integer32
_PduStatusExtTemp1_Object = MibScalar
pduStatusExtTemp1 = _PduStatusExtTemp1_Object(
    (1, 3, 6, 1, 4, 1, 45553, 5, 8),
    _PduStatusExtTemp1_Type()
)
pduStatusExtTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatusExtTemp1.setStatus("mandatory")
_PduStatusExtTemp2_Type = Integer32
_PduStatusExtTemp2_Object = MibScalar
pduStatusExtTemp2 = _PduStatusExtTemp2_Object(
    (1, 3, 6, 1, 4, 1, 45553, 5, 9),
    _PduStatusExtTemp2_Type()
)
pduStatusExtTemp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatusExtTemp2.setStatus("mandatory")


class _PduStatusOffRequest_Type(Integer32):
    """Custom type pduStatusOffRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noShutDownRequestedForSystem", 1),
          ("shutDownRequested", 2))
    )


_PduStatusOffRequest_Type.__name__ = "Integer32"
_PduStatusOffRequest_Object = MibScalar
pduStatusOffRequest = _PduStatusOffRequest_Object(
    (1, 3, 6, 1, 4, 1, 45553, 5, 10),
    _PduStatusOffRequest_Type()
)
pduStatusOffRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatusOffRequest.setStatus("mandatory")


class _PduStatusMains_Type(Integer32):
    """Custom type pduStatusMains based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 1),
          ("present", 2))
    )


_PduStatusMains_Type.__name__ = "Integer32"
_PduStatusMains_Object = MibScalar
pduStatusMains = _PduStatusMains_Object(
    (1, 3, 6, 1, 4, 1, 45553, 5, 11),
    _PduStatusMains_Type()
)
pduStatusMains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatusMains.setStatus("mandatory")


class _PduStatusInternalImmediate_Type(Integer32):
    """Custom type pduStatusInternalImmediate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_PduStatusInternalImmediate_Type.__name__ = "Integer32"
_PduStatusInternalImmediate_Object = MibScalar
pduStatusInternalImmediate = _PduStatusInternalImmediate_Object(
    (1, 3, 6, 1, 4, 1, 45553, 5, 12),
    _PduStatusInternalImmediate_Type()
)
pduStatusInternalImmediate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatusInternalImmediate.setStatus("mandatory")


class _PduStatusInternalDelayed_Type(Integer32):
    """Custom type pduStatusInternalDelayed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_PduStatusInternalDelayed_Type.__name__ = "Integer32"
_PduStatusInternalDelayed_Object = MibScalar
pduStatusInternalDelayed = _PduStatusInternalDelayed_Object(
    (1, 3, 6, 1, 4, 1, 45553, 5, 13),
    _PduStatusInternalDelayed_Type()
)
pduStatusInternalDelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatusInternalDelayed.setStatus("mandatory")


class _PduStatusInternalMainsMem_Type(Integer32):
    """Custom type pduStatusInternalMainsMem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("memoryNotRemoved", 1),
          ("memoryRemoved", 2))
    )


_PduStatusInternalMainsMem_Type.__name__ = "Integer32"
_PduStatusInternalMainsMem_Object = MibScalar
pduStatusInternalMainsMem = _PduStatusInternalMainsMem_Object(
    (1, 3, 6, 1, 4, 1, 45553, 5, 14),
    _PduStatusInternalMainsMem_Type()
)
pduStatusInternalMainsMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatusInternalMainsMem.setStatus("mandatory")


class _PduStatusInternalDelayedMem_Type(Integer32):
    """Custom type pduStatusInternalDelayedMem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("memoryNotRemoved", 1),
          ("memoryRemoved", 2))
    )


_PduStatusInternalDelayedMem_Type.__name__ = "Integer32"
_PduStatusInternalDelayedMem_Object = MibScalar
pduStatusInternalDelayedMem = _PduStatusInternalDelayedMem_Object(
    (1, 3, 6, 1, 4, 1, 45553, 5, 15),
    _PduStatusInternalDelayedMem_Type()
)
pduStatusInternalDelayedMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatusInternalDelayedMem.setStatus("mandatory")


class _PduStatusInternalVcimPowerRmv_Type(Integer32):
    """Custom type pduStatusInternalVcimPowerRmv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerNotRemoved", 1),
          ("powerRemoved", 2))
    )


_PduStatusInternalVcimPowerRmv_Type.__name__ = "Integer32"
_PduStatusInternalVcimPowerRmv_Object = MibScalar
pduStatusInternalVcimPowerRmv = _PduStatusInternalVcimPowerRmv_Object(
    (1, 3, 6, 1, 4, 1, 45553, 5, 16),
    _PduStatusInternalVcimPowerRmv_Type()
)
pduStatusInternalVcimPowerRmv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatusInternalVcimPowerRmv.setStatus("mandatory")


class _PduStatusInternalVcimPowerRmvMem_Type(Integer32):
    """Custom type pduStatusInternalVcimPowerRmvMem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("memoryNotRemoved", 1),
          ("memoryRemoved", 2))
    )


_PduStatusInternalVcimPowerRmvMem_Type.__name__ = "Integer32"
_PduStatusInternalVcimPowerRmvMem_Object = MibScalar
pduStatusInternalVcimPowerRmvMem = _PduStatusInternalVcimPowerRmvMem_Object(
    (1, 3, 6, 1, 4, 1, 45553, 5, 17),
    _PduStatusInternalVcimPowerRmvMem_Type()
)
pduStatusInternalVcimPowerRmvMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatusInternalVcimPowerRmvMem.setStatus("mandatory")


class _PduStatusInternalVcimPower_Type(Integer32):
    """Custom type pduStatusInternalVcimPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vcimNotPowered", 1),
          ("vcimPowered", 2))
    )


_PduStatusInternalVcimPower_Type.__name__ = "Integer32"
_PduStatusInternalVcimPower_Object = MibScalar
pduStatusInternalVcimPower = _PduStatusInternalVcimPower_Object(
    (1, 3, 6, 1, 4, 1, 45553, 5, 18),
    _PduStatusInternalVcimPower_Type()
)
pduStatusInternalVcimPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatusInternalVcimPower.setStatus("mandatory")
_PduError_ObjectIdentity = ObjectIdentity
pduError = _PduError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45553, 6)
)


class _PduErrorPowerSupply_Type(Integer32):
    """Custom type pduErrorPowerSupply based on Integer32"""
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
        *(("noPowerSupplyFails", 1),
          ("powerSupply1Fails", 2),
          ("powerSupply2Fails", 3),
          ("powerSupply1and2Fails", 4))
    )


_PduErrorPowerSupply_Type.__name__ = "Integer32"
_PduErrorPowerSupply_Object = MibScalar
pduErrorPowerSupply = _PduErrorPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 45553, 6, 1),
    _PduErrorPowerSupply_Type()
)
pduErrorPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduErrorPowerSupply.setStatus("mandatory")
_PduErrorStatus2_Type = Integer32
_PduErrorStatus2_Object = MibScalar
pduErrorStatus2 = _PduErrorStatus2_Object(
    (1, 3, 6, 1, 4, 1, 45553, 6, 2),
    _PduErrorStatus2_Type()
)
pduErrorStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduErrorStatus2.setStatus("mandatory")

# Managed Objects groups


# Notification objects

pduTrapErrorPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 45553, 0, 1)
)
pduTrapErrorPowerSupply.setObjects(
    ("INNOVA-POWER-MIB", "pduErrorPowerSupply")
)
if mibBuilder.loadTexts:
    pduTrapErrorPowerSupply.setStatus(
        ""
    )

pduTrapOffRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 45553, 0, 2)
)
pduTrapOffRequest.setObjects(
    ("INNOVA-POWER-MIB", "pduStatusOffRequest")
)
if mibBuilder.loadTexts:
    pduTrapOffRequest.setStatus(
        ""
    )

pduTrapMainsStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 45553, 0, 3)
)
pduTrapMainsStatus.setObjects(
    ("INNOVA-POWER-MIB", "pduStatusMains")
)
if mibBuilder.loadTexts:
    pduTrapMainsStatus.setStatus(
        ""
    )

pduTrapGeneratorPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 45553, 0, 4)
)
pduTrapGeneratorPowerSupply.setObjects(
    ("INNOVA-POWER-MIB", "pduStatusGeneratorPowerSupply")
)
if mibBuilder.loadTexts:
    pduTrapGeneratorPowerSupply.setStatus(
        ""
    )

pduTrapInput1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 45553, 0, 5)
)
pduTrapInput1.setObjects(
    ("INNOVA-POWER-MIB", "pduStatusInput1")
)
if mibBuilder.loadTexts:
    pduTrapInput1.setStatus(
        ""
    )

pduTrapInput2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 45553, 0, 6)
)
pduTrapInput2.setObjects(
    ("INNOVA-POWER-MIB", "pduStatusInput2")
)
if mibBuilder.loadTexts:
    pduTrapInput2.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INNOVA-POWER-MIB",
    **{"gehc-eng": gehc_eng,
       "pduTrapErrorPowerSupply": pduTrapErrorPowerSupply,
       "pduTrapOffRequest": pduTrapOffRequest,
       "pduTrapMainsStatus": pduTrapMainsStatus,
       "pduTrapGeneratorPowerSupply": pduTrapGeneratorPowerSupply,
       "pduTrapInput1": pduTrapInput1,
       "pduTrapInput2": pduTrapInput2,
       "pduSnmpAgent": pduSnmpAgent,
       "pduSnmpAgentName": pduSnmpAgentName,
       "pduSnmpAgentVersion": pduSnmpAgentVersion,
       "pduSnmpAgentDate": pduSnmpAgentDate,
       "pduTrapReceiver": pduTrapReceiver,
       "trapTable": trapTable,
       "trapEntry": trapEntry,
       "trapReceiverNumber": trapReceiverNumber,
       "trapEnabled": trapEnabled,
       "trapReceiverIPAddress": trapReceiverIPAddress,
       "trapCommunity": trapCommunity,
       "pduId": pduId,
       "pduUniqueId": pduUniqueId,
       "pduFirmwareRevision": pduFirmwareRevision,
       "pduControl": pduControl,
       "pduControlOffDelayed": pduControlOffDelayed,
       "pduControlGeneratorPowerSupply": pduControlGeneratorPowerSupply,
       "pduControlChillerAndTubePumpPowerSupply": pduControlChillerAndTubePumpPowerSupply,
       "pduControlOutput1": pduControlOutput1,
       "pduControlOutput2": pduControlOutput2,
       "pduControlXrayLight": pduControlXrayLight,
       "pduControlRoomLight": pduControlRoomLight,
       "pduStatus": pduStatus,
       "pduStatusOffCountDown": pduStatusOffCountDown,
       "pduStatusGeneratorPowerSupply": pduStatusGeneratorPowerSupply,
       "pduStatusInput1": pduStatusInput1,
       "pduStatusInput2": pduStatusInput2,
       "pduStatusInternal24V1": pduStatusInternal24V1,
       "pduStatusInternal24V2": pduStatusInternal24V2,
       "pduStatusIntTemp": pduStatusIntTemp,
       "pduStatusExtTemp1": pduStatusExtTemp1,
       "pduStatusExtTemp2": pduStatusExtTemp2,
       "pduStatusOffRequest": pduStatusOffRequest,
       "pduStatusMains": pduStatusMains,
       "pduStatusInternalImmediate": pduStatusInternalImmediate,
       "pduStatusInternalDelayed": pduStatusInternalDelayed,
       "pduStatusInternalMainsMem": pduStatusInternalMainsMem,
       "pduStatusInternalDelayedMem": pduStatusInternalDelayedMem,
       "pduStatusInternalVcimPowerRmv": pduStatusInternalVcimPowerRmv,
       "pduStatusInternalVcimPowerRmvMem": pduStatusInternalVcimPowerRmvMem,
       "pduStatusInternalVcimPower": pduStatusInternalVcimPower,
       "pduError": pduError,
       "pduErrorPowerSupply": pduErrorPowerSupply,
       "pduErrorStatus2": pduErrorStatus2}
)

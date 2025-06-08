# SNMP MIB module (AIRCELL-ABS-ATG5K-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/aircell_28382/AIRCELL-ABS-ATG5K-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:18:40 2025
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

aircellAbsAtg5kMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 6)
)
if mibBuilder.loadTexts:
    aircellAbsAtg5kMib.setRevisions(
        ("2011-07-26 14:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aircell_ObjectIdentity = ObjectIdentity
aircell = _Aircell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382)
)
_AbsAtg5kPac_ObjectIdentity = ObjectIdentity
absAtg5kPac = _AbsAtg5kPac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1)
)


class _AtgPacBridgeStatus_Type(Integer32):
    """Custom type atgPacBridgeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AtgPacBridgeStatus_Type.__name__ = "Integer32"
_AtgPacBridgeStatus_Object = MibScalar
atgPacBridgeStatus = _AtgPacBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 1),
    _AtgPacBridgeStatus_Type()
)
atgPacBridgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atgPacBridgeStatus.setStatus("current")


class _AtgPacOperStatus_Type(Integer32):
    """Custom type atgPacOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AtgPacOperStatus_Type.__name__ = "Integer32"
_AtgPacOperStatus_Object = MibScalar
atgPacOperStatus = _AtgPacOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 2),
    _AtgPacOperStatus_Type()
)
atgPacOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atgPacOperStatus.setStatus("current")


class _AtgPacAdminState_Type(Integer32):
    """Custom type atgPacAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("unlock", 2))
    )


_AtgPacAdminState_Type.__name__ = "Integer32"
_AtgPacAdminState_Object = MibScalar
atgPacAdminState = _AtgPacAdminState_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 3),
    _AtgPacAdminState_Type()
)
atgPacAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atgPacAdminState.setStatus("current")


class _AtgPacDeviceReset_Type(Integer32):
    """Custom type atgPacDeviceReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noreset", 1),
          ("reset", 2))
    )


_AtgPacDeviceReset_Type.__name__ = "Integer32"
_AtgPacDeviceReset_Object = MibScalar
atgPacDeviceReset = _AtgPacDeviceReset_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 4),
    _AtgPacDeviceReset_Type()
)
atgPacDeviceReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atgPacDeviceReset.setStatus("current")


class _AtgPacAircard2Reset_Type(Integer32):
    """Custom type atgPacAircard2Reset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noreset", 1),
          ("reset", 2))
    )


_AtgPacAircard2Reset_Type.__name__ = "Integer32"
_AtgPacAircard2Reset_Object = MibScalar
atgPacAircard2Reset = _AtgPacAircard2Reset_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 5),
    _AtgPacAircard2Reset_Type()
)
atgPacAircard2Reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atgPacAircard2Reset.setStatus("current")


class _AtgPacInterfaceReset_Type(Integer32):
    """Custom type atgPacInterfaceReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noreset", 1),
          ("reset", 2))
    )


_AtgPacInterfaceReset_Type.__name__ = "Integer32"
_AtgPacInterfaceReset_Object = MibScalar
atgPacInterfaceReset = _AtgPacInterfaceReset_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 6),
    _AtgPacInterfaceReset_Type()
)
atgPacInterfaceReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atgPacInterfaceReset.setStatus("current")


class _AtgPacResetAcpu_Type(Integer32):
    """Custom type atgPacResetAcpu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noreset", 1),
          ("reset", 2))
    )


_AtgPacResetAcpu_Type.__name__ = "Integer32"
_AtgPacResetAcpu_Object = MibScalar
atgPacResetAcpu = _AtgPacResetAcpu_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 7),
    _AtgPacResetAcpu_Type()
)
atgPacResetAcpu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atgPacResetAcpu.setStatus("current")


class _AtgPacTemperature_Type(DisplayString):
    """Custom type atgPacTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AtgPacTemperature_Type.__name__ = "DisplayString"
_AtgPacTemperature_Object = MibScalar
atgPacTemperature = _AtgPacTemperature_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 8),
    _AtgPacTemperature_Type()
)
atgPacTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atgPacTemperature.setStatus("current")


class _AtgPacCpuUtilization_Type(DisplayString):
    """Custom type atgPacCpuUtilization based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AtgPacCpuUtilization_Type.__name__ = "DisplayString"
_AtgPacCpuUtilization_Object = MibScalar
atgPacCpuUtilization = _AtgPacCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 9),
    _AtgPacCpuUtilization_Type()
)
atgPacCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atgPacCpuUtilization.setStatus("current")


class _AtgPacMemoryUtilization_Type(DisplayString):
    """Custom type atgPacMemoryUtilization based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AtgPacMemoryUtilization_Type.__name__ = "DisplayString"
_AtgPacMemoryUtilization_Object = MibScalar
atgPacMemoryUtilization = _AtgPacMemoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 10),
    _AtgPacMemoryUtilization_Type()
)
atgPacMemoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atgPacMemoryUtilization.setStatus("current")


class _AtgPacKernelVersion_Type(DisplayString):
    """Custom type atgPacKernelVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AtgPacKernelVersion_Type.__name__ = "DisplayString"
_AtgPacKernelVersion_Object = MibScalar
atgPacKernelVersion = _AtgPacKernelVersion_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 11),
    _AtgPacKernelVersion_Type()
)
atgPacKernelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atgPacKernelVersion.setStatus("current")


class _AtgPacFileSystemVersion_Type(DisplayString):
    """Custom type atgPacFileSystemVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AtgPacFileSystemVersion_Type.__name__ = "DisplayString"
_AtgPacFileSystemVersion_Object = MibScalar
atgPacFileSystemVersion = _AtgPacFileSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 12),
    _AtgPacFileSystemVersion_Type()
)
atgPacFileSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atgPacFileSystemVersion.setStatus("current")


class _AtgPacHardwarePartNumber_Type(DisplayString):
    """Custom type atgPacHardwarePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AtgPacHardwarePartNumber_Type.__name__ = "DisplayString"
_AtgPacHardwarePartNumber_Object = MibScalar
atgPacHardwarePartNumber = _AtgPacHardwarePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 13),
    _AtgPacHardwarePartNumber_Type()
)
atgPacHardwarePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atgPacHardwarePartNumber.setStatus("current")


class _AtgPacSoftwarePartNumber_Type(DisplayString):
    """Custom type atgPacSoftwarePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AtgPacSoftwarePartNumber_Type.__name__ = "DisplayString"
_AtgPacSoftwarePartNumber_Object = MibScalar
atgPacSoftwarePartNumber = _AtgPacSoftwarePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 14),
    _AtgPacSoftwarePartNumber_Type()
)
atgPacSoftwarePartNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atgPacSoftwarePartNumber.setStatus("current")


class _AtgPacSerialNumber_Type(DisplayString):
    """Custom type atgPacSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AtgPacSerialNumber_Type.__name__ = "DisplayString"
_AtgPacSerialNumber_Object = MibScalar
atgPacSerialNumber = _AtgPacSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 15),
    _AtgPacSerialNumber_Type()
)
atgPacSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atgPacSerialNumber.setStatus("current")


class _AtgPacMuxReset_Type(Integer32):
    """Custom type atgPacMuxReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noreset", 1),
          ("reset", 2))
    )


_AtgPacMuxReset_Type.__name__ = "Integer32"
_AtgPacMuxReset_Object = MibScalar
atgPacMuxReset = _AtgPacMuxReset_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 16),
    _AtgPacMuxReset_Type()
)
atgPacMuxReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atgPacMuxReset.setStatus("current")


class _AtgPacMuxStatus_Type(Integer32):
    """Custom type atgPacMuxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AtgPacMuxStatus_Type.__name__ = "Integer32"
_AtgPacMuxStatus_Object = MibScalar
atgPacMuxStatus = _AtgPacMuxStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 17),
    _AtgPacMuxStatus_Type()
)
atgPacMuxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atgPacMuxStatus.setStatus("current")


class _AtgPacAircard1PPPIpAddress_Type(DisplayString):
    """Custom type atgPacAircard1PPPIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AtgPacAircard1PPPIpAddress_Type.__name__ = "DisplayString"
_AtgPacAircard1PPPIpAddress_Object = MibScalar
atgPacAircard1PPPIpAddress = _AtgPacAircard1PPPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 18),
    _AtgPacAircard1PPPIpAddress_Type()
)
atgPacAircard1PPPIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atgPacAircard1PPPIpAddress.setStatus("current")


class _AtgPacAircard2PPPIpAddress_Type(DisplayString):
    """Custom type atgPacAircard2PPPIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AtgPacAircard2PPPIpAddress_Type.__name__ = "DisplayString"
_AtgPacAircard2PPPIpAddress_Object = MibScalar
atgPacAircard2PPPIpAddress = _AtgPacAircard2PPPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 19),
    _AtgPacAircard2PPPIpAddress_Type()
)
atgPacAircard2PPPIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atgPacAircard2PPPIpAddress.setStatus("current")


class _AtgPacMuxPIPStatus_Type(Integer32):
    """Custom type atgPacMuxPIPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AtgPacMuxPIPStatus_Type.__name__ = "Integer32"
_AtgPacMuxPIPStatus_Object = MibScalar
atgPacMuxPIPStatus = _AtgPacMuxPIPStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 20),
    _AtgPacMuxPIPStatus_Type()
)
atgPacMuxPIPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atgPacMuxPIPStatus.setStatus("current")


class _AtgPacAcpuDefaultRoute_Type(Integer32):
    """Custom type atgPacAcpuDefaultRoute based on Integer32"""
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
        *(("aircard1", 1),
          ("aircard2", 2),
          ("atgPac", 3),
          ("noRoute", 4))
    )


_AtgPacAcpuDefaultRoute_Type.__name__ = "Integer32"
_AtgPacAcpuDefaultRoute_Object = MibScalar
atgPacAcpuDefaultRoute = _AtgPacAcpuDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 21),
    _AtgPacAcpuDefaultRoute_Type()
)
atgPacAcpuDefaultRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atgPacAcpuDefaultRoute.setStatus("current")


class _AtgPacAircard2AdminStatus_Type(Integer32):
    """Custom type atgPacAircard2AdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("unlock", 2))
    )


_AtgPacAircard2AdminStatus_Type.__name__ = "Integer32"
_AtgPacAircard2AdminStatus_Object = MibScalar
atgPacAircard2AdminStatus = _AtgPacAircard2AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 22),
    _AtgPacAircard2AdminStatus_Type()
)
atgPacAircard2AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atgPacAircard2AdminStatus.setStatus("current")


class _AtgPacAircard2OperStatus_Type(Integer32):
    """Custom type atgPacAircard2OperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AtgPacAircard2OperStatus_Type.__name__ = "Integer32"
_AtgPacAircard2OperStatus_Object = MibScalar
atgPacAircard2OperStatus = _AtgPacAircard2OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 1, 23),
    _AtgPacAircard2OperStatus_Type()
)
atgPacAircard2OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atgPacAircard2OperStatus.setStatus("current")
_AbsAtg5kTable_ObjectIdentity = ObjectIdentity
absAtg5kTable = _AbsAtg5kTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 6, 2)
)
_AtgPacEthernetPortTable_Object = MibTable
atgPacEthernetPortTable = _AtgPacEthernetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 2, 1)
)
if mibBuilder.loadTexts:
    atgPacEthernetPortTable.setStatus("current")
_AtgPacEthernetPortEntry_Object = MibTableRow
atgPacEthernetPortEntry = _AtgPacEthernetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 2, 1, 1)
)
atgPacEthernetPortEntry.setIndexNames(
    (0, "AIRCELL-ABS-ATG5K-MIB", "atgPacEthernetPortIndex"),
)
if mibBuilder.loadTexts:
    atgPacEthernetPortEntry.setStatus("current")


class _AtgPacEthernetPortIndex_Type(Integer32):
    """Custom type atgPacEthernetPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AtgPacEthernetPortIndex_Type.__name__ = "Integer32"
_AtgPacEthernetPortIndex_Object = MibTableColumn
atgPacEthernetPortIndex = _AtgPacEthernetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 2, 1, 1, 1),
    _AtgPacEthernetPortIndex_Type()
)
atgPacEthernetPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atgPacEthernetPortIndex.setStatus("current")


class _AtgPacEthernetPortName_Type(DisplayString):
    """Custom type atgPacEthernetPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AtgPacEthernetPortName_Type.__name__ = "DisplayString"
_AtgPacEthernetPortName_Object = MibTableColumn
atgPacEthernetPortName = _AtgPacEthernetPortName_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 2, 1, 1, 2),
    _AtgPacEthernetPortName_Type()
)
atgPacEthernetPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atgPacEthernetPortName.setStatus("current")


class _AtgPacEthernetPortStatus_Type(Integer32):
    """Custom type atgPacEthernetPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AtgPacEthernetPortStatus_Type.__name__ = "Integer32"
_AtgPacEthernetPortStatus_Object = MibTableColumn
atgPacEthernetPortStatus = _AtgPacEthernetPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 2, 1, 1, 3),
    _AtgPacEthernetPortStatus_Type()
)
atgPacEthernetPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atgPacEthernetPortStatus.setStatus("current")


class _AtgPacEthernetPortLinkRate_Type(DisplayString):
    """Custom type atgPacEthernetPortLinkRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AtgPacEthernetPortLinkRate_Type.__name__ = "DisplayString"
_AtgPacEthernetPortLinkRate_Object = MibTableColumn
atgPacEthernetPortLinkRate = _AtgPacEthernetPortLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 2, 1, 1, 4),
    _AtgPacEthernetPortLinkRate_Type()
)
atgPacEthernetPortLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atgPacEthernetPortLinkRate.setStatus("current")


class _AtgPacEthernetPortDuplexity_Type(Integer32):
    """Custom type atgPacEthernetPortDuplexity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("half", 1),
          ("full", 2))
    )


_AtgPacEthernetPortDuplexity_Type.__name__ = "Integer32"
_AtgPacEthernetPortDuplexity_Object = MibTableColumn
atgPacEthernetPortDuplexity = _AtgPacEthernetPortDuplexity_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 2, 1, 1, 5),
    _AtgPacEthernetPortDuplexity_Type()
)
atgPacEthernetPortDuplexity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atgPacEthernetPortDuplexity.setStatus("current")
_AtgPacEthernetPortRxCrcErrFrameCnt_Type = Integer32
_AtgPacEthernetPortRxCrcErrFrameCnt_Object = MibTableColumn
atgPacEthernetPortRxCrcErrFrameCnt = _AtgPacEthernetPortRxCrcErrFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 2, 1, 1, 6),
    _AtgPacEthernetPortRxCrcErrFrameCnt_Type()
)
atgPacEthernetPortRxCrcErrFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atgPacEthernetPortRxCrcErrFrameCnt.setStatus("current")
_AtgPacEthernetPortTxOctets_Type = Counter64
_AtgPacEthernetPortTxOctets_Object = MibTableColumn
atgPacEthernetPortTxOctets = _AtgPacEthernetPortTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 2, 1, 1, 7),
    _AtgPacEthernetPortTxOctets_Type()
)
atgPacEthernetPortTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atgPacEthernetPortTxOctets.setStatus("current")
_AtgPacEthernetPortRxOctets_Type = Counter64
_AtgPacEthernetPortRxOctets_Object = MibTableColumn
atgPacEthernetPortRxOctets = _AtgPacEthernetPortRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28382, 6, 2, 1, 1, 8),
    _AtgPacEthernetPortRxOctets_Type()
)
atgPacEthernetPortRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atgPacEthernetPortRxOctets.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIRCELL-ABS-ATG5K-MIB",
    **{"aircell": aircell,
       "aircellAbsAtg5kMib": aircellAbsAtg5kMib,
       "absAtg5kPac": absAtg5kPac,
       "atgPacBridgeStatus": atgPacBridgeStatus,
       "atgPacOperStatus": atgPacOperStatus,
       "atgPacAdminState": atgPacAdminState,
       "atgPacDeviceReset": atgPacDeviceReset,
       "atgPacAircard2Reset": atgPacAircard2Reset,
       "atgPacInterfaceReset": atgPacInterfaceReset,
       "atgPacResetAcpu": atgPacResetAcpu,
       "atgPacTemperature": atgPacTemperature,
       "atgPacCpuUtilization": atgPacCpuUtilization,
       "atgPacMemoryUtilization": atgPacMemoryUtilization,
       "atgPacKernelVersion": atgPacKernelVersion,
       "atgPacFileSystemVersion": atgPacFileSystemVersion,
       "atgPacHardwarePartNumber": atgPacHardwarePartNumber,
       "atgPacSoftwarePartNumber": atgPacSoftwarePartNumber,
       "atgPacSerialNumber": atgPacSerialNumber,
       "atgPacMuxReset": atgPacMuxReset,
       "atgPacMuxStatus": atgPacMuxStatus,
       "atgPacAircard1PPPIpAddress": atgPacAircard1PPPIpAddress,
       "atgPacAircard2PPPIpAddress": atgPacAircard2PPPIpAddress,
       "atgPacMuxPIPStatus": atgPacMuxPIPStatus,
       "atgPacAcpuDefaultRoute": atgPacAcpuDefaultRoute,
       "atgPacAircard2AdminStatus": atgPacAircard2AdminStatus,
       "atgPacAircard2OperStatus": atgPacAircard2OperStatus,
       "absAtg5kTable": absAtg5kTable,
       "atgPacEthernetPortTable": atgPacEthernetPortTable,
       "atgPacEthernetPortEntry": atgPacEthernetPortEntry,
       "atgPacEthernetPortIndex": atgPacEthernetPortIndex,
       "atgPacEthernetPortName": atgPacEthernetPortName,
       "atgPacEthernetPortStatus": atgPacEthernetPortStatus,
       "atgPacEthernetPortLinkRate": atgPacEthernetPortLinkRate,
       "atgPacEthernetPortDuplexity": atgPacEthernetPortDuplexity,
       "atgPacEthernetPortRxCrcErrFrameCnt": atgPacEthernetPortRxCrcErrFrameCnt,
       "atgPacEthernetPortTxOctets": atgPacEthernetPortTxOctets,
       "atgPacEthernetPortRxOctets": atgPacEthernetPortRxOctets}
)

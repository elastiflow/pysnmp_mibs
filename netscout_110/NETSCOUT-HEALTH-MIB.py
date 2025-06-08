# SNMP MIB module (NETSCOUT-HEALTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/netscout_110/NETSCOUT-HEALTH-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:36:28 2025
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

netscoutHealth = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 110)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PlatformGroup_ObjectIdentity = ObjectIdentity
platformGroup = _PlatformGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 110, 1)
)
_PlatformInformationTable_Object = MibTable
platformInformationTable = _PlatformInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 1)
)
if mibBuilder.loadTexts:
    platformInformationTable.setStatus("current")
_PlatformInformationEntry_Object = MibTableRow
platformInformationEntry = _PlatformInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 1, 1)
)
platformInformationEntry.setIndexNames(
    (0, "NETSCOUT-HEALTH-MIB", "platformInformationIndex"),
)
if mibBuilder.loadTexts:
    platformInformationEntry.setStatus("current")


class _PlatformInformationIndex_Type(Integer32):
    """Custom type platformInformationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformInformationIndex_Type.__name__ = "Integer32"
_PlatformInformationIndex_Object = MibTableColumn
platformInformationIndex = _PlatformInformationIndex_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 1, 1, 1),
    _PlatformInformationIndex_Type()
)
platformInformationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformInformationIndex.setStatus("current")


class _PlatformProductId_Type(Integer32):
    """Custom type platformProductId based on Integer32"""
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
          ("infiniStream", 1),
          ("pfs", 2))
    )


_PlatformProductId_Type.__name__ = "Integer32"
_PlatformProductId_Object = MibTableColumn
platformProductId = _PlatformProductId_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 1, 1, 2),
    _PlatformProductId_Type()
)
platformProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformProductId.setStatus("current")


class _PlatformModel_Type(DisplayString):
    """Custom type platformModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PlatformModel_Type.__name__ = "DisplayString"
_PlatformModel_Object = MibTableColumn
platformModel = _PlatformModel_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 1, 1, 3),
    _PlatformModel_Type()
)
platformModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformModel.setStatus("current")


class _PlatformSoftwareVersion_Type(DisplayString):
    """Custom type platformSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PlatformSoftwareVersion_Type.__name__ = "DisplayString"
_PlatformSoftwareVersion_Object = MibTableColumn
platformSoftwareVersion = _PlatformSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 1, 1, 4),
    _PlatformSoftwareVersion_Type()
)
platformSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformSoftwareVersion.setStatus("current")


class _PlatformDecodeVersion_Type(DisplayString):
    """Custom type platformDecodeVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PlatformDecodeVersion_Type.__name__ = "DisplayString"
_PlatformDecodeVersion_Object = MibTableColumn
platformDecodeVersion = _PlatformDecodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 1, 1, 5),
    _PlatformDecodeVersion_Type()
)
platformDecodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformDecodeVersion.setStatus("current")


class _PlatformMode_Type(Integer32):
    """Custom type platformMode based on Integer32"""
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
        *(("unknown", 0),
          ("pm", 1),
          ("inmc", 2),
          ("pmANDinmc", 3))
    )


_PlatformMode_Type.__name__ = "Integer32"
_PlatformMode_Object = MibTableColumn
platformMode = _PlatformMode_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 1, 1, 6),
    _PlatformMode_Type()
)
platformMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformMode.setStatus("current")
_PlatformMACAddress_Type = DisplayString
_PlatformMACAddress_Object = MibTableColumn
platformMACAddress = _PlatformMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 1, 1, 7),
    _PlatformMACAddress_Type()
)
platformMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformMACAddress.setStatus("current")
_PlatformIpAddressType_Type = InetAddressType
_PlatformIpAddressType_Object = MibTableColumn
platformIpAddressType = _PlatformIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 1, 1, 8),
    _PlatformIpAddressType_Type()
)
platformIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformIpAddressType.setStatus("current")
_PlatformIpAddress_Type = InetAddress
_PlatformIpAddress_Object = MibTableColumn
platformIpAddress = _PlatformIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 1, 1, 9),
    _PlatformIpAddress_Type()
)
platformIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformIpAddress.setStatus("current")
_PlatformMemory_Type = Integer32
_PlatformMemory_Object = MibTableColumn
platformMemory = _PlatformMemory_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 1, 1, 10),
    _PlatformMemory_Type()
)
platformMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformMemory.setStatus("current")
_PlatformCPU_Type = Integer32
_PlatformCPU_Object = MibTableColumn
platformCPU = _PlatformCPU_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 1, 1, 11),
    _PlatformCPU_Type()
)
platformCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformCPU.setStatus("current")
_PlatformCPUCores_Type = Integer32
_PlatformCPUCores_Object = MibTableColumn
platformCPUCores = _PlatformCPUCores_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 1, 1, 12),
    _PlatformCPUCores_Type()
)
platformCPUCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformCPUCores.setStatus("current")


class _PlatformStatus_Type(Integer32):
    """Custom type platformStatus based on Integer32"""
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
          ("ok", 1),
          ("degraded", 2))
    )


_PlatformStatus_Type.__name__ = "Integer32"
_PlatformStatus_Object = MibTableColumn
platformStatus = _PlatformStatus_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 1, 1, 13),
    _PlatformStatus_Type()
)
platformStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformStatus.setStatus("current")
_PlatformGatewayIpAddressType_Type = InetAddressType
_PlatformGatewayIpAddressType_Object = MibTableColumn
platformGatewayIpAddressType = _PlatformGatewayIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 1, 1, 14),
    _PlatformGatewayIpAddressType_Type()
)
platformGatewayIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformGatewayIpAddressType.setStatus("current")
_PlatformGatewayIpAddress_Type = InetAddress
_PlatformGatewayIpAddress_Object = MibTableColumn
platformGatewayIpAddress = _PlatformGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 1, 1, 15),
    _PlatformGatewayIpAddress_Type()
)
platformGatewayIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformGatewayIpAddress.setStatus("current")


class _PlatformHealthMibVersion_Type(Integer32):
    """Custom type platformHealthMibVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformHealthMibVersion_Type.__name__ = "Integer32"
_PlatformHealthMibVersion_Object = MibTableColumn
platformHealthMibVersion = _PlatformHealthMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 1, 1, 16),
    _PlatformHealthMibVersion_Type()
)
platformHealthMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformHealthMibVersion.setStatus("current")
_PlatformChassisTable_Object = MibTable
platformChassisTable = _PlatformChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 3)
)
if mibBuilder.loadTexts:
    platformChassisTable.setStatus("current")
_PlatformChassisEntry_Object = MibTableRow
platformChassisEntry = _PlatformChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 3, 1)
)
platformChassisEntry.setIndexNames(
    (0, "NETSCOUT-HEALTH-MIB", "platformChassisIndex"),
)
if mibBuilder.loadTexts:
    platformChassisEntry.setStatus("current")


class _PlatformChassisIndex_Type(Integer32):
    """Custom type platformChassisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformChassisIndex_Type.__name__ = "Integer32"
_PlatformChassisIndex_Object = MibTableColumn
platformChassisIndex = _PlatformChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 3, 1, 1),
    _PlatformChassisIndex_Type()
)
platformChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformChassisIndex.setStatus("current")


class _PlatformChassisType_Type(Integer32):
    """Custom type platformChassisType based on Integer32"""
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
          ("infiniStream", 1),
          ("jbod", 2))
    )


_PlatformChassisType_Type.__name__ = "Integer32"
_PlatformChassisType_Object = MibTableColumn
platformChassisType = _PlatformChassisType_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 3, 1, 2),
    _PlatformChassisType_Type()
)
platformChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformChassisType.setStatus("current")


class _PlatformChassisSN_Type(DisplayString):
    """Custom type platformChassisSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_PlatformChassisSN_Type.__name__ = "DisplayString"
_PlatformChassisSN_Object = MibTableColumn
platformChassisSN = _PlatformChassisSN_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 3, 1, 3),
    _PlatformChassisSN_Type()
)
platformChassisSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformChassisSN.setStatus("current")
_PlatformControllerTable_Object = MibTable
platformControllerTable = _PlatformControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 4)
)
if mibBuilder.loadTexts:
    platformControllerTable.setStatus("current")
_PlatformControllerEntry_Object = MibTableRow
platformControllerEntry = _PlatformControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 4, 1)
)
platformControllerEntry.setIndexNames(
    (0, "NETSCOUT-HEALTH-MIB", "platformControllerIndex"),
)
if mibBuilder.loadTexts:
    platformControllerEntry.setStatus("current")


class _PlatformControllerIndex_Type(Integer32):
    """Custom type platformControllerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformControllerIndex_Type.__name__ = "Integer32"
_PlatformControllerIndex_Object = MibTableColumn
platformControllerIndex = _PlatformControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 4, 1, 1),
    _PlatformControllerIndex_Type()
)
platformControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformControllerIndex.setStatus("current")


class _PlatformControllerState_Type(Bits):
    """Custom type platformControllerState based on Bits"""
    namedValues = NamedValues(
        *(("ok", 0),
          ("failed", 1),
          ("online", 2),
          ("offline", 3),
          ("unavailable", 4),
          ("reset", 5),
          ("memoryerror", 6))
    )

_PlatformControllerState_Type.__name__ = "Bits"
_PlatformControllerState_Object = MibTableColumn
platformControllerState = _PlatformControllerState_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 4, 1, 2),
    _PlatformControllerState_Type()
)
platformControllerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformControllerState.setStatus("current")


class _PlatformControllerModel_Type(DisplayString):
    """Custom type platformControllerModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PlatformControllerModel_Type.__name__ = "DisplayString"
_PlatformControllerModel_Object = MibTableColumn
platformControllerModel = _PlatformControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 4, 1, 3),
    _PlatformControllerModel_Type()
)
platformControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformControllerModel.setStatus("current")


class _PlatformControllerFirwareRev_Type(DisplayString):
    """Custom type platformControllerFirwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PlatformControllerFirwareRev_Type.__name__ = "DisplayString"
_PlatformControllerFirwareRev_Object = MibTableColumn
platformControllerFirwareRev = _PlatformControllerFirwareRev_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 4, 1, 4),
    _PlatformControllerFirwareRev_Type()
)
platformControllerFirwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformControllerFirwareRev.setStatus("current")


class _PlatformControllerSerial_Type(DisplayString):
    """Custom type platformControllerSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PlatformControllerSerial_Type.__name__ = "DisplayString"
_PlatformControllerSerial_Object = MibTableColumn
platformControllerSerial = _PlatformControllerSerial_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 4, 1, 5),
    _PlatformControllerSerial_Type()
)
platformControllerSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformControllerSerial.setStatus("current")


class _PlatformControllerSEDState_Type(Bits):
    """Custom type platformControllerSEDState based on Bits"""
    namedValues = NamedValues(
        *(("unknown", 0),
          ("no-security", 1),
          ("secure-capable", 2),
          ("encrypt-enable", 3),
          ("encrypt-failed", 4))
    )

_PlatformControllerSEDState_Type.__name__ = "Bits"
_PlatformControllerSEDState_Object = MibTableColumn
platformControllerSEDState = _PlatformControllerSEDState_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 4, 1, 6),
    _PlatformControllerSEDState_Type()
)
platformControllerSEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformControllerSEDState.setStatus("current")
_PlatformRAIDArrayTable_Object = MibTable
platformRAIDArrayTable = _PlatformRAIDArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 5)
)
if mibBuilder.loadTexts:
    platformRAIDArrayTable.setStatus("current")
_PlatformRAIDArrayEntry_Object = MibTableRow
platformRAIDArrayEntry = _PlatformRAIDArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 5, 1)
)
platformRAIDArrayEntry.setIndexNames(
    (0, "NETSCOUT-HEALTH-MIB", "platformRAIDArrayIndex"),
)
if mibBuilder.loadTexts:
    platformRAIDArrayEntry.setStatus("current")


class _PlatformRAIDArrayIndex_Type(Integer32):
    """Custom type platformRAIDArrayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformRAIDArrayIndex_Type.__name__ = "Integer32"
_PlatformRAIDArrayIndex_Object = MibTableColumn
platformRAIDArrayIndex = _PlatformRAIDArrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 5, 1, 1),
    _PlatformRAIDArrayIndex_Type()
)
platformRAIDArrayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformRAIDArrayIndex.setStatus("current")


class _PlatformControllerIDX_Type(Integer32):
    """Custom type platformControllerIDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformControllerIDX_Type.__name__ = "Integer32"
_PlatformControllerIDX_Object = MibTableColumn
platformControllerIDX = _PlatformControllerIDX_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 5, 1, 2),
    _PlatformControllerIDX_Type()
)
platformControllerIDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformControllerIDX.setStatus("current")


class _PlatformRAIDArrayName_Type(DisplayString):
    """Custom type platformRAIDArrayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PlatformRAIDArrayName_Type.__name__ = "DisplayString"
_PlatformRAIDArrayName_Object = MibTableColumn
platformRAIDArrayName = _PlatformRAIDArrayName_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 5, 1, 3),
    _PlatformRAIDArrayName_Type()
)
platformRAIDArrayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformRAIDArrayName.setStatus("current")


class _PlatformRAIDArrayState_Type(Bits):
    """Custom type platformRAIDArrayState based on Bits"""
    namedValues = NamedValues(
        *(("ok", 0),
          ("failed", 1),
          ("missing", 2),
          ("online", 3),
          ("offline", 4),
          ("initializing", 5),
          ("initpaused", 6),
          ("hotspareactive", 7),
          ("degraded", 8),
          ("partdegraded", 9),
          ("rebuildpaused", 10),
          ("rebuilding", 11),
          ("partrebuilding", 12),
          ("verifying", 13),
          ("verifypaused", 14),
          ("inoperable", 15),
          ("operational", 16),
          ("unavailable", 17),
          ("migrating", 18),
          ("badshutdown", 19),
          ("rebuilderror", 20),
          ("verifyerror", 21),
          ("unhandled", 22),
          ("mib-array-state-inconsistent", 23))
    )

_PlatformRAIDArrayState_Type.__name__ = "Bits"
_PlatformRAIDArrayState_Object = MibTableColumn
platformRAIDArrayState = _PlatformRAIDArrayState_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 5, 1, 4),
    _PlatformRAIDArrayState_Type()
)
platformRAIDArrayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformRAIDArrayState.setStatus("current")


class _PlatformRAIDArrayProgress_Type(Integer32):
    """Custom type platformRAIDArrayProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformRAIDArrayProgress_Type.__name__ = "Integer32"
_PlatformRAIDArrayProgress_Object = MibTableColumn
platformRAIDArrayProgress = _PlatformRAIDArrayProgress_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 5, 1, 5),
    _PlatformRAIDArrayProgress_Type()
)
platformRAIDArrayProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformRAIDArrayProgress.setStatus("current")


class _PlatformRAIDArrayType_Type(DisplayString):
    """Custom type platformRAIDArrayType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PlatformRAIDArrayType_Type.__name__ = "DisplayString"
_PlatformRAIDArrayType_Object = MibTableColumn
platformRAIDArrayType = _PlatformRAIDArrayType_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 5, 1, 6),
    _PlatformRAIDArrayType_Type()
)
platformRAIDArrayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformRAIDArrayType.setStatus("current")


class _PlatformRAIDArrayFormat_Type(Integer32):
    """Custom type platformRAIDArrayFormat based on Integer32"""
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
          ("raw", 1),
          ("xfs", 2))
    )


_PlatformRAIDArrayFormat_Type.__name__ = "Integer32"
_PlatformRAIDArrayFormat_Object = MibTableColumn
platformRAIDArrayFormat = _PlatformRAIDArrayFormat_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 5, 1, 7),
    _PlatformRAIDArrayFormat_Type()
)
platformRAIDArrayFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformRAIDArrayFormat.setStatus("current")


class _PlatformRAIDArraySize_Type(Integer32):
    """Custom type platformRAIDArraySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformRAIDArraySize_Type.__name__ = "Integer32"
_PlatformRAIDArraySize_Object = MibTableColumn
platformRAIDArraySize = _PlatformRAIDArraySize_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 5, 1, 8),
    _PlatformRAIDArraySize_Type()
)
platformRAIDArraySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformRAIDArraySize.setStatus("current")


class _PlatformRAIDArrayDrives_Type(Integer32):
    """Custom type platformRAIDArrayDrives based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformRAIDArrayDrives_Type.__name__ = "Integer32"
_PlatformRAIDArrayDrives_Object = MibTableColumn
platformRAIDArrayDrives = _PlatformRAIDArrayDrives_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 5, 1, 9),
    _PlatformRAIDArrayDrives_Type()
)
platformRAIDArrayDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformRAIDArrayDrives.setStatus("current")


class _PlatformRAIDArraySEDState_Type(Bits):
    """Custom type platformRAIDArraySEDState based on Bits"""
    namedValues = NamedValues(
        *(("unknown", 0),
          ("not-secure", 1),
          ("secure", 2),
          ("part-secure", 3),
          ("secure-failure", 4))
    )

_PlatformRAIDArraySEDState_Type.__name__ = "Bits"
_PlatformRAIDArraySEDState_Object = MibTableColumn
platformRAIDArraySEDState = _PlatformRAIDArraySEDState_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 5, 1, 10),
    _PlatformRAIDArraySEDState_Type()
)
platformRAIDArraySEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformRAIDArraySEDState.setStatus("current")
_PlatformDiskTable_Object = MibTable
platformDiskTable = _PlatformDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 6)
)
if mibBuilder.loadTexts:
    platformDiskTable.setStatus("current")
_PlatformDiskEntry_Object = MibTableRow
platformDiskEntry = _PlatformDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 6, 1)
)
platformDiskEntry.setIndexNames(
    (0, "NETSCOUT-HEALTH-MIB", "platformDiskIndex"),
)
if mibBuilder.loadTexts:
    platformDiskEntry.setStatus("current")


class _PlatformDiskIndex_Type(Integer32):
    """Custom type platformDiskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformDiskIndex_Type.__name__ = "Integer32"
_PlatformDiskIndex_Object = MibTableColumn
platformDiskIndex = _PlatformDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 6, 1, 1),
    _PlatformDiskIndex_Type()
)
platformDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformDiskIndex.setStatus("current")


class _PlatformRAIDArrayIDX_Type(Integer32):
    """Custom type platformRAIDArrayIDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformRAIDArrayIDX_Type.__name__ = "Integer32"
_PlatformRAIDArrayIDX_Object = MibTableColumn
platformRAIDArrayIDX = _PlatformRAIDArrayIDX_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 6, 1, 2),
    _PlatformRAIDArrayIDX_Type()
)
platformRAIDArrayIDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformRAIDArrayIDX.setStatus("current")


class _PlatformDiskChassisIDX_Type(Integer32):
    """Custom type platformDiskChassisIDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformDiskChassisIDX_Type.__name__ = "Integer32"
_PlatformDiskChassisIDX_Object = MibTableColumn
platformDiskChassisIDX = _PlatformDiskChassisIDX_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 6, 1, 3),
    _PlatformDiskChassisIDX_Type()
)
platformDiskChassisIDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformDiskChassisIDX.setStatus("current")


class _PlatformDiskName_Type(DisplayString):
    """Custom type platformDiskName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PlatformDiskName_Type.__name__ = "DisplayString"
_PlatformDiskName_Object = MibTableColumn
platformDiskName = _PlatformDiskName_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 6, 1, 4),
    _PlatformDiskName_Type()
)
platformDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformDiskName.setStatus("current")


class _PlatformDiskType_Type(Integer32):
    """Custom type platformDiskType based on Integer32"""
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
        *(("unknown", 0),
          ("system-ssd", 1),
          ("system-hdd", 2),
          ("data-ssd", 3),
          ("data-hdd", 4),
          ("spare-ssd", 5),
          ("spare-hdd", 6))
    )


_PlatformDiskType_Type.__name__ = "Integer32"
_PlatformDiskType_Object = MibTableColumn
platformDiskType = _PlatformDiskType_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 6, 1, 5),
    _PlatformDiskType_Type()
)
platformDiskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformDiskType.setStatus("current")


class _PlatformDiskState_Type(Bits):
    """Custom type platformDiskState based on Bits"""
    namedValues = NamedValues(
        *(("ok", 0),
          ("failed", 1),
          ("failing", 2),
          ("missing", 3),
          ("available", 4),
          ("unavaialable", 5),
          ("offline", 6),
          ("online", 7),
          ("ready", 8),
          ("rebuilding", 9),
          ("foreign", 10),
          ("removed", 11),
          ("degraded", 12),
          ("initializing", 13),
          ("hotspare", 14),
          ("badsector", 15),
          ("eccerror", 16),
          ("dcberror", 17),
          ("srceccerror", 18),
          ("unhandled", 19))
    )

_PlatformDiskState_Type.__name__ = "Bits"
_PlatformDiskState_Object = MibTableColumn
platformDiskState = _PlatformDiskState_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 6, 1, 6),
    _PlatformDiskState_Type()
)
platformDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformDiskState.setStatus("current")


class _PlatformDiskModel_Type(DisplayString):
    """Custom type platformDiskModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PlatformDiskModel_Type.__name__ = "DisplayString"
_PlatformDiskModel_Object = MibTableColumn
platformDiskModel = _PlatformDiskModel_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 6, 1, 7),
    _PlatformDiskModel_Type()
)
platformDiskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformDiskModel.setStatus("current")


class _PlatformDiskSize_Type(Integer32):
    """Custom type platformDiskSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformDiskSize_Type.__name__ = "Integer32"
_PlatformDiskSize_Object = MibTableColumn
platformDiskSize = _PlatformDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 6, 1, 8),
    _PlatformDiskSize_Type()
)
platformDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformDiskSize.setStatus("current")


class _PlatformDiskFirmware_Type(DisplayString):
    """Custom type platformDiskFirmware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PlatformDiskFirmware_Type.__name__ = "DisplayString"
_PlatformDiskFirmware_Object = MibTableColumn
platformDiskFirmware = _PlatformDiskFirmware_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 6, 1, 9),
    _PlatformDiskFirmware_Type()
)
platformDiskFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformDiskFirmware.setStatus("current")


class _PlatformDiskSlot_Type(Integer32):
    """Custom type platformDiskSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformDiskSlot_Type.__name__ = "Integer32"
_PlatformDiskSlot_Object = MibTableColumn
platformDiskSlot = _PlatformDiskSlot_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 6, 1, 10),
    _PlatformDiskSlot_Type()
)
platformDiskSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformDiskSlot.setStatus("current")


class _PlatformDiskSEDState_Type(Bits):
    """Custom type platformDiskSEDState based on Bits"""
    namedValues = NamedValues(
        *(("unknown", 0),
          ("not-SED", 1),
          ("sed-capable", 2),
          ("sed-enable", 3),
          ("sed-secured", 4),
          ("sed-locked", 5),
          ("sed-foreign-locked", 6),
          ("sed-secure-failed", 7),
          ("sed-secure-erased", 8))
    )

_PlatformDiskSEDState_Type.__name__ = "Bits"
_PlatformDiskSEDState_Object = MibTableColumn
platformDiskSEDState = _PlatformDiskSEDState_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 6, 1, 11),
    _PlatformDiskSEDState_Type()
)
platformDiskSEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformDiskSEDState.setStatus("current")
_PlatformPowerSupplyTable_Object = MibTable
platformPowerSupplyTable = _PlatformPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 7)
)
if mibBuilder.loadTexts:
    platformPowerSupplyTable.setStatus("current")
_PlatformPowerSupplyEntry_Object = MibTableRow
platformPowerSupplyEntry = _PlatformPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 7, 1)
)
platformPowerSupplyEntry.setIndexNames(
    (0, "NETSCOUT-HEALTH-MIB", "platformPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    platformPowerSupplyEntry.setStatus("current")


class _PlatformPowerSupplyIndex_Type(Integer32):
    """Custom type platformPowerSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformPowerSupplyIndex_Type.__name__ = "Integer32"
_PlatformPowerSupplyIndex_Object = MibTableColumn
platformPowerSupplyIndex = _PlatformPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 7, 1, 1),
    _PlatformPowerSupplyIndex_Type()
)
platformPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformPowerSupplyIndex.setStatus("current")


class _PlatformChassisIDX_Type(Integer32):
    """Custom type platformChassisIDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformChassisIDX_Type.__name__ = "Integer32"
_PlatformChassisIDX_Object = MibTableColumn
platformChassisIDX = _PlatformChassisIDX_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 7, 1, 2),
    _PlatformChassisIDX_Type()
)
platformChassisIDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformChassisIDX.setStatus("current")


class _PlatformPowerSupplyState_Type(Bits):
    """Custom type platformPowerSupplyState based on Bits"""
    namedValues = NamedValues(
        *(("ok", 0),
          ("failed", 1),
          ("critical", 2),
          ("presence-detected", 3),
          ("ac-lost", 4),
          ("not-available", 5),
          ("missing", 6),
          ("ac-added", 7))
    )

_PlatformPowerSupplyState_Type.__name__ = "Bits"
_PlatformPowerSupplyState_Object = MibTableColumn
platformPowerSupplyState = _PlatformPowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 7, 1, 3),
    _PlatformPowerSupplyState_Type()
)
platformPowerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformPowerSupplyState.setStatus("current")


class _PlatformPowerSupplyName_Type(DisplayString):
    """Custom type platformPowerSupplyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PlatformPowerSupplyName_Type.__name__ = "DisplayString"
_PlatformPowerSupplyName_Object = MibTableColumn
platformPowerSupplyName = _PlatformPowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 7, 1, 4),
    _PlatformPowerSupplyName_Type()
)
platformPowerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformPowerSupplyName.setStatus("current")
_PlatformMonitorIfTable_Object = MibTable
platformMonitorIfTable = _PlatformMonitorIfTable_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 8)
)
if mibBuilder.loadTexts:
    platformMonitorIfTable.setStatus("current")
_PlatformMonitorIfEntry_Object = MibTableRow
platformMonitorIfEntry = _PlatformMonitorIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 8, 1)
)
platformMonitorIfEntry.setIndexNames(
    (0, "NETSCOUT-HEALTH-MIB", "platformMonitorIfIndex"),
)
if mibBuilder.loadTexts:
    platformMonitorIfEntry.setStatus("current")


class _PlatformMonitorIfIndex_Type(Integer32):
    """Custom type platformMonitorIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformMonitorIfIndex_Type.__name__ = "Integer32"
_PlatformMonitorIfIndex_Object = MibTableColumn
platformMonitorIfIndex = _PlatformMonitorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 8, 1, 1),
    _PlatformMonitorIfIndex_Type()
)
platformMonitorIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformMonitorIfIndex.setStatus("current")


class _PlatforMonitorIfTableIDX_Type(Integer32):
    """Custom type platforMonitorIfTableIDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatforMonitorIfTableIDX_Type.__name__ = "Integer32"
_PlatforMonitorIfTableIDX_Object = MibTableColumn
platforMonitorIfTableIDX = _PlatforMonitorIfTableIDX_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 8, 1, 2),
    _PlatforMonitorIfTableIDX_Type()
)
platforMonitorIfTableIDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platforMonitorIfTableIDX.setStatus("current")


class _PlatformMonitorIfType_Type(DisplayString):
    """Custom type platformMonitorIfType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PlatformMonitorIfType_Type.__name__ = "DisplayString"
_PlatformMonitorIfType_Object = MibTableColumn
platformMonitorIfType = _PlatformMonitorIfType_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 8, 1, 3),
    _PlatformMonitorIfType_Type()
)
platformMonitorIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformMonitorIfType.setStatus("current")


class _PlatformMonitorIFXcvrType_Type(DisplayString):
    """Custom type platformMonitorIFXcvrType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PlatformMonitorIFXcvrType_Type.__name__ = "DisplayString"
_PlatformMonitorIFXcvrType_Object = MibTableColumn
platformMonitorIFXcvrType = _PlatformMonitorIFXcvrType_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 8, 1, 4),
    _PlatformMonitorIFXcvrType_Type()
)
platformMonitorIFXcvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformMonitorIFXcvrType.setStatus("current")


class _PlatformMonitorIfState_Type(Bits):
    """Custom type platformMonitorIfState based on Bits"""
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1),
          ("shutdown", 2),
          ("noModule", 3))
    )

_PlatformMonitorIfState_Type.__name__ = "Bits"
_PlatformMonitorIfState_Object = MibTableColumn
platformMonitorIfState = _PlatformMonitorIfState_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 8, 1, 5),
    _PlatformMonitorIfState_Type()
)
platformMonitorIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformMonitorIfState.setStatus("current")


class _PlatformMonitorIfRxPwr_Type(Integer32):
    """Custom type platformMonitorIfRxPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformMonitorIfRxPwr_Type.__name__ = "Integer32"
_PlatformMonitorIfRxPwr_Object = MibTableColumn
platformMonitorIfRxPwr = _PlatformMonitorIfRxPwr_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 8, 1, 6),
    _PlatformMonitorIfRxPwr_Type()
)
platformMonitorIfRxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformMonitorIfRxPwr.setStatus("current")
_PlatformMonitorIfName_Type = DisplayString
_PlatformMonitorIfName_Object = MibTableColumn
platformMonitorIfName = _PlatformMonitorIfName_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 8, 1, 7),
    _PlatformMonitorIfName_Type()
)
platformMonitorIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformMonitorIfName.setStatus("current")
_PlatformMgmtIfTable_Object = MibTable
platformMgmtIfTable = _PlatformMgmtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 9)
)
if mibBuilder.loadTexts:
    platformMgmtIfTable.setStatus("current")
_PlatformMgmtIfEntry_Object = MibTableRow
platformMgmtIfEntry = _PlatformMgmtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 9, 1)
)
platformMgmtIfEntry.setIndexNames(
    (0, "NETSCOUT-HEALTH-MIB", "platformMgmtIfIndex"),
)
if mibBuilder.loadTexts:
    platformMgmtIfEntry.setStatus("current")


class _PlatformMgmtIfIndex_Type(Integer32):
    """Custom type platformMgmtIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformMgmtIfIndex_Type.__name__ = "Integer32"
_PlatformMgmtIfIndex_Object = MibTableColumn
platformMgmtIfIndex = _PlatformMgmtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 9, 1, 1),
    _PlatformMgmtIfIndex_Type()
)
platformMgmtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformMgmtIfIndex.setStatus("current")
_PlatformMgmtIfName_Type = DisplayString
_PlatformMgmtIfName_Object = MibTableColumn
platformMgmtIfName = _PlatformMgmtIfName_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 9, 1, 2),
    _PlatformMgmtIfName_Type()
)
platformMgmtIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformMgmtIfName.setStatus("current")


class _PlatformMgmtIfState_Type(Bits):
    """Custom type platformMgmtIfState based on Bits"""
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1),
          ("shutdown", 2),
          ("noModule", 3))
    )

_PlatformMgmtIfState_Type.__name__ = "Bits"
_PlatformMgmtIfState_Object = MibTableColumn
platformMgmtIfState = _PlatformMgmtIfState_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 9, 1, 3),
    _PlatformMgmtIfState_Type()
)
platformMgmtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformMgmtIfState.setStatus("current")
_PlatformFanTable_Object = MibTable
platformFanTable = _PlatformFanTable_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 10)
)
if mibBuilder.loadTexts:
    platformFanTable.setStatus("current")
_PlatformFanEntry_Object = MibTableRow
platformFanEntry = _PlatformFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 10, 1)
)
platformFanEntry.setIndexNames(
    (0, "NETSCOUT-HEALTH-MIB", "platformFanIndex"),
)
if mibBuilder.loadTexts:
    platformFanEntry.setStatus("current")


class _PlatformFanIndex_Type(Integer32):
    """Custom type platformFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformFanIndex_Type.__name__ = "Integer32"
_PlatformFanIndex_Object = MibTableColumn
platformFanIndex = _PlatformFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 10, 1, 1),
    _PlatformFanIndex_Type()
)
platformFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformFanIndex.setStatus("current")


class _PlatformFanChassisIDX_Type(Integer32):
    """Custom type platformFanChassisIDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformFanChassisIDX_Type.__name__ = "Integer32"
_PlatformFanChassisIDX_Object = MibTableColumn
platformFanChassisIDX = _PlatformFanChassisIDX_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 10, 1, 2),
    _PlatformFanChassisIDX_Type()
)
platformFanChassisIDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformFanChassisIDX.setStatus("current")


class _PlatformFanName_Type(DisplayString):
    """Custom type platformFanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PlatformFanName_Type.__name__ = "DisplayString"
_PlatformFanName_Object = MibTableColumn
platformFanName = _PlatformFanName_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 10, 1, 3),
    _PlatformFanName_Type()
)
platformFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformFanName.setStatus("current")


class _PlatformFanState_Type(Bits):
    """Custom type platformFanState based on Bits"""
    namedValues = NamedValues(
        *(("ok", 0),
          ("failed", 1),
          ("low-nonrecover", 2),
          ("low-critical", 3),
          ("low-noncritical", 4),
          ("high-noncritical", 5),
          ("high-critical", 6),
          ("high-nonrecover", 7))
    )

_PlatformFanState_Type.__name__ = "Bits"
_PlatformFanState_Object = MibTableColumn
platformFanState = _PlatformFanState_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 10, 1, 4),
    _PlatformFanState_Type()
)
platformFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformFanState.setStatus("current")


class _PlatformFanSpeed_Type(Integer32):
    """Custom type platformFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformFanSpeed_Type.__name__ = "Integer32"
_PlatformFanSpeed_Object = MibTableColumn
platformFanSpeed = _PlatformFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 10, 1, 5),
    _PlatformFanSpeed_Type()
)
platformFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformFanSpeed.setStatus("current")
_PlatformTemperatureTable_Object = MibTable
platformTemperatureTable = _PlatformTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 11)
)
if mibBuilder.loadTexts:
    platformTemperatureTable.setStatus("current")
_PlatformTemperatureEntry_Object = MibTableRow
platformTemperatureEntry = _PlatformTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 11, 1)
)
platformTemperatureEntry.setIndexNames(
    (0, "NETSCOUT-HEALTH-MIB", "platformTemperatureIndex"),
)
if mibBuilder.loadTexts:
    platformTemperatureEntry.setStatus("current")


class _PlatformTemperatureIndex_Type(Integer32):
    """Custom type platformTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformTemperatureIndex_Type.__name__ = "Integer32"
_PlatformTemperatureIndex_Object = MibTableColumn
platformTemperatureIndex = _PlatformTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 11, 1, 1),
    _PlatformTemperatureIndex_Type()
)
platformTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformTemperatureIndex.setStatus("current")


class _PlatformTemperatureChassisIDX_Type(Integer32):
    """Custom type platformTemperatureChassisIDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformTemperatureChassisIDX_Type.__name__ = "Integer32"
_PlatformTemperatureChassisIDX_Object = MibTableColumn
platformTemperatureChassisIDX = _PlatformTemperatureChassisIDX_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 11, 1, 2),
    _PlatformTemperatureChassisIDX_Type()
)
platformTemperatureChassisIDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformTemperatureChassisIDX.setStatus("current")


class _PlatformTemperatureName_Type(DisplayString):
    """Custom type platformTemperatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PlatformTemperatureName_Type.__name__ = "DisplayString"
_PlatformTemperatureName_Object = MibTableColumn
platformTemperatureName = _PlatformTemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 11, 1, 3),
    _PlatformTemperatureName_Type()
)
platformTemperatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformTemperatureName.setStatus("current")


class _PlatformTemperatureState_Type(Bits):
    """Custom type platformTemperatureState based on Bits"""
    namedValues = NamedValues(
        *(("ok", 0),
          ("failed", 1),
          ("low-nonrecover", 2),
          ("low-critical", 3),
          ("low-noncritical", 4),
          ("high-noncritical", 5),
          ("high-critical", 6),
          ("high-nonrecover", 7))
    )

_PlatformTemperatureState_Type.__name__ = "Bits"
_PlatformTemperatureState_Object = MibTableColumn
platformTemperatureState = _PlatformTemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 11, 1, 4),
    _PlatformTemperatureState_Type()
)
platformTemperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformTemperatureState.setStatus("current")


class _PlatformTemperatureValue_Type(Integer32):
    """Custom type platformTemperatureValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformTemperatureValue_Type.__name__ = "Integer32"
_PlatformTemperatureValue_Object = MibTableColumn
platformTemperatureValue = _PlatformTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 11, 1, 5),
    _PlatformTemperatureValue_Type()
)
platformTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformTemperatureValue.setStatus("current")
_PlatformVoltagesTable_Object = MibTable
platformVoltagesTable = _PlatformVoltagesTable_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 12)
)
if mibBuilder.loadTexts:
    platformVoltagesTable.setStatus("current")
_PlatformVoltagesEntry_Object = MibTableRow
platformVoltagesEntry = _PlatformVoltagesEntry_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 12, 1)
)
platformVoltagesEntry.setIndexNames(
    (0, "NETSCOUT-HEALTH-MIB", "platformVoltagesIndex"),
)
if mibBuilder.loadTexts:
    platformVoltagesEntry.setStatus("current")


class _PlatformVoltagesIndex_Type(Integer32):
    """Custom type platformVoltagesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformVoltagesIndex_Type.__name__ = "Integer32"
_PlatformVoltagesIndex_Object = MibTableColumn
platformVoltagesIndex = _PlatformVoltagesIndex_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 12, 1, 1),
    _PlatformVoltagesIndex_Type()
)
platformVoltagesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformVoltagesIndex.setStatus("current")


class _PlatformVoltagesChassisIDX_Type(Integer32):
    """Custom type platformVoltagesChassisIDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformVoltagesChassisIDX_Type.__name__ = "Integer32"
_PlatformVoltagesChassisIDX_Object = MibTableColumn
platformVoltagesChassisIDX = _PlatformVoltagesChassisIDX_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 12, 1, 2),
    _PlatformVoltagesChassisIDX_Type()
)
platformVoltagesChassisIDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformVoltagesChassisIDX.setStatus("current")


class _PlatformVoltagesName_Type(DisplayString):
    """Custom type platformVoltagesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PlatformVoltagesName_Type.__name__ = "DisplayString"
_PlatformVoltagesName_Object = MibTableColumn
platformVoltagesName = _PlatformVoltagesName_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 12, 1, 3),
    _PlatformVoltagesName_Type()
)
platformVoltagesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformVoltagesName.setStatus("current")


class _PlatformVoltagesState_Type(Bits):
    """Custom type platformVoltagesState based on Bits"""
    namedValues = NamedValues(
        *(("ok", 0),
          ("failed", 1),
          ("low-nonrecover", 2),
          ("low-critical", 3),
          ("low-noncritical", 4),
          ("high-noncritical", 5),
          ("high-critical", 6),
          ("high-nonrecover", 7))
    )

_PlatformVoltagesState_Type.__name__ = "Bits"
_PlatformVoltagesState_Object = MibTableColumn
platformVoltagesState = _PlatformVoltagesState_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 12, 1, 4),
    _PlatformVoltagesState_Type()
)
platformVoltagesState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformVoltagesState.setStatus("current")


class _PlatformVoltagesValue_Type(Integer32):
    """Custom type platformVoltagesValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformVoltagesValue_Type.__name__ = "Integer32"
_PlatformVoltagesValue_Object = MibTableColumn
platformVoltagesValue = _PlatformVoltagesValue_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 12, 1, 5),
    _PlatformVoltagesValue_Type()
)
platformVoltagesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformVoltagesValue.setStatus("current")
_PlatformNTPTable_Object = MibTable
platformNTPTable = _PlatformNTPTable_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 13)
)
if mibBuilder.loadTexts:
    platformNTPTable.setStatus("current")
_PlatformNTPTableEntry_Object = MibTableRow
platformNTPTableEntry = _PlatformNTPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 13, 1)
)
platformNTPTableEntry.setIndexNames(
    (0, "NETSCOUT-HEALTH-MIB", "platformNTPServerIndex"),
)
if mibBuilder.loadTexts:
    platformNTPTableEntry.setStatus("current")


class _PlatformNTPServerIndex_Type(Integer32):
    """Custom type platformNTPServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformNTPServerIndex_Type.__name__ = "Integer32"
_PlatformNTPServerIndex_Object = MibTableColumn
platformNTPServerIndex = _PlatformNTPServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 13, 1, 1),
    _PlatformNTPServerIndex_Type()
)
platformNTPServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformNTPServerIndex.setStatus("current")
_PlatformNTPIpAddressType_Type = InetAddressType
_PlatformNTPIpAddressType_Object = MibTableColumn
platformNTPIpAddressType = _PlatformNTPIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 13, 1, 2),
    _PlatformNTPIpAddressType_Type()
)
platformNTPIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformNTPIpAddressType.setStatus("current")
_PlatformNTPIpAddress_Type = InetAddress
_PlatformNTPIpAddress_Object = MibTableColumn
platformNTPIpAddress = _PlatformNTPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 13, 1, 3),
    _PlatformNTPIpAddress_Type()
)
platformNTPIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformNTPIpAddress.setStatus("current")
_PlatformIPMITable_Object = MibTable
platformIPMITable = _PlatformIPMITable_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 14)
)
if mibBuilder.loadTexts:
    platformIPMITable.setStatus("current")
_PlatformIPMITableEntry_Object = MibTableRow
platformIPMITableEntry = _PlatformIPMITableEntry_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 14, 1)
)
platformIPMITableEntry.setIndexNames(
    (0, "NETSCOUT-HEALTH-MIB", "platformIPMIIndex"),
)
if mibBuilder.loadTexts:
    platformIPMITableEntry.setStatus("current")


class _PlatformIPMIIndex_Type(Integer32):
    """Custom type platformIPMIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformIPMIIndex_Type.__name__ = "Integer32"
_PlatformIPMIIndex_Object = MibTableColumn
platformIPMIIndex = _PlatformIPMIIndex_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 14, 1, 1),
    _PlatformIPMIIndex_Type()
)
platformIPMIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformIPMIIndex.setStatus("current")
_PlatformIPMIIpAddressType_Type = InetAddressType
_PlatformIPMIIpAddressType_Object = MibTableColumn
platformIPMIIpAddressType = _PlatformIPMIIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 14, 1, 2),
    _PlatformIPMIIpAddressType_Type()
)
platformIPMIIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformIPMIIpAddressType.setStatus("current")
_PlatformIPMIIpAddress_Type = InetAddress
_PlatformIPMIIpAddress_Object = MibTableColumn
platformIPMIIpAddress = _PlatformIPMIIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 14, 1, 3),
    _PlatformIPMIIpAddress_Type()
)
platformIPMIIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformIPMIIpAddress.setStatus("current")


class _PlatformIPMIAddressSource_Type(DisplayString):
    """Custom type platformIPMIAddressSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PlatformIPMIAddressSource_Type.__name__ = "DisplayString"
_PlatformIPMIAddressSource_Object = MibTableColumn
platformIPMIAddressSource = _PlatformIPMIAddressSource_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 14, 1, 4),
    _PlatformIPMIAddressSource_Type()
)
platformIPMIAddressSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformIPMIAddressSource.setStatus("current")
_PlatformIPMISubnetMask_Type = InetAddress
_PlatformIPMISubnetMask_Object = MibTableColumn
platformIPMISubnetMask = _PlatformIPMISubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 14, 1, 5),
    _PlatformIPMISubnetMask_Type()
)
platformIPMISubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformIPMISubnetMask.setStatus("current")
_PlatformIPMISubnetMaskType_Type = InetAddressType
_PlatformIPMISubnetMaskType_Object = MibTableColumn
platformIPMISubnetMaskType = _PlatformIPMISubnetMaskType_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 14, 1, 6),
    _PlatformIPMISubnetMaskType_Type()
)
platformIPMISubnetMaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformIPMISubnetMaskType.setStatus("current")


class _PlatformIPMIMacAddress_Type(DisplayString):
    """Custom type platformIPMIMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PlatformIPMIMacAddress_Type.__name__ = "DisplayString"
_PlatformIPMIMacAddress_Object = MibTableColumn
platformIPMIMacAddress = _PlatformIPMIMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 14, 1, 7),
    _PlatformIPMIMacAddress_Type()
)
platformIPMIMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformIPMIMacAddress.setStatus("current")
_PlatformIPMIGWAddrType_Type = InetAddressType
_PlatformIPMIGWAddrType_Object = MibTableColumn
platformIPMIGWAddrType = _PlatformIPMIGWAddrType_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 14, 1, 8),
    _PlatformIPMIGWAddrType_Type()
)
platformIPMIGWAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformIPMIGWAddrType.setStatus("current")
_PlatformIPMIGWAddr_Type = InetAddress
_PlatformIPMIGWAddr_Object = MibTableColumn
platformIPMIGWAddr = _PlatformIPMIGWAddr_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 14, 1, 9),
    _PlatformIPMIGWAddr_Type()
)
platformIPMIGWAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformIPMIGWAddr.setStatus("current")


class _PlatformIPMIPortRxPkts_Type(Integer32):
    """Custom type platformIPMIPortRxPkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PlatformIPMIPortRxPkts_Type.__name__ = "Integer32"
_PlatformIPMIPortRxPkts_Object = MibTableColumn
platformIPMIPortRxPkts = _PlatformIPMIPortRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 110, 1, 14, 1, 10),
    _PlatformIPMIPortRxPkts_Type()
)
platformIPMIPortRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformIPMIPortRxPkts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCOUT-HEALTH-MIB",
    **{"netscoutHealth": netscoutHealth,
       "platformGroup": platformGroup,
       "platformInformationTable": platformInformationTable,
       "platformInformationEntry": platformInformationEntry,
       "platformInformationIndex": platformInformationIndex,
       "platformProductId": platformProductId,
       "platformModel": platformModel,
       "platformSoftwareVersion": platformSoftwareVersion,
       "platformDecodeVersion": platformDecodeVersion,
       "platformMode": platformMode,
       "platformMACAddress": platformMACAddress,
       "platformIpAddressType": platformIpAddressType,
       "platformIpAddress": platformIpAddress,
       "platformMemory": platformMemory,
       "platformCPU": platformCPU,
       "platformCPUCores": platformCPUCores,
       "platformStatus": platformStatus,
       "platformGatewayIpAddressType": platformGatewayIpAddressType,
       "platformGatewayIpAddress": platformGatewayIpAddress,
       "platformHealthMibVersion": platformHealthMibVersion,
       "platformChassisTable": platformChassisTable,
       "platformChassisEntry": platformChassisEntry,
       "platformChassisIndex": platformChassisIndex,
       "platformChassisType": platformChassisType,
       "platformChassisSN": platformChassisSN,
       "platformControllerTable": platformControllerTable,
       "platformControllerEntry": platformControllerEntry,
       "platformControllerIndex": platformControllerIndex,
       "platformControllerState": platformControllerState,
       "platformControllerModel": platformControllerModel,
       "platformControllerFirwareRev": platformControllerFirwareRev,
       "platformControllerSerial": platformControllerSerial,
       "platformControllerSEDState": platformControllerSEDState,
       "platformRAIDArrayTable": platformRAIDArrayTable,
       "platformRAIDArrayEntry": platformRAIDArrayEntry,
       "platformRAIDArrayIndex": platformRAIDArrayIndex,
       "platformControllerIDX": platformControllerIDX,
       "platformRAIDArrayName": platformRAIDArrayName,
       "platformRAIDArrayState": platformRAIDArrayState,
       "platformRAIDArrayProgress": platformRAIDArrayProgress,
       "platformRAIDArrayType": platformRAIDArrayType,
       "platformRAIDArrayFormat": platformRAIDArrayFormat,
       "platformRAIDArraySize": platformRAIDArraySize,
       "platformRAIDArrayDrives": platformRAIDArrayDrives,
       "platformRAIDArraySEDState": platformRAIDArraySEDState,
       "platformDiskTable": platformDiskTable,
       "platformDiskEntry": platformDiskEntry,
       "platformDiskIndex": platformDiskIndex,
       "platformRAIDArrayIDX": platformRAIDArrayIDX,
       "platformDiskChassisIDX": platformDiskChassisIDX,
       "platformDiskName": platformDiskName,
       "platformDiskType": platformDiskType,
       "platformDiskState": platformDiskState,
       "platformDiskModel": platformDiskModel,
       "platformDiskSize": platformDiskSize,
       "platformDiskFirmware": platformDiskFirmware,
       "platformDiskSlot": platformDiskSlot,
       "platformDiskSEDState": platformDiskSEDState,
       "platformPowerSupplyTable": platformPowerSupplyTable,
       "platformPowerSupplyEntry": platformPowerSupplyEntry,
       "platformPowerSupplyIndex": platformPowerSupplyIndex,
       "platformChassisIDX": platformChassisIDX,
       "platformPowerSupplyState": platformPowerSupplyState,
       "platformPowerSupplyName": platformPowerSupplyName,
       "platformMonitorIfTable": platformMonitorIfTable,
       "platformMonitorIfEntry": platformMonitorIfEntry,
       "platformMonitorIfIndex": platformMonitorIfIndex,
       "platforMonitorIfTableIDX": platforMonitorIfTableIDX,
       "platformMonitorIfType": platformMonitorIfType,
       "platformMonitorIFXcvrType": platformMonitorIFXcvrType,
       "platformMonitorIfState": platformMonitorIfState,
       "platformMonitorIfRxPwr": platformMonitorIfRxPwr,
       "platformMonitorIfName": platformMonitorIfName,
       "platformMgmtIfTable": platformMgmtIfTable,
       "platformMgmtIfEntry": platformMgmtIfEntry,
       "platformMgmtIfIndex": platformMgmtIfIndex,
       "platformMgmtIfName": platformMgmtIfName,
       "platformMgmtIfState": platformMgmtIfState,
       "platformFanTable": platformFanTable,
       "platformFanEntry": platformFanEntry,
       "platformFanIndex": platformFanIndex,
       "platformFanChassisIDX": platformFanChassisIDX,
       "platformFanName": platformFanName,
       "platformFanState": platformFanState,
       "platformFanSpeed": platformFanSpeed,
       "platformTemperatureTable": platformTemperatureTable,
       "platformTemperatureEntry": platformTemperatureEntry,
       "platformTemperatureIndex": platformTemperatureIndex,
       "platformTemperatureChassisIDX": platformTemperatureChassisIDX,
       "platformTemperatureName": platformTemperatureName,
       "platformTemperatureState": platformTemperatureState,
       "platformTemperatureValue": platformTemperatureValue,
       "platformVoltagesTable": platformVoltagesTable,
       "platformVoltagesEntry": platformVoltagesEntry,
       "platformVoltagesIndex": platformVoltagesIndex,
       "platformVoltagesChassisIDX": platformVoltagesChassisIDX,
       "platformVoltagesName": platformVoltagesName,
       "platformVoltagesState": platformVoltagesState,
       "platformVoltagesValue": platformVoltagesValue,
       "platformNTPTable": platformNTPTable,
       "platformNTPTableEntry": platformNTPTableEntry,
       "platformNTPServerIndex": platformNTPServerIndex,
       "platformNTPIpAddressType": platformNTPIpAddressType,
       "platformNTPIpAddress": platformNTPIpAddress,
       "platformIPMITable": platformIPMITable,
       "platformIPMITableEntry": platformIPMITableEntry,
       "platformIPMIIndex": platformIPMIIndex,
       "platformIPMIIpAddressType": platformIPMIIpAddressType,
       "platformIPMIIpAddress": platformIPMIIpAddress,
       "platformIPMIAddressSource": platformIPMIAddressSource,
       "platformIPMISubnetMask": platformIPMISubnetMask,
       "platformIPMISubnetMaskType": platformIPMISubnetMaskType,
       "platformIPMIMacAddress": platformIPMIMacAddress,
       "platformIPMIGWAddrType": platformIPMIGWAddrType,
       "platformIPMIGWAddr": platformIPMIGWAddr,
       "platformIPMIPortRxPkts": platformIPMIPortRxPkts}
)

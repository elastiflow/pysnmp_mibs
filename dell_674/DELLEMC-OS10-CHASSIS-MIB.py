# SNMP MIB module (DELLEMC-OS10-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/dell_674/DELLEMC-OS10-CHASSIS-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 16:03:24 2025
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

(os10,) = mibBuilder.importSymbols(
    "DELLEMC-OS10-SMI-MIB",
    "os10")

(Os10CardOperStatus,
 Os10ChassisDefType,
 Os10CmnOperStatus,
 Os10DeviceType,
 Os10SystemCardType) = mibBuilder.importSymbols(
    "DELLEMC-OS10-TC-MIB",
    "Os10CardOperStatus",
    "Os10ChassisDefType",
    "Os10CmnOperStatus",
    "Os10DeviceType",
    "Os10SystemCardType")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

os10ChassisMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4)
)
if mibBuilder.loadTexts:
    os10ChassisMib.setRevisions(
        ("2017-06-21 12:00",
         "2017-01-25 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Os10SysObject_ObjectIdentity = ObjectIdentity
os10SysObject = _Os10SysObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1)
)
_Os10ChassisObject_ObjectIdentity = ObjectIdentity
os10ChassisObject = _Os10ChassisObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1)
)
_Os10NumChassis_Type = Unsigned32
_Os10NumChassis_Object = MibScalar
os10NumChassis = _Os10NumChassis_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 1),
    _Os10NumChassis_Type()
)
os10NumChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10NumChassis.setStatus("current")
_Os10MaxNumChassis_Type = Unsigned32
_Os10MaxNumChassis_Object = MibScalar
os10MaxNumChassis = _Os10MaxNumChassis_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 2),
    _Os10MaxNumChassis_Type()
)
os10MaxNumChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10MaxNumChassis.setStatus("current")
_Os10ChassisTable_Object = MibTable
os10ChassisTable = _Os10ChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    os10ChassisTable.setStatus("current")
_Os10ChassisEntry_Object = MibTableRow
os10ChassisEntry = _Os10ChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 3, 1)
)
os10ChassisEntry.setIndexNames(
    (0, "DELLEMC-OS10-CHASSIS-MIB", "os10ChassisIndex"),
)
if mibBuilder.loadTexts:
    os10ChassisEntry.setStatus("current")
_Os10ChassisIndex_Type = Unsigned32
_Os10ChassisIndex_Object = MibTableColumn
os10ChassisIndex = _Os10ChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 3, 1, 1),
    _Os10ChassisIndex_Type()
)
os10ChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    os10ChassisIndex.setStatus("current")
_Os10ChassisType_Type = Os10ChassisDefType
_Os10ChassisType_Object = MibTableColumn
os10ChassisType = _Os10ChassisType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 3, 1, 2),
    _Os10ChassisType_Type()
)
os10ChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10ChassisType.setStatus("current")
_Os10ChassisMacAddr_Type = MacAddress
_Os10ChassisMacAddr_Object = MibTableColumn
os10ChassisMacAddr = _Os10ChassisMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 3, 1, 3),
    _Os10ChassisMacAddr_Type()
)
os10ChassisMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10ChassisMacAddr.setStatus("current")


class _Os10ChassisPartNum_Type(DisplayString):
    """Custom type os10ChassisPartNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_Os10ChassisPartNum_Type.__name__ = "DisplayString"
_Os10ChassisPartNum_Object = MibTableColumn
os10ChassisPartNum = _Os10ChassisPartNum_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 3, 1, 4),
    _Os10ChassisPartNum_Type()
)
os10ChassisPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10ChassisPartNum.setStatus("current")


class _Os10ChassisPPID_Type(DisplayString):
    """Custom type os10ChassisPPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Os10ChassisPPID_Type.__name__ = "DisplayString"
_Os10ChassisPPID_Object = MibTableColumn
os10ChassisPPID = _Os10ChassisPPID_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 3, 1, 5),
    _Os10ChassisPPID_Type()
)
os10ChassisPPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10ChassisPPID.setStatus("current")


class _Os10ChassisHwRev_Type(DisplayString):
    """Custom type os10ChassisHwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Os10ChassisHwRev_Type.__name__ = "DisplayString"
_Os10ChassisHwRev_Object = MibTableColumn
os10ChassisHwRev = _Os10ChassisHwRev_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 3, 1, 6),
    _Os10ChassisHwRev_Type()
)
os10ChassisHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10ChassisHwRev.setStatus("current")


class _Os10ChassisServiceTag_Type(DisplayString):
    """Custom type os10ChassisServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_Os10ChassisServiceTag_Type.__name__ = "DisplayString"
_Os10ChassisServiceTag_Object = MibTableColumn
os10ChassisServiceTag = _Os10ChassisServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 3, 1, 7),
    _Os10ChassisServiceTag_Type()
)
os10ChassisServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10ChassisServiceTag.setStatus("current")


class _Os10ChassisExpServiceCode_Type(DisplayString):
    """Custom type os10ChassisExpServiceCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Os10ChassisExpServiceCode_Type.__name__ = "DisplayString"
_Os10ChassisExpServiceCode_Object = MibTableColumn
os10ChassisExpServiceCode = _Os10ChassisExpServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 3, 1, 8),
    _Os10ChassisExpServiceCode_Type()
)
os10ChassisExpServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10ChassisExpServiceCode.setStatus("current")
_Os10ChassisNumFanTrays_Type = Unsigned32
_Os10ChassisNumFanTrays_Object = MibTableColumn
os10ChassisNumFanTrays = _Os10ChassisNumFanTrays_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 3, 1, 9),
    _Os10ChassisNumFanTrays_Type()
)
os10ChassisNumFanTrays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10ChassisNumFanTrays.setStatus("current")
_Os10ChassisNumPowerSupplies_Type = Unsigned32
_Os10ChassisNumPowerSupplies_Object = MibTableColumn
os10ChassisNumPowerSupplies = _Os10ChassisNumPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 3, 1, 10),
    _Os10ChassisNumPowerSupplies_Type()
)
os10ChassisNumPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10ChassisNumPowerSupplies.setStatus("current")
_Os10ChassisTemp_Type = Integer32
_Os10ChassisTemp_Object = MibTableColumn
os10ChassisTemp = _Os10ChassisTemp_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 3, 1, 11),
    _Os10ChassisTemp_Type()
)
os10ChassisTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10ChassisTemp.setStatus("current")
if mibBuilder.loadTexts:
    os10ChassisTemp.setUnits("degrees Centigrade")


class _Os10ChassisProductBase_Type(DisplayString):
    """Custom type os10ChassisProductBase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Os10ChassisProductBase_Type.__name__ = "DisplayString"
_Os10ChassisProductBase_Object = MibTableColumn
os10ChassisProductBase = _Os10ChassisProductBase_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 3, 1, 12),
    _Os10ChassisProductBase_Type()
)
os10ChassisProductBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10ChassisProductBase.setStatus("current")


class _Os10ChassisProductSN_Type(DisplayString):
    """Custom type os10ChassisProductSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Os10ChassisProductSN_Type.__name__ = "DisplayString"
_Os10ChassisProductSN_Object = MibTableColumn
os10ChassisProductSN = _Os10ChassisProductSN_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 3, 1, 13),
    _Os10ChassisProductSN_Type()
)
os10ChassisProductSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10ChassisProductSN.setStatus("current")


class _Os10ChassisProductPN_Type(DisplayString):
    """Custom type os10ChassisProductPN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Os10ChassisProductPN_Type.__name__ = "DisplayString"
_Os10ChassisProductPN_Object = MibTableColumn
os10ChassisProductPN = _Os10ChassisProductPN_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 3, 1, 14),
    _Os10ChassisProductPN_Type()
)
os10ChassisProductPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10ChassisProductPN.setStatus("current")
_Os10CardTable_Object = MibTable
os10CardTable = _Os10CardTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    os10CardTable.setStatus("current")
_Os10CardEntry_Object = MibTableRow
os10CardEntry = _Os10CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 4, 1)
)
os10CardEntry.setIndexNames(
    (0, "DELLEMC-OS10-CHASSIS-MIB", "os10ChassisIndex"),
    (0, "DELLEMC-OS10-CHASSIS-MIB", "os10CardIndex"),
)
if mibBuilder.loadTexts:
    os10CardEntry.setStatus("current")
_Os10CardIndex_Type = Unsigned32
_Os10CardIndex_Object = MibTableColumn
os10CardIndex = _Os10CardIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 4, 1, 1),
    _Os10CardIndex_Type()
)
os10CardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    os10CardIndex.setStatus("current")
_Os10CardType_Type = Os10SystemCardType
_Os10CardType_Object = MibTableColumn
os10CardType = _Os10CardType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 4, 1, 2),
    _Os10CardType_Type()
)
os10CardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10CardType.setStatus("current")


class _Os10CardDescription_Type(DisplayString):
    """Custom type os10CardDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_Os10CardDescription_Type.__name__ = "DisplayString"
_Os10CardDescription_Object = MibTableColumn
os10CardDescription = _Os10CardDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 4, 1, 3),
    _Os10CardDescription_Type()
)
os10CardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10CardDescription.setStatus("current")
_Os10CardStatus_Type = Os10CardOperStatus
_Os10CardStatus_Object = MibTableColumn
os10CardStatus = _Os10CardStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 4, 1, 4),
    _Os10CardStatus_Type()
)
os10CardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10CardStatus.setStatus("current")
_Os10CardTemp_Type = Integer32
_Os10CardTemp_Object = MibTableColumn
os10CardTemp = _Os10CardTemp_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 4, 1, 5),
    _Os10CardTemp_Type()
)
os10CardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10CardTemp.setStatus("current")
if mibBuilder.loadTexts:
    os10CardTemp.setUnits("degrees Centigrade")


class _Os10CardPartNum_Type(DisplayString):
    """Custom type os10CardPartNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_Os10CardPartNum_Type.__name__ = "DisplayString"
_Os10CardPartNum_Object = MibTableColumn
os10CardPartNum = _Os10CardPartNum_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 4, 1, 6),
    _Os10CardPartNum_Type()
)
os10CardPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10CardPartNum.setStatus("current")


class _Os10CardPPID_Type(DisplayString):
    """Custom type os10CardPPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Os10CardPPID_Type.__name__ = "DisplayString"
_Os10CardPPID_Object = MibTableColumn
os10CardPPID = _Os10CardPPID_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 4, 1, 7),
    _Os10CardPPID_Type()
)
os10CardPPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10CardPPID.setStatus("current")


class _Os10CardHwRev_Type(DisplayString):
    """Custom type os10CardHwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Os10CardHwRev_Type.__name__ = "DisplayString"
_Os10CardHwRev_Object = MibTableColumn
os10CardHwRev = _Os10CardHwRev_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 4, 1, 8),
    _Os10CardHwRev_Type()
)
os10CardHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10CardHwRev.setStatus("current")


class _Os10CardServiceTag_Type(DisplayString):
    """Custom type os10CardServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_Os10CardServiceTag_Type.__name__ = "DisplayString"
_Os10CardServiceTag_Object = MibTableColumn
os10CardServiceTag = _Os10CardServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 4, 1, 9),
    _Os10CardServiceTag_Type()
)
os10CardServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10CardServiceTag.setStatus("current")


class _Os10CardExpServiceCode_Type(DisplayString):
    """Custom type os10CardExpServiceCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Os10CardExpServiceCode_Type.__name__ = "DisplayString"
_Os10CardExpServiceCode_Object = MibTableColumn
os10CardExpServiceCode = _Os10CardExpServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 1, 4, 1, 10),
    _Os10CardExpServiceCode_Type()
)
os10CardExpServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10CardExpServiceCode.setStatus("current")
_Os10SystemComponent_ObjectIdentity = ObjectIdentity
os10SystemComponent = _Os10SystemComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2)
)
_Os10PowerSupplyTable_Object = MibTable
os10PowerSupplyTable = _Os10PowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    os10PowerSupplyTable.setStatus("current")
_Os10PowerSupplyEntry_Object = MibTableRow
os10PowerSupplyEntry = _Os10PowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 1, 1)
)
os10PowerSupplyEntry.setIndexNames(
    (0, "DELLEMC-OS10-CHASSIS-MIB", "os10PowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    os10PowerSupplyEntry.setStatus("current")
_Os10PowerSupplyIndex_Type = Unsigned32
_Os10PowerSupplyIndex_Object = MibTableColumn
os10PowerSupplyIndex = _Os10PowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 1, 1, 1),
    _Os10PowerSupplyIndex_Type()
)
os10PowerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    os10PowerSupplyIndex.setStatus("current")
_Os10PowerSupplyDevice_Type = Os10DeviceType
_Os10PowerSupplyDevice_Object = MibTableColumn
os10PowerSupplyDevice = _Os10PowerSupplyDevice_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 1, 1, 2),
    _Os10PowerSupplyDevice_Type()
)
os10PowerSupplyDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10PowerSupplyDevice.setStatus("current")
_Os10PowerSupplyDeviceIndex_Type = Unsigned32
_Os10PowerSupplyDeviceIndex_Object = MibTableColumn
os10PowerSupplyDeviceIndex = _Os10PowerSupplyDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 1, 1, 3),
    _Os10PowerSupplyDeviceIndex_Type()
)
os10PowerSupplyDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10PowerSupplyDeviceIndex.setStatus("current")
_Os10PowerSupplyOperStatus_Type = Os10CmnOperStatus
_Os10PowerSupplyOperStatus_Object = MibTableColumn
os10PowerSupplyOperStatus = _Os10PowerSupplyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 1, 1, 4),
    _Os10PowerSupplyOperStatus_Type()
)
os10PowerSupplyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10PowerSupplyOperStatus.setStatus("current")


class _Os10PowerSupplyType_Type(Integer32):
    """Custom type os10PowerSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ac", 2),
          ("dc", 3))
    )


_Os10PowerSupplyType_Type.__name__ = "Integer32"
_Os10PowerSupplyType_Object = MibTableColumn
os10PowerSupplyType = _Os10PowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 1, 1, 5),
    _Os10PowerSupplyType_Type()
)
os10PowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10PowerSupplyType.setStatus("current")


class _Os10PowerSupplyPPID_Type(DisplayString):
    """Custom type os10PowerSupplyPPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Os10PowerSupplyPPID_Type.__name__ = "DisplayString"
_Os10PowerSupplyPPID_Object = MibTableColumn
os10PowerSupplyPPID = _Os10PowerSupplyPPID_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 1, 1, 6),
    _Os10PowerSupplyPPID_Type()
)
os10PowerSupplyPPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10PowerSupplyPPID.setStatus("current")


class _Os10PowerSupplyServiceTag_Type(DisplayString):
    """Custom type os10PowerSupplyServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_Os10PowerSupplyServiceTag_Type.__name__ = "DisplayString"
_Os10PowerSupplyServiceTag_Object = MibTableColumn
os10PowerSupplyServiceTag = _Os10PowerSupplyServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 1, 1, 7),
    _Os10PowerSupplyServiceTag_Type()
)
os10PowerSupplyServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10PowerSupplyServiceTag.setStatus("current")


class _Os10PowerSupplyExpServiceCode_Type(DisplayString):
    """Custom type os10PowerSupplyExpServiceCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Os10PowerSupplyExpServiceCode_Type.__name__ = "DisplayString"
_Os10PowerSupplyExpServiceCode_Object = MibTableColumn
os10PowerSupplyExpServiceCode = _Os10PowerSupplyExpServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 1, 1, 8),
    _Os10PowerSupplyExpServiceCode_Type()
)
os10PowerSupplyExpServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10PowerSupplyExpServiceCode.setStatus("current")
_Os10FanTrayTable_Object = MibTable
os10FanTrayTable = _Os10FanTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    os10FanTrayTable.setStatus("current")
_Os10FanTrayEntry_Object = MibTableRow
os10FanTrayEntry = _Os10FanTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 2, 1)
)
os10FanTrayEntry.setIndexNames(
    (0, "DELLEMC-OS10-CHASSIS-MIB", "os10FanTrayIndex"),
)
if mibBuilder.loadTexts:
    os10FanTrayEntry.setStatus("current")
_Os10FanTrayIndex_Type = Unsigned32
_Os10FanTrayIndex_Object = MibTableColumn
os10FanTrayIndex = _Os10FanTrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 2, 1, 1),
    _Os10FanTrayIndex_Type()
)
os10FanTrayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    os10FanTrayIndex.setStatus("current")
_Os10FanTrayDevice_Type = Os10DeviceType
_Os10FanTrayDevice_Object = MibTableColumn
os10FanTrayDevice = _Os10FanTrayDevice_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 2, 1, 2),
    _Os10FanTrayDevice_Type()
)
os10FanTrayDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10FanTrayDevice.setStatus("current")
_Os10FanTrayDeviceIndex_Type = Unsigned32
_Os10FanTrayDeviceIndex_Object = MibTableColumn
os10FanTrayDeviceIndex = _Os10FanTrayDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 2, 1, 3),
    _Os10FanTrayDeviceIndex_Type()
)
os10FanTrayDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10FanTrayDeviceIndex.setStatus("current")
_Os10FanTrayOperStatus_Type = Os10CmnOperStatus
_Os10FanTrayOperStatus_Object = MibTableColumn
os10FanTrayOperStatus = _Os10FanTrayOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 2, 1, 4),
    _Os10FanTrayOperStatus_Type()
)
os10FanTrayOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10FanTrayOperStatus.setStatus("current")


class _Os10FanTrayPPID_Type(DisplayString):
    """Custom type os10FanTrayPPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Os10FanTrayPPID_Type.__name__ = "DisplayString"
_Os10FanTrayPPID_Object = MibTableColumn
os10FanTrayPPID = _Os10FanTrayPPID_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 2, 1, 5),
    _Os10FanTrayPPID_Type()
)
os10FanTrayPPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10FanTrayPPID.setStatus("current")


class _Os10FanTrayServiceTag_Type(DisplayString):
    """Custom type os10FanTrayServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_Os10FanTrayServiceTag_Type.__name__ = "DisplayString"
_Os10FanTrayServiceTag_Object = MibTableColumn
os10FanTrayServiceTag = _Os10FanTrayServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 2, 1, 6),
    _Os10FanTrayServiceTag_Type()
)
os10FanTrayServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10FanTrayServiceTag.setStatus("current")


class _Os10FanTrayExpServiceCode_Type(DisplayString):
    """Custom type os10FanTrayExpServiceCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Os10FanTrayExpServiceCode_Type.__name__ = "DisplayString"
_Os10FanTrayExpServiceCode_Object = MibTableColumn
os10FanTrayExpServiceCode = _Os10FanTrayExpServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 2, 1, 7),
    _Os10FanTrayExpServiceCode_Type()
)
os10FanTrayExpServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10FanTrayExpServiceCode.setStatus("current")
_Os10FanTable_Object = MibTable
os10FanTable = _Os10FanTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    os10FanTable.setStatus("current")
_Os10FanEntry_Object = MibTableRow
os10FanEntry = _Os10FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 3, 1)
)
os10FanEntry.setIndexNames(
    (0, "DELLEMC-OS10-CHASSIS-MIB", "os10FanIndex"),
)
if mibBuilder.loadTexts:
    os10FanEntry.setStatus("current")
_Os10FanIndex_Type = Unsigned32
_Os10FanIndex_Object = MibTableColumn
os10FanIndex = _Os10FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 3, 1, 1),
    _Os10FanIndex_Type()
)
os10FanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    os10FanIndex.setStatus("current")
_Os10FanDevice_Type = Os10DeviceType
_Os10FanDevice_Object = MibTableColumn
os10FanDevice = _Os10FanDevice_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 3, 1, 2),
    _Os10FanDevice_Type()
)
os10FanDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10FanDevice.setStatus("current")
_Os10FanDeviceIndex_Type = Unsigned32
_Os10FanDeviceIndex_Object = MibTableColumn
os10FanDeviceIndex = _Os10FanDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 3, 1, 3),
    _Os10FanDeviceIndex_Type()
)
os10FanDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10FanDeviceIndex.setStatus("current")


class _Os10FanEntity_Type(Integer32):
    """Custom type os10FanEntity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("psu", 1),
          ("fanTray", 2))
    )


_Os10FanEntity_Type.__name__ = "Integer32"
_Os10FanEntity_Object = MibTableColumn
os10FanEntity = _Os10FanEntity_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 3, 1, 4),
    _Os10FanEntity_Type()
)
os10FanEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10FanEntity.setStatus("current")
_Os10FanEntitySlot_Type = Unsigned32
_Os10FanEntitySlot_Object = MibTableColumn
os10FanEntitySlot = _Os10FanEntitySlot_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 3, 1, 5),
    _Os10FanEntitySlot_Type()
)
os10FanEntitySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10FanEntitySlot.setStatus("current")
_Os10FanId_Type = Unsigned32
_Os10FanId_Object = MibTableColumn
os10FanId = _Os10FanId_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 3, 1, 6),
    _Os10FanId_Type()
)
os10FanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10FanId.setStatus("current")
_Os10FanOperStatus_Type = Os10CmnOperStatus
_Os10FanOperStatus_Object = MibTableColumn
os10FanOperStatus = _Os10FanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 2, 3, 1, 7),
    _Os10FanOperStatus_Type()
)
os10FanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10FanOperStatus.setStatus("current")
_Os10AlmObjects_ObjectIdentity = ObjectIdentity
os10AlmObjects = _Os10AlmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3)
)
_Os10AlmMibNotifications_ObjectIdentity = ObjectIdentity
os10AlmMibNotifications = _Os10AlmMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 1)
)
_Os10AlmVariable_ObjectIdentity = ObjectIdentity
os10AlmVariable = _Os10AlmVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 2)
)
_Os10AlmVarInteger_Type = Integer32
_Os10AlmVarInteger_Object = MibScalar
os10AlmVarInteger = _Os10AlmVarInteger_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 2, 1),
    _Os10AlmVarInteger_Type()
)
os10AlmVarInteger.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    os10AlmVarInteger.setStatus("current")


class _Os10AlmVarString_Type(OctetString):
    """Custom type os10AlmVarString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Os10AlmVarString_Type.__name__ = "OctetString"
_Os10AlmVarString_Object = MibScalar
os10AlmVarString = _Os10AlmVarString_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 2, 2),
    _Os10AlmVarString_Type()
)
os10AlmVarString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    os10AlmVarString.setStatus("current")
_Os10AlmVarChassisId_Type = Integer32
_Os10AlmVarChassisId_Object = MibScalar
os10AlmVarChassisId = _Os10AlmVarChassisId_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 2, 3),
    _Os10AlmVarChassisId_Type()
)
os10AlmVarChassisId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    os10AlmVarChassisId.setStatus("current")
_Os10AlmVarSlot_Type = Integer32
_Os10AlmVarSlot_Object = MibScalar
os10AlmVarSlot = _Os10AlmVarSlot_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 2, 4),
    _Os10AlmVarSlot_Type()
)
os10AlmVarSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    os10AlmVarSlot.setStatus("current")
_Os10AlmVarPort_Type = Integer32
_Os10AlmVarPort_Object = MibScalar
os10AlmVarPort = _Os10AlmVarPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 2, 5),
    _Os10AlmVarPort_Type()
)
os10AlmVarPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    os10AlmVarPort.setStatus("current")

# Managed Objects groups


# Notification objects

os10AlmMinorTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 1, 1)
)
os10AlmMinorTempHigh.setObjects(
      *(("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarInteger"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarString"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarChassisId"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarSlot"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarPort"))
)
if mibBuilder.loadTexts:
    os10AlmMinorTempHigh.setStatus(
        "current"
    )

os10AlmMinorTempClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 1, 2)
)
os10AlmMinorTempClr.setObjects(
      *(("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarInteger"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarString"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarChassisId"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarSlot"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarPort"))
)
if mibBuilder.loadTexts:
    os10AlmMinorTempClr.setStatus(
        "current"
    )

os10AlmMajorTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 1, 3)
)
os10AlmMajorTempHigh.setObjects(
      *(("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarInteger"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarString"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarChassisId"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarSlot"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarPort"))
)
if mibBuilder.loadTexts:
    os10AlmMajorTempHigh.setStatus(
        "current"
    )

os10AlmMajorTempClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 1, 4)
)
os10AlmMajorTempClr.setObjects(
      *(("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarInteger"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarString"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarChassisId"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarSlot"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarPort"))
)
if mibBuilder.loadTexts:
    os10AlmMajorTempClr.setStatus(
        "current"
    )

os10AlmPowerSupplyDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 1, 5)
)
os10AlmPowerSupplyDown.setObjects(
      *(("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarInteger"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarString"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarChassisId"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarSlot"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarPort"))
)
if mibBuilder.loadTexts:
    os10AlmPowerSupplyDown.setStatus(
        "current"
    )

os10AlmPowerSupplyClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 1, 6)
)
os10AlmPowerSupplyClr.setObjects(
      *(("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarInteger"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarString"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarChassisId"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarSlot"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarPort"))
)
if mibBuilder.loadTexts:
    os10AlmPowerSupplyClr.setStatus(
        "current"
    )

os10AlmMajorPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 1, 7)
)
os10AlmMajorPowerSupply.setObjects(
      *(("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarInteger"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarString"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarChassisId"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarSlot"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarPort"))
)
if mibBuilder.loadTexts:
    os10AlmMajorPowerSupply.setStatus(
        "current"
    )

os10AlmMajorPowerSupplyClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 1, 8)
)
os10AlmMajorPowerSupplyClr.setObjects(
      *(("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarInteger"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarString"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarChassisId"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarSlot"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarPort"))
)
if mibBuilder.loadTexts:
    os10AlmMajorPowerSupplyClr.setStatus(
        "current"
    )

os10AlmMinorPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 1, 9)
)
os10AlmMinorPowerSupply.setObjects(
      *(("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarInteger"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarString"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarChassisId"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarSlot"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarPort"))
)
if mibBuilder.loadTexts:
    os10AlmMinorPowerSupply.setStatus(
        "current"
    )

os10AlmMinorPowerSupplyClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 1, 10)
)
os10AlmMinorPowerSupplyClr.setObjects(
      *(("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarInteger"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarString"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarChassisId"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarSlot"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarPort"))
)
if mibBuilder.loadTexts:
    os10AlmMinorPowerSupplyClr.setStatus(
        "current"
    )

os10AlmFanTrayDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 1, 11)
)
os10AlmFanTrayDown.setObjects(
      *(("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarInteger"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarString"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarChassisId"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarSlot"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarPort"))
)
if mibBuilder.loadTexts:
    os10AlmFanTrayDown.setStatus(
        "current"
    )

os10AlmFanTrayClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 1, 12)
)
os10AlmFanTrayClr.setObjects(
      *(("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarInteger"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarString"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarChassisId"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarSlot"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarPort"))
)
if mibBuilder.loadTexts:
    os10AlmFanTrayClr.setStatus(
        "current"
    )

os10AlmMinorFanTray = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 1, 13)
)
os10AlmMinorFanTray.setObjects(
      *(("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarInteger"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarString"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarChassisId"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarSlot"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarPort"))
)
if mibBuilder.loadTexts:
    os10AlmMinorFanTray.setStatus(
        "current"
    )

os10AlmMinorFanTrayClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 4, 1, 3, 1, 14)
)
os10AlmMinorFanTrayClr.setObjects(
      *(("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarInteger"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarString"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarChassisId"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarSlot"),
        ("DELLEMC-OS10-CHASSIS-MIB", "os10AlmVarPort"))
)
if mibBuilder.loadTexts:
    os10AlmMinorFanTrayClr.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELLEMC-OS10-CHASSIS-MIB",
    **{"os10ChassisMib": os10ChassisMib,
       "os10SysObject": os10SysObject,
       "os10ChassisObject": os10ChassisObject,
       "os10NumChassis": os10NumChassis,
       "os10MaxNumChassis": os10MaxNumChassis,
       "os10ChassisTable": os10ChassisTable,
       "os10ChassisEntry": os10ChassisEntry,
       "os10ChassisIndex": os10ChassisIndex,
       "os10ChassisType": os10ChassisType,
       "os10ChassisMacAddr": os10ChassisMacAddr,
       "os10ChassisPartNum": os10ChassisPartNum,
       "os10ChassisPPID": os10ChassisPPID,
       "os10ChassisHwRev": os10ChassisHwRev,
       "os10ChassisServiceTag": os10ChassisServiceTag,
       "os10ChassisExpServiceCode": os10ChassisExpServiceCode,
       "os10ChassisNumFanTrays": os10ChassisNumFanTrays,
       "os10ChassisNumPowerSupplies": os10ChassisNumPowerSupplies,
       "os10ChassisTemp": os10ChassisTemp,
       "os10ChassisProductBase": os10ChassisProductBase,
       "os10ChassisProductSN": os10ChassisProductSN,
       "os10ChassisProductPN": os10ChassisProductPN,
       "os10CardTable": os10CardTable,
       "os10CardEntry": os10CardEntry,
       "os10CardIndex": os10CardIndex,
       "os10CardType": os10CardType,
       "os10CardDescription": os10CardDescription,
       "os10CardStatus": os10CardStatus,
       "os10CardTemp": os10CardTemp,
       "os10CardPartNum": os10CardPartNum,
       "os10CardPPID": os10CardPPID,
       "os10CardHwRev": os10CardHwRev,
       "os10CardServiceTag": os10CardServiceTag,
       "os10CardExpServiceCode": os10CardExpServiceCode,
       "os10SystemComponent": os10SystemComponent,
       "os10PowerSupplyTable": os10PowerSupplyTable,
       "os10PowerSupplyEntry": os10PowerSupplyEntry,
       "os10PowerSupplyIndex": os10PowerSupplyIndex,
       "os10PowerSupplyDevice": os10PowerSupplyDevice,
       "os10PowerSupplyDeviceIndex": os10PowerSupplyDeviceIndex,
       "os10PowerSupplyOperStatus": os10PowerSupplyOperStatus,
       "os10PowerSupplyType": os10PowerSupplyType,
       "os10PowerSupplyPPID": os10PowerSupplyPPID,
       "os10PowerSupplyServiceTag": os10PowerSupplyServiceTag,
       "os10PowerSupplyExpServiceCode": os10PowerSupplyExpServiceCode,
       "os10FanTrayTable": os10FanTrayTable,
       "os10FanTrayEntry": os10FanTrayEntry,
       "os10FanTrayIndex": os10FanTrayIndex,
       "os10FanTrayDevice": os10FanTrayDevice,
       "os10FanTrayDeviceIndex": os10FanTrayDeviceIndex,
       "os10FanTrayOperStatus": os10FanTrayOperStatus,
       "os10FanTrayPPID": os10FanTrayPPID,
       "os10FanTrayServiceTag": os10FanTrayServiceTag,
       "os10FanTrayExpServiceCode": os10FanTrayExpServiceCode,
       "os10FanTable": os10FanTable,
       "os10FanEntry": os10FanEntry,
       "os10FanIndex": os10FanIndex,
       "os10FanDevice": os10FanDevice,
       "os10FanDeviceIndex": os10FanDeviceIndex,
       "os10FanEntity": os10FanEntity,
       "os10FanEntitySlot": os10FanEntitySlot,
       "os10FanId": os10FanId,
       "os10FanOperStatus": os10FanOperStatus,
       "os10AlmObjects": os10AlmObjects,
       "os10AlmMibNotifications": os10AlmMibNotifications,
       "os10AlmMinorTempHigh": os10AlmMinorTempHigh,
       "os10AlmMinorTempClr": os10AlmMinorTempClr,
       "os10AlmMajorTempHigh": os10AlmMajorTempHigh,
       "os10AlmMajorTempClr": os10AlmMajorTempClr,
       "os10AlmPowerSupplyDown": os10AlmPowerSupplyDown,
       "os10AlmPowerSupplyClr": os10AlmPowerSupplyClr,
       "os10AlmMajorPowerSupply": os10AlmMajorPowerSupply,
       "os10AlmMajorPowerSupplyClr": os10AlmMajorPowerSupplyClr,
       "os10AlmMinorPowerSupply": os10AlmMinorPowerSupply,
       "os10AlmMinorPowerSupplyClr": os10AlmMinorPowerSupplyClr,
       "os10AlmFanTrayDown": os10AlmFanTrayDown,
       "os10AlmFanTrayClr": os10AlmFanTrayClr,
       "os10AlmMinorFanTray": os10AlmMinorFanTray,
       "os10AlmMinorFanTrayClr": os10AlmMinorFanTrayClr,
       "os10AlmVariable": os10AlmVariable,
       "os10AlmVarInteger": os10AlmVarInteger,
       "os10AlmVarString": os10AlmVarString,
       "os10AlmVarChassisId": os10AlmVarChassisId,
       "os10AlmVarSlot": os10AlmVarSlot,
       "os10AlmVarPort": os10AlmVarPort}
)

# SNMP MIB module (SUBAGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_2352/SUBAGENT-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:10:27 2025
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

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

subagentxMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 103)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Subagent_ObjectIdentity = ObjectIdentity
subagent = _Subagent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 103, 1)
)
_SubagentManufacturer_Type = DisplayString
_SubagentManufacturer_Object = MibScalar
subagentManufacturer = _SubagentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 103, 1, 1),
    _SubagentManufacturer_Type()
)
subagentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subagentManufacturer.setStatus("current")
_SubagentModelNumber_Type = DisplayString
_SubagentModelNumber_Object = MibScalar
subagentModelNumber = _SubagentModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 103, 1, 2),
    _SubagentModelNumber_Type()
)
subagentModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subagentModelNumber.setStatus("current")


class _SubagentControl_Type(Integer32):
    """Custom type subagentControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SubagentControl_Type.__name__ = "Integer32"
_SubagentControl_Object = MibScalar
subagentControl = _SubagentControl_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 103, 1, 3),
    _SubagentControl_Type()
)
subagentControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subagentControl.setStatus("current")


class _SubagentDoneness_Type(Integer32):
    """Custom type subagentDoneness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SubagentDoneness_Type.__name__ = "Integer32"
_SubagentDoneness_Object = MibScalar
subagentDoneness = _SubagentDoneness_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 103, 1, 4),
    _SubagentDoneness_Type()
)
subagentDoneness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subagentDoneness.setStatus("current")


class _SubagentMaterialType_Type(Integer32):
    """Custom type subagentMaterialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("gypsum", 1),
          ("calcite", 2),
          ("fluorite", 3),
          ("apatite", 4),
          ("topaz", 5),
          ("garnet", 6),
          ("diamond", 7))
    )


_SubagentMaterialType_Type.__name__ = "Integer32"
_SubagentMaterialType_Object = MibScalar
subagentMaterialType = _SubagentMaterialType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 103, 1, 5),
    _SubagentMaterialType_Type()
)
subagentMaterialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subagentMaterialType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUBAGENT-MIB",
    **{"subagentxMIB": subagentxMIB,
       "subagent": subagent,
       "subagentManufacturer": subagentManufacturer,
       "subagentModelNumber": subagentModelNumber,
       "subagentControl": subagentControl,
       "subagentDoneness": subagentDoneness,
       "subagentMaterialType": subagentMaterialType}
)

# SNMP MIB module (GLOBAL-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/delta_20246/GLOBAL-REG.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:25:26 2025
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

globalRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Delta_ObjectIdentity = ObjectIdentity
delta = _Delta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246)
)
_Root_ObjectIdentity = ObjectIdentity
root = _Root_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2)
)
_Reg_ObjectIdentity = ObjectIdentity
reg = _Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 1)
)
_Modules_ObjectIdentity = ObjectIdentity
modules = _Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 1, 1)
)
_ControllerReg_ObjectIdentity = ObjectIdentity
controllerReg = _ControllerReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 1, 2)
)
_ControllerOrionReg_ObjectIdentity = ObjectIdentity
controllerOrionReg = _ControllerOrionReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    controllerOrionReg.setStatus("current")
_Generic_ObjectIdentity = ObjectIdentity
generic = _Generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 2)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3)
)
_Controller_ObjectIdentity = ObjectIdentity
controller = _Controller_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1)
)
_Orion_ObjectIdentity = ObjectIdentity
orion = _Orion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1)
)
_Caps_ObjectIdentity = ObjectIdentity
caps = _Caps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 4)
)
_Regs_ObjectIdentity = ObjectIdentity
regs = _Regs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 5)
)
_Expr_ObjectIdentity = ObjectIdentity
expr = _Expr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GLOBAL-REG",
    **{"delta": delta,
       "root": root,
       "reg": reg,
       "modules": modules,
       "globalRegModule": globalRegModule,
       "controllerReg": controllerReg,
       "controllerOrionReg": controllerOrionReg,
       "generic": generic,
       "products": products,
       "controller": controller,
       "orion": orion,
       "caps": caps,
       "regs": regs,
       "expr": expr}
)

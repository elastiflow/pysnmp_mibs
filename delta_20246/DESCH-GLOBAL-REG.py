# SNMP MIB module (DESCH-GLOBAL-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/delta_20246/DESCH-GLOBAL-REG.mib
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

deschGlobalRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    deschGlobalRegModule.setRevisions(
        ("2004-07-20 20:31",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Delta_ObjectIdentity = ObjectIdentity
delta = _Delta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246)
)
_DeschRoot_ObjectIdentity = ObjectIdentity
deschRoot = _DeschRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2)
)
_DeschReg_ObjectIdentity = ObjectIdentity
deschReg = _DeschReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 1)
)
_DeschModules_ObjectIdentity = ObjectIdentity
deschModules = _DeschModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 1, 1)
)
_ControllerReg_ObjectIdentity = ObjectIdentity
controllerReg = _ControllerReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 1, 2)
)
_ControllerPsc3Reg_ObjectIdentity = ObjectIdentity
controllerPsc3Reg = _ControllerPsc3Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    controllerPsc3Reg.setStatus("current")
_DeschGeneric_ObjectIdentity = ObjectIdentity
deschGeneric = _DeschGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 2)
)
_DeschProducts_ObjectIdentity = ObjectIdentity
deschProducts = _DeschProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3)
)
_DeschController_ObjectIdentity = ObjectIdentity
deschController = _DeschController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1)
)
_DeschPsc3_ObjectIdentity = ObjectIdentity
deschPsc3 = _DeschPsc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1)
)
_DeschCaps_ObjectIdentity = ObjectIdentity
deschCaps = _DeschCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 4)
)
_DeschRegs_ObjectIdentity = ObjectIdentity
deschRegs = _DeschRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 5)
)
_DeschExpr_ObjectIdentity = ObjectIdentity
deschExpr = _DeschExpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DESCH-GLOBAL-REG",
    **{"delta": delta,
       "deschRoot": deschRoot,
       "deschReg": deschReg,
       "deschModules": deschModules,
       "deschGlobalRegModule": deschGlobalRegModule,
       "controllerReg": controllerReg,
       "controllerPsc3Reg": controllerPsc3Reg,
       "deschGeneric": deschGeneric,
       "deschProducts": deschProducts,
       "deschController": deschController,
       "deschPsc3": deschPsc3,
       "deschCaps": deschCaps,
       "deschRegs": deschRegs,
       "deschExpr": deschExpr}
)

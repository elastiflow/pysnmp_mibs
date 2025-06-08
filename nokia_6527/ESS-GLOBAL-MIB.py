# SNMP MIB module (ESS-GLOBAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/ESS-GLOBAL-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:45:25 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(timetraModules,
 timetraProducts,
 timetraReg) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraModules",
    "timetraProducts",
    "timetraReg")


# MODULE-IDENTITY

essGlobalMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    essGlobalMIBModule.setRevisions(
        ("2003-12-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TimetraESSMIBModules_ObjectIdentity = ObjectIdentity
timetraESSMIBModules = _TimetraESSMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 4)
)
_TimetraServiceSwitches_ObjectIdentity = ObjectIdentity
timetraServiceSwitches = _TimetraServiceSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 6)
)
_TmnxModelESS1Reg_ObjectIdentity = ObjectIdentity
tmnxModelESS1Reg = _TmnxModelESS1Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxModelESS1Reg.setStatus("current")
_TmnxModelESS4Reg_ObjectIdentity = ObjectIdentity
tmnxModelESS4Reg = _TmnxModelESS4Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 6, 2)
)
if mibBuilder.loadTexts:
    tmnxModelESS4Reg.setStatus("current")
_TmnxModelESS7Reg_ObjectIdentity = ObjectIdentity
tmnxModelESS7Reg = _TmnxModelESS7Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 6, 3)
)
if mibBuilder.loadTexts:
    tmnxModelESS7Reg.setStatus("current")
_TmnxModelESS12Reg_ObjectIdentity = ObjectIdentity
tmnxModelESS12Reg = _TmnxModelESS12Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 6, 4)
)
if mibBuilder.loadTexts:
    tmnxModelESS12Reg.setStatus("current")
_TmnxESSMIB_ObjectIdentity = ObjectIdentity
tmnxESSMIB = _TmnxESSMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 2)
)
_TmnxESSConfs_ObjectIdentity = ObjectIdentity
tmnxESSConfs = _TmnxESSConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 2, 1)
)
_TmnxESSObjs_ObjectIdentity = ObjectIdentity
tmnxESSObjs = _TmnxESSObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 2, 2)
)
_TmnxESSNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxESSNotifyPrefix = _TmnxESSNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 2, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ESS-GLOBAL-MIB",
    **{"timetraESSMIBModules": timetraESSMIBModules,
       "essGlobalMIBModule": essGlobalMIBModule,
       "timetraServiceSwitches": timetraServiceSwitches,
       "tmnxModelESS1Reg": tmnxModelESS1Reg,
       "tmnxModelESS4Reg": tmnxModelESS4Reg,
       "tmnxModelESS7Reg": tmnxModelESS7Reg,
       "tmnxModelESS12Reg": tmnxModelESS12Reg,
       "tmnxESSMIB": tmnxESSMIB,
       "tmnxESSConfs": tmnxESSConfs,
       "tmnxESSObjs": tmnxESSObjs,
       "tmnxESSNotifyPrefix": tmnxESSNotifyPrefix}
)

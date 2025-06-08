# SNMP MIB module (FORTINET-FORTIMANAGER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/fortinet_12356/FORTINET-FORTIMANAGER-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:36:32 2025
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

(fnSysSerial,
 fortinet) = mibBuilder.importSymbols(
    "FORTINET-CORE-MIB",
    "fnSysSerial",
    "fortinet")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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


# MODULE-IDENTITY

fnFortiManagerMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103)
)
if mibBuilder.loadTexts:
    fnFortiManagerMib.setRevisions(
        ("2008-07-18 00:00",
         "2008-06-26 00:00",
         "2008-06-16 00:00",
         "2008-06-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FmTraps_ObjectIdentity = ObjectIdentity
fmTraps = _FmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0)
)
_FmTrapPrefix_ObjectIdentity = ObjectIdentity
fmTrapPrefix = _FmTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 0)
)
_FmTrapObject_ObjectIdentity = ObjectIdentity
fmTrapObject = _FmTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 1)
)
_FmModel_ObjectIdentity = ObjectIdentity
fmModel = _FmModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1)
)
_Fmg100_ObjectIdentity = ObjectIdentity
fmg100 = _Fmg100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 1000)
)
_Fmg400_ObjectIdentity = ObjectIdentity
fmg400 = _Fmg400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 4000)
)
_Fmg400A_ObjectIdentity = ObjectIdentity
fmg400A = _Fmg400A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 4001)
)
_Fmg2000XL_ObjectIdentity = ObjectIdentity
fmg2000XL = _Fmg2000XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 20000)
)
_Fmg3000_ObjectIdentity = ObjectIdentity
fmg3000 = _Fmg3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 30000)
)
_Fmg3000B_ObjectIdentity = ObjectIdentity
fmg3000B = _Fmg3000B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 30002)
)
_FmMIBConformance_ObjectIdentity = ObjectIdentity
fmMIBConformance = _FmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 10)
)

# Managed Objects groups


# Notification objects

fmTrapHASwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 0, 401)
)
fmTrapHASwitch.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fmTrapHASwitch.setStatus(
        "current"
    )


# Notifications groups

fmTrapsComplianceGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 103, 10, 1)
)
fmTrapsComplianceGroup.setObjects(
    ("FORTINET-FORTIMANAGER-MIB", "fmTrapHASwitch")
)
if mibBuilder.loadTexts:
    fmTrapsComplianceGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 103, 10, 100)
)
fmMIBCompliance.setObjects(
    ("FORTINET-FORTIMANAGER-MIB", "fmTrapsComplianceGroup")
)
if mibBuilder.loadTexts:
    fmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-FORTIMANAGER-MIB",
    **{"fnFortiManagerMib": fnFortiManagerMib,
       "fmTraps": fmTraps,
       "fmTrapPrefix": fmTrapPrefix,
       "fmTrapHASwitch": fmTrapHASwitch,
       "fmTrapObject": fmTrapObject,
       "fmModel": fmModel,
       "fmg100": fmg100,
       "fmg400": fmg400,
       "fmg400A": fmg400A,
       "fmg2000XL": fmg2000XL,
       "fmg3000": fmg3000,
       "fmg3000B": fmg3000B,
       "fmMIBConformance": fmMIBConformance,
       "fmTrapsComplianceGroup": fmTrapsComplianceGroup,
       "fmMIBCompliance": fmMIBCompliance}
)

# SNMP MIB module (CNM-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/s30labs_34225/CNM-TRAPS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:09:28 2025
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S30labs_ObjectIdentity = ObjectIdentity
s30labs = _S30labs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34225)
)
_CnmTraps_ObjectIdentity = ObjectIdentity
cnmTraps = _CnmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34225, 0)
)
_CnmTrapsBase_ObjectIdentity = ObjectIdentity
cnmTrapsBase = _CnmTrapsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34225, 0, 1)
)
_CnmTrapsData_ObjectIdentity = ObjectIdentity
cnmTrapsData = _CnmTrapsData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34225, 101)
)
_CnmTrapCode_Type = Integer32
_CnmTrapCode_Object = MibScalar
cnmTrapCode = _CnmTrapCode_Object(
    (1, 3, 6, 1, 4, 1, 34225, 101, 1),
    _CnmTrapCode_Type()
)
cnmTrapCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnmTrapCode.setStatus("mandatory")
_CnmTrapMsg_Type = DisplayString
_CnmTrapMsg_Object = MibScalar
cnmTrapMsg = _CnmTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 34225, 101, 2),
    _CnmTrapMsg_Type()
)
cnmTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnmTrapMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cnmAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 34225, 0, 1, 0, 1)
)
cnmAlarmSet.setObjects(
      *(("CNM-TRAPS-MIB", "cnmTrapCode"),
        ("CNM-TRAPS-MIB", "cnmTrapMsg"))
)
if mibBuilder.loadTexts:
    cnmAlarmSet.setStatus(
        ""
    )

cnmAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 34225, 0, 1, 0, 2)
)
cnmAlarmClear.setObjects(
      *(("CNM-TRAPS-MIB", "cnmTrapCode"),
        ("CNM-TRAPS-MIB", "cnmTrapMsg"))
)
if mibBuilder.loadTexts:
    cnmAlarmClear.setStatus(
        ""
    )

cnmInfoMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 34225, 0, 1, 0, 3)
)
cnmInfoMsg.setObjects(
      *(("CNM-TRAPS-MIB", "cnmTrapCode"),
        ("CNM-TRAPS-MIB", "cnmTrapMsg"))
)
if mibBuilder.loadTexts:
    cnmInfoMsg.setStatus(
        ""
    )

cnmTrapNoLinkSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 34225, 0, 1, 0, 100)
)
cnmTrapNoLinkSet.setObjects(
      *(("CNM-TRAPS-MIB", "cnmTrapCode"),
        ("CNM-TRAPS-MIB", "cnmTrapMsg"))
)
if mibBuilder.loadTexts:
    cnmTrapNoLinkSet.setStatus(
        ""
    )

cnmTrapIFDownfSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 34225, 0, 1, 0, 102)
)
cnmTrapIFDownfSet.setObjects(
      *(("CNM-TRAPS-MIB", "cnmTrapCode"),
        ("CNM-TRAPS-MIB", "cnmTrapMsg"))
)
if mibBuilder.loadTexts:
    cnmTrapIFDownfSet.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CNM-TRAPS-MIB",
    **{"DisplayString": DisplayString,
       "s30labs": s30labs,
       "cnmTraps": cnmTraps,
       "cnmTrapsBase": cnmTrapsBase,
       "cnmAlarmSet": cnmAlarmSet,
       "cnmAlarmClear": cnmAlarmClear,
       "cnmInfoMsg": cnmInfoMsg,
       "cnmTrapNoLinkSet": cnmTrapNoLinkSet,
       "cnmTrapIFDownfSet": cnmTrapIFDownfSet,
       "cnmTrapsData": cnmTrapsData,
       "cnmTrapCode": cnmTrapCode,
       "cnmTrapMsg": cnmTrapMsg}
)

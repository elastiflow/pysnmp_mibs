# SNMP MIB module (ALU-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/ALU-SYSTEM-MIB.mib
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

(aluSARConfs,
 aluSARMIBModules,
 aluSARNotifyPrefix,
 aluSARObjs) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARConfs",
    "aluSARMIBModules",
    "aluSARNotifyPrefix",
    "aluSARObjs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(TmnxAdminState,) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TmnxAdminState")


# MODULE-IDENTITY

aluSystemMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 13)
)
if mibBuilder.loadTexts:
    aluSystemMIBModule.setRevisions(
        ("1911-06-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluTod1PpsMessageType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("cm", 1),
          ("ct", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AluSystemMIBConformance_ObjectIdentity = ObjectIdentity
aluSystemMIBConformance = _AluSystemMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13)
)
_AluSystemMIBCompliances_ObjectIdentity = ObjectIdentity
aluSystemMIBCompliances = _AluSystemMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 1)
)
_AluSystemMIBGroups_ObjectIdentity = ObjectIdentity
aluSystemMIBGroups = _AluSystemMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 2)
)
_AluSystemObjs_ObjectIdentity = ObjectIdentity
aluSystemObjs = _AluSystemObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13)
)
_AluTod1PpsInfo_ObjectIdentity = ObjectIdentity
aluTod1PpsInfo = _AluTod1PpsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 1)
)


class _AluTod1PpsMessageType_Type(AluTod1PpsMessageType):
    """Custom type aluTod1PpsMessageType based on AluTod1PpsMessageType"""
    defaultValue = 0


_AluTod1PpsMessageType_Type.__name__ = "AluTod1PpsMessageType"
_AluTod1PpsMessageType_Object = MibScalar
aluTod1PpsMessageType = _AluTod1PpsMessageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 1, 1),
    _AluTod1PpsMessageType_Type()
)
aluTod1PpsMessageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluTod1PpsMessageType.setStatus("current")


class _AluTod1PpsOutput_Type(TmnxAdminState):
    """Custom type aluTod1PpsOutput based on TmnxAdminState"""
    defaultValue = 3


_AluTod1PpsOutput_Type.__name__ = "TmnxAdminState"
_AluTod1PpsOutput_Object = MibScalar
aluTod1PpsOutput = _AluTod1PpsOutput_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 1, 2),
    _AluTod1PpsOutput_Type()
)
aluTod1PpsOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluTod1PpsOutput.setStatus("current")


class _AluTod1PpsInput_Type(TmnxAdminState):
    """Custom type aluTod1PpsInput based on TmnxAdminState"""
    defaultValue = 3


_AluTod1PpsInput_Type.__name__ = "TmnxAdminState"
_AluTod1PpsInput_Object = MibScalar
aluTod1PpsInput = _AluTod1PpsInput_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 1, 3),
    _AluTod1PpsInput_Type()
)
aluTod1PpsInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluTod1PpsInput.setStatus("current")
_AluSystemNotifyPrefix_ObjectIdentity = ObjectIdentity
aluSystemNotifyPrefix = _AluSystemNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 9)
)

# Managed Objects groups

aluTod1PpsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 2, 1)
)
aluTod1PpsGroup.setObjects(
      *(("ALU-SYSTEM-MIB", "aluTod1PpsMessageType"),
        ("ALU-SYSTEM-MIB", "aluTod1PpsOutput"),
        ("ALU-SYSTEM-MIB", "aluTod1PpsInput"))
)
if mibBuilder.loadTexts:
    aluTod1PpsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aluSystemMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 1, 1)
)
aluSystemMIBCompliance.setObjects(
    ("ALU-SYSTEM-MIB", "aluTod1PpsGroup")
)
if mibBuilder.loadTexts:
    aluSystemMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-SYSTEM-MIB",
    **{"AluTod1PpsMessageType": AluTod1PpsMessageType,
       "aluSystemMIBModule": aluSystemMIBModule,
       "aluSystemMIBConformance": aluSystemMIBConformance,
       "aluSystemMIBCompliances": aluSystemMIBCompliances,
       "aluSystemMIBCompliance": aluSystemMIBCompliance,
       "aluSystemMIBGroups": aluSystemMIBGroups,
       "aluTod1PpsGroup": aluTod1PpsGroup,
       "aluSystemObjs": aluSystemObjs,
       "aluTod1PpsInfo": aluTod1PpsInfo,
       "aluTod1PpsMessageType": aluTod1PpsMessageType,
       "aluTod1PpsOutput": aluTod1PpsOutput,
       "aluTod1PpsInput": aluTod1PpsInput,
       "aluSystemNotifyPrefix": aluSystemNotifyPrefix}
)

# SNMP MIB module (CEM-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-SMI.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:21 2025
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
 iso,
 mib_2,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "snmpModules")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

catena = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnProducts_ObjectIdentity = ObjectIdentity
cnProducts = _CnProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1)
)
_CnCN1000_ObjectIdentity = ObjectIdentity
cnCN1000 = _CnCN1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2)
)
_CnONU_ObjectIdentity = ObjectIdentity
cnONU = _CnONU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 3)
)
_CnSystemGroup_ObjectIdentity = ObjectIdentity
cnSystemGroup = _CnSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 2)
)
_CnDsx1Group_ObjectIdentity = ObjectIdentity
cnDsx1Group = _CnDsx1Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 3)
)
_CnAtmMIB_ObjectIdentity = ObjectIdentity
cnAtmMIB = _CnAtmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 4)
)
_CnCardRedundancyModule_ObjectIdentity = ObjectIdentity
cnCardRedundancyModule = _CnCardRedundancyModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 6)
)
_CnCommonProcessorModule_ObjectIdentity = ObjectIdentity
cnCommonProcessorModule = _CnCommonProcessorModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 7)
)
_CnCN1000HardwareModule_ObjectIdentity = ObjectIdentity
cnCN1000HardwareModule = _CnCN1000HardwareModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 8)
)
_CemCN1000ReferenceTiming_ObjectIdentity = ObjectIdentity
cemCN1000ReferenceTiming = _CemCN1000ReferenceTiming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 9)
)
_CnDiagnostics_ObjectIdentity = ObjectIdentity
cnDiagnostics = _CnDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 10)
)
_CnAlarmsModule_ObjectIdentity = ObjectIdentity
cnAlarmsModule = _CnAlarmsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 11)
)
_CnInterfaces_ObjectIdentity = ObjectIdentity
cnInterfaces = _CnInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 12)
)
_CnTextualConventions_ObjectIdentity = ObjectIdentity
cnTextualConventions = _CnTextualConventions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 13)
)
_CnApsMIB_ObjectIdentity = ObjectIdentity
cnApsMIB = _CnApsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 14)
)
_Cnx5ringModule_ObjectIdentity = ObjectIdentity
cnx5ringModule = _Cnx5ringModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 15)
)
_Cn1000SubtendingModule_ObjectIdentity = ObjectIdentity
cn1000SubtendingModule = _Cn1000SubtendingModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 16)
)
_CnTcaModule_ObjectIdentity = ObjectIdentity
cnTcaModule = _CnTcaModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 17)
)
_CnSonetModule_ObjectIdentity = ObjectIdentity
cnSonetModule = _CnSonetModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 18)
)
_CnDs3Module_ObjectIdentity = ObjectIdentity
cnDs3Module = _CnDs3Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 19)
)
_CemIpoaModule_ObjectIdentity = ObjectIdentity
cemIpoaModule = _CemIpoaModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 20)
)
_CemEtherIfModule_ObjectIdentity = ObjectIdentity
cemEtherIfModule = _CemEtherIfModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 21)
)
_CemDiagTestModule_ObjectIdentity = ObjectIdentity
cemDiagTestModule = _CemDiagTestModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 22)
)
_CemEquipmentModule_ObjectIdentity = ObjectIdentity
cemEquipmentModule = _CemEquipmentModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 23)
)
_CemIpIfModule_ObjectIdentity = ObjectIdentity
cemIpIfModule = _CemIpIfModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 24)
)
_CnATMServiceConnectionModule_ObjectIdentity = ObjectIdentity
cnATMServiceConnectionModule = _CnATMServiceConnectionModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 25)
)
_CnCN1000UserModule_ObjectIdentity = ObjectIdentity
cnCN1000UserModule = _CnCN1000UserModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 26)
)
_CnCN1000RingModule_ObjectIdentity = ObjectIdentity
cnCN1000RingModule = _CnCN1000RingModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 27)
)
_CnCentralizedManagementModule_ObjectIdentity = ObjectIdentity
cnCentralizedManagementModule = _CnCentralizedManagementModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 28)
)
_CnShdslMIB_ObjectIdentity = ObjectIdentity
cnShdslMIB = _CnShdslMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 30)
)
_CnErrorMIB_ObjectIdentity = ObjectIdentity
cnErrorMIB = _CnErrorMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 31)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-SMI",
    **{"catena": catena,
       "cnProducts": cnProducts,
       "cnCN1000": cnCN1000,
       "cnONU": cnONU,
       "cnSystemGroup": cnSystemGroup,
       "cnDsx1Group": cnDsx1Group,
       "cnAtmMIB": cnAtmMIB,
       "cnCardRedundancyModule": cnCardRedundancyModule,
       "cnCommonProcessorModule": cnCommonProcessorModule,
       "cnCN1000HardwareModule": cnCN1000HardwareModule,
       "cemCN1000ReferenceTiming": cemCN1000ReferenceTiming,
       "cnDiagnostics": cnDiagnostics,
       "cnAlarmsModule": cnAlarmsModule,
       "cnInterfaces": cnInterfaces,
       "cnTextualConventions": cnTextualConventions,
       "cnApsMIB": cnApsMIB,
       "cnx5ringModule": cnx5ringModule,
       "cn1000SubtendingModule": cn1000SubtendingModule,
       "cnTcaModule": cnTcaModule,
       "cnSonetModule": cnSonetModule,
       "cnDs3Module": cnDs3Module,
       "cemIpoaModule": cemIpoaModule,
       "cemEtherIfModule": cemEtherIfModule,
       "cemDiagTestModule": cemDiagTestModule,
       "cemEquipmentModule": cemEquipmentModule,
       "cemIpIfModule": cemIpIfModule,
       "cnATMServiceConnectionModule": cnATMServiceConnectionModule,
       "cnCN1000UserModule": cnCN1000UserModule,
       "cnCN1000RingModule": cnCN1000RingModule,
       "cnCentralizedManagementModule": cnCentralizedManagementModule,
       "cnShdslMIB": cnShdslMIB,
       "cnErrorMIB": cnErrorMIB}
)
